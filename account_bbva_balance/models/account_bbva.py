# -*- coding: utf-8 -*-

from openerp import models, fields,api,_

class AccountBbva(models.Model):
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

    description = fields.Char(
        string='Concept')

    bbva_id = fields.Many2one(
        comodel_name='account.bbva',
        string='Account')
