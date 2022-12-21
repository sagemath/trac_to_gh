# Issue 5766: improve coverage of structure/formal_sum.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-11 23:58:16

Assignee: somebody




---

Comment by was created at 2009-04-12 01:07:57

BUGS FOUND:
1. The reduce option to formal sum is totally ignored.

```
sage: FormalSum([(1,2/3), (3,2/3), (-5, 7)], reduce=False)
4*2/3 - 5*7
```


2. Latexing formal sums is completely broken (I think this is actually #5707):

```
sage: latex(FormalSum([(1,2), (5, 8/9), (-3, 7)]))
5\frac{8}{9}2 - 37
```



---

Attachment


---

Comment by ncalexan created at 2009-04-12 05:02:32

There's an `indirect doctest` missing from nonzero and a typoed `indirect doctest` on len, but other than that this looks good.


---

Comment by mabshoff created at 2009-04-13 01:39:04

Mhh, ther seems to be a 32 vs. 64 bit issue here:

```
sage -t -long "devel/sage/sage/structure/formal_sum.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py", line 333:
    sage: a
Expected:
    2/3 - 3*4/5 + 7*2
Got:
    7*2 + 2/3 - 3*4/5
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/formal_sum.py", line 335:
    sage: a._repr_()
Expected:
    '2/3 - 3*4/5 + 7*2'
Got:
    '7*2 + 2/3 - 3*4/5'
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2009-04-27 20:01:57

Sorry, but on my 32-bit laptop I get

```
**********************************************************************
File "/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py", line 333:
    sage: a
Expected:
    2/3 - 3*4/5 + 7*2                       -- comparing Mod(2,3) and rationals ill-defined
Got:
    7*2 + 2/3 - 3*4/5
**********************************************************************
File "/home/john/sage-3.4.2.alpha0/devel/sage-tests/sage/structure/formal_sum.py", line 336:
    sage: a._repr_()
Expected:
    '2/3 - 3*4/5 + 7*2'                    
Got:
    '7*2 + 2/3 - 3*4/5'
**********************************************************************
```


Perhaps all formal sums should be sorted?  As part of the reduce() method (which should then be called after creation)?


---

Comment by was created at 2009-04-28 14:10:18

> Perhaps all formal sums should be sorted? As part of the reduce() method (which should then be called after creation)? 

They are sorted.  That's why the doctests failed for you -- because sort is not well defined as indicated in the comment.


---

Attachment


---

Comment by cremona created at 2009-04-28 16:30:00

OK with all three patches the tests pass.  It's a pity we cannot make it deterministic but the only thing I could think of was sorting on the strong representations (of the base of each pair) and that would take too long I suppose.


---

Comment by mabshoff created at 2009-04-30 00:44:15

With all three patch applied I am seeing the following doctest failure:

```
sage -t -long "devel/sage/sage/misc/latex.py"               
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.rc0/devel/sage/sage/misc/latex.py", line 942:
    sage: repr_lincomb([1,5,-3],[2,8/9,7])
Expected:
    '2*1 + 8/9*5 + 7*-3'
Got:
    '21 + \\frac{8}{9}5 + 7-3'
**********************************************************************
```

Since this seems to be the correct LaTeX representation I am fixing this failure.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 00:45:33

Actually, the above seems broken, i.e. notice the missing *** - so 'needs work'.

Cheers,

Michaek


---

Comment by AlexGhitza created at 2009-06-04 01:54:52

I have folded William's patches and rebased them against 4.0.alpha0.

I made an attempt to fix the latex-ing, see the patch.


---

Comment by AlexGhitza created at 2009-06-04 01:55:43

apply instead of the other patches


---

Comment by mhansen created at 2009-06-04 18:33:58

Resolution: fixed


---

Attachment

Looks good to me.

Merged trac_5766-rebased.patch in 4.0.1.rc1.
