def power(base, exponent):
	if base == 0.0 and exponent < 0:
		print "valid input"
		return 
	if exponent < 0:
		absExponent = -exponent
	result = powerWithUnsignedExponent(base, exponent)
	if exponent < 0:
		result = 1.0 / result
	return result

def powerWithUnsignedExponent(base, absExponent):
	result = 1.0;
	for i in range(absExponent):
		result *= base
	return result
