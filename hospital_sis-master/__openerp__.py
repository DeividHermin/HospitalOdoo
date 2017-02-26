{
    'name': 'Sistema de Información Hospitalario',
    'version': '1.1',
    'author': 'David Hernández Mingorance',
    'category': 'Accounting & Finance',
    'summary': 'Modulo de gestion de hospital',
    'sequence': 30,
    'website': 'https://www.iesayala.com',
    'description': """
Es un módulo de ejemplo
======================
Con este modulo haremos nuestra primera aplicación en Odoo.
 * Uno
 * Dos
Nota: Necesita Ventas.
    """,
    'license' : 'AGPL-3',
    'depends': ['sale','base_setup', 'product', 'analytic', 'report'],
    'data': [
        'views/partner_view.xml',
        'views/hospital_view.xml',
        'views/especialidades_view.xml',
        'views/consultas_view.xml',
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}