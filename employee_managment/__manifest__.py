# -*- coding: utf-8 -*-
{
    'name':'Employee Managment',
    'version': '1.1',
    'author': 'G.Gozal',
    'summary': "Employee Managment System",
    'sequence': 1,
    'description':"Employee Managment System",
    'category':'Administration',
    'website':'https://github.com/georgegozal',
    'depends':['mail','report_xlsx'],
    'data':[
        "security/ir.model.access.csv",
        'data/data.xml',
        "views/id_view.xml",
        "views/id_department.xml",
        "views/id_features.xml",
        
        "report/id_card.xml",
        "report/report.xml"


    ],
    'demo':[],
    'installable': True,
    'application': True,
    'auto_install': False,
}