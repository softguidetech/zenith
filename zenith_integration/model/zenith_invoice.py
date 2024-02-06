from odoo import models, fields, api
from odoo.exceptions import UserError


class ZenithInvoice(models.Model):
    _name = 'zenith.invoice'
    _description = 'Zenith Invoice'

    partner_id = fields.Many2one('res.partner', string='Customers')
    agency_name = fields.Char(string='Agency Name')
    date_of_payment = fields.Date(string='Date of Payment')
    payment_amount = fields.Float(string='Payment Amount')
    sale_currency = fields.Many2one('res.currency',string='Sale Currency')
    available_credit_before_payment = fields.Float(string='Available Credit Before Payment')
    credit_currency = fields.Many2one('res.currency',string='Credit Currency')
    available_credit_after_payment = fields.Float(string='Available Credit After Payment')
    payment_registered_by = fields.Char(string='Payment Registered By')
    authorized_credit = fields.Float(string='Authorized Credit')
    authorized_currency = fields.Many2one('res.currency',string='Authorized Credit Currency')
    total_sold = fields.Float(string='Total Sold')
    sold_currency = fields.Many2one('res.currency',string='Sold Currency')
    total_paid = fields.Float(string='Total Paid')
    paid_currency = fields.Many2one('res.currency',string='Paid Currency')
    reference_number = fields.Char(string='Reference Number')
    sales_report = fields.Char(string='Sales Report')
    fop = fields.Char(string='FOP')
    transaction_number = fields.Char(string='Transaction Number')
    is_invoice_sync = fields.Boolean(string='Is Invoice Sync')
    invoice_id = fields.Many2one('account.move', string='Invoice ID')

    def transfer_data_to_customer_invoice(self):
        for rec in self:
            if not rec.invoice_id:
                raise UserError("No associated customer invoice found. Please set the 'Invoice ID' field.")
            rec.invoice_id.write({
                'partner_id': rec.partner_id.id,
                'date': rec.date_of_payment,
                # 'amount': rec.payment_amount,
                # 'currency': rec.sale_currency,
            })
