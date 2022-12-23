# Issue 4142: limit bug: should be -Infinity, but gives +Infinity

Issue created by migration from https://trac.sagemath.org/ticket/4142

Original creator: ddrake

Original creation time: 2008-09-18 06:14:18

Assignee: burcin

As discussed in http://groups.google.com/group/sage-devel/browse_thread/thread/7afc9f414413906 , some limits are not evaluated correctly:


```
sage: f = sqrt(1-x^2)
sage: g = diff(f, x); g
-x/sqrt(1 - x^2)
sage: limit(g, x=1, dir='below')
+Infinity
```


The last command should give -Infinity, of course, since `f` is a semicircle. At the other endpoint, the limit is correct (+Infinity). 


---

Comment by kcrisman created at 2009-09-29 16:02:44

As it happens, this is still a problem in Sage 4.1.x - but the problem is somewhat more subtle than just some Maxima bug, or Sage incorrectly parsing Maxima output:

```
(%i1) limit(-x/sqrt(1-x^2),x,1,minus);
(%o1)                                            infinity
```

BUT Maxima's infinity is not Sage's infinity; it is the complex infinity!  If the answer is +infinity, Maxima would return 'inf'.   I've asked the Maxima list about this, so we'll see what happens.


---

Comment by kcrisman created at 2009-10-05 18:13:48

This is fixed in the latest Maxima CVS version, so whenever we upgrade again, this one will hopefully be closed.

```
Maxima 5.19post http://maxima.sourceforge.net
using Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) limit(-x/sqrt(1-x^2),x,1,minus);
(%o1)                                minf
```



---

Comment by kcrisman created at 2009-12-22 17:18:49

This is now correct in Maxima 5.20.1, so it just needs a doctest once the new spkg is merged.


---

Comment by kcrisman created at 2009-12-22 21:27:30

The patch here depends on the spkg at #7745 to work properly.  It also depends on the patch there, and at #6423, but will probably still apply if someone forgot to apply them first.


---

Comment by kcrisman created at 2009-12-22 21:27:30

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-22 21:27:45

Based on 4.3.alpha1


---

Attachment

The spkg and patch at #7745 fix this problem, and the doctest passes. Positive review; this can be merged as soon as #7745 is in.


---

Comment by ddrake created at 2009-12-23 08:12:20

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 03:09:14

Resolution: fixed
