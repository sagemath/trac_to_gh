# Issue 7746: Blum-Goldwasser probabilistic encryption

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-12-21 03:37:12

Assignee: mvngu

CC:  wdj

Keywords: Blum-Goldwasser, probabilistic encryption

The Blum-Goldwasser probabilistic public-key encryption scheme. This scheme was originally described by (Blum and Goldwasser 1985). See also section 8.7.2 of (Menezes et al. 1996) and the [Wikipedia article](http://en.wikipedia.org/wiki/Blum-Goldwasser_cryptosystem) on this scheme.

 * (Blum and Goldwasser 1985) M. Blum and S. Goldwasser. An Efficient Probabilistic Public-Key Encryption Scheme Which Hides All Partial Information. In Proceedings of CRYPTO 84 on Advances in Cryptology, pp. 289–299, Springer, 1985.

 * (Menezes et al. 1996) A. J. Menezes, P. C. van Oorschot, and S. A. Vanstone. Handbook of Applied Cryptography. CRC Press, 1996.


---

Comment by mvngu created at 2009-12-21 04:00:58

public domain version by Mike Hogan and David Joyner


---

Comment by mvngu created at 2009-12-21 04:02:37

Changing status from new to needs_review.


---

Attachment

The patch `trac_7746-blum-goldwasser.patch` introduces two new files:

 * `sage/crypto/public_key/blum_goldwasser.py` --- A class implementing the Blum-Goldwasser probabilistic public-key encryption scheme. This is a complete rewrite of the version by Mike Hogan and David Joyner, which was originally released as public domain software. The rewrite is licensed under GPLv2+. For reference, I have also attached the original public domain version.
 
 * `sage/crypto/util.py` --- A module containing miscellaneous functions for cryptographic purposes. The Blum-Goldwasser implementation makes use of various functions in this module.


---

Comment by wdj created at 2009-12-21 13:11:06

This applies and tests fine (modulo the usual failures) on sage-4.3.rc0 on a mac running 10.6.2.

This is definitely a complete reimplementation (as stated in the docstring) of Hogan's module, since we actually did a hybrid of the HAC version and the Wikipedia version of the algorithm.

I am not crazy about this:


```

 	289	    However, if there are no primes between the lower and upper bounds, 
 	290	    this function could hang forever. For instance, a lower bound of 24 and 
 	291	    an upper bound of 28 would trigger an infinite loop. 
```


It seems to violate the "defensive programming" (or "assume all people are stupid") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.

Other than this, the patch looks very well documented, gives good references and examples. I've forgotten how to compile the docs to see if the html comes out okay. Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in 


```
sage-4.3.rc0/devel/sage-BG-7746/doc/output/html/en/reference/sage/crypto/cryptosystem.html
```


Finally, some general more-or-less stylistic questions.

Is SageObject the best superclass for this? 

Is the best place for blum_blum_shub in util or in a stream cipher module?


---

Comment by mvngu created at 2009-12-21 14:21:04

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-12-21 14:21:04

Replying to [comment:2 wdj]:
> It seems to violate the "defensive programming" (or "assume all people are stupid") principle that if the is some very bad input which can be entered, then you should assume that it *will* be entered at some point.

It looks to me that there needs to be a function called, say, "has_blum_prime(lbound, ubound)" in the module `sage/crypto/util.py`. This function checks to see if there is a Blum prime within the specified lower and upper bounds. One could then use `has_blum_prime()` to first check for the presence of a Blum prime within a specified interval, prior to actually computing a random Blum prime.





> Can someone point to a page in the Developers' manual of something where html generation is explained? I don't see the changes in 

After you have applied the patch and rebuilt your branch, you could use the following command to rebuild the HTML version of the reference manual:

```
./sage -docbuild reference html
```





> Is SageObject the best superclass for this? 

No, not really. Ideally, the best parent class for the class `BlumGoldwasser` is `sage.crypto.cryptosystem.PublicKeyCryptosystem`. I'll see what I can do to make `sage.crypto.cryptosystem.PublicKeyCryptosystem` the parent class of `BlumGoldwasser`.





> Is the best place for blum_blum_shub in util or in a stream cipher module? 

I think the best place for the function `blum_blum_shub()` is in a module for pseudorandom number generators. The module that comes to mind is `sage/misc/prandom.py`. But all functions in that module are exported to the global name space, so those functions are available upon starting Sage, without having to explicitly import them. Adding more functions to the global name space is not a good idea. One wants to minimize Sage's loading time, but also to have a default set of common useful functions. Adding `blum_blum_shub()` to `sage/misc/prandom.py` and polluting the global name space is not my intention. The Blum-Blum-Shub pseudorandom bit generator is not as commonly used as, say, `random()` and `randint()`. For now, `blum_blum_shub()` fits OK in `sage/crypto/util.py`. Functions in that module are not exported by default, which is why you see lots of import statements throughout examples in that module.


---

Comment by wdj created at 2009-12-22 03:56:23

Replying to [comment:3 mvngu]:
> Replying to [comment:2 wdj]:


> It looks to me that there needs to be a function called, say, 
> "has_blum_prime(lbound, ubound)" in the module `sage/crypto/util.py`. 
> This function checks to see if there is a Blum prime within the 
> specified lower and upper bounds. 


Sounds good.


> use the following command to rebuild the HTML version of the reference manual:
> {{{
> ./sage -docbuild reference html
> }}}
> 

> 


Thanks. Docs compile fine and look great.



> 
> 
> > Is the best place for blum_blum_shub in util or in a stream cipher module? 
> 
> I think the best place for the function `blum_blum_shub()` is in a module 
> for pseudorandom number generators. The module that comes to mind 
> is `sage/misc/prandom.py`. But all functions in that module are exported to the 

Why not 


```
sage/crypto/stream_cipher.py
```

instead?


---

Comment by mvngu created at 2010-02-12 05:30:30

based on Sage 4.3.2


---

Comment by mvngu created at 2010-02-12 05:36:43

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:4 wdj]:
> Sounds good.

I have attached an updated patch which also implements the function `has_blum_prime()`.





> Why not 
> 

```
sage/crypto/stream_cipher.py
```

> instead?

The module `sage/crypto/stream_cipher.py` acts as a back-end for `sage/crypto/stream.py`. I believe a more appropriate place is to put `blum_blum_shub()` in  `sage/crypto/stream.py`. The latest version of the patch does this.


---

Comment by wdj created at 2010-02-13 13:14:55

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-02-13 13:14:55

Applied fine to 4.3.3.a0 and passes sage -testall. Reference manual looks good too.

Positive review.

Thank you very much Minh!


---

Comment by mvngu created at 2010-02-15 03:42:09

Resolution: fixed
