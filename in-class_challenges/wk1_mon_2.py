s = "Hi "

print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))

print_bytes(s)