#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'Profesor de escuela'

    name = fields.Char()
    edad = fields.Integer()



class Alumno(models.Model):
    _name = 'escuela.alumno'
    _description = 'Alumno escuela'
    
    name = fields.Char()
    edad = fields.Integer()

