import sys

if len(sys.argv) != 2:
	print("Usage: python xxx input")
	exit(-1)

total_count = 0
first_count = 0
last_count = 0
context_ins = 0
linenum = 0
with open(sys.argv[1], "r") as fin:
	for line in fin:
		linenum += 1
		if line == "##########\n":
			linenum = 0
			total_count += 1
		if linenum == 3:
			line = line.strip().split()
			vocab = line
			first = line[0]
			last = line[-2]
		if linenum == 7:
			line = line.strip()
			if line in vocab:
				context_ins += 1
			if first == line:
				first_count += 1
			if last == line:
				last_count += 1

print("total count: {}".format(total_count))
print("context ins count: {}".format(context_ins))
print("first_count: {}".format(first_count))
print("last count: {}".format(last_count))
print("last count: {}".format(last_count))
print("first context word accuracy: {}".format(float(first_count)/float(total_count)))
print("first context word accuracy with context cases only: {}".format(float(first_count)/float(context_ins)))
print("last context word accuracy: {}".format(float(last_count)/float(total_count)))
print("last context word accuracy with context cases only: {}".format(float(last_count)/float(context_ins)))
