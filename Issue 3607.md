# Issue 3607: graph_isom.py: "Conditional jump or move depends on uninitialised value(s)"

archive/issues_003607.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\n==19975== Conditional jump or move depends on uninitialised value(s)\n==19975==    at 0x1F3E16DD: __pyx_pf_4sage_6graphs_10graph_isom_search_tree (graph_isom.c:12972)\n==19975==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)\n==19975==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==19975==    by 0x4952F3: do_call (ceval.c:3784)\n==19975==    by 0x494BAA: call_function (ceval.c:3596)\n==19975==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)\n==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==19975==    by 0x48B385: PyEval_EvalCode (ceval.c:494)\n==19975==    by 0x4965CA: exec_statement (ceval.c:4177)\n==19975==    by 0x48EE67: PyEval_EvalFrameEx (ceval.c:1666)\n==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==19975==    by 0x494E7C: fast_function (ceval.c:3669)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3607\n\n",
    "created_at": "2008-07-08T11:51:25Z",
    "labels": [
        "component: memleak",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "graph_isom.py: \"Conditional jump or move depends on uninitialised value(s)\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @rlmill


```
==19975== Conditional jump or move depends on uninitialised value(s)
==19975==    at 0x1F3E16DD: __pyx_pf_4sage_6graphs_10graph_isom_search_tree (graph_isom.c:12972)
==19975==    by 0x4F0F43: PyCFunction_Call (methodobject.c:77)
==19975==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==19975==    by 0x4952F3: do_call (ceval.c:3784)
==19975==    by 0x494BAA: call_function (ceval.c:3596)
==19975==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==19975==    by 0x48B385: PyEval_EvalCode (ceval.c:494)
==19975==    by 0x4965CA: exec_statement (ceval.c:4177)
==19975==    by 0x48EE67: PyEval_EvalFrameEx (ceval.c:1666)
==19975==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==19975==    by 0x494E7C: fast_function (ceval.c:3669)
```


Issue created by migration from https://trac.sagemath.org/ticket/3607





---

archive/issue_comments_025427.json:
```json
{
    "body": "In state 6 and state 16, the two lines\n\n```\nif hb > nu.k: # update hb since we are backtracking (not in [1])\n    hb = nu.k # recall hb is the longest common ancestor of rho and nu\n```\n\nneed to be wrapped with an `if lab:` clause. Will post a patch once my build finishes.",
    "created_at": "2008-07-08T19:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25427",
    "user": "https://github.com/rlmill"
}
```

In state 6 and state 16, the two lines

```
if hb > nu.k: # update hb since we are backtracking (not in [1])
    hb = nu.k # recall hb is the longest common ancestor of rho and nu
```

need to be wrapped with an `if lab:` clause. Will post a patch once my build finishes.



---

archive/issue_comments_025428.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-08T19:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25428",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025429.json:
```json
{
    "body": "Attachment [trac3607.patch](tarball://root/attachments/some-uuid/ticket3607/trac3607.patch) by mabshoff created at 2008-07-08 20:09:30",
    "created_at": "2008-07-08T20:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac3607.patch](tarball://root/attachments/some-uuid/ticket3607/trac3607.patch) by mabshoff created at 2008-07-08 20:09:30



---

archive/issue_comments_025430.json:
```json
{
    "body": "Nice job rlm, this nails the issue and valgrind now gives graph_isom.py a clean bill of health.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-08T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice job rlm, this nails the issue and valgrind now gives graph_isom.py a clean bill of health.

Cheers,

Michael



---

archive/issue_comments_025431.json:
```json
{
    "body": "For the record: This is before the patch on Itanium SLES 10:\n\n```\nsage -t  devel/sage/sage/graphs/graph_isom.pyx              **********************************************************************\nFile \"/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py\", line 1383:\n    sage: Y0.is_isomorphic(Y1)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py\", line 1385:\n    sage: Y0.is_isomorphic(HS)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n```\n\nBut with the patch applied it still fails:\n\n```\nmabshoff@iras:~/sage-3.0.4.alpha2-SLES10-4.3.1> ./sage -t -long devel/sage-main/sage/graphs/graph_isom.pyx\nsage -t -long devel/sage-main/sage/graphs/graph_isom.pyx    **********************************************************************\nFile \"/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py\", line 1383:\n    sage: Y0.is_isomorphic(Y1)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py\", line 1385:\n    sage: Y0.is_isomorphic(HS)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   2 of 124 in __main__.example_24\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/.doctest_graph_isom.py\n         [89.4 s]\nexit code: 1024\n```\n\nSo this is likely a gcc bug or something that exposes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-09T07:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: This is before the patch on Itanium SLES 10:

```
sage -t  devel/sage/sage/graphs/graph_isom.pyx              **********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1383:
    sage: Y0.is_isomorphic(Y1)
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1385:
    sage: Y0.is_isomorphic(HS)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
```

But with the patch applied it still fails:

```
mabshoff@iras:~/sage-3.0.4.alpha2-SLES10-4.3.1> ./sage -t -long devel/sage-main/sage/graphs/graph_isom.pyx
sage -t -long devel/sage-main/sage/graphs/graph_isom.pyx    **********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1383:
    sage: Y0.is_isomorphic(Y1)
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/graph_isom.py", line 1385:
    sage: Y0.is_isomorphic(HS)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of 124 in __main__.example_24
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mabshoff/sage-3.0.4.alpha2-SLES10-4.3.1/tmp/.doctest_graph_isom.py
         [89.4 s]
exit code: 1024
```

So this is likely a gcc bug or something that exposes the issue.

Cheers,

Michael



---

archive/issue_comments_025432.json:
```json
{
    "body": "The patch itself fixes a problem and should be applied obviously. I meant to mention that on the ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-09T07:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25432",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch itself fixes a problem and should be applied obviously. I meant to mention that on the ticket.

Cheers,

Michael



---

archive/issue_comments_025433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-09T16:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25433",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_025434.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc2",
    "created_at": "2008-07-09T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3607#issuecomment-25434",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.rc2
