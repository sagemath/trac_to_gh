# Issue 2820: notebook -- turn off the jsmath warning

archive/issues_002820.json:
```json
{
    "body": "Assignee: boothby\n\nI think the plan should be \n1. get rid of it; \n2. make much better jsmath instructions;\n3. put something like it back (that doesn't suck)\n\nAlso, we could support official jsmath image fonts (150MB) as an optional package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2820\n\n",
    "created_at": "2008-04-06T04:02:16Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- turn off the jsmath warning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2820",
    "user": "was"
}
```
Assignee: boothby

I think the plan should be 
1. get rid of it; 
2. make much better jsmath instructions;
3. put something like it back (that doesn't suck)

Also, we could support official jsmath image fonts (150MB) as an optional package.

Issue created by migration from https://trac.sagemath.org/ticket/2820





---

archive/issue_comments_019359.json:
```json
{
    "body": "The jsmath image fonts are already an optional package.  See #1971.",
    "created_at": "2008-04-06T04:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19359",
    "user": "jason"
}
```

The jsmath image fonts are already an optional package.  See #1971.



---

archive/issue_comments_019360.json:
```json
{
    "body": "The attached patch does the following:\n* turns off the jsmath warning\n* greatly improves how the input text area gets autoresized\n* fixes all cursor/tab location bugs from #2840\n* makes some small cosmetic changes to finish #2852\n* restores backspace in empty cell to delete functionality (to avoid confusion)\n* turns on javascript compression so main.js is 1/3rd the size, which means loading sage worksheets will be faster. \n* get rid of lisp from the list-of-systems menu, since it doesn't work.",
    "created_at": "2008-04-08T17:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19360",
    "user": "was"
}
```

The attached patch does the following:
* turns off the jsmath warning
* greatly improves how the input text area gets autoresized
* fixes all cursor/tab location bugs from #2840
* makes some small cosmetic changes to finish #2852
* restores backspace in empty cell to delete functionality (to avoid confusion)
* turns on javascript compression so main.js is 1/3rd the size, which means loading sage worksheets will be faster. 
* get rid of lisp from the list-of-systems menu, since it doesn't work.



---

archive/issue_comments_019361.json:
```json
{
    "body": "Attachment [sage-2820.patch](tarball://root/attachments/some-uuid/ticket2820/sage-2820.patch) by mabshoff created at 2008-04-08 17:14:32\n\nThis patch also fixes #2800.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T17:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19361",
    "user": "mabshoff"
}
```

Attachment [sage-2820.patch](tarball://root/attachments/some-uuid/ticket2820/sage-2820.patch) by mabshoff created at 2008-04-08 17:14:32

This patch also fixes #2800.

Cheers,

Michael



---

archive/issue_comments_019362.json:
```json
{
    "body": "Works for me.",
    "created_at": "2008-04-08T18:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19362",
    "user": "boothby"
}
```

Works for me.



---

archive/issue_comments_019363.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-08T18:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19363",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019364.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T18:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2820",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2820#issuecomment-19364",
    "user": "mabshoff"
}
```

Resolution: fixed
