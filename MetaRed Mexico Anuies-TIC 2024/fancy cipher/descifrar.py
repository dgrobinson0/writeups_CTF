ciphertext = '-3(.4?B,5*9@7;065&0:&:6&-(5*@D'

def decode(data, shift):
    dec = ''
    for _ in data:
        dec += chr((ord(_) - shift) % 0xff)
    return dec

# Probar valores de shift
for shift in range(256):
    decoded = decode(ciphertext, shift)
    print(f"Shift: {shift} -> {decoded}")
