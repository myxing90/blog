def my_encode(password):
	encrypt_str = ''
	for c in password:
		encrypt_c =  hex(ord(c)-15)[2:4]
		encrypt_str = encrypt_str + encrypt_c

	print(encrypt_str)
	return(encrypt_str)

def my_decode(encrypted_str):
	str_length = len(encrypted_str)
	N = 2
	decrypt_str = ''
	while N != str_length + 2:
		decrypt_c_1 = encrypted_str[N-2:N]
		decrypt_c_2 = chr(int(decrypt_c_1,16)+15)
		decrypt_str = decrypt_str + decrypt_c_2
		N = N+2

	print(decrypt_str)
	return(decrypt_str)

if __name__ == '__main__':
	encrypt_data = my_encode('myx.1990')
	my_decode(encrypt_data)
