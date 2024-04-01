import gnupg

gpg = gnupg.GPG()

path = '/Users/19049/Videos/aravind'
filename = '/sample.txt.encrypted'

with open(path + filename, 'rb') as f:
        status = gpg.decrypt_file(f, passphrase='studentatumkc', output= path + filename + ".decrypted")

print(status.ok)