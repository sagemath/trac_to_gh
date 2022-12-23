# Issue 4111: [with patch, needs review] move QQ to new coercion model

Issue created by migration from https://trac.sagemath.org/ticket/4111

Original creator: robertwb

Original creation time: 2008-09-14 01:30:08

Assignee: robertwb

This ticket depends on #4058


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Patches rebased against 3.1.2.


---

Comment by mhansen created at 2008-09-24 07:07:18

Looks good and passes tests for me.  Excellent work getting this patch made!


---

Comment by mabshoff created at 2008-09-24 08:00:54

Robert,

unfortunately I cannot get the patches to apply cleanly and there are various rejects. Sage 3.1.3.alpha1 should be out in a few hours. Could you please rebase them against that release and I will make sure they go in first. 

Cheers,

Michael


---

Comment by robertwb created at 2008-09-24 08:03:00

Argh... I just rebased these against 3.1.2... 

OK, I'll rebase them again (shouldn't be too hard).


---

Comment by robertwb created at 2008-09-24 17:19:30

I got a single reject in 4111-coerce-RR.patch, which I resolved, and some fuzz in 4111-coerce-QQ.patch, which I'm reposting. These should all apply fine against 3.1.3.alpha1 now.


---

Comment by robertwb created at 2008-09-24 17:20:01

against 3.1.3.alpha1


---

Attachment

against alpha 3.1.3.alpha1


---

Comment by robertwb created at 2008-09-24 17:22:40

The order to apply is QQ, RR, simplify, CC.


---

Comment by mabshoff created at 2008-09-25 00:10:28

Robert,

I merged the four patches and the only issue is the following:

```
sage -t -long devel/sage/sage/rings/real_mpfr.pyx           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/real_mpfr.py", line 1900:
    sage: RR(-1.234567)._pari_()
Expected:
    -1.2345670000000000000
Got:
    -1.2345670000000000001
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_58
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.alpha2/tmp/.doctest_real_mpfr.py
         [10.8 s]
```

I don't changing the doctest is the solution here since the "Real Number Inputs Improved" patch from 3.1.2 was supposed to fix this. Or am I completely wrong here? Either way: feel free to add a patch here or in case it is something more than non-trivial open another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-25 00:11:39

Merged 4111-coerce-simplify.patch, 4111-coerce-CC.patch, 4111-coerce-QQ.2.patch and 4111-coerce-RR.2.patch in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-25 00:11:39

Resolution: fixed


---

Comment by robertwb created at 2008-09-25 00:20:02

Oh, I think I know what the issue is (we have two real fields of 53 bits prec). I'll post a patch that addresses this. 


```
sage: (1.2).parent() is RR
 False
```



---

Comment by AlexGhitza created at 2008-09-25 00:24:12

Also, the patches at #4096 (which I will rebase against 3.1.3.alpha1 as soon as I have built it) will take care of this.


---

Comment by robertwb created at 2008-09-25 00:53:05

Actually, after those patches I get 


```
sage: 1.2.parent() is RR
True
```


Sit looks like a pari issue for sure. For example, I get 


```
sage: (-1.23456)._pari_()
-1.2345600000000000001
```


which isn't using `RR.__call__` at all.


---

Comment by mabshoff created at 2008-09-26 02:45:51

I opened #4199 to make sure the issue does not escape us. I will test the pari patch and see if it fixes the problem.

Cheers,

Michael
