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
    postgres:13
```

## PGCLI

```
pgcli -h localhost -p 5432 -u root -d ny_taxi
```
# Week 2
# Week 3
# Week 4