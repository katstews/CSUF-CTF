FROM ubuntu:22.04 AS app
FROM redpwn/jail:v0.0.2

COPY --from=app / /srv
WORKDIR /srv/app/

COPY bin/flag.txt .
COPY bin/chall run