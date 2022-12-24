# Issue 2612: String to Integer Conversion

archive/issues_002612.json:
```json
{
    "body": "Assignee: somebody\n\nSince python does well with a leading sign (+ or -)\n\n```\nsage: int('+1')\n1\nsage: int('-1')\n-1\n```\n\nthe sage Integers should do the same.\n\n```\nsage: Integer('-1')\n-1\nsage: Integer('+1')\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/mrk/<ipython console> in <module>()\n\n/home/mrk/integer.pyx in sage.rings.integer.Integer.__init__()\n\n<type 'exceptions.TypeError'>: unable to convert x (=+1) to an integer\n```\n\nSo the case of a leading \"+\" must be fixed\n\nIssue created by migration from https://trac.sagemath.org/ticket/2612\n\n",
    "created_at": "2008-03-20T12:40:51Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "String to Integer Conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2612",
    "user": "vgermrk"
}
```
Assignee: somebody

Since python does well with a leading sign (+ or -)

```
sage: int('+1')
1
sage: int('-1')
-1
```

the sage Integers should do the same.

```
sage: Integer('-1')
-1
sage: Integer('+1')
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mrk/<ipython console> in <module>()

/home/mrk/integer.pyx in sage.rings.integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to convert x (=+1) to an integer
```

So the case of a leading "+" must be fixed

Issue created by migration from https://trac.sagemath.org/ticket/2612





---

archive/issue_comments_017926.json:
```json
{
    "body": "Attachment [2612-integer_plus.patch](tarball://root/attachments/some-uuid/ticket2612/2612-integer_plus.patch) by robertwb created at 2008-03-26 06:16:58",
    "created_at": "2008-03-26T06:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2612#issuecomment-17926",
    "user": "robertwb"
}
```

Attachment [2612-integer_plus.patch](tarball://root/attachments/some-uuid/ticket2612/2612-integer_plus.patch) by robertwb created at 2008-03-26 06:16:58



---

archive/issue_comments_017927.json:
```json
{
    "body": "Looks good: fixes the bug, doesn't break anything else.",
    "created_at": "2008-03-27T22:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2612#issuecomment-17927",
    "user": "AlexGhitza"
}
```

Looks good: fixes the bug, doesn't break anything else.



---

archive/issue_comments_017928.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2. I had to merge the first hunk of 2612-integer_plus.patch manually due to trivial merge conflicts.",
    "created_at": "2008-03-28T08:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2612#issuecomment-17928",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2. I had to merge the first hunk of 2612-integer_plus.patch manually due to trivial merge conflicts.



---

archive/issue_comments_017929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T08:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2612#issuecomment-17929",
    "user": "mabshoff"
}
```

Resolution: fixed
