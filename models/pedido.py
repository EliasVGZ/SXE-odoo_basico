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


    #TODO Actualiza el campo de sexo cuando el autorizado está a false
    def actualizadorSexo(self):
        informacion_ids = self.env['odoo_basico.informacion'].search([('autorizado', '=', False)])
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion']._cambia_campo_sexo(rexistro)

    #TODO Crea regisotr de informacion DESDE PEDIDO
    def creaRexistroInformacion(self):
        creado_id = self.env['odoo_basico.informacion'].create({'name': 'Creado dende pedido'})
        creado_id.descripcion = "Creado dende o modelo pedido"
        creado_id.autorizado = False


    #Todo Actualiza registro de informacion DESDE PEDIDO
    def actualizaRexistroInformacion(self):
        informacion_id = self.env['odoo_basico.informacion'].search([('name', '=', 'Creado dende pedido')])
        if informacion_id:
            informacion_id.name = "Actualizado ..."
            informacion_id.descripcion = "Actualizado dende o modelo pedido"
            informacion_id.sexo_traducido = "Mujer"

    def actualizadorHoraTimezone(self):
        informacion_ids = self.env['odoo_basico.informacion'].search([])
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion'].actualiza_hora_timezone_usuario(rexistro)


