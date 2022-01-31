import ..review import BaseCharacter, Mage

b0 = BaseCharacter('Rico')
m0 = Mage('Mirlin')


def test_temp_level_one():
    assert b0.level == 1


def test_temp_level_is_int():
    assert isinstance(b0.level, int)

def test_mage_health_and_resource():
    assert hasattr(m0, 'health')
    assert hasattr(m0, 'mana')

def test_mage_greater_stats():
    assert b0.intel < m0.intel
    assert b0.stam < m0.stam

def test_level_up():
    assert b0.level < b0.level_up().level
    assert m0.level < m0.level_up().level