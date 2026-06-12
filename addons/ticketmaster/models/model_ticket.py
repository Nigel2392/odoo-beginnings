from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Ticket(models.Model):
    _name = "ticketmaster.ticket"
    _description = """Support Ticket"""
    _inherit = ['mail.thread']

    @api.model
    def _default_status(self):
        return self.env.ref('ticketmaster.status_open').id

    title = fields.Char(
        string=_("Title"),
        help=_("The title of the ticket."),
        required=True,
    )
    description = fields.Text(
        string=_("Description"),
        help=_("The description of the ticket."),
        required=True,
    )
    date = fields.Date(
        string=_("Date Created"),
        default=fields.Date.today,
    )
    status_id = fields.Many2one(
        "ticketmaster.status",
        string=_("Status"),
        help=_("The status of the ticket."),
        default=_default_status,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        help=_("The contact who created the ticket."),
        default=lambda self: self.env.user.partner_id.id,
    )
    technician_user_id = fields.Many2one(
        "res.users",
        string=_("Technician"),
        help=_("The technician who will handle the ticket."),
        default=lambda self: self.env.user.id,
    )

