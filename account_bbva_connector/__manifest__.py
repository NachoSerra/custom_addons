# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2018 Ignacio José Serra Almenar
#                       info <nachoserra1988@gmail.com>
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
{
'name' : 'Account BBVA Connector',
'summary': 'Connector between Odoo and BBVA accounts',
'version' : '10.0.1.0.0',
'license': 'AGPL-3',
'author' : 'NachoSerra',
'website': 'https://github.com/NachoSerra/custom_addons/',
'category' : 'Accounting',
'depends' : ['account',],
'data': ['views/account_bbva.xml',
         'wizard/account_bbva_import.xml'],
'qweb' : [],
'demo': [],
'test': [],
'installable': True,
}
