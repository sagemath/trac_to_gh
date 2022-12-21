# Issue 6461: Schaefer's Simplified Data Encryption Standard for educational purposes

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-04 09:44:37

Assignee: somebody

CC:  malb

Keywords: cryptography, DES, S-DES

This is a follow-up to #6164. The goal here is to implement the S-DES block cipher of Schaefer as described in the paper:

 E. Schaefer. A simplified data encryption algorithm. Cryptologia, 20(1):77--84, 1996.

This is a simplified variant of the Data Encryption Standard (DES) to be used for cryptography education.


---

Comment by malb created at 2009-07-16 12:19:37

*Review*:

 * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?
 * The code looks good and is nicely documented (coverage: 100%)
 * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html
 *  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper
 * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1
 * patch applies cleanly against 4.1.
 * reference manual builds without warnings and the result looks okay.
 * doctests pass on sage.math

Bottomline: positive review except some nitpicks.


---

Comment by mvngu created at 2009-07-16 12:52:19

Replying to [comment:2 malb]:
>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?
Unfortunately, I don't have access to the original paper by Schaefer, and neither do my institution. I relied on the note at

http://bitterroot.vancouver.wsu.edu/cs427_Spring09/docs/sdes.pdf




>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html
Before switching to using `__cmp__()`, I used `==` for comparing objects. But then doing `a == loads(dumps(a))` consistently returned `False` for me. Let me try it again.



>  *  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper
Ah... the notes I referenced above uses `IP` to denote the initial permutation and `IP^-1` for its inverse. Perhaps that is less confusing you think?



>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1
That can be done.


---

Comment by malb created at 2009-07-16 13:18:07

I just found this: http://buzzard.ups.edu/sdes/sdes.html :)


---

Comment by mvngu created at 2009-07-24 20:56:28

based on Sage 4.1.1.alpha0


---

Attachment

Replying to [comment:2 malb]:
>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?

There are no official test vectors for simplified DES. Even the original paper by Schaefer doesn't contain any such vectors.




>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html

The latest patch `trac_6461-sdes.patch` now uses `__eq__()`. I have also modified the class `MiniAES` in `sage/crypto/block_cipher/miniaes.py` so it now also uses `__eq__()`.




>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1

Done.


---

Comment by was created at 2009-07-27 15:32:41

Looks good to me, and Martin says it's ok if it fixes the nitpicks, which I think it does.


---

Comment by mvngu created at 2009-08-23 14:01:48

Resolution: fixed
