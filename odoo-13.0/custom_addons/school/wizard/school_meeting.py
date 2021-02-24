from datetime import date

from odoo import _, api, fields, models


class SchoolMeetingsWizard(models.TransientModel):
    _name = 'school.meeting'
    _description = 'School Wizard test'
    classroom_name = fields.Many2one('school.classroom', string='Classrooms')

    start_date = fields.Date(string='Opening Date', required=True, readonly=False)
    end_date = fields.Date(string='Closing Date', required=True, readonly=False)

    def print_report(self):
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

        return self.env.ref('school.report_meeting_card').report_action([], data=data)