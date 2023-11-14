
from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo informacion'

    name = fields.Char(required=True, size=20, string="Escriba algo para odoo_basico:")
    descripcion = fields.Text(string="A descripcion: ")
    alto_en_cms = fields.Integer(string="Alto en centimetros: ")
    longo_en_cms = fields.Integer(string="Longo en centimetros: ")
    ancho_en_cms = fields.Integer(string="Ancho en centimetros: ")
    peso = fields.Float(digits=(6,2), default = 2.7, string="Peso en Kgs: " )
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)
    sexo_traducido = fields.Selection([('Hombre', 'Home'), ('Mujer', 'Muller'), ('Otros', 'otros')], string="Sexo")


