# Issue 3388: Fix gmp 4.2.2 speed regression on Core2

Issue created by migration from https://trac.sagemath.org/ticket/3388

Original creator: mabshoff

Original creation time: 2008-06-10 02:35:04

Assignee: tbd

In http://groups.google.com/group/sage-devel/t/ba359f3b1ba435d David wrote:

```
Okay, I can confirm that with sage 3.0.1, sage -gp has the same speed  
as my standalone GP build. So mostly likely the change to GMP 4.2.2  
introduced a speed regression (probably the core 2 patches not being  
applied properly).

david 
```

Fix this!

Cheers,

Michael


---

Comment by dmharvey created at 2008-06-21 22:05:14

Yeah, I went back and looked at the log, and found this:


```
Do we have a Core2 CPU?... Yes
Detected Intel Core 2 CPU
Found GMP at /home/dmharvey/sage-3.0.2/spkg/build/gmp-4.2.2/src
ERROR: Incorrect GMP Version.  Found GMP version: 4.2.2
       needed version 4.2.1
```


So it's simply that jason's script knows not to try patching the wrong version of GMP.

We should probably ignore this, since MPIR should be here soonish.


---

Comment by mabshoff created at 2008-06-21 22:32:04

Ok, we might want to ask Jason about whether there are any issues with gmp 4.2.2, but I would assume they would not be. I agree that MPIR should arrive soon enough to make this a non-issue.

Cheers,

Michael


---

Comment by dmharvey created at 2008-06-21 22:40:44

I will ping Jason and ask him if there is a quick fix for sage, in case MPIR takes longer than we expect.


---

Comment by dmharvey created at 2008-06-22 16:26:08

Further developments:

Jason updated his patch to a 4.2.2 version, now available from his website.

I tested it and it does work against a vanilla 4.2.2 build.

However, when I put it in the 4.2.2 spkg, it doesn't work. Specifically: it copies the core 2 files, but then GMP's configure script doesn't link to the files, in fact it uses GENERIC code for all the mpn routines.

I dug a little further and discovered the probable culprit: the configure script is from 4.2.1, not 4.2.2!!! And this appears to be because we *overwrite* the configure script when installing the fast gcd patch.

Grrrr. I will try to fix this later today.


---

Comment by dmharvey created at 2008-06-22 16:26:08

Changing component from algebra to build.


---

Comment by dmharvey created at 2008-06-22 16:26:08

Changing assignee from tbd to mabshoff.


---

Comment by malb created at 2008-08-16 23:44:14

What's the current status of this ticket? Presumably, the 4.2.1 vs. 4.2.2 issue was fixed or wasn't it?


---

Comment by mabshoff created at 2008-08-30 07:06:43

Since we will switch to eMPIRe this is invalid.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 07:06:43

Resolution: invalid


---

Comment by dmharvey created at 2008-09-15 18:11:43

Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.


---

Comment by mabshoff created at 2008-09-15 20:16:04

Replying to [comment:7 dmharvey]:
> Well it's been three months since the ticket was created. If there is no serious plan to get MPIR out soon, I'd like to see this ticket reinstated.

We are working on a spkg that will be merged this month.

Cheers,

Michael
