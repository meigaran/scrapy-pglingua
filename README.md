# scrapy-pglingua

Aranha para exportar os artigos do antigo pgl (2008-2014)

Executa launcer.sh para começar a descarga

Ao correr cria uma pasta 'assets' com o conteudo multimédia:
.
├── assets
│   ├── files
│   └── images

Também criará os ficheiros na raiz com o log e os post obtidos

├── pglingua.json
├── pglingua.log


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

TODOS:
 - Só descarrega um par de secçoes, há que engadir mais url na lista start_urls
 - apanhar os pés dos médias
 - apanhar o resumo das entrevistas de agal-hoje
 - Dividir por secçoes (em diferentes .json de baixada) ou fazer este processado no script de subida ao wordpress a partir de um só .json?


Uma vez rematado, subir os ficheiros ao servidor:
├── assets
│   ├── files
│   └── images
├── postArtigos.py
└── pglingua.json

E correr:
python postArtigos.py pglingua.json

Temos que ter instalado wp-cli https://github.com/wp-cli/wp-cli no Wordpress de destino
