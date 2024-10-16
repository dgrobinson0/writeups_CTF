from hidden import flag, shift

def encode(data, shift):
	enc = ''
	for _ in data:
		enc += chr((ord(_)+shift) % 0xff)
	return enc

assert encode(flag, shift) == '-3(.4?B,5*9@7;065&0:&:6&-(5*@D'