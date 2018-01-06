# -*- coding: utf-8 -*-
import json
import sys
import os
import re

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
    #print "Querem adaptar <%s>" % formatoOriginal

    # Cadeas para obtero numeral de mês
    meses=['Janeiro','Fevereiro',u'Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

    # regex para obteros dados
    #print re.match(r"\n\t\t(?P<feira>\S*), (?P<dia>[0-9]*) (?P<mes>\S*) (?P<ano>[0-9]*) (?P<hora>[0-9]*):(?P<minuto>[0-9]*)",formatoOriginal).groupdict()
    formatado = re.match(r"\n\t\t(?P<feira>\S*), (?P<dia>[0-9]*) (?P<mes>\S*) (?P<ano>[0-9]*) (?P<hora>[0-9]*):(?P<minuto>[0-9]*)",formatoOriginal)

    # obtemos o numeral do mes
    if formatado.group('mes') in meses:
        mes=meses.index(formatado.group('mes'))+1
    else:
        print "Error obtendo numeral de %s" % formatado.group('mes')
        exit(1)

    if formatado:
        """
        print "Feira: %s" % formatado.group('feira')
        print "Mês: %s" % formatado.group('mes').encode('ascii','ignore')
        print "Dia: %s" % formatado.group('dia')
        print "Ano: %s" % formatado.group('ano')
        print "Hora: %s" % formatado.group('hora')
        print "Minuto: %s" % formatado.group('minuto')
        """
        formatoAdaptado= "%s-%02i-%s %s:%s:00" % (formatado.group('ano'),mes,formatado.group('dia'),formatado.group('hora'),formatado.group('minuto'))
        #print "FormatoAdaptado <%s>" % formatoAdaptado
        return formatoAdaptado
    else:
        print "Error no formatado"

"""
chama a wp-cli para publicar um item
"""
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
    items += " --post_content='%s" % "".join(item['body'])+"'"
    items += " --post_title='"+item['title']+"'"
    # url como name: temos que editar (quitar) a raiz http://pglingua.org/agal/agal-hoje/5838-matias-g-rodrigues-licendiado-em-historia-da-arte-le-preciso-e-e
    items += " --post_name='"+item['url'][item['url'].rfind('/')+1:]+"'"
    items += " --post_modified='"+adaptaDate(item['date'])+"'"
    #print items
    itemsEncoded = u''.join(items).encode('utf-8').strip()
    #print itemsEncoded

    # Chamamos ao wp-cli
    php wp-cli.phar post create --post_type=post --post_status=publish --comment_status=open --ping_status=close --post_date="2013-12-04 19:28:40" --post_content="<p>meu primeiro post automatico</p>" --post_title="Este é o title do meu primeiro post automátcio" --post_name="o-meu-primeiro-post-automatico" --post_modified="2013-12-04 19:28:40"
    os.system("php wp-cli.phar post create --post_type=post --post_status=publish --comment_status=open --ping_status=close" + itemsEncoded)

# publica o json
def publicaJson(jsonToPublish):
    if not os.path.isfile(jsonToPublish):
        print "Nom existe o ficheiro: %s" % jsonToPublish

    jsonData = json.load(open(jsonToPublish))
    print "Temos %i artigos" % len(jsonData)

    # temos len(jsonData) artigos
    #for i in range(len(jsonData)):
    #    publicaPost(jsonData[i])
    publicaPost(jsonData[0])


if __name__ == "__main__":
    print '\nTemos %i argumentos' % len(sys.argv)
    print 'Argument List:', str(sys.argv)

    if len(sys.argv) != 2:
        print "\nMoinante! aguardo:\n %s ficheiro.json\n" % sys.argv[0]
        exit(1)

    publicaJson(sys.argv[1])
    exit(0)
