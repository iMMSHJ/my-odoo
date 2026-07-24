# DOC-011
# System Architecture

**Status:** Approved

---

# Purpose

تعریف معماری کلان سیستم و ارتباط بین اجزای اصلی پروژه.

این سند فقط ساختار منطقی سیستم را مشخص می‌کند و وارد جزئیات پیاده‌سازی یا انتخاب ماژول‌های Odoo نمی‌شود.

---

# Architecture Principles

- Odoo First
- OCA First
- Custom Last
- Modular Design
- Mobile First
- API Ready
- Upgrade Friendly

---

# High Level Architecture

```text
                        Internet
                            │
                     Reverse Proxy (Nginx)
                            │
            ┌───────────────┴───────────────┐
            │                               │
     Public Website                  Customer Portal
            │                               │
            └───────────────┬───────────────┘
                            │
                         Odoo Core
                            │
 ┌──────────────┬──────────────┬──────────────┬──────────────┐
 │              │              │              │
 Helpdesk     Contacts      Inventory     Accounting
 │              │              │              │
 ├──────────────┼──────────────┼──────────────┤
 │              │              │
 Contracts    Assets        Timesheet
 │
 Service Reports
 │
 Attachments
 │
 Notifications
                            │
                     PostgreSQL Database
                            │
                        File Storage
```

---

# Logical Layers

## Presentation Layer

مسئول تعامل با کاربران

- Website
- Customer Portal
- Backend UI
- Mobile Browser

---

## Business Layer

منطق اصلی کسب‌وکار

- Ticket Management
- Service Workflow
- Contract Management
- SLA Engine
- Package Management
- Service Reports

---

## Odoo Core

هسته استاندارد Odoo

- Contacts
- Helpdesk
- Inventory
- Accounting
- Calendar
- Timesheet
- Security

---

## Data Layer

ذخیره‌سازی اطلاعات

- PostgreSQL
- Filestore
- Attachments

---

# User Groups

External Users

- Guest
- Customer Manager
- Customer Service
- Customer Operator
- Customer Accountant

Internal Users

- Super Admin
- Service Manager
- Technician
- Sales
- Warehouse
- Accountant

---

# Core Business Objects

- Customer
- Site
- Asset
- Package
- Contract
- SLA
- Ticket
- Service Report
- Parts
- Inventory
- User

---

# Workflow Overview

Guest / Customer

↓

Service Request

↓

Service Manager

↓

Technician

↓

Service Report

↓

Customer Feedback

↓

Service Manager

↓

Close Ticket

---

# External Interfaces

سیستم در آینده امکان اتصال به سرویس‌های زیر را خواهد داشت.

- Email
- SMS
- WhatsApp (Optional)
- REST API
- Customer Portal

---

# Security

سیستم امنیتی بر پایه قابلیت‌های استاندارد Odoo پیاده‌سازی می‌شود.

- Users
- Groups
- ACL
- Record Rules

هیچ سیستم امنیتی سفارشی در فاز اول توسعه ایجاد نخواهد شد.

---

# Design Decisions

## Accepted

- Odoo as Core Platform
- Native Inventory
- Native Accounting
- Native Security
- Native Portal
- Native Website

---

## Deferred

- Field Service
- Planning
- GIS / Maps
- Reservation Engine
- IAM
- Marketplace Integration

---

# Technical Principles

- Business Logic inside Odoo
- Minimum Customization
- Reuse Standard Modules
- Reuse OCA Modules
- Loose Coupling
- High Maintainability

---

# Out of Scope (MVP)

- Native Mobile Application
- AI Diagnosis
- IoT Integration
- Automatic Dispatch
- Predictive Maintenance
- Customer Self Scheduling

---

# Notes

این سند نمای کلی معماری سیستم را ارائه می‌دهد.

انتخاب ماژول‌های Odoo، OCA و Custom در **DOC-012 (Odoo Modules Mapping)** به صورت کامل بررسی خواهد شد.

---

**Status:** Approved
