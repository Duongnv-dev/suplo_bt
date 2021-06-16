from odoo import api, models, fields, tools, _


class CourseLessonReport(models.Model):
    _name = 'course.lesson.report'
    _auto = False

    id = fields.Integer('ID')
    measure = fields.Integer(string=_('Measure Lessons'), readonly=True)
    course_id = fields.Many2one('course.course')

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'course_lesson_report')
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW course_lesson_report AS
            (
            SELECT 
                row_number() OVER() AS id,
                cc.id as course_id,
                cc.lesson_number as measure
                FROM
                course_course AS cc              
            );
        ''')
