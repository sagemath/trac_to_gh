# Issue 9683: pretty_print clobbers _ (history)

archive/issues_009683.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mwhansen\n\nKeywords: pretty_print, history\n\nAfter using `pretty_print`, the first history variable (`_`) no longer updates.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: combinat\nsage: 17\n17\nsage: _\n17\nsage: 23\n23\nsage: _\n23\nsage: pretty_print(17)\n<html><span class=\"math\">\\newcommand{\\Bold}[1]{\\mathbf{#1}}17</span></html>\nsage: _\n17\nsage: 23\n23\nsage: _\n17\n```\n\n| Sage Version 4.5.1, Release Date: 2010-07-19                       |\n| Type notebook() for the GUI, and license() for information.        |\nThe relevant function seems to be `pretty_print` in `/sage/misc/latex.py`, but I don't know the right way to fix it. The function and `pretty_print_default` in same file, and the functions `displayhook` and `install` in `/sage/misc/displayhook.py` may also be relevant.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9683\n\n",
    "created_at": "2010-08-04T05:05:14Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "pretty_print clobbers _ (history)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9683",
    "user": "https://github.com/mguaypaq"
}
```
Assignee: @williamstein

CC:  @mwhansen

Keywords: pretty_print, history

After using `pretty_print`, the first history variable (`_`) no longer updates.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: 17
17
sage: _
17
sage: 23
23
sage: _
23
sage: pretty_print(17)
<html><span class="math">\newcommand{\Bold}[1]{\mathbf{#1}}17</span></html>
sage: _
17
sage: 23
23
sage: _
17
```

| Sage Version 4.5.1, Release Date: 2010-07-19                       |
| Type notebook() for the GUI, and license() for information.        |
The relevant function seems to be `pretty_print` in `/sage/misc/latex.py`, but I don't know the right way to fix it. The function and `pretty_print_default` in same file, and the functions `displayhook` and `install` in `/sage/misc/displayhook.py` may also be relevant.


Issue created by migration from https://trac.sagemath.org/ticket/9683





---

archive/issue_comments_093974.json:
```json
{
    "body": "In the  ipython `displayhook` it checks to see if underscore was set explicitly and if so, it stops tracking.  We are setting it explicitly in `pretty_print`.  Maybe if we just stop doing this it will work.  Also we probably need to fix `pretty_print_default` to set it to the ipython `displayhook` instead of the default one.\n\n\n```\n    def check_for_underscore(self):\n        \"\"\"Check if the user has set the '_' variable by hand.\"\"\"\n        # If something injected a '_' variable in __builtin__, delete\n        # ipython's automatic one so we don't clobber that.  gettext() in\n        # particular uses _, so we need to stay away from it.\n        if '_' in __builtin__.__dict__:\n            try:\n                del self.shell.user_ns['_']\n            except KeyError:\n                pass\n```\n",
    "created_at": "2012-11-25T21:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93974",
    "user": "https://github.com/gvol"
}
```

In the  ipython `displayhook` it checks to see if underscore was set explicitly and if so, it stops tracking.  We are setting it explicitly in `pretty_print`.  Maybe if we just stop doing this it will work.  Also we probably need to fix `pretty_print_default` to set it to the ipython `displayhook` instead of the default one.


```
    def check_for_underscore(self):
        """Check if the user has set the '_' variable by hand."""
        # If something injected a '_' variable in __builtin__, delete
        # ipython's automatic one so we don't clobber that.  gettext() in
        # particular uses _, so we need to stay away from it.
        if '_' in __builtin__.__dict__:
            try:
                del self.shell.user_ns['_']
            except KeyError:
                pass
```




---

archive/issue_comments_093975.json:
```json
{
    "body": "Attachment [trac_9683.patch](tarball://root/attachments/some-uuid/ticket9683/trac_9683.patch) by @mwhansen created at 2013-07-24 16:09:34\n\nI've posted a patch.  It doesn't have a test for this problem. I could make one, but it's slightly annoying since you have to do everything indirectly through an IPython shell object.",
    "created_at": "2013-07-24T16:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93975",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_9683.patch](tarball://root/attachments/some-uuid/ticket9683/trac_9683.patch) by @mwhansen created at 2013-07-24 16:09:34

I've posted a patch.  It doesn't have a test for this problem. I could make one, but it's slightly annoying since you have to do everything indirectly through an IPython shell object.



---

archive/issue_comments_093976.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-24T16:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93976",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093977.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-04-10T21:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93977",
    "user": "https://github.com/vbraun"
}
```

New commits:



---

archive/issue_comments_093978.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-10T21:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93978",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093979.json:
```json
{
    "body": "Changing keywords from \"pretty_print, history\" to \"pretty_print, history, days57\".",
    "created_at": "2014-04-10T21:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93979",
    "user": "https://github.com/vbraun"
}
```

Changing keywords from "pretty_print, history" to "pretty_print, history, days57".



---

archive/issue_events_009815.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-04-13T19:33:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9683#event-9815"
}
```



---

archive/issue_comments_093980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-04-13T19:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9683",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9683#issuecomment-93980",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
