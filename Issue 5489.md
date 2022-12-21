# Issue 5489: add a non library level interface to 4ti2 to Sage

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-03-11 18:05:10

Assignee: was




---

Attachment


---

Attachment


---

Comment by broune created at 2009-06-26 16:47:45

The patch 4ti2_interface.patch builds on mhansens work. It adds the method groebner, which computes Toric grobner bases, and adds documentation and doctests. It also updates the code so that it can be built as part of Sage.

You need 4ti2 installed to review this, but the experimental spkg from 2006 is incompatible with this patch. Download 4ti2 from www.4ti2.de and put the binaries from that somewhere on your Sage path. E.g. dumping them in sage/local/bin will work.

Patch applies cleanly to Sage 4.0.1 and doctests pass on my Mac.


---

Comment by malb created at 2009-08-18 10:58:39

*Review*

 * the docstrings are not according to the current Sage standard.
 * IMHO one should update the experimental 4ti2 spkg in parallel with accepting this patch
 * how much hassle would it be to replace docs like 

```
Runs the 4ti2 program ``qsolve`` on the parameters. See ``http://www.4ti2.de/`` for details. 
```

   with docs which describe the program somewhat?
 * patch applies cleanly against 4.1.1.
 * `devel/sage/sage/interfaces/four_ti_2.py # 9 doctests failed` if 4ti2 is not installed, because `#optional` tag is missing


---

Comment by broune created at 2009-08-22 00:09:13

Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.

Inlining the 4ti2 documentation from 4ti2 into Sage opens the issue of licenses. I do not know what license is used for the 4ti2 documentation, and I don't think this is explicit anywhere. I agree it would be an improvement, though this would have to wait until someone (not me) in future volunteers to investigate the 4ti2 license for documentation.

I agree it would be good to update the experimental 4ti2 spkg, which is however beyond the scope of what I'm willing to do on this at this time. If this is a requirement of acceptance of the patch, it will have to wait until someone chooses to update the 4ti2 spkg.


---

Comment by jhpalmieri created at 2009-11-19 22:36:35

Replying to [comment:3 broune]:
> Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.

I don't have answers for your other questions, but for this one:

(1) "EXAMPLES:" should be changed to "EXAMPLES::"  (double colon), and it should be followed by a blank line.

(2) In the `__init__` method at the beginning of the file, the INPUT block is not formatted correctly: after the first line, the other lines should be indented so that they line up with ```directory``` (as you've done later).

(3) In all of your INPUT blocks, the leading hyphens should not be indented: they should line up with the "I" in "INPUT".

(4) A few methods have blank lines after the initial `r"""`.  I think those should be deleted.


---

Comment by mhampton created at 2011-03-29 03:16:19

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2011-03-29 03:20:42

I believe I have addressed all the comments of jhpalmieri above.  It is true that better descriptions of the functionality would be nice, but I think this is OK for inclusion anyway - sometimes the perfect is the enemy of the good.

Although it does not have a positive review (please someone take a look!) please test this against [http://trac.sagemath.org/sage_trac/ticket/8217](http://trac.sagemath.org/sage_trac/ticket/8217).


---

Attachment

Cumulative patch


---

Comment by davidloeffler created at 2012-03-10 17:16:31

Apply trac_5489_4ti2_interface.patch

(for the patchbot)


---

Comment by chapoton created at 2012-07-24 20:15:23

The code looks good, the doc coverage is 100% and the tests pass. I am almost ready to give a positive review.

I have only some basic comments:

* there is a typo here in "does" (in the method directory)


```
# method since apparently importing sage.misc.misc oes not
```


* Why not gather these import statements at the beginning ?


```
 from sage.matrix.constructor import matrix 
 from sage.matrix.matrix import is_Matrix 
 from sage.rings.integer_ring import ZZ 
 import subprocess
```


If there is no technical difficulty (as for sage.misc.misc), it seems better to import them once and for all. At least those about matrices and integers ?

* There seem to be some 'trailing whitespaces' that could be removed. All the lines just after an EXAMPLES:: should rather be empty.

* The minimize method is NotImplemented. This can of course wait for another ticket.


---

Comment by jdemeyer created at 2012-07-27 20:43:04

Please fill in your real name as Author.


---

Attachment


---

Comment by chapoton created at 2012-08-26 19:25:42

Apply only: trac_5489_4ti2_interface-reviewer.patch


---

Comment by chapoton created at 2012-08-26 19:49:02

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2012-08-26 19:49:02

I have made some small changes that I suggested, in a new patch. The bot is green, and everything looks good. Positive review !


---

Comment by jdemeyer created at 2012-09-03 12:51:12

Resolution: fixed
