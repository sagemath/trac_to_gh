# Issue 7933: update copyright years to span 2006--2010

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-15 03:58:23

Assignee: mvngu

It's that time of the year again when the copyright years for Sage need to be updated to reflect the new year. The copyright years should now span 2006--2010. The [Sage wiki](http://wiki.sagemath.org/devel/UpdateCopyright) contains a page that lists file you need to edit in order to update the copyright years.


---

Attachment

README.txt with updated copyright years; based on Sage 4.3.1.alpha2


---

Comment by mvngu created at 2010-01-15 10:57:44

differences between the above updated README.txt and the current one in Sage 4.3.1.alpha2


---

Attachment


---

Attachment

updated copyright years for the Mac app


---

Attachment

apply to sage-main; based on Sage 4.3.1.alpha2


---

Comment by mvngu created at 2010-01-16 07:59:46

I think the above patches should take care of updating the copyright years. Here's a description of these patches and where to apply them:

 1. The file [README.txt](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.txt) should be placed under `SAGE_ROOT/`. That file is not under revision control, so the release manager needs to replace the current `README.txt` with the attached updated `README.txt`. To show the differences between the current `README.txt` in Sage 4.3.1.alpha2 and the updated `README.txt`, see the patch file [README.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/README.patch). Note that this patch is only for showing differences; don't apply it.
 1. The patch [trac_7933-mac-app.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-mac-app.patch) should be applied to the `data/` repository under `SAGE_ROOT/data/extcode`. Before applying that patch, the release manager needs to remove a junk file under that directory:
 {{{
[mvngu`@`mod extcode]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2/data/extcode
[mvngu`@`mod extcode]$ hg st
? sage/ext/.DS_Store.rej
[mvngu`@`mod extcode]$ rm sage/ext/.DS_Store.rej 
[mvngu`@`mod extcode]$ hg st
<no-output>
 }}}
 After removing the junk file, then apply the patch.
 1. Finally, apply the patch [trac_7933-doc-builder.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7933/trac_7933-doc-builder.patch) to the repository `sage-main`. This patch affects the configuration file `doc/common/conf.py`, so the file's corresponding Python byte code file should be removed:
 {{{
[mvngu`@`mod common]$ pwd
/dev/shm/mvngu/sage-4.3.1.alpha2/devel/sage-main/doc/common
[mvngu`@`mod common]$ rm conf.pyc
 }}}
 This ensures that, after the patch is applied, generating the documentation with "./sage -docbuild ..." would first generate a byte code version of the patched `doc/common/conf.py` file. If the previous byte code file of `doc/common/conf.py` is not removed, then it's likely that the generated documentation (especially the HTML version) would still use the current copyright years "2005--2009".


---

Comment by mvngu created at 2010-01-16 07:59:46

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-31 00:17:56

All three patches apply cleanly.  In particular, they're in line with [UpdateCopyright](http://wiki.sagemath.org/devel/UpdateCopyright).

Note: I don't have access to a Mac, so I can't test the changes in the extcode patch (if they're testable).

In case someone hasn't already mentioned it: a current copyright year also hints that a project is actively developed.


---

Comment by mpatel created at 2010-01-31 00:17:56

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-02 05:17:16

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 05:17:16

Merged as per the above instructions.
