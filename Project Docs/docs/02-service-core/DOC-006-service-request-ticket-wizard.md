# DOC-006
# Service Request (Ticket Wizard)

**Status:** Approved

---

# Purpose

Service Request نقطه شروع تمام فرآیندهای سرویس است.

هر درخواست مشتری، بدون توجه به نوع آن، یک Ticket ایجاد می‌کند.

سیستم در این مرحله هیچ تصمیم فنی یا اجرایی نمی‌گیرد.

بررسی، برنامه‌ریزی و تصمیم نهایی توسط Service Manager انجام می‌شود.

---

# Business Rules

## BR-001

هر درخواست مشتری یک Ticket ایجاد می‌کند.

نوع درخواست در مرحله ثبت توسط مشتری تعیین نمی‌شود.

---

## BR-002

ثبت Ticket برای همه مجاز است.

- Guest
- Registered Customer

---

## BR-003

داشتن Contract برای ثبت Ticket الزامی نیست.

Contract فقط شرایط ارائه سرویس را مشخص می‌کند.

---

## BR-004

پس از ثبت Ticket، Service Manager مسئول بررسی و تصمیم‌گیری است.

نمونه تصمیم‌ها:

- Remote Support
- Onsite Visit
- Preventive Maintenance
- Inspection
- Quotation
- Spare Parts
- سایر اقدامات

---

# Ticket Wizard

هدف Wizard دریافت حداقل اطلاعات لازم از مشتری است.

سیستم تا حد امکان اطلاعات موجود را از پایگاه داده استخراج می‌کند.

---

# Guest Workflow

اطلاعات پیشنهادی:

- Name
- Company
- Mobile
- Email (Optional)
- City
- Device Brand
- Device Model
- Serial Number (Optional)
- Description

هدف:

- ثبت درخواست
- شناسایی دستگاه
- ایجاد Lead
- دعوت به ایجاد حساب کاربری

---

# Customer Workflow

پس از Login

سیستم اطلاعات مشتری را بارگذاری می‌کند.

هیچ گزینه‌ای به صورت پیش‌فرض انتخاب نمی‌شود.

کاربر از لیست موجود انتخاب می‌کند.

---

# Asset Selection

مبنای ثبت Ticket انتخاب Asset است.

Customer ابتدا دستگاه مورد نظر را انتخاب می‌کند.

نمونه:

- Kodak Magnus
- Kodak RIP
- Processor

در صورت وجود دستگاه‌های مشابه، شماره سریال نمایش داده می‌شود.

مثال:

Kodak RIP

SN : RIP001

Kodak RIP

SN : RIP002

---

# Automatic Detection

پس از انتخاب Asset، سیستم به صورت خودکار اطلاعات زیر را پیدا می‌کند.

- Customer
- Site
- Service Package
- Contract
- Service Policy (SLA)
- Warranty (در صورت وجود)
- Previous Service History

مشتری این اطلاعات را وارد نمی‌کند.

---

# Smart Wizard

اصل طراحی:

Never ask if the system already knows.

اگر فقط یک گزینه وجود داشته باشد، مستقیماً استفاده می‌شود.

اگر چند گزینه وجود داشته باشد، لیست نمایش داده می‌شود.

---

# Description

مشتری فقط نیاز یا مشکل خود را توضیح می‌دهد.

سیستم تلاش نمی‌کند از مشتری عیب‌یابی انجام دهد.

تشخیص فنی بر عهده کارشناسان شرکت است.

---

# Ticket Confirmation

پس از ثبت Ticket، پیام مناسب نمایش داده می‌شود.

---

## Guest

درخواست شما ثبت شد.

کارشناسان ما اطلاعات را بررسی کرده و با شما تماس خواهند گرفت.

در صورت ایجاد حساب کاربری، امکان مشاهده وضعیت درخواست‌ها و سوابق سرویس فراهم خواهد شد.

---

## Customer بدون Contract

درخواست شما ثبت شد.

پس از بررسی، شرایط ارائه سرویس و هزینه احتمالی به شما اعلام خواهد شد.

---

## Customer دارای Contract

درخواست شما ثبت شد.

حداکثر زمان پاسخگویی اولیه مطابق Service Policy قرارداد شما خواهد بود.

---

# Ticket Ownership

هر Ticket فقط به یک Asset تعلق دارد.

تمام اطلاعات مرتبط از روی همان Asset استخراج می‌شود.

Asset مرکز اصلی ارتباط بین موجودیت‌های سیستم است.

---

# Odoo Mapping

| Business Entity | Odoo |
|-----------------|------|
| Ticket | helpdesk.ticket |
| Customer | res.partner |
| Asset | maintenance.equipment |
| Contract | OCA Contract |
| SLA | Custom Service Policy |
| Activities | mail.activity |
| Chatter | mail.thread |

---

# Design Principles

- One Request = One Ticket
- One Ticket = One Asset
- Customer describes the need
- Service Manager decides the execution
- Minimum Questions
- Maximum Automatic Detection
- No Technical Diagnosis by Customer
- Odoo First
- OCA First
- Custom Last

---

**Status:** Approved
