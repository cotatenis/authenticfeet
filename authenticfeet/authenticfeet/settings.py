BOT_NAME = 'authenticfeet'
VERSION = "0-4-1"
SPIDER_MODULES = ['authenticfeet.spiders']
NEWSPIDER_MODULE = 'authenticfeet.spiders'

ROBOTSTXT_OBEY = False

ENDPOINT_HEADERS = {
    "authority": "www.authenticfeet.com.br",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "sec-ch-ua-platform": "\"Linux\"",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

MAGIC_FIELDS = {
    "timestamp": "$isotime",
    "spider": "$spider:name",
    "url": "$response:url",
}
SPIDER_MIDDLEWARES = {
    "scrapy_magicfields.MagicFieldsMiddleware": 100,
}
#SPIDERMON
SPIDERMON_ENABLED = True
EXTENSIONS = {
    'authenticfeet.extensions.SentryLogging' : -1,
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}
ITEM_PIPELINES = {
    "authenticfeet.pipelines.DiscordMessenger" : 100,
    "authenticfeet.pipelines.AuthenticFeetImagePipeline" : 200,
    "authenticfeet.pipelines.GCSPipeline": 300,
}
SPIDERMON_SPIDER_CLOSE_MONITORS = (
'authenticfeet.monitors.SpiderCloseMonitorSuite',
)

SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = False
SPIDERMON_CUSTOM_MIN_ITEMS = {
    'authenticfeet-adidas-male' : 130,
    'authenticfeet-adidas-kids' : 70,
    'authenticfeet-adidas-female' : 100,
    'authenticfeet-nike-male' : 500,
    'authenticfeet-nike-female' : 400,
    'authenticfeet-nike-kids' : 100,
}
SPIDERMON_PERIODIC_MONITORS = {
'authenticfeet.monitors.PeriodicMonitorSuite': 30, # time in seconds
}
SPIDERMON_MIN_ITEMS = 170
SENTRY_DSN = ""
SPIDERMON_SENTRY_PROJECT_NAME = ""
SPIDERMON_SENTRY_ENVIRONMENT_TYPE = ""
#THROTTLE
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 5

#GCP
GCS_PROJECT_ID = ""
GCP_CREDENTIALS = ""
GCP_STORAGE = ""
GCP_STORAGE_CRAWLER_STATS = ""
#FOR IMAGE UPLOAD
IMAGES_STORE = f''
IMAGES_THUMBS = {
    '400_400': (400, 400),
}
#DISCORD
DISCORD_WEBHOOK_URL = ""
DISCORD_THUMBNAIL_URL = ""
SPIDERMON_DISCORD_WEBHOOK_URL = ""

#LOGGING
LOG_LEVEL = 'INFO'