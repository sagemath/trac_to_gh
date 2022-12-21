# Issue 1121: improve point counting for curvers over extension fields

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-07 15:57:31

Assignee: was

John Cremona wrote


```
You are right of course -- one should always compute the order over
the smallest field of definition and then use the easy formula to get
the order of E(GF(q^d)) from that of E(GF(q)).

While you are at it you should not stop at the smallest field
containing the coefficients of the given curve, it would be enough to
work over the field containing the j-invariant, plus a little work
deciding which twist your need and all this is as usual a little more
complicated when j=0 or j=1728, or in characteristics 2 and 3.

This feels like reinventing wheels -- i wonder who has done this already?

As for implementation, it is *extremely* ugly to work with floating
point complex numbers for this (as both Graeme and Alex seem to do.
It should be done algebraically!

If n = #E(GF(q)) then a=1+q-n is the trace of alpha =
(a+sqrt(a^2-4*q))/2, and then #E(GF(q^d)) = 1+q^d-trace(alpha^d).  The
trace of the d'th power of alpha is just a resultant calculation.
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/69ebf55ee4f22278/23c61ad57cbff62a

#1119 implements to computing over GF(p) if possible, but it doesn't implement computing over GF(p<sup>m</sup>) if m|n. Also #1119 still relies on floating point arithmetic.


---

Comment by malb created at 2007-11-07 15:59:12

that should be #1120 instead of #1119


---

Attachment

8312 just corrects minor thing in documentation

The Documentation said the cardinality was not cached, but in fact the code does cache.


---

Comment by robertwb created at 2008-02-14 06:40:51

Yep, looks good to me.


---

Comment by mabshoff created at 2008-02-14 09:37:24

Applied 8312.patch to Sage 2.10.2.alpha0


---

Comment by malb created at 2008-02-14 09:54:31

Replying to [comment:2 gmoose05]:
> 8312 just corrects minor thing in documentation
> 
> The Documentation said the cardinality was not cached, but in fact the code does cache. 

I am confused. Does the patch address the ticket?


---

Comment by mabshoff created at 2008-02-14 09:58:48

I don't think that the patch addresses the ticket, it just corrects the issue about caching. So I am removing the `with positive review` - I guess we should have opened another ticket for the documentation issue.

Cheers,

Michael


---

Comment by cremona created at 2008-04-06 11:36:08

The issues raised here have all been sorted under other tickets.  This one can be closed.


---

Comment by mabshoff created at 2008-04-06 14:11:49

Closing this on the recommendation of John Cremona since the issues have all been fixed.


---

Comment by mabshoff created at 2008-04-06 14:11:49

Resolution: fixed
