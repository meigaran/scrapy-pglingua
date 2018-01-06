# Informaçom sobre wp-cli e organizaçom de dados no Wordpress

### wp-cli: Wordpress por comandos
#### Instalar
```
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
php wp-cli.phar --info
chmod +x wp-cli.phar
```

#### Alguns comandos básicos
```
php wp-cli.phar --info
php wp-cli.phar --help
php wp-cli.phar update
php wp-cli.phar config creat
php wp-cli.phar cli update
```

#### Importar BBDD dende um xml
```
php wp-cli.phar install wordpress-importer --activate
php wp-cli.phar import portalgalegodalngua-pglgal.wordpress.2017-12-10.xml --authors=create
```


#### Listar os POSTs
```
php wp-cli.phar post list
php wp-cli.phar post get 26
```

#### TAGs e categories
Num POST, os tags mais os categories nom estam almacenados no próprio POST
```
php wp-cli.phar term list post_tag
php wp-cli.phar term list category
```

O formato de saida pode ser json, csv, ...
```
php wp-cli.phar term list --help
php wp-cli.phar term list category --format=json > category.json
```

#### 'Categorias' atuais:
```
+---------+------------------+---------------------------+---------------------------+-------------+--------+-------+
| term_id | term_taxonomy_id | name                      | slug                      | description | parent | count |
+---------+------------------+---------------------------+---------------------------+-------------+--------+-------+
| 58      | 58               | AGAL                      | agal                      |             | 0      | 304   |
| 1854    | 1854             | AGAL De ontem para amanhã | agal-de-ontem-para-amanha |             | 0      | 3     |
| 12      | 12               | AGAL Hoje                 | agal-hoje                 |             | 0      | 67    |
| 33      | 33               | AGLP                      | aglp                      |             | 0      | 26    |
| 35      | 35               | Análise                   | analise                   |             | 0      | 536   |
| 102     | 102              | As Aulas no Cinema        | as-aulas-no-cinema        |             | 0      | 190   |
| 40      | 40               | Através | Editora         | atraves-editora           |             | 0      | 135   |
| 8       | 8                | Babel                     | babel                     |             | 0      | 17    |
| 132     | 132              | Canal Aberto              | canal-aberto              |             | 0      | 17    |
| 32      | 32               | Crónicas                  | cronicas                  |             | 0      | 27    |
| 249     | 249              | Dia das Letras            | dia-das-letras            |             | 0      | 0     |
| 4       | 4                | Entrevistas               | entrevistas               |             | 0      | 165   |
| 67      | 67               | Espaço Brasil             | espaco-brasil             |             | 0      | 67    |
| 34      | 34               | Especiais                 | especiais                 |             | 0      | 331   |
| 72      | 72               | Eventos                   | eventos                   |             | 0      | 261   |
| 739     | 739              | Foi notícia               | foi-noticia               |             | 0      | 0     |
| 76      | 76               | Formaçom                  | formacom                  |             | 0      | 91    |
| 6       | 6                | Início                    | inicio                    |             | 0      | 1365  |
| 1329    | 1329             | mincinho                  | mincinho                  |             | 0      | 21    |
| 7       | 7                | Notícias                  | noticias                  |             | 0      | 612   |
| 634     | 634              | Novas da Galiza           | novas-da-galiza           |             | 0      | 15    |
| 842     | 842              | O Apalpador               | o-apalpador               |             | 0      | 0     |
| 17      | 17               | Opiniom                   | artigos-de-opiniom        |             | 0      | 354   |
| 981     | 981              | Quinta de Comadres        | quinta-de-comadres        |             | 0      | 0     |
| 351     | 351              | Reportagens               | reportagens               |             | 0      | 22    |
| 1       | 1                | Sem categoria             | sem-categoria             |             | 0      | 2     |
+---------+------------------+---------------------------+---------------------------+-------------+--------+-------+
```
#### 'tags' atuais:
Mirar os ficheiros ./wp-info/post_tag.*

#### De um POST (ID) concreto
```
php wp-cli.phar post term list 187 category
php wp-cli.phar post term list 26 post_tag
```

#### POST de um artigo dende a linha de comandos
```
php wp-cli.phar post create --post_type=post --post_status=publish --comment_status=open --ping_status=close --post_date="2013-12-04 19:28:40" --post_content="<p>meu primeiro post automatico</p>" --post_title="Este é o title do meu primeiro post automátcio" --post_name="o-meu-primeiro-post-automatico" --post_modified="2013-12-04 19:28:40"
```
Uma vez posteado, se foi correto devolve o ID do POST

Para apagá-lo:
```
php wp-cli.phar post delete 13208
```


Temos que apanhar esse ID e fazer os ADDs pertinentes para categorias e tags do artigo
