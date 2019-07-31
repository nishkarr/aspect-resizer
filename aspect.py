def calc_aspect_ratios(w, h):
	if w == h:
		yield (w, h)
	landscape = w > h
	short = w
	long = h
	if landscape:
		short = h
		long = w
	for x in range(1, long):
		if short % x > 0:
			continue
		rem = short / x
		if long % rem == 0:
			yield (int(long / rem), int(x)) if landscape else (int(x), int(long / rem))

if __name__ == "__main__":

	for x,y in calc_aspect_ratios(7952,5304):
		print("%dx%d" % (x,y))

	print("--")

	for x,y in calc_aspect_ratios(5304,7952):
		print("%dx%d" % (x,y))


	#print("%d:%d\n" % aspect(10,30))
	#print("%d:%d\n" % aspect(900,900))