# Issue 9476: Upgrade eclib to version 20100711

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-07-11 20:36:54

Assignee: tbd

CC:  was wuthrich

Keywords: eclib modular symbols

I have made several enhancements to eclib:

    1. Support for minus space modular symbols
    2. Some sparse linear algebra improvements

The new version is called eclib-20100711 since it is more than just a patch-level change.  New spkgs will be linked here shortly.

The interface in sage/libs/cremona has been updated accordingly in the patch (to appear shortly);  this depends on #9441


---

Comment by cremona created at 2010-07-11 21:23:59

The new spkg is here: http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg


---

Attachment

Applies after eclib-20100711.patch and trac_9441-atkin-lehner.patch


---

Comment by cremona created at 2010-07-11 21:26:18

Changing status from new to needs_review.


---

Comment by rlm created at 2010-07-17 10:59:36

I'm reviewing this and #9441 at the same time. So far it compiles just fine with sage-4.5 final, on Intel OS X 10.6.4, and I'm currently running tests. I'll also give it a try on geom.math, which has begun at the moment.


---

Comment by rlm created at 2010-07-17 12:59:28

Looks good on OS X. Same on geom.math.


---

Comment by rlm created at 2010-07-17 12:59:28

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-17 13:18:19

Small reviewer patch coming up in a minute!


---

Comment by rlm created at 2010-07-17 13:18:19

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-07-17 13:21:03

Thanks!


---

Comment by rlm created at 2010-07-17 13:28:43

Changing status from needs_work to needs_info.


---

Comment by rlm created at 2010-07-17 13:28:43

Hmm. I think this might have something to do with one of the things I saw on #9247.

I'm attaching the reviewer patch, which causes the following:


```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py"
**********************************************************************
File "/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 429:
    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)
Expected nothing
Got:
    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.
**********************************************************************
File "/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 438:
    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)
Expected nothing
Got:
    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.
**********************************************************************
```


John,

Can you give some info about what's going on here?


---

Comment by cremona created at 2010-07-17 14:23:41

I have added Chris W to the CC list since we'll need his input, as he wrote ell_modular_symbols.

I agree that that file needs updating as a consequence of my upgrade;  but that can be done on a separate ticket?


---

Comment by rlm created at 2010-07-17 14:31:17

John,

I thought that eclib was propagating that warning, but clearly it's coming from ell_modular_symbols.py. Have a look at the new ref patch, and let me know what you think.


---

Comment by rlm created at 2010-07-17 14:31:49

Changing status from needs_info to needs_review.


---

Attachment


---

Comment by was created at 2010-07-21 13:50:40

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-07-21 13:50:40

reviewer addendum looks good to me.


---

Comment by mpatel created at 2010-08-07 02:54:08

I'm having difficulty getting the new package:

```
$ wget http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg
--19:50:47--  http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg
           => `eclib-20100711.spkg'
Resolving www.warwick.ac.uk... 137.205.243.107
Connecting to www.warwick.ac.uk|137.205.243.107|:80... connected.
HTTP request sent, awaiting response... 
```


Can someone check its availability and perhaps put a copy on the Sage cluster?

Also, should I apply both patches, too?


---

Comment by mpatel created at 2010-08-07 02:54:23

Changing status from positive_review to needs_info.


---

Comment by mpatel created at 2010-08-08 04:39:13

Changing status from needs_info to needs_review.


---

Comment by mpatel created at 2010-08-08 04:39:13

The package is available now.  I'll include both patches.


---

Comment by mpatel created at 2010-08-08 04:39:18

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:49:55

Resolution: fixed


---

Comment by cremona created at 2010-08-11 15:58:32

Sorry not to have responded earlier but I was on holiday for a few days.  I think they were doing some network updating at U of Warwick, which could  explain why you could not get the file.  Glad it's fixed -- and thanks for the review.
