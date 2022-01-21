import base64 ,hashlib
import pyinputplus as pyip
import string
import secrets

class Hashing:
	'''
		1- string to base_64
		2- string to multidigest(MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)
		3- Hash Password Cracker (MD5, SHA1, SHA256, SHA384, SHA512, RIPEMD-160)
		4- secure password generator
	'''

	@classmethod
	def choose_method(cls):
		method = pyip.inputMenu(list(['MD5', 'SHA1', 'SHA256']))
		return method

	def base64_encoder(self,text):
		text_bytes = text.encode("ascii")
		base64_bytes = base64.b64encode(text_bytes)
		return base64_bytes

	@classmethod
	def text_to_hash(cls,text,method):
		encoded_text = text.encode()
		if(method.upper() == 'MD5'):
			return "*** Your hashed code is : "+hashlib.md5(encoded_text).hexdigest()+" ***"
		if(method.upper() == 'SHA1'):
			return "*** Your hashed code is : "+hashlib.sha1(encoded_text).hexdigest()+" ***"
		if(method.upper() == 'SHA256'):
			return "*** Your hashed code is : "+hashlib.sha256(encoded_text).hexdigest()+" ***"

	@classmethod
	def multidigest(cls , text):
		method = Hashing.choose_method()
		hash = Hashing.text_to_hash(text,method)
		return hash
	
	@classmethod
	def password_cracker(cls, hash):
		methods = list(hashlib.algorithms_guaranteed)
		with open('wlist.txt', 'r+') as f:
			passwords = f.read().splitlines()
		for password in passwords: 
			for method in methods:
				if( Hashing.text_to_hash(password,method) == hash ):
					return password

		return 'Sorry we didn\'t find the password'

	def generate_password(self):
		alphabet = string.ascii_letters + string.digits
		while True:
			password = ''.join(secrets.choice(alphabet) for i in range(10))
			if (any(c.islower() for c in password)
					and any(c.isupper() for c in password)
					and sum(c.isdigit() for c in password) >= 3):
				break
		return password

	@classmethod
	def hash_menu(cls):

		while(True):
			print('\n')
			choice = pyip.inputMenu(['Hash','Quit'])
			if(choice=='Hash'):
				text = pyip.inputStr('Please enter text for hashing : ')
				hashed_text = Hashing.multidigest(text)
				print(hashed_text)
			else:
				return

	@classmethod
	def crack_menu(cls):
		while(True):
			print('\n')
			choice = pyip.inputMenu(['crack','quit'])
			if(choice=='crack'):
				hash = pyip.inputStr('Enter hash for cracking : ')
				cracked_hash = Hashing.password_cracker(hash)
				print('\n*** Cracked hash is ====>   ' + cracked_hash+' ***')
			else:
				return