
from odoo.models import *

from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.addons.sale.models.sale import SaleOrderLine


class SaleLine((models.Model)):
    _inherit = 'sale.order.line'
    def unlink(self):
        for line in self:
            if line._check_line_unlink() and not line.display_type:
                raise UserError(_('You can not remove an order line once the sales order is confirmed.\nYou should rather set the quantity to 0.'))
            super(SaleOrderLine, line).unlink()

