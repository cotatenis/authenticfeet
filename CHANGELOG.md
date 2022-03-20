# Change Log
Arquivo para documentação das mudanças realizadas ao longo do projeto. O formato desse arquivo é baseado no [Keep a Changelog](http://keepachangelog.com/)
e o presente projeto adota o [Semantic Versioning](http://semver.org/).

## [0.4.1] - 2021-11-17
- [COT-372](https://ecoanalytics.atlassian.net/browse/COT-372)
### Alterado
- Atualizado a variável `DISCORD_THUMBNAIL_URL`.

## [0.4.0] - 2021-11-17
- [COT-396](https://ecoanalytics.atlassian.net/browse/COT-396)
### Adicionado
- Sobrescrito a função `image_downloaded` do objeto `ImagesPipeline` para garantir a persistência de apenas imagens que ainda não estão salvas no storage.

## [0.3.0] - 2021-11-09
### [COT-335](https://ecoanalytics.atlassian.net/browse/COT-335)
#### Adicionado
- Adicionado as spiders `NikeFemaleSpider`, `NikeKidsSpider`, `NikeMaleSpider`.
#### Removido
- Removido a persistência de imagens no tamanho 800x600.
#### Alterado
- Alterado o XPATH que mapeia os produtos no resultado de busca.

## [0.2.0] - 2021-10-09
### [COT-203](https://ecoanalytics.atlassian.net/browse/COT-203)
#### Adicionado
- Adicionado a feature `reference_first_image` ao objeto `AuthenticFeetAdidasItem`.
#### Alterado
- Alterado a configuração `IMAGES_THUMBS` para salvar imagens no padrão 400x400.

## [0.1.1] - 2021-10-09
### [COT-193](https://ecoanalytics.atlassian.net/browse/COT-143)

