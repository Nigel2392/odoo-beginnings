# Creates a mail alias

This file tells odoo's routing engine that emails sent to `support@...` should be directed to the `ticketmaster.ticket` mdoel.

The model must(?) inherit from `mail.thread` for this alias to have any effect.
