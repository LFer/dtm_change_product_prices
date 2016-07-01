# -*- coding: utf_8 -*-
from openerp import models, fields, _, api, exceptions
from openerp.tools.misc import DEFAULT_SERVER_DATE_FORMAT
import datetime
from datetime import date, timedelta
import locale
import time
import logging
import ipdb as pdb
from openerp.exceptions import Warning
_logger = logging.getLogger(__name__)
import math
import calendar

class product_price(models.Model):
    _name = 'product.price'
    _description = 'Product Price'


    name = fields.Char(string='Name')
    products_ids = fields.Many2many(comodel_name='product.template',relation='product_id', string='Products')
    no_stock = fields.Boolean(string='Reajustar Todos los Produtos sin Sto')
    nuevo_precio = fields.Float(string='Nuevo Precio')


    @api.multi
    def cambiar_precio(self):
        if self.no_stock:
            productos_sin_stock = self.env['product.template'].search([('qty_available','=',0)])
            for sin_stock in productos_sin_stock:
                sin_stock.list_price = self.nuevo_precio
        else:
            for prods in self.products_ids:
                prods.list_price = self.nuevo_precio

product_price()
