#!/bin/bash
stopwords=$1
train=$2
test=$3
python convert-lambada-test-for-ngram.py $test test.txt $stopwords correct_index.txt
bash run-ngram.sh $train lm.txt test.txt > scores.txt
python calc_accuracy.py test.txt scores.txt correct_index.txt
