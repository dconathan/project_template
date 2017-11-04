#! /usr/bin/env bash

source activate {{cookiecutter.project_name}}

export PYTHONPATH=$(readlink -f backend/src)
