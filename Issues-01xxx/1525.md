# Issue 1525: [with patch and spkg, with positive review] NetworkX upgraded spkg, Bipartite graphs

archive/issues_001525.json:
```json
{
    "body": "Assignee: @rlmill\n\nThere is a bug in the NetworkX function is_bipartite, which sometimes gives False positives. Due to this, a few examples in graph_generators.py give possibly bad output. I have labeled them with # random, and the following URL:\n\nhttps://networkx.lanl.gov/ticket/132\n\nOnce this bug is fixed, and NX updated in Sage, someone needs to go fix those docstrings.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1525\n\n",
    "closed_at": "2008-01-19T19:53:10Z",
    "created_at": "2007-12-15T20:28:49Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch and spkg, with positive review] NetworkX upgraded spkg, Bipartite graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1525",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

There is a bug in the NetworkX function is_bipartite, which sometimes gives False positives. Due to this, a few examples in graph_generators.py give possibly bad output. I have labeled them with # random, and the following URL:

https://networkx.lanl.gov/ticket/132

Once this bug is fixed, and NX updated in Sage, someone needs to go fix those docstrings.

Issue created by migration from https://trac.sagemath.org/ticket/1525





---

archive/issue_events_003846.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-15T20:29:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "milestone": "sage-2.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1525#event-3846"
}
```



---

archive/issue_comments_009728.json:
```json
{
    "body": "Changing assignee from @williamstein to @rlmill.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9728",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @williamstein to @rlmill.



---

archive/issue_comments_009729.json:
```json
{
    "body": "Changing component from algebraic geometry to graph theory.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9729",
    "user": "https://github.com/rlmill"
}
```

Changing component from algebraic geometry to graph theory.



---

archive/issue_comments_009730.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9730",
    "user": "https://github.com/rlmill"
}
```

Changing priority from major to minor.



---

archive/issue_comments_009731.json:
```json
{
    "body": "OK, now the NX ticket is closed, so the next step is to upgrade NX downstream.",
    "created_at": "2008-01-13T21:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9731",
    "user": "https://github.com/rlmill"
}
```

OK, now the NX ticket is closed, so the next step is to upgrade NX downstream.



---

archive/issue_comments_009732.json:
```json
{
    "body": "spkg is here:\nhttp://sage.math.washington.edu/home/rlmill/networkx-0.36.spkg",
    "created_at": "2008-01-14T00:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9732",
    "user": "https://github.com/rlmill"
}
```

spkg is here:
http://sage.math.washington.edu/home/rlmill/networkx-0.36.spkg



---

archive/issue_comments_009733.json:
```json
{
    "body": "Attachment [bipartite.patch](tarball://root/attachments/some-uuid/ticket1525/bipartite.patch) by @rlmill created at 2008-01-14 00:27:36\n\nNote that now these numbers are backed up by Sloane!",
    "created_at": "2008-01-14T00:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9733",
    "user": "https://github.com/rlmill"
}
```

Attachment [bipartite.patch](tarball://root/attachments/some-uuid/ticket1525/bipartite.patch) by @rlmill created at 2008-01-14 00:27:36

Note that now these numbers are backed up by Sloane!



---

archive/issue_comments_009734.json:
```json
{
    "body": "Looks good (and works) for me.",
    "created_at": "2008-01-19T00:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9734",
    "user": "https://github.com/mwhansen"
}
```

Looks good (and works) for me.



---

archive/issue_comments_009735.json:
```json
{
    "body": "An updated spkg with the content of doc/data removed, a new SPKG.txt and a hg repo can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/networkx-0.36.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T19:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated spkg with the content of doc/data removed, a new SPKG.txt and a hg repo can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/networkx-0.36.p0.spkg

Cheers,

Michael



---

archive/issue_events_003847.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-19T19:53:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1525#event-3847"
}
```



---

archive/issue_comments_009736.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T19:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_009737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T19:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9737",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
