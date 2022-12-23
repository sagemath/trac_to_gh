# Issue 3020: Finite Fields of characteristic 2 slow to construct

Issue created by migration from https://trac.sagemath.org/ticket/3020

Original creator: cremona

Original creation time: 2008-04-24 21:40:17

Assignee: tbd

CC:  malb cwitty

Keywords: finite fields

Construction of GF(2^n) is very slow for n>=16 (out of the givaro range), owing to slow search for suitable defining irreducible polynomials over GF(2).  Also the polynomials produced are dense.

A new function GF2X_sparse_irreducible() has been added, using a precomputed lookup table for degrees up to 2048 (taken from NTL's source code) and otherwise looking for tri- and pentanomials first.

Patch attached, based on 3.0.


---

Attachment


---

Comment by malb created at 2008-04-24 23:47:32

The patch looks good, some comments though:
 * I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?
 * This is table from NTL? Can't we just read in the NTL table automatically?
 * Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.


---

Comment by malb created at 2008-04-24 23:47:32

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-04-25 06:56:53

Changing assignee from tbd to cremona.


---

Comment by cremona created at 2008-04-25 08:08:23

Replying to [comment:2 malb]:
> The patch looks good, some comments though:
>  * I'd prefer to have the table in a different file rather than `finite_field.py`, say `gf2x_irred_table.py`?

Ok, I can do that.  If I then put

```
   import gf2x_irred_table
```

at the appropriate point in finite_field.py, it would only read it in if the function is called, right?

>  * This is table from NTL? Can't we just read in the NTL table automatically?

This was intended to be a quick fix.  A better fix (as I originally posted) is to change the NTL wrapping code to use NTL's own function, when creating the field.  At the same time we could just wrap NTL's BuildSparseIrred() function.

>  * Did you check if each entry is irreducible? I assume so, I just want to make it formally sure.

I checked for k<1000 and was intending to do the rest (as you say, to be formally sure), but it takes quite a long time.


---

Attachment


---

Comment by cremona created at 2008-04-25 08:23:33

The second patch moves the table to a separate file as recommended.  Apply *both* patches!


---

Comment by cremona created at 2008-04-27 10:14:13

I have now checked that all 2048 polynomials in the table are irreducible, using Sage's .is_irreducible() function.  This took a _very_ long time (more than 36 hours to do the last thousand) indicating that some improvement might be possible.  But it's done.


---

Comment by cremona created at 2008-04-27 16:11:25

apply after both the preceding patches


---

Attachment

Trivial fix to previous, correcting a very stupid Python indentation howler -- which meant that for all n for which the tabulated irreducib;e was a trinomial, it did not return the table poly but searched for one.


---

Comment by malb created at 2008-05-05 21:27:43

I've attached an alternative implementation which uses NTL directly rather than re-implementing its behaviour in Sage. 

`@`John: I hope you don't mind, i.e. I don't step on your toes with that, but since you stated that your patch was a quick fix and we should switch to use NTL eventually, I figured it would be a good idea to do it know. Could you review the patch, i.e. check if it does what you want?

`@`Carl: Somehow the NTL random polynomial generation doesn't obey your randgen framework, any idea why?


---

Comment by cremona created at 2008-05-06 08:39:06

No problem, I am delighted that someone has done this properly, and only wish that it had been me to do that.  I am off to look at what you have done and test it now...

Comments: 
    #  typo in line 147 (spare -> sparse)

    #  l.203-4: I wondered why you call BuildSparseIrred first.  But  I see that NTL's BuildRandomIrred takes a monic irreducible as input and returns another of the same degree, which is rather bizarre, so I guess you had no choice.  

I checked the logic of the new code and am happy with it.
The patch applies cleanly to 3.0.1, and all doctests in sage/rings pass.

Verdict: positive review! apart from the typo this patch (just the last one from malb) is good to go.


---

Comment by cremona created at 2008-05-06 08:39:48

Sorry forgot to change the summary


---

Attachment

updated patch which fixes the typo


---

Comment by malb created at 2008-05-06 10:17:05

> # typo in line 147 (spare -> sparse) 

Fixed in updated patch (same patch, overwritten) 

> # l.203-4: I wondered why you call BuildSparseIrred first. But
> I see that NTL's BuildRandomIrred takes a monic irreducible as
> input and returns another of the same degree, which is rather
> bizarre, so I guess you had no choice.

exactly, but I'm not an NTL expert.


---

Comment by mabshoff created at 2008-05-06 11:05:28

Hi,

it is my understand now to only apply GF2X_sparse_poly.patch. What is the status of the concern regarding the random state? Was that just a general observation since Carl only covered so many randomness sources by his framework?

Cheers,

Michael


---

Comment by malb created at 2008-05-06 11:09:44

Replying to [comment:13 mabshoff]:
> it is my understand now to only apply GF2X_sparse_poly.patch. 

correct.

> What is the status of the concern regarding the random state? Was that just a 
> general observation since Carl only covered so many randomness sources by his
> framework?

My guess is that he covers NTL, but we can always open another ticket and address the issue there.


---

Comment by mabshoff created at 2008-05-06 19:28:04

Resolution: fixed


---

Comment by mabshoff created at 2008-05-06 19:28:04

Merged GF2X_sparse_poly.patch in Sage 3.0.2.alpha0
