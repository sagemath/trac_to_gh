# Issue 1525: Bipartite graphs

archive/issues_001525.json:
```json
{
    "body": "Assignee: was\n\nThere is a bug in the NetworkX function is_bipartite, which sometimes gives False positives. Due to this, a few examples in graph_generators.py give possibly bad output. I have labeled them with # random, and the following URL:\n\nhttps://networkx.lanl.gov/ticket/132\n\nOnce this bug is fixed, and NX updated in Sage, someone needs to go fix those docstrings.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1525\n\n",
    "created_at": "2007-12-15T20:28:49Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Bipartite graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1525",
    "user": "rlm"
}
```
Assignee: was

There is a bug in the NetworkX function is_bipartite, which sometimes gives False positives. Due to this, a few examples in graph_generators.py give possibly bad output. I have labeled them with # random, and the following URL:

https://networkx.lanl.gov/ticket/132

Once this bug is fixed, and NX updated in Sage, someone needs to go fix those docstrings.

Issue created by migration from https://trac.sagemath.org/ticket/1525





---

archive/issue_comments_009754.json:
```json
{
    "body": "Changing assignee from was to rlm.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9754",
    "user": "rlm"
}
```

Changing assignee from was to rlm.



---

archive/issue_comments_009755.json:
```json
{
    "body": "Changing component from algebraic geometry to graph theory.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9755",
    "user": "rlm"
}
```

Changing component from algebraic geometry to graph theory.



---

archive/issue_comments_009756.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-12-15T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9756",
    "user": "rlm"
}
```

Changing priority from major to minor.



---

archive/issue_comments_009757.json:
```json
{
    "body": "OK, now the NX ticket is closed, so the next step is to upgrade NX downstream.",
    "created_at": "2008-01-13T21:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9757",
    "user": "rlm"
}
```

OK, now the NX ticket is closed, so the next step is to upgrade NX downstream.



---

archive/issue_comments_009758.json:
```json
{
    "body": "spkg is here:\nhttp://sage.math.washington.edu/home/rlmill/networkx-0.36.spkg",
    "created_at": "2008-01-14T00:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9758",
    "user": "rlm"
}
```

spkg is here:
http://sage.math.washington.edu/home/rlmill/networkx-0.36.spkg



---

archive/issue_comments_009759.json:
```json
{
    "body": "Attachment [bipartite.patch](tarball://root/attachments/some-uuid/ticket1525/bipartite.patch) by rlm created at 2008-01-14 00:27:36\n\nNote that now these numbers are backed up by Sloane!",
    "created_at": "2008-01-14T00:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9759",
    "user": "rlm"
}
```

Attachment [bipartite.patch](tarball://root/attachments/some-uuid/ticket1525/bipartite.patch) by rlm created at 2008-01-14 00:27:36

Note that now these numbers are backed up by Sloane!



---

archive/issue_comments_009760.json:
```json
{
    "body": "Looks good (and works) for me.",
    "created_at": "2008-01-19T00:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9760",
    "user": "mhansen"
}
```

Looks good (and works) for me.



---

archive/issue_comments_009761.json:
```json
{
    "body": "An updated spkg with the content of doc/data removed, a new SPKG.txt and a hg repo can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/networkx-0.36.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T19:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9761",
    "user": "mabshoff"
}
```

An updated spkg with the content of doc/data removed, a new SPKG.txt and a hg repo can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha0/networkx-0.36.p0.spkg

Cheers,

Michael



---

archive/issue_comments_009762.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-19T19:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9762",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_comments_009763.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T19:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1525#issuecomment-9763",
    "user": "mabshoff"
}
```

Resolution: fixed
