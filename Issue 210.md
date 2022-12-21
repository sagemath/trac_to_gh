# Issue 210: discrete log

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-23 20:48:16

Assignee: somebody


```
From David Kohel:
> ... dlog in SAGE mod p is slow.
 
Anyway, yes, PARI has a function znlog, which should be very fast:
 
    gp.znlog
 
I'll have to add it to the PARI interface (libs/pari/gen.pyx) then that should
give a very fast implementation mod p for p a not-too-big prime.  E.g.,
 
--------------------
 
sage: p = 2^32+61
sage: a = gp.znprimroot(p); a
Mod(2, 4294967357)
sage: time gp.znlog(97, a)
498735128
CPU time: 0.00 s,  Wall time: 0.05 s
 
--------------------
 
I'm really glad I'm not writing everything in SAGE from scratch!
 
If somebody on sage-dev sends me a patch that does what you want (see email below)
instead of me having to do it, that would be nice...  I won't work
on this until probably a day from now...
 
  -- William
 
 
On Mon, 22 Jan 2007 21:51:52 -0800, David R. Kohel <kohel`@`maths.usyd.edu.au> wrote:
 
> Hi William, David,
>  
> I produced the following baby examples in Magma for use in my course.
>  
> First a prime for which p-1 is smooth:
>  
> sage: p = 2^32+15
> sage: (p-1).factor()
> 2 * 3^2 * 5 * 131 * 364289
>  
> Then one containing a "large" prime factor:
>  
> sage: p = 2^32+61
> sage: (p-1).factor()
> 2^2 * 1073741839
>  
> Both should take relatively trivial time to solve discrete logarithms,
> but the former "should" recognize by initial trial division that the
> problem is much easier.
>  
> Unfortunately the problem in my book doesn't come back snappily:
>  
> sage: FF = FiniteField(p)
> sage: c = FF(4294967356)
> sage: x = FF(2)
> sage: c.log(x)
>  
> This gets down to the following function:
>  
>  return arith.discrete_log_generic(self, a, n) # TODO update this function
>  
> which does a BSGS (not even Pollard rho).
>  
> Shouldn't Pari or gmp have a more reasonable implementation?
>  
> This is at the level of IntegerMod_abstract rather than finite fields.
>  
> --David
>  
>  
```



---

Attachment


---

Comment by cremona created at 2008-04-04 09:01:28

The attached patch 9124.patch (based on 2.11) implements several completely generic group algorithms, including discrete log, which goes some way towards the issues raised in this ticket.

Many of these functions were first written for elliptic curves over finite fields and then made generic.  They work in additive and multiplicative groups.  There is one new file sage/groups/generic.py;  some older versions which used to be in sage/rings/arith.py have been removed;  other changes are just those necessary for all doctests to pass.

So far I have not attepmted to use these functions everywhere they could be (even in the elliptic curve code) since I wanted this to be reviewed first.

On specific question:  would this generic code benefit from being done in cython?  If so that would be very well worth doing.


---

Comment by mhansen created at 2008-04-04 21:23:02

Excellent work!  The code looks nice and is well-documented.  All tests pass as well.


---

Comment by mabshoff created at 2008-04-04 21:43:44

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 21:43:44

Merged in Sage 3.0.alpha1
