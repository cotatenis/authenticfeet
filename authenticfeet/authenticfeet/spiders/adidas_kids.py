from authenticfeet.spiders import AdidasMaleSpider


class AdidasKidsSpider(AdidasMaleSpider):
    start_urls =["https://www.authenticfeet.com.br/infantil/adidas/T%C3%AAnis"]
    name = 'authenticfeet-adidas-kids'