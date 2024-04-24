#!/usr/bin/env bash

echo " ✔︎ Staring Build process.."
echo ""
#check_mark="\033[1;32m✔\033[0m"

header() { echo -e "\n\033[1m$1\033[0m"; }


header "Loading Build Enviornment...\n"

pip3 install git+https://${GH_TOKEN}@github.com/squidfunk/mkdocs-material-insiders.git
pip3 install -r requirements.txt

mkdocs build --clean  --site-dir site/
mkdir -p site/.well-known
mike deploy --push --update-aliases 0.1.7 latest


header "Next Steps\n"
echo "Build Artifact is available at: site/build_id.txt"


date "+%Y-%m-%dT%H:%M:%S%z" > site/.well-known/build_id.txt

sleep 1

echo "Build completed successfully"
