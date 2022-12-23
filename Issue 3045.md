# Issue 3045: K.gen() where K = GF(p) returns 1, not a primitive element

Issue created by migration from https://trac.sagemath.org/ticket/3045

Original creator: jxxcarlson

Original creation time: 2008-04-27 15:06:13

Assignee: was

Keywords: galois field


```
sage: k = GF(7)
sage: k.gen()
1
```





---

Comment by AlexGhitza created at 2009-01-23 08:31:46

This is actually the correct behaviour.  The function that returns a primitive element is K.multiplicative_generator(), not K.gen().  There was some inconsistency in the docstrings of the various types of finite fields, which is fixed by the attached patch.


---

Comment by kedlaya created at 2009-01-23 22:20:08

This otherwise deserves a positive review, except that I couldn't verify the claim in the doctest that the outputs of gen() and multiplicative_generator() can vary between runs. Is that really true?


---

Attachment

Kiran, I tried to find some examples and couldn't.  I think the point of the warning in the docstring is that we are not guaranteeing that the finite fields code wouldn't change in the future in such a way that other generators would be returned; or, for that matter, that the same version of Sage running on wildly different architectures won't return different generators.  I modified the docstrings a bit to (hopefully) make that more clear.

Note that multiplicative_generator() calls pari's znprimroot(), so whatever fuzziness there is in pari's finding a generator gets automatically inherited by Sage.


---

Comment by roed created at 2009-01-24 11:31:13

Looks good to me.  I think the docstrings are clear enough.


---

Comment by mabshoff created at 2009-01-25 02:20:34

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 02:20:34

Resolution: fixed
