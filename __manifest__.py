# -*- coding: utf-8 -*-
###################################################################################
# Author: Quaint Park <https://www.quaintpark.com>
# Copyright (c) Quaint Park. All Rights Reserved.
#
# This program is the copyright property of the author, mentioned above.
# You can't redistribute it and/or modify it without permission.
#
# You should have received a copy of the License along with this program.
# If not, visit <https://www.github.com/QuaintPark/license>
###################################################################################
{
    'name': 'Quaint Starter',
    'summary': """Basic description.""",
    'description': """
Quaint Starter
==============
Basic description.
    """,
    'version': '13.0.1.0',
    'author': 'Quaint Park',
    'website': 'https://www.quaintpark.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
    ],
    'data': [
        ## Data
        # 'data/ir_sequence.xml',

        ## Security
        # 'security/ir.model.access.csv',

        ## Report
        # 'reports/my_model_name_report.xml',
        
        ## Wizard
        # 'wizards/my_model_name_wizard.xml',
        
        ## View
        # 'views/web_assets.xml',
        # 'views/my_model_name_view.xml',
        # 'views/menus.xml',
    ],
    'qweb': [
        ## Template
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'icon': '/qp_starter/static/description/icon.png',
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Jeshad Khan <https://github.com/jeshadkhan>',
    ],
}
