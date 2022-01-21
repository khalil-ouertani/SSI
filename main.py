import pyinputplus as pyip
import pyfiglet

from SymmetricEncryption import SymmetricEncryption
from AsymmetricEncryption import AsymmetricEncryption
from Encoding import Encoding
from Hashing import Hashing


def menu():
    while(True):
        choice = pyip.inputMenu(['Encoding','Hashing','Cracking','Symmetric','Asymmetric','Quit'])
        if(choice=='Encoding'):
            Encoding.menu()
        elif(choice=='Hashing'):
            Hashing.hash_menu()
        elif(choice=='Cracking'):
            Hashing.crack_menu()
        elif(choice=='Symmetric'):
            SymmetricEncryption.menu()
        elif(choice=='Asymmetric'):
            AsymmetricEncryption.menu()
        
        elif(choice=='Quit'):
            return



menu()