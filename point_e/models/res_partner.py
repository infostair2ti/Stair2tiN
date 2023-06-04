
from .connect_api import get_genre, get_recommed_song
from odoo import api, fields, models






class ResPartner(models.Model):
    _inherit = 'res.partner'

    musical_genre_ids = fields.Many2many("musical.genre",string="Generos")
    musical_songs_ids = fields.Many2many("musical.song",string="Canciones R.",readonly=True)

    def search_genre(self):
        genres = get_genre()
        model_genre = self.env["musical.genre"]
        model_genre.search([]).unlink()
        self.env["musical.song"].search([]).unlink()
        

        vals = [ {
            'name': i
        }
            for i in genres.get("genres",[])]
        model_genre.create(vals)
        
    def search_songs(self):
        if self.musical_genre_ids:
            songs = get_recommed_song(self.musical_genre_ids.mapped("name"))
            vals = [(5,0,0)]
            vals += [(0,0,{'name':i.get("name",""),'link':i.get("href","")})
                     for i in songs.get("tracks",[])]
            self.musical_songs_ids = vals
    
    def write(self,vals):
        res = super(ResPartner,self).write(vals)
        if "musical_genre_ids" in vals:
            self.search_songs()
        return res

