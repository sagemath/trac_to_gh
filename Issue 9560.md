# Issue 9560: Symbolic expressions don't do arithmetic with bools nicely

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2010-07-21 09:06:17

Assignee: burcin

CC:  cwitty mstreng kcrisman

It's convenient to assume that True and False are equivalent to 1 and 0 in Python, but this doesn't work as expected with symbolic expressions:


```
sage: SR(5) + True; SR(5) * True; SR(5) - True
2
1
0
sage: 5 + True; 5 * True; 5 - True
6
5
4
```



---

Comment by burcin created at 2010-07-24 21:03:15

I understand that this is a Python convention, but I can't think of any situation where it would be useful. IMHO, adding a bool to an integer should be a type error. I'll raise the issue on sage-devel.


---

Comment by burcin created at 2010-07-24 21:03:15

Changing status from new to needs_info.


---

Comment by mstreng created at 2010-07-25 08:54:07

See
[http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd](http://groups.google.com/group/sage-devel/browse_thread/thread/2821c770f3c62efd) and [http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d](http://groups.google.com/group/sage-devel/browse_thread/thread/43798faef815a86d)


---

Attachment


---

Comment by burcin created at 2010-09-25 20:31:39

Changing status from needs_info to needs_review.


---

Comment by burcin created at 2010-09-25 20:31:39

attachment:trac_9560-symbolic_bool_arith.patch _fixes_ this problem...


---

Comment by burcin created at 2011-05-30 21:08:39

This is a trivial patch. I don't understand why it hasn't been reviewed all this time. Fredrik, can you review this?


---

Comment by kcrisman created at 2011-06-08 18:00:38

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-08 18:00:38

Probably it hasn't been reviewed for the same reason as people disagreed with it in the past - not really worth the effort :)

My favorites:

```
sage: e-True
e - 1
sage: pi+False
pi
```


Anyway, positive review.  It would have been nice to have an example with `False`, but that's not worth holding this up any further.


---

Comment by jdemeyer created at 2011-06-14 21:08:10

Resolution: fixed
