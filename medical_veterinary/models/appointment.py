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

    appointment_lines = fields.One2many(
        comodel_name='medical.veterinary.appointment.line',
        inverse_name='appointment_id',
        string='Appointment Lines')

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

    @api.multi
    def action_confirm(self):
        for record in self:
            record.write({'state':'confirmed'})
            vals = {'origin': record.name,
                    'type': 'out_invoice',
                    'account_id': record.partner_id.property_account_receivable_id.id,
                    'partner_id': record.partner_id.id,
                    'partner_shipping_id': record.partner_id.id,
                    'merged': True,
                    'fiscal_position_id': record.partner_id.property_account_position_id.id,
                    'user_id': record.env.user.id,
                    }
            invoice_id = self.env['account.invoice'].create(vals)
            record.invoice_id = invoice_id
            invoice_id.appointment_id = record.id
            for lines in record.mapped('appointment_lines'):
                ir_property_obj = self.env['ir.property']
                account_id = False
                if lines.product_id.id:
                    account_id = lines.product_id.property_account_income_id.id
                if not account_id:
                    inc_acc = ir_property_obj.get('property_account_income_categ_id', 'product.category')
                    account_id = invoice_id.fiscal_position_id.map_account(inc_acc).id if inc_acc else False

                invoice_id.write({
                    'invoice_line_ids': [(0, 0, {
                        'name': lines.product_id.display_name,
                        'origin': lines.appointment_id.name,
                        'account_id': account_id,
                        'price_unit': lines.product_id.lst_price,
                        'quantity': lines.qty,
                        'uom_id': lines.product_id.uom_id.id,
                        'product_id': lines.product_id.id,
                    })],
                })
            invoice_id.compute_taxes()

            invoices = record.mapped('invoice_id')
            action = self.env.ref('account.action_invoice_tree1').read()[0]
            if len(invoices) == 1:
                action['views'] = [(self.env.ref('account.invoice_form').id, 'form')]
                action['res_id'] = invoices.ids[0]
            else:
                action = {'type': 'ir.actions.act_window_close'}
            return action

class MedicalVeterinaryAppointmentLine(models.Model):
    _name = 'medical.veterinary.appointment.line'
    _description = 'Appointment Lines'

    appointment_id = fields.Many2one(
        comodel_name='medical.veterinary.appointment',
        string='Appointment')

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product')

    qty = fields.Float(
        string='Quantity',
        default=1)
