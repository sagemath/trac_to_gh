# Issue 5327: multiple edge plots use symbolic computations

archive/issues_005327.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage: S = SupersingularModule(389)\nsage: H = S.hecke_matrix(2)\nsage: D = DiGraph(H)\nsage: P = D.plot()\n^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n```\n\n\nMaxima is absolutely not the thing to use here: I see in `graph_plot.py` the use of\n\n```\nx = SymbolicVariable('x')\nd = SymbolicVariable('d')\n```\n\netc.\n\nProbably my bad for letting that past review.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5327\n\n",
    "created_at": "2009-02-21T02:35:37Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "multiple edge plots use symbolic computations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5327",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill


```
sage: S = SupersingularModule(389)
sage: H = S.hecke_matrix(2)
sage: D = DiGraph(H)
sage: P = D.plot()
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
```


Maxima is absolutely not the thing to use here: I see in `graph_plot.py` the use of

```
x = SymbolicVariable('x')
d = SymbolicVariable('d')
```

etc.

Probably my bad for letting that past review.

Issue created by migration from https://trac.sagemath.org/ticket/5327





---

archive/issue_comments_040928.json:
```json
{
    "body": "Attachment [trac_5327.patch](tarball://root/attachments/some-uuid/ticket5327/trac_5327.patch) by @rlmill created at 2009-02-21 02:42:54",
    "created_at": "2009-02-21T02:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5327#issuecomment-40928",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5327.patch](tarball://root/attachments/some-uuid/ticket5327/trac_5327.patch) by @rlmill created at 2009-02-21 02:42:54



---

archive/issue_comments_040929.json:
```json
{
    "body": "Excellent.  I'm glad you were so fast with this and that you (rlm) got to look like Bill Gates doing the demo today instead of me looking like that again at Microsoft!",
    "created_at": "2009-02-21T03:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5327#issuecomment-40929",
    "user": "https://github.com/williamstein"
}
```

Excellent.  I'm glad you were so fast with this and that you (rlm) got to look like Bill Gates doing the demo today instead of me looking like that again at Microsoft!



---

archive/issue_comments_040930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-21T09:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5327#issuecomment-40930",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040931.json:
```json
{
    "body": "Merged in Sage 3.3.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T09:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5327#issuecomment-40931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.final.

Cheers,

Michael



---

archive/issue_events_005580.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-21T09:42:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5327",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5327#event-5580"
}
```
