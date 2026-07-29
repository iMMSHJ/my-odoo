{
    'name': 'PPS Ticket Wizard',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Custom multi-step ticket submission form (Guest & Customer)',
    'author': 'Your Company',
    'depends': ['website', 'helpdesk_mgmt', 'pps_asset', 'pps_contract', 'pps_sla'],
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'pps_ticket_wizard/static/src/css/wizard.css',
            'pps_ticket_wizard/static/src/js/device_step.js',
        ],
    },
    'installable': True,
    'application': False,
}
