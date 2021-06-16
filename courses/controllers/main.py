from odoo import http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request
from werkzeug.exceptions import NotFound


class WebsiteHrRecruitment(http.Controller):
    @http.route(['/courses'], type='http', auth="public", website=True)
    def courses(self, **kwargs):
        courses = request.env['course.course'].search([])
        return request.render("courses.index", {
            'courses': courses,
        })

    @http.route('''/courses/detail/<model("course.course"):course>''', type='http', auth="public", website=True)
    def jobs_detail(self, course, **kwargs):
        return request.render("courses.detail", {
            'course': course,
            'main_object': course,
        })
