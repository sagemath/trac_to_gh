# Issue 7926: Bring coverage of monsky_washnitzer up to 50%

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-14 06:52:08

Assignee: was

CC:  jen kedlaya

There's still lots to do here, but I started plowing through the file. 


---

Comment by kedlaya created at 2010-02-20 14:56:13

I haven't looked closely enough yet to be sure, but there's a chance this might need to be rebased after #7927 and #8304 get merged in.


---

Comment by zimmerma created at 2011-09-16 13:28:31

Changing keywords from "" to "ecc2011".


---

Comment by zimmerma created at 2011-09-16 13:28:31

I confirm, this patch fails to apply to Sage 4.7.1 and thus should be rebased:

```
sage: hg_sage.import_patch("/tmp/7926-mw-docs.patch")
cd "/usr/local/sage-4.7.1/sage/devel/sage" && hg status
cd "/usr/local/sage-4.7.1/sage/devel/sage" && hg status
cd "/usr/local/sage-4.7.1/sage/devel/sage" && hg import   "/tmp/7926-mw-docs.patch"
applying /tmp/7926-mw-docs.patch
patching file sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #3 FAILED at 2228
Hunk #6 FAILED at 2391
2 out of 9 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej
patching file sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
Hunk #1 FAILED at 174
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py.rej
abort: patch failed to apply
```

Paul


---

Comment by jen created at 2012-03-21 18:44:52

Changing status from new to needs_review.


---

Comment by jen created at 2012-03-21 18:44:52

Changing keywords from "ecc2011" to "ecc2011, rd2".


---

Attachment

This is a rebase against 5.0.beta9.


---

Comment by davidloeffler created at 2012-03-24 17:30:27

Apply trac_7926_new.patch

(for the patchbot)


---

Comment by zimmerma created at 2012-03-27 16:11:20

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-03-27 16:11:20

positive review. The coverage increased to 53%, which is above the 50% goal of this ticket.

Paul


---

Comment by robertwb created at 2012-03-27 21:05:44

Sorry I never got to 100%, but getting this in now is better than letting it bitrot again.


---

Comment by jdemeyer created at 2012-03-28 07:03:26

The documentation doesn't even build properly:

```
dochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:7: WARNING: Block quote ends without a blank line; unexpected unindent.
dochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:15: WARNING: Block quote ends without a blank line; unexpected unindent.
dochtml.log:WARNING: inline latex u'\\phi(x) = x^p\n\n\\phi(y) = y^p \\sqrt{1 ': latex exited with error:
dochtml.log:WARNING: inline latex u'\\phi^*(dx/2y) = px^{p-1} y(\\phi(y))^{-1} dx/2y\n              = px^{p-1} y^{1-p} \\sqrt{1 ': latex exited with error:
```



---

Comment by jdemeyer created at 2012-03-28 07:03:26

Changing status from positive_review to needs_work.


---

Comment by zimmerma created at 2012-03-28 09:46:05

sorry Jeroen I did a bad reviewer job. But how can one check the documentation builds properly?

Paul


---

Comment by jdemeyer created at 2012-03-28 09:50:52

The easiest way is

```
make doc
```

from $SAGE_ROOT, but that will build more than you need.

You could also do (from $SAGE_ROOT):

```
./sage --docbuild reference html
```


Note that the documentation will actually build, there aren only WARNINGs.  So you have to look for warnings in the on-screen output.


---

Comment by davidloeffler created at 2012-03-28 10:01:09

You can also look in the output of the patchbot (click on the swirly round blob by the ticket title and go to "plugins.docbuild"). The patchbot builds the reference manual with jsmath, which means it misses the third error (because it doesn't attempt to process latex formulae at build time), but it spots the other two.


---

Comment by zimmerma created at 2012-03-28 11:07:59

thank you Jeroen and David, but how can I identify the corrupted lines? The numbers 7 and 15 do not seem to correspond to bad block quotes.

Paul


---

Comment by davidloeffler created at 2012-03-28 12:23:34

The problem is that the docstring of ` matrix_of_frobenius ` is a plain string, not a raw string (`r""" ... """)` and hence it interprets the ` \f ` in ` \frac ` as a form feed character! This completely mangles Sphinx's parsing of the Latex formulae, unsurprisingly.


---

Comment by davidloeffler created at 2012-03-28 12:25:08

Apply over previous patch


---

Attachment

Here's a patch which makes the reference manual build without errors, and corrects a few other minor formatting problems which I spotted while I was fixing this.


---

Comment by davidloeffler created at 2012-03-28 12:26:08

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-03-28 12:30:02

Not tested yet, but looks good on first sight.


---

Comment by zimmerma created at 2012-03-28 13:08:44

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-03-28 13:08:44

I've done `make doc` and there is no warning any more (more precisely the only warnings I get are because the dvipng command is not installed on my computer).

Paul


---

Comment by jdemeyer created at 2012-04-02 15:23:57

Resolution: fixed
