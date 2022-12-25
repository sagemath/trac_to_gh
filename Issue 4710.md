# Issue 4710: fix docstring for divisors

archive/issues_004710.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nOn Dec 4, 2008, at 9:35 PM, pong wrote:\n\nIn SAGE 3.2.1 , the docstring of divisors says:\n\nDefinition:\tdivisors(n)\nDocstring:\n\n        Returns a list of all positive integer divisors\n        of the nonzero integer n.\n\n        A second parameter may be passed to surpress sorting\n        of the list (as ordering the list can be more time\n        consuming then creating it).\n\n        INPUT:\n            n -- the element\n            sorted -- whether or not to sort the output (default True)\n\nMy question is how to get an unsorted output?\n\nI tried divisors(300, sorted=False) but SAGE complaints that divisors\nonly takes 1 argument. In fact, the source codes seem to suggest that\nit will always return a sorted list.\n```\n\n\nNow the divisors are always returned sorted (as we have resolved the issue of sorting taking the majority of the time). The documentation needs to be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4710\n\n",
    "created_at": "2008-12-05T06:09:06Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "fix docstring for divisors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4710",
    "user": "https://github.com/robertwb"
}
```
Assignee: tba


```
On Dec 4, 2008, at 9:35 PM, pong wrote:

In SAGE 3.2.1 , the docstring of divisors says:

Definition:	divisors(n)
Docstring:

        Returns a list of all positive integer divisors
        of the nonzero integer n.

        A second parameter may be passed to surpress sorting
        of the list (as ordering the list can be more time
        consuming then creating it).

        INPUT:
            n -- the element
            sorted -- whether or not to sort the output (default True)

My question is how to get an unsorted output?

I tried divisors(300, sorted=False) but SAGE complaints that divisors
only takes 1 argument. In fact, the source codes seem to suggest that
it will always return a sorted list.
```


Now the divisors are always returned sorted (as we have resolved the issue of sorting taking the majority of the time). The documentation needs to be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/4710





---

archive/issue_comments_035446.json:
```json
{
    "body": "Here's a trivial patch.  Is this good enough?",
    "created_at": "2009-02-26T17:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4710#issuecomment-35446",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a trivial patch.  Is this good enough?



---

archive/issue_comments_035447.json:
```json
{
    "body": "Attachment [4710.patch](tarball://root/attachments/some-uuid/ticket4710/4710.patch) by @jhpalmieri created at 2009-02-26 17:08:29",
    "created_at": "2009-02-26T17:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4710#issuecomment-35447",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [4710.patch](tarball://root/attachments/some-uuid/ticket4710/4710.patch) by @jhpalmieri created at 2009-02-26 17:08:29



---

archive/issue_comments_035448.json:
```json
{
    "body": "Yep, looks good to me.",
    "created_at": "2009-02-26T20:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4710#issuecomment-35448",
    "user": "https://github.com/robertwb"
}
```

Yep, looks good to me.



---

archive/issue_events_004955.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-28T17:07:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4710#event-4955"
}
```



---

archive/issue_comments_035449.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T17:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4710#issuecomment-35449",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_035450.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T17:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4710#issuecomment-35450",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
