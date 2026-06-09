from odoo import api, fields, models


class TicketStatus(models.Model):
    _name = "ticketmaster.status"
    _description = """Status for support ticket"""