# -*- coding: utf-8 -*-

{
    'name': 'Payroll Management',
    'version': '1.0.0',
    'category': 'Payroll',
    'website': 'https://github.com/amarjin6/payroll',
    'author': 'Alexander Marjin',
    'sequence': -100,
    'summary': 'Payroll Management System',
    'description': """Payroll Management System""",
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}
