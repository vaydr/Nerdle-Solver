def clip_possible(p, in_place, out_place, nowhere):

	set_cut = set()

	for i in range(len(in_place)):
		for elem in p:
			if in_place[i] is not None:
				if elem[i] != in_place[i]:
					set_cut.add(elem)

			if out_place[i] is not None:
				for char in out_place[i]:
					if (char not in elem or elem[i] == char):
						set_cut.add(elem)

			for non in nowhere:
				if non in elem:
					set_cut.add(elem)
	p = p.difference(set_cut)
	return p

def main():
	with open('nerdle_wordlist.txt') as f:
		possible = set(f.readlines())
	#one should edit in_place and out_place as they play the game, then rerun the script.
	in_place = [None, None, None, None, None, None, None, None] #elements here should just be the CHARACTER that's found at that place
	out_place = [None, None, None, None, None, None, None, None] #elements here are TUPLES of out of place elems
	nowhere = ['8', '-', '7'] #add the characters here that aren't anywhere in the solution.
	final = clip_possible(possible, in_place, out_place, nowhere)
	print(final)

main()

