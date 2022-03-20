
░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------

# Web crawler

url: [https://www.authenticfeet.com.br/](https://www.authenticfeet.com.br/)

# 1. Configuration
Before you run this project and for the proper running of this program you need to set up some variables inside `authenticfeet/authenticfeet/settings.py`.
## 1.1 SENTRY
This project utilizes [SENTRY](https://sentry.io/) for error tracking.

- `SENTRY_DSN`
- `SPIDERMON_SENTRY_PROJECT_NAME`
- `SPIDERMON_SENTRY_ENVIRONMENT_TYPE`

## 1.2 GOOGLE CLOUD PLATFORM

- `GCS_PROJECT_ID` 
- `GCP_CREDENTIALS`
- `GCP_STORAGE`
- `GCP_STORAGE_CRAWLER_STATS`
- `IMAGES_STORE`

## 1.3 DISCORD
- `DISCORD_WEBHOOK_URL`
- `DISCORD_THUMBNAIL_URL`
- `SPIDERMON_DISCORD_WEBHOOK_URL`

# 2. Implemented Brands
- authenticfeet-adidas-male [`AdidasMaleSpider`]
- authenticfeet-adidas-female [`AdidasFemaleSpider`]
- authenticfeet-adidas-kids [`AdidasKidsSpider`]
- authenticfeet-nike-male [`NikeMaleSpider`]
- authenticfeet-nike-female [`NikeFemaleSpider`]
- authenticfeet-nike-kids [`NikeKidsSpider`]

# 3. Build

```shell
cd authenticfeet
make docker-build-production
```

# 4. Publish

```shell
make docker-publish-production
```

# 5. Use
The parameter `brand` could receive one of the following values: [`authenticfeet-adidas-male`, `authenticfeet-adidas-female`, `authenticfeet-adidas-kids`, `authenticfeet-nike-male`,    `authenticfeet-nike-female`, `authenticfeet-nike-kids`].

```shell
docker run gcr.io/cotatenis/cotatenis-crawl-authenticfeet:0.4.1 --brand=authenticfeet-adidas-male
```
