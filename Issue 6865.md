# Issue 6865: Use templates for CSS

archive/issues_006865.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: notebook css stylesheets\n\nCSS is currently served by `css()` in `css.py`, even though it is completely static. Using templates for it should make things easier to customize in the future.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6865\n\n",
    "created_at": "2009-09-02T15:30:45Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Use templates for CSS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6865",
    "user": "timdumol"
}
```
Assignee: boothby

Keywords: notebook css stylesheets

CSS is currently served by `css()` in `css.py`, even though it is completely static. Using templates for it should make things easier to customize in the future.

Issue created by migration from https://trac.sagemath.org/ticket/6865





---

archive/issue_comments_056658.json:
```json
{
    "body": "Moved CSS in `css.py` to templates, and adjusted `twist.py` to use them.",
    "created_at": "2009-09-02T16:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56658",
    "user": "timdumol"
}
```

Moved CSS in `css.py` to templates, and adjusted `twist.py` to use them.



---

archive/issue_comments_056659.json:
```json
{
    "body": "Attachment [trac_6865-templates-css.patch](tarball://root/attachments/some-uuid/ticket6865/trac_6865-templates-css.patch) by timdumol created at 2009-09-02 16:20:43",
    "created_at": "2009-09-02T16:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56659",
    "user": "timdumol"
}
```

Attachment [trac_6865-templates-css.patch](tarball://root/attachments/some-uuid/ticket6865/trac_6865-templates-css.patch) by timdumol created at 2009-09-02 16:20:43



---

archive/issue_comments_056660.json:
```json
{
    "body": "This probably needs to be rebased after #6939 to include the CSS fix there (or the rebasing should go the other way, if this gets reviewed before that gets merged...)",
    "created_at": "2009-09-17T19:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56660",
    "user": "jason"
}
```

This probably needs to be rebased after #6939 to include the CSS fix there (or the rebasing should go the other way, if this gets reviewed before that gets merged...)



---

archive/issue_comments_056661.json:
```json
{
    "body": "#6940 is a dup of this ticket (i.e., close #6940).",
    "created_at": "2009-09-17T19:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56661",
    "user": "jason"
}
```

#6940 is a dup of this ticket (i.e., close #6940).



---

archive/issue_comments_056662.json:
```json
{
    "body": "Does the patch depend on another ticket's patch?  Applying [attachment:trac_6865-templates-css.patch] to 4.1.2.alpha1, I get\n\n```\napplying trac_6865-templates-css.patch\npatching file sage/server/notebook/css.py\nHunk #1 FAILED at 0\n1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/css.py.rej\npatching file sage/server/notebook/twist.py\nHunk #1 FAILED at 133\nHunk #2 succeeded at 1787 with fuzz 1 (offset 37 lines).\nHunk #3 FAILED at 2315\n2 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_6865-templates-css.patch\n```\n\nThe important one is the last, which doesn't apply because the local `twist.py` contains\n\n```python\n        elif self.problem == 'suspended':\n            return HTMLResponse(stream = message(\"Your account is currently suspended.\"))\n```\n\nBut I could have altered my configuration.",
    "created_at": "2009-09-17T22:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56662",
    "user": "mpatel"
}
```

Does the patch depend on another ticket's patch?  Applying [attachment:trac_6865-templates-css.patch] to 4.1.2.alpha1, I get

```
applying trac_6865-templates-css.patch
patching file sage/server/notebook/css.py
Hunk #1 FAILED at 0
1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/css.py.rej
patching file sage/server/notebook/twist.py
Hunk #1 FAILED at 133
Hunk #2 succeeded at 1787 with fuzz 1 (offset 37 lines).
Hunk #3 FAILED at 2315
2 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/twist.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6865-templates-css.patch
```

The important one is the last, which doesn't apply because the local `twist.py` contains

```python
        elif self.problem == 'suspended':
            return HTMLResponse(stream = message("Your account is currently suspended."))
```

But I could have altered my configuration.



---

archive/issue_comments_056663.json:
```json
{
    "body": "I think we need to add\n\n```\ninclude sage/server/notebook/css/*\n```\n\nto `MANIFEST.in,` or we'll definitely hear from the release manager...",
    "created_at": "2009-09-18T02:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56663",
    "user": "mpatel"
}
```

I think we need to add

```
include sage/server/notebook/css/*
```

to `MANIFEST.in,` or we'll definitely hear from the release manager...



---

archive/issue_comments_056664.json:
```json
{
    "body": "What is MANIFEST.in and when do we need to add things to it?",
    "created_at": "2009-09-19T02:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56664",
    "user": "jason"
}
```

What is MANIFEST.in and when do we need to add things to it?



---

archive/issue_comments_056665.json:
```json
{
    "body": "(setting to \"needs work\", based on mpatel's comment about MANIFEST.in and his comment about applying the patch)",
    "created_at": "2009-09-19T02:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56665",
    "user": "jason"
}
```

(setting to "needs work", based on mpatel's comment about MANIFEST.in and his comment about applying the patch)



---

archive/issue_comments_056666.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> What is MANIFEST.in and when do we need to add things to it?\nI believe the `sage -bdist` and `sage -sdist` invoke [distutils](http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute) to build `sage-*.spkg`.  Distutils uses `SAGE_ROOT/devel/sage/MANIFEST.in` to determine which files to include in the distribution.  If we add files to the local Mercurial repository, we should check that some line(s) in `MANIFEST.in` includes the newly tracked files or add a new line.  Otherwise, the next (pre-)release of Sage will not include them.  As mvngu puts it, this results in [\"repository corruption\"](http://groups.google.com/group/sage-devel/browse_thread/thread/697693c77e8d7ee8/290f2ec5412b909d?q=repository+corruption+group:sage-devel#290f2ec5412b909d).\n\nPrevious sightings: #4460, #5653, #5799, #6568, etc.",
    "created_at": "2009-09-19T05:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56666",
    "user": "mpatel"
}
```

Replying to [comment:6 jason]:
> What is MANIFEST.in and when do we need to add things to it?
I believe the `sage -bdist` and `sage -sdist` invoke [distutils](http://docs.python.org/distutils/sourcedist.html#specifying-the-files-to-distribute) to build `sage-*.spkg`.  Distutils uses `SAGE_ROOT/devel/sage/MANIFEST.in` to determine which files to include in the distribution.  If we add files to the local Mercurial repository, we should check that some line(s) in `MANIFEST.in` includes the newly tracked files or add a new line.  Otherwise, the next (pre-)release of Sage will not include them.  As mvngu puts it, this results in ["repository corruption"](http://groups.google.com/group/sage-devel/browse_thread/thread/697693c77e8d7ee8/290f2ec5412b909d?q=repository+corruption+group:sage-devel#290f2ec5412b909d).

Previous sightings: #4460, #5653, #5799, #6568, etc.



---

archive/issue_comments_056667.json:
```json
{
    "body": "No, this doesn't depend on other patches. It is based on 4.1.2.alpha1.\n\nI've made the requisite changes to `MANIFEST.in`.",
    "created_at": "2009-09-20T03:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56667",
    "user": "timdumol"
}
```

No, this doesn't depend on other patches. It is based on 4.1.2.alpha1.

I've made the requisite changes to `MANIFEST.in`.



---

archive/issue_comments_056668.json:
```json
{
    "body": "Moved CSS in css.py to templates, and adjusted twist.py to use them. Rev 2. Apply this patch only.",
    "created_at": "2009-09-20T03:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56668",
    "user": "timdumol"
}
```

Moved CSS in css.py to templates, and adjusted twist.py to use them. Rev 2. Apply this patch only.



---

archive/issue_comments_056669.json:
```json
{
    "body": "Attachment [trac_6865-templates-css.3.patch](tarball://root/attachments/some-uuid/ticket6865/trac_6865-templates-css.3.patch) by mpatel created at 2009-09-21 00:30:15\n\nMoved CSS in css.py to templates, and adjusted twist.py to use them. Rev 3. Apply this patch only.",
    "created_at": "2009-09-21T00:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56669",
    "user": "mpatel"
}
```

Attachment [trac_6865-templates-css.3.patch](tarball://root/attachments/some-uuid/ticket6865/trac_6865-templates-css.3.patch) by mpatel created at 2009-09-21 00:30:15

Moved CSS in css.py to templates, and adjusted twist.py to use them. Rev 3. Apply this patch only.



---

archive/issue_comments_056670.json:
```json
{
    "body": "Changes in patch v3:\n\n* `css.py`: `if os.path.exists(user_css):` --> `if os.path.exists(user_css_path):`\n* `css.py`: `+` --> `os.path.join()`\n* `css.py`: html -> HTML in docstring\n* `main.css`: {% ->  {%-\n\nSorry about the trivial stuff.  I just noticed the [whitespace control](http://jinja.pocoo.org/2/documentation/templates#whitespace-control) part of the Jinja2 docs.\n\nThis is a positive review from me, but someone should review my changes.",
    "created_at": "2009-09-21T00:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56670",
    "user": "mpatel"
}
```

Changes in patch v3:

* `css.py`: `if os.path.exists(user_css):` --> `if os.path.exists(user_css_path):`
* `css.py`: `+` --> `os.path.join()`
* `css.py`: html -> HTML in docstring
* `main.css`: {% ->  {%-

Sorry about the trivial stuff.  I just noticed the [whitespace control](http://jinja.pocoo.org/2/documentation/templates#whitespace-control) part of the Jinja2 docs.

This is a positive review from me, but someone should review my changes.



---

archive/issue_comments_056671.json:
```json
{
    "body": "Your changes look good to me.",
    "created_at": "2009-09-22T17:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56671",
    "user": "jason"
}
```

Your changes look good to me.



---

archive/issue_comments_056672.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-09-22T17:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56672",
    "user": "jason"
}
```

Changing priority from minor to major.



---

archive/issue_comments_056673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-22T17:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56673",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056674.json:
```json
{
    "body": "Merged `trac_6865-templates-css.3.patch`.",
    "created_at": "2009-09-22T17:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56674",
    "user": "mvngu"
}
```

Merged `trac_6865-templates-css.3.patch`.



---

archive/issue_comments_056675.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.",
    "created_at": "2009-09-27T09:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6865#issuecomment-56675",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
