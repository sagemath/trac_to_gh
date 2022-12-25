# Issue 677: add doctest option to check if result and expected result are numerically close

archive/issues_000677.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: doctest, numerical noise\n\n\n```\n[02:48] <mhansen_> Regarding testing with small numerical differences, that would still be something that'd need to be handled in within the doctest code since nose provides a \"wrapper\" around doctest.\n[02:48] <mabshoff> ok\n[02:48] <williamstein> The point would only be about what options there might be for doing it.\n[02:49] <williamstein> It might still have to go via preparsing.\n[02:49] <williamstein> E.g., a special comment\n[02:49] <williamstein> sage: foo(2.1)      # random low order bits\n[02:49] <williamstein> could mean that the output should be checked except the last 3 bits discarded\n[02:49] <williamstein> Another possibility would be to rewrite the doctests like this:\n[02:49] <williamstein> sage: foo(2.1)\n[02:50] <williamstein> 1.239930820384...\n[02:50] <williamstein> Then the doctest framework just ignored everythign starting at the ...'s.\n[02:50] <williamstein> But everything before will be checked to make sure it is the same.\n[02:50] <mabshoff> That sounds like a good solution with the \"...\"\n[02:50] <williamstein> That actually might be a good approach, since it will work in more complicated cases:\n[02:50] <williamstein> [foo(2.1), foo(2.2)]\n[02:50] <williamstein> [1.20919..., 2.233....]\n[02:50] <williamstein> You could try it with that doctest just now.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/677\n\n",
    "created_at": "2007-09-17T01:12:00Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "add doctest option to check if result and expected result are numerically close",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/677",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen

Keywords: doctest, numerical noise


```
[02:48] <mhansen_> Regarding testing with small numerical differences, that would still be something that'd need to be handled in within the doctest code since nose provides a "wrapper" around doctest.
[02:48] <mabshoff> ok
[02:48] <williamstein> The point would only be about what options there might be for doing it.
[02:49] <williamstein> It might still have to go via preparsing.
[02:49] <williamstein> E.g., a special comment
[02:49] <williamstein> sage: foo(2.1)      # random low order bits
[02:49] <williamstein> could mean that the output should be checked except the last 3 bits discarded
[02:49] <williamstein> Another possibility would be to rewrite the doctests like this:
[02:49] <williamstein> sage: foo(2.1)
[02:50] <williamstein> 1.239930820384...
[02:50] <williamstein> Then the doctest framework just ignored everythign starting at the ...'s.
[02:50] <williamstein> But everything before will be checked to make sure it is the same.
[02:50] <mabshoff> That sounds like a good solution with the "..."
[02:50] <williamstein> That actually might be a good approach, since it will work in more complicated cases:
[02:50] <williamstein> [foo(2.1), foo(2.2)]
[02:50] <williamstein> [1.20919..., 2.233....]
[02:50] <williamstein> You could try it with that doctest just now.
```


Issue created by migration from https://trac.sagemath.org/ticket/677





---

archive/issue_comments_003497.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/677#issuecomment-3497",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003498.json:
```json
{
    "body": "Ok, this works in python's doctests, so no need to implement this. Maybe it still needs to be added to the manual.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-26T22:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/677#issuecomment-3498",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this works in python's doctests, so no need to implement this. Maybe it still needs to be added to the manual.

Cheers,

Michael



---

archive/issue_comments_003499.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-26T22:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/677#issuecomment-3499",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000745.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-26T22:20:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/677",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/677#event-745"
}
```
