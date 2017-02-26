from openerp.osv import fields, osv
from openerp.tools.translate import _

class res_partner(osv.osv):
	_name = 'res.partner'
	_inherit = 'res.partner'
	_columns = {
	   'rut' : fields.char('Rut' , size=10 , help='Este es rut'),
	   'edad' : fields.integer('Edad', size=3, help='Aqui pones la edad'),
	   'profesion' : fields.char('Profesion' , size=10 , help='Este es rut'),
	}


res_partner()