# Issue 5990: [with patch, needs review] developer's guide: more on .spkg files

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-05-05 18:23:20

Assignee: jhpalmieri

This is an amalgamation of information from the patch at #4857 and the wiki page [http://wiki.sagemath.org/SPKG_Audit](http://wiki.sagemath.org/SPKG_Audit).  Therefore Georg Weber should get credit for the parts coming from #4857, while Michael Abshoff and Dan Drake should get credit for the parts coming from the wiki page.



---

Comment by GeorgSWeber created at 2009-05-05 20:08:36

"Positive Review" because I just read the patch online on trac and it is definitely an enhancement over the old documentation.

"Minus epsilon" because I actually didn't download and test the patch (whether it applies to Sage-3.4.2, whether the documentation still builds, and such).

There is still room for improvement, e.g. display sample contents of the ".hgignore" file --- this file has to contain necessarily "src" as an exception.


---

Comment by jhpalmieri created at 2009-05-05 22:00:33

Here's a new version with a sample .hgignore file.


---

Attachment


---

Comment by jhpalmieri created at 2009-05-31 22:26:09

I'm changing this from "positive review minus epsilon" to "needs review" so that it still appears in the list of tickets needing review.  If someone is willing to confirm that the patch applies and that the documentation builds correctly (with `sage -docbuild developer FORMAT`, with FORMAT being "html", "pdf", etc.) then I think it can get a full positive review.


---

Comment by wdj created at 2009-06-01 00:27:37

The patch applies to 4.0.rc2 and sage -docbuild developer html works on a mac OS 10.4. I don't have pdflatex installed yet, so the pdf option fails.


---

Comment by wdj created at 2009-06-01 00:50:09

Both work in ubuntu 9.04, with the pdf placed in devel/sage/doc/output/pdf/en/developer and the html in
/home/wdj/sagefiles/sage-4.0.rc1/devel/sage/doc/output/html/en/developer. According to the comment above by  jhpalmieri, I am therefore changing this to a positive review.


---

Comment by mhansen created at 2009-06-01 05:26:52

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 05:26:52

Resolution: fixed
