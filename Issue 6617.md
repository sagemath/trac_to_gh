# Issue 6617: remove stale SageTeX files from latex_embed

Issue created by migration from https://trac.sagemath.org/ticket/6617

Original creator: ddrake

Original creation time: 2009-07-25 12:30:24

Assignee: tbd

Keywords: sagetex latex_embed

The directory `$SAGE_ROOT/examples/latex_embed` contains an old version of SageTeX, which is now a full-fledged Sage package. We should delete these old files. The attached patch does this, leaving behind just a pointer to the current SageTeX stuff.


---

Attachment


---

Comment by ddrake created at 2009-07-25 13:03:05

I don't know if the attached patch will do this, but be sure that the PDF files in that directory are also deleted. There should only be a README file remaining.


---

Comment by ddrake created at 2009-07-25 13:06:21

Changing assignee from tbd to ddrake.


---

Comment by ddrake created at 2009-07-25 13:06:21

Changing status from new to assigned.


---

Comment by schilly created at 2009-07-25 17:04:18

Patch works and cleans directory up. Just one thing: in my installation there is a hidden `.example.sage.py` file left in latex_embed. Is it just here in my installation? If yes, positive review, otherwise we have to investigate where it is coming from ;)


---

Comment by ddrake created at 2009-07-25 17:19:04

I see the hidden file too. I'll update the patch to remove it too.


---

Comment by ddrake created at 2009-07-25 17:20:53

Oops, I just checked and that file is not tracked. So whoever merges this patch will need to delete that file manually, and perhaps run a "hg status" to see if there's any other cruft around.


---

Comment by schilly created at 2009-07-25 17:23:57

Yes, same for me, otherwise i would have updated the patch myself ;)

I confirmed this with the hg.sagemath.org tracker, too. .* files seem to be ignored by hg anyways.

Good, apart from that positive review. So, whoever merges this: *you have to delete a hidden file by hand*!!!


---

Comment by mvngu created at 2009-07-25 20:56:10

Resolution: fixed


---

Comment by mvngu created at 2009-07-25 20:56:10

Deleted `SAGE_ROOT/examples/latex_embed/.example.sage.py` by hand, not using

```
hg remove
```

