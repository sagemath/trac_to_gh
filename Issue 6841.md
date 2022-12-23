# Issue 6841: the shift cryptosystem

Issue created by migration from https://trac.sagemath.org/ticket/6841

Original creator: mvngu

Original creation time: 2009-08-29 08:55:28

Assignee: somebody

CC:  rbeezer

Implement the shift cryptosystem for educational purposes. This adds to the classical cryptosystems already implemented.


---

Comment by mvngu created at 2009-08-29 09:07:44

The patch `trac_6841-shift-cipher.patch` implements the shift cryptosystem. It also adds some doctests and documentation to existing crypto modules.


---

Comment by mvngu created at 2009-09-23 06:31:57

Here are some of rbeezer's comments on sanity checking the key value:

```
23:24 < mvngu-6971> rbeezer: Going back to shift cipher: The callable of 
                    ShiftCryptosystem (i.e. __call__) takes care of converting 
                    any value of key to 0 <= key < alphabet_size.
23:24 < mvngu-6971> rbeezer: Perhaps I should make that clear in the 
                    documentation.
23:27 < rbeezer> mvngu-6971: yes, I see it being Mod'ed, but I think you should 
                 disallow bad keys on input
23:27 < rbeezer> S(29) for "regular" alphabet just churns along, I'd prefer an 
                 error
23:27 < mvngu-6971> rbeezer: New patch coming up... in a hour or so. I'm still 
                    doing some release manage work...
23:28 < mvngu-6971> rbeezer: Thank you *very* much for the valuable feedback!
23:28 < rbeezer> For example with binary strings, my S(5) could have thrown an 
                 error, and I would have had to think about it right then, 
                 instead of looking for a positional shift of 5.  ;-)
23:29 < rbeezer> mvngu-6971: no rush, probably be tomorrow night before I get 
                 to it
23:29 < mvngu-6971> rbeezer: Cool.
```



---

Comment by mvngu created at 2009-09-24 03:19:18

based on Sage 4.1.2.alpha2


---

Attachment

The updated patch addresses rbeezer's comments on sanity checking the value of the encryption/decryption key. The sanity checking is done in the callable `__call__()` of the class `ShiftCryptosystem`. I have added doctests to that callable. Currently, methods beginning with an underscore "`_`" don't show up in the reference manual, so I have also added the doctests for checking key value to the docstring for the class `ShiftCryptosystem`. In this way, reading the reference manual for the shift cryptosystem should make it clear (hopefully) that the value of an encryption/decryption key must lie within the range of acceptable values, i.e. must be within the key space.


---

Comment by rbeezer created at 2009-09-25 05:23:24

Builds and runs on 4.1.2.alpha2.  Passes tests, docs build without warnings.  Great documentation.

Would you want to put similar input protections on `inverse_key()`?  Your call.

Positive review, either way.


---

Comment by mvngu created at 2009-09-25 07:16:42

Replying to [comment:7 rbeezer]:
> Would you want to put similar input protections on `inverse_key()`?  Your call.
Yes, I like your idea: be consistent. Please see ticket #7010 for sanity checking the value of the inverse key.


---

Comment by mvngu created at 2009-09-25 08:12:46

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:32:45

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
