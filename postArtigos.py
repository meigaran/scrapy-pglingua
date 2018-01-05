# -*- coding: utf-8 -*-
import json
import sys
import os

"""
Publica os artigos de um .json (e a pasta assets com os mídia)
"""


"""
* scrapy lee do pgl a data:
    "date": "\n\t\tSegunda, 17 Fevereiro 2014 00:00\t"

* wordpress aguarda:
    2013-12-04 19:28:40
"""
def adaptaDate(formatoOriginal):
    print "Querem adaptar <%s>" % formatoOriginal
    meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    mes=0
    for i in range(len(meses)):
        if str(formatoOriginal).find(meses[i]) > 0:
            mes=i+1
    if mes == 0:
        print "Error! nom consego adaptar <%s>" % formatoOriginal
        exit(3)

    print "Mes: %i" % mes

    return "1-2-3-4-5-6"

# chama a
def publicaPost(item):
    # Campos necessários para o wp-cli
    # post_author
    # post_date
    # post_content
    # post_title
    # post_status publish
    # comment_status open
    # ping_status close ?
    # post_name  carme-saborido-professora-do-curso-on-line-falarmos-brasil-o-leque-de-possibilidades-e-imenso-num-pais-continental-como-o-brasil
    # post_modified

    # Fazemos os items
    items = ""
    # TODO: adaptar o formato da data "Sexta, 25 Outubro 2013 00:00" a "2013-12-04 19:28:40"
    items += " --post_date='"+adaptaDate(item['date'])+"'"
    items += " --post_content='%s" % "".join(item['body'])
    items += " --post_title='"+item['title']+"'"
    # url como name: temos que editar (quitar) a raiz http://pglingua.org/agal/agal-hoje/5838-matias-g-rodrigues-licendiado-em-historia-da-arte-le-preciso-e-e
    items += " --post_name='"+item['url'][item['url'].rfind('/')+1:]+"'"
    items += " --post_modified='"+adaptaDate(item['date'])+"'"

    print items

    # Chamamos ao wp-cli
    #os.system("php wp-cli.phar post create --post_type=post --post_status=publish --comment_status=open --ping_status=close" + items

# publica o json
def publicaJson(jsonToPublish):
    if not os.path.isfile(jsonToPublish):
        print "Nom existe o ficheiro: %s" % jsonToPublish

    jsonData = json.load(open(jsonToPublish))
    print "Temos %i artigos" % len(jsonData)
    # temos len(jsonData) artigos
    #for i in range(len(jsonData)):
    #    print str(i)+": "+jsonData[i]['head']+"; date: "+jsonData[i]['date']

    publicaPost(jsonData[0])
        #php wp-cli.phar



if __name__ == "__main__":
    print '\nTemos %i argumentos' % len(sys.argv)
    print 'Argument List:', str(sys.argv)

    if len(sys.argv) != 2:
        print "\nMoinante! aguardo:\n %s ficheiro.json\n" % sys.argv[0]
        exit(1)

    publicaJson(sys.argv[1])
    exit(0)
