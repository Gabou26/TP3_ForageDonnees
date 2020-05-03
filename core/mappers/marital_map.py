import logging

MARITAL_MAP = {
    ' Never-married': 0,
    ' Separated': 0,
    ' Divorced': 1,
    ' Widowed': 1,
    ' Married-spouse-absent': 2,
    ' Married-AF-spouse': 2,
    ' Married-civ-spouse': 2
}

MARITAL_TAG = [
    ('Single', 0),
    ('Was married', 1),
    ('Married', 2)
]

def string_to_tag(value):
    """Converts a string from the data frame to a tag"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        res = MARITAL_TAG[MARITAL_MAP[value]][1]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error("Key [%s] does not exists", err)

def tag_to_string(value):
    """Converts a tag to a readable string"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        # Ugly reversal :(
        res = MARITAL_TAG[value][0]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError:
        logger.error("Key [%s] does not exists", value)
