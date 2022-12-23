# Issue 2229: sage-2.10.2.alpha1 -- breakage in new totally_rel.py

Issue created by migration from https://trac.sagemath.org/ticket/2229

Original creator: was

Original creation time: 2008-02-20 07:03:35

Assignee: was

I don't know about this code at all, but something is messed up:

```
         [2.8 s]
sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py**********************************************************************
File "totallyreal_rel.py", line 654:
    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        [NumberField(ZZx(_[i][Integer(1)]), 't').is_galois() for i in range(len(_))]###line 654:
    sage: [NumberField(ZZx(_[i][1]), 't').is_galois() for i in range(len(_))]
    TypeError: 'int' object is unsubscriptable
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_totallyreal_rel.py
         [50.8 s]

```



---

Comment by craigcitro created at 2008-02-20 20:08:34

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-02-20 20:08:34

So I don't see this doctest failure on my machine, but looking at the doctests, they're clearly nonsense (i.e. the above error *should* be showing up on my machine). I'm very curious why it doesn't.

In any event, the attached patch *should* fix it.


---

Comment by craigcitro created at 2008-02-20 20:08:34

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-02-20 20:15:16

The patch fixes the doctest failure, positive review.


---

Comment by mabshoff created at 2008-02-20 20:16:20

Resolution: fixed


---

Comment by mabshoff created at 2008-02-20 20:16:20

Merged in Sage 2.10.2.alpha2
