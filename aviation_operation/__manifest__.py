{
    'name': 'Aviation Operation',
    'version': '16.0',
    'summary': 'Integration with Zenith',
    'description': """
        This module integrates with Zenith.
    """,
    'depends': ['base', 'account','hr'],
    'data': [
        'security/ir.model.access.csv',
        'view/operation_operation_view.xml',
        'view/airport_airport_view.xml',
        'view/aircraft_aircraft_view.xml',
        'view/crew_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
