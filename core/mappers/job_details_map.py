import logging

DETAILS_MAP = {
    ' Adm-clerical': 0,
    ' Exec-managerial': 1,
    ' Handlers-cleaners': 2,
    ' Prof-specialty': 3,
    ' Other-service': 4,
    ' Sales': 5,
    ' Craft-repair': 6,
    ' Transport-moving': 7,
    ' Farming-fishing': 8,
    ' Machine-op-inspct': 9,
    ' Tech-support': 10,
    ' Protective-serv': 11,
    ' Armed-Forces': 12,
    ' Priv-house-serv': 13,
    ' ?': 14
}

DETAILS_TAG = [
    ('Clearical', 0),
    ('Manager', 1),
    ('Cleaner', 2),
    ('Specialist', 3),
    ('Other', 4),
    ('Sales', 5),
    ('Mechanic', 6),
    ('Logistic', 7),
    ('Farmer-Fisher', 8),
    ('Machine operator', 9),
    ('Tech-support', 10),
    ('Protection', 11),
    ('Armed forces', 12),
    ('House servant', 13),
    (None, None)
]

def string_to_tag(value):
    """Converts a string from the data frame to a tag"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        res = DETAILS_TAG[DETAILS_MAP[value]][1]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError:
        logger.error("Key [%s] does not exists", value)
