from odoo import models, fields, api

class pedido(models.Model):
    _name = 'odoo_basico.pedido'
    _description = 'Exemplo Pedido'
    _sql_constraints = [('nomeUnico', 'unique(name)',
                         'O identificador de Pedido xa existe na base de datos')]  # RESTRICCION SQL, en este caso por el nombre, no pueden repetir el titulo
    _order = "name asc" #Se ordenada descendente


    name = fields.Char(required=True, size=20, string="Pedido")
    descripcion = fields.Text(string="A Descripción do Pedido")  # string é a etiqueta do campo
    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.linea_pedido", 'pedido_id')
