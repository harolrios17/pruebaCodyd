from odoo import models, fields, api

class VotingProcess(models.Model):
    _name = 'voting.process'
    _description = 'Proceso de Votación'

    name = fields.Char(string='Nombre', required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_process', 'Proceso'),
        ('closed', 'Cerrado')],
        string='Estado', default='draft', required=True)
    candidates = fields.Many2many('res.partner', string='Candidatos')
    votes = fields.One2many('vote', 'voting_process_id', string='Resultados de Votos')

    @api.multi
    def action_confirm(self):
        self.state = 'in_process'

    @api.multi
    def action_close(self):
        self.state = 'closed'

class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_candidate = fields.Boolean(string = 'Es candidato?')