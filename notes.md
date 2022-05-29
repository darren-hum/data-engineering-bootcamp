# Week 1
## Ingesting Data to Postgres

- docker local volume created to circumvent permission on /var/lib.. issue
- '-it' flag allocates pseudo-tty (interactive pseudo-terminal)
- passing parameters with '-e' flag
- mounting the local drive to var/lib/postgresql/data
- map host machine port for postgres to container port

```
docker volume create --name dtc_postgres_volume_local -d local
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v dtc_postgres_volume_local:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13 
```

## Postgres
#### PGCLI

```
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

#### PGADMIN
```
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgdamin \
    dpage/pgadmin4

```
#### Create Network

```
docker network create <NAME>
```

#### Ingestion Script
```
URL="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.parquet"
python ingest_data.py \
    --user=root \
    --pw=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_trips \
    --url=${URL}
```

```
docker build -t taxi_ingest:v001 .
docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
    --user=root \
    --pw=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table=yellow_taxi_trips_docker \
    --url=${URL}
```
# Week 2
# Week 3
# Week 4