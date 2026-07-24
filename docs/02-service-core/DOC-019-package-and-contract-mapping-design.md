# DOC-019 — Package & Contract Mapping Design

**Status:** Approved
**Version:** 2.0 (Refactored)
**Phase:** Phase 3
**Document Type:** Business Analysis & Entity Relationship Design

---

# 1. Purpose

تعریف مفهوم **Package** و ارتباط آن با **Contract، Asset، و SLA**.

هدف اصلی:
- توضیح Package به عنوان یک مفهوم **قراردادی** نه **عملیاتی**
- جلوگیری از اشتباه گرفتن Package با Product یا Inventory Item
- تعریف دقیق رابطه Package ↔ Contract ↔ Asset ↔ SLA

---

# 2. Package Definition

## Package چیست؟

**Package** یک گروه منطقی از **Assets (تجهیزات)** است که برای ارائه سرویس در یک **Contract مشخص** تجمیع شده‌اند.

مثال:

```
Contract: ABC Service Agreement

├── Package 1: Prepress System
│   ├── Plate Tester (SN: 12532)
│   ├── RIP Server (SN: 546558)
│   └── Processor (SN: 655585)
│
└── Package 2: Digital Printing
    ├── Digital Press (SN: 5548855)
    └── RIP Server (SN: 66559)
```

---

## Package نیست:

❌ **Product** — برای فروش و Inventory  
❌ **Inventory Item** — فقط قطعات است  
❌ **Entity مستقل** — وابسته به Contract است  
❌ **Service Ticket** — فقط برای مدیریت قراردادی است

---

# 3. Package Purpose

Package **تنها** برای موارد زیر استفاده می‌شود:

✅ Contract Management  
✅ SLA Definition  
✅ Service Relationship  
✅ Asset Grouping  

---

Package در این موارد **وارد نمی‌شود:**

❌ Inventory Flow  
❌ Product Catalog  
❌ Marketplace  
❌ Ticket Creation Flow  
❌ Financial Calculations

---

# 4. Package vs Contract

### Contract
- یک سند **حقوقی رسمی**
- دارای شماره قرارداد، تاریخ، امضا
- دارای شرایط مالی و حقوقی
- دارای SLA مشخص
- **Entity در Odoo**

### Package
- یک **گروه منطقی Assets**
- داخل یک Contract تعریف می‌شود
- فقط برای **Grouping و Mapping**
- بخشی از توصیف‌کننده Contract است
- ممکن است Entity جداگانه یا فقط Reference باشد

---

# 5. Core Relationship Model

```
Customer
  │
  ├── Contract 1
  │   ├── Package 1
  │   │   ├── Asset 1
  │   │   ├── Asset 2
  │   │   └── Asset 3
  │   └── SLA 1
  │
  └── Contract 2
      ├── Package 2
      │   ├── Asset 4
      │   └── Asset 5
      └── SLA 2
```

---

# 6. Key Rule: One Package = One Contract

**تصمیم اساسی:**

هر Package دارای **یک Contract مستقل** است.

**دلیل:**
- SLA ممکن است متفاوت باشد
- شرایط مالی ممکن است متفاوت باشد
- تاریخ شروع/پایان ممکن است متفاوت باشد
- مسئولیت قانونی جداگانه است

**نتیجه:**
```
حتی اگر دو Package شرایط مشابه داشته باشند،
دو Contract جداگانه و مستقل هستند.
```

---

# 7. Package Lifecycle

```
Draft
  ↓
Active
  ↓
Expired
  ↓
Archived
```

Package lifecycle **کاملاً وابسته به Contract** است.

---

# 8. Package Changes

اگر Assets درون یک Package تغییر کنند:

```
Question:
├── آیا Contract تغییر می‌کند؟
├── آیا SLA تغییر می‌کند؟
└── آیا هزینه تغییر می‌کند؟
```

**قاعده:** هر تغییر اساسی نیازمند **Contract Amendment** یا **Contract جدید** است.

---

# 9. Asset Ownership & Package

- **مالک Asset:** Customer
- **Grouping Asset:** Package (در سیاق Contract)
- **Tracking Asset:** Service Manager

---

# 10. SLA Relationship

SLA **متعلق به Contract است، نه Package:**

```
Contract
  │
  └── SLA
      │
      └── Applied to Assets in Package
```

---

# 11. Ticket Relationship

Ticket **مستقیماً Package را انتخاب نمی‌کند:**

```
Customer
  ↓
Ticket
  ↓
Select Asset
  ↓
Find Related Package (via Asset)
  ↓
Find Related Contract
  ↓
Apply SLA
```

---

# 12. Package vs Marketplace / Product

| موضوع | Package | Product | Inventory |
|------|---------|---------|-----------|
| مقصد | قرارداد | فروش | انبار |
| SLA | ✅ | ❌ | ❌ |
| Contract | ✅ | محدود | ❌ |
| موجودی | نه | بله | بله |
| مشتری | نامعلوم | عموم | داخلی |

---

# 13. Customer Visibility

در Customer Portal:

```
Customer می‌بیند:
├── Assets (لیست تجهیزات)
├── Asset Detail (مرتبط با Package)
├── Related Contract
└── Related SLA
```

اما **Package name** نمایش داده نمی‌شود اگر Metadata داخلی باشد.

---

# 14. Multiple Contracts Scenario

```
Customer XYZ:

├── Contract A (Package: Prepress)
│   ├── Plate Tester
│   ├── RIP
│   └── Processor
│   └── SLA: 48 Hours
│
└── Contract B (Package: Digital)
    ├── Digital Press
    └── Scanner
    └── SLA: 24 Hours
```

هر Contract مستقل و جداگانه است.

---

# 15. Integration Notes

### Related Documents:

**↔ DOC-020:** Entity Mapping & Contract Details  
👉 برای جزئیات Entity Relationship ببینید DOC-020

**↔ DOC-021:** Ticket Lifecycle & SLA Application  
👉 برای جریان Ticket ↔ Package ببینید DOC-021

**↔ DOC-025:** Customization Boundary  
👉 Package فقط Logical Grouping است

---

# 16. Design Decision Summary

✅ Package = Logical Group of Assets within Contract  
✅ Package ≠ Independent Entity  
✅ Package is Contractual, not Operational  
✅ One Package = One Contract Rule  
✅ SLA belongs to Contract, applies to Package  
✅ Asset ownership is Customer, grouping is Package  
✅ Package changes require Contract Amendment  

---

# Status

**APPROVED** ✅

