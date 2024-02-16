from odoo import models, fields, api

class OperationOperation(models.Model):
    _name = 'operation.operation'
    _description = 'Aviation Operation'
    _rec_name = 'flight_no'

    def _default_value(self):
        # if self.flight_type == 'charter':
        #     return ''
        if self.flight_type != 'charter':
            return 'TARCO AVIATION CO. LTD'
        else:
            return ' '

    from_location = fields.Many2one('airport.airport',string='From')
    to_location = fields.Many2one('airport.airport',string='To')
    flight_no = fields.Char(string='Flight Number')
    flight_date = fields.Date(string='Flight Date', required=True)
    aircraft_id = fields.Many2one('aircraft.aircraft',string='Aircraft Registration')
    aircraft_type = fields.Char(related='aircraft_id.aircraft_type',string='Aircraft Type')
    flight_type = fields.Selection([('schedule','Schedule'),
                                    ('additional','Additional'),
                                    ('hajj','Hajj'),
                                    ('charter','Charter'),
                                    ('others','Others')],string='Flight Type')
    customer = fields.Char(string='Customer',default=_default_value)
    line_ids = fields.One2many('operation.operation.line','operation_id',string=' ')
    aircraft_mtow = fields.Float(related='aircraft_id.aircraft_mtow',string='Aircraft MTOW / KG')
    passenger_business = fields.Float(string='Passenger Business')
    passenger_economy = fields.Float(string='Passenger economy')
    chock_off = fields.Float(string='Chock off')

    std = fields.Float(string='STD')
    sta = fields.Float(string='STA')
    # atd = fields.Float(string='Actual Time Departure (ATD)')
    # ata = fields.Float(string='Actual Time Arrival (ATA)')
    chock_on = fields.Float(string='Chock On')
    landing = fields.Float(string='Landing')
    chock_off = fields.Float(string='Chock Off')
    airborne = fields.Float(string='Airborne')
    flight_time = fields.Float(string='Flight Time',compute='_flight_time')
    block_time = fields.Float(string='Block Time',compute='_block_time')
    state = fields.Selection([('draft','draft'),
                              ('submitted','Submitted')],default='draft',)
    cargo_line_ids = fields.One2many('cargo.cargo.line','cargo_operation_id',string=' ')


    @api.depends('landing','airborne')
    def _flight_time(self):
        if self.airborne > self.landing:
            cal = 24 - self.landing
            self.flight_time = cal - self.airborne
        else:
            self.flight_time = self.landing - self.airborne

    @api.depends('chock_on','chock_off')
    def _block_time(self):
        if self.chock_off > self.chock_on:
            cal = 24 - self.chock_off
            self.block_time = cal - self.chock_on
        else:
            self.block_time = self.chock_on - self.chock_off

    def submit(self):
        for rec in self:
            rec.state = 'submitted'


class OperationLine(models.Model):
    _name = 'operation.operation.line'

    crew_id = fields.Many2one('crew.crew',string='Crew First Name',required=True)
    operation_id = fields.Many2one('operation.operation',string='Operation')
    passport_no = fields.Char(related='crew_id.passport_no',string='Passport Number')
    job_id = fields.Many2one(related='crew_id.job_id',string='Position on flight')
    position_name = fields.Selection([('Captain','Captain'),
                                      ('First Officer','First Officer'),
                                      ('Flight Perusal', 'Flight Perusal'),
                                      ('Cabin Crew', 'Cabin Crew'),
                                      ('Engineer', 'Engineer'),
                                      ('Security','Security'),
                                      ('SNY','SNY'),
                                      ('Dispatcher', 'Dispatcher'),
                                      ('Traffic Officer','Traffic Officer')],string='Position on Flight')
    nationality_id = fields.Many2one(related='crew_id.nationality_id',sting='Nationality')
    dob = fields.Date(related='crew_id.dob',sting='Date of Birth')
    gender = fields.Selection(related='crew_id.gender',sting='Sex')



class CargoCargo(models.Model):
    _name = 'cargo.cargo.line'

    awb_number = fields.Char(string='AWB Number')
    number_of_pieces = fields.Integer(string='Number of Pieces')
    total_weight = fields.Float(string='Total Weight')
    nature = fields.Char(string='Nature')
    cargo_operation_id = fields.Many2one('operation.operation',string='Operation')

    def holds(self):
        pass