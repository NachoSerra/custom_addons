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

    last_import = fields.Date(
        string='Last Import')


    @api.multi
    def post(self):
        pass
    @api.multi
    def update_moves(self):
        pass
class AccountBbvaLine(models.Model):
    _name = 'account.bbva.line'

    company_id = fields.Many2one(
    comodel_name='res.company',
    string='Compañía',
    default=lambda self: self.env.user.company_id)


    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        readonly="True",
        related='company_id.currency_id')

    bbva_id = fields.Many2one(
        comodel_name='account.bbva',
        string='Account')

    fecha = fields.Date(
        string='Date')

    fechavalor = fields.Date(
        string='Date Value')

    concepto = fields.Char(
        string='Concept')

    movimiento = fields.Char(
        string='Movement')

    importe = fields.Float(
        string='Amount')

    disponible = fields.Float(
        string='Amount available')

    observaciones = fields.Char(
        string='Observaciones')






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
