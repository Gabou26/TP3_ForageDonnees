import logging

[' State-gov' ' Self-emp-not-inc' ' Private' ' Federal-gov' ' Local-gov'
 ' ?' ' Self-emp-inc' ' Without-pay' ' Never-worked']

JOBS_NAME = {
    ' State-gov': 'Government',
    ' Federal-gov': 'Government',
    ' Local-gov': 'Government',
    ' Self-emp-not-inc': 'Self-employed',
    ' Self-emp-inc': 'Self-employed',
    ' Private': 'Company',
    ' Without-pay': 'No job',
    ' Never-worked': 'No job',
    ' ?': None
}

JOBS_TAG = {
    'Government': 0,
    'Self-employed': 1,
    'Company': 2,
    'No job': 3,
    None: 'NaN'
}

def string_to_tag(value):
    """Converts a string from the data frame to a tag number"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        res = JOBS_TAG[JOBS_NAME[value]]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error(err)

def tag_to_string(value):
    """Converts a tag number to a readable string"""
    logger = logging.getLogger("core")
    logger.debug("Mapping value %s", value)
    try:
        # Ugly reversal :(
        res = list(JOBS_TAG.keys())[list(JOBS_TAG.values()).index(value)]
        logger.debug("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error(err)