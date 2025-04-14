import enum

class CharacterRarity(int, enum.Enum):
    PURPLE = 4
    GOLD = 5
    
class Element(str, enum.Enum):
    FUSION = "fusion"
    GLACIO = "glacio"
    AERO = "aero"
    ELECTRO = "electro"
    SPECTRO = "spectro"
    HAVOC = "havoc"

class SkillType(str, enum.Enum):
    ACTIVE = "active"
    PASSIVE = "passive"
    CONCERTO = "concerto"

class SkillCategory(str, enum.Enum):
    BASIC_ATTACK = "basic_attack"
    INTRO = "intro"
    OUTRO = "outro"
    LIBERATION = "liberation"
