# Issue 7007: generator of RR['t'] has a float attached

Issue created by migration from https://trac.sagemath.org/ticket/7007

Original creator: jason

Original creation time: 2009-09-25 01:29:49

Assignee: tbd


```
[20:22] <jason-> here's something funny:
[20:22] <jason-> sage: QQ['t'].gen()
[20:22] <jason-> t
[20:22] <jason-> sage: RR['t'].gen()
[20:22] <jason-> 1.00000000000000*t
[20:23] <jason-> what's the extra 1.0000000 in there for?
[20:24] <jason-> that means that I get a very funny variables() function:
[20:24] <jason-> sage: R.<t>=RR[]
[20:24] <jason-> sage: (t^2).variables()
[20:24] <jason-> (1.00000000000000*t,)
```



---

Comment by jason created at 2009-09-25 01:31:02

Same problem: 

```
sage: RDF['t'].gen(0)
1.0*t
```



---

Comment by kcrisman created at 2009-09-29 18:15:32

This is nice, but it's a little troubling that it returns things looking "exact" that aren't actually exact.   Are there any Sage defaults for this?


---

Comment by kcrisman created at 2009-09-29 18:56:44

Maybe the more natural fix to this is to change symbolic/expression_conversions.py in PolynomialConverter.__init__ , where instead of checking repr(v) one would check ring.base_ring()(1)*v, I think.  For this to work, there needs to be consistency in the representations of these, of course.

However, as it turns out, somebody (Pynac?) simplifies like this patch does already, but for the symbolic ring, though only for the case with Ring(1), not Ring(2) or others.

```
sage: RR(1)*x
x
sage: RR(2)*x
2.000..000*x
```

Reverting that to at least printing 1.0 (and cutting off the extra zeros, which happens for RDF) seems to be the best strategy.  Then one could change PolynomialConverter.  But I don't know how to fix Pynac representations of this kind.

Incidentally, note that #5755 probably will be fixed by this ticket, one way or another (the current patch fixes it, though as noted above not in a manner to my liking).


---

Attachment


---

Comment by jason created at 2009-09-29 20:05:15

After talking on IRC, I think this patch is okay.  In Sage, there is no such thing as the pure variable in this case; the variable is the polynomial 1.0000000*x.  As such, I think it's fine to extend the printing conveniences to 1.0000*x that are currently given to 1*x.

Plus this fixes at least two issues (here and #5755).


---

Comment by mhansen created at 2009-10-15 07:10:49

Resolution: fixed
