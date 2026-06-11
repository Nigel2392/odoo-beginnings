from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Ticket(models.Model):
    _name = "ticketmaster.ticket"
    _description = """Support Ticket"""
    
    @api.model
    def _default_status(self):
        return self.env.ref('ticketmaster.status_open').id

    title = fields.Char(
        string=_("Title"),
        required=True,
    )
    description = fields.Text(
        string=_("Description"),
        required=True,
    )
    date = fields.Date(
        string=_("Date Created"),
        default=fields.Date.today,
    )
    status_id = fields.Many2one(
        "ticketmaster.status",
        string=_("Status"),
        default=_default_status,
    )
    user_id = fields.Many2one(
        "res.users",
        string=_("User"),
        default=lambda self: self.env.user.id,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string=_("Partner"),
        default=lambda self: self.env.user.partner_id.id,
    )
       
    def action_close_ticket(self):
        for ticket in self:
            if ticket.status_id.code != 'resolved':
                raise UserError(_("You can only close resolved tickets."))