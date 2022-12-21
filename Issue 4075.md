# Issue 4075: bug in BCHCode

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-09-08 11:15:56

Assignee: rlm

This was reported by Felipe Voloch:


```
Hi,

I am not sure how to report bugs in Sage but I see you are involved
with their coding theory. I was playing around with BCH codes and
in particular I wanted the BCH code over F_5 of length 26 and designed
distance 5. Sage reports this code as having dimension 25 (see below)
but the dimension should be 10, which Magma computes correctly (see
below also).

Thanks 

Felipe

---------------------SAGE---------------------------------------------
amd13:~> sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: C = BCHCode(26,5,GF(5)); C
Linear code of length 26, dimension 25 over Finite Field of size 5


---------------------MAGMA--------------------------------------------
linux182~> magma
Magma V2.14-10    Fri Sep  5 2008 14:24:48 on linux182 [Seed = 1390124479]
Type ? for help.  Type <Ctrl>-D to quit.
> > C:=BCHCode(GF(5),26,5); 
> > Dimension(C);
10
```


Incidently, Guava does this correctly. The problem is that I used the wrong element to construct the generator polynomial. 

This is fixed in the attached patch, based on 3.1.2.alpha4. It passes sage -testall and also adds a test in the docstring to include the example reported by Felipe.


---

Attachment

based on 3.1.2.alpha4


---

Comment by rlm created at 2008-09-08 20:27:58

If tests pass, this looks good to me.


---

Comment by mabshoff created at 2008-09-08 20:56:11

Doctests pass in my current 3.1.2.rc1 merge tree with this patch applied. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-08 20:56:24

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-08 20:56:24

Resolution: fixed
