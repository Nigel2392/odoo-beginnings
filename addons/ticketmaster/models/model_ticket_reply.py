from odoo import api, fields, models


class TicketReply(models.Model):
    _name = "ticketmaster.reply"
    _description = """Reply to support ticket"""

    master_id = fields.Many2one("ticketmaster.ticket", string="Ticket", required=True)
    user = fields.Many2one("res.users", string="User", required=True)
    date = fields.Date(string="Date Created", default=fields.Date.today())
    description = fields.Text(string="Description", required=True)
