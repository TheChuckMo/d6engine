from d6engine.resource.base import CharacterEntry
import pytest
import random

count: int = 4
entry_value_strings = [f'An answer {x + 1}' for x in range(0, count)]
entry_value_numbers = [random.randint(1, 6) for x in range(0, count)]


@pytest.fixture(scope='module', params=entry_value_strings)
def character_entry_strings(request):
    return {'entry_label': f'Entry {request.param}', 'entry_value': f'{request.param}'}


@pytest.fixture(scope='module', params=entry_value_numbers)
def character_entry_numbers(request):
    return {'entry_label': f'Entry {request.param}', 'entry_value': int(request.param)}


class TestCharacterEntry:
    """unit tests of CharacterEntry"""

    def test_string_entry(self, character_entry_strings):
        entry = CharacterEntry(**character_entry_strings)
        assert entry.label is character_entry_strings.get('entry_label')
        assert entry.value is character_entry_strings.get('entry_value')

    def test_number_entry(self, character_entry_numbers):
        entry = CharacterEntry(**character_entry_numbers)
        assert entry.label is character_entry_numbers.get('entry_label')
        assert entry.value == character_entry_numbers.get('entry_value')

    # todo add test to verify message format and system (api not consistent yet)
    # def test_message(self, data):
    #     pass
