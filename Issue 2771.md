# Issue 2771: [with patch, needs review] PolyBoRi doctest coverage at 54%

Issue created by migration from https://trac.sagemath.org/ticket/2771

Original creator: malb

Original creation time: 2008-04-02 13:41:42

Assignee: malb

CC:  burcin

Keywords: coverage, polybori

... working towards 100% :-)


---

Attachment


---

Comment by mabshoff created at 2008-04-02 15:18:25

Hi malb,

I skimmed the code, so no final review yet. But I noticed that you use

```
sage: from polybori import BooleSet 
```

for imports. This will cause trouble once  #2746, i.e. "Support for writing test-related files in SAGE_TESTDIR", is applied. 

Cheers,

Michael


---

Comment by malb created at 2008-04-02 15:27:14

Replying to [comment:1 mabshoff]:
> Hi malb,
> 
> I skimmed the code, so no final review yet. But I noticed that you use
> {{{
> sage: from polybori import BooleSet 
> }}}
> for imports. This will cause trouble once  #2746, i.e. "Support for writing test-related files in SAGE_TESTDIR", is applied. 

It won't. There is `sage.rings.polynomial.pbori` and there is `polybori`. `polybori` is indeed at the global top-level.


```
malb@XXX:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: polybori
sage: from polybori import *
sage:
```



---

Comment by mabshoff created at 2008-04-03 20:29:13

I found two small issues:

 * One time you use "Gröbner" while in all other places you use Groebner
 * I would use a verb for "The opposite of navigation down a ZDD using navigators is to" 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 21:14:33

Resolution: fixed


---

Comment by mabshoff created at 2008-04-03 21:14:33

Merged in Sage 3.0.alpha1 with the two above mentioned minimal changes.
