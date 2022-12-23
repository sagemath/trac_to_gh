# Issue 4023: Sage 3.1.2.alpha3: 32 vs. 64 b bit doctesting issuess for gp

Issue created by migration from https://trac.sagemath.org/ticket/4023

Original creator: mabshoff

Original creation time: 2008-08-31 18:58:50

Assignee: mabshoff

CC:  malb

John Cremona reported:

```
sage -t  devel/sage/sage/interfaces/gp.py 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 266: 
    sage: gp.get_precision() 
Expected: 
    38 
Got: 
    28 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 520: 
    sage: gp.new_with_bits_prec(pi, 100) 
Expected: 
    3.1415926535897932384626433832795028842 
Got: 
    3.141592653589793238462643383 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 244: 
    sage: gp.get_precision() 
Expected: 
    38 
Got: 
    28 
********************************************************************** 
3 items had failures: 
   1 of   6 in __main__.example_10 
   1 of   3 in __main__.example_27 
   1 of   3 in __main__.example_9 
***Test Failed*** 3 failures. 
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2008-09-05 01:38:55

Standard fix (gp has a default precision of 38 on 64-bit architectures, and 28 on 32-bit).

There are more serious pari precision issues tracked at #4064.


---

Comment by mabshoff created at 2008-09-05 01:42:39

Yeah, I had similar changes to submit. But I would like to add a remark to the gp.new_with_bits_prec(pi, 100) that the result is wrong and the issue tracked at #4064.

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2008-09-05 04:02:14

I have looked into the matter of the second doctest failure more carefully and figured out that there were two problems with the function gp.new_with_bits_prec():

1. the code was doing the wrong thing

2. the doctest was testing the wrong thing (but the result was correct)

Basically, asking gp to print out pi was pointless because gp's precision had been reset to its default (so of course it would only print the first 28 or 38 digits).  The new patch fixes the code and the doctests.  I don't have access to a 64-bit machine so I had to produce the 64-bit doctest results by pure thought, so it would be great if someone could actually doctest this.


---

Comment by mabshoff created at 2008-09-05 06:14:21

Patch looks good to me, but we have one doctest failure:

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha5/tmp/sr.py", line 1407:
    sage: s
Expected:
    {k000: 1, k001: 0, k003: 1, k002: 0}
Got:
    {k000: 1, k001: 0, k002: 0, k003: 1}
**********************************************************************
```

The output is identical except that the order has slightly changed. Malb? 

Cheers,

Michael


---

Comment by malb created at 2008-09-05 09:56:44

That's alright, it is a set and thus the order depends on the hash.


---

Comment by mabshoff created at 2008-09-05 10:05:53

Replying to [comment:5 malb]:
> That's alright, it is a set and thus the order depends on the hash.

Ok, with Martin's approval of the sr.py doctest fix this is a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 11:12:21

Merged in Sage 3.1.2.rc0. I also fixed the doctest failure.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 11:12:21

Resolution: fixed
