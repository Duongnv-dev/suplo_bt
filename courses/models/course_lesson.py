from odoo import api, models, fields, _


class CourseLesson(models.Model):
    _name = 'course.lesson'
    _description = 'Lessons'

    name = fields.Char(_('Name'))
