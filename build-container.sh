#!/usr/bin/env bash

cd frontend
yarn build
cd ..
docker login registry.it-a.net $1 $2
docker-compose build
docker-compose push