Imlementation of **Vigenère** algorithm for encryption and decryption.


    The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.


    In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.


The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.


Example

var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key

var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj');  // returns 'waffles'

Any character not in the alphabet must be left as is. For example (following from above):

c.encode('CODEWARS'); // returns 'CODEWARS'

The problem is from https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
