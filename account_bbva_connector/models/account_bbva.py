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

class AccountBbvaLine(models.Model):
    _name = 'account.bbva.line'

    amount = fields.Float(
        string='Amount')

    company_id = fields.Many2one(
    comodel_name='res.company',
    string='Compañía',
    default=lambda self: self.env['res.company'].browse(self.env['res.company']._company_default_get()))


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
