# Issue 1816: rename MPolynomialRing.repr_long method to __str__

Issue created by migration from https://trac.sagemath.org/ticket/1816

Original creator: malb

Original creation time: 2008-01-17 23:38:32

Assignee: malb

Just as symbolic variables behave (and what is the Python-way IIRC):

```
sage: f = x/var('y')
sage: f
x/y
sage: str(f)
'                                       x\r\n                                       -\r\n                                       y'
sage: print str(f)
                                       x
                                       -
                                       y
```



---

Attachment


---

Comment by ncalexan created at 2008-01-20 07:02:52

The patch is fine, and does what it says, but it makes it look like printing a polynomial ring will give this verbose output:

```
sage: P.<x,y,z> = PolynomialRing(QQ,order=TermOrder('degrevlex',1)+TermOrder('lex',2)) 
sage: print P
Multivariate Polynomial Ring
Base Ring : Rational Field 
Size : 3 Variables 
Block  0 : Ordering : degrevlex 
```

That's *not* okay -- way too much by default!


---

Comment by malb created at 2008-01-20 16:27:03

Because I disagree with Nick's verdict, I forwarded this to [sage-devel]:

  http://groups.google.com/group/sage-devel/browse_thread/thread/612b3ec4a61310fa

I figure, that this is more a design choice than a correctness issue and thus it should be discussed on [sage-devel] rather than here. I hope that's okay with you, Nick.


---

Comment by malb created at 2008-02-27 00:03:39

My impression is: The verdict on [sage-devel] was overall negative, so I propose to close this ticket as `wontfix`.


---

Comment by malb created at 2008-04-01 12:06:41

Resolution: wontfix
