# Issue 8283: A better Carmichael lambda function

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2010-02-16 16:36:13

Assignee: mvngu

Reported by ylchapuy:

Here is another implementation:

 {{{

 def carmichael_lambda(n):
    n = Integer(n)

    if n < 1:
        raise ValueError("Input n must be a positive integer.")

    F = n.factor()
    L = []

    # first get rid of the even part
    if n & 1 == 0:
        e = F[0][1]
        F = F[1:]
        if e < 3:
            e = e-1
        else:
            e = e-2
        L.append(1<<e)

    # then other prime factors
    L += [ p**(k-1)*(p-1) for p,k in F]

    # finish the job
    return lcm(L)

 }}}

This is a bit faster than the current implementation and, if you replace lcm with sage.rings.integer.LCM_list, it is even faster.

A bug with the current function is that the output is not always an integer: e.g., carmichael_lambda(16) is of type sage.rings.rational.Rational .



---

Comment by ylchapuy created at 2010-03-01 10:09:02

based on 4.3.3


---

Comment by ylchapuy created at 2010-03-01 10:10:29

Changing status from new to needs_review.


---

Attachment

I don't use `sage.rings.integer.LCM_list` because I think it's less readable.


---

Comment by wdj created at 2010-03-02 21:41:10

Applies okay to 10.26.2 mac and passes sage -testall.

Okay with me. Minh, what do you think?


---

Comment by mvngu created at 2010-03-03 13:21:44

apply on top of previous one


---

Attachment

Replying to [comment:2 wdj]:
> Okay with me. Minh, what do you think?

I agree with Yann's rewrite. It's much more compact than the previous version. However, I have attached the reviewer patch [trac_8283-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8283/trac_8283-reviewer.patch), whose changes include:

 * Remove the import statements
 {{{
from sage.rings.arith import factor
from sage.structure.element import generic_power
 }}}
 These import statements are no longer required due to Yann's rewrite of the Carmichael lambda function.
 * Move the import statement
 {{{
import sage.rings.integer
 }}}
 to the module preamble, so that it now reads
 {{{
from sage.rings.integer import Integer
 }}}
 This has the effect of importing only what is required, i.e. the class `Integer`, instead of importing the whole module `sage.rings.integer`.
 * Some typo fixes.
 * Clean up à la [PEP8](http://www.python.org/dev/peps/pep-0008/).
 * Removing a redundant `lambda` construct by replacing
 {{{
lambda x: int(x)
 }}}
 with the more compact
 {{{
int
 }}}

Only my patch needs review by anyone but me. If it's OK, then the whole ticket gets a positive review.


---

Comment by wdj created at 2010-03-04 01:17:14

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-03-04 01:17:14

I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary? If that is okay, positive review from me.


---

Comment by mvngu created at 2010-03-04 01:31:30

Replying to [comment:4 wdj]:
> I read this over - looks good. I also installed it on top of the previous patch - passed sage -t devel/sage/sage/crypto/util.py. Is that enough, or it sage -testall necessary?

Running all doctests in the cryptography module subdirectory would be nice. Something like:

```
./sage -t -long devel/sage-main/sage/crypto/
```

The module `sage/crypto/util.py` is at least used by the Blum-Goldwasser class under `sage/crypto/public_key/`. So naturally one would like to know how the above two patches would affect any other modules under the cryptography subdirectory.


---

Comment by wdj created at 2010-03-04 01:46:36

Done. All tests passed!


---

Comment by mhansen created at 2010-03-06 08:36:59

Resolution: fixed
