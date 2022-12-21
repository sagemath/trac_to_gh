# Issue 7124: affine cipher and its cryptanalysis

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-10-05 16:13:43

Assignee: somebody

CC:  rbeezer




---

Comment by mvngu created at 2009-10-10 00:09:31

Changing keywords from "" to "affine cipher".


---

Comment by mvngu created at 2009-10-10 00:09:31

Changing status from new to needs_work.


---

Comment by mvngu created at 2009-10-10 00:09:31

The patch `trac_7124-affine.patch` implements the affine cryptosystem.


---

Comment by mvngu created at 2009-10-13 01:47:52

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-15 00:38:10

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-15 00:38:10

In light of rbeezer's comments at #7123, I need to update the patches on this ticket since they depend on #7123. Also, I would like to add some more stuff to the patches for the affine cipher.


---

Attachment

Sample output for odd behavior of `brute_force()`


---

Comment by rbeezer created at 2009-10-15 01:07:36

Minh,

Output of plain `brute_force()` looks suspicious, and when a ranking is suggested, errors are raised.  Tests are failing as well.  See attached.

Inside `brute_force()` method, should the `L` list be so empty?

Rob


---

Comment by mvngu created at 2009-10-15 01:17:57

Please try the latest patches based on Sage 4.1.2.rc2.


---

Comment by mvngu created at 2009-10-15 01:21:53

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-15 01:21:53


```
18:13 < mvngu> rbeezer: The output of brute_force() is all the 312 possible
               dicipherments.
18:14 < mvngu> rbeezer: It uses a list of list for an indexing scheme that's
               meant for readability.
18:14 < rbeezer> but I'm not getting the keys that achieves them
18:14 < rbeezer> the L list is a list of empty lists??
18:14 < mvngu> rbeezer: Let me upload my recent patches....
18:14 < rbeezer> aah, that'd help  ;-) ;-)
18:18 < mvngu> rbeezer: Uploaded patches.
18:18 < mvngu> rbeezer: Note the ticket dependency.
18:19 < rbeezer> thanks - do they include whatever prompted you to take the 
                 ticket back to "needs work"
18:19 < mvngu> rbeezer: yes
18:19 < rbeezer> In other words, should I attempt a full review in the next 6 
                 hours, or no?
18:19 < mvngu> rbeezer: I fixed some documentation typos, add an example on the 
               decimation cipher.
18:20 < mvngu> rbeezer: And yes, I think it's ready for a full review.
18:20 < mvngu> rbeezer: Thank you very much for spending time on these crypto 
               stuff!
```



---

Comment by mvngu created at 2009-10-15 01:52:24

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-15 01:52:24

At present, here's what happening with the method `brute_force()`: it returns a list of lists `L` that contains all the possible decipherments. And that's it, not even the key that results in a candidate decipherment. If you think the present behaviour is confusing, yes, I agree with that. Here's a sample session.

```
sage: A = AffineCryptosystem(AlphabeticStrings())
sage: cipher = A(11, 4)
sage: P = A.encoding("Have a nice day at the seashore.")
sage: C = cipher(P); C
DEBWEROAWLEIEFFDWUWEUDCJW
sage: candidates = A.brute_force(C)
sage: candidates[1]

[DEBWEROAWLEIEFFDWUWEUDCJW,
 CDAVDQNZVKDHDEECVTVDTCBIV,
 BCZUCPMYUJCGCDDBUSUCSBAHU,
 ABYTBOLXTIBFBCCATRTBRAZGT,
 ZAXSANKWSHAEABBZSQSAQZYFS,
 YZWRZMJVRGZDZAAYRPRZPYXER,
 XYVQYLIUQFYCYZZXQOQYOXWDQ,
 WXUPXKHTPEXBXYYWPNPXNWVCP,
 VWTOWJGSODWAWXXVOMOWMVUBO,
 UVSNVIFRNCVZVWWUNLNVLUTAN,
 TURMUHEQMBUYUVVTMKMUKTSZM,
 STQLTGDPLATXTUUSLJLTJSRYL,
 RSPKSFCOKZSWSTTRKIKSIRQXK,
 QROJREBNJYRVRSSQJHJRHQPWJ,
 PQNIQDAMIXQUQRRPIGIQGPOVI,
 OPMHPCZLHWPTPQQOHFHPFONUH,
 NOLGOBYKGVOSOPPNGEGOENMTG,
 MNKFNAXJFUNRNOOMFDFNDMLSF,
 LMJEMZWIETMQMNNLECEMCLKRE,
 KLIDLYVHDSLPLMMKDBDLBKJQD,
 JKHCKXUGCRKOKLLJCACKAJIPC,
 IJGBJWTFBQJNJKKIBZBJZIHOB,
 HIFAIVSEAPIMIJJHAYAIYHGNA,
 GHEZHURDZOHLHIIGZXZHXGFMZ,
 FGDYGTQCYNGKGHHFYWYGWFELY,
 EFCXFSPBXMFJFGGEXVXFVEDKX]
```

I think this is perhaps why you said the output of `brute_force()` is odd. In the method `brute_force()` of the shift cipher from #7123, it provides both the key together with the corresponding candidate decipherment. In the current affine cipher implementation, I forgot about the output of the brute force method in #7123. OK, move to "needs work" again.


---

Comment by mvngu created at 2009-10-15 21:19:47

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-15 21:19:47

rbeezer --- I think I have addressed your comment about the output of `brute_force()` being odd. Please use the latest version of the patches.


---

Comment by rbeezer created at 2009-10-16 05:29:47

Hi Minh,

Two comments:

1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run

`x=S.random_key(); print x, S.inverse_key(*x)` 

repeatedly.

This shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).

Maybe you just need subtraction someplace where you have a addition, or...

2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem?  Then you could skip some of the gcd-stuff.  For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing.  Or when checking validity for a new key, you could just test on the list.  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.

Rob


---

Comment by rbeezer created at 2009-10-16 05:29:47

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-16 20:09:54

Replying to [comment:11 rbeezer]:
> 1.  I think `inverse_key()` is broken.  The constant term is always identical, for example, run

```
x=S.random_key(); print x, S.inverse_key(*x)
```

> repeatedly. This shouldn't happen even for a=1 as is written in the doctests, since when a=1 it is a shift system.  For testing, the inverse of (a,b)=(5,7) should be (21,9).  You can test this by enchipering with one key and deciphering with the other, results should be the same (this might be good thing to do in the doctests).

I may be misunderstanding your comment here, so please tell me if that's the case. Any key `(a,b) in ZZ/nZZ x ZZ/nZZ` of the affine cipher is such that `gcd(a,n) = 1`. So you're saying that the inverse key corresponding to `(a, b)` is `(a^{-1}, -b)` where `a^{-1}` is the multiplicative inverse of `a` modulo `n`? If that is the case, then the current implementation of `inverse_key()` is clearly broken:

```
        try:
            from copy import copy
            from sage.rings.arith import inverse_mod
            n = self.alphabet_size()
            return (inverse_mod(a, n), copy(b))
        except:
            raise ValueError("(a, b) = (%s, %s) is outside the range of acceptable values for a key of this affine cipher." % (a, b))
```


How then would one use the above defined inverse key to decrypt a ciphertext? The current implementation of the method `deciphering()` follows this Wikipedia description of the encryption and decryption functions of the affine cipher:

http://en.wikipedia.org/wiki/Affine_cipher

This agrees with the following text that I have access to:

 * Doug Stinson. "Cryptography: Theory and Practice" 3rd edition.
 * Wade Trappe and Lawrence C. Washington. "Introduction to Cryptography with Coding Theory"





> Maybe you just need subtraction someplace where you have a addition, or...

I don't quite understand this comment. Can you please explain it?





> 2.  Would it make sense to build the list `A` of invertible linear coefficients in the `brute_force` method as part of `__init__` for the cryptosystem? 

Yes it does make sense to do so, and I have implemented this in response to your suggestion. The resulting code of the affine crypto module looks less "ugly" from my point of view. Thank you, Rob. Please see the latest version of the patches.





> Then you could skip some of the gcd-stuff.

And I have skipped some of the GCD computation with the above implementation of a list of invertible elements in the multiplicative group of `ZZ/nZZ`.





> For example when building a random key, you could just grab a linear coefficient, instead of repeatedly testing. 

Done according to your suggestion.





> Or when checking validity for a new key, you could just test on the list. 

Done according to your suggestion.





>  Done right, the generation of `A` could easily generalize to a new alphabet length for a new monoid as the alphabet.

I can see in my mind how to implement this based on the implementation of generating invertible elements in the multiplicative group of `ZZ/nZZ`. I think this would entail changing the implementation of the class(es) that implement say, the hexadecimal monoid. Getting the affine cipher to support the hexadecimal and radix-64 monoids should be another ticket in itself.


---

Comment by rbeezer created at 2009-10-16 23:45:25

Replying to [comment:12 mvngu]:

Well, I didn't really say exactly what `inverse_key()` should be on purpose - figuring it was your thesis and I shouldn't have all the fun.

Wikipedia is right on this one and it's what you have implemented in the deciphering routine.

If enciphering is accomplished by  x -> ax+b  (ie key is (a,b)) then 

deciphering is accomplished by  `x -> a^{-1}(x-b) = a^{-1}x - a^{-1}b`

so the inverse key would be the pair `(a^{-1}, -a^{-1}b)`

Note the constant term.  In other words, the inverse key should be what you use for the same algorithm (linear function mod 26) to reverse the process, ie create the inverse function.

Try the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.

1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.

2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.


---

Comment by mvngu created at 2009-10-17 02:42:04

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-10-17 02:42:04

Replying to [comment:13 rbeezer]:
> Try the following: start with plain text P, encipher with key (a,b) to get ciphertext C.  Now encipher C with the inverse key, and you should get P back.  This would be a good doctest someplace, maybe for `inverse_key()`, to demonstrate its intent.

I have added this doctest.





> 1.  Consider the `enciphering()` and `deciphering()` routines in `AffineCipher` - they could each call some helper function that does the linear function, but to decipher, you just pass the inverse key rather than the key.

Done.





> 2.  Its not clear to me why this won't all generalize easily to other alphabets?  You just need to know the size of the alphabet (n) and then construct the invertible elements in `A`}, and you need some kind of correspondence between the alphabet and the integers 0 through n-1.  But I haven't studied the monoid implementations to say for sure.

It can be generalized to other non-empty alphabets with more than 2 elements. An alphabet with 2 elements is not interesting enough to use for studying the affine cipher. In fact, I think that with the current implementation of the affine cipher, one can extend it to support alphabets such as the octal and hexadecimal number systems, radix-64 alphabet, and even the ASCII alphabet itself. It's just that doing so is tedious work for which I don't currently have time for. The same can be said for the shift cipher as well.


---

Comment by rbeezer created at 2009-10-17 05:45:07

Minh,

Some specific comments:

1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.

2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.

3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.

Rob


---

Comment by rbeezer created at 2009-10-17 05:45:07

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-17 06:31:29

based on Sage 4.1.2.rc2 and #7123


---

Attachment

apply on top of previous


---

Comment by mvngu created at 2009-10-17 06:36:45

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:15 rbeezer]:
> 1.  In `AffineCryptoSystem` there are comments about the list L which can probably be deleted.

Fixed.





> 2.  In `__call__` the sanity check computes d and checks d == 1.  This could be removed if you trust your `_invertible` list.

I have removed the test. In its place, I added some comments explaining why we don't need to test that each `a` is coprime to `n`, the alphabet size.





> 3.  Docstring on `inverse_key` has an odd test about euler_phi=12, a list of invertibles is computed, etc.  Not sure this is really germane.

That doctest is meant to explain what sort of values that `a` can take on if `(a,b)` is to be a secret key. I have rewritten the doctest to explain this.


---

Comment by rbeezer created at 2009-10-19 02:31:37

This should be pretty much read to go now, but I've got a six errors being raised in the doctests.  They all seem to be due to lines 2912 and 3158 of  classical.py  which are identical

`OM.setdefault(e, 0.0)`

The error is

`AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`


---

Comment by rbeezer created at 2009-10-19 02:31:37

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-10-28 12:11:36

Replying to [comment:17 rbeezer]:
> The error is
> 
> `AttributeError: 'DiscreteProbabilitySpace' object has no attribute 'setdefault'`

I took Sage 4.2 and successfully applied the attached two patches. The reference manual rebuilt successfully. Doctesting the whole Sage library didn't show up the error you reported. Can you please try using Sage 4.2? Please tell me if I've misunderstood your comments.


---

Comment by rbeezer created at 2009-10-30 04:53:26

Alright, against 4.2 there are no doctest errors in sage/crypto, so this is done.

Positive review.

Release manager: apply two patches - first "affine" then "cryptanalysis."


---

Comment by rbeezer created at 2009-10-30 04:53:26

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2009-10-30 04:53:38

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 15:39:33

Resolution: fixed
