#!/bin/sh
# Builds a standalone dist/ (index.html is authored without the html/head wrapper).
set -e
cd "$(dirname "$0")"
mkdir -p dist
{
  printf '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n'
  cat index.html
  printf '\n</body>\n</html>\n'
} > dist/index.html
cp names.js dist/names.js
rm -rf dist/illustrations && cp -r illustrations dist/illustrations
