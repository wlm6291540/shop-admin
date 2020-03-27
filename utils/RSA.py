from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA, FILETYPE_PEM
from OpenSSL.crypto import dump_privatekey, dump_publickey, load_privatekey, load_publickey


class RSA:
    def __init__(self):
        self.pk = PKey()
        self.pk.generate_key(TYPE_RSA, 1024)
        self.private_key = self.strip_pri(dump_privatekey(FILETYPE_PEM, self.pk))
        self.public_key = self.strip_pub(dump_publickey(FILETYPE_PEM, self.pk))

    def strip_pub(self, content):
        content = content.replace(b'-----BEGIN PUBLIC KEY-----\n', b'')
        content = content.replace(b'\n-----END PUBLIC KEY-----\n', b'')
        content = content.replace(b'\n', b'')
        return content

    def strip_pri(self, content):
        content = content.replace(b'-----BEGIN PRIVATE KEY-----\n', b'')
        content = content.replace(b'\n-----END PRIVATE KEY-----\n', b'')
        content = content.replace(b'\n', b'')
        return content

    def get_public_key(self):
        return self.public_key.decode('utf8')

    def get_private_key(self):
        return self.private_key.decode('utf8')