{
    'name': 'PPS SLA',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Service Level Agreement templates for contracts',
    'author': 'Your Company',
    'depends': ['pps_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/pps_sla_views.xml',
    ],
    'installable': True,
    'application': False,
}
