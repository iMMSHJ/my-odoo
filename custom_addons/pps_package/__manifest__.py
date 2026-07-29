{
    'name': 'PPS Package',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Groups customer assets under a service contract',
    'author': 'Your Company',
    'depends': ['pps_asset', 'contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/pps_package_views.xml',
    ],
    'installable': True,
    'application': False,
}
