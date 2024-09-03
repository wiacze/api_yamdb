NAME_LENGTH = 256
SLUG_LENGTH = 50
USERFIELDS_LENGTH = 150
EMAIL_LENGTH = 254

EMAIL_YAMDB = 'YaMDB@mail.com'
REGEX = r'^[\w.@+-]+$'

# Адреса для urls.py
REVIEWS = r'titles/(?P<title_id>\d+)/reviews'
COMMENTS = r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments'
