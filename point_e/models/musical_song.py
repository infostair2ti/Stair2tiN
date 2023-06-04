from odoo import api, fields, models

class MusicalSong(models.Model):
    _name = 'musical.song'
    _description = 'Canciones'

    name = fields.Char("Nombre")
    link = fields.Char("Link")