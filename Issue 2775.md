# Issue 2775: multivariate factoring over some rings gives incorrect results

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-02 16:16:26

Assignee: somebody

This example is from Genya Zaytman:


```
sage: version()
'SAGE Version sage-2.11, Release Date: 2008-03-30'
sage: q = 1073741789
sage: T.<aa, bb> = PolynomialRing(GF(q))
sage: f = aa^2 + 12124343*bb*aa + 32434598*bb^2; f
aa^2 + 12124343*aa*bb + 32434598*bb^2
sage: f.factor()
(32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2)
sage: g = (32434598) * (16373350*aa^2 + 437239695*aa*bb + bb^2); g
aa^2 - 49344938*aa*bb + 32434598*bb^2
sage: f == g
False
```


Michael Abshoff reports that this is a bug in Singular itself.

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/bb040b4580b44184



---

Comment by mabshoff created at 2008-04-03 11:14:15

Changing assignee from somebody to tbd.


---

Comment by mabshoff created at 2008-04-03 11:14:15

Changing component from basic arithmetic to factorization.


---

Comment by malb created at 2008-04-04 08:58:28

We got word from the Singular team: My rough translation follows: 

Our analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as "Type indicator").
Unfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).


---

Comment by dmharvey created at 2008-04-04 13:00:59

Replying to [comment:3 malb]:
> We got word from the Singular team: My rough translation follows: 
> 
> Our analysis revealed that the cause is that the characteristic is too big: despite the fact that the Singular kernel can compute with characteristics up to 2<sup>31</sup> since 3-0-0, Factory has a limit of p <2<sup>29</sup> (31 bit for signed int, 2 bit as "Type indicator").
> Unfortunately this wasn't tested, since the former limit for Singular was much lower (2<sup>15</sup>).

Clarification: is "Factory" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?

Another question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?


---

Comment by mabshoff created at 2008-04-04 13:21:59

Replying to [comment:4 dmharvey]:

> Clarification: is "Factory" something in Sage, or something in Singular? i.e. is this still a bug (or possibly documentation bug) at their end, or do we just need to stop using Singular when the characteristic gets this big?

Factory is a library that is part of Singular and used to do factorization. Other projects like M2 also use it. As you write we need to check the characteristic before passing the polynomial to factory nee Singular and otherwise throw an exception. 
 
> Another question: is it really always 29 bits, or is it going to be 61 bits on a 64-bit machine?

It seems to be always 29 bits. I tested on sage.math with a 64 bit Singular.

Cheers,

Michael


---

Comment by malb created at 2008-04-04 13:23:18

> Clarification: is "Factory" something in Sage, or something in Singular? i.e. is
> this still a bug (or possibly documentation bug) at their end, or do we just need
> to stop using Singular when the characteristic gets this big?

"Factory" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.

> Another question: is it really always 29 bits, or is it going to be 61 bits on a
> 64-bit machine?

The word is 29 bits, but I'll check later, too.


---

Comment by dmharvey created at 2008-04-04 13:30:34

Replying to [comment:6 malb]:
> "Factory" is a Singular thing and we need to raise an `Exception` if the user attempts to factor of fields that large. I'll provide a patch later.

Ummm.... do we have any other way to provide the factorisation? For example, Genya (who reported this bug) actually wanted to factor the polynomial :-) I agree that an exception is better than an incorrect result, but it would be nice if.....


---

Attachment


---

Comment by malb created at 2008-04-05 21:36:02

The attached patch raises a `NotImplementedError` if a factorisation with characteristic > 2<sup>29</sup> is attempted.


---

Comment by mabshoff created at 2008-04-06 03:08:10

Patch looks good to me. It adds the original bug report as a doctest. Positive review. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 03:09:36

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 03:09:36

Merged in Sage 3.0.alpha2
