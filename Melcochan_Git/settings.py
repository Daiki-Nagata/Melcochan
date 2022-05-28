from os import environ

SESSION_CONFIGS = [
    dict(
        name='Melcochan_firstexp_con',
        display_name='Melcochan_firstexp_con',
        num_demo_participants=1,
        app_sequence=['Melcochan_firstexp_con_prc', 'Melcochan_firstexp_con_main', 'Melcochan_firstexp_con_survey', 'payment_info'],
    ),
        dict(
        name='trust',
        display_name='trust',
        num_demo_participants=2,
        app_sequence=['trust', 'payment_info'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7)q9wtm)3(%m5$+d5_rpzgxme)wno#*+91ho#kk-$=z=rdit25'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
