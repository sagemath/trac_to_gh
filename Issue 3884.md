# Issue 3884: change banner in "sage -advanced"

archive/issues_003884.json:
```json
{
    "body": "Assignee: cwitty\n\nFrom Ralf Hemmecke:\n\n\n```\nwoodpecker:~/scratch/SAGE>./sage -advanced\n-----------------------------------------------------------\n-----------------------------------------------------------\n| SAGE: Software for Algebra and Geometry Experimentation |\nDidn't I hear you saying at ISSAC that SAGE is no longer an abbreviation?\n```\n\n\nIt should be the normal Sage banner. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3884\n\n",
    "created_at": "2008-08-17T19:40:27Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "change banner in \"sage -advanced\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3884",
    "user": "was"
}
```
Assignee: cwitty

From Ralf Hemmecke:


```
woodpecker:~/scratch/SAGE>./sage -advanced
-----------------------------------------------------------
-----------------------------------------------------------
| SAGE: Software for Algebra and Geometry Experimentation |
Didn't I hear you saying at ISSAC that SAGE is no longer an abbreviation?
```


It should be the normal Sage banner. 

Issue created by migration from https://trac.sagemath.org/ticket/3884





---

archive/issue_comments_027711.json:
```json
{
    "body": "Attachment [trac_3884.patch](tarball://root/attachments/some-uuid/ticket3884/trac_3884.patch) by mabshoff created at 2008-08-22 22:14:26\n\nThis patch changes the banner printed to something very similar at the startup of Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T22:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27711",
    "user": "mabshoff"
}
```

Attachment [trac_3884.patch](tarball://root/attachments/some-uuid/ticket3884/trac_3884.patch) by mabshoff created at 2008-08-22 22:14:26

This patch changes the banner printed to something very similar at the startup of Sage.

Cheers,

Michael



---

archive/issue_comments_027712.json:
```json
{
    "body": "With the patch applied we now get:\n{{\nmabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n Optional arguments:\n<SNIP>\n}}}\n| SAGE Version 3.1.1, Release Date: 2008-08-17                       |\nCheers,\n\nMichael",
    "created_at": "2008-08-22T23:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27712",
    "user": "mabshoff"
}
```

With the patch applied we now get:
{{
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
}}}
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
Cheers,

Michael



---

archive/issue_comments_027713.json:
```json
{
    "body": "With the patch we now get (better formatting):\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n Optional arguments:\n<SNIP>\n```\n",
    "created_at": "2008-08-22T23:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27713",
    "user": "mabshoff"
}
```

With the patch we now get (better formatting):

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.1$ ./sage -h
----------------------------------------------------------------------
----------------------------------------------------------------------
 Optional arguments:
<SNIP>
```




---

archive/issue_comments_027714.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-23T00:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27714",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_comments_027715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T00:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3884#issuecomment-27715",
    "user": "mabshoff"
}
```

Resolution: fixed
