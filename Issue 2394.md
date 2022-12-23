# Issue 2394: Wrap Cremona's newforms class

Issue created by migration from https://trac.sagemath.org/ticket/2394

Original creator: boothby

Original creation time: 2008-03-05 07:19:41

Assignee: boothby

Wrap the newforms class in eclib


---

Comment by mabshoff created at 2008-03-09 06:46:00

Three remarks:

 * I am splitting the updated eclib.spkg off into its own ticket #2347
 * doctests seems to be missing
 * It would be interesting to see if this conflicts with wstein's mwrank rewrite

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-09 06:50:28

I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?

Cheers,

Michael


---

Comment by cremona created at 2008-03-09 16:25:05

mabshoff is right -- this is the same as eclib-20080127.    I think boothby forgot to check in his changes?


---

Comment by mabshoff created at 2008-03-09 16:37:15

Yep. Checking the repo I see:

```
eclib-20080304/src$ hg status
M g0n/Makefile
M g0n/hecketest.cc
M g0n/homspace.cc
M g0n/homspace.h
M g0n/newforms.cc
M g0n/newforms.h
M g0n/nftest.cc
M procs/rat.h
? g0n/ecnf.cc
```


Cheers,

Michael


---

Comment by boothby created at 2008-03-09 22:59:12

I didn't change the title of this ticket for a reason!  Nothing here is ready for review.  The eclib spkg has *bad* changes, like I made some private class members public, etc.  The patch (as noted) doesn't have doctests, and doesn't work.  I put this up as a preliminary version for William to work with.  Later this week, I'll make it all kosher.


---

Comment by boothby created at 2008-03-10 00:20:30

See #2437 (not 2347)


---

Attachment


---

Comment by malb created at 2008-04-05 23:22:35

patch looks good, except:
  * newly created files don't have file level documentation
  * newly created files don't have copyright statement (do they need one?)
  * Does it make sense to add doctests to `class ECModularSymbol` ?


---

Comment by cremona created at 2008-04-06 20:12:11

I also think the patch looks good, though I agree with malb's points.  Also I have no experience myself in wrapping code (even my own ;)) so the fact that it looks ok to me does not count for much.

Since this patch has required a little tinkering with eclib itself, I think I need to download that, compare with the latest version of my own, and check that nothing is broken...


---

Attachment

2394-license.patch adds a copyright statement.  File-level documentation would be redundant since the file only has a single class, and the class is documented.  Also, ECModularSymbol has doctests on every function.  Should we add more?  If so, what?  Modulo any further complaints, we should add this in to avoid bitrot.


---

Comment by malb created at 2008-04-11 21:07:52


```
[22:00] <boothby> Please look at my comments on #2394
[22:01] <boothby> valid/invalid?
[22:02] <malb> I'm still in favour of module level docs but that is taste I reckon
```


I say apply.


---

Comment by mabshoff created at 2008-04-12 00:10:46

Resolution: fixed


---

Comment by mabshoff created at 2008-04-12 00:10:46

Merged both patches in Sage 3.0.alpha4
