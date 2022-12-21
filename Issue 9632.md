# Issue 9632: System-dependent term order for printed expressions

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-29 06:16:00

Assignee: burcin

CC:  burcin cwitty ddrake jhpalmieri kcrisman

The order in which the terms in some symbolic expressions are printed depends on the platform/system.  For example, evaluating `cos(x) + zeta(x)` yields

 * `zeta(x) + cos(x)` on Linux
 * `cos(x) + zeta(x)` on OS X

in Sage 4.4.4 and 4.5.2.alpha{0,1}, at least.

Please see #9582 for some details and discussion.


---

Comment by burcin created at 2010-11-18 15:40:36

#10282 is a duplicate of this issue.

The patches attached to #9880 fix this.


---

Comment by burcin created at 2010-11-18 15:40:36

Changing status from new to needs_work.


---

Comment by kcrisman created at 2010-11-18 16:11:24

#10282 almost certainly is the same thing.


---

Comment by kcrisman created at 2011-01-13 03:15:06

When this is closed (which would hopefully happen with #9880 integrated), let's be sure to write doctests for both this ticket and #10282, which would just be to say that 

```
sage: psi(1,1/3)*log(3)
log(3)*psi(1, 1/3)
```

is the same on all systems, in addition to the `zeta(x)+cos(x)` example here.


---

Comment by burcin created at 2013-07-01 00:49:12

Changing status from needs_work to needs_review.


---

Attachment

This was fixed by #9880. [attachment:trac_9632-doctests.patch] adds doctests.


---

Comment by vbraun created at 2013-07-12 13:24:56

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-07-31 12:53:09

Resolution: fixed
