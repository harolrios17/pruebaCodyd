from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    @api.model
    def create(self, vals):
        voting_process_id = vals.get('voting_process_id')
        if voting_process_id:
            voting_process = self.env['voting.process'].browse(voting_process_id)
            if voting_process.state != 'in_process':
                raise ValidationError('La votación no está en "Proceso". No se puede votar.')

            voter_id = vals.get('voter')
            if voter_id:
                existing_vote = self.search([('voter', '=', voter_id), ('voting_process_id', '=', voting_process_id)])
                if existing_vote:
                    raise ValidationError('Ya se registró un voto para este sufragante.')

        return super(Vote, self).create(vals)