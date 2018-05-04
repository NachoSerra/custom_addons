# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Nacho Serra Almenar <nachoserra1988@gmail.com> @NachoSerra GitHub
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields, api, _
from datetime import datetime


class MedicalVeterinaryAppointment(models.Model):
    _name = 'medical.veterinary.appointment'
    _inherit = 'mail.thread'
    _description = 'Appointment'

    @api.model
    def _default_name(self):
        return self._description

    name = fields.Char(
        string='Name',
        default=_default_name)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner')

    patient = fields.Many2one(
        comodel_name='medical.veterinary.pet',
        string='Patient')

    state = fields.Selection(
        [('draft', 'Draft'),
         ('confirmed','Confirmed'),
         ('finished','Finished'),
         ('cancel', 'Canceled')],default='draft',
        string='State')

    @api.model
    def _default_datetime(self):
        date = datetime.now()
        return date

    date = fields.Datetime(
        string='Date',
        default=_default_datetime)

    invoice_id = fields.Many2one(
        comodel_name='account.invoice',
        string='Invoice')

    @api.model
    def create(self, vals):
        new_id = super(MedicalVeterinaryAppointment, self).create(vals)
        # new_id.message_post(body='Appointment created',subject='Appointment',message_type='notification')
        return new_id
