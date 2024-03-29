from odoo import models, fields, api

class linea_pedido(models.Model):
    _name = 'odoo_basico.linea_pedido'
    _description = 'Exemplo Linea Pedido'
    _order = "name asc"


    name = fields.Char(required=True, size=20, string="Linea Pedido")
    descripcion = fields.Text(string="A Descripción da Linea Pedido")  # string é a etiqueta do campo
    # Os campos One2many Non se almacenan na BD
    # Os campos Many2one crean un campo na BD
    pedido_id = fields.Many2one('odoo_basico.pedido', ondelete="cascade", required=True)
    # Os campos Many2many crean unha táboa na BD
    informacion_ids = fields.Many2many("odoo_basico.informacion",
                                       relation="odoo_basico_lineapedido_informacion",
                                       column1="lineapedido_id", column2="informacion_id")
