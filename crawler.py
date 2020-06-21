from creepy import Crawler
import sys
from urlparse import urlparse
from selenium import webdriver
from multiprocessing import Process
import signal
from time import sleep
import os 

class WebCrawler(Crawler):
    def __init__(self, url,  maxdepth, maxprocesses, urlfilter):

        print "[+] Mapping out website..."
        crawler = Crawler()
        crawler.set_follow_mode(Crawler.F_SAME_DOMAIN)
        crawler.set_max_depth = maxdepth
        crawler.add_url_filter(urlfilter)
        try:
            crawler.crawl(url)
        except KeyboardInterrupt:
            pass
        print "[+] Done mapping. Found {0} URLs".format(len(crawler.visited))
        collected_data = ""
        print "[+] Collecting text..."
        if os.path.exists('tmpdata'):
            os.remove('tmpdata')
        out = open('tmpdata','ab')
        processes = []
        blacklist = ['jpg','jpeg','gif','png','js','css','swf', 'xml', 'pdf', 'ico', 'json']
        for url in crawler.visited.keys():
            black = False
            for b in blacklist:
                if '.' + b in url.lower():
                    black = True
            if black:
                continue
            while True:
                if len(processes) > maxprocesses:
                    sleep(5)
                    for proc in processes:
                        if not proc.is_alive():
                            proc.terminate()
                            processes.remove(proc)
                else:
                    break
            
            p = Process(target=self.fetch, args=(url,))
            processes.append(p)
            p.start()

            sys.stdout.write("\t[-] Fetching {0}\n".format(url))
            #collected_data += self.fetch(url)
        while len(processes)>0:
                
                for proc in processes:
                    if not proc.is_alive():
                        processes.remove(proc)
        out.close()


        print "[+] Done collecting text..."
        output = open(urlparse(url).netloc, 'wb')
        output.write(u' '.join(collected_data).encode('utf-8').strip())
        output.close()
        self.collected_data = open("tmpdata", 'rb').read()

    def fetch(self,url):
        out = open('tmpdata','ab')
        mydriver = webdriver.PhantomJS()
        try:
            mydriver.get(url)
            mydriver.find_element_by_tag_name("body").text          
            out.write(u''.join(mydriver.find_element_by_tag_name("body").text).encode('utf-8')+'\n')
            out.close()
            mydriver.close()
            mydriver.service.process.send_signal(signal.SIGTERM)
        except:
            mydriver.service.process.send_signal(signal.SIGTERM)
            mydriver.close()