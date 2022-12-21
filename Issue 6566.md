# Issue 6566: method key_space() for classical cryptosystems

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-20 11:56:13

Assignee: somebody

Keywords: key space, classical cryptosystems

Add method `key_space()` to the following classes:

 * `sage.crypto.classical.HillCryptosystem`

 * `sage.crypto.classical.SubstitutionCryptosystem`

 * `sage.crypto.classical.TranspositionCryptosystem`

 * `sage.crypto.classical.VigenereCryptosystem`

The new method `key_space()` should output the number of possible keys for each of the above cryptosystems.


---

Comment by scotts created at 2012-12-16 13:27:17

As far as I can tell, these have been implemented since forever. For example: 


```
sage: S = AlphabeticStrings()
sage: H = HillCryptosystem(S,3)
sage: H.key_space()
Full MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26
}}}    

Similar results can be produced for all other ciphers mentioned. This is either inherited from SymmetricKeyCryptosystem or is overridden in the init methods.


---

Comment by tscholl2 created at 2015-05-26 18:40:28

Changing status from new to needs_review.


---

Comment by tscholl2 created at 2015-05-26 18:40:45

Changing status from needs_review to positive_review.


---

Comment by tscholl2 created at 2015-05-26 18:43:39

I marked this as wont fix because it's implemented at least as of 6.4. In 6.7 The following works


```
    sage: S = HillCryptosystem(AlphabeticStrings(),3)
    sage: S.key_space()
    Full MatrixSpace of 3 by 3 dense matrices over Ring of integers modulo 26

    sage: S = SubstitutionCryptosystem(AlphabeticStrings())
    sage: S.key_space()
    Free alphabetic string monoid on A-Z

    sage: S = TranspositionCryptosystem(AlphabeticStrings(),2)
    sage: S.key_space()
    Symmetric group of order 2! as a permutation group

    sage: S = VigenereCryptosystem(AlphabeticStrings(), 2)
    sage: S.key_space()
    Free alphabetic string monoid on A-Z
```



---

Comment by vbraun created at 2015-06-19 08:38:33

Resolution: fixed
