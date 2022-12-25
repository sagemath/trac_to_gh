# Issue 4851: infinite recursion with encoding entities for worksheet titles with apostrophes, etc

archive/issues_004851.json:
```json
{
    "body": "Assignee: boothby\n\nThe title seems complicated but the problem is easy to see: if one creates a worksheet with an apostrophe in the title, like this:\n\n```\nI'm an apostrophe\n```\n\nthen saves, quits, and reloads the worksheet, the title is now:\n\n```\nI&apos;m an apostrophe\n```\n\nIf you quit and reload the worksheet, the title becomes:\n\n```\nI&amp;apos;m an apostrophe\n```\n\n...and so on. The ampersand is replaced by \"`&amp;`\", and then THAT ampersand gets replaced by...and so on. The problem seems to happen with any HTML entity. I'm seeing this with 3.2.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4851\n\n",
    "created_at": "2008-12-22T07:34:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "infinite recursion with encoding entities for worksheet titles with apostrophes, etc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4851",
    "user": "https://github.com/dandrake"
}
```
Assignee: boothby

The title seems complicated but the problem is easy to see: if one creates a worksheet with an apostrophe in the title, like this:

```
I'm an apostrophe
```

then saves, quits, and reloads the worksheet, the title is now:

```
I&apos;m an apostrophe
```

If you quit and reload the worksheet, the title becomes:

```
I&amp;apos;m an apostrophe
```

...and so on. The ampersand is replaced by "`&amp;`", and then THAT ampersand gets replaced by...and so on. The problem seems to happen with any HTML entity. I'm seeing this with 3.2.2.

Issue created by migration from https://trac.sagemath.org/ticket/4851





---

archive/issue_comments_036708.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-19T08:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4851#issuecomment-36708",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_036709.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-19T08:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4851#issuecomment-36709",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036710.json:
```json
{
    "body": "Attachment [trac_4851.patch](tarball://root/attachments/some-uuid/ticket4851/trac_4851.patch) by @dandrake created at 2009-01-19 08:34:25\n\nThe code looks good, and the reported problem is fixed. I give this a positive review provided that a doctest gets added, or a test in the Selenium test suite is added.",
    "created_at": "2009-01-19T08:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4851#issuecomment-36710",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_4851.patch](tarball://root/attachments/some-uuid/ticket4851/trac_4851.patch) by @dandrake created at 2009-01-19 08:34:25

The code looks good, and the reported problem is fixed. I give this a positive review provided that a doctest gets added, or a test in the Selenium test suite is added.



---

archive/issue_events_005096.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-19T09:51:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4851#event-5096"
}
```



---

archive/issue_comments_036711.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T09:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4851#issuecomment-36711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_036712.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T09:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4851#issuecomment-36712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
