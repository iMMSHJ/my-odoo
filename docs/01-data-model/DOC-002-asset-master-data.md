# DOC-002
# Asset Master Data

**Version:** 0.1

**Status:** Approved

---

# Purpose

Asset فقط برای شناسایی دستگاه و نگهداری تاریخچه سرویس استفاده می‌شود.

اطلاعات فنی، تنظیمات و مشخصات تخصصی دستگاه در این موجودیت نگهداری نمی‌شوند.

---

# Required Fields

| Field | Required | Description |
|--------|----------|-------------|
| Serial Number | Yes | شماره سریال یکتا |
| Brand | Yes | سازنده دستگاه |
| Model | Yes | مدل دستگاه |
| Manufacture Date | Yes | سال یا ماه/سال ساخت |

---

# Business Rules

### BR-001

شماره سریال در کل سیستم یکتا است.

---

### BR-002

Brand از لیست از پیش تعریف شده انتخاب می‌شود.

---

### BR-003

Model وابسته به Brand است.

مثال:

Kodak

- Magnus
- Trendsetter
- Achieve

Heidelberg

- Suprasetter 106
- Suprasetter 75
- SM74

---

### BR-004

Brand و Model فقط توسط کاربران داخلی مدیریت می‌شوند.

Customer اجازه ایجاد یا ویرایش آن‌ها را ندارد.

---

### BR-005

تمام دستگاه‌ها قابل ثبت درخواست سرویس هستند.

داشتن یا نداشتن قرارداد مانع ثبت درخواست نیست.

---

### BR-006

Asset فقط اطلاعات لازم برای شناسایی دستگاه را نگهداری می‌کند.

اطلاعات سرویس، قرارداد، مالکیت و محل نصب در موجودیت‌های مرتبط مدیریت می‌شوند.

---

# Odoo Mapping

| Business Entity | Odoo Model | Status |
|-----------------|------------|--------|
| Brand | Product Attribute / Custom Dictionary | بررسی |
| Model | Product Variant / Custom Dictionary | بررسی |
| Asset | maintenance.equipment | استفاده با توسعه سبک |

---

# Notes

- طراحی Asset باید تا حد امکان از مدل‌های استاندارد Odoo استفاده کند.
- از ایجاد جدول جدید فقط در صورت نبود راهکار مناسب در Odoo یا OCA استفاده می‌شود.
