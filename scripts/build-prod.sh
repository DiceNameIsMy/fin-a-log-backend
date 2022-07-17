#!/usr/bin/env

docker build --target builder . -f compose/prod/Dockerfile --cache-from fin-a-log-backend-builder:latest --tag fin-a-log-backend-builder:latest
docker build . -f compose/prod/Dockerfile --cache-from fin-a-log-backend-builder:latest --cache-from fin-a-log-backend:latest --tag fin-a-log-backend:latest
