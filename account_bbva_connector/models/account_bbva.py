# -*- coding: utf-8 -*-

from openerp import models, fields,api,_

class AccountBbva(models.Model):
    _inherit = 'mail.thread'
    _name = 'account.bbva'


    name = fields.Char(
        string='Cuenta')

    bbva_lines = fields.One2many(
        comodel_name='account.bbva.line',
        inverse_name='bbva_id',
        string='Moves')

    @api.multi
    def post(self):
        import pdb; pdb.set_trace()

    @api.multi
    def update_moves(self):
        import pdb; pdb.set_trace()
        

class AccountBbvaLine(models.Model):
    _name = 'account.bbva.line'

    amount = fields.Float(
        string='Amount')

    company_id = fields.Many2one(
    comodel_name='res.company',
    string='Compañía',
    default=lambda self: self.env.user.company_id)


    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        readonly="True",
        related='company_id.currency_id')

    description = fields.Char(
        string='Concept')

    category = fields.Char(
        string='Category')

    bbva_id = fields.Many2one(
        comodel_name='account.bbva',
        string='Account')

# class BbvaConfigSettings(models.TransientModel):
#     _name = 'account.bbva.config.settings'
#     _inherit = 'res.config.settings'
#
#     nif = fields.Char(
#         string='NIF')
#
#     password = fields.Char(
#         string='Password')
#
#     @api.multi
#     def execute(self):
#         values = {}
#         res = super(BbvaConfigSettings,self).execute()
#         ctx = {}
#         import pdb; pdb.set_trace()
#         config_obj = self.env['account.bbva.config.instance']
#         config_id = config_obj.search([])
#         values['nif'] = self.nif or False
#         values['password'] = self.password or False
#         if not config_id:
#             config_id = config_obj.create(values)
#         else:
#             config_id.write(values)
#
#         if res:
#             res['context']=ctx
#             res['params']={'nif':self.nif,'password': self.password or False}
#         return res

class BbvaConfigSettings(models.Model):
    _name = 'account.bbva.config'

    name = fields.Char(
        string='Name',
        default='Config')

    nif = fields.Char(
        string='NIF')

    password = fields.Char(
        string='Password')

    _sql_constraints = [
        ('bbva_sql_name_config',
         'unique(name)',
        "1 Config only"),]
