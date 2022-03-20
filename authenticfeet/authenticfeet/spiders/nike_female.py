from authenticfeet.spiders import AdidasMaleSpider


class NikeFemaleSpider(AdidasMaleSpider):
    start_urls =["https://www.authenticfeet.com.br/feminino/nike/T%C3%AAnis?O=OrderByPriceASC&PS=24"]
    name = 'authenticfeet-nike-female'