from authenticfeet.spiders import AdidasMaleSpider


class NikeMaleSpider(AdidasMaleSpider):
    start_urls =["https://www.authenticfeet.com.br/masculino/nike/T%C3%AAnis"]
    name = 'authenticfeet-nike-male'