import enum

class ItemType(str, enum.Enum):
    SUPPLIE = "supplie"
    DEVELOPMENT = "development"
    VALUABLE = "valuable"
    RESOURCE = "resource"
    MISSION = "mission"
    