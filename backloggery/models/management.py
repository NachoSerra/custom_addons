# -*- coding: utf-8 -*-

from openerp import models, fields,api,_

class BackLoggeryManagement(models.Model):
    _name = 'backloggery.management'
    _description = 'Product Management'

    name = fields.Char(
        string='Name')

    hours_total = fields.Float(
        string='Hours',
        compute='_compute_hours',
        store=True)

    lines = fields.One2many(
        comodel_name='backloggery.management.line',
        inverse_name='backlog_id',
        string='Games played')

    @api.depends('lines.hours')
    def _compute_hours(self):
        for record in self:
            record.hours_total = sum(record.lines.mapped('hours'))

class BackLoggeryManagementLine(models.Model):
    _name = 'backloggery.management.line'

    backlog_id = fields.Many2one(
        comodel_name='backloggery.management',
        string='Backlog')

    game = fields.Many2one(
        comodel_name='backloggery.game',
        string='Game')

    start_date = fields.Date(
        string='Start Date')

    end_date = fields.Date(
        string='End Date')

    hours = fields.Float(
        string='Hours')

    review = fields.Float(
        string='Review')
