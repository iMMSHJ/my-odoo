# DOC-053 — Production Migration & Backup Plan

**Status:** LOCKED
**Phase:** Cross-Phase (آماده‌سازی خروج از Staging)
**Document Type:** Runbook
**Traces to:** DOC-014, DOC-040, DOC-048, DOC-050, DOC-052

---

# 1. Objective

دستورالعمل عملی برای سه اقدام مستقل قبل از انتقال به Production:

1. انتقال کامل ماژول‌های اختصاصی (`pps_*`) به GitHub
2. تهیه Backup کامل از دیتابیس خام و خروج از Staging
3. تهیه Backup از تمام Configها و ذخیره‌سازی خارج از سرور

⚠️ این سند فقط **راهنمای اجراست** — من (Claude) دسترسی مستقیم به سرور شما یا اینترنت GitHub ندارم؛ همه‌ی دستورات باید توسط شما اجرا شوند.

---

# 2. بخش ۱ — انتقال ماژول‌های اختصاصی به GitHub

## 2.1 پیش‌نیاز

یک Repository خالی روی GitHub بسازید (یا از همون `IMMSHJ/my-odoo` که قبلاً اشاره کردید استفاده کنید، اگر برای این کار مناسبه).

## 2.2 دستورات

```bash
cd /opt/odoo/custom_addons

# اگر هنوز Git Repo نیست
git init
git remote add origin https://github.com/<username>/<repo>.git

# فایل .gitignore برای جلوگیری از Commit فایل‌های کش
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
EOF

git add pps_asset pps_contract pps_sla pps_ticket_wizard .gitignore
git commit -m "Add pps_* custom modules (asset, contract, sla, ticket_wizard)"
git branch -M main
git push -u origin main
```

⚠️ **نکته امنیتی:** قبل از Push، مطمئن شوید هیچ فایل حساس (Password، API Key) داخل کد ماژول‌ها نوشته نشده — کد ما (`pps_asset`, `pps_contract`, `pps_sla`, `pps_ticket_wizard`) هیچ Credential داخلش ندارد، پس ایمن است.

## 2.3 ماژول‌های OCA — استراتژی جدا

ماژول‌های `oca/*` (Clone شده از GitHub رسمی OCA) **نباید** داخل همین Repository شخصی شما Commit شوند — این‌ها Repository مستقل خودشان را دارند. به‌جای Commit کردن کدشان، فقط لیست دقیق (نسخه/Commit) آن‌ها مستند می‌شود (بخش ۴).

---

# 3. بخش ۲ — Backup دیتابیس خام

## 3.1 دستور Backup کامل

```bash
mkdir -p ~/backups
sudo -u postgres pg_dump -Fc vina-odoo > ~/backups/vina-odoo-$(date +%Y%m%d-%H%M).dump
ls -lh ~/backups/
```

(از فرمت `-Fc` — Custom Format — استفاده شد چون فشرده‌تر است و امکان Restore انتخابی جدول‌به‌جدول هم می‌دهد.)

## 3.2 خروج از Staging (انتقال فایل به بیرون از سرور)

```bash
# روی سیستم لوکال خودتان (نه روی سرور i-srv)، این دستور رو بزنید:
scp mmshj@<آی‌پی-سرور>:~/backups/vina-odoo-*.dump ./
```

یا اگر سرور فقط لوکال (VMware) است، مستقیم از طریق Shared Folder یا کپی فایل به هاست خارج کنید.

## 3.3 تست صحت Backup (خیلی مهم — قبل از اعتماد کامل)

```bash
sudo -u postgres createdb vina-odoo-test-restore
sudo -u postgres pg_restore -d vina-odoo-test-restore ~/backups/vina-odoo-*.dump
# اگر بدون خطا تموم شد:
sudo -u postgres dropdb vina-odoo-test-restore
```

---

# 4. بخش ۳ — Backup Configها

## 4.1 فایل‌های لازم

```bash
mkdir -p ~/backups/configs
sudo cp /etc/odoo/odoo.conf ~/backups/configs/
sudo cp /etc/systemd/system/odoo.service ~/backups/configs/
```

## 4.2 لیست دقیق ماژول‌های OCA (نسخه/Commit) — برای بازتولید دقیق محیط

```bash
for dir in /opt/odoo/oca/*/; do
    name=$(basename "$dir")
    commit=$(cd "$dir" && git rev-parse HEAD 2>/dev/null)
    branch=$(cd "$dir" && git rev-parse --abbrev-ref HEAD 2>/dev/null)
    echo "$name | branch=$branch | commit=$commit" >> ~/backups/configs/oca-modules-versions.txt
done
cat ~/backups/configs/oca-modules-versions.txt
```

## 4.3 لیست نهایی ماژول‌های نصب‌شده در دیتابیس (طبق توصیه DOC-040 §6)

```bash
sudo -u odoo /opt/odoo/venv/bin/python3 /opt/odoo/src/odoo/odoo-bin shell -c /etc/odoo/odoo.conf -d vina-odoo --no-http << 'PYEOF'
mods = env['ir.module.module'].search([('state', '=', 'installed')])
with open('/tmp/installed_modules.txt', 'w') as f:
    for m in mods:
        f.write(f"{m.name} | {m.latest_version}\n")
print("Done — /tmp/installed_modules.txt")
PYEOF
cp /tmp/installed_modules.txt ~/backups/configs/
```

## 4.4 فشرده‌سازی و خروج نهایی

```bash
tar -czf ~/backups/configs-full-$(date +%Y%m%d).tar.gz ~/backups/configs/
```

سپس همین فایل رو هم مثل بخش ۳.۲ به بیرون از سرور منتقل کنید.

---

# 5. چک‌لیست نهایی قبل از انتقال به Production

- [ ] کد ماژول‌های `pps_*` روی GitHub Push شد
- [ ] Backup کامل دیتابیس گرفته شد و بیرون از سرور ذخیره شد
- [ ] صحت Backup با Restore آزمایشی تأیید شد
- [ ] `odoo.conf` و `odoo.service` بیرون از سرور ذخیره شدند
- [ ] لیست دقیق نسخه/Commit همه‌ی ماژول‌های OCA ثبت شد
- [ ] لیست کامل ماژول‌های نصب‌شده در دیتابیس ثبت شد

---

**Status:** LOCKED
