# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Domatix (http://www.domatix.com)
#                       info <email@domatix.com>
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
from odoo.tools import float_compare, float_is_zero
from odoo.exceptions import UserError
from odoo.exceptions import Warning
import logging
import mimetypes
from lxml import etree
import base64
import xlrd
import tempfile
import datetime

logger = logging.getLogger(__name__)

class AccountBbvaImport(models.TransientModel):
    _name = 'account.bbva.import'
    _description = 'Import BBVA moves'

    order_file = fields.Binary(
        string='File', required=True,
        help="Movements from BBVA to upload")
    order_filename = fields.Char(string='File')

    account_number = fields.Char(
        string='Account Number')


    @api.model
    def _read_xls(self, datafile):
        try:
            wb = xlrd.open_workbook(datafile)
            sh = wb.sheet_by_index(0)
            header = sh.row_values(4)
            lines = []
        except Exception:
            return False

        if sh.nrows == 0:
            return False

        for rownum in range(5, sh.nrows):
            i = 0
            data = {}
            for col in sh.row_values(rownum):
                data[header[i]] = col
                i += 1
            lines.append(data)
        return lines


    @api.multi
    def import_button(self):
        f = tempfile.NamedTemporaryFile()
        f.write(base64.decodestring(self.order_file))
        f.flush()

        lines = self._read_xls(f.name)
        f.close()
        # Recorrer excel
        account_number = self.account_number
        account_obj = self.env['account.bbva']
        account_id = account_obj.search([('name','=',account_number)])
        if not account_id:
            account_vals = {
                            'name': account_number,
                            'last_import': datetime.datetime.now()
                            }

            account_id = account_obj.create(account_vals)

        for line in lines:
            fecha = line['Fecha']
            fechavalor = line['F.Valor']
            concepto = line['Concepto']
            movimiento = line['Movimiento']
            importe = line['Importe']
            disponible = line['Disponible']
            observaciones = line['Observaciones']

            #Conversión de fecha del excel
            start_date = "30/12/1899"
            timedelta = datetime.timedelta(days=int(fecha))
            date_1_line = datetime.datetime.strptime(start_date,"%d/%m/%Y")
            end_date = date_1_line + timedelta
            fecha = end_date

            timedelta = datetime.timedelta(days=int(fechavalor))
            date_1_line = datetime.datetime.strptime(start_date,"%d/%m/%Y")
            end_date = date_1_line + timedelta
            fechavalor = end_date
            account_line_vals = {
                            'bbva_lines': [(0,0,{'fecha': fecha,
                                                 'fechavalor': fechavalor,
                                                 'concepto': concepto,
                                                 'movimiento': movimiento,
                                                 'importe': importe,
                                                 'disponible': disponible,
                                                 'observaciones': observaciones,
                                                 })]
                                }
            account_id.write(account_line_vals)

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.bbva',
            'target': 'current',
            'res_id': account_id.id,
            'type': 'ir.actions.act_window'
            }
