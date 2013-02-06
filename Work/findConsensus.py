A = []
consensus = open("consensus.fq", "r")
reference = open("human_long.fas", "r")
pos = 1
append = False

for line in consensus:
	line.rstrip('/r/n')
	for i in range (0, len(line)):
		if line[i] == '\n':
			continue
		else:
	 		pos += 1
			if pos == 4892:
				append = True
			if pos == 5077:
				append = False
			if append == True:		
				A.append(line[i])
pos = 1
B = []

for line in reference:
        line.rstrip('/r/n')
        for i in range (0, len(line)):
                if line[i] == '\n':
                        continue
                else:
                        pos += 1
                        if pos == 4892:
                                append = True
                        if pos == 5077:
                                append = False
                        if append == True:
                                B.append(line[i])


results = open("ref_cons.txt", "w")

results.write("> Ref\n")
results.write("".join(B))
results.write("\n")
results.write("> Cons\n")
results.write("".join(A))

results.close()
