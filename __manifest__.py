# -*- coding: utf-8 -*-
{
    'name': "Owl Dashboard",
    'summary': """Best Custom Dashboard""",
    'description': """Owl Custom Dashboard""",
    'author': "Tasin Tarek",
    'website': "https://tasin-tarek.odoo.com/",
    'category': 'Customizations',
    'version': '16.0.1',
    'depends': [
        'base',
        'web',
        'sale',
        'board',
    ],
    'data': [
        'views/dashboard.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl/static/src/components/dashboard.js',
            'owl/static/src/components/dashboard.xml',
            'owl/static/src/components/dashboard.scss',
        ],
    },
}
