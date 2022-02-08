#!/bin/bash

pip install -r requirements.txt
cd fairseq
pip install --editable .

cd ../data
#bash ../fairseq/examples/translation/prepare-iwslt14.sh
