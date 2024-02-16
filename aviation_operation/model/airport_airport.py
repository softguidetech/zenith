from odoo import models, fields

class AirportAirport(models.Model):
    _name = 'airport.airport'
    _description = 'Airports'
    # _rec_name = 'airport_name'

    name = fields.Char(string='Airport Name')
    iata_code = fields.Char(string='IATA Code')
    icao_code = fields.Char(string='ICAO Code')
    city_id = fields.Many2one('res.country.state',string='City')
    country_id = fields.Many2one('res.country',string='Country')
