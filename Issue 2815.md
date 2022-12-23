# Issue 2815: docstring errors in coding/pbori

Issue created by migration from https://trac.sagemath.org/ticket/2815

Original creator: wdj

Original creation time: 2008-04-05 21:30:38

Assignee: tba

The attached patch fixes some latex docstring errors. No code is modified or added.


---

Comment by wdj created at 2008-04-05 21:31:25

docstring patch based on sage-3.0.alpha0


---

Attachment


---

Attachment

doc patch based on sage-3.0.alpha0 which adds sections to ref.tex


---

Comment by malb created at 2008-04-05 21:49:32

Looks good.

I wonder if this could be an issue though, but I doubt it.


``` 
- \setshortversion{2.11} 
+ \setshortversion{3.0.alpha0} 
```



---

Comment by mabshoff created at 2008-04-05 21:58:56

Replying to [comment:2 malb]:
> Looks good.
> 
> I wonder if this could be an issue though, but I doubt it.
> 
> {{{ 
> - \setshortversion{2.11} 
> + \setshortversion{3.0.alpha0} 
> }}}

I will delete that bit from the patch. Thanks for the review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 22:07:05

David: I do not see any fixes to PolyBoRi. There are changes to the crystal code and the other patch adds the documentation of coding/sd-codes and coding/code-constructions to the manual. Is there anything coming for PolyBori?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 22:29:34

mmmh, the crystals patch does not apply at all:

```
patch -p1 --dry-run < trac_2815_9217.patch
patching file sage/combinat/crystals/letters.py
Hunk #1 FAILED at 197.
Hunk #2 FAILED at 213.
Hunk #3 FAILED at 234.
Hunk #4 FAILED at 243.
Hunk #5 FAILED at 267.
```


I changed the summary to "dd more coding theory to the reference manual" since that patch does apply. Please open another ticket for any new patches.

Thoughts?


---

Comment by mabshoff created at 2008-04-05 22:30:08

Resolution: fixed


---

Comment by mabshoff created at 2008-04-05 22:30:08

Merged 511.patch in Sage 3.0.alpha2
