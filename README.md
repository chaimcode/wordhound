Welcome to the completely redesigned, simplified WordHound. This is a tool that builds a list of password candidates for a specific target website to use with something like Hashcat or Hydra. 

If you were familiar with the old version, this is much better. It uses a better known technique called TF-IDF to extract interesting terms from target websites. Under the hood, it actually renders each and every page with using selenium and phantomjs. 

This project is going to be basically unmaintained, except maybe by you reading this! Please contribute any awesome changes you make back to the project. It's super simple:

1. Fork it
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

# Usage:

	python wordhound.py https://targeturl.com/

# Installation on Ubuntu/Deb/Kali:

	./install.sh

# Installation on any other platform:
	1. Install phantomjs from their website: 
			http://phantomjs.org/download.html
	2. Install the python requirements from requirements.txt:
			pip install -r requirements.txt

# Help:

~~~
Usage: wordhound.py [OPTIONS] URL

Options:
  --outputcandidates INTEGER  How many password candidates should be returned
  --outputfile TEXT           Where should the results be stored
  --maxdepth INTEGER          How many layers deep should the crawler go
  --contentfile TEXT          Instead of crawling a given URL, use a text file
                              with previously crawled data or an arbitrary
                              text file.
  --maxprocesses INTEGER      How many processes to use for scraping
  --help                      Show this message and exit.
~~~
