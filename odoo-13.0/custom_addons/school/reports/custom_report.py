from odoo import api, models

class ParticularReport(models.AbstractModel):
    _name = 'report.school.report_meeting_template'

    @api.model
    def _get_report_values(self, docids, data=None):

        # user_lang = self.env.user.partner_id.lang
        # usr_lang2 = self.env.lang
        user = self.env.user
        stop = True
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('school.report_meeting_template')
        self.env['stock.inventory'].browse(docids)
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
            'data': data
        }
        return docargs