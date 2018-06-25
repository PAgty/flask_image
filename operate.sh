apt-get update
apt-get install -y redis-server
wget http://download.redis.io/releases/redis-4.0.10.tar.gz
tar xzf redis-4.0.10.tar.gz
cd redis-4.0.10
make
cd ..
redis-4.0.10/src/redis-server