# Issue 6955: update simon denis pari-scripts

Issue created by migration from https://trac.sagemath.org/ticket/6955

Original creator: wuthrich

Original creation time: 2009-09-18 11:03:40

Assignee: davidloeffler

Keywords: two descent,

I found out that sage comes with old versions of the files ell.gp,  ellQ.gp,  qfsolve.gp. This should be updated. The newest version can be found at http://www.math.unicaen.fr/~simon/ .


---

Comment by wuthrich created at 2009-09-18 11:04:41

This should be very easy to do, but I don't know how to submit a patch for this. Sorry.


---

Comment by davidloeffler created at 2009-10-09 09:10:03

Remove assignee davidloeffler.


---

Comment by cremona created at 2009-12-14 17:14:35

See also #5153.  We'll need to check that the version on Denis's home page is at least as up-to-date as the one he sent me which apparently fixed the bug I sent him.  I'll also try to find that email correspondence and add it to one of these tickets.


---

Comment by cremona created at 2010-04-03 16:36:40

I have updated the scripts (attached to the ticket) to the ones on DS's home page on 3 April 2010, which are dated as follows:
    - ell.gp (v. 2009-03-25)
    - ellQ.gp (v. 2008-04-29)
    - qfsolve.gp (v. 2008-02-26)
The patch (to appear) applies to 4.3.5 and fixes some small things:  Simon's variable DEBUGLEVEL has been renamed DEBUGLEVEL_ell, and some of the verbose output changes a little.  ALso, some "generators" appear in a different order or are otherwise (mathematically) trivially different.

This does not fix other issues with these scripts, as in #5153.


---

Attachment


---

Attachment

Applies to 4.3.5


---

Comment by cremona created at 2010-04-03 16:43:44

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-03 16:43:44

The three scripts should replace those in SAGE_ROOT/data/extcode/pari/simon/


---

Comment by cremona created at 2010-04-03 18:33:24

Apply in SAGE_ROOT/data/extcode before other patch


---

Attachment

The patch trac_6955-simon-update-extcode.patch should be applied in the directory SAGE_ROOT/data/extcode in addition to the usual patch for sage-main.  The gp files on the ticket are just for reference.


---

Comment by wuthrich created at 2010-04-08 13:53:20

Sorry, John, I am a newbie to anything that is outside the devel-tree. Can you tell me exactly what I have to do (if you want me to review it) ?

Chris.


---

Comment by cremona created at 2010-04-08 15:39:10

Replying to [comment:7 wuthrich]:
> Sorry, John, I am a newbie to anything that is outside the devel-tree.

So was I before I did this!

> Can you tell me exactly what I have to do (if you want me to review it) ?
>

OK.  You need to be careful, since you will be changing files outside $SAGE_ROOT/devel, which are therefore not covered by the cloning system, so you have to work a bit harder both to apply the patches and to unapply them.  I will assume that you will use mercurial queues (but it would be possible without).

First make a clone in the usual way, say called simon, so you have created $SAGE_ROOT/devel/sage-simon as a copy of $SAGE_ROOT/devel/sage-main.

Now apply the patch to the extcode:

```
cd SAGE_ROOT/data/extcode  
hg qseries      # test that queues have been initialised here;  if not, do hg qinit first
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update-extcode.patch
hg qpush
```

Now apply the ordinary patch:

```
cd ../../devel/sage-simon
hg qinit  # if not already done
hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6955/trac_6955-simon-update.patch
hg qpush
sage -b
```


That's it applied.  Run, test, as much as you like.  To reverse the changes:

```
# in devel/sage-simon
hg qpop
cd ../../data/extcode
hg qpop
sage -b
```


 
> Chris.


---

Comment by wuthrich created at 2010-04-09 17:14:47

Thanks a lot for the very helpful comments. I assume the next time I would be able to make a patch myself for this.

All tests passed after having deleted the first change in the patch (it added a space at the start of the file.)

The modified patch corrects this.


---

Attachment

replaces the previous patch of this name


---

Comment by wuthrich created at 2010-04-09 17:18:46

So I give a positive review. The two patches trac_6955-simon-update_reviewer.patch and trac_6955-simon-update-extcode.patch have to be applied as described by John.


---

Comment by wuthrich created at 2010-04-09 17:18:46

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-09 18:05:54

Thanks -- sorry about that space, which I thought I had put in before making the patch and not after!  It has been bugging me ever since.


---

Comment by jhpalmieri created at 2010-04-15 22:45:12

The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py?


---

Comment by jhpalmieri created at 2010-04-15 22:45:12

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-04-16 08:42:27

Replying to [comment:12 jhpalmieri]:
> The reviewer patch doesn't apply cleanly.  Is it okay to just delete the portion of the patch for the file sage/schemes/elliptic_curves/gp_simon.py? 

No, that part is crucial.  Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  The only difference between them is that my patch wrongly inserts a space in the first line of the file ell_number_field.py, and Chris's patch removes that bit of my patch,


---

Comment by jhpalmieri created at 2010-04-16 17:14:14

Replying to [comment:13 cremona]:
> Did you see that the review patch is instead of my patch called trac_6955-simon-update.patch, and not a second one to b applied after it?  

Ah, no, I'd missed that.  Sorry.


---

Comment by jhpalmieri created at 2010-04-16 17:14:21

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-04-16 17:14:26

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:58:22

Merged in 4.4.alpha0:
 - trac_6955-simon-update-extcode.patch
 - trac_6955-simon-update_reviewer.patch


---

Comment by jhpalmieri created at 2010-04-16 18:58:22

Resolution: fixed


---

Comment by cremona created at 2010-04-16 19:22:10

Many thanks, jhp -- seems that you are release manager, and busy!
