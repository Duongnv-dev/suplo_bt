from odoo import api, models, fields, _


class CourseAttendee(models.Model):
    _name = 'course.attendee'
    _description = 'Attendee'

    partner_id = fields.Many2one('res.partner', _('Contact'), required=True)
    email = fields.Char(_('Email'), related='partner_id.email')
    phone = fields.Char(_('Phone'), related='partner_id.phone')
    course_id = fields.Many2one('course.course', _('Course'))
