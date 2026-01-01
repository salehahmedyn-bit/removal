# Removal SDK 🚀
مكتبة بايثون احترافية لإزالة خلفيات الصور برمجياً عبر API.

## التثبيت
```bash
pip install git+https://github.com/salehahmedyn-bit/removal.git
```

## مثال سريع للاستخدام
```python
import asyncio
from ezremove import EzRemoveClient

async def main():
    client = EzRemoveClient(api_key="YOUR_API_KEY")
    print("SDK Initialized Successfully!")

if __name__ == "__main__":
    asyncio.run(main())
```
