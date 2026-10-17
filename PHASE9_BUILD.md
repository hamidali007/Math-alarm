# المرحلة التاسعة — مسار بناء أندرويد آلي

تمت إضافة سير عمل GitHub Actions لإنشاء مشروع أندرويد من مصدر Flutter وتشغيل تحليل Dart ثم بناء APK تجريبي. **لم يتم تشغيل سير العمل هنا**؛ نجاح البناء غير مؤكد.

## طريقة الحصول على APK
1. ارفع محتويات مجلد `almohaseb` إلى مستودع GitHub خاص (لا ترفع بيانات عملاء أو مفاتيح سرية).
2. افتح Actions ثم Android debug build واضغط Run workflow.
3. إذا نجحت جميع الخطوات، نزّل artifact باسم `almohaseb-debug-apk`، وفيه `app-debug.apk`.
4. إن فشل تحليل Flutter، راجع السجل وأصلح أخطاء Dart ثم أعد التشغيل.

**تحذير:** APK التجريبي غير صالح للاستخدام الإنتاجي. لا توجد مصادقة آمنة ولا مزامنة سحابية حقيقية، ولا ضمان لدقة الحسابات أو امتثال الفواتير. بناء APK لا يعني اكتمال البرنامج.

## تشغيل محلي
```
flutter create --platforms=android --project-name almohaseb .
flutter pub get
flutter analyze
flutter build apk --debug
```

## فحص ملفات المصدر
يوجد `tools/check_project.py` لفحص بنية الملفات الأساسية محليًا دون Flutter.
