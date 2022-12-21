# Issue 4132: complex arithmetic passes via pari

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-16 04:58:32

Assignee: somebody

Passing through pari for every simple operation is probably unnecessary and slow...


---

Comment by was created at 2008-09-16 17:53:08

Clarification: By "every simple operation" robertwb does not mean "arithmetic operations", which don't use PARI at all.  He means special functions like, exp, sin, Riemann zeta, etc. 

Robert, what do you propose to use instead of pari for these?  In some cases you can implement things building on what is in mpfr...


---

Comment by was created at 2008-09-16 17:53:08

Changing type from defect to enhancement.


---

Comment by robertwb created at 2008-09-16 18:26:02

Yes, thanks for the clarification. I meant for many of them one could implement them directly against mpfr. For example:


```

include "sage/rings/mpfr.pxi"
from sage.rings.complex_number cimport ComplexNumber

def my_exp(ComplexNumber self):
    cdef ComplexNumber z = self._new()
    cdef mpfr_t r
    mpfr_init2(r, self._prec)
    mpfr_exp(r, self.__re, GMP_RNDN)
    mpfr_cos(z.__re, self.__im, GMP_RNDN)
    mpfr_mul(z.__re, z.__re, r, GMP_RNDN)
    mpfr_sin(z.__im, self.__im, GMP_RNDN)
    mpfr_mul(z.__im, z.__im, r, GMP_RNDN)
    mpfr_clear(r)
    return z
```


Then


```
sage: a = CC.pi() + CC.0/3
sage: my_exp(a) == a.exp()
True
sage: timeit("a.exp()")
625 loops, best of 3: 514 µs per loop
sage: timeit("my_exp(a)")
625 loops, best of 3: 16.1 µs per loop
sage: 514/16.1
31.9254658385093
```


This could be low-hanging fruit for a new developer.


---

Comment by AlexGhitza created at 2008-09-25 22:05:01

Changing assignee from somebody to AlexGhitza.


---

Comment by AlexGhitza created at 2008-09-25 22:05:10

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-09-28 09:33:45

The attached patch does the following:

 * based on Robert's example, gets rid of Pari calls in cos, cosh, sin, sinh, tan, tanh, exp, sqrt, nth_root, !__pow!__
 * adds csc() and sec()
 * adds a !__nonzero!__() method to speed up is_zero()
 * fixes doctests that were affected by these changes

The patch is currently based on 3.1.3.alpha1, and I'm putting it out as such so that it can be reviewed.  I am aware of some interaction with patches that were merged in alpha2, so I will rebase it once alpha2 is out.


---

Comment by robertwb created at 2008-09-28 10:17:33

Thanks. For the most part it looks good. Here's some suggestions though: 

 * Sqrt(x) for negative x should be pure imaginary, even if a special case is needed. 
 * Calling `a.__invert__()` manually is a Python call, use `~a` instead. 
 * There seems to be a regression of accuracy in some of these examples. And some give totally different answers! Ideally, none of the doctests should have to change--and if any of them do there should be an explanation as to why the new answer is the correct one (if there are ones your not sure on, feel free to ask). 
 * some benchmarking would be good, especially for some of the more complicated ones like tan, or even sqrt. You _should_ be faster, but it's best to be safe.


---

Attachment

I have replaced the old patch with one that addresses the first two points made above.  I had actually done benchmarks while writing the code, and they're now listed further down in this comment.

As for the point on accuracy: I guess the issue is elliptic_logarithm, which was somewhat broken before this patch and is still broken now (see #4214); this has nothing to do with this ticket, though.

Timings after/before the patch (z was chosen randomly):


```
sage: z = CC(0.588296734970724 - 0.918562568630843*I)
sage: z
0.588296734970724 - 0.918562568630843*I
sage: timeit("z.is_zero()")                          
625 loops, best of 3: 901 ns per loop    # was 11.7 µs
sage: timeit("z^(2/3)")
625 loops, best of 3: 80 µs per loop     # was 110 µs
sage: timeit("z.csch()")
625 loops, best of 3: 18.2 µs per loop   # was 70.4 µs
sage: timeit("z.sech()")
625 loops, best of 3: 18.3 µs per loop   # was 70.2 µs
sage: timeit("z.cotan()")
625 loops, best of 3: 24.6 µs per loop   # was 52.5 µs
sage: timeit("z.cos()")  
625 loops, best of 3: 21.9 µs per loop   # was 50.2 µs
sage: timeit("z.cosh()")
625 loops, best of 3: 16.9 µs per loop   # was 50.9 µs
sage: timeit("z.sin()") 
625 loops, best of 3: 22.1 µs per loop   # was 50.2 µs
sage: timeit("z.sinh()")
625 loops, best of 3: 17.2 µs per loop   # was 51.3 µs
sage: timeit("z.tan()") 
625 loops, best of 3: 22.9 µs per loop   # was 52.8 µs
sage: timeit("z.tanh()")
625 loops, best of 3: 17.8 µs per loop   # was 51.8 µs
sage: timeit("z.argument()")
625 loops, best of 3: 26.4 µs per loop   # was 36.3 µs
sage: timeit("z.exp()")     
625 loops, best of 3: 10.8 µs per loop   # was 49.2 µs
sage: timeit("z.sqrt()")
625 loops, best of 3: 34.4 µs per loop   # was 44.1 µs
sage: timeit("z.nth_root(20)")
625 loops, best of 3: 56 µs per loop     # was 94.1 µs
sage: timeit("z.nth_root(20, all=True)")             
625 loops, best of 3: 232 µs per loop    # was 537 µs
```



---

Comment by robertwb created at 2008-09-29 18:41:28

Nice work. You've probably noticed by now that the trig operations are expensive, so you could possibly shave 25% of some of the calls where you compute both sinh and cosh by using the identity

    cosh(x) = sqrt(1+sinh(x)).

On the note of expensive trig, might I suggest a faster sqrt 


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
    # z = x + yi = (a+bi)^2
    # expand, substitute, solve (note that a is nonzero)
    # a^2 = (x + sqrt(x^2+y^2))/2
    cdef mpfr_t a2
    mpfr_init2(a2, self._prec)
    mpfr_hypot(a2, self.__re, self.__im, rnd)
    mpfr_add(a2, a2, self.__re, rnd)
    mpfr_mul_2si(a2, a2, -1, rnd)
    # a = sqrt(a2)
    mpfr_sqrt(z.__re, a2, rnd)
    # b = y/(2a)
    mpfr_div(z.__im, self.__im, z.__re, rnd)
    mpfr_mul_2si(z.__im, z.__im, -1, rnd)
    mpfr_clear(a2)
    if all:
        return [z, -z]
    else:
        return z
```


which should run in 3 or 4 µs with 53 bits, and an even more significant improvement further out. 

This patch is very good, exactly what I wanted when I wrote the ticket, so thanks. The only thing that _needs_ to change for a positive review is I noticed in several case you write `long(n)` when you want an unsigned long. What this does is create a python int, call the python type "long" on it to get a python long, then extract that as a c long. In summary, just write `n` to get a C [unsigned] long just as you would in C. (This is a common confusion with Cython, as the C long and python long are totally different things.)


---

Comment by robertwb created at 2008-09-29 18:48:18

On the sinh/cosh comment, I should note that this is what mpfr_sin_cos does, though in that case more care needs to be taken to make sure enough precision is obtained.


---

Comment by robertwb created at 2008-09-30 00:49:19

I keep replying to myself, but I realized while I was sitting in class today that my sqrt function has numerical instability near the branch cut. I've got a fix, perhaps I should post it as a new patch on top of the one you posted.


---

Comment by AlexGhitza created at 2008-09-30 04:18:40

apply after the first patch


---

Attachment

Hi Robert,

Thanks for looking at this so carefully!  I have uploaded an additional patch that gets rid of the long's and avoids computing cosh's as you suggested.  This does indeed speed things by about 1/4.  Having seen your other comment, can I leave it to you to make sqrt fast?  I tried the code you posted above and it is really fast, but I didn't look into stability questions.

On a related note, I emailed Paul Zimmermann to ask if MPFR could get a function mpfr_sinh_cosh() sometime in the future.  Then I stumbled upon his library MPC (see http://www.multiprecision.org/mpc/ ).  Should we start thinking about using this as the backbone for arbitrary precision complex numbers, the same way we use MPFR for real numbers?


---

Comment by mabshoff created at 2008-09-30 12:02:44

I would suggest we move sqrt to another ticket and merge the code (assuming the changes Alex made are satisfactory to Robert) in 3.1.3.alphaX now. No point in letting this patch potentially bitrot :)

Cheers,

Michael


---

Comment by robertwb created at 2008-09-30 20:54:34

Yes, for sure lests get this in. 

Follow-up sqrt ticket at #4225. As for MPC, I'd never heard of it. Certainly something to keep our eyes on.


---

Comment by mabshoff created at 2008-09-30 23:48:16

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-30 23:48:16

Resolution: fixed
