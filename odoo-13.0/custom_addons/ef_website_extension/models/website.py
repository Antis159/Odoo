from odoo import models


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        res = super(Website, self).sale_product_domain()
        user = self.env.user
        partner_id = user.partner_id
        pricelist_id = False
        if partner_id:
            pricelist_id = partner_id.property_product_pricelist.item_ids.product_tmpl_id.ids
        if pricelist_id and partner_id.name != 'Public user':
                res += [('id', 'in', pricelist_id)]
        return res
