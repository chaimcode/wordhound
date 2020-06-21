import click
from crawler import WebCrawler
from selenium import webdriver
import tfidf
from sys import exit
from urlparse import urlparse
from nltk.tokenize import wordpunct_tokenize

@click.command()
@click.argument('url')
@click.option('--outputcandidates', default=200, help='How many password candidates should be returned')
@click.option('--outputfile', help='Where should the results be stored')
@click.option('--maxdepth', default=2, help='How many layers deep should the crawler go')
@click.option('--contentfile',help='Instead of crawling a given URL, use a text file with previously crawled data or an arbitrary text file.')
@click.option('--maxprocesses',default=5,help='How many processes to use for scraping')
@click.option('--urlfilter',default='\.(jpg|jpeg|gif|png|js|css|swf|xml)$',help='''Set a python regex to exclude certain URLs. Default is '\.(jpg|jpeg|gif|png|js|css|swf|xml)$' ''')


def main(url, outputcandidates, outputfile,  maxdepth, contentfile, maxprocesses, urlfilter):  
    try:
        urlparse(url)
    except:
        print "[!] URL not valid."
        sys.exit()
    if contentfile:
        content = open(contentfile, 'rb')
        target_text = content.read()
        content.close()
    else:
        #Instantiate web crawler
        crawler = WebCrawler(url,  maxdepth, maxprocesses, urlfilter)
        target_text = crawler.collected_data.lower()      

    #Tokenize the string
    target_words = wordpunct_tokenize(target_text)

    #Initialise the TF-IDF model
    tfidf_model = tfidf.tdidf()
    final_words = tfidf_model.top_words(outputcandidates, target_words)


    if not outputfile:
        outputfile = urlparse(url).netloc
    output = open(urlparse(url).netloc, 'wb')
    for i in final_words:
        output.write(u''.join(i[0]).encode('utf-8').strip()+ '\n')
    output.close()
    print "[+] Wrote {0} words to {1}. Done.\n\n--------\nGood luck. By @tehnlulz from (originally) @mwrlabs.".format(len(final_words),outputfile)

if __name__ == '__main__':
    main()