# DOC-038 — `pps_ticket_wizard` Technical Design

**Status:** LOCKED
**Phase:** Phase 3 (Custom Experience Layer)
**Document Type:** Technical Design
**Traces to:** DOC-006 (Business Rules), DOC-025 §4.A, DOC-036 §4, DOC-039 §6

---

# 1. Objective

طراحی فنی ماژول `pps_ticket_wizard` — تنها راه ثبت Ticket برای Guest و Customer.
این سند، قوانین کسب‌وکار DOC-006 را به یک معماری فنی قابل پیاده‌سازی تبدیل می‌کند، بدون استفاده از فرم استاندارد Helpdesk یا هر OCA Portal Template (طبق DOC-036 §4).

---

# 2. Module Boundaries

```
pps_ticket_wizard/
├── __manifest__.py
├── controllers/
│   └── ticket_wizard_controller.py     # HTTP endpoints (JSON-RPC)
├── models/
│   └── ticket_wizard_helper.py         # منطق کمکی روی helpdesk.ticket (بدون تغییر ساختار Core)
├── static/src/
│   ├── js/                             # Owl Components (اختصاصی)
│   ├── scss/                           # از pps_theme import می‌شود، فایل جدا برای رنگ ندارد
│   └── xml/                            # Templates (نه Website Builder Snippet)
└── security/
    └── ir.model.access.csv             # دسترسی Guest/Portal به Endpointها
```

**وابستگی‌ها:** `helpdesk`, `portal`, `pps_asset`, `pps_contract`, `pps_sla`, `pps_theme`
**عدم وابستگی عمدی:** هیچ ماژول OCA UI/Portal، هیچ `website` Snippet.

---

# 3. Wizard State Machine

**به‌روزرسانی (طبق DOC-039 §6.3):** یک Step جدید «نوع درخواست» قبل از Page 1 اضافه شد که Team مقصد Ticket را تعیین می‌کند: **سرویس دستگاه / IT / آموزش**.

برای حفظ سادگی v1 (طبق اصل «شلوغش نکنیم»): فقط مسیر **سرویس دستگاه** از Page 2 (انتخاب دستگاه/محل) عبور می‌کند. برای IT و آموزش، Page 2 (که مخصوص Asset است) **حذف/Skip** می‌شود و مستقیم به مرحله توضیحات می‌رویم — چون این دو نوع لزوماً به یک Asset ثبت‌شده گره نخورده‌اند.

```mermaid
stateDiagram-v2
    [*] --> IdentifyUser
    IdentifyUser --> RequestType: انتخاب نوع درخواست

    RequestType --> Page1_ContactInfo: دستگاه / IT / آموزش

    Page1_ContactInfo --> Page2_DeviceAndLocation: نوع = سرویس دستگاه
    Page1_ContactInfo --> DescriptionStep: نوع = IT یا آموزش (Page 2 حذف می‌شود)

    Page2_DeviceAndLocation --> AutoDetect: دستگاه و محل مشخص شد
    AutoDetect --> DescriptionStep

    DescriptionStep --> Review: توضیح و پیوست ثبت شد
    Review --> Submit: تأیید نهایی
    Submit --> Confirmation
    Confirmation --> [*]
```

هر گذار (Transition) دقیقاً منطبق بر یک قانون کسب‌وکار در DOC-006 یا DOC-039 است — Wizard هیچ مرحله اضافه‌ای نسبت به مستندات تأییدشده اضافه نمی‌کند.

---

# 4. Step-by-Step Field Spec

## Step 1 — Identify User
| فیلد | منبع | یادداشت |
|---|---|---|
| Session/Login State | Odoo `request.env.user` | تعیین Guest vs Customer |

## Step 2 — Request Type (جدید)
| فیلد | نوع | الزامی | نگاشت Odoo | یادداشت |
|---|---|---|---|---|
| Request Type | Select (۳ گزینه) | ✅ | `helpdesk.ticket.team_id` | گزینه‌ها: «سرویس دستگاه»، «خدمات IT»، «آموزش» — طبق DOC-039 §6.2 |

> SLA در همه حالت‌ها از یک موتور واحد محاسبه می‌شود (DOC-039 §10.1)؛ این انتخاب فقط Team/دسته‌بندی را تعیین می‌کند، نه موتور SLA جدا.

## Page 1 — Contact Info (مشترک برای Guest و Customer، در هر سه نوع درخواست)

**Guest:** فیلدها به‌صورت دستی پر می‌شوند.
**Customer:** فیلدها از `res.partner` پیش‌بارگذاری و قابل تأیید/ویرایش هستند (مطابق DOC-006: «هیچ گزینه‌ای پیش‌فرض انتخاب نمی‌شود» برای لیست‌ها، اما اطلاعات تماس شناخته‌شده نمایش داده می‌شود).

| فیلد | نوع | الزامی | نگاشت Odoo |
|---|---|---|---|
| Name | Text | ✅ | `res.partner.name` |
| Company | Text | ❌ | `res.partner.parent_id` / تکست آزاد (Guest) |
| Mobile | Text | ✅ | `res.partner.mobile` |
| Email | Text | ❌ | `res.partner.email` |
| City | Select | ❌ | `res.partner.city_id` |

## Page 2 — Device & Location (فقط برای نوع «سرویس دستگاه»)

**Guest:** فیلدهای دستگاه به‌صورت دستی + یک فیلد آزاد محل قرارگیری دستگاه.
**Customer:** انتخاب Asset از لیست موجود؛ محل قرارگیری از `pps_asset.location` پیش‌بارگذاری می‌شود ولی قابل ویرایش است (دستگاه ممکن است جابه‌جا شده باشد).

| فیلد | نوع | الزامی | نگاشت Odoo | یادداشت |
|---|---|---|---|---|
| Device Brand | Select | ✅ (Guest) | برای Auto-match `maintenance.equipment` | فقط Guest |
| Device Model | Select | ✅ (Guest) | همان | فقط Guest |
| Serial Number | Text | ❌ | `maintenance.equipment.serial_no` | فقط Guest |
| Asset (دستگاه) | Select | ✅ (Customer) | `pps_asset` مرتبط با `partner_id` جاری | فقط Customer |
| Device Location | Text/Select (Site) | ✅ | `pps_asset.location_id` (Customer) یا آدرس آزاد (Guest) | محل نصب/استقرار دستگاه — برای برنامه‌ریزی Onsite Visit ضروری است |

**Serial Number Disambiguation (Customer):** فقط اگر بیش از یک Asset مشابه وجود داشته باشد نمایش داده می‌شود (DOC-006 «Kodak RIP SN:...»). طبق قانون طلایی *Never ask if the system already knows*، اگر فقط یک Asset مطابقت داشته باشد، انتخاب به‌صورت خودکار انجام می‌شود.

**IT / آموزش:** این صفحه کاملاً حذف می‌شود؛ در صورت نیاز، اشاره به دستگاه/نرم‌افزار مرتبط در همان فیلد توضیحات (Step بعد) به‌صورت متن آزاد ذکر می‌شود — بدون فیلد ساختاریافته اضافه در v1.

## Step 3 — Auto Detect (Read-only، فقط برای «سرویس دستگاه»)
داده‌های زیر از Asset/Device انتخاب‌شده در Page 2 استخراج و به‌صورت Read-only نمایش داده می‌شوند:
- Customer, Site, Service Package, Contract, SLA/Service Policy, Warranty, Previous Service History

منبع: متد کمکی `_get_asset_context(asset_id)` در `ticket_wizard_helper.py` که به مدل‌های `pps_contract`, `pps_package`, `pps_sla` Join می‌زند.

برای IT/آموزش، این Step هم Skip می‌شود؛ SLA برای این دو نوع طبق قانون Fallback در DOC-039 §10.1 محاسبه می‌شود (سطح قرارداد مشتری در صورت وجود، وگرنه پایین‌ترین سطح).

## Step 4 — Description & Attachment
| فیلد | نوع | الزامی |
|---|---|---|
| Issue Description | Textarea | ✅ |
| Attachment | Image Upload (چندتایی) | ❌ |

**تصمیم نهایی روی Attachment:** هر فرمت تصویری با هر سطح فشرده‌سازی/کیفیتی پذیرفته می‌شود (JPEG، PNG، WebP، HEIC و غیره) — بدون محدودیت یا تبدیل اجباری سمت کلاینت. اعتبارسنجی فقط بر مبنای MIME Type عمومی `image/*` انجام می‌شود؛ فشرده‌سازی/بهینه‌سازی (در صورت نیاز آینده برای کاهش حجم Storage) به‌صورت غیرمسدودکننده (Async) در بک‌اند قابل انجام است، نه به‌عنوان پیش‌شرط ثبت.

> طبق DOC-006، سیستم از مشتری عیب‌یابی فنی نمی‌خواهد — فقط توضیح آزاد نیاز و مشکل، به‌همراه تصویر اختیاری.

## Step 5 — Review & SLA Preview
نمایش خلاصه غیرقابل‌ویرایش (شامل Page 1، Page 2 و Description) + پیش‌نمایش SLA محاسبه‌شده (Read-only، از `pps_sla`) — مطابق اصل «SLA Calculation» در DOC-025 §4.A.

## Step 6 — Confirmation

پیام‌های خروجی طبق DOC-006 (سه حالت) + عناصر تکمیلی زیر:

### همه حالت‌ها (Guest / Customer)
| عنصر | توضیح |
|---|---|
| کد رهگیری (Tracking Code) | شناسه یکتا و کوتاه (نه ID داخلی دیتابیس) — نمایش برجسته، قابل کپی |
| پیام تشکر | متن کوتاه و گرم، مطابق زبان طراحی DOC-018 §8 (Minimal, Modern) |
| خلاصه SLA | زمان پاسخگویی/رسیدگی مورد انتظار — از همان پیش‌نمایش Step 5 |

### فقط Guest — عناصر اضافه
| عنصر | توضیح |
|---|---|
| پیشنهاد ساخت حساب کاربری | CTA برجسته: «برای پیگیری آنلاین وضعیت، حساب بسازید» |
| هشدار عدم امکان پیگیری آنلاین | تصریح می‌شود که بدون حساب کاربری، پیگیری وضعیت تیکت از طریق پورتال ممکن نیست و فقط با کد رهگیری (تلفنی/حضوری) قابل استعلام است |

> کد رهگیری برای Guest **جایگزین** دسترسی پورتال است، نه معادل آن — این تفاوت باید در UI کاملاً شفاف بیان شود تا انتظار اشتباه ایجاد نشود.

---

# 5. Guest Duplicate-Submission Prevention (پنجره ۴۵ روزه)

## 5.1 هدف

جلوگیری از ثبت تیکت تکراری توسط یک Guest برای همان درخواست، بدون نیاز به احراز هویت کامل یا CRM Lead.

## 5.2 مکانیزم

پس از ثبت موفق تیکت توسط Guest، **۱ یا ۲ فیلد شناسایی‌کننده** (مثلاً ترکیب `Mobile` + `Serial Number`، یا در نبود Serial، `Mobile` + `Device Brand/Model`) به‌همراه Timestamp در یک جدول سبک (`pps.guest.submission.lock`) ذخیره می‌شود.

```
Key   = hash(Mobile + Serial/Device)
TTL   = 45 روز
Value = تاریخ آخرین ثبت + Tracking Code مرتبط
```

## 5.3 رفتار در ثبت بعدی

اگر Guestای با همان Key در بازه ۴۵ روزه دوباره اقدام به ثبت کند:

- سیستم اجازه ثبت Ticket جدید نمی‌دهد.
- پیام روشن نمایش داده می‌شود: «برای همین درخواست قبلاً یک تیکت با کد `XXXXXX` ثبت شده است.»
- کد رهگیری قبلی مجدداً به کاربر نمایش داده می‌شود (بازیابی، نه ثبت مجدد).

## 5.4 محدودیت‌های عمدی (Scope)

- این مکانیزم **جایگزین احراز هویت یا CRM Lead نیست** — صرفاً جلوگیری از ثبت تکراری (Spam/Duplicate) در بازه کوتاه‌مدت است.
- بعد از انقضای ۴۵ روز، Guest می‌تواند دوباره برای همان دستگاه تیکت ثبت کند (فرض بر این است که مشکل قبلی یا حل‌شده یا نیاز به پیگیری تازه دارد).
- این قفل مانع مراجعه Guest به روش‌های دیگر (تماس تلفنی و غیره) نمی‌شود؛ فقط مسیر Wizard آنلاین را محدود می‌کند.

## 5.5 Odoo Mapping

| جزء | پیاده‌سازی |
|---|---|
| ذخیره‌سازی | مدل سبک اختصاصی `pps.guest.submission.lock` (نه توسعه روی `res.partner` یا `helpdesk.ticket`) |
| پاک‌سازی خودکار | Scheduled Action (Cron) روزانه برای حذف رکوردهای منقضی‌شده |
| بدون ارتباط با CRM | این مدل کاملاً مستقل از Lead/Opportunity است (طبق تصمیم این بخش، Lead ساخته نمی‌شود) |

---

# 5. Backend Flow (Controller → ORM)

```mermaid
flowchart LR
    UI["Custom Wizard UI\n(Owl Component)"] -->|"JSON-RPC POST"| CTRL["TicketWizardController\n(http.Controller)"]
    CTRL -->|"sudo() فقط برای Guest"| ORM["ORM Layer"]
    ORM --> HD["helpdesk.ticket\n(Standard)"]
    ORM --> AST["pps_asset"]
    ORM --> SLA["pps_sla"]
    CTRL -->|"JSON Response"| UI
```

- کنترلر هیچ View استاندارد Odoo برنمی‌گرداند — فقط JSON.
- برای Guest از `sudo()` محدود و کنترل‌شده استفاده می‌شود (فقط برای Create روی `helpdesk.ticket` و `res.partner`، نه دسترسی عمومی).
- برای Customer از Session Portal استاندارد استفاده می‌شود (بدون sudo).

---

# 6. Non-Goals (صراحتاً خارج از Scope)

- ❌ تغییر ساختار مدل `helpdesk.ticket` (فقط استفاده، طبق DOC-025 §5)
- ❌ استفاده از `portal.mixin` Templates پیش‌فرض برای نمایش فرم
- ❌ استفاده از هیچ OCA Helpdesk Portal Module
- ❌ منطق تشخیص فنی/عیب‌یابی سمت مشتری

---

# 7. Resolved Questions

1. **Attachment:** حل شد — هر فرمت تصویری با هر کمپرسی پذیرفته می‌شود (بخش ۴، Step 4).
2. **CRM Lead برای Guest ناشناخته:** حل شد — Lead ساخته نمی‌شود (طبق DOC-039 §10، تصمیم پروژه سادگی v1 است). به‌جای آن، مکانیزم سبک «جلوگیری از ثبت تکراری Guest» (بخش ۵) برای کنترل درخواست‌های تکراری کافی است.
3. **نوع درخواست (IT/آموزش):** حل شد — Step جدید «Request Type» اضافه شد (بخش ۳ و ۴)، طبق DOC-039 §6.3.

---

# DOC-038 — LOCKED ✅
