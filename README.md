# EzRemove SDK 🚀

مكتبة بايثون متطورة وغير متزامنة (Asynchronous) لإزالة خلفية الصور باستخدام ذكاء EzRemove الاصطناعي.

## 📥 التثبيت
يمكنك تثبيت المكتبة مباشرة من GitHub:
```bash
pip install git+[https://github.com/salehahmedyn-bit/removal.git](https://github.com/salehahmedyn-bit/removal.git)

🛠️ مثال لاستخدام المكتبة
import asyncio
from ezremove import EzRemoveClient

async def main():
    # إنشاء العميل (تأكد من تعديل الكلاس ليكون المفتاح اختيارياً)
    client = EzRemoveClient()
    
    # مثال لإزالة خلفية صورة
    # url = await client.remove_background("image.png")
        print(f"الرابط: {url}")

if __name__ == "__main__":
    asyncio.run(main())

