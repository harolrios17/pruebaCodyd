from odoo import models, fields

class Vote(models.Model):
    _name = 'vote'
    _description = 'Voto'

    voter = fields.Many2one('res.partner', string='Votante', required=True)
    candidate = fields.Many2one('res.partner', string='Candidato', required=True)
    voting_process_id = fields.Many2one('voting.process', string='Proceso de Votación', required=True)
    unique_vote = fields.Boolean(string='Voto Único', compute='_compute_unique_vote', store=True)

    @api.depends('voter', 'voting_process_id')
    def _compute_unique_vote(self):
        for record in self:
            if record.voter and record.voting_process_id:
                domain = [('voter', '=', record.voter.id), ('voting_process_id', '=', record.voting_process_id.id)]
                existing_votes = self.search_count(domain)
                record.unique_vote = existing_votes == 0
            else:
                record.unique_vote = False