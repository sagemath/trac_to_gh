# Issue 2060: Update PolyBoRi spkg to 0.2

Issue created by migration from https://trac.sagemath.org/ticket/2060

Original creator: malb

Original creation time: 2008-02-05 17:35:05

Assignee: burcin


```
The first release candidate of PolyBoRi 0.2 is available in the download area.
This version comes with refined Gröbner algorithms and several stability
improvements. Also new procedures for interpolation of Boolean polynomials
have been added.
```

http://polybori.sourceforge.net/


---

Comment by mabshoff created at 2008-02-17 19:57:41

Note that #1611 is the ticket to split out and use the dynamic version of libm4ri. 

Cheers,

Michael


---

Attachment

update polybori interface to version 0.3.1


---

Comment by burcin created at 2008-03-25 20:42:51

attachment:2060-polybori_interface_update_0.3.1.patch includes the changes to the polybori wrapper for version 0.3.1, the corresponding package is here:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.3.1.spkg


---

Comment by burcin created at 2008-03-25 20:42:51

Changing status from new to assigned.


---

Comment by malb created at 2008-03-26 21:21:30

The SPKG installs fine but I cannot apply the patch neither against my modified copy of Sage (which is expected) nor a vanilla 2.10.4, which is unexpected. I've attached the reject files for both.


---

Comment by malb created at 2008-04-01 13:03:23

FYI, this patch still applies against 2.11:

```
applying /home/malb/2060-polybori_interface_update_0.3.1.patch?format=raw
patching file sage/rings/polynomial/pbori.pyx
Hunk #1 succeeded at 148 with fuzz 1 (offset 100 lines).
```



---

Attachment

The attached patch (`polybori_0.3.1_doctest_coverage_48.patch`) which is to be applied on top of `2060-polybori_interface_update_0.3.1.patch` increases the doctest coverage to 47%.


```
pbori.pyx
SCORE pbori.pyx: 47% (98 of 205)
```


Before both patches the coverage was at:


```
pbori.pyx
SCORE pbori.pyx: 33% (52 of 157)
```


and thus this is an improvement over vanilla 2.11 too.

 * I give Burcin's patch a positive review: doctests pass and we *need* `PolyBoRi` 0.3.1
 * someone should review my patch
 * if my patch gets a positive review both patches should be applied, since then not only is the functionality improved but also the doctest coverage which should make the everything-new-needs-doctest faction happy.
 * Burcin's patch was also doctested with the `PolyBoRi` test suite by him, so there is even an undocumented extra level of assurance.
 * In any case: We'll be working on getting the coverage close to 100% in the very near future.


---

Comment by burcin created at 2008-04-01 21:41:05

I agree that waiting to add doctests to each wrapped function from polybori will hold up the patch unnecessarily. The `PolyBoRi` test suite stresses the (yet) undocumented functions thoroughly.

I give Martin's patch a positive review, both patches should be applied


---

Comment by mabshoff created at 2008-04-01 22:14:04

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 22:14:04

Resolution: fixed
