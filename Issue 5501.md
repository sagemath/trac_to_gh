# Issue 5501: pickling high-precision intervals is broken

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-03-12 15:35:45

Assignee: jkantor

CC:  cwitty

The following explodes in sage 3.4:


```
sage: R = RealIntervalField(4000)
sage: s = 1/R(3)
sage: t = loads(dumps(s))Traceback (most recent call last):
  File "pikltest.py", line 6, in <module>
    t = loads(dumps(s))
  File "sage_object.pyx", line 623, in 
sage.structure.sage_object.loads (sage/structure/sage_object.c:6159)
RuntimeError: ('Unable to convert number to real interval.',
 <built-in function __create__RealIntervalFieldElement_version0>, 
(Real Interval Field with 4000 bits of precision, 
'[a.lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalal0`@`-1 .. 
a.lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalalala
lalalalalalalalalalalalalalalalalalalalalalalalalalalg`@`-1]', 32))
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```


Furthermore, it dumps the contents of dumps(s) to the console, which I'm told is a no-no because when one uses ~20kbits of precision with 24 processes via `@`parallel, the error messages are ridiculously huge.

On a personal note, I'd prefer if my CAS didn't stick its fingers in its ears and chant "lalalala..." whenever it doesn't like what I'm doing.  This is *not* how a mature system should behave.


---

Comment by cwitty created at 2009-03-13 01:12:16

This is presumably due to these lines from mpfi_set_str, in mpfi_io.c (in the MPFI library):

```
  char tmp[1000];

  /* bzero(tmp,1000); */
  memset(tmp,0,1000);

  slen= (int)strlen(s);
  if(slen >=1000) return -1;
```


As a workaround, instead of passing the `RealIntervalFieldElement` x, you could pass (x.parent(), x.lower(), x.upper()); then on the other side, given (parent, lower, upper), reconstruct the original element with parent(lower,upper).


---

Comment by boothby created at 2009-03-13 02:14:39

Wow.  I'll report this upstream.  Your proposed solution looks good to me.


---

Attachment


---

Comment by robertwb created at 2010-01-17 10:22:34

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-17 10:22:34

Yep, pickling the endpoints was the first thought I had as well.


---

Comment by timdumol created at 2010-01-20 10:42:17

LGTM. By the way, what's the upstream report status on this?


---

Comment by timdumol created at 2010-01-20 10:42:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-24 10:58:47

Resolution: fixed
