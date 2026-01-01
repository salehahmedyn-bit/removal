import asyncio
import sys
import os

# إضافة المسار الحالي ليتعرف البايثون على المجلد كمكتبة محلياً
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ezremove import EzRemoveClient, EzRemoveError

async def main():
    client = EzRemoveClient()
    
    # قائمة الصور (يمكنك وضع مئات المسارات هنا)
    # ملاحظة: استبدل هذه الأسماء بملفات حقيقية موجودة لديك للتجربة
    images = [
        "ke5a4xtzhnrmr0cvf5d9nnts2w_result_0.png",
        # "test2.png", 
        # "test3.png"
    ]
    
    print(f"🔥 بدء المعالجة الجماعية لـ {len(images)} صور...")

    # تشغيل المعالجة المتوازية (5 صور في نفس اللحظة)
    results = await client.remove_background_bulk(images, max_concurrent=5)
    
    print("\n" + "="*30)
    print("📊 النتائج النهائية:")
    print("="*30)
    
    for res in results:
        if res['status'] == 'success':
            print(f"✅ ناجح: {res['file']}")
            print(f"🔗 الرابط: {res['url']}\n")
        else:
            print(f"❌ فشل: {res['file']}")
            print(f"⚠️  السبب: {res['error']}\n")

if __name__ == "__main__":
    if not os.path.exists("ke5a4xtzhnrmr0cvf5d9nnts2w_result_0.png"):
        print("⚠️  تنبيه: لم يتم العثور على صورة التجربة الافتراضية.")
    
    asyncio.run(main())
