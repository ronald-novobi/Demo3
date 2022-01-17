
from odoo.models import *

from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.exceptions import AccessError, UserError, ValidationError


class SaleLine((models.Model)):
    _inherit = 'sale.order.line'
    def unlink(self):
        if self._check_line_unlink() and not self.display_type:
            raise UserError(_('You can not remove an order line once the sales order is confirmed.\nYou should rather set the quantity to 0.'))
        return self.unlink()

