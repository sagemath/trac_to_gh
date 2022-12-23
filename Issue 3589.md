# Issue 3589: numerical noise -- number_field.py

Issue created by migration from https://trac.sagemath.org/ticket/3589

Original creator: was

Original creation time: 2008-07-07 20:31:16

Assignee: failure


```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/mariah/sage/sage-3.0.4.alpha2-x86-Linux-fc8/tmp/number_field.py",
line 3630:
   sage: K.embeddings(CC)
Expected:
   [
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947436 - 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947436 + 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> 1.25992104989487
   ]
Got:
   [
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947437 - 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947437 + 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> 1.25992104989487
   ]
```



---

Comment by mabshoff created at 2008-07-07 20:33:05

This is all mine!

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 20:33:05

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-07-07 20:33:05

Changing status from new to assigned.


---

Attachment


---

Comment by craigcitro created at 2008-07-07 21:55:26

Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?


---

Comment by mabshoff created at 2008-07-07 21:56:42

Replying to [comment:3 craigcitro]:
> Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?

No, we should only kill the digits needed, not any more. Otherwise numeric stability would go out the window :)

Cheers,

Michael


---

Comment by was created at 2008-07-07 22:35:59

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 23:00:48

Merged in Sage 3.0.4.rc0
