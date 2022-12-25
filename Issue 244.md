# Issue 244: linbox into SAGE

archive/issues_000244.json:
```json
{
    "body": "Assignee: @williamstein\n\nBug problems:\n\n1. Find a way to turn off their very verbose output in some cases.  (The documented ways don't work.)\n2. Fix / investigate bug where charpoly hangs (see matrix2.pyx).  Or turn off using linbox by default for charpoly, since it's flake.  Or reimplement myself...\n  \nWhat will be included in the first release:\n* Fast dense echelon over QQ (via multimodular algorithm?)\n* (done) Fast minpoly over QQ\n* (done) Fast charpoly over QQ\n* Fast dense matrix multiply over Z/nZ\n* Fast sparse matrix multiply over Z/nZ\n* Fast minpoly over Z/nZ\n* Fast charpoly over Z/nZ\n\nIssue created by migration from https://trac.sagemath.org/ticket/244\n\n",
    "created_at": "2007-02-05T01:51:04Z",
    "labels": [
        "component: linear algebra"
    ],
    "title": "linbox into SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/244",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Bug problems:

1. Find a way to turn off their very verbose output in some cases.  (The documented ways don't work.)
2. Fix / investigate bug where charpoly hangs (see matrix2.pyx).  Or turn off using linbox by default for charpoly, since it's flake.  Or reimplement myself...
  
What will be included in the first release:
* Fast dense echelon over QQ (via multimodular algorithm?)
* (done) Fast minpoly over QQ
* (done) Fast charpoly over QQ
* Fast dense matrix multiply over Z/nZ
* Fast sparse matrix multiply over Z/nZ
* Fast minpoly over Z/nZ
* Fast charpoly over Z/nZ

Issue created by migration from https://trac.sagemath.org/ticket/244





---

archive/issue_events_000258.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-08-10T19:28:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/244",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/244#event-258"
}
```



---

archive/issue_comments_001077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-10T19:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/244#issuecomment-1077",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_001078.json:
```json
{
    "body": "LinBox was included a while ago.",
    "created_at": "2007-08-10T19:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/244",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/244#issuecomment-1078",
    "user": "https://github.com/malb"
}
```

LinBox was included a while ago.
