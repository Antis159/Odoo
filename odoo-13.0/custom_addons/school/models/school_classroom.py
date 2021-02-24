from odoo import api, fields, models, _, tools


class SchoolClassroom(models.Model):
    _name = 'school.classroom'
    _description = 'School Classroom'
    _order = 'classroom_grade desc, name'
    _rec_name = 'short_name'
    name = fields.Char('Classroom name', required=True)
    classroom_grade = fields.Integer(string='Classroom grade')
    classroom_students = fields.Many2many('res.partner', string='Students')

    short_name = fields.Char(
        string='Short Title',
        size=100,
        translate=False, )
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State')
    description = fields.Html(
        string='Description',
        sanitize=True,
        strip_style=False,
        translate=False, )
    cover = fields.Binary('Classroom Picture')
    still_in_school = fields.Boolean('Class still in school?')
    date_start = fields.Date('Start date')
    date_updated = fields.Datetime('Last Updated')
    students = fields.Integer(
        string='Number of Students',
        default=0,
        help='Total classroom student count',
        groups='base.group_user',
        states={'not in school': [('readonly', True)]},
        copy=True,
        index=False,
        readonly=False,
        required=False,
        company_dependant=False, )
    teacher_rating = fields.Float('Teacher Average Rating', digits=(14, 4), )

    # def name_get(self):
    #     result = []
    #     for record in self:
    #         result.append(
    #             (record.id,
    #              "%s (%s)" % (record.name, record.classroom_grade)
    #         ))
    #     return result


