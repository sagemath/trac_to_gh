# Issue 8960: doctest coverage for real_mpfr.pyx

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-14 09:27:18

Assignee: AlexGhitza

CC:  robertwb was

This patch works on doctest coverage.

It also changes the latex representation of a real field to indicate the precision and rounding


---

Comment by jason created at 2010-05-14 09:31:41

The patch brings coverage in the file from 75% to 93%.


---

Comment by jason created at 2010-05-14 13:40:33

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-14 13:40:33

CCing possible reviewers; this patch increases real_mpfr.pyx doctest coverage from ~75% to about 93%


---

Attachment

I've split off changing the latex representation to #8962.

This patch also changes a deprecated call to MPFR, and redefines several functions to be aliases when it is more appropriate (e.g., self.prec is an alias to self.precision)


---

Attachment

Changes in the reviewer patch include:

 * Typo fixes.
 * Fix errors/warnings with LaTeX markups in docstrings.
 * Use error types, e.g. IndexError, etc., as callables in accordance with Python 3.x.
 * Don't LaTeX expressions wherever that makes sense. For example, something like
 {{{
`self`
 }}}
 would actually LaTeX the word "self".

Incidentally, I came across the following line

```
elif PY_TYPE_CHECK(x, gen) and typ((<gen>x).g) == t_REAL:
```

from the function

```
cdef _set(self, x, int base):
        # This should not be called except when the number is being created.    
        # Real Numbers are supposed to be immutable.
<...>
```

Notice the call

```
typ((<gen>x).g)
```

Should this be

```
type((<gen>x).g)
```

That is, use "type" instead of "typ"?



Apart from the above, I'm OK with Jason's changes. So only my patch needs review by anyone but me.


---

Comment by cremona created at 2010-06-06 20:07:09

I applied the two patches to 4.4.3 and all is well.  And I took literally the advice that only the review patch needed to be reviewed, I did not look at the other in any detail.  Tests pass and docbuild gave no errors.


---

Comment by cremona created at 2010-06-06 20:07:09

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-07 04:48:09

Resolution: fixed
