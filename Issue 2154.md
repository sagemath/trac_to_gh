# Issue 2154: Infinite memory allocation bug in PermutationGroupElement

archive/issues_002154.json:
```json
{
    "body": "Assignee: joyner\n\nRun the following code in a virtual machine with a smallish bound on its memory.  Or it will crash your machine.  (it took me 2 reboots to isolate the problem...)\n\n\n```\nPermutationGroup(2)\nPermutationGroupElement([1,1],S,check=False)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2154\n\n",
    "created_at": "2008-02-14T01:09:40Z",
    "labels": [
        "group theory",
        "blocker",
        "bug"
    ],
    "title": "Infinite memory allocation bug in PermutationGroupElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2154",
    "user": "boothby"
}
```
Assignee: joyner

Run the following code in a virtual machine with a smallish bound on its memory.  Or it will crash your machine.  (it took me 2 reboots to isolate the problem...)


```
PermutationGroup(2)
PermutationGroupElement([1,1],S,check=False)
```


Issue created by migration from https://trac.sagemath.org/ticket/2154





---

archive/issue_comments_014146.json:
```json
{
    "body": "Changing assignee from joyner to robertwb.",
    "created_at": "2008-02-14T01:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14146",
    "user": "boothby"
}
```

Changing assignee from joyner to robertwb.



---

archive/issue_comments_014147.json:
```json
{
    "body": "GAP is involved here, so the issue might not be in Sage itself.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T10:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14147",
    "user": "mabshoff"
}
```

GAP is involved here, so the issue might not be in Sage itself.

Cheers,

Michael



---

archive/issue_comments_014148.json:
```json
{
    "body": "Attachment\n\nIt looks like the problem here was actually infinite loops, but it now checks to make sure it always gets a valid permutation (even if check=False is set).",
    "created_at": "2008-02-21T22:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14148",
    "user": "robertwb"
}
```

Attachment

It looks like the problem here was actually infinite loops, but it now checks to make sure it always gets a valid permutation (even if check=False is set).



---

archive/issue_comments_014149.json:
```json
{
    "body": "\n```\n[02:01] <mabshoff> craigcitro: can you look at #2154 ? It looks good, \nbut I would like a second opinion.\n[02:11] <craigcitro> mabshoff: sure, it looks good to me.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T01:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14149",
    "user": "mabshoff"
}
```


```
[02:01] <mabshoff> craigcitro: can you look at #2154 ? It looks good, 
but I would like a second opinion.
[02:11] <craigcitro> mabshoff: sure, it looks good to me.
```


Cheers,

Michael



---

archive/issue_comments_014150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T01:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14150",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014151.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T01:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2154#issuecomment-14151",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
