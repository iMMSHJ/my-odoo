{
    'name': 'PPS Asset',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Customer-owned prepress equipment registry',
    'description': """
Custom Asset model for customer-owned prepress equipment.
Independent from Odoo's maintenance.equipment (per DOC-041 decision).
    """,
    'author': 'Your Company',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/pps_asset_views.xml',
        'views/pps_asset_brand_model_views.xml',
    ],
    'installable': True,
    'application': False,
}
