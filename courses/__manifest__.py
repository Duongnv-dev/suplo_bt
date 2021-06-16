# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Course',
    'version': '14.0.0.0.1',
    'author': 'Duong Nguyen',
    'category': 'Test',
    'sequence': 10,
    'website': '',
    'licence': 'AGPL-3',
    'summary': 'Management Course',
    'depends': [
        'mail', 'website',
    ],
    'css': [

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/res_partner.xml',
        'views/course_lesson.xml',
        'views/website_form.xml',
        'report/course_report.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
