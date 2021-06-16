from odoo import api, models, fields, _


class CourseRoom(models.Model):
    _name = 'course.room'
    _description = 'Room'

    name = fields.Char(_('Name'), required=True)
    capacity = fields.Integer(_('Capacity'))

