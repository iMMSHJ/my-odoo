# Documentation Index — Prepress Service Platform (Odoo Implementation)

این پوشه شامل تمام اسناد طراحی و تحلیل پروژه است که بر اساس فازهای یک پیاده‌سازی استاندارد Odoo دسته‌بندی شده‌اند: از تعریف دامنه کسب‌وکار تا معماری، طراحی داده، فرآیندها، تجربه کاربری و ماژول‌های عملیاتی.

## 00 — Business & Domain
پایه و قوانین اصلی کسب‌وکار که مبنای تمام تصمیمات طراحی بعدی است.
- [DOC-001 — Business Domain and Core Rules](00-business-and-domain/DOC-001-business-domain-and-core-rules.md)

## 01 — Data Model
مدل داده اصلی و نگاشت موجودیت‌ها (Entities).
- [DOC-002 — Asset Master Data](01-data-model/DOC-002-asset-master-data.md)
- [DOC-013 — Data Model / Entity Mapping](01-data-model/DOC-013-data-model-entity-mapping.md)
- [DOC-020 — Entity Mapping Design](01-data-model/DOC-020-entity-mapping-design.md)

## 02 — Service Core (Contracts, SLA, Packages, Tickets)
هسته دامنه سرویس: قرارداد، SLA، پکیج، تیکت، گزارش خدمات و انبار قطعات.
- [DOC-003 — Contract and Service Policy](02-service-core/DOC-003-contract-and-service-policy.md)
- [DOC-004 — Service Policy / SLA](02-service-core/DOC-004-service-policy-sla.md)
- [DOC-005 — Service Package](02-service-core/DOC-005-service-package.md)
- [DOC-006 — Service Request / Ticket Wizard](02-service-core/DOC-006-service-request-ticket-wizard.md)
- [DOC-007 — Service Report](02-service-core/DOC-007-service-report.md)
- [DOC-008 — Parts and Inventory](02-service-core/DOC-008-parts-and-inventory.md)
- [DOC-019 — Package / Contract / SLA Mapping Design](02-service-core/DOC-019-package-contract-and-sla-mapping-design.md)
- [DOC-022 — Contract Management Detail](02-service-core/DOC-022-contract-management-detail.md)

## 03 — Architecture
معماری سیستم، نگاشت ماژول‌های Odoo، ساختار پروژه، استقرار و مرز استاندارد/سفارشی‌سازی.
- [DOC-011 — System Architecture](03-architecture/DOC-011-system-architecture.md)
- [DOC-012 — Odoo Modules Mapping](03-architecture/DOC-012-odoo-modules-mapping.md)
- [DOC-014 — Project Structure](03-architecture/DOC-014-project-structure.md)
- [DOC-015 — Deployment and Infrastructure](03-architecture/DOC-015-deployment-and-infrastructure.md)
- [DOC-025 — Odoo Standard Alignment and Customization Boundary](03-architecture/DOC-025-odoo-standard-alignment-and-customization-boundary.md)
- [DOC-036 — OCA Minimization and Presentation Layer Customization Strategy](03-architecture/DOC-036-oca-minimization-and-presentation-layer-strategy.md)

## 04 — Workflow & Lifecycle
جریان کاری سیستم، چرخه عمر تیکت، اجرای عملیات میدانی و بستن سرویس.
- [DOC-010 — System Workflow](04-workflow-and-lifecycle/DOC-010-system-workflow.md)
- [DOC-021 — Ticket Lifecycle, Roles and Permissions](04-workflow-and-lifecycle/DOC-021-service-management-ticket-lifecycle-roles-and-permissions.md)
- [DOC-023 — Technician Task and Field Service Execution](04-workflow-and-lifecycle/DOC-023-technician-task-and-field-service-execution.md)
- [DOC-024 — Service Completion and Ticket Closure](04-workflow-and-lifecycle/DOC-024-service-completion-and-ticket-closure.md)

## 05 — UX / UI
معماری تجربه کاربری و ناوبری.
- [DOC-016 — UI/UX Architecture](05-ux-ui/DOC-016-ui-ux-architecture.md)
- [DOC-017 — User Journey and Navigation Architecture](05-ux-ui/DOC-017-user-journey-and-navigation-architecture.md)

## 06 — Roles & Access
نقش‌ها و سطوح دسترسی.
- [DOC-009 — Roles and Permissions](06-roles-and-access/DOC-009-roles-and-permissions.md)

## 07 — Customer Experience
تجربه مشتری: پورتال، CRM، پشتیبانی و مارکت‌پلیس.
- [DOC-018 — Service Ecosystem: CRM, Customer Portal and Localization Design](07-customer-experience/DOC-018-service-ecosystem-crm-customer-portal-and-localization-design.md)
- [DOC-026 — Customer Service Management Experience](07-customer-experience/DOC-026-customer-service-management-experience.md)
- [DOC-027 — Customer Support Center and Communication](07-customer-experience/DOC-027-customer-support-center-and-communication.md)
- [DOC-028 — Customer Marketplace Experience](07-customer-experience/DOC-028-customer-marketplace-experience.md)

## 08 — Dashboards
داشبوردهای نقش‌محور برای ادمین، مدیر سرویس و تکنسین.
- [DOC-029 — Role-Based Dashboard Experience](08-dashboards/DOC-029-role-based-dashboard-experience.md)
- [DOC-030 — Admin Dashboard Experience](08-dashboards/DOC-030-admin-dashboard-experience.md)
- [DOC-031 — Service Manager Dashboard Experience](08-dashboards/DOC-031-service-manager-dashboard-experience.md)
- [DOC-032 — Technician Dashboard Experience](08-dashboards/DOC-032-technician-dashboard-experience.md)

## 09 — Technician Operations
هزینه و مدیریت دانش/آموزش تکنسین‌ها.
- [DOC-033 — Technician Expense and Cost Management](09-technician-operations/DOC-033-technician-expense-and-cost-management.md)
- [DOC-035 — Knowledge Management and Technician Learning](09-technician-operations/DOC-035-knowledge-management-and-technician-learning.md)

## 10 — Notifications
مرکز اطلاع‌رسانی و مدیریت نوتیفیکیشن.
- [DOC-034 — Notification Center and Notification Management](10-notifications/DOC-034-notification-center-and-notification-management.md)

## 11 — Roadmap
نقشه راه اجرایی پروژه (فازبندی و وابستگی‌ها).
- [DOC-037 — Implementation Roadmap](11-roadmap/DOC-037-implementation-roadmap.md)

## 12 — Technical Design
طراحی فنی ماژول‌های اختصاصی (سطح پیاده‌سازی).
- [DOC-038 — pps_ticket_wizard Technical Design](12-technical-design/DOC-038-pps-ticket-wizard-technical-design.md) *(Draft)*

---

## وضعیت اسناد (Status Summary)

| بازه شماره | وضعیت غالب |
|---|---|
| DOC-001 تا DOC-017 | Approved |
| DOC-018 تا DOC-022 | Business Analysis / Design (فاز ۳) |
| DOC-023 تا DOC-035 | Locked |

> این جدول بر اساس فیلد Status درج‌شده در ابتدای هر سند تهیه شده؛ برای وضعیت دقیق هر سند به همان فایل مراجعه کنید.
