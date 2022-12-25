# Issue 5143: shift-enter should save and exit tinyMCE

archive/issues_005143.json:
```json
{
    "body": "Assignee: boothby\n\nThis would be more consistent with calculation cells.\n\nReferences for developement:\n\nIt looks like we might be able to do this with the current key handler attaching an event to the tinymce instance that calls the triggerSave tinyMCE trigger: http://wiki.moxiecode.com/index.php/TinyMCE:Functions#tinyMCE.triggerSave\n\nAlso, see the bottom of the following page for a way to get tinyMCE to associate an event with a keypress:\nhttp://tinymce.moxiecode.com/punbb/viewtopic.php?id=1321\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5143\n\n",
    "created_at": "2009-01-30T23:11:30Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "shift-enter should save and exit tinyMCE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5143",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

This would be more consistent with calculation cells.

References for developement:

It looks like we might be able to do this with the current key handler attaching an event to the tinymce instance that calls the triggerSave tinyMCE trigger: http://wiki.moxiecode.com/index.php/TinyMCE:Functions#tinyMCE.triggerSave

Also, see the bottom of the following page for a way to get tinyMCE to associate an event with a keypress:
http://tinymce.moxiecode.com/punbb/viewtopic.php?id=1321



Issue created by migration from https://trac.sagemath.org/ticket/5143





---

archive/issue_comments_039268.json:
```json
{
    "body": "See also: http://wiki.moxiecode.com/index.php/TinyMCE:API/tinymce.Editor/onKeyDown",
    "created_at": "2009-01-30T23:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39268",
    "user": "https://github.com/jasongrout"
}
```

See also: http://wiki.moxiecode.com/index.php/TinyMCE:API/tinymce.Editor/onKeyDown



---

archive/issue_comments_039269.json:
```json
{
    "body": "Attachment [trac_5143-tinymce-shift-enter.patch](tarball://root/attachments/some-uuid/ticket5143/trac_5143-tinymce-shift-enter.patch) by @jasongrout created at 2009-02-03 08:15:04",
    "created_at": "2009-02-03T08:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39269",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5143-tinymce-shift-enter.patch](tarball://root/attachments/some-uuid/ticket5143/trac_5143-tinymce-shift-enter.patch) by @jasongrout created at 2009-02-03 08:15:04



---

archive/issue_comments_039270.json:
```json
{
    "body": "This patch also adds font formatting buttons that have been requested by several people.",
    "created_at": "2009-02-03T08:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39270",
    "user": "https://github.com/jasongrout"
}
```

This patch also adds font formatting buttons that have been requested by several people.



---

archive/issue_comments_039271.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-03T08:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39271",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039272.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T09:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39272",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039273.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-02-03T09:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39273",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_039274.json:
```json
{
    "body": "Tested in FF3 & Safari on Mac.",
    "created_at": "2009-02-04T01:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39274",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Tested in FF3 & Safari on Mac.



---

archive/issue_comments_039275.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T01:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039276.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T01:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005393.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-04T01:17:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5143#event-5393"
}
```
