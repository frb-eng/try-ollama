#!/bin/sh

brew update && brew upgrade && brew install miniconda

if [ ! -d ".conda" ]; then
    conda init
    conda create --prefix .conda --yes python=3.12
fi

conda activate $PWD/.conda
pip install -r requirements.txt