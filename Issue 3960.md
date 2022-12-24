# Issue 3960: "edit this" on published worksheets doesn't work anymore in 3.1.1

archive/issues_003960.json:
```json
{
    "body": "Assignee: boothby\n\nWay to reproduce:\n\n- start notebook\n- create worksheet\n- publish worksheet\n- go to \"published worksheets\"\n- click published worksheet\n\nresult:\n\n\"edit this\" or \"edit a copy\" link lead to another \"published\" version, not a normal worksheet\n\nexpected result:\n\nan editable worksheet\n\nNOTE: This worked properly in 3.0.6\n\nIssue created by migration from https://trac.sagemath.org/ticket/3960\n\n",
    "created_at": "2008-08-26T18:27:26Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "title": "\"edit this\" on published worksheets doesn't work anymore in 3.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3960",
    "user": "nbruin"
}
```
Assignee: boothby

Way to reproduce:

- start notebook
- create worksheet
- publish worksheet
- go to "published worksheets"
- click published worksheet

result:

"edit this" or "edit a copy" link lead to another "published" version, not a normal worksheet

expected result:

an editable worksheet

NOTE: This worked properly in 3.0.6

Issue created by migration from https://trac.sagemath.org/ticket/3960





---

archive/issue_comments_028442.json:
```json
{
    "body": "This is definitely a blocker for 3.1.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T07:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28442",
    "user": "mabshoff"
}
```

This is definitely a blocker for 3.1.2.

Cheers,

Michael



---

archive/issue_comments_028443.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-08-27T07:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28443",
    "user": "mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_028444.json:
```json
{
    "body": "I believe that this is because somewhere the wrong username is taken into account. Here is an example: publish a worksheet, and navigate to it. The link should say \"edit this\", not \"edit a copy\".\n\nAlternatively, I found that the username passed to worksheet_html() in notebook.py is \"pub\", but was unable to find the source of the problem.",
    "created_at": "2008-08-27T16:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28444",
    "user": "itolkov"
}
```

I believe that this is because somewhere the wrong username is taken into account. Here is an example: publish a worksheet, and navigate to it. The link should say "edit this", not "edit a copy".

Alternatively, I found that the username passed to worksheet_html() in notebook.py is "pub", but was unable to find the source of the problem.



---

archive/issue_comments_028445.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28445",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028446.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2008-09-03T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28446",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_028447.json:
```json
{
    "body": "Attachment [trac_3960.patch](tarball://root/attachments/some-uuid/ticket3960/trac_3960.patch) by mhansen created at 2008-09-04 01:35:54",
    "created_at": "2008-09-04T01:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28447",
    "user": "mhansen"
}
```

Attachment [trac_3960.patch](tarball://root/attachments/some-uuid/ticket3960/trac_3960.patch) by mhansen created at 2008-09-04 01:35:54



---

archive/issue_comments_028448.json:
```json
{
    "body": "This patch fixes the issue and Mike walked through the code with me. Positive review. Mike is also writing a Selenium doctest for this bug, so we will catch it in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T01:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28448",
    "user": "mabshoff"
}
```

This patch fixes the issue and Mike walked through the code with me. Positive review. Mike is also writing a Selenium doctest for this bug, so we will catch it in the future.

Cheers,

Michael



---

archive/issue_comments_028449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T02:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28449",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028450.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T02:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28450",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc0
