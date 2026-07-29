# -*- coding: utf-8 -*-

{
    "name": "Vina Service",
    "version": "19.0.1.0.0",
    "summary": "Vina Service Management",
    "description": "Core Service Module for Vina ERP",

    "author": "Vina Group",
    "category": "Services",
    "license": "LGPL-3",

    "depends": [
        "vina_base",
        "mail",
        "contacts",
    ],

    "data": [
        "security/security.xml",
        

        "views/menus.xml",
        "views/ticket_views.xml",
        "views/service_job_views.xml",
        "views/service_report_views.xml",
        "views/equipment_views.xml",
    ],

    "application": True,
    "installable": True,
}
