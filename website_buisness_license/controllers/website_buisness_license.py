# coding: utf-8



from datetime import datetime
import requests, json
from odoo import _, api, exceptions, fields, models, modules,http
from odoo.http import request, Response
from odoo.addons.base.models.res_users import is_selection_groups
from odoo.addons.mail.models.res_users import *
from zipfile import ZipFile
import os
import shutil
import werkzeug
import base64
import hashlib
from werkzeug.exceptions import NotFound

class businessLicense((http.Controller)):
    @http.route('/business-license/form/', auth='public',  website=True, csrf=False)
    def display_buisnes_license_page(self,**kw):

        if 'token' in kw and request.env['res.partner'].search([('business_license_token','=',kw['token'])]):
            return request.render("website_buisness_license.buiness_license_page",{'token':kw['token']})
        else:
            return NotFound()

    @http.route(['/business-license/submit'],  type="http", auth='public',  methods=['POST'],  website=True, csrf=False)
    def recieve_buisness_license(self,**kw):

        if 'token' in kw:
            related_partner_id = request.env['res.partner'].search([('business_license_token','=',kw['token'])],limit=1)
            business_file = kw['Business File']

            related_partner_id.write({'business_license': base64.b64encode(business_file.read())})
            return request.render("website_buisness_license.website_buiness_license_success")
