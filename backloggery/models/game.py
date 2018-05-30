# -*- coding: utf-8 -*-

from openerp import models, fields,api,_

class BackLoggeryGame(models.Model):
    _name = 'backloggery.game'
    _description = 'Product Game'

    name = fields.Char(
        string='Name')

    release_date = fields.Date(
        string='Release Date')

    platform = fields.Many2many(
        comodel_name='backloggery.platform',
        relation='backloggery_rel',
        column1='games',
        column2='platform',
        string='Platform')
