import asyncio
import aiohttp
import os
from .exceptions import APIError, TimeoutError, FileError
from .models import JobResult

class EzRemoveClient:
    BASE_URL = "https://api.ezremove.ai/api/ez-remove/background-remove"
    
    def __init__(self, product_serial="6659e980c010f1f4e450e36d0955eb8d"):
        self.headers = {
            'product-serial': product_serial,
            'origin': 'https://ezremove.ai',
            'referer': 'https://ezremove.ai/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36'
        }

    async def remove_background(self, image_path: str, poll_interval: int = 3, timeout: int = 90) -> str:
        """معالجة صورة واحدة: رفع -> انتظار -> رابط"""
        if not os.path.exists(image_path):
            raise FileError(f"File not found: {image_path}")

        async with aiohttp.ClientSession(headers=self.headers) as session:
            job_id = await self._upload_image(session, image_path)
            return await self._wait_for_result(session, job_id, poll_interval, timeout)

    async def remove_background_bulk(self, image_paths: list, max_concurrent: int = 5):
        """معالجة مئات الصور بالتوازي مع التحكم في عدد المهام المتزامنة"""
        semaphore = asyncio.Semaphore(max_concurrent)

        async def sem_task(img_path):
            async with semaphore:
                try:
                    url = await self.remove_background(img_path)
                    return {"file": img_path, "status": "success", "url": url}
                except Exception as e:
                    return {"file": img_path, "status": "error", "error": str(e)}

        tasks = [sem_task(path) for path in image_paths]
        return await asyncio.gather(*tasks)

    async def _upload_image(self, session, image_path):
        data = aiohttp.FormData()
        data.add_field('image_file', open(image_path, 'rb'), 
                       filename=os.path.basename(image_path),
                       content_type='image/png')
        data.add_field('turnstile_token', '')

        async with session.post(f"{self.BASE_URL}/create-job-v2", data=data) as resp:
            if resp.status != 200:
                raise APIError(f"HTTP Error: {resp.status}")
            
            res = await resp.json()
            if res.get('code') == 100000:
                return res['result']['job_id']
            raise APIError(f"API Error: {res.get('message', {}).get('en', 'Unknown error')}")

    async def _wait_for_result(self, session, job_id, interval, timeout):
        elapsed = 0
        while elapsed < timeout:
            async with session.get(f"{self.BASE_URL}/get-job/{job_id}") as resp:
                res = await resp.json()
                if res.get('code') == 100000:
                    return res['result']['output'][0]
                elif res.get('code') == 300001:
                    await asyncio.sleep(interval)
                    elapsed += interval
                else:
                    raise APIError(f"Polling error: {res}")
        raise TimeoutError(f"Process exceeded {timeout} seconds")
