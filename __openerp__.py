{
    'name': 'NOTIFICATION EMAIL AUTOMATIC',
    'version': '1.0',
    'depends': ["base", "crm"],
    'author': 'Edgard Pimentel',
    'email': 'pimentelrojas@gmail.com',
    'website': '',
    'description': 'module customized for CUIDUM',
    'data': [
        "security/ir.model.access.csv",
        "data/cront_data.xml",
        "views/send_automatic_view.xml"
    ],
    'installable': True,
    'active': False
}
