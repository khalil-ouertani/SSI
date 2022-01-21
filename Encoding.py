import base64 ,hashlib
import string
import re
import pyfiglet
import pyinputplus as pyip

class Encoding:
	'''
		1- Encode my message
		2- Decode my message
	'''

	@classmethod
	def encode(cls,data, method):
		if(method =='ascii'):
			encoded_text = str.encode(data,encoding=method)
			print('*** Your encoded text is : ')
			print(encoded_text)
			return(encoded_text)
		
		elif(method == 'base64'):
			message_bytes = data.encode('ascii')
			base64_bytes = base64.b64encode(message_bytes)
			base64_message = base64_bytes.decode('ascii')
			print('*** Your encoded text is : ' + base64_message + ' ***')
			return(base64_message)
		
		elif(method == 'base32'):
			message_bytes = data.encode('ascii')
			base32_bytes = base64.b32encode(message_bytes)
			base32_message = base32_bytes.decode('ascii')
			print('*** Your encoded text is : ' + base32_message + ' ***')
			return(base32_message)
			
		elif(method=='base16'):
			message_bytes = data.encode('ascii')
			base16_bytes = base64.b32encode(message_bytes)
			base16_message = base16_bytes.decode('ascii')
			print('*** Your encoded text is : ' + base16_message + ' ***')
			return(base16_message)

	@classmethod
	def decode(cls, encoded_data, method):
		if(method == 'ascii'):
			data = encoded_data.decode(encoding=method)
			print('<<< Your plain text is : ' + data + '>>>')
			return(data)
		
		elif(method == 'base64'):
			message_bytes = encoded_data.encode('ascii')
			base64_bytes = base64.b64decode(message_bytes)
			base64_message = base64_bytes.decode('ascii')
			print('<<< Your plain text is : ' + base64_message + ' >>>')
			return(base64_message)
		
		elif(method == 'base32'):
			message_bytes = encoded_data.encode('ascii')
			base32_bytes = base64.b32decode(message_bytes)
			base32_message = base32_bytes.decode('ascii')
			print('<<< Your plain text is : ' + base32_message + ' >>>')
			return(base32_message)
			
		elif(method=='base16'):
			message_bytes = encoded_data.encode('ascii')
			base16_bytes = base64.b32decode(message_bytes)
			base16_message = base16_bytes.decode('ascii')
			print('<<< Your plain text is : ' + base16_message + ' >>>')
			return(base16_message)


	

	@classmethod
	def menu(cls):
		while(True):
			print('\n')
			choice = pyip.inputMenu(['Encode', 'Quit'])
			if(choice=='Encode'):
				data = pyip.inputStr('Please enter text to encode : ')
				method = pyip.inputMenu(['ascii', 'base16', 'base32', 'base64'])
				encoded_data = Encoding.encode(data,method)

				print('\nDo you want to decode your message? ')
				decode = pyip.inputMenu(['Yes','No'])
				if(decode=='No'):
					continue
				else :
					Encoding.decode(encoded_data , method)
			
			else:
				return
