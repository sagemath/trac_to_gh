# Issue 5727: Improve doctest coverage for sage/modular

archive/issues_005727.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: doctests\n\nThe attached patch adds doctests for 28 previously undoctested functions in the sage/modular directory, and fixes 2 small bugs uncovered in the process: one in pickling of arithmetic subgroups defined by permutations, and one in dirichlet characters (galois_orbits() returned meaningless garbage when the base ring wasn't an integral domain). \n\nThis brings the doctest coverage to 100% for everything *except* the three big subdirectories modform/, modsym/ and hecke/. I will get to work on these next.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5727\n\n",
    "created_at": "2009-04-09T18:05:44Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Improve doctest coverage for sage/modular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5727",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

Keywords: doctests

The attached patch adds doctests for 28 previously undoctested functions in the sage/modular directory, and fixes 2 small bugs uncovered in the process: one in pickling of arithmetic subgroups defined by permutations, and one in dirichlet characters (galois_orbits() returned meaningless garbage when the base ring wasn't an integral domain). 

This brings the doctest coverage to 100% for everything *except* the three big subdirectories modform/, modsym/ and hecke/. I will get to work on these next.

Issue created by migration from https://trac.sagemath.org/ticket/5727





---

archive/issue_comments_044665.json:
```json
{
    "body": "patch against 3.4.1.rc1",
    "created_at": "2009-04-09T18:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44665",
    "user": "https://github.com/loefflerd"
}
```

patch against 3.4.1.rc1



---

archive/issue_comments_044666.json:
```json
{
    "body": "Attachment [modular_docs.patch](tarball://root/attachments/some-uuid/ticket5727/modular_docs.patch) by mabshoff created at 2009-04-09 18:36:10\n\nLet's change the status so the right reports pick up this ticket :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T18:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [modular_docs.patch](tarball://root/attachments/some-uuid/ticket5727/modular_docs.patch) by mabshoff created at 2009-04-09 18:36:10

Let's change the status so the right reports pick up this ticket :)

Cheers,

Michael



---

archive/issue_comments_044667.json:
```json
{
    "body": "REVIEW:\n* Put backquotes aroudn start_weight in the modform_generators docstring: \n  ` - start_weight -- an integer (default: 2) `\n* A doctest fails on 32-bit OS X: \n\n```\nsage -t --long devel/sage/sage/modular/arithgroup/arithgroup_perm.py\n**********************************************************************\nFile \"/Users/wstein/build/sage-3.4.1.rc1/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py\", line 202:\n    sage: cmp(G, 1)\nExpected:\n    -1\nGot:\n    1\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_9\n***Test Failed*** 1 failures.\n```\nI recommend changing the doctest to:\n\n```\n   sage: cmp(G,1) in [-1,1]\n```\nsince it depends on the OS.\n\n\nThese are trivial changes, so I've posted a tiny patch that adds them and given this a positive review.",
    "created_at": "2009-04-10T00:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44667",
    "user": "https://github.com/williamstein"
}
```

REVIEW:
* Put backquotes aroudn start_weight in the modform_generators docstring: 
  ` - start_weight -- an integer (default: 2) `
* A doctest fails on 32-bit OS X: 

```
sage -t --long devel/sage/sage/modular/arithgroup/arithgroup_perm.py
**********************************************************************
File "/Users/wstein/build/sage-3.4.1.rc1/devel/sage-main/sage/modular/arithgroup/arithgroup_perm.py", line 202:
    sage: cmp(G, 1)
Expected:
    -1
Got:
    1
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_9
***Test Failed*** 1 failures.
```
I recommend changing the doctest to:

```
   sage: cmp(G,1) in [-1,1]
```
since it depends on the OS.


These are trivial changes, so I've posted a tiny patch that adds them and given this a positive review.



---

archive/issue_events_013437.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-04-10T00:51:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5727#event-13437"
}
```



---

archive/issue_comments_044668.json:
```json
{
    "body": "Attachment [trac_5727_referee.patch](tarball://root/attachments/some-uuid/ticket5727/trac_5727_referee.patch) by @williamstein created at 2009-04-10 00:51:29\n\napply this after applying the above patch",
    "created_at": "2009-04-10T00:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44668",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5727_referee.patch](tarball://root/attachments/some-uuid/ticket5727/trac_5727_referee.patch) by @williamstein created at 2009-04-10 00:51:29

apply this after applying the above patch



---

archive/issue_comments_044669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-10T01:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044670.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T01:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_events_013438.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-10T01:53:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5727#event-13438"
}
```



---

archive/issue_comments_044671.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-10T19:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44671",
    "user": "https://github.com/loefflerd"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_044672.json:
```json
{
    "body": "Here's some more -- mostly in sage/modular/hecke/hecke_operator.py and sage/modular/hecke/module.py. This patch also adds Brandt modules into the reference manual.",
    "created_at": "2009-04-10T19:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44672",
    "user": "https://github.com/loefflerd"
}
```

Here's some more -- mostly in sage/modular/hecke/hecke_operator.py and sage/modular/hecke/module.py. This patch also adds Brandt modules into the reference manual.



---

archive/issue_comments_044673.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-10T19:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44673",
    "user": "https://github.com/loefflerd"
}
```

Changing status from closed to reopened.



---

archive/issue_events_013439.json:
```json
{
    "actor": "https://github.com/loefflerd",
    "created_at": "2009-04-10T19:31:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5727#event-13439"
}
```



---

archive/issue_comments_044674.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-10T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013440.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-10T19:39:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5727#event-13440"
}
```



---

archive/issue_comments_044675.json:
```json
{
    "body": "Please do not reopen tickets with merged patches. Instead open a new ticket for the new patch. I have deleted the new patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5727#issuecomment-44675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please do not reopen tickets with merged patches. Instead open a new ticket for the new patch. I have deleted the new patch.

Cheers,

Michael
