from odoo import models, fields

class AircraftAircraft(models.Model):
    _name = 'aircraft.aircraft'
    _description = 'Aircraft'
    _rec_name = 'aircraft_registration'

    aircraft_registration = fields.Char(string='Aircraft Registration')
    aircraft_type = fields.Char(string='Aircraft Type')
    seat_configuration_eco = fields.Char(string='Seat Configuration (Y)')
    seat_configuration_bus = fields.Char(string='Seat Configuration (C)')
    aircraft_mtow = fields.Float(string='Aircraft MTOW / KG')