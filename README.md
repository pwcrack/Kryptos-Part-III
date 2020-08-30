# Kryptos-Part-III

Kryptos (https://en.wikipedia.org/wiki/Kryptos) is a well-known sculpture at CIA Headquarters in Langley, Virginia by artist James Sanborn (http://jimsanborn.net/).  It contains four cryptograms.  The first three have been solved while the fourth remains unsolved at this time.  
                                                                                                                                        
Part III of Kryptos is encrypted using a Route Transposition followed by a Keyed Columnar Transposition. The plaintext was also written backwards.  While this does not add to the complexity of the solution, it is a factor I’ll address later.  To solve this type of cryptogram the most difficult part is to know or understand the methodology used to do the encryption in the first place.  Once the methodology is known, there are still complications (keys, grid length, etc.)

I did not solve Kryptos Part III in any way.  I am indebted and give credit to the UCSD website (https://math.ucsd.edu/~crypto/Projects/KarlWang/index2.html#3) which was useful in understanding the methodology of Kryptos Part III.  At this site, they give credit to another website which is no longer running, so I won’t list it here.

While the solution to Kryptos Part III was well-known, I was not able to find a script or source-code that would perform this specific decryption programmatically.  I wanted this in order to solve a different cryptogram that had been encrypted in the same way as Kryptos Part III (but using a different key and grid length.)  In order to solve this I needed to write an encryptor, a decryptor and a brute-forcer.

# The Encryptor

The encryptor script (encryptor-final.py) accepts four arguments in addition to the name of the program.  The first argument is the name of the file from which to draw the plaintext.  The second argument is the columnar transposition key expressed numerically.  For instance, if you want to use five columns in reverse order you would express the key as 43210.  In the case of Kryptos Part III, the key used was the word Kryptos which was then alphabetized.  Expressed numerically the key is 0362514 (to learn more about this see the solution page referenced above from UCSD.)  The encryption also requires a grid length.  In the case of Kryptos Part III the grid length used in the cryptogram was 86.  Any number greater than the length of the key and less than the length of the plaintext would be acceptable.  The final argument is the output file where the crypttext will be written.  In the case of Kryptos Part III the syntax which would accept the plaintext as input and generate the Kryptos Part III crypttext would be:

 ./encryptor-final.py kryptos-p3-plaintext.txt 0362514 86 kryptos-p3-crypttext.txt

I have included a plaintext file in this repo.  You can try out the encryptor script and compare the output to the actual sculpture (or use the solution website above.)

# The Decryptor

The decryptor (decryptor-final.py) is very similar to the encryptor except it is opposite.  It accepts the same four arguments, but will take crypttext as input and output plaintext.  You can test it on the actual Kryptos Part III crypttext, either by using the supplied crypttext file or by creating one yourself using the Encryptor.  The result will be the same.  The syntax would be:

./decryptor-final.py kryptos-p3-crypttext-86.txt 0362514 86 plaintext.txt

# General Purpose

While both the encryptor and decryptor will work with the Kryptos Part III to perform plaintext-to-crypttext and crypttext-to-plaintext functions, both are general purpose and will work with any valid key and grid length.  The programs accept keys with up to 10 unique digits (0-9) and will accept any grid length longer than the key length and shorter than the plaintext length.  The programs could be modified to accept longer keys.  You can test this out by encrypting any plaintext with another key and grid length and then decyrpting it using the same key and grid length.

# K3 Brute-Forcer

In order to solve the other cryptogram I was working on, I needed a brute-forcer (as I did know the methodology used to create the crypttext, but I did not know the key or grid length.)  The brute forcer script accepts as input a file with the crypttext and a key length guess (you can start at 2 and work your way up.)  It requires the top_1000_english_words.txt file, but you can add or remove words from this file.  The script iterates through all factorial combinations of keys for the given length and for each key, all valid grid lengths and builds potential plaintext candidates both forwards and backwards.  It then counts the number of words (with three or more characters) found in the candidate plaintext from the wordlist and outputs the count, key, grid length and plaintext to a file called results.txt. A threshold of 10 words is used to minimize writes to the file of bad candidates, but this can be modified as necessary by changing the line “if counter >= 10:” to another number near the end of the script.  Sorting results.txt by the first column (word count) will generally show the best result at the top.

You can try this with the Kryptos Part III crypttext file using the following syntax:

./k3bruter-final.py kryptos-p3-crypttext-86.txt 2

Start with the syntax above which will iterate through all factorial combinations of two digit keys and all possible grid lengths up to the length of the crypttext.  Then change the 2 to a 3, 4, 5, 6 and eventually 7.  This will continue to append a few candidate plaintext combinations to the results,txt file.  Once the pass with 7 is completed, the results.txt file will include the actual plaintext which will be easy to identify by sorting the file (it will have a larger number of identified words.)  It will then show the correct key and grid length used to generate this plaintext candidate.  You can also test this by using the encryptor to create other key, grid length and plaintext combinations and using the brute-forcer to break those.  Depending upon the length of your plaintext and the actual number of words, you may need to adjust the counter threshold.  The only reason I didn’t output every result was that this would needlessly waste disk space and disk I/O time.

# A note on Kryptos Part IV

Could Kryptos Part IV use the same encryption methodology as Part III, but with a different (likely longer) key and grid length?  Until recently this would have been an interesting question and worthy of some testing.  Kryptos Part II does use the same methodology as Kryptos Part I.  The specific encryption methodology for Kryptos Part III does not change any of the characters, it just changes their order.  Therefore, the incidence of coincidence of Kryptos Part III resembles that of English plaintext.  The incidence of coincidence of Kryptos Part IV does not resemble that of English plaintext, so it very likely is not encrypted using the same methodology.  But it might have been possible until recently.

Recently, James Sanborn released a fourth clue.  Together we now know that the plaintext solution to Kryptos Part IV includes the following words:  BERLIN, CLOCK, NORTHEAST, and EAST.  These words cannot be created from the letters in the Kryptos Part IV crypttext making it impossible that the same methodology was used for Kryptos Part III and Kryptos Part IV.  So there is no need to use the brute-forcer on the Kryptos Part IV crypttext, but you are welcome to try.
