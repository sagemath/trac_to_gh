# Issue 7475: bug pickling ZZ.residue_field's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-16 17:41:54

Assignee: tbd


```
sage: K = ZZ.residue_field(2)
sage: dumps(K)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()

TypeError: 'NoneType' object is unsubscriptable
sage: K = ZZ.residue_field(3)
sage: dumps(K)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/flat.local/44250/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.dumps (sage/structure/sage_object.c:7951)()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.FiniteField.__reduce__ (sage/rings/ring.c:12800)()

TypeError: 'NoneType' object is unsubscriptable
```



---

Comment by was created at 2009-11-16 17:42:07

Changing component from misc to pickling.


---

Comment by was created at 2009-11-16 17:42:07

Changing assignee from tbd to was.


---

Attachment

The pickle in a different system


---

Comment by itaibn created at 2012-02-26 04:49:43

I tested this and the bug doesn't appear in my system. I attached the pickle and the result of `pickle_explain` on the pickle.


---

Comment by itaibn created at 2012-02-26 04:50:17

An explanation of the pickle


---

Attachment


---

Comment by itaibn created at 2013-09-03 10:19:54

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-02-03 07:25:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-02-03 07:25:44

Looks good.


---

Comment by vbraun created at 2014-02-03 22:59:33

Resolution: fixed
