import sys
import numpy as np

if len(sys.argv) != 4:
	print("Usage: python calc_accuracy.py input score correct_index")
	exit(-1)

correct_index = []
with open(sys.argv[3], "r") as fin:
	for line in fin:
		correct_index.append(int(line))

fscore = open(sys.argv[2], "r")
count = 0
total = 0
scores = []
linenum = 0
testlinenum = 0
test_ins_index = 0
context_count = 0
with open(sys.argv[1], "r") as fin:
	for line in fin:

		testlinenum += 1
		if line.strip() == "":
			test_ins_index += 1
			
			scores = np.asarray(scores)
			idx = np.argmin(scores)
			scores = np.sort(scores)

			if idx + 1 == correct_index[test_ins_index-1]: #and scores[1] - scores[0] > 2:
				count += 1
			total += 1
			if correct_index[test_ins_index-1] <> -1:
				context_count += 1
			scores = []
			continue
		elif "thisisnotaword" in line:
			fscore.readline()	
			linenum += 1
			fscore.readline()	
			linenum += 1
			fscore.readline()	
			linenum += 1
			fscore.readline()	
			linenum += 1
			continue


		scoreline = fscore.readline()
		linenum += 1
		if line.strip() != scoreline.strip():
			print(linenum)
			print(testlinenum)
			print(line)
			print(scoreline)
			break
		fscore.readline()
		linenum += 1
		scoreline = fscore.readline()
		linenum += 1
		fscore.readline()
		linenum += 1
		score = float(scoreline.split()[-3])
		scores.append(score)

fscore.close()
print("number of correct predictions: {}".format(count))
print("total number of instances: {}".format(total))
print("context count: {}".format(context_count))
print("context_accuracy: {}".format(float(count) / float(context_count)))
print("accuracy: " + str(float(count) / float(total)))	
