docker build -t time_series .
docker run -p 4000:80 --name $1 time_series &
sleep 5
docker exec -i $1 bash < operate.sh