import logging


SCHOLARSHIP_NAME = {
    ' Doctorate': 'Doctorate',
    ' Masters': 'Master',
    ' Bachelors': 'Bachelors',
    ' Some-college': 'High School',
    ' HS-grad': 'High School',
    ' 12th': 'High School',
    ' 11th': 'High School',
    ' 10th': 'High School',
    ' 9th': 'High School',
    ' 7th-8th': 'Elementary School',
    ' 5th-6th': 'Elementary School',
    ' 1st-4th': 'Elementary School',
    ' Preschool': 'Preschool',
    ' Prof-school': None,
    ' Assoc-acdm': None,
    ' Assoc-voc': None
}

SCHOLARSHIP_TAG = {
    'Doctorate': 0,
    'Master': 1,
    'Bachelors': 2,
    'High School': 3,
    'Elementary School': 4,
    'Preschool': 5,
    None: 'NaN'
}

def string_to_tag(value):
    """Maps a value from a string in the dataframe to a number"""
    logger = logging.getLogger("core")

    # logger.debug("Mapping %s", value)
    try:
        res = SCHOLARSHIP_TAG[SCHOLARSHIP_NAME[value]]
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
        res = list(SCHOLARSHIP_TAG.keys())[list(SCHOLARSHIP_TAG.values()).index(value)]
        logger.trace("Mapped value %s", res)
        return res
    except KeyError as err:
        logger.error(err)