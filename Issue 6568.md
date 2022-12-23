# Issue 6568: Migrate Notebook to Jinja

archive/issues_006568.json:
```json
{
    "body": "Assignee: timdumol\n\nCC:  jason\n\nKeywords: notebook, jinja,templating engine\n\nJinja is a templating engine based on Django's. It's already included\nin Sage due to the inclusion of Sphinx. Migrating from HTML to\ntemplates should make it easier to make future changes to the code,\nand make things easier to read.\n\nAdditionally, this will give us the option of switching to a web framework such as Django.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6568\n\n",
    "created_at": "2009-07-20T13:50:24Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "Migrate Notebook to Jinja",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6568",
    "user": "timdumol"
}
```
Assignee: timdumol

CC:  jason

Keywords: notebook, jinja,templating engine

Jinja is a templating engine based on Django's. It's already included
in Sage due to the inclusion of Sphinx. Migrating from HTML to
templates should make it easier to make future changes to the code,
and make things easier to read.

Additionally, this will give us the option of switching to a web framework such as Django.

Issue created by migration from https://trac.sagemath.org/ticket/6568





---

archive/issue_comments_053580.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-20T17:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53580",
    "user": "timdumol"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053581.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-07-20T17:40:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53581",
    "user": "timdumol"
}
```

Changing priority from major to minor.



---

archive/issue_comments_053582.json:
```json
{
    "body": "timdumol: There should be a proper username on the patch. At the moment I see this\n\n```\n# User deadlyx@localhost.localdomain\n```\n\nThe username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:\n\n```\n# User Full Name <email@somewhere.com>\n```\n\nYou can set a proper username in the file `~/.hgrc` with something like\n\n```\n[ui]\nusername = Full Name <email@somewhere.com>\n```\n\nI say \"should\", not \"must\". If you don't want to, then at least fill in the \"Author(s):\" field with your full name. That way, it makes it easy to credit you.",
    "created_at": "2009-07-20T19:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53582",
    "user": "mvngu"
}
```

timdumol: There should be a proper username on the patch. At the moment I see this

```
# User deadlyx@localhost.localdomain
```

The username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:

```
# User Full Name <email@somewhere.com>
```

You can set a proper username in the file `~/.hgrc` with something like

```
[ui]
username = Full Name <email@somewhere.com>
```

I say "should", not "must". If you don't want to, then at least fill in the "Author(s):" field with your full name. That way, it makes it easy to credit you.



---

archive/issue_comments_053583.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> timdumol: There should be a proper username on the patch. At the moment I see this\n> {{{\n> # User deadlyx`@`localhost.localdomain\n> }}}\n> The username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:\n> {{{\n> # User Full Name <email`@`somewhere.com>\n> }}}\n> You can set a proper username in the file `~/.hgrc` with something like\n> {{{\n> [ui]\n> username = Full Name <email`@`somewhere.com>\n> }}}\n> I say \"should\", not \"must\". If you don't want to, then at least fill in the \"Author(s):\" field with your full name. That way, it makes it easy to credit you.\n\nThank you very much for noticing that. I didn't realize that my local username was included in the patch. I'll fix it asap.",
    "created_at": "2009-07-21T10:10:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53583",
    "user": "timdumol"
}
```

Replying to [comment:3 mvngu]:
> timdumol: There should be a proper username on the patch. At the moment I see this
> {{{
> # User deadlyx`@`localhost.localdomain
> }}}
> The username should not be a leet handle or anything like that. In order to properly credit contributors to Sage, the username should following this format:
> {{{
> # User Full Name <email`@`somewhere.com>
> }}}
> You can set a proper username in the file `~/.hgrc` with something like
> {{{
> [ui]
> username = Full Name <email`@`somewhere.com>
> }}}
> I say "should", not "must". If you don't want to, then at least fill in the "Author(s):" field with your full name. That way, it makes it easy to credit you.

Thank you very much for noticing that. I didn't realize that my local username was included in the patch. I'll fix it asap.



---

archive/issue_comments_053584.json:
```json
{
    "body": "Changing keywords from \"notebook, jinja,templating engine\" to \"notebook, jinja, templating engine\".",
    "created_at": "2009-07-21T12:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53584",
    "user": "timdumol"
}
```

Changing keywords from "notebook, jinja,templating engine" to "notebook, jinja, templating engine".



---

archive/issue_comments_053585.json:
```json
{
    "body": "Hi,\n\nI get 8 rejects when trying to apply the first patch to a 100% clean build of sage-4.1:\n\n\n```\nwstein@sage:~/build/sage-4.1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: ref3\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6568/12659.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6568/12659.patch\nLoading: [.........]\ncd \"/scratch/wstein/build/sage-4.1/devel/sage\" && hg status\n/scratch/wstein/build/sage-4.1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.\n  x = os.popen3(s)\ncd \"/scratch/wstein/build/sage-4.1/devel/sage\" && hg status\ncd \"/scratch/wstein/build/sage-4.1/devel/sage\" && hg import   \"/scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch\"\napplying /scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch\npatching file sage/server/notebook/notebook.py\nHunk #1 FAILED at 23\nHunk #2 FAILED at 32\nHunk #3 FAILED at 1355\nHunk #4 FAILED at 1402\nHunk #5 FAILED at 1506\nHunk #6 FAILED at 1704\nHunk #7 FAILED at 1903\nHunk #8 FAILED at 2162\n8 out of 8 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej\nfile sage/server/notebook/templates/debug_window.html already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/debug_window.html.rej\nfile sage/server/notebook/templates/guest_top_bar_and_worksheet.html already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/guest_top_bar_and_worksheet.html.rej\nfile sage/server/notebook/templates/head.html already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/head.html.rej\nfile sage/server/notebook/templates/top_bar_and_worksheet.html already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/top_bar_and_worksheet.html.rej\nfile sage/server/notebook/templates/user_controls.tmpl already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/user_controls.tmpl.rej\nfile sage/server/notebook/templates/worksheet_body.html already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_body.html.rej\nfile sage/server/notebook/templates/worksheet_topbar.tmpl already exists\n1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_topbar.tmpl.rej\nabort: patch failed to apply\n```\n\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\nWhat should I do?  What are these patches against exactly?",
    "created_at": "2009-07-26T19:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53585",
    "user": "was"
}
```

Hi,

I get 8 rejects when trying to apply the first patch to a 100% clean build of sage-4.1:


```
wstein@sage:~/build/sage-4.1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref3
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6568/12659.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6568/12659.patch
Loading: [.........]
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg status
/scratch/wstein/build/sage-4.1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-4.1/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/5378/tmp_1.patch
patching file sage/server/notebook/notebook.py
Hunk #1 FAILED at 23
Hunk #2 FAILED at 32
Hunk #3 FAILED at 1355
Hunk #4 FAILED at 1402
Hunk #5 FAILED at 1506
Hunk #6 FAILED at 1704
Hunk #7 FAILED at 1903
Hunk #8 FAILED at 2162
8 out of 8 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
file sage/server/notebook/templates/debug_window.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/debug_window.html.rej
file sage/server/notebook/templates/guest_top_bar_and_worksheet.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/guest_top_bar_and_worksheet.html.rej
file sage/server/notebook/templates/head.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/head.html.rej
file sage/server/notebook/templates/top_bar_and_worksheet.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/top_bar_and_worksheet.html.rej
file sage/server/notebook/templates/user_controls.tmpl already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/user_controls.tmpl.rej
file sage/server/notebook/templates/worksheet_body.html already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_body.html.rej
file sage/server/notebook/templates/worksheet_topbar.tmpl already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_topbar.tmpl.rej
abort: patch failed to apply
```

| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
What should I do?  What are these patches against exactly?



---

archive/issue_comments_053586.json:
```json
{
    "body": "`@`was:\nIt seems something went wrong with the patch exporting. I cleaned up my hg history and combined a few changesets to make the patches easier to apply. The new patches are _12659.patch and _12660.patch. Sorry for the inconvenience.\n\nThe new patches are against r12658. The old ones were as well, but I don't know what happened to them.",
    "created_at": "2009-07-27T02:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53586",
    "user": "timdumol"
}
```

`@`was:
It seems something went wrong with the patch exporting. I cleaned up my hg history and combined a few changesets to make the patches easier to apply. The new patches are _12659.patch and _12660.patch. Sorry for the inconvenience.

The new patches are against r12658. The old ones were as well, but I don't know what happened to them.



---

archive/issue_comments_053587.json:
```json
{
    "body": "I can't apply/review this patch immediately, but it seems that each change appears twice in the latest version.  For example, \n\n```\n$ grep \"sage/server/notebook/templates/notebook/worksheet.html\" _12660.patch\ndiff -r d3be9e0b1090 -r a60e86f38be7 sage/server/notebook/templates/notebook/worksheet.html\n+++ b/sage/server/notebook/templates/notebook/worksheet.html    Sun Jul 26 14:08:17 2009 +0800\ndiff -r d3be9e0b1090 -r 1335daa5adcd sage/server/notebook/templates/notebook/worksheet.html\n+++ b/sage/server/notebook/templates/notebook/worksheet.html    Tue Jul 28 21:33:54 2009 +0800\n```\n\nAlso, should \"reviisons\" appear in the patch?  Sorry, if I'm wrong.",
    "created_at": "2009-08-04T06:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53587",
    "user": "mpatel"
}
```

I can't apply/review this patch immediately, but it seems that each change appears twice in the latest version.  For example, 

```
$ grep "sage/server/notebook/templates/notebook/worksheet.html" _12660.patch
diff -r d3be9e0b1090 -r a60e86f38be7 sage/server/notebook/templates/notebook/worksheet.html
+++ b/sage/server/notebook/templates/notebook/worksheet.html    Sun Jul 26 14:08:17 2009 +0800
diff -r d3be9e0b1090 -r 1335daa5adcd sage/server/notebook/templates/notebook/worksheet.html
+++ b/sage/server/notebook/templates/notebook/worksheet.html    Tue Jul 28 21:33:54 2009 +0800
```

Also, should "reviisons" appear in the patch?  Sorry, if I'm wrong.



---

archive/issue_comments_053588.json:
```json
{
    "body": "The transition to templates is much needed and appreciated.  Thanks very much for doing this.  Is it possible to break up the changes into a few separate pieces, possibly logically independent?  This might make it easier to review them and to get feedback on and track down any changes in the behavior of the notebook.  On the other hand, it may be better to do it all at once.  Thoughts?",
    "created_at": "2009-08-04T06:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53588",
    "user": "mpatel"
}
```

The transition to templates is much needed and appreciated.  Thanks very much for doing this.  Is it possible to break up the changes into a few separate pieces, possibly logically independent?  This might make it easier to review them and to get feedback on and track down any changes in the behavior of the notebook.  On the other hand, it may be better to do it all at once.  Thoughts?



---

archive/issue_comments_053589.json:
```json
{
    "body": "`@`mpatel\n\nThanks for the feedback. Yeah, that's a typo. Thanks for catching it.\n\nIt seems that the patches are messed up. I've fixed them up with `hg histedit`. I don't see any repeated changes in the patches anymore. Please tell me if there are anymore problems.\n\nBreaking them up seems like a good idea. There are quite a lot of functions though, so there'll be a lot of patches. It may be inconvenient to try them all. Anyways, I'll work on them asap.",
    "created_at": "2009-08-05T01:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53589",
    "user": "timdumol"
}
```

`@`mpatel

Thanks for the feedback. Yeah, that's a typo. Thanks for catching it.

It seems that the patches are messed up. I've fixed them up with `hg histedit`. I don't see any repeated changes in the patches anymore. Please tell me if there are anymore problems.

Breaking them up seems like a good idea. There are quite a lot of functions though, so there'll be a lot of patches. It may be inconvenient to try them all. Anyways, I'll work on them asap.



---

archive/issue_comments_053590.json:
```json
{
    "body": "Migrated notebook.py from HTML to Jinja. Base: r12658 (Sage 4.4.1)",
    "created_at": "2009-08-05T01:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53590",
    "user": "timdumol"
}
```

Migrated notebook.py from HTML to Jinja. Base: r12658 (Sage 4.4.1)



---

archive/issue_comments_053591.json:
```json
{
    "body": "Attachment\n\nMigrated worksheet.py to Jinja. Added doctests. Removed html_slide_controls. Incremental patch from the first patch.",
    "created_at": "2009-08-05T01:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53591",
    "user": "timdumol"
}
```

Attachment

Migrated worksheet.py to Jinja. Added doctests. Removed html_slide_controls. Incremental patch from the first patch.



---

archive/issue_comments_053592.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53592",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053593.json:
```json
{
    "body": "OBSOLETE.",
    "created_at": "2009-08-05T01:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53593",
    "user": "timdumol"
}
```

OBSOLETE.



---

archive/issue_comments_053594.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:41:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53594",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053595.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53595",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053596.json:
```json
{
    "body": "OBSOLETE.",
    "created_at": "2009-08-05T01:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53596",
    "user": "timdumol"
}
```

OBSOLETE.



---

archive/issue_comments_053597.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53597",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053598.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53598",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053599.json:
```json
{
    "body": "OBSOLETE.",
    "created_at": "2009-08-05T01:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53599",
    "user": "timdumol"
}
```

OBSOLETE.



---

archive/issue_comments_053600.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53600",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053601.json:
```json
{
    "body": "OBSOLETE.",
    "created_at": "2009-08-05T01:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53601",
    "user": "timdumol"
}
```

OBSOLETE.



---

archive/issue_comments_053602.json:
```json
{
    "body": "Attachment\n\nOBSOLETE.",
    "created_at": "2009-08-05T01:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53602",
    "user": "timdumol"
}
```

Attachment

OBSOLETE.



---

archive/issue_comments_053603.json:
```json
{
    "body": "Attachment\n\n#4808 appears to be a duplicate of this ticket.  When one is merged, please consider closing the other.",
    "created_at": "2009-08-10T09:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53603",
    "user": "mpatel"
}
```

Attachment

#4808 appears to be a duplicate of this ticket.  When one is merged, please consider closing the other.



---

archive/issue_comments_053604.json:
```json
{
    "body": "From some testing in Firefox 3.5 on Linux, with both new patches applied:\n* Live doc worksheets do not load their stylesheets.\n* Published worksheets are now [partially] editable.\n* The \"re-publish\" and \"stop publishing\" buttons do not work, apparently.\n* The print representation of a worksheet is missing cell boundaries.\n\nAlso, a number of doctests in `notebook.py` and `worksheet.py` failed with `sage -t -long -option -verbose -randorder`.  For `worksheet.py`, there are mostly just small changes in expected HTML output.  I think some of the randomized failures are pre-existing:\n\n```\nsage -t -long -optional -randorder=87873 \"4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py\"\n**********************************************************************\nFile \"/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py\", line 178:\n    sage: sage.server.notebook.worksheet.one_prestarted_sage(None,None)\nExpected:\n    Sage\nGot nothing\n**********************************************************************\nFile \"/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py\", line 148:\n    sage: sage.server.notebook.worksheet._a_sage\nExpected nothing\nGot:\n    Sage\n**********************************************************************\n2 items had failures:\n   1 of   6 in __main__.example_1270084472\n   1 of   5 in __main__.example_1700749147\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/apps/sage/tmp/.doctest_worksheet.py\n         [7.9 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n        sage -t -long -optional -randorder=87873 \"4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py\"\nTotal time for all tests: 7.9 seconds\n```\n\nFor `notebook.py`, there are other error types.",
    "created_at": "2009-08-13T06:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53604",
    "user": "mpatel"
}
```

From some testing in Firefox 3.5 on Linux, with both new patches applied:
* Live doc worksheets do not load their stylesheets.
* Published worksheets are now [partially] editable.
* The "re-publish" and "stop publishing" buttons do not work, apparently.
* The print representation of a worksheet is missing cell boundaries.

Also, a number of doctests in `notebook.py` and `worksheet.py` failed with `sage -t -long -option -verbose -randorder`.  For `worksheet.py`, there are mostly just small changes in expected HTML output.  I think some of the randomized failures are pre-existing:

```
sage -t -long -optional -randorder=87873 "4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py"
**********************************************************************
File "/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py", line 178:
    sage: sage.server.notebook.worksheet.one_prestarted_sage(None,None)
Expected:
    Sage
Got nothing
**********************************************************************
File "/home/apps/sage-4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py", line 148:
    sage: sage.server.notebook.worksheet._a_sage
Expected nothing
Got:
    Sage
**********************************************************************
2 items had failures:
   1 of   6 in __main__.example_1270084472
   1 of   5 in __main__.example_1700749147
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/apps/sage/tmp/.doctest_worksheet.py
         [7.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:
        sage -t -long -optional -randorder=87873 "4.1.1.rc1/devel/sage-main/sage/server/notebook/worksheet.py"
Total time for all tests: 7.9 seconds
```

For `notebook.py`, there are other error types.



---

archive/issue_comments_053605.json:
```json
{
    "body": "Also,\n\n```\n$ grep reviisons sage-trac-6568.*\nsage-trac-6568.2.patch:+<a class=\"listcontrol\" href=\"reviisons?rev={{ rev }}&action=publis\">Publish this one</a>&nbsp;&nbsp;\n```\n",
    "created_at": "2009-08-13T06:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53605",
    "user": "mpatel"
}
```

Also,

```
$ grep reviisons sage-trac-6568.*
sage-trac-6568.2.patch:+<a class="listcontrol" href="reviisons?rev={{ rev }}&action=publis">Publish this one</a>&nbsp;&nbsp;
```




---

archive/issue_comments_053606.json:
```json
{
    "body": "I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.\n\nI'm working on the rest of the problems now.",
    "created_at": "2009-08-13T10:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53606",
    "user": "timdumol"
}
```

I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.

I'm working on the rest of the problems now.



---

archive/issue_comments_053607.json:
```json
{
    "body": "Replying to [comment:16 timdumol]:\n> I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.\n> \n> I'm working on the rest of the problems now.\n\nI'm sorry, I meant r12658.",
    "created_at": "2009-08-13T11:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53607",
    "user": "timdumol"
}
```

Replying to [comment:16 timdumol]:
> I've checked the doctests out on a fresh install (r12659). They also fail, so I assume they're pre-existing. I'm not too familiar with the Notebook code, but I'll see if I can fix them up. Meanwhile, perhaps they should be put on a new ticket.
> 
> I'm working on the rest of the problems now.

I'm sorry, I meant r12658.



---

archive/issue_comments_053608.json:
```json
{
    "body": "Fixed several bugs. Incremental patch from sage-trac-6568.2.patch",
    "created_at": "2009-08-13T12:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53608",
    "user": "timdumol"
}
```

Fixed several bugs. Incremental patch from sage-trac-6568.2.patch



---

archive/issue_comments_053609.json:
```json
{
    "body": "Attachment\n\nFixed bug in styling of documentation pages.",
    "created_at": "2009-08-13T13:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53609",
    "user": "timdumol"
}
```

Attachment

Fixed bug in styling of documentation pages.



---

archive/issue_comments_053610.json:
```json
{
    "body": "I've fixed all the outlined bugs, and one more. The doctests all seem to pass, except for the pre-existing failures that you pointed out.",
    "created_at": "2009-08-13T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53610",
    "user": "timdumol"
}
```

I've fixed all the outlined bugs, and one more. The doctests all seem to pass, except for the pre-existing failures that you pointed out.



---

archive/issue_comments_053611.json:
```json
{
    "body": "* I think clicking \"No\" in reply to \"Do you want to publish this worksheet\" unpublishes the worksheet, but it does not return the sheet to interactive mode.\n\n  * jsMath is not included in printed worksheets.  The page itself is missing the title.\n\n  * How does the `morecss` block work?  Can we now avoid `twist.py`'s \"hack\" altogether?\n\n  * Should, e.g., `server/notebook/templates/doc.html` still be there?\n\nIf you're not already using the [Mercurial Queues extension](http://wiki.sagemath.org/MercurialQueues), it may be worth trying. `hg qrefresh` can be very helpful.\n\nI've added Jason Grout to the CC: list, since my checks may not cover the range of notebook usage patterns.  Perhaps we can get other volunteers?",
    "created_at": "2009-08-13T22:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53611",
    "user": "mpatel"
}
```

* I think clicking "No" in reply to "Do you want to publish this worksheet" unpublishes the worksheet, but it does not return the sheet to interactive mode.

  * jsMath is not included in printed worksheets.  The page itself is missing the title.

  * How does the `morecss` block work?  Can we now avoid `twist.py`'s "hack" altogether?

  * Should, e.g., `server/notebook/templates/doc.html` still be there?

If you're not already using the [Mercurial Queues extension](http://wiki.sagemath.org/MercurialQueues), it may be worth trying. `hg qrefresh` can be very helpful.

I've added Jason Grout to the CC: list, since my checks may not cover the range of notebook usage patterns.  Perhaps we can get other volunteers?



---

archive/issue_comments_053612.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-08-13T22:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53612",
    "user": "mpatel"
}
```

Changing priority from minor to major.



---

archive/issue_comments_053613.json:
```json
{
    "body": "* The `morecss` inserts the code in the block after the first css include. It should be possible to avoid it by creating another template specifically for documentation pages.\n* Probably not. I'll work on cleaning up the file tree asap.\n* I'll work on the rest of the bugs.\n\nI've actually been using histedit to combine changesets. Although I'm guessing patch queues are more idiomatic.\n\nI'm pretty new to the Sage community, so I don't know.",
    "created_at": "2009-08-14T04:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53613",
    "user": "timdumol"
}
```

* The `morecss` inserts the code in the block after the first css include. It should be possible to avoid it by creating another template specifically for documentation pages.
* Probably not. I'll work on cleaning up the file tree asap.
* I'll work on the rest of the bugs.

I've actually been using histedit to combine changesets. Although I'm guessing patch queues are more idiomatic.

I'm pretty new to the Sage community, so I don't know.



---

archive/issue_comments_053614.json:
```json
{
    "body": "The [official site](http://mercurial.selenic.com/wiki/) of Mercurial contains many tutorials on using Mercurial itself. In particular, I recommend that you go through its [tutorial for beginners](http://mercurial.selenic.com/wiki/Tutorial). After that, you might want to look through a [section](http://hgbook.red-bean.com/read/managing-change-with-mercurial-queues.html) on using Mercurial queues to manage patches. Anyway, please tell me if you have problems with using Mercurial or its queue extension.",
    "created_at": "2009-08-14T04:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53614",
    "user": "mvngu"
}
```

The [official site](http://mercurial.selenic.com/wiki/) of Mercurial contains many tutorials on using Mercurial itself. In particular, I recommend that you go through its [tutorial for beginners](http://mercurial.selenic.com/wiki/Tutorial). After that, you might want to look through a [section](http://hgbook.red-bean.com/read/managing-change-with-mercurial-queues.html) on using Mercurial queues to manage patches. Anyway, please tell me if you have problems with using Mercurial or its queue extension.



---

archive/issue_comments_053615.json:
```json
{
    "body": "Also, you might look at http://wiki.sagemath.org/MercurialQueues for a quick hands-on introduction to queues.",
    "created_at": "2009-08-14T05:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53615",
    "user": "jason"
}
```

Also, you might look at http://wiki.sagemath.org/MercurialQueues for a quick hands-on introduction to queues.



---

archive/issue_comments_053616.json:
```json
{
    "body": "Actually, I meant \"I don't know.\" as in I don't know about the possibility of finding other volunteers. I'm familiar with patch queues. Thanks for the help.",
    "created_at": "2009-08-14T08:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53616",
    "user": "timdumol"
}
```

Actually, I meant "I don't know." as in I don't know about the possibility of finding other volunteers. I'm familiar with patch queues. Thanks for the help.



---

archive/issue_comments_053617.json:
```json
{
    "body": "Attachment\n\nFixed a few bugs in templating.",
    "created_at": "2009-08-14T09:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53617",
    "user": "timdumol"
}
```

Attachment

Fixed a few bugs in templating.



---

archive/issue_comments_053618.json:
```json
{
    "body": "Attachment\n\nRemoved hack in twist.py for documentation page creation. Removed unused files.",
    "created_at": "2009-08-14T09:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53618",
    "user": "timdumol"
}
```

Attachment

Removed hack in twist.py for documentation page creation. Removed unused files.



---

archive/issue_comments_053619.json:
```json
{
    "body": "Attachment\n\nCumulative patches from sage-trac-6568.2.patch to sage-trac-6568.6.patch. Incremental patch from sage-trac-6568.1.patch.",
    "created_at": "2009-08-14T09:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53619",
    "user": "timdumol"
}
```

Attachment

Cumulative patches from sage-trac-6568.2.patch to sage-trac-6568.6.patch. Incremental patch from sage-trac-6568.1.patch.



---

archive/issue_comments_053620.json:
```json
{
    "body": "I've fixed all the bugs pointed out, and the kludge/\"hack\" was removed. I've also cleaned up the templates file tree. Thanks for noting them.",
    "created_at": "2009-08-14T10:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53620",
    "user": "timdumol"
}
```

I've fixed all the bugs pointed out, and the kludge/"hack" was removed. I've also cleaned up the templates file tree. Thanks for noting them.



---

archive/issue_comments_053621.json:
```json
{
    "body": "All-in-one.  Apply only this patch.",
    "created_at": "2009-08-15T03:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53621",
    "user": "mpatel"
}
```

All-in-one.  Apply only this patch.



---

archive/issue_comments_053622.json:
```json
{
    "body": "Attachment\n\nI've attached a solo patch comprised of Tim Dumol's six recent patches.  (I did not use the cumulative patch.)  I've ignored a few small rejected hunks from the sixth patch --- in `notebook.py`, `twist.py`, and `base.html` --- since it appears that the rejected changes are applied by an earlier patch.  Of course, all credit for the hard work of migrating the notebook to Jinja should go to Tim.\n\nI haven't tested the latest changes extensively, but I've noticed no unwelcome surprises.",
    "created_at": "2009-08-15T03:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53622",
    "user": "mpatel"
}
```

Attachment

I've attached a solo patch comprised of Tim Dumol's six recent patches.  (I did not use the cumulative patch.)  I've ignored a few small rejected hunks from the sixth patch --- in `notebook.py`, `twist.py`, and `base.html` --- since it appears that the rejected changes are applied by an earlier patch.  Of course, all credit for the hard work of migrating the notebook to Jinja should go to Tim.

I haven't tested the latest changes extensively, but I've noticed no unwelcome surprises.



---

archive/issue_comments_053623.json:
```json
{
    "body": "Fixed introspection, minor clean-ups.  Apply only this patch.",
    "created_at": "2009-08-16T13:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53623",
    "user": "mpatel"
}
```

Fixed introspection, minor clean-ups.  Apply only this patch.



---

archive/issue_comments_053624.json:
```json
{
    "body": "Attachment\n\nVersion 2 (of the uber-patch) should fix introspection.  It also\n* Simplifies `Notebook.plain_text_worksheet_html()`.\n* Indents `Notebook.html_debug_window()`'s docstring.\n\nThere's still some HTML generation in\n* `Notebook.object_list_html()`, `Notebook.list_window_javascript()`, `Notebook.html_settings()`.\n* `Worksheet.html_ratings_into()`\nbut these methods are unused or minor.  Of course, there's markup in `interact.py`, etc.\n\nShould we make a separate ticket for moving `css.py`'s stylesheets to `templates/`?  Rebasing other tickets against this one may be easier than the opposite.\n\nMy review is positive, though someone else should check the most recent changes.  It would be useful to get feedback from other testers.",
    "created_at": "2009-08-16T14:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53624",
    "user": "mpatel"
}
```

Attachment

Version 2 (of the uber-patch) should fix introspection.  It also
* Simplifies `Notebook.plain_text_worksheet_html()`.
* Indents `Notebook.html_debug_window()`'s docstring.

There's still some HTML generation in
* `Notebook.object_list_html()`, `Notebook.list_window_javascript()`, `Notebook.html_settings()`.
* `Worksheet.html_ratings_into()`
but these methods are unused or minor.  Of course, there's markup in `interact.py`, etc.

Should we make a separate ticket for moving `css.py`'s stylesheets to `templates/`?  Rebasing other tickets against this one may be easier than the opposite.

My review is positive, though someone else should check the most recent changes.  It would be useful to get feedback from other testers.



---

archive/issue_comments_053625.json:
```json
{
    "body": "The patch seems quite large enough as is without including the sheets from `css.py`. I think another ticket would be more suitable.\n\nActually, I hope to clean the HTML up and replace the table layout with CSS once this gets committed, so it may be nice to put those changes into a new ticket as well.",
    "created_at": "2009-08-16T16:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53625",
    "user": "timdumol"
}
```

The patch seems quite large enough as is without including the sheets from `css.py`. I think another ticket would be more suitable.

Actually, I hope to clean the HTML up and replace the table layout with CSS once this gets committed, so it may be nice to put those changes into a new ticket as well.



---

archive/issue_comments_053626.json:
```json
{
    "body": "Sounds great.  I'll steer clear.  In the near term, I'll try to simplify the jsMath-related code for #4714, along the lines of #6673.\n\nI should add that v2 of the uni-patch also fixes the \"User Management\" page at, e.g., `http://localhost:8000/users` (for admins).  The problem was a misuse of `template.template()` in `twist.py`.",
    "created_at": "2009-08-17T06:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53626",
    "user": "mpatel"
}
```

Sounds great.  I'll steer clear.  In the near term, I'll try to simplify the jsMath-related code for #4714, along the lines of #6673.

I should add that v2 of the uni-patch also fixes the "User Management" page at, e.g., `http://localhost:8000/users` (for admins).  The problem was a misuse of `template.template()` in `twist.py`.



---

archive/issue_comments_053627.json:
```json
{
    "body": "REFEREE REPORT:\n\nThe Sphinx docstrings that you added, which are very good, have a formatting problem, namely below there needs to be a newline before each - (i.e., lots of whitespace):\n\n```\n \t1315\t        INPUT: \n \t1316\t        - ``username`` - a string \n \t1317\t        - ``worksheet`` - an instance of Worksheet \n \t1318\t \n \t1319\t        OUTPUT: \n \t1320\t        - a string containing the HTML \n```\n\nSee this screenshot: http://wstein.org/home/wstein/tmp/jinja1.png which illustrates how the ReST is messed up.  This isn't a big deal, since I don't think this code is even in the reference manual yet...  But it would be good to go through and fix. \n\nAll doctests pass, and *using* the notebook after applying the patches seems to work fine -- I can't find any visible difference. \n\nI give this a positive review.  Proper Sphinxing of docs can go in a future patch, and be done throughout the notebook server code.",
    "created_at": "2009-08-29T05:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53627",
    "user": "was"
}
```

REFEREE REPORT:

The Sphinx docstrings that you added, which are very good, have a formatting problem, namely below there needs to be a newline before each - (i.e., lots of whitespace):

```
 	1315	        INPUT: 
 	1316	        - ``username`` - a string 
 	1317	        - ``worksheet`` - an instance of Worksheet 
 	1318	 
 	1319	        OUTPUT: 
 	1320	        - a string containing the HTML 
```

See this screenshot: http://wstein.org/home/wstein/tmp/jinja1.png which illustrates how the ReST is messed up.  This isn't a big deal, since I don't think this code is even in the reference manual yet...  But it would be good to go through and fix. 

All doctests pass, and *using* the notebook after applying the patches seems to work fine -- I can't find any visible difference. 

I give this a positive review.  Proper Sphinxing of docs can go in a future patch, and be done throughout the notebook server code.



---

archive/issue_comments_053628.json:
```json
{
    "body": "I've created a new ticket for notebook documentation at #6840. The docstrings fixes are there.",
    "created_at": "2009-08-29T07:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53628",
    "user": "timdumol"
}
```

I've created a new ticket for notebook documentation at #6840. The docstrings fixes are there.



---

archive/issue_comments_053629.json:
```json
{
    "body": "In part, the patch \"v2\" at #5360 is an attempt to include some `server/` docstrings in the reference manual.",
    "created_at": "2009-08-30T10:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53629",
    "user": "mpatel"
}
```

In part, the patch "v2" at #5360 is an attempt to include some `server/` docstrings in the reference manual.



---

archive/issue_comments_053630.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T11:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53630",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053631.json:
```json
{
    "body": "The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:14: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:19: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:8: (WARNING/2) Literal block expected; none found.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.DIR:1: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:17: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:17: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:25: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py:docstring of sage.server.notebook.worksheet.Worksheet.html_menu:10: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n\nWhen I ran the test suite with the patch, I received a timed out error:\n\n```\nsage -t -long devel/sage-main/sage/interfaces/ecm.py\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n\t [1800.1 s]\n```\n\nThis error has nothing to do with the patch. It might be due to sage.math being too busy or its system resources (probably RAM) nearing capacity. Merged `trac_6568-jinja_migration_v2.patch`.",
    "created_at": "2009-08-30T11:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53631",
    "user": "mvngu"
}
```

The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:14: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_beforepublish_window:19: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:8: (WARNING/2) Literal block expected; none found.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.DIR:1: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_debug_window:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_doc:17: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:17: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_download_or_delete_datafile:25: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_plain_text_window:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_share:24: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_upload_data_window:18: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_revision_list:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:13: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.html_worksheet_settings:20: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:16: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/notebook.py:docstring of sage.server.notebook.notebook.Notebook.worksheet_html:23: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py:docstring of sage.server.notebook.worksheet.Worksheet.html_menu:10: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```

When I ran the test suite with the patch, I received a timed out error:

```
sage -t -long devel/sage-main/sage/interfaces/ecm.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [1800.1 s]
```

This error has nothing to do with the patch. It might be due to sage.math being too busy or its system resources (probably RAM) nearing capacity. Merged `trac_6568-jinja_migration_v2.patch`.



---

archive/issue_comments_053632.json:
```json
{
    "body": "Replying to [comment:33 mvngu]:\n> The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:\nI think #6840 will take care of these.",
    "created_at": "2009-08-30T18:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53632",
    "user": "mpatel"
}
```

Replying to [comment:33 mvngu]:
> The patch `trac_6568-jinja_migration_v2.patch` results in over 20 warnings when building the reference manual:
I think #6840 will take care of these.



---

archive/issue_comments_053633.json:
```json
{
    "body": "Attachment\n\nThe patch `trac_6568-manifest.patch` prevents repository corruption. A repository corruption can happen because `trac_6568-jinja_migration_v2.patch` adds two new directories:\n\n1. `sage/server/notebook/templates/notebook/`\n2. `sage/server/notebook/templates/worksheet/`\n\nIf the file `SAGE_ROOT/devel/sage-main/MANIFEST.in` is not patched to handle files under these new directories, those files won't be picked up when making a source release with `sage -sdist`.",
    "created_at": "2009-09-07T11:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53633",
    "user": "mvngu"
}
```

Attachment

The patch `trac_6568-manifest.patch` prevents repository corruption. A repository corruption can happen because `trac_6568-jinja_migration_v2.patch` adds two new directories:

1. `sage/server/notebook/templates/notebook/`
2. `sage/server/notebook/templates/worksheet/`

If the file `SAGE_ROOT/devel/sage-main/MANIFEST.in` is not patched to handle files under these new directories, those files won't be picked up when making a source release with `sage -sdist`.



---

archive/issue_comments_053634.json:
```json
{
    "body": "The \"manifest\" patch should fix #6884.  If so, please close that ticket.",
    "created_at": "2009-09-07T11:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53634",
    "user": "mpatel"
}
```

The "manifest" patch should fix #6884.  If so, please close that ticket.



---

archive/issue_comments_053635.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6568-jinja_migration_v2.patch`\n2. `trac_6568-manifest.patch`",
    "created_at": "2009-09-07T16:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6568#issuecomment-53635",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6568-jinja_migration_v2.patch`
2. `trac_6568-manifest.patch`
