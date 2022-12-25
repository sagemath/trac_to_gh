# Issue 6170: automate applying patches from a ticket and testing them

archive/issues_006170.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @ncalexan\n\nAutomate the process of \n\n1. take a subset of patch from a ticket\n\n2. merge\n\n3. Run \"sage -br\"\n\n4. Run \"make ptest\"\n\nand much more.  \n\n\nThis could look like the following, though the first patch to this ticket should be much less ambitious and just do *something* useful.\n\n```\nsage: hg_devel.test(6738)\n\n[[applying patches on trac ticket 6738 to the correct repos...]]\n\n[[starting new sage process in os.system and doing \"sage -br\"]]\n\n[[report any failures]]\n\n[[run make ptestlong and report results]]\n\n[[revert state of sage to exactly what it was before stuff applied]]\n\nsage: hg_devel.apply(6738)\n\n[[apply everything from ticket 6738 to all relevant repos -- basically hg_devel.test without running tests, and without undoing at the end;  would also place all relevant downloaded patches in a directory -- this is what Michael always did manually with the patches/ directory]]\n\nsage: hg_devel.needs_review()\n\n[[would query trac and make a list of all tickets that are [with patch; needs review], and would return a list of the ticket numbers.]]\n\nsage: hg_devel.positive_review()\n\n[[would query trac and make a list of all tickets that are [with patch; positive review], and would return a list of the ticket numbers.]]\n\nsage: hg_devel.test_positive_review()\n\n[[would try hg_devel.test(...) on every ticket with positive review and make a nice html (and/or text) based report summarizing what happened]]\n\n\nsage: hg_devel.test_needs_review()\n\n[[would try hg_devel.test(...) on every ticket that needs review and make a nice html (and/or text) based report summarizing what happened.   This could probably quickly indicate that half the tickets \"needs review\" are broken or need a rebase -- it could easily take several hours to run.  This would be incredibly valuable, imho.]]\n\n\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6170\n\n",
    "created_at": "2009-05-31T08:12:37Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "automate applying patches from a ticket and testing them",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6170",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  @ncalexan

Automate the process of 

1. take a subset of patch from a ticket

2. merge

3. Run "sage -br"

4. Run "make ptest"

and much more.  


This could look like the following, though the first patch to this ticket should be much less ambitious and just do *something* useful.

```
sage: hg_devel.test(6738)

[[applying patches on trac ticket 6738 to the correct repos...]]

[[starting new sage process in os.system and doing "sage -br"]]

[[report any failures]]

[[run make ptestlong and report results]]

[[revert state of sage to exactly what it was before stuff applied]]

sage: hg_devel.apply(6738)

[[apply everything from ticket 6738 to all relevant repos -- basically hg_devel.test without running tests, and without undoing at the end;  would also place all relevant downloaded patches in a directory -- this is what Michael always did manually with the patches/ directory]]

sage: hg_devel.needs_review()

[[would query trac and make a list of all tickets that are [with patch; needs review], and would return a list of the ticket numbers.]]

sage: hg_devel.positive_review()

[[would query trac and make a list of all tickets that are [with patch; positive review], and would return a list of the ticket numbers.]]

sage: hg_devel.test_positive_review()

[[would try hg_devel.test(...) on every ticket with positive review and make a nice html (and/or text) based report summarizing what happened]]


sage: hg_devel.test_needs_review()

[[would try hg_devel.test(...) on every ticket that needs review and make a nice html (and/or text) based report summarizing what happened.   This could probably quickly indicate that half the tickets "needs review" are broken or need a rebase -- it could easily take several hours to run.  This would be incredibly valuable, imho.]]



```



Issue created by migration from https://trac.sagemath.org/ticket/6170





---

archive/issue_comments_049122.json:
```json
{
    "body": "Attachment [trac-6170-bin.patch](tarball://root/attachments/some-uuid/ticket6170/trac-6170-bin.patch) by @craigcitro created at 2009-06-18 08:46:05\n\napply to $SAGE_LOCAL/bin",
    "created_at": "2009-06-18T08:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49122",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6170-bin.patch](tarball://root/attachments/some-uuid/ticket6170/trac-6170-bin.patch) by @craigcitro created at 2009-06-18 08:46:05

apply to $SAGE_LOCAL/bin



---

archive/issue_comments_049123.json:
```json
{
    "body": "Attachment [trac-6170-bin-pt2.patch](tarball://root/attachments/some-uuid/ticket6170/trac-6170-bin-pt2.patch) by @craigcitro created at 2009-06-18 23:54:48",
    "created_at": "2009-06-18T23:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49123",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6170-bin-pt2.patch](tarball://root/attachments/some-uuid/ticket6170/trac-6170-bin-pt2.patch) by @craigcitro created at 2009-06-18 23:54:48



---

archive/issue_comments_049124.json:
```json
{
    "body": "I've added a second patch that does a bit of error checking with the `$EDITOR` variable.",
    "created_at": "2009-06-18T23:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49124",
    "user": "https://github.com/craigcitro"
}
```

I've added a second patch that does a bit of error checking with the `$EDITOR` variable.



---

archive/issue_comments_049125.json:
```json
{
    "body": "First cut looks good!",
    "created_at": "2009-06-19T06:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49125",
    "user": "https://github.com/ncalexan"
}
```

First cut looks good!



---

archive/issue_comments_049126.json:
```json
{
    "body": "Merged first patch in `rc3`, second in final release.",
    "created_at": "2009-06-19T06:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49126",
    "user": "https://github.com/craigcitro"
}
```

Merged first patch in `rc3`, second in final release.



---

archive/issue_comments_049127.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-19T06:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6170#issuecomment-49127",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_events_006419.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-19T06:44:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6170",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6170#event-6419"
}
```
