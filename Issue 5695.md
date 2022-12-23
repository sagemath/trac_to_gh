# Issue 5695: Sgae 3.4.1.rc1: doctest failure in combinat/words/words.py on 32 bit boxen

Issue created by migration from https://trac.sagemath.org/ticket/5695

Original creator: mabshoff

Original creation time: 2009-04-06 18:31:14

Assignee: mabshoff

CC:  hivert saliola

This looks like fallout from #5308:

```
sage -t -long "devel/sage/sage/combinat/words/words.py"     
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py", line 760:
    sage: Words(7,13).cardinality()
Expected:
    96889010407L               
Got:
    96889010407
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc1/devel/sage/sage/combinat/words/words.py", line 763:
    sage: Words(['a','b','c','d','e','f','g'],13).cardinality()
Expected:
    96889010407L               
Got:
    96889010407
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_31
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.4.1.rc1/tmp/.doctest_words.py
	 [18.4 s]
exit code: 1024
```


Trivial patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 18:42:43

Changing status from new to assigned.


---

Attachment

Franco or Florent, since either one of you broke this in #5308 feel free to review this trivial and obvious patch :P

Cheers,

Michael


---

Comment by jsp created at 2009-04-06 18:56:17

OK, I don't want Franco or Florent to be offended.

But this patch is trivial and obvious.

Positive review :)

Jaap


---

Comment by hivert created at 2009-04-06 19:56:57

Oops !!! I solved the problem in #5308 but it seems I completely forgot to update the doctests in words ! One hundred apologies.

By the way since it is not yet merged I can also add my positive review :)

Florent


---

Comment by mabshoff created at 2009-04-06 21:17:11

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 21:17:11

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
