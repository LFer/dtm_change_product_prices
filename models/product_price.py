# -*- coding: utf_8 -*-
from openerp import models, fields, _, api, exceptions
from openerp.tools.misc import DEFAULT_SERVER_DATE_FORMAT
import datetime
from datetime import date, timedelta
import locale
import time
import logging
import ipdb as pdb
from openerp.exceptions import ValidationError, Warning
_logger = logging.getLogger(__name__)
import math
import calendar

class product_price(models.Model):
    _name = 'product.price'
    _description = 'Product Price'


    name = fields.Char(string='Name')
    products_ids = fields.Many2many(comodel_name='product.template',relation='product_id', string='Products')
    no_stock = fields.Boolean(string='Reajustar Todos los Produtos sin Stock')
    nuevo_precio = fields.Float(string='Nuevo Precio')
    porcentaje = fields.Float(string='Reajuste Percentual', size=3)
    precio_venta = fields.Boolean(string='Basado en Precio de Venta')
    precio_costo = fields.Boolean(string='Basado en Precio de Costo')
    tipo_ajuste = fields.Selection([('porcentaje', 'Porcentaje'), ('manual', 'Ingreso Manual')])


    @api.multi
    def cambiar_precio(self):
        #pdb.set_trace()
        if [self.no_stock,self.precio_venta,self.precio_costo].count(True) == 0:
            raise Warning('No ha establecido un un tipo de reajuste!')

        l = [self.no_stock,self.precio_venta,self.precio_costo]
        if sum(bool(x) for x in l) == 0:
            raise Warning('No ha establecido un un tipo de reajuste!')

        if self.precio_venta:
            if not self.porcentaje:
                raise Warning('No ha establecido un porcentaje!')
            if not self.products_ids:
                raise Warning('No ha selecionado ningun producto!')
            if 'porcentaje' in self.tipo_ajuste:
                for art in self.products_ids:
                    art.list_price = art.list_price*self.porcentaje/100 + art.list_price
                    print ('El nuevo precio de venta del articulo %s es' %(self.env['product.template'].browse(art.id).name), art.list_price)
            if 'manual' in self.tipo_ajuste:
                for art in self.products_ids:
                    art.list_price = self.nuevo_precio
                    print ('El nuevo precio de coste del articulo %s es' %(self.env['product.template'].browse(art.id).name), art.list_price)

        if self.precio_costo:
            if not self.porcentaje:
                raise Warning('No ha establecido un porcentaje!')
            if not self.products_ids:
                raise Warning('No ha selecionado ningun producto!')
            if 'porcentaje' in self.tipo_ajuste:
                for art in self.products_ids:
                    art.standard_price = art.standard_price*self.porcentaje/100 + art.standard_price
                    print ('El nuevo precio de coste del articulo %s es' %(self.env['product.template'].browse(art.id).name), art.standard_price)
            if 'manual' in self.tipo_ajuste:
                for art in self.products_ids:
                    art.standard_price = self.nuevo_precio
                    print ('El nuevo precio de coste del articulo %s es' %(self.env['product.template'].browse(art.id).name), art.standard_price)

        if self.no_stock:
            productos_sin_stock = self.env['product.template'].search([('qty_available','=',0)])
            for sin_stock in productos_sin_stock:
                sin_stock.list_price = self.nuevo_precio

        return {
            'type': 'ir.actions.client',
            'tag': 'action_warn',
            'name': 'Notificación',
            'params': {
                'title': 'Ajuste',
                'text': 'El ajuste de precios se realizó con éxito',
                'sticky': False
            }
        }

product_price()
