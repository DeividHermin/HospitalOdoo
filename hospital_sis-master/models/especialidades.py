from openerp.osv import fields, osv

class especialidades(osv.osv):
	_name = 'sis.especialidades'
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	}

especialidades();
