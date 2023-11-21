from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo informacion'
    _sql_constraints = [('nomeUnico', 'unique(name)', 'O Titulo xa existe na Base de Datos')] #RESTRICCION SQL, en este caso por el nombre, no pueden repetir el titulo
    _order = "descripcion desc" #Se ordenada descendente

    name = fields.Char(required=True, size=20, string="Escriba algo para odoo_basico:")
    descripcion = fields.Text(string="A descripcion: ")
    alto_en_cms = fields.Integer(string="Alto en centimetros: ")
    longo_en_cms = fields.Integer(string="Longo en centimetros: ")
    ancho_en_cms = fields.Integer(string="Ancho en centimetros: ")
    volume = fields.Float(digits=(6, 6), compute="_volume", store=True, string="Volume en m3")  # true, se almacena en bbdd
    literal = fields.Char(store=False)  # si esta en false no se almacenada en la base de datos
    peso = fields.Float(digits=(6, 2), default=2.7, string="Peso en Kgs: ")
    densidade = fields.Float(compute="_densidade", store="True", string="Densidade en KG/m3")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    sexo_traducido = fields.Selection([('Hombre', 'Home'), ('Mujer', 'Muller'), ('Otros', 'otros')], string="Sexo")

    # Cuando se cambien alguno de los campos vaise a ejecutar este metodo
    @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = (float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(rexistro.ancho_en_cms)) / 1000000

    @api.depends('volume', 'peso')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            else:
                rexistro.densidade = 0

    @api.onchange('alto_en_cms')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que estar entre 1 e 4 ' % rexistro.name)


