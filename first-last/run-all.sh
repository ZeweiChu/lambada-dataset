#!/bin/bash
echo "running dev set"
python first-last-context-word.py ../data/lambada_development.txt
echo "running test set"
python first-last-context-word.py ../data/lambada_test.txt
echo "running control set"
python first-last-context-word.py ../data/lambada_control.txt
