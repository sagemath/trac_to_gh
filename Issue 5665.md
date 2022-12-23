# Issue 5665: Bug in ShrinkingGeneratorCipher

Issue created by migration from https://trac.sagemath.org/ticket/5665

Original creator: sbulygin

Original creation time: 2009-04-02 07:54:42

Assignee: kohel

Keywords: stream cipher, shrinking generator

In class ShrinkingGeneratorCipher, function `__call__` the initialization and update of the initial states is buggy. Namely in the peace of code

```
g1 = e1.connection_polynomial()
n1 = g1.degree()
IS_1 = e1.initial_state()
g2 = e2.connection_polynomial()
n2 = g2.degree()
IS_2 = e1.initial_state()
```

the last line 'IS_2 = e1.initial_state()' should be 'IS_2 = e2.initial_state()'. 
Also at the end in

```
  IS_1 = KStream[r-n-1:r-n+n1]
  IS_2 = KStream[r-n-1:r-n+n2]
```

the last line should be 'IS_2 = DStream[r-n-1:r-n+n2]'
The corrected file is attached.


---

Comment by sbulygin created at 2009-04-02 07:55:35

bugs in initialization and update of initial state are fixed


---

Attachment


---

Comment by kohel created at 2009-04-23 09:17:17

Resolution: fixed


---

Comment by kohel created at 2009-04-23 09:17:17

The two changes are necessary and correct.


---

Comment by mabshoff created at 2009-04-23 09:33:03

Thanks for the review David, but tickets only get closed once a patch has actually been merged :).

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 09:33:03

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-04-23 09:33:03

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-04-23 09:34:47

On top of this someone needs to make a proper patch out of this and check in the changes in sbulygin's name. One would also need to check if doctests have been added since that is unclear to me without taking a closer look and comparing to the file that is in 3.4.1.

Cheers,

Michael


---

Comment by kohel created at 2009-04-23 10:34:07

Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. 

Creating a patch seems overkill, since only two characters have changed (1->2 and K->D).  

However, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. 

Cheers,

David


---

Comment by mabshoff created at 2009-04-23 10:40:46

Replying to [comment:6 kohel]:
> Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. 

Well, a fixed ticket no longer appears on the default view and just because someone does give a ticket a positive review does not mean it will be merged since any doctest failure will bounce the ticket right back. Closing tickets once a patch has been merged is the only sane way to keep track of which fix was merged in Sage.

> Creating a patch seems overkill, since only two characters have changed (1->2 and K->D).  

No, creating a patch is essential for credit, etc. 

> However, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. 

It is essential to run doctests and to add additional doctests in case the problem was not previously covered by a doctest. This does not seem to be the case here, but I will find out in the morning.

> Cheers,
> 
> David

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 02:52:18

This ticket needs at least a doctest fix:

```
sage -t -long "devel/sage/sage/crypto/stream_cipher.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/crypto/stream_cipher.py", line 228:
    sage: c.decoding()
Expected:
    '\xac\xfa\xfd\xc6\xa7\xe5\x16\x8f\xa2Q\xb8\xb7\xbe\xab'
Got:
    "t\xb6\xc1'\x83\x17\xae\xc9ZO\x84V\x7fX"
**********************************************************************
1 items had failures:
   1 of  17 in __main__.example_8
```


It would also be nice if someone posted a patch giving credit to Stanislav.

Cheers,

Michael


---

Attachment

based on Sage 4.1.alpha1


---

Comment by mvngu created at 2009-06-26 04:37:28

Only apply `trac_5665.patch`.


---

Comment by mvngu created at 2009-06-26 21:42:04

Note: the patch `trac_5665.patch` is due to Stanislav Bulygin. I produced the patch file from the Python file.


---

Comment by rlm created at 2009-07-04 01:31:08

Resolution: fixed
