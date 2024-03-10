from odoo import fields, models


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Ticket'

    name = fields.Char()
    number = fields.Char()
    tag = fields.Char()
    description = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    active = fields.Boolean(default=True)