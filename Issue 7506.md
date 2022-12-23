# Issue 7506: NotebookObject documentation is out of date

archive/issues_007506.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  jhpalmieri\n\nKeywords: notebook, documentation, server\n\nFrom Chris Wuthrich on sage-edu:\n\"From my perspective the biggest problem was that I did not allocate\nenough resources to the virtual server the notebook was running on.\nI was a bit disappointed with the documentation for setting up a\nserver etc. For instance the docstring of the notebook still contains\nlines like\n  nb = load('./sage/sage_notebook/nb.sobj')\nwhich do not seem to apply any longer. \"\n\nSo at least that needs to be cleaned up in notebook_object.py.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7506\n\n",
    "created_at": "2009-11-21T02:46:12Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "NotebookObject documentation is out of date",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7506",
    "user": "mhampton"
}
```
Assignee: boothby

CC:  jhpalmieri

Keywords: notebook, documentation, server

From Chris Wuthrich on sage-edu:
"From my perspective the biggest problem was that I did not allocate
enough resources to the virtual server the notebook was running on.
I was a bit disappointed with the documentation for setting up a
server etc. For instance the docstring of the notebook still contains
lines like
  nb = load('./sage/sage_notebook/nb.sobj')
which do not seem to apply any longer. "

So at least that needs to be cleaned up in notebook_object.py.

Issue created by migration from https://trac.sagemath.org/ticket/7506





---

archive/issue_comments_063496.json:
```json
{
    "body": "Attachment\n\nThis updates the notebook_object.py documentation and removes the warnings on build.",
    "created_at": "2010-01-19T21:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63496",
    "user": "timdumol"
}
```

Attachment

This updates the notebook_object.py documentation and removes the warnings on build.



---

archive/issue_comments_063497.json:
```json
{
    "body": "Adds `notebook_object` to the reference manual",
    "created_at": "2010-01-19T22:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63497",
    "user": "timdumol"
}
```

Adds `notebook_object` to the reference manual



---

archive/issue_comments_063498.json:
```json
{
    "body": "Attachment\n\nRelated: #4574.",
    "created_at": "2010-01-20T11:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63498",
    "user": "mpatel"
}
```

Attachment

Related: #4574.



---

archive/issue_comments_063499.json:
```json
{
    "body": "Several formatting tweaks.  ``sagenb`` repo.  Replaces previous.",
    "created_at": "2010-01-24T20:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63499",
    "user": "mpatel"
}
```

Several formatting tweaks.  ``sagenb`` repo.  Replaces previous.



---

archive/issue_comments_063500.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-24T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63500",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063501.json:
```json
{
    "body": "Attachment\n\nHi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?\n\nAlso, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?",
    "created_at": "2010-01-24T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63501",
    "user": "mpatel"
}
```

Attachment

Hi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?

Also, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?



---

archive/issue_comments_063502.json:
```json
{
    "body": "V2 just makes formatting changes.",
    "created_at": "2010-01-24T20:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63502",
    "user": "mpatel"
}
```

V2 just makes formatting changes.



---

archive/issue_comments_063503.json:
```json
{
    "body": "A mock-up of V2 is [here](http://sage.math.washington.edu/home/mpatel/trac/7506/notebook_object.html).",
    "created_at": "2010-01-24T20:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63503",
    "user": "mpatel"
}
```

A mock-up of V2 is [here](http://sage.math.washington.edu/home/mpatel/trac/7506/notebook_object.html).



---

archive/issue_comments_063504.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Hi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?\n\nThe patch looks good. \n \n> Also, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?\n\nSure, although that's a bit out of date now...it's still pretty useful, though. I'm planning on updating that page later this spring after Ubuntu Lucid is out.",
    "created_at": "2010-01-25T04:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63504",
    "user": "ddrake"
}
```

Replying to [comment:2 mpatel]:
> Hi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?

The patch looks good. 
 
> Also, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?

Sure, although that's a bit out of date now...it's still pretty useful, though. I'm planning on updating that page later this spring after Ubuntu Lucid is out.



---

archive/issue_comments_063505.json:
```json
{
    "body": "Changing component from notebook to documentation.",
    "created_at": "2010-02-06T16:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63505",
    "user": "mpatel"
}
```

Changing component from notebook to documentation.



---

archive/issue_comments_063506.json:
```json
{
    "body": "Requesting an assist, if time permits.",
    "created_at": "2010-02-06T16:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63506",
    "user": "mpatel"
}
```

Requesting an assist, if time permits.



---

archive/issue_comments_063507.json:
```json
{
    "body": "Given this documentation, should the file sagenb.notebook.notebook_object be added to the Sage reference manual?",
    "created_at": "2010-02-07T21:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63507",
    "user": "jhpalmieri"
}
```

Given this documentation, should the file sagenb.notebook.notebook_object be added to the Sage reference manual?



---

archive/issue_comments_063508.json:
```json
{
    "body": "The patch looks good.  Here's an accompanying patch for the Sage library: for the notebook, the docs here seem like the ones people will want first, so I put it first in the reference manual.\n\n(I feel like I'm missing something: this isn't already in the reference manual, is it?  I looked, but I didn't see it.)",
    "created_at": "2010-02-07T21:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63508",
    "user": "jhpalmieri"
}
```

The patch looks good.  Here's an accompanying patch for the Sage library: for the notebook, the docs here seem like the ones people will want first, so I put it first in the reference manual.

(I feel like I'm missing something: this isn't already in the reference manual, is it?  I looked, but I didn't see it.)



---

archive/issue_comments_063509.json:
```json
{
    "body": "Attachment\n\npatch for the sage repo",
    "created_at": "2010-02-07T21:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63509",
    "user": "jhpalmieri"
}
```

Attachment

patch for the sage repo



---

archive/issue_comments_063510.json:
```json
{
    "body": "I'm willing to give the main patch a positive review.  If the patch for the ref manual is okay, the whole thing can get a positive review.",
    "created_at": "2010-02-07T21:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63510",
    "user": "jhpalmieri"
}
```

I'm willing to give the main patch a positive review.  If the patch for the ref manual is okay, the whole thing can get a positive review.



---

archive/issue_comments_063511.json:
```json
{
    "body": "We should have added a note about [attachment:trac_7506-sage_core_lib-notebook-obj-ref.patch], which also adds `notebook_object` to the reference manual.  I'm not sure why it's missing the usual Mercurial header.\n\nIf Tim doesn't mind, I suggest that the release manager merge\n\n* [attachment:trac_7506-ref-manual.patch] into the sage repo.\n* [attachment:trac_7506-notebook_object-documentation.2.patch] into the sagenb repo.",
    "created_at": "2010-02-09T03:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63511",
    "user": "mpatel"
}
```

We should have added a note about [attachment:trac_7506-sage_core_lib-notebook-obj-ref.patch], which also adds `notebook_object` to the reference manual.  I'm not sure why it's missing the usual Mercurial header.

If Tim doesn't mind, I suggest that the release manager merge

* [attachment:trac_7506-ref-manual.patch] into the sage repo.
* [attachment:trac_7506-notebook_object-documentation.2.patch] into the sagenb repo.



---

archive/issue_comments_063512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-09T03:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63512",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063513.json:
```json
{
    "body": "Oops, I missed that patch -- I saw \"replaces previous\" on the next patch and immediately ignored everything above it.  The two Sage library patches are the same, so it's fine with me if Tim gets credit (I don't care either way about the attribution -- I just want to make sure this gets added to the reference manual).",
    "created_at": "2010-02-09T04:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63513",
    "user": "jhpalmieri"
}
```

Oops, I missed that patch -- I saw "replaces previous" on the next patch and immediately ignored everything above it.  The two Sage library patches are the same, so it's fine with me if Tim gets credit (I don't care either way about the attribution -- I just want to make sure this gets added to the reference manual).



---

archive/issue_comments_063514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7506#issuecomment-63514",
    "user": "mpatel"
}
```

Resolution: fixed
