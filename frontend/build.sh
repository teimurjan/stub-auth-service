#!/usr/bin/env bash

react-scripts build
cd build
mv static/js/*.js ../../backend/app/static/js/main.js
mv static/js/*.js.map ../../backend/app/static/js/main.js.map
mv service-worker.js ../../backend/app/static
cd ..
rm -r build