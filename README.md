# scrapy-pglingua

Aranha para exportar os artigos do antigo pgl (2008-2014)

## Descarregar os artigos do antigo PGL

Executa launcer.sh para começar a descarga

Ao correr cria uma pasta 'assets' com o conteudo multimédia:
```
├── assets
│   ├── files
│   └── images
```

Também criará os ficheiros na raiz com o log e os post obtidos
```
├── pglingua.json
├── pglingua.log
```

O arquivo json resultante terá os seguintes campos:
 - body []
 - files []
 - head
 - subhead
 - title
 - url
 - image_urls []
 - date
 - author
 - images []

#### Funcionamento
Definir os campos a descarregar (estructura do json resultante) em [./pglingua/items.py](../pglingua/spiders/items.py)

Definir as urls nas que buscar, assim como as regras para cubrir a estructura do json no [./pglingua/spiders/sitepoint.py](./pglingua/spiders/sitepoint.py)

#### TODO:
 - Só descarrega um par de secçoes, há que engadir mais url na lista start_urls
 - apanhar os pés dos médias -> já reconhemos alguns mas os que ficam abaixo de todo é necessário ver como saca-los
 - apanhar o resumo das entrevistas de agal-hoje
 - Dividir por secçoes (em diferentes .json de baixada) ou fazer este processado no script de subida ao wordpress a partir de um só .json?

## Post dos artigos num Wordpress

Uma vez rematado, subir os ficheiros ao servidor:
```
├── assets
│   ├── files
│   └── images
├── postArtigos.py
└── pglingua.json
```

E correr:
python postArtigos.py pglingua.json

#### TODO:
 - Já funciona correctamente a creaçom dos artigos do .json
 - Agora falta ver como ordear o .json, se em vários .json e o POST de eles etiquetem-se de diferente jeito

Temos que ter instalado wp-cli https://github.com/wp-cli/wp-cli no Wordpress de destino

#### +info em [./wp-cli-info.md](./wp-cli-info.md)
