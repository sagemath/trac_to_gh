# Issue 1832: change how real(...) is defined in Sage

Issue created by migration from https://trac.sagemath.org/ticket/1832

Original creator: was

Original creation time: 2008-01-18 16:12:15

Assignee: somebody


```


On Jan 18, 2008 7:23 AM, Georg wrote:
> 
> Hi,
> questions concerning numbers, look at the following session
> (sage-2.9.3):
> 
> sage: r = 5/3
> sage: a = 2.5
> sage: type(a)
> <type 'sage.rings.real_mpfr.RealNumber'>
> sage: type(real(r))
> <type 'sage.rings.real_double.RealDoubleElement'>
> sage: type(real(a))
> <type 'sage.rings.real_mpfr.RealNumber'>
> sage: type(RR(r))
> <type 'sage.rings.real_mpfr.RealNumber'>
> 
> so real() converts a rational to a real_double 

real is defined as:
    try: return x.real()
    except AttributeError: return CDF(x).real()
so it's fallback behavior is to create an RDF, if it hasn't
been otherwise defined.  It should be the "real part"
in general, so for the rationals (and integers) it should be defined to
just return the rational number.   Even better, the definition
of the real default method should be changed to try coercing
x to RDF and if that succeeds, just return x itself.

> and a real_mpfr to a
> real_mpfr, what's the difference between these types?  Is a
> real_double just a special case of a real_mpfr with precision 53?  

No.  A real double is a double precision machine real.  It is much
faster than a real_mpfr with precision 53 bits.  However, mpfr's have
better numerical semantics. 

sage: a, b = RDF(3993), RDF(18)
sage: c, d = RR(3993), RR(18)
sage: time for _ in xrange(10^6): e = a*b
CPU times: user 0.29 s, sys: 0.01 s, total: 0.30 s
Wall time: 0.31
sage: time for _ in xrange(10^6): e = c*d
CPU times: user 0.77 s, sys: 0.01 s, total: 0.78 s
Wall time: 0.83
sage: time for _ in xrange(10^6): e = a.sin()
CPU times: user 0.50 s, sys: 0.00 s, total: 0.51 s
Wall time: 0.56
sage: time for _ in xrange(10^6): e = c.sin()
CPU times: user 12.24 s, sys: 1.38 s, total: 13.61 s
Wall time: 14.98

> But
> in this case the variable should be of type real_double?
> Is there a performance difference between real_mpfr of precision 53
> and real_double, and if yes how can one convert to a real_double (from
> real_mpfr with precision 53), like seen above with real() it's not
> poosible, i just found out to do this by RDF(a), so maybe it's a bug
> that real(a) is still a real_mpfr?

real( ... ) means "real part"

> How is the real_double implemented, i guess though mpfr?

No.  It uses GSL for most functionality actually.  CDF for complex
double is similar. 

William

```



---

Attachment


---

Comment by mhansen created at 2008-01-18 23:05:46

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-18 23:05:46

Changing assignee from somebody to mhansen.


---

Comment by ncalexan created at 2008-01-21 20:03:07

I can imagine similar problems arising, but this seems like a reasonable fix.  Apply.


---

Comment by mabshoff created at 2008-01-22 01:28:54

Resolution: fixed


---

Comment by mabshoff created at 2008-01-22 01:28:54

Merged in Sage 2.10.1.alpha1
