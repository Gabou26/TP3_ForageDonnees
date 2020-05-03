import logging

COUNTRIES = ['United-States', 'Cuba', 'Jamaica', 'India', '?', 'Mexico', 'South',
             'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran',
             'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia', 'Thailand',
             'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic',
             'El-Salvador', 'France', 'Guatemala', 'China', 'Japan', 'Yugoslavia',
             'Peru', 'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago',
             'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
             'Holand-Netherlands']

def string_to_tag(value):
    """Converts a string from the dataframe to a tag"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)

    try:
        i = COUNTRIES.index(value.strip())
        logger.trace("Mapped value %d: %s", i, COUNTRIES[i])
        if COUNTRIES[i] == '?':
            logger.trace("Mapped value is '?', returning NaN")
            return None
        return i
    except ValueError as err:
        logger.error(err)

def tag_to_string(value):
    """Converts a tag number to a string"""
    logger = logging.getLogger("core")
    logger.trace("Mapping value %s", value)

    try:
        country = COUNTRIES[value]
        logger.trace("Mapped value %s", country)
        return country
    except IndexError as err:
        logger.error(err)
