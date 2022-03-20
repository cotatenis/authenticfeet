from authenticfeet.spiders import AdidasMaleSpider


class NikeKidsSpider(AdidasMaleSpider):
    start_urls =["https://www.authenticfeet.com.br/infantil/nike/T%C3%AAnis"]
    name = 'authenticfeet-nike-kids'