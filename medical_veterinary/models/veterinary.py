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


class MedicalVeterinaryPet(models.Model):
    _name = 'medical.veterinary.pet'
    _description = 'Pet'
    _inherit = 'mail.thread'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        help='Select or create a new Partner')

    appointment_ids = fields.One2many(
        comodel_name='medical.veterinary.appointment',
        inverse_name='patient',
        string='Appointments')


    name = fields.Char(
        string='Name')

    age = fields.Integer(
        string='Age')

    type = fields.Many2one(
        comodel_name='medical.veterinary.type',
        string='Type')

    breed = fields.Many2one(
        comodel_name='medical.veterinary.breed',
        string='Breed')


class MedicalVeterinaryType(models.Model):
    _name = 'medical.veterinary.type'

    name = fields.Char(
        string='Name')

class MedicalVeterinaryBreed(models.Model):
    _name = 'medical.veterinary.breed'

    name = fields.Char(
        string='Name')
