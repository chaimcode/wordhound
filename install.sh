echo "[=] Installing phantomjs, python-pip, libfontconfig"
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar -xvf phantomjs-2.1.1-linux-x86_64.tar.bz2
cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/
apt-get install libfontconfig -y


echo "[=] Installing python dependencies"
pip install -r requirements.txt