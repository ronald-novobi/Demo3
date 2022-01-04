


import odoo

from odoo.models import *
from datetime import datetime
import requests
from odoo import _, api, exceptions, fields, models, modules,http
from odoo.http import request
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.addons.mail.models.res_users import *
from zipfile import ZipFile
import os
import shutil
import base64


import logging

from pytz import timezone
_logger = logging.getLogger(__name__)
class res_partner((models.Model)):
    _inherit = 'res.partner'
    status = fields.Selection([('New', 'New'),('In Review', 'In Review'),('Approved', 'Approved')])


    def action_set_approved(self):
        self.status='Approved'