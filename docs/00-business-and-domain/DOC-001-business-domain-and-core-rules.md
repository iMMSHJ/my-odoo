# DOC-001
# Business Domain & Core Rules

**Version:** 1.0

**Status:** Approved

---

# Purpose

تعریف ساختار اصلی کسب‌وکار و قوانین پایه سیستم قبل از طراحی دیتابیس و توسعه.

این سند مرجع اصلی تمام مستندات بعدی است.

---

# Business Domain

```text
Customer
│
├── Head Office (Optional)
│
├── Sites (0..N)
│
│      ├── Contacts
│      ├── Service Packages
│      └── Assets
│
└── Contracts
```

---

# Customer Types

سیستم از دو نوع مشتری پشتیبانی می‌کند.

- Company (حقوقی)
- Individual (حقیقی)

---

# Customer Structure

هر Customer می‌تواند:

- چند Site داشته باشد.
- چند Contact داشته باشد.
- چند Contract داشته باشد.
- چند Service Package داشته باشد.

---

# Site

Site محل ارائه سرویس است.

نمونه:

- کارخانه
- دفتر
- شعبه
- انبار
- منزل مشتری

Site فقط یک آدرس نیست.

بر موارد زیر اثر دارد:

- هزینه اعزام
- زمان اعزام
- برنامه سرویس
- SLA عملیاتی

---

# Contacts

هر Contact می‌تواند به چند Site متصل باشد.

هر Contact می‌تواند چند Role مشتری داشته باشد.

---

# Customer Roles

Roleهای مشتری محدود و ثابت هستند.

- Manager
- Service (Technical Contact)
- Operator
- Accountant

هر Contact می‌تواند بیش از یک Role داشته باشد.

مثال:

Manager + Accountant

یا

Operator + Service

---

# Internal Roles

Roleهای کاربران داخلی کاملاً مستقل از مشتری هستند.

نمونه:

- Super Admin
- Service Manager
- Technician
- Warehouse
- Accountant
- Sales

---

# Security Rules

Customer هیچ‌وقت Role داخلی دریافت نمی‌کند.

Internal User هیچ‌وقت Role مشتری دریافت نمی‌کند.

هر User می‌تواند چند Role داخلی داشته باشد.

هر Contact مشتری نیز می‌تواند چند Role مشتری داشته باشد.

---

# Asset Ownership

مالک دستگاه Customer است.

Contact مالک دستگاه نیست.

---

# Asset History

جابجایی دستگاه بین مشتریان مجاز است.

مالکیت تغییر می‌کند.

تاریخچه سرویس حذف نمی‌شود.

Customer جدید فقط تاریخچه مربوط به دوره مالکیت خود را مشاهده می‌کند.

کاربران داخلی به تاریخچه کامل دسترسی دارند.

---

# Contracts

هر Customer می‌تواند چند Contract داشته باشد.

هر Contract برای یک Service Package تعریف می‌شود.

هر Package می‌تواند SLA متفاوتی داشته باشد.

---

# Service Packages

Service Package مجموعه‌ای از تجهیزات است.

نمونه:

Commercial Prepress

- CTP
- Processor
- RIP

یا

Digital Printing

- Digital Press
- RIP
- Finishing Equipment

---

# Ticket Philosophy

ثبت درخواست سرویس همیشه مجاز است.

وجود یا عدم وجود Contract مانع ثبت Ticket نیست.

Contract فقط روی نحوه ارائه سرویس اثر می‌گذارد.

---

# Ticket Types

## Guest

بدون ورود به سیستم

فرم ساده

ثبت درخواست تماس

---

## Authenticated Customer

پس از ورود

انتخاب:

- Site
- Package
- Device

سپس ثبت درخواست سرویس.

---

# Design Principles

- Odoo First
- OCA First
- Custom Last

---

تا حد امکان از مدل‌های استاندارد Odoo استفاده می‌شود.

در صورت نیاز فقط Modelهای کوچک و مستقل ایجاد خواهند شد.

---

# UI / UX

رابط کاربری مشتری و کارشناس به صورت اختصاصی طراحی می‌شود.

Backend کاربران داخلی تا حد امکان از رابط استاندارد Odoo استفاده خواهد کرد.

---

# Localization

- Persian Calendar (OCA)
- Persian Documents
- Persian Date
- English Language
- Bilingual (FA / EN)

---

# Project Principles

- Business First
- Domain Driven Design
- Modular Architecture
- Small Documents
- Fast Development
- Easy Maintenance
- Upgrade Friendly

---

# Odoo Mapping

| Business Entity | Odoo Model |
|-----------------|------------|
| Customer | res.partner |
| Contact | res.partner |
| Internal User | res.users |
| Site | res.partner (Child Address) |
| Asset | maintenance.equipment |
| Ticket | helpdesk.ticket |
| Warehouse | stock |
| Accounting | account |

---

# Document Roadmap

- DOC-001 Business Domain & Core Rules
- DOC-002 Asset Master Data
- DOC-003 Contract
- DOC-004 Service Policy (SLA)
- DOC-005 Service Package
- DOC-006 Service Request
- DOC-007 Service Report
- DOC-008 Parts & Inventory
- DOC-009 Roles & Permissions
- DOC-010 Workflow

---

**Status:** Approved
