import logging


SCHOLARSHIP_MAP = {
    ' Doctorate': 0,
    ' Masters': 1,
    ' Bachelors': 2,
    ' Some-college': 3,
    ' HS-grad': 3,
    ' 12th': 3,
    ' 11th': 3,
    ' 10th': 3,
    ' 9th': 3,
    ' 7th-8th': 4,
    ' 5th-6th': 4,
    ' 1st-4th': 4,
    ' Preschool': 5,
    ' Prof-school': 6,
    ' Assoc-acdm': 6,
    ' Assoc-voc': 6
}

SCHOLARSHIP_TAG = [
    ('Doctorate', 0),
    ('Master', 1),
    ('Bachelors', 2),
    ('High School', 3),
    ('Elementary School', 4),
    ('Preschool', 5),
    (None, None)
]

def string_to_tag(value):
    """Maps a value from a string in the dataframe to a number"""
    logger = logging.getLogger("core")

    # logger.debug("Mapping %s", value)
    try:
        res = SCHOLARSHIP_TAG[SCHOLARSHIP_MAP[value]][1]
        # logger.debug("Mapped value: %s", res)
        return res
    except KeyError as err:
        logger.error(err)

def tag_to_string(value):
    """Maps a number to a string"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)
    try:
        # Ugly reversal :(
        res = SCHOLARSHIP_TAG[value][0]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error(err)
        