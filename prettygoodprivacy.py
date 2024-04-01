import gnupg
gpg = gnupg.GPG()

input_data = gpg.gen_key_input(
    name_email='aravind@gmail.com',
    passphrase='studentatumkc',
    key_type = 'RSA',
    key_length = 4096
)

key = gpg.gen_key(input_data)
print(key)