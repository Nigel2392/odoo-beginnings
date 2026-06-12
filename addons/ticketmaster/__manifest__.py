{
    "name": "Odoo TicketMaster",
    "version": "1.0",
    'depends': ['base', 'mail'],
    "author": "Nigel2392",
    "category": "learning",
    'application': True,
    "description": """
    Learning the basics of the Odoo platform, implemented as a simple ticketing system.
    """,
    # data files always loaded at installation
    'data': [
        "data/status_data.xml",
        "views/menu.xml",
    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}
