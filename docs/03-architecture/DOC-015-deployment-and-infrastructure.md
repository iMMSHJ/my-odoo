# DOC-015
# Deployment & Infrastructure

**Status:** Approved

---

# Purpose

تعریف معماری استقرار (Deployment) و زیرساخت مورد نیاز برای اجرای سیستم به صورت Self-Hosted.

هدف این سند ارائه یک معماری پایدار، ساده، قابل نگهداری و مستقل از زیرساخت مشتری است.

---

# Deployment Philosophy

این محصول به صورت **Self-Hosted** ارائه می‌شود.

هر مشتری نسخه اختصاصی خود را بر روی زیرساخت خود نصب و نگهداری خواهد کرد.

---

# Infrastructure Principle

> The product must be infrastructure independent.

سیستم نباید وابسته به نوع Virtualization، نوع Storage یا تجهیزات شبکه باشد.

در صورت فراهم بودن پیش‌نیازهای استاندارد، محصول باید بدون تغییر روی هر زیرساختی قابل اجرا باشد.

---

# Operating System

سیستم به صورت رسمی بر روی نسخه‌های LTS اوبونتو پشتیبانی می‌شود.

Recommended

- Ubuntu Server LTS

---

# Application Stack

```text
Ubuntu Server

↓

Python

↓

PostgreSQL

↓

Odoo

↓

Nginx

↓

SSL
```

---

# Deployment Model

نوع استقرار

- Self Hosted

پشتیبانی می‌شود روی

- Physical Server
- Virtual Machine
- Private Cloud
- Customer Datacenter

---

# Containerization

در فاز اول پروژه از Docker یا سایر Container Runtimeها استفاده نخواهد شد.

استقرار به صورت Native Linux انجام می‌شود.

---

# Service Management

سرویس‌های سیستم توسط Systemd مدیریت خواهند شد.

نمونه سرویس‌ها

- Odoo Service
- PostgreSQL Service
- Nginx Service

---

# Reverse Proxy

از Nginx به عنوان Reverse Proxy استفاده خواهد شد.

وظایف

- SSL Termination
- Reverse Proxy
- Static Files
- Compression

---

# Database

Database Engine

- PostgreSQL

هیچ پایگاه داده دیگری در MVP پشتیبانی نمی‌شود.

---

# Storage

اطلاعات سیستم در سه بخش نگهداری می‌شوند.

- PostgreSQL Database
- Odoo Filestore
- Configuration Files

تمام این بخش‌ها باید در فرآیند Backup لحاظ شوند.

---

# Backup Strategy

حداقل اقلام Backup

- Database
- Filestore
- Configuration

امکان تهیه Backup خودکار باید وجود داشته باشد.

---

# Restore

فرآیند Restore باید به صورت مستقل قابل اجرا باشد.

بازگردانی شامل موارد زیر است.

- Database
- Filestore
- Configuration

---

# Installation

برای نصب سیستم اسکریپت‌های استاندارد ارائه خواهند شد.

نمونه

```text
install.sh
update.sh
backup.sh
restore.sh
```

هدف کاهش خطای انسانی و استانداردسازی فرآیند نصب و نگهداری است.

---

# Security

ارتباطات سیستم باید از طریق HTTPS انجام شود.

استفاده از SSL الزامی است.

---

# Logging

از سیستم Logging استاندارد Odoo استفاده خواهد شد.

در صورت نیاز امکان اتصال به سامانه‌های مرکزی جمع‌آوری Log در آینده وجود خواهد داشت.

---

# Monitoring

Monitoring در دو سطح تعریف می‌شود.

## Business Monitoring

برای مدیران سیستم

نمونه شاخص‌ها

- Open Tickets
- SLA Status
- Delayed Services
- Technician Workload
- Customer Satisfaction
- Parts Consumption
- Service Statistics

---

## Infrastructure Monitoring

در فاز اول خارج از محدوده پروژه است.

در آینده امکان اتصال به ابزارهای متن‌باز مانیتورینگ وجود خواهد داشت.

---

# High Availability

پیاده‌سازی HA بر عهده زیرساخت مشتری است.

سیستم باید قابلیت اجرا در محیط‌های High Availability را بدون نیاز به تغییر در نرم‌افزار داشته باشد.

---

# Open Source Policy

در انتخاب ابزارهای جانبی، اولویت با راهکارهای Open Source خواهد بود.

---

# Out of Scope

موارد زیر در MVP پیاده‌سازی نمی‌شوند.

- Docker
- Kubernetes
- Multi Node Deployment
- Distributed Database
- Infrastructure Monitoring
- Cloud Native Deployment

---

# Design Principles

- Self Hosted First
- Native Linux Deployment
- Infrastructure Independent
- Open Source First
- Upgrade Friendly
- Simple Maintenance
- Automated Installation
- Automated Backup

---

# Notes

این سند تنها معماری استقرار نرم‌افزار را مشخص می‌کند.

طراحی و مدیریت زیرساخت فیزیکی، تجهیزات شبکه، مجازی‌سازی، ذخیره‌سازی و امنیت محیط اجرا بر عهده تیم زیرساخت مشتری خواهد بود.

---

**Status:** Approved
