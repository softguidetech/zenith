from odoo import models, fields

class CreditLimit(models.Model):
    _name = 'credit.limit'
    _description = 'Credit Limit'

    date = fields.Date(string='Date', required=True)
    customer_id = fields.Char(string='Customer ID')
    agency_name = fields.Char(string='Agency Name')
    date_of_payment = fields.Char(string='Date of payment')
    payment_amount = fields.Char(string='Payment amount (Sale currency)')
    sale_currency = fields.Char(string='Sale currency')
    available_credit_before = fields.Char(string='Available credit before payment (incl. authorized credit)')
    currency_before = fields.Char(string='Currency Before')
    available_credit_after = fields.Char(string='Available credit after payment (incl. authorized credit)')
    currency_after = fields.Char(string='Currency After')
    payment_registered = fields.Char(string='Payment registered by')
    autherized_credit = fields.Char(string='Authorized credit (credit limit)')
    currency_credit = fields.Char(string='Currency Credit')
    total_sold = fields.Char(string='Total sold')
    sold_currency = fields.Char(string='Sold Currency')
    total_paid = fields.Char(string='Total Paid')
    total_paid_currency = fields.Char(string='Total Paid Currency')
    reference_number = fields.Char(string='Reference number')
    sales_report = fields.Char(string='Sales report')
    fop = fields.Char(string='FOP')
    transaction_number = fields.Char(string='Transaction number')
