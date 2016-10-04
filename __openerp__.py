# -*- encoding: utf-8 -*-
##########################################################################
#    Copyright (C) OpenERP Uruguay (<http://openerp.com.uy>).
#    All Rights Reserved
# Credits######################################################
#    Coded by: Felipe Ferreira
#    Planified by: Felipe Ferreira - Carlos Lamas
#    Finance by: Datamatic S.A. - www.datamatic.com.uy
#
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
{
    'name': 'Precio de Productos',
    'version': '1.0',
    'website' : 'www.datamatic.com.uy',
    'category': 'Proyectos',
    'summary': 'Cambio Masivo de Precios de Productos',
    'description': """
Cambio masivo a precios de productos
====================================

Este modulo permite cambiar masivamente los precios


Caracteristicas Principales
---------------------------
* Define roles de seguridad
* Manager: Permiso de acceso admnisitrativo.
* Officer: Permisos de acceso para gestionar las liquidaciones.
* User: Usuario del sistema que ve solo los datos refentes a su liquidación
""",
    'author': 'Datamatic',
    'depends': ['base','product','stock'],
    'data': [
        'views/product_price_view.xml',
#        'views/stock_move.xml',
#        'views/work_order_hour.xml',
#        'views/account_invoice.xml',
#        'views/account_account_view.xml',
#        'views/account_analytic_account_view.xml',
#        'views/holydays_config.xml',
#        'views/partner_view.xml',
#        'wizard/export_to_csv_view.xml',
#        'wizard/create_invoice_view.xml',
#        'data/work_order_sequence.xml',
#        'data/work_order_hour_tasks.xml',
#        'data/holydays_data.xml',
#        'data/holydays.config.csv',
#        'data/viaticos_data.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}