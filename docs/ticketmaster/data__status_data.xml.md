# Pre-creates records for ticket statuses

[Doclink](https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html)

Defines **6** records to pre-create to use in tickets as the `status` flag.

These pre-defiend status models can easilt be retrieved using `self.env.ref('ticketmaster.status_x')`.

If a status gets deleted, the above call might throw an error. This can be fixed with the `raise_if_not_found = False` argument

Statuses:

| Name        | Code                |
| ----------- | ------------------- |
| Open        |  status_open        |
| In Progress |  status_in_progress |
| Resolved    |  status_resolved    |
| Closed      |  status_closed      |
| Pending     |  status_pending     |
| On Hold     |  status_on_hold     |
