# DOC-014
# Project Structure

**Status:** Approved

---

# Purpose

تعریف ساختار پروژه، Repository و نحوه سازمان‌دهی ماژول‌های Odoo به گونه‌ای که توسعه، نگهداری و ارتقاء سیستم در آینده ساده و پایدار باشد.

---

# Design Principles

- Clean Project Structure
- Modular Development
- Odoo First
- OCA First
- Custom Last
- Upgrade Friendly
- Single Responsibility
- Loose Coupling

---

# Repository Structure

```text
prepress-service-platform/

├── odoo/                 # Odoo Core
│
├── oca/                  # OCA Community Modules
│
├── addons/               # Custom Modules
│
├── themes/               # Website & Portal Theme
│
├── config/               # Configuration Files
│
├── docker/               # Docker & Deployment
│
├── docs/                 # Project Documentation
│
├── scripts/              # Utility Scripts
│
└── backups/              # Backup Scripts & Templates
```

---

# Custom Modules

تمام توسعه‌های اختصاصی پروژه داخل پوشه `addons` قرار می‌گیرند.

هر ماژول تنها یک مسئولیت مشخص خواهد داشت.

نمونه:

```text
addons/

pps_asset
pps_package
pps_contract
pps_sla
pps_ticket
pps_service_report
pps_portal
pps_theme
pps_notification
pps_dashboard
```

---

# Module Naming Convention

تمام ماژول‌های اختصاصی با Prefix زیر آغاز می‌شوند.

```text
pps_
```

Example

- pps_asset
- pps_ticket
- pps_contract
- pps_package
- pps_portal
- pps_theme

---

# Odoo Core

هسته Odoo بدون تغییر نگهداری می‌شود.

هیچ تغییری روی Source Code اصلی Odoo انجام نخواهد شد.

---

# OCA Modules

تمام ماژول‌های Community در پوشه مستقل نگهداری می‌شوند.

```text
oca/
```

در صورت انتشار نسخه جدید، امکان بروزرسانی مستقل آن‌ها وجود خواهد داشت.

---

# Custom Development

تمام توسعه‌های اختصاصی فقط داخل پوشه

```text
addons/
```

انجام می‌شود.

وابستگی مستقیم به Core Odoo یا OCA مجاز نیست.

---

# Themes

تمام فایل‌های مربوط به رابط کاربری در پوشه

```text
themes/
```

نگهداری می‌شوند.

شامل:

- Website Theme
- Portal Theme
- Assets
- SCSS
- JavaScript
- Images
- Fonts

---

# Documentation

تمام مستندات پروژه داخل

```text
docs/
```

نگهداری خواهند شد.

شامل:

- Functional Documents
- Technical Documents
- ERD
- Architecture
- API Documentation

---

# Configuration

تمام فایل‌های پیکربندی داخل

```text
config/
```

نگهداری می‌شوند.

نمونه:

- odoo.conf
- logging.conf
- environment templates

---

# Docker

تمام فایل‌های مربوط به استقرار پروژه داخل

```text
docker/
```

قرار می‌گیرند.

---

# Scripts

اسکریپت‌های کمکی پروژه در مسیر

```text
scripts/
```

نگهداری می‌شوند.

نمونه:

- Backup
- Restore
- Migration
- Maintenance

---

# Design Rules

- Core Odoo is never modified.
- OCA modules remain independent.
- Custom modules are isolated.
- One module, one responsibility.
- Low coupling between modules.
- Reusable architecture.
- Upgrade friendly structure.

---

# Future Scalability

این ساختار امکان موارد زیر را فراهم می‌کند:

- ارتقاء نسخه Odoo
- بروزرسانی مستقل OCA
- توسعه ماژول‌های جدید
- جداسازی تیم‌های توسعه
- CI/CD
- Automated Testing

---

# Notes

این ساختار مبنای توسعه تمام فازهای پروژه خواهد بود.

هر توسعه جدید باید در یکی از ماژول‌های موجود انجام شود یا در صورت نیاز، به عنوان یک ماژول مستقل جدید ایجاد گردد.

---

**Status:** Approved
