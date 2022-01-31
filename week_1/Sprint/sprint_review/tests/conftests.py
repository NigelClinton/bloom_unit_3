import pytest
import ..review import BaseCharacter, Mage

@pytest.fixture()
def template_character():
    return BaseCharacter('Rico')

@pytest.fixture()
def mage_character():
    return BaseCharacter('Merlin')
