# -*- coding: utf-8 -*-
{
    'name': "Disable Enterprise",
    'summary': """Disable Enterprise Code""",
    'description': """Disable Enterprise Code""",
    'author': "Odoo Community Iran",
    'website': "https://odoo-community.ir/",
    'category': 'Technical',
    'version': '1.0',
    "license": "AGPL-3",
    'depends': ['base', 'mail'],
    'data': [
        'data/update_notification.xml',
        'data/service_cron.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'disable_enterprise/static/src/webclient/**/*.xml',
        ],
    },
    "installable": True,
}
