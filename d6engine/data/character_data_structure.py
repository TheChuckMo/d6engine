d6_character = {
    'control': {
        'id': bytes(),  # Character UUID
        'home': str(),  # Server/Client source
        'owner': str(),  # Username on home of owner
        'code': bytes(),  # Character HASH for verification
    },
    'character': {
        'traits': [  # Born that way - WILL NEVER IMPACT CHARACTER!
            {'name': str(), 'label': str(), 'value': str()},
            {'name': 'name', 'label': 'Name', 'value': 'Character Name'},
            {'name': 'description', 'label': 'Description', 'value': 'Short character description'},
        ],
        'features': [  # Could change, could impact character one-day (target optional and IGNORED for now)
            {'name': str(), 'label': str(), 'value': int(), 'metric': str(), 'target': list()},
            {'name': 'height', 'label': 'Height', 'value': 71, 'metric': 'inches'},
            {'name': 'weight', 'label': 'Weight', 'value': 162, 'metric': 'lbs'}
        ],
        'advancement': [  # Advancement Points - ALL entries required
            {'name': 'adv_points', 'label': 'Advancement Points', 'value': 22},
            {'name': 'atr_points', 'label': 'Attribute Points', 'value': int(), 'cost': int()},
            {'name': 'skl_points', 'label': 'Skill Points', 'value': 2},
            {'name': 'sub_points', 'label': 'Sub Skill Points', 'value': 8}
        ],
        'state': [  # Character state and calculated Values and States - ALL REQUIRED! (no value!)
            {'name': str(), 'label': str(), 'source': list()},
            {'name': 'health', 'label': 'Health',
             'source': ['attributes.strength', 'attributes.dexterity', 'attributes.endurance']},
        ],
        'attributes': [  # Direct impact on character
            {'name': str(), 'label': str(), 'value': int(), 'max': int(), 'min': int(), 'description': str()},
            {'name': 'strength', 'label': 'Strength', 'value': 3, 'max': 6, 'min': 1,
             'description': 'Character Strength'},
            {'name': 'dexterity', 'label': 'Dexterity', 'value': 3, 'max': 6, 'min': 1,
             'description': 'Character Dexterity'},
            {'name': 'chance', 'label': 'Chance', 'value': 3, 'max': 6, 'min': 1, 'description': 'Character Dexterity'},
        ],
        'skills': [  # Character skills (TENTATIVE - skill system not started)
            {'name': str(), 'label': str(), 'value': int(), 'description': str(), 'target': list(),
             'action': str()},
            {'name': 'small_weapon', 'label': 'Small Weapon', 'value': 1, 'description': 'Small weapon skill',
             'target': ['attributes.dexterity'], 'action': 'add'},
        ],
        'equipped': [  # FUTURE: Equipped inventory (JUST IDEA - future scope)
            {'name': str(), 'label': str(), 'type': str(), 'value': int(), 'description': str(), 'target': list(),
             'action': str()},
            {'name': 'pea_shooter', 'label': 'Pea Shooter', 'value': 1, 'description': 'A shooter that shoots peas',
             'target': ['skills.small_weapon'], 'action': 'subtract'},
        ],
        'inventory': [  # FUTURE: Not-Equipped inventory (JUST IDEA - future scope)
            {'name': str(), 'label': str(), 'type': str(), 'value': int(), 'description': str(), 'target': list(),
             'action': str()},
            {'name': 'potato_shooter', 'label': 'Potato Shooter', 'value': 1,
             'description': 'A shooter that shoots potatos',
             'target': ['skills.small_weapon'], 'action': 'add'},
        ],
    },
    'history': {}  # FUTURE: will implement with event system
}
