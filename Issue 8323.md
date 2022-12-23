# Issue 8323: The variable "name" is predefined in Sage

Issue created by migration from https://trac.sagemath.org/ticket/8323

Original creator: roed

Original creation time: 2010-02-22 02:33:45

Assignee: tbd

Try the following:

```
sage: name
'KodairaSymbol'
sage: type(name)
<type 'str'>
```


I'm not sure where this gets imported, but it seems wrong.


---

Comment by craigcitro created at 2010-02-22 05:40:39

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-02-22 05:40:39

It's coming from near line 150 in `sage/all.py`: 


```
#Deprecate the is_* functions from the top level
#All of these functions should be removed from the top level
#after a few releases, and this code should be removed.
#--Mike Hansen 9/25/2008
globs = globals()
from functools import wraps, partial
for name,func in globs.items():
```


... but then `name` and `func` are never deleted. (Ahh, scoping in Python.) Sure enough, `func` is defined, too:


```
sage: func
<function KodairaSymbol at 0x10940daa0>
```


So I'm attaching an obvious patch -- there might be something classier, but this works. (And yes, this is still necessary in Py3.)


---

Comment by zimmerma created at 2010-02-25 15:50:20

After applying the patch, `sage -t` gives the same 22 failures as with vanilla 4.3.3
(see #7773). However it would be good to add one test to check that `name` and `func`
are undefined at start.


---

Comment by zimmerma created at 2010-02-25 15:50:20

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by craigcitro created at 2010-02-25 17:48:54

Changing status from needs_work to needs_review.


---

Comment by craigcitro created at 2010-02-25 17:48:54

Ahh, good point. We don't really have a standard place to put doctests for build/startup stuff, so I picked `sage/misc/misc.py`. If anyone can think of a better place, I'm happy to hear. (I don't think it's worth creating a whole new file for until we have a few more tests.)

I've added a test and a new version of the patch.


---

Comment by zimmerma created at 2010-02-25 18:10:15

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-02-25 18:10:15

> I've added a test and a new version of the patch. 

great: positive review for me.


---

Comment by mvngu created at 2010-03-02 21:02:08

Resolution: fixed
