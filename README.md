# CineMagic (Django)

مشروع Django تدريبي لعرض/إدارة أفلام.

## تشغيل سريع (Windows / PowerShell)

1) تفعيل البيئة الافتراضية:

```powershell
.\.venv\Scripts\Activate.ps1
```

إذا لم تكن موجودة:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) تثبيت Django (الإصدار المستخدم في المشروع: `6.0.3`):

```powershell
pip install django==6.0.3
```

3) تشغيل الترحيلات (migrations) ثم تشغيل السيرفر:

```powershell
python manage.py migrate
python manage.py runserver
```

4) افتح:

- `http://127.0.0.1:8000/`

## الروابط (Routes)

- `/` الصفحة الرئيسية
- `/info/` معلومات
- `/film/<titre>/` مثال: `/film/Inception/`
- `/stats/` إحصائيات

## بنية المشروع

- `manage.py` أوامر Django
- `cinemagic_project/` إعدادات المشروع + `urls.py`
- `cataloge/` التطبيق (views / models / templates / static)
- `db.sqlite3` قاعدة البيانات (SQLite)

## ملاحظة

لوحة الإدارة (Admin) غير مفعّلة في `cinemagic_project/urls.py` حاليًا (لا يوجد مسار `admin/`).
