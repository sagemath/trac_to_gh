# Issue 3646: Implement paren matching

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-07-11 22:15:08

Assignee: boothby

CC:  was tclemans yiqiang

People have been complaining about a lack of paren matching in the notebook.  Do something.


---

Comment by jhpalmieri created at 2008-07-18 20:41:11

On my intel mac: works for me in Safari, and works in Firefox but noisily: it beeps whenever I hit ctrl-0 (whether it matches a parenthesis or not).


---

Attachment

I just discovered quilt!  4 patches all rolled into one.


---

Comment by boothby created at 2008-07-29 17:23:55

Oh, and this patch addresses jhpalmieri's issue.


---

Comment by was created at 2008-07-29 17:33:23

REVIEW:

 * Looks very good but does *not* address jhpalmieri's issue successfully.  I can replicate the bing, which is OK, but pressing ctrl-] does not get recognized at all.  I'm using a macbookpro.


---

Attachment

rebased against #6307


---

Attachment


---

Comment by boothby created at 2009-06-16 20:24:31

Ok, this really solves jhpalmieri's issue.  This time, I tested it on a mac with firefox!  I removed the ctrl-] keycode.


---

Comment by jhpalmieri created at 2009-06-20 00:12:38

If I create a cell with

```
3+2)
```

put the cursor at the end and hit ctrl-0, the parenthesis gets replaced with "undefined".  Is this the intended behavior?  It doesn't seem ideal to me; maybe ctrl-0 should do nothing in this situation?

(Otherwise, it works well for me.)


---

Comment by boothby created at 2009-09-22 05:15:10

replaces all previous


---

Attachment


---

Comment by jhpalmieri created at 2009-09-22 18:03:45

This looks good to me.


---

Comment by jhpalmieri created at 2009-09-22 18:07:52

Oops, sorry, I forgot: the patch doesn't apply cleanly for me against 4.1.2.alpha2.  I'm attaching a rebased patch, but all credit should still go to boothby.


---

Comment by jhpalmieri created at 2009-09-22 18:08:17

replaces all previous patches


---

Attachment

replaces all previous patches + boothby's name as author


---

Attachment

The patch `trac_3646-rebased-v2.patch` is the same as `trac_3646-rebased.patch`. The only difference is that v2 has the author name set to Tom Boothby.


---

Comment by mvngu created at 2009-09-24 07:54:10

Resolution: fixed


---

Comment by mvngu created at 2009-09-24 07:54:10

Merged `trac_3646-rebased-v2.patch`.


---

Comment by mvngu created at 2009-09-27 10:15:56

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.


---

Comment by mpatel created at 2009-10-15 18:47:42

Rebase v. #7196.  Apply only this patch.


---

Attachment

[attachment:trac_3646-sagenb_paren_match.patch Patch] rebased against SageNB's #7196.


---

Comment by was created at 2009-10-17 05:15:33

Merged into sagenb (for the sage-4.2 release cycle).
