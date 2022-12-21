# Issue 4225: faster sqrt for complex numbers

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-30 20:51:33

Assignee: tbd

This is a followup to #4132.


---

Comment by robertwb created at 2008-09-30 20:55:30

Code: 


```
def new_sqrt(ComplexNumber self, all=False):
    cdef ComplexNumber z = self._new()
    if mpfr_zero_p(self.__im):
        if mpfr_sgn(self.__re) >= 0:
            mpfr_set_ui(z.__im, 0, rnd)
            mpfr_sqrt(z.__re, self.__re, rnd)
        else:
            mpfr_set_ui(z.__re, 0, rnd)
            mpfr_neg(z.__im, self.__re, rnd)
            mpfr_sqrt(z.__im, z.__im, rnd)
        if all:
            return [z, -z] if z else [z]
        else:
            return z
    # self = x + yi = (a+bi)^2
    # expand, substitute, solve
    # a^2 = (x + sqrt(x^2+y^2))/2
    cdef bint avoid_branch = mpfr_sgn(self.__re) < 0 and mpfr_cmpabs(self.__im, self.__re) < 0
    cdef mpfr_t a2
    mpfr_init2(a2, self._prec)
    mpfr_hypot(a2, self.__re, self.__im, rnd)
    if avoid_branch:
        # x + sqrt(x^2+y^2) numerically unstable for x near negative real axis
        # so we compute sqrt of (-z) and shift by i at the end
        mpfr_sub(a2, a2, self.__re, rnd)
    else:
        mpfr_add(a2, a2, self.__re, rnd)
    mpfr_mul_2si(a2, a2, -1, rnd)
    # a = sqrt(a2)
    mpfr_sqrt(z.__re, a2, rnd)
    # b = y/(2a)
    mpfr_div(z.__im, self.__im, z.__re, rnd)
    mpfr_mul_2si(z.__im, z.__im, -1, rnd)
    mpfr_clear(a2)
    if avoid_branch:
        # Now we shift by i depending on what side of the branch we were on.
        mpfr_swap(z.__re, z.__im)
        # Note that y was never negated, so b already has the opposite sign. 
        if mpfr_sgn(self.__im) < 0:
            mpfr_neg(z.__re, z.__re, rnd)
            mpfr_neg(z.__im, z.__im, rnd)
    if all:
        return [z, -z]
    else:
        return z
```


I will post a patch (with more documentation) when I have a copy of sage with #4132 included.


---

Attachment


---

Comment by AlexGhitza created at 2008-10-03 12:49:46

Looks good to me.

For some reason I had some trouble applying the patch to my 3.1.3.alpha2, but I think that might be something messed up on my end.  I applied the patch manually and it works.


---

Comment by mabshoff created at 2008-10-07 19:13:31

Yeah, I am having merge trouble against 3.1.3.alpha3, too. Can someone rebase this against alpha2?

Cheers,

Michael


---

Comment by robertwb created at 2008-10-07 19:17:58

Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do.


---

Comment by mabshoff created at 2008-10-07 19:21:03

Replying to [comment:5 robertwb]:
> Shoot... It's a pain to build an alpha just to do a rebase, but I'll see what I can do. 

You can pull from

/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/devel/sage

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-10-07 22:25:57

Replying to [comment:5 robertwb]:

I can do it in a couple of hours (since I already have alpha2 built).


---

Comment by AlexGhitza created at 2008-10-08 06:08:53

rebased against 3.1.3.alpha2


---

Attachment

OK, I've uploaded a version rebased against 3.1.3.alpha2.

For the record, here is some timing info:

before the patch:


```
sage: C = ComplexField()
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 8.57 µs per loop
sage: C = ComplexField(10000)
sage: z = C(1+i)
sage: timeit("z.sqrt()")
125 loops, best of 3: 6.95 ms per loop
```


after the patch:


```
sage: C = ComplexField()
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 2.27 µs per loop
sage: C = ComplexField(10000)
sage: z = C(1+i)
sage: timeit("z.sqrt()")
625 loops, best of 3: 509 µs per loop
```



---

Comment by robertwb created at 2008-10-08 06:47:16

Thanks!


---

Comment by mabshoff created at 2008-10-08 08:43:46

Merged in Sage 3.1.3.alpha3


---

Comment by mabshoff created at 2008-10-08 08:43:46

Resolution: fixed
