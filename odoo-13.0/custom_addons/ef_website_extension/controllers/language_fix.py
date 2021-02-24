from odoo.addons.website.controllers.main import Website
from odoo import http
from odoo.http import request

class WebsiteExt(Website):
    @http.route()
    def change_lang(self, lang, r='/', **kwargs):
        res = super(WebsiteExt, self).change_lang(lang, r, **kwargs)
        if not request.env.user._is_public():
            request.env.user.partner_id.lang = lang
            request.env.user.lang = lang
            request.env['ir.http'].webclient_rendering_context()
        return res