import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from math import ceil
from urllib.parse import urljoin
from scrapy.utils.project import get_project_settings
from authenticfeet.items import AuthenticFeetAdidasItem
import re
class AdidasMaleSpider(scrapy.Spider):
    name = 'authenticfeet-adidas-male'
    allowed_domains = ['www.authenticfeet.com.br']
    start_urls = ['https://www.authenticfeet.com.br/masculino/adidas/T%C3%AAnis']
    PAGINATION_PREFIX = "https://www.authenticfeet.com.br/"
    settings = get_project_settings()
    version = settings.get("VERSION")
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, method='GET', callback=self.results_page, cb_kwargs={'page_number' : 1})
    
    def results_page(self, response, page_number: int):
        if page_number == 1:
            #get total number of products
            num_results = int(response.xpath("//span[@class='resultado-busca-numero']/span[@class='value']/text()").get())
            #this result page for default shows 24 products per page
            total_num_pages = ceil(num_results/24)

            product_details = LinkExtractor(restrict_xpaths="//div[@class='ns-product-item']//a[@class='ns-product-item-cover']")
            for url in [data.url for data in product_details.extract_links(response)]:
                yield Request(url=url, method='GET', callback=self.parse_products)

            #create a list to holds the page numbers to visit
            pags_to_visit = [pag for pag in range(2, total_num_pages+1)]
            BASE_PAGINATION_URL = "".join(response.xpath("//script").re(r"/buscapagina\?.+")).split("+")[0][:-2] 
            for pagination in pags_to_visit:
                pagination_url = f"{urljoin(self.PAGINATION_PREFIX,BASE_PAGINATION_URL)}{pagination}"
                yield Request(url=pagination_url, method="GET", callback=self.results_page, cb_kwargs={'page_number' : int(pagination)})
        else:
            product_details = LinkExtractor(restrict_xpaths="//div[@class='ns-product-item']//a[@class='ns-product-item-cover']")
            for url in [data.url for data in product_details.extract_links(response)]:
                yield Request(url=url, method='GET', callback=self.parse_products)

    def parse_products(self, response):
        skuId = response.xpath("//input[@id='___rc-p-sku-ids']/@value").get()
        if skuId:
            skuId = skuId.split(',')[0]
            headers = self.settings.get("ENDPOINT_HEADERS")
            headers['referer'] = response.url
            url = f"https://www.authenticfeet.com.br/api/catalog_system/pub/products/search?&fq=skuId:{skuId}"
            yield Request(url=url, method='GET', dont_filter=True, headers=headers, callback=self.parse)

    def parse(self, response):
        data = self.parse_item(response=response)
        if data:
            yield data

    def parse_item(self, response):
        data = response.json()[0]
        if data:
            sku = data['productReference'].replace("-","")[:6]
            data['sku'] = sku
            image_urls = set()
            items = data.get("items")
            for item in items:
                images_data = item.get("images")
                for image_data in images_data:
                    image_url = image_data.get("imageUrl")
                    image_urls.add(image_url)
            data['image_urls'] = list(image_urls)
            data['image_uris'] = self.fetch_image_uris(image_urls=data['image_urls'], sku=sku)
            data['reference_first_image'] = [v for v in data['image_uris'] if re.search("-[A-Za-z]+(.jpg|.png)", v)]
            data['spider'] = self.name
            data['spider_version'] = self.version
            tipo_produto = data.get("Tipo de Produto", None)
            if tipo_produto:
                del data['Tipo de Produto']
                data['TipodeProduto'] = tipo_produto
            lancamento_calendario = data.get("Lançto Calendário", None)
            if lancamento_calendario:
                del data['Lançto Calendário']
                data['LanctoCalendario'] = lancamento_calendario
            cod_ref_multi_var = data.get("Cod. Ref. Multi Var.", None)
            if cod_ref_multi_var:
                del data['Cod. Ref. Multi Var.']
                data['CodRefMultiVar'] = cod_ref_multi_var
            cod_ref_variacao = data.get("Cod. Ref. Variação", None)
            if cod_ref_variacao:
                del data['Cod. Ref. Variação']
                data['CodRefVariacao'] = cod_ref_variacao
            lancamento_mundial = data.get("Lançto Mundial", None)
            if lancamento_mundial:
                del data['Lançto Mundial']
                data['LanctoMundial'] = lancamento_mundial 
            black_friday = data.get("Black Friday", None)
            if black_friday:
                del data['Black Friday']
                data['BlackFriday'] = black_friday
            data['spider_version'] = self.version
            data['spider'] = self.name
            if set(data.keys()).difference(set(AuthenticFeetAdidasItem.fields.keys())):
                return data
            else:
                return AuthenticFeetAdidasItem(**data)
        else:
            return None

    def fetch_image_uris(self, image_urls, sku):
        image_uris = []
        for image in image_urls:
            rawi = image.split("?")[-2].split("/")[-1]
            fname = f"{self.settings.get('IMAGES_STORE')}{sku}_{rawi}"
            image_uris.append(fname)
        return image_uris