from odoo import api, fields, models

class MusicalGenre(models.Model):
    _name = 'musical.genre'
    _description = 'Géneros'

    name = fields.Char("Género")