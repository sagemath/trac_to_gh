# Issue 4001: [with patch, needs review] ZZ['x'].gen()^(2^20) should work but doesn't

Issue created by migration from https://trac.sagemath.org/ticket/4001

Original creator: malb

Original creation time: 2008-08-30 12:36:40

Assignee: somebody

On [sage-devel] Bill Hart wrote:

> I don't seem to be able to create large polynomials in SAGE currently.
> If I try to create a polynomial f(x)=x<sup>2**20</sup> where I am working in a
>  genuine univariate polynomial ring over ZZ, it just tells me it is out
> of memory.

> It looks like a message from the memory manager from FLINT, but FLINT
> really has no problem creating polynomials of this size. So I'm a bit
> puzzled as to what is going on there.

> Magma, by the way, can create polynomials up to length about 2<sup>28</sup> and
> can store polynomials (as a result of a computation) up to about
> length 2<sup>30</sup>.

> I was interested in seeing if SAGE could do better than that. However,
> not being able to create a polynomial of length 1 million seems really
> limiting to me. Does someone know why this is?


---

Attachment


---

Comment by cremona created at 2008-08-30 16:03:32


```
sage: x^(2^20) 
1048576 
```


I think you have set the 1st coefficient to exp instead of the other way round!


---

Comment by malb created at 2008-08-30 16:18:07

Wow, I even doctested the wrong behavior. No clue, how I managed to miss that. Sorry. New patch coming up.


---

Attachment

Actually, It was only a copy'n'paste error in the doctest, the actual implementation was fine. I was just too lazy to run the doctest afterwards, that should teach me.


---

Comment by cremona created at 2008-08-30 16:30:19

... and to be honest I had not applied the patch, just read it!

Patch applies ok to 3.1.2.alpha2, doctests in sage.rings.polynomial all pass.

By the way, `x<sup>(2</sup>25)` works ok too, but `x<sup>(2</sup>30)` causes Sage to crash:

```
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Does that mean that your new special code should have _sig_on, _sig_off?


---

Attachment

Replying to [comment:4 cremona]:
> Does that mean that your new special code should have _sig_on, _sig_off?

Yes, I've just updated the patch. I'm not going to write a doctest for this, since it unnecessarily slows down the user's computer by filling up his/her RAM ... on a related note: Incredible in how many ways I can screw up such a short patch.


---

Comment by cremona created at 2008-08-30 17:07:38

Looks good to me.  Note for mabshoff: apply *only* the last of the three patches.


---

Comment by mabshoff created at 2008-08-30 18:11:16

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 18:11:16

Merged 4001_flint_gen_power.3.patch in Sage 3.1.2.alpha3
