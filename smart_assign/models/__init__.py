# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from . import stock_move_assign
from odoo.addons.stock.models import stock_move
stock_move.StockMove._action_assign = stock_move_assign._action_assign

