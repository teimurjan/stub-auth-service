#!/usr/bin/env bash

cd frontend
yarn build
cd ..
docker login $1 $2
docker-compose build
docker-compose push