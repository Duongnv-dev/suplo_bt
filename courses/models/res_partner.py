from odoo import api, models, fields, _


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    course_ids = fields.Many2many('course.course', 'course_partner_rel', 'partner_id', 'course_id', _('Courses'))
