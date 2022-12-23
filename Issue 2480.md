# Issue 2480: problem parsing arguments to NumberField.order()

Issue created by migration from https://trac.sagemath.org/ticket/2480

Original creator: ncalexan

Original creation time: 2008-03-12 03:19:59

Assignee: was

CC:  ncalexan robertwb mhansen

Keywords: number field order arguments


```
sage: y = ZZ['y'].0; K = NumberField(y^4 + 4*y^2 + 2, 'a'); K
Number Field in a with defining polynomial y^4 + 4*y^2 + 2
sage: B = K.integral_basis()
sage: B
[1, a, a^2, a^3]
sage: K.order(B)
Order in Number Field in a with defining polynomial y^4 + 4*y^2 + 2
sage: K.order(gens=B)
+Infinity
```



---

Comment by davidloeffler created at 2009-07-20 19:57:01

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:57:01

Changing component from number theory to number fields.


---

Comment by craigcitro created at 2010-01-20 06:23:18

This wasn't so bad -- the problem was that `gens=` put the list of gens in the `kwds` dict, instead of in the `*`-argument. I've attached a fix, but I'd love for someone to tell me if deleting `gens` out of the `kwds` dict is sufficiently pythonic. (If you don't, the call to `absolute_order_from_ring_generators` rightfully complains that `gens` is specified twice.) Another option would be to reassign `kwds['dict']` at the end, but I don't think that's any nicer. (In fact, that might be epsilon slower, since it's another argument to unpack from the dictionary on the other side.)

Also, the comment block in the docstring *really* looks like something was accidentally cut off at some point. Amusingly, this isn't the case: I actually dug through the hg logs, and it was really committed just like that.


---

Comment by craigcitro created at 2010-01-20 06:23:18

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-20 06:24:51

Mike and Robert, I'm adding you on the cc so that you can tell me if I'm being sufficiently pythonic. `:)`


---

Comment by mhansen created at 2010-01-20 07:00:50

Hey Craig,


```
gens = kwds.pop('gens')
```


is probably better.


---

Comment by mhansen created at 2010-01-20 07:05:08

Err,


```
gens = kwds.pop('gens', args)
```



---

Attachment

Nice. New patch with Mike's suggestion incorporated posted.


---

Comment by mhansen created at 2010-01-20 07:16:08

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 03:22:20

Resolution: fixed
