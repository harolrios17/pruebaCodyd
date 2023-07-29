{
    'name': 'Gestión de Votaciones',
    'version': '1.0',
    'summary': 'Módulo para gestionar procesos de votación con candidatos y resultados de votos.',
    'category': 'Human Resources',
    'author': 'Harol Rios',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/voting_process_views.xml',
        'views/candidate_views.xml',
        'views/vote_views.xml',
    ],
    'installable': True,
    'application': True,
}