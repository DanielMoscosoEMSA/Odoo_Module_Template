# -*- coding: utf-8 -*-
from odoo import http

# class Trial(http.Controller):
#     @http.route('/trial/trial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trial/trial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trial.listing', {
#             'root': '/trial/trial',
#             'objects': http.request.env['trial.trial'].search([]),
#         })

#     @http.route('/trial/trial/objects/<model("trial.trial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trial.object', {
#             'object': obj
#         })