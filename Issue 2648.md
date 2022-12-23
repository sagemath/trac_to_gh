# Issue 2648: bug in octave version

archive/issues_002648.json:
```json
{
    "body": "Assignee: was\n\n\n```\nThe octave.version() command is returning '.1.73' when it should\nalmost certainly be returning '2.1.73'\n\nThis has been verified on three systems:\n-- Sage 2.10.1 running in the Windows VM\n-- Sage 2.10.3 running in the Windows VM\n-- sagenb.org\n\nIf this is in fact a bug, I wonder if it is a bug in this command\nalone or a more general bug having to do with returning strings from\nOctave\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1, Release Date: 2008-02-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: octave.min([1,2,3])\n 1\nsage: octave.version()\n'.1.73'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2648\n\n",
    "created_at": "2008-03-22T18:10:02Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "bug in octave version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2648",
    "user": "was"
}
```
Assignee: was


```
The octave.version() command is returning '.1.73' when it should
almost certainly be returning '2.1.73'

This has been verified on three systems:
-- Sage 2.10.1 running in the Windows VM
-- Sage 2.10.3 running in the Windows VM
-- sagenb.org

If this is in fact a bug, I wonder if it is a bug in this command
alone or a more general bug having to do with returning strings from
Octave

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: octave.min([1,2,3])
 1
sage: octave.version()
'.1.73'
```


Issue created by migration from https://trac.sagemath.org/ticket/2648





---

archive/issue_comments_018205.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-22T18:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2648#issuecomment-18205",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_018206.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-22T18:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2648#issuecomment-18206",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018207.json:
```json
{
    "body": "Patch looks good to me. Positive review.",
    "created_at": "2008-03-22T19:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2648#issuecomment-18207",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.



---

archive/issue_comments_018208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T19:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2648#issuecomment-18208",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018209.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T19:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2648#issuecomment-18209",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1
