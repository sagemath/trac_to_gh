# Issue 5143: shift-enter should save and exit tinyMCE

archive/issues_005143.json:
```json
{
    "body": "Assignee: boothby\n\nThis would be more consistent with calculation cells.\n\nReferences for developement:\n\nIt looks like we might be able to do this with the current key handler attaching an event to the tinymce instance that calls the triggerSave tinyMCE trigger: http://wiki.moxiecode.com/index.php/TinyMCE:Functions#tinyMCE.triggerSave\n\nAlso, see the bottom of the following page for a way to get tinyMCE to associate an event with a keypress:\nhttp://tinymce.moxiecode.com/punbb/viewtopic.php?id=1321\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5143\n\n",
    "created_at": "2009-01-30T23:11:30Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "shift-enter should save and exit tinyMCE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5143",
    "user": "jason"
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

archive/issue_comments_039344.json:
```json
{
    "body": "See also: http://wiki.moxiecode.com/index.php/TinyMCE:API/tinymce.Editor/onKeyDown",
    "created_at": "2009-01-30T23:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39344",
    "user": "jason"
}
```

See also: http://wiki.moxiecode.com/index.php/TinyMCE:API/tinymce.Editor/onKeyDown



---

archive/issue_comments_039345.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-03T08:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39345",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_039346.json:
```json
{
    "body": "This patch also adds font formatting buttons that have been requested by several people.",
    "created_at": "2009-02-03T08:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39346",
    "user": "jason"
}
```

This patch also adds font formatting buttons that have been requested by several people.



---

archive/issue_comments_039347.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-03T08:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39347",
    "user": "jason"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039348.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T09:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39348",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039349.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-02-03T09:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39349",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_039350.json:
```json
{
    "body": "Tested in FF3 & Safari on Mac.",
    "created_at": "2009-02-04T01:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39350",
    "user": "TimothyClemans"
}
```

Tested in FF3 & Safari on Mac.



---

archive/issue_comments_039351.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-04T01:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39351",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_comments_039352.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-04T01:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5143#issuecomment-39352",
    "user": "mabshoff"
}
```

Resolution: fixed
