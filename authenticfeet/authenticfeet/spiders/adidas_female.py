from authenticfeet.spiders import AdidasMaleSpider


class AdidasFemaleSpider(AdidasMaleSpider):
    start_urls =["https://www.authenticfeet.com.br/feminino/adidas/T%C3%AAnis"]
    name = 'authenticfeet-adidas-female'