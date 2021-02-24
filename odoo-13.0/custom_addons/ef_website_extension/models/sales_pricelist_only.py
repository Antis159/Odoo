from odoo import api, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def onchange_product_id(self):
        user = self.env['product.template']
        if self.order_id.pricelist_id:
            product_template_ids = self.env['product.template'].search([('id', 'in', self.order_partner_id.property_product_pricelist.item_ids.product_tmpl_id.ids)])
            product_ids = self.env['product.product'].search([('product_tmpl_id', 'in', product_template_ids.ids)])
            return {'domain': {'product_id': [('id', 'in', product_ids.ids)]}}
