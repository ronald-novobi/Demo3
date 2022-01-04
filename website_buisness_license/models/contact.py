# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.


from odoo.models import *
from datetime import datetime
import requests
from odoo import _, api, exceptions, fields, models, modules
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.addons.mail.models.res_users import *
from zipfile import ZipFile
import os
import shutil
import base64
from time import time
import hashlib

class ResPartner((models.Model)):
    _inherit = 'res.partner'
    business_license_token = fields.Char("Business License Token")
    business_license = fields.Binary("Business License")

    def generate_token(self):
            t = time()
            key = (str(t)+str(self.id))
            generated_token = hashlib.sha256(key.encode()).hexdigest()

            while len(self.env['res.partner'].search([('business_license_token','=',generated_token)])):
                t = time()
                key = (str(t)+str(self.id))
                generated_token = hashlib.sha256(key.encode()).hexdigest()
            self.business_license_token = generated_token

