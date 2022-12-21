# Issue 4807: bug in exponential integral

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-12-16 04:49:43

Assignee: burcin

This was reported by M. Yurko in an email to sage-support:

here are some examples of what I did:
#First, an example of the bug

```
Ei(20)
Output: 25615646.4145 + 6.28318530718*I 
```

it should instead be just 25615646.4145

```
Ei(19)
Output: 9950907.25105 
```

the error doesn't occur here

```
-exponential_integral_1(-20).n(digits=50)
Output: 25615652.664056588 
```

here the bug doesn't occur, although the
code for exponential_integral_1  loses a lot 
of accuracy by converting the number returned 
from PARI into a float, so it has much less
accuracy

```
-pari(-20).eint1().n(digits = 50)
Output: 2.5615652664056588773746625520288944244384765625000e7 }}}
here the full accuracy from PARI is preserved
the following shows the difference in the speed 
of the two methods 

the current implementation
{{{
%time
for i in srange (1,10^6):
   num = Ei(10)
Output: CPU time: 51.64 s,  Wall time: 51.81 s
}}}
the time of PARI's implementation
{{{
%time
for i in srange (1,10^6):
   num = pari(-i).eint1()
Output: CPU time: 20.12 s,  Wall time: 20.32 s
}}}
PARI's implementation seems to be more than twice as fast

William Stein added this:

A quick remark: The Pari Ei only works with *real* input, whereas the scipy one works with complex input.
The Sage function will have to fixed in the meantime or
at least as a bare minimum have a big comment at the top explaining that there is a bug.


---

Comment by mabshoff created at 2008-12-16 09:03:34

The solution seems to be the following from the Scipy mailing list:

```
Robert Kern wrote:
> >
> > Ah, I think found it using this clue. It's a bug in SPECFUN. The
> > "IMPLICIT DOUBLE PRECISION" statement is missing "A" so A0 is REAL
> > rather than DOUBLE. Fixing that makes both of them go through the same
> > code path. Can you change the line to this:
> >
> >           IMPLICIT DOUBLE PRECISION (A,D-H,O-Y)
> >
> > in your specfun.f file, and rebuild scipy?
> >   

Sorry for the delay: you're right, this seems to fix the problem, at
least for me. The example now gives me:

(25615628.4058-3.14159265359j)
(25615630.8316-3.14159265359j)

cheers,

David
```



---

Comment by was created at 2009-01-24 12:11:44

Mike Hansen observes that one could implement Ei in *general* and with arbitrary precision by using the library "mpmath", which just happens to already be in Sage.  That library can be made fast if we included gmpy or hack it to use our integers.


```
sage: import sympy.mpmath as a
sage: a.ei(complex(2r,3r))
mpc(real='-0.3615519445996403', imag='5.2705484358136943')
sage: a.mp.prec = 1000
sage: a.ei('20.1000000000000000000000000000000000000000000000000000000000000000000')
mpf('28160453.3833994153950012661507902048168259435687244439573563929054452528467189574883919398422855919158391624626109323992762879680063235714851415880668470266487381859473426294489489391883476549497496312702303650499027252495570681212146125439331860229395375385300595969122490770779143241578042047266845835')
```


So this is an alternative approach to fixing this bug and greatly improving


---

Comment by fredrik.johansson created at 2009-02-05 22:18:21

The exponential integral implementation in mpmath was recently improved to work for large arguments too:


```
>>> mp.dps = 50
>>> ei(mpc(10**30, 10**40))
mpc(real='-2.2944454721211223524123643204705731535186663746073664e+4342944819032
51827651128918876', imag='3.310554099386694677220121243704912443715898934912981e
+434294481903251827651128918876')
```


However, it is not optimized at all at the moment, and is probably many times slower than PARI. ei in mpmath is about 4-8 times slower than the cosine integral ci (which is almost the same function as ei, so properly optimized they should be about equally fast). [mpmath.ci(x) for x in range(10**6)] takes 132 seconds on my laptop.

If I find the time, I'll try to both optimize and assure accuracy everywhere for all the incarnations of exponential, trigonometric and hyperbolic integrals in mpmath for the next version.


---

Comment by mhansen created at 2009-06-04 23:39:45

Changing assignee from burcin to fredrik.


---

Comment by myurko created at 2009-09-29 20:08:18

Change implementation to mpmath and PARI to fix bug


---

Attachment


---

Attachment

I posted a new patch with a few changes to the original patch.  I'm using mpmath for everything since for uniformity and because it handles the increased precision.  Also, I changed the second example to highlight the branch cut and added the failing example in the ticket as a test.

Michael, if you're okay with my changes, then you can mark the patch as positive review.  I left the patch in your name.


---

Comment by myurko created at 2009-09-30 17:50:03

Your patch looks good. On second thought, it probably is better to just use mpmath since is_RealNumber doesn't really do what I had originally thought. That and mpmath only seems to be getting faster.


---

Comment by mhansen created at 2009-10-15 05:24:53

Resolution: fixed
