cd /usr/local
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
tar xzf Python-3.6.0.tgz
cd Python-3.6.0
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
cd /usr/local/Python-3.6.0
make && make altinstall
