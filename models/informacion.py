from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo informacion'
    _sql_constraints = [('nomeUnico', 'unique(name)', 'O Titulo xa existe na Base de Datos')] #RESTRICCION SQL, en este caso por el nombre, no pueden repetir el titulo
    _order = "descripcion desc" #Se ordenada descendente

    name = fields.Char(required=True, size=20, string="Titulo")
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
    foto = fields.Binary(string='Foto')
    adxunto_nome = fields.Char(string="Nome Adxunto")
    adxunto = fields.Binary(string="Arquivo adxunto")



    # Os campos Many2one crean un campo na BD
    moeda_id = fields.Many2one('res.currency', string="Moneda ELIAS", domain="[('position','=','after')]")
    # con domain, filtramos os valores mostrados. Pode ser mediante unha constante (vai entre comillas) ou unha variable
    # Cuando se cambien alguno de los campos vaise a ejecutar este metodo

    # PARA VER LA MONEDA EN MODO TEXTO
    moeda_en_texto = fields.Char(related="moeda_id.currency_unit_label",
                                 string="Moeda en formato texto", store=True)

    moeda_euro_id = fields.Many2one('res.currency',
                                    default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")],limit=1))
    gasto_en_euros = fields.Monetary("Gasto en Euros", 'moeda_euro_id')



#PARA SABER QUIEN ES EL USUARIO CREADOR
    creador_da_moeda = fields.Char(related="moeda_id.create_uid.login",
                                   string="Usuario creador da moeda", store=True)




    #TODO CAMBIAR A HOMBRE CUANDO AUTORIZADO ESTE A FALSE
    def _cambia_campo_sexo(self, rexistro):
        rexistro.sexo_traducido = "Hombre"


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


