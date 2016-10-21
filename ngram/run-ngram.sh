#!/bin/bash

# $1: text file
# $2: language model file
# $3: test file

#ngram-count -order 3 -interpolate -kndiscount -gt1min 5 -gt2min 4 -gt3min 3 -unk -text $1 -lm $2
#accuracy: 0.0560690080099
#accuracy: 0.150133497638
#ngram-count -order 4 -interpolate -kndiscount -gt1min 6 -gt2min 5 -gt3min 4 -gt4min 3 -unk -text $1 -lm $2
#accuracy: 0.0503183405217
#accuracy: 0.146025878004

#ngram-count -order 4 -interpolate -kndiscount -gt1min 5 -gt2min 4 -gt3min 3 -gt4min 2 -unk -text $1 -lm $2


#accuracy: 0.0591497227357
#accuracy: 0.159375641816
#ngram-count -order 5 -interpolate -kndiscount -gt1min 5 -gt2min 4 -gt3min 3 -gt4min 2 -gt5min 2 -unk -text $1 -lm $2
#accuracy: 0.0575066748819
#accuracy: 0.157321831998

#ngram-count -order 5 -interpolate -kndiscount -gt1min 7 -gt2min 6 -gt3min 5 -gt4min 4 -gt5min 4 -unk -text $1 -lm $2
#accuracy: 0.0414869583077
#accuracy: 0.131649209283
#ngram-count -order 5 -interpolate -kndiscount -gt1min 6 -gt2min 5 -gt3min 4 -gt4min 3 -gt5min 2 -unk -text $1 -lm $2
#accuracy: 0.0499075785582
#ngram-count -order 6 -interpolate -kndiscount -gt1min 7 -gt2min 6 -gt3min 5 -gt4min 4 -gt5min 3 -gt6min 3 -unk -text $1 -lm $2
#ngram-count -order 7 -interpolate -kndiscount -gt1min 20 -gt2min 18 -gt3min 16 -gt4min 14 -gt5min 14 -gt6min 14 -gt7min 14 -unk -text $1 -lm $2
#ngram-count -order 7 -interpolate -kndiscount -gt1min 50 -gt2min 45 -gt3min 40 -gt4min 35 -gt5min 30 -gt6min 25 -gt7min 20 -unk -text $1 -lm $2
#accuracy: 0.00759909632368
#ngram-count -order 9 -interpolate -kndiscount -gt1min 30 -gt2min 28 -gt3min 26 -gt4min 24 -gt5min 22 -gt6min 20 -gt7min 18 -gt8min 18 -gt9min 18 -unk -text $1 -lm $2
#ngram-count -order 10 -interpolate -kndiscount -gt1min 30 -gt2min 28 -gt3min 26 -gt4min 24 -gt5min 22 -gt6min 20 -gt7min 18 -gt8min 18 -gt9min 18 -unk -text $1 -lm $2
#ngram-count -order 10 -interpolate -kndiscount -gt1min 50 -gt2min 47 -gt3min 44 -gt4min 40 -gt5min 35 -gt6min 30 -gt7min 25 -gt8min 20 -gt9min 20 -unk -text $1 -lm $2


#ngram -ppl $3 -cache 100 -debug 1 -order 4 -lm $2


ngram -ppl $3 -debug 1 -order 4 -lm $2
