# Issue 7926: Bring coverage of monsky_washnitzer up to 50%

archive/issues_007926.json:
```json
{
    "body": "Assignee: was\n\nCC:  jen kedlaya\n\nThere's still lots to do here, but I started plowing through the file. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7926\n\n",
    "created_at": "2010-01-14T06:52:08Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Bring coverage of monsky_washnitzer up to 50%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7926",
    "user": "robertwb"
}
```
Assignee: was

CC:  jen kedlaya

There's still lots to do here, but I started plowing through the file. 

Issue created by migration from https://trac.sagemath.org/ticket/7926





---

archive/issue_comments_068981.json:
```json
{
    "body": "I haven't looked closely enough yet to be sure, but there's a chance this might need to be rebased after #7927 and #8304 get merged in.",
    "created_at": "2010-02-20T14:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68981",
    "user": "kedlaya"
}
```

I haven't looked closely enough yet to be sure, but there's a chance this might need to be rebased after #7927 and #8304 get merged in.



---

archive/issue_comments_068982.json:
```json
{
    "body": "Changing keywords from \"\" to \"ecc2011\".",
    "created_at": "2011-09-16T13:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68982",
    "user": "zimmerma"
}
```

Changing keywords from "" to "ecc2011".



---

archive/issue_comments_068983.json:
```json
{
    "body": "I confirm, this patch fails to apply to Sage 4.7.1 and thus should be rebased:\n\n```\nsage: hg_sage.import_patch(\"/tmp/7926-mw-docs.patch\")\ncd \"/usr/local/sage-4.7.1/sage/devel/sage\" && hg status\ncd \"/usr/local/sage-4.7.1/sage/devel/sage\" && hg status\ncd \"/usr/local/sage-4.7.1/sage/devel/sage\" && hg import   \"/tmp/7926-mw-docs.patch\"\napplying /tmp/7926-mw-docs.patch\npatching file sage/schemes/elliptic_curves/monsky_washnitzer.py\nHunk #3 FAILED at 2228\nHunk #6 FAILED at 2391\n2 out of 9 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej\npatching file sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\nHunk #1 FAILED at 174\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py.rej\nabort: patch failed to apply\n```\n\nPaul",
    "created_at": "2011-09-16T13:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68983",
    "user": "zimmerma"
}
```

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

archive/issue_comments_068984.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-21T18:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68984",
    "user": "jen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068985.json:
```json
{
    "body": "Changing keywords from \"ecc2011\" to \"ecc2011, rd2\".",
    "created_at": "2012-03-21T18:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68985",
    "user": "jen"
}
```

Changing keywords from "ecc2011" to "ecc2011, rd2".



---

archive/issue_comments_068986.json:
```json
{
    "body": "Attachment [trac_7926_new.patch](tarball://root/attachments/some-uuid/ticket7926/trac_7926_new.patch) by jen created at 2012-03-21 18:44:52\n\nThis is a rebase against 5.0.beta9.",
    "created_at": "2012-03-21T18:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68986",
    "user": "jen"
}
```

Attachment [trac_7926_new.patch](tarball://root/attachments/some-uuid/ticket7926/trac_7926_new.patch) by jen created at 2012-03-21 18:44:52

This is a rebase against 5.0.beta9.



---

archive/issue_comments_068987.json:
```json
{
    "body": "Apply trac_7926_new.patch\n\n(for the patchbot)",
    "created_at": "2012-03-24T17:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68987",
    "user": "davidloeffler"
}
```

Apply trac_7926_new.patch

(for the patchbot)



---

archive/issue_comments_068988.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-27T16:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68988",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068989.json:
```json
{
    "body": "positive review. The coverage increased to 53%, which is above the 50% goal of this ticket.\n\nPaul",
    "created_at": "2012-03-27T16:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68989",
    "user": "zimmerma"
}
```

positive review. The coverage increased to 53%, which is above the 50% goal of this ticket.

Paul



---

archive/issue_comments_068990.json:
```json
{
    "body": "Sorry I never got to 100%, but getting this in now is better than letting it bitrot again.",
    "created_at": "2012-03-27T21:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68990",
    "user": "robertwb"
}
```

Sorry I never got to 100%, but getting this in now is better than letting it bitrot again.



---

archive/issue_comments_068991.json:
```json
{
    "body": "The documentation doesn't even build properly:\n\n```\ndochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:7: WARNING: Block quote ends without a blank line; unexpected unindent.\ndochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:15: WARNING: Block quote ends without a blank line; unexpected unindent.\ndochtml.log:WARNING: inline latex u'\\\\phi(x) = x^p\\n\\n\\\\phi(y) = y^p \\\\sqrt{1 ': latex exited with error:\ndochtml.log:WARNING: inline latex u'\\\\phi^*(dx/2y) = px^{p-1} y(\\\\phi(y))^{-1} dx/2y\\n              = px^{p-1} y^{1-p} \\\\sqrt{1 ': latex exited with error:\n```\n",
    "created_at": "2012-03-28T07:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68991",
    "user": "jdemeyer"
}
```

The documentation doesn't even build properly:

```
dochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:7: WARNING: Block quote ends without a blank line; unexpected unindent.
dochtml.log:/padic/scratch/jdemeyer/merger/sage-5.0.beta12/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py:docstring of sage.schemes.elliptic_curves.monsky_washnitzer:15: WARNING: Block quote ends without a blank line; unexpected unindent.
dochtml.log:WARNING: inline latex u'\\phi(x) = x^p\n\n\\phi(y) = y^p \\sqrt{1 ': latex exited with error:
dochtml.log:WARNING: inline latex u'\\phi^*(dx/2y) = px^{p-1} y(\\phi(y))^{-1} dx/2y\n              = px^{p-1} y^{1-p} \\sqrt{1 ': latex exited with error:
```




---

archive/issue_comments_068992.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-28T07:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68992",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068993.json:
```json
{
    "body": "sorry Jeroen I did a bad reviewer job. But how can one check the documentation builds properly?\n\nPaul",
    "created_at": "2012-03-28T09:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68993",
    "user": "zimmerma"
}
```

sorry Jeroen I did a bad reviewer job. But how can one check the documentation builds properly?

Paul



---

archive/issue_comments_068994.json:
```json
{
    "body": "The easiest way is\n\n```\nmake doc\n```\n\nfrom $SAGE_ROOT, but that will build more than you need.\n\nYou could also do (from $SAGE_ROOT):\n\n```\n./sage --docbuild reference html\n```\n\n\nNote that the documentation will actually build, there aren only WARNINGs.  So you have to look for warnings in the on-screen output.",
    "created_at": "2012-03-28T09:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68994",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_068995.json:
```json
{
    "body": "You can also look in the output of the patchbot (click on the swirly round blob by the ticket title and go to \"plugins.docbuild\"). The patchbot builds the reference manual with jsmath, which means it misses the third error (because it doesn't attempt to process latex formulae at build time), but it spots the other two.",
    "created_at": "2012-03-28T10:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68995",
    "user": "davidloeffler"
}
```

You can also look in the output of the patchbot (click on the swirly round blob by the ticket title and go to "plugins.docbuild"). The patchbot builds the reference manual with jsmath, which means it misses the third error (because it doesn't attempt to process latex formulae at build time), but it spots the other two.



---

archive/issue_comments_068996.json:
```json
{
    "body": "thank you Jeroen and David, but how can I identify the corrupted lines? The numbers 7 and 15 do not seem to correspond to bad block quotes.\n\nPaul",
    "created_at": "2012-03-28T11:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68996",
    "user": "zimmerma"
}
```

thank you Jeroen and David, but how can I identify the corrupted lines? The numbers 7 and 15 do not seem to correspond to bad block quotes.

Paul



---

archive/issue_comments_068997.json:
```json
{
    "body": "The problem is that the docstring of ` matrix_of_frobenius ` is a plain string, not a raw string (`r\"\"\" ... \"\"\")` and hence it interprets the ` \\f ` in ` \\frac ` as a form feed character! This completely mangles Sphinx's parsing of the Latex formulae, unsurprisingly.",
    "created_at": "2012-03-28T12:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68997",
    "user": "davidloeffler"
}
```

The problem is that the docstring of ` matrix_of_frobenius ` is a plain string, not a raw string (`r""" ... """)` and hence it interprets the ` \f ` in ` \frac ` as a form feed character! This completely mangles Sphinx's parsing of the Latex formulae, unsurprisingly.



---

archive/issue_comments_068998.json:
```json
{
    "body": "Apply over previous patch",
    "created_at": "2012-03-28T12:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68998",
    "user": "davidloeffler"
}
```

Apply over previous patch



---

archive/issue_comments_068999.json:
```json
{
    "body": "Attachment [trac_7926-fix.patch](tarball://root/attachments/some-uuid/ticket7926/trac_7926-fix.patch) by davidloeffler created at 2012-03-28 12:26:08\n\nHere's a patch which makes the reference manual build without errors, and corrects a few other minor formatting problems which I spotted while I was fixing this.",
    "created_at": "2012-03-28T12:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-68999",
    "user": "davidloeffler"
}
```

Attachment [trac_7926-fix.patch](tarball://root/attachments/some-uuid/ticket7926/trac_7926-fix.patch) by davidloeffler created at 2012-03-28 12:26:08

Here's a patch which makes the reference manual build without errors, and corrects a few other minor formatting problems which I spotted while I was fixing this.



---

archive/issue_comments_069000.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-28T12:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-69000",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069001.json:
```json
{
    "body": "Not tested yet, but looks good on first sight.",
    "created_at": "2012-03-28T12:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-69001",
    "user": "jdemeyer"
}
```

Not tested yet, but looks good on first sight.



---

archive/issue_comments_069002.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-28T13:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-69002",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069003.json:
```json
{
    "body": "I've done `make doc` and there is no warning any more (more precisely the only warnings I get are because the dvipng command is not installed on my computer).\n\nPaul",
    "created_at": "2012-03-28T13:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-69003",
    "user": "zimmerma"
}
```

I've done `make doc` and there is no warning any more (more precisely the only warnings I get are because the dvipng command is not installed on my computer).

Paul



---

archive/issue_comments_069004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-02T15:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7926#issuecomment-69004",
    "user": "jdemeyer"
}
```

Resolution: fixed
