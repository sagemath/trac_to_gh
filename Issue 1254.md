# Issue 1254: revision to combinat.py

Issue created by migration from https://trac.sagemath.org/ticket/1254

Original creator: wdj

Original creation time: 2007-11-24 17:40:57

Assignee: wdj

CC:  sage-combinat

The patch
http://sage.math.washington.edu/home/wdj/patches/combinat20071124.hg
does the following: 
(1) adds a wrapper to guava's HadamardMat, constructing Hadamard matrices of 
certain types,
(2) modifies the function permutations following the suggestions in the 
"bug in permutations" thread
http://thread.gmane.org/gmane.comp.mathematics.sage.support/2245


---

Comment by was created at 2007-11-24 18:32:27

use this instead of the hg bundle linked to


---

Attachment

I've refereed this -- it has some typos, and bad design, but this is fixed in hadamard.hg.


---

Comment by mabshoff created at 2007-11-24 18:48:53

Resolution: fixed


---

Comment by mabshoff created at 2007-11-24 18:48:53

Merged in 2.8.14.rc2.
