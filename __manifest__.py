# -*- coding: utf-8 -*-
# Part of eagle. See LICENSE file for full copyright and licensing details.


{
    'name' : 'Eagle Custom Document Templates',
    'version' : '14.0.1',
    'summary': 'Customization',
    'sequence': 15,
    'description': """
Customisation Eagle ERP
=======================
    """,
    'category': 'Custom',
    'website': 'http://www.eagle.com',
    'images' : [],
    'depends' : ['base','web','sale'],
    'data': [
        'views/templates.xml',
    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    # 'post_init_hook': '_auto_install_l10n',
}
