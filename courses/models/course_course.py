from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class CourseCourse(models.Model):
    _name = 'course.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Course'

    name = fields.Char(_('Name'), required=True)
    description = fields.Text(_('Description'))
    location_id = fields.Many2one('course.location', _('Location'))
    schedule = fields.Char(_('Schedule'))
    responsible_id = fields.Many2one('res.users', _('Responsible'))
    attendee_ids = fields.One2many('course.attendee', 'course_id', _('Attendees'))
    lesson_line_ids = fields.One2many('lesson.line', 'course_id', _('Lessons'))
    attendee_number = fields.Integer(_('Number of Attendees'), compute='_compute_attendee_number', store=True)
    lesson_number = fields.Integer(_('Number of Lessons'), compute='_compute_lesson_number', store=True)
    partner_ids = fields.Many2many('res.partner', 'course_partner_rel', 'course_id', 'partner_id',
                                   compute='_compute_partner_ids', store=True)

    @api.model
    def create(self, vals):
        res = super(CourseCourse, self).create(vals)
        if res.attendee_ids and res.lesson_line_ids:
            for line in res.lesson_line_ids:
                if len(res.attendee_ids) > line.room_id.capacity:
                    raise ValidationError(_('Number of attendees must be not than capacity of room'))
        if set(res.attendee_ids.mapped('partner_id')) & set(res.lesson_line_ids.mapped('instructor_id')):
            raise ValidationError(_('A person can not be an instructor and attendee of the same course'))
        return res

    def write(self, vals):
        res = super(CourseCourse, self).write(vals)
        if 'attendee_ids' in vals or 'lesson_line_ids' in vals:
            for line in self.lesson_line_ids:
                if len(self.attendee_ids) > line.room_id.capacity:
                    raise ValidationError(_('Number of attendees must be not than capacity of room'))
        if set(self.attendee_ids.mapped('partner_id')) & set(self.lesson_line_ids.mapped('instructor_id')):
            raise ValidationError(_('A person can not be an instructor and attendee of the same course'))
        return res

    @api.depends('attendee_ids')
    def _compute_partner_ids(self):
        for rec in self:
            if rec.attendee_ids:
                partner_ids = rec.attendee_ids.mapped('partner_id').ids
                rec.partner_ids = [(6, 0, partner_ids)]

    @api.depends('attendee_ids')
    def _compute_attendee_number(self):
        for rec in self:
            if rec.attendee_ids:
                rec.attendee_number = len(rec.attendee_ids)

    @api.depends('lesson_line_ids')
    def _compute_lesson_number(self):
        for rec in self:
            if rec.lesson_line_ids:
                rec.lesson_number = len(rec.lesson_line_ids)


class LessonLine(models.Model):
    _name = 'lesson.line'
    _description = 'Lesson Line'

    lesson_id = fields.Many2one('course.lesson', required=True)
    room_id = fields.Many2one('course.room')
    course_id = fields.Many2one('course.course')
    instructor_id = fields.Many2one('res.partner', _('Instructor'))
    capacity = fields.Integer(_('Capacity Room'), related='room_id.capacity', store=True)


class CourseLocation(models.Model):
    _name = 'course.location'
    _description = 'Course Location'

    name = fields.Char(_('Name'), required=True)
