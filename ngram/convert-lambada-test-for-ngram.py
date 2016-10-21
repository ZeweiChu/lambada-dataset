import sys
import code

if len(sys.argv) != 5:
	print("Usage: python xxx input output stopwords correct_index")
	exit(-1)

stopwords = []
with open(sys.argv[3], "r") as fin:
	for line in fin:	
		stopwords.append(line.strip())

fout = open(sys.argv[2], "w")
fcorrect = open(sys.argv[4], "w")
with open(sys.argv[1], "r") as fin:
	for line in fin:
		target_index = -1
		linenum = 0
		vocab = line.strip().split()
		target_word = vocab[-1]
		vocab = vocab[:-1]
		line = vocab
		for v in vocab:
			#code.interact(local=locals())
			if not v in stopwords:
				linenum += 1
				if v == target_word:
					target_index = linenum
				newline = line[:]
				newline.append(v)
				fout.write(" ".join(newline) + "\n")
				fout.write("thisisnotaword "*120 + "\n")				
	
		fcorrect.write(str(target_index) + "\n")
		fout.write("\n")
		
fout.close()	
fcorrect.close()
		
