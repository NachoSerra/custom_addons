# -*- coding: utf-8 -*-

from openerp import models, fields,api,_

class BackLoggeryPlatform(models.Model):
    _name = 'backloggery.platform'
    _description = 'Product Game'

    name = fields.Char(
        string='Name')

    # games = fields.Many2one(
    #     comodel_name='backloggery.game',
    #     string='Games')

    games = fields.Many2many(
        comodel_name='backloggery.game',
        relation='backloggery_rel',
        column1='platform',
        column2='games',
        string='Games')
