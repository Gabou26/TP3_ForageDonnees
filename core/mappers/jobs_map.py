import logging

JOBS_MAP = {
    ' State-gov': 0,
    ' Federal-gov': 0,
    ' Local-gov': 0,
    ' Self-emp-not-inc': 1,
    ' Self-emp-inc': 1,
    ' Private': 2,
    ' Without-pay': 3,
    ' Never-worked': 3,
    ' ?': 4
}

JOBS_TAG = [
    ('Government', 0),
    ('Self-employed', 1),
    ('Company', 2),
    ('No job', 3),
    (None, None)
]

def string_to_tag(value):
    """Converts a string from the data frame to a tag number"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        res = JOBS_TAG[JOBS_MAP[value]][1]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error(err)

def tag_to_string(value):
    """Converts a tag number to a readable string"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        # Ugly reversal :(
        res = JOBS_TAG[value][0]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError:
        logger.error("Key [%s] does not exists", value)