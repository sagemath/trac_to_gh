# Issue 905: update the version of ipython included in sage

archive/issues_000905.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/905\n\n",
    "created_at": "2007-10-16T01:39:38Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "update the version of ipython included in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/905",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/905





---

archive/issue_comments_005554.json:
```json
{
    "body": "Changing assignee from @williamstein to @burcin.",
    "created_at": "2008-05-11T16:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5554",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @williamstein to @burcin.



---

archive/issue_comments_005555.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-11T16:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5555",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005556.json:
```json
{
    "body": "New package with upstream version 0.8.2 available here:\n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/ipython-0.8.2.spkg\n\nIt works for me.\n\nThere are quite a few entries in trac about updating ipython, see #1625, #1264, #1969.\n\n#1625 is a duplicate of this. The problem mentioned in #1264 doesn't happen with 0.8.2. I didn't update to svn as mentioned in #1969, since I don't know if it is stable enough to distribute with Sage.",
    "created_at": "2008-05-11T16:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5556",
    "user": "https://github.com/burcin"
}
```

New package with upstream version 0.8.2 available here:

http://www.risc.uni-linz.ac.at/people/berocal/sage/ipython-0.8.2.spkg

It works for me.

There are quite a few entries in trac about updating ipython, see #1625, #1264, #1969.

#1625 is a duplicate of this. The problem mentioned in #1264 doesn't happen with 0.8.2. I didn't update to svn as mentioned in #1969, since I don't know if it is stable enough to distribute with Sage.



---

archive/issue_comments_005557.json:
```json
{
    "body": "A couple remarks:\n\n* no need to add me to the CC - I get email from all tickets anyway\n* there is no hg repo in the spkg. I am fixing that\n* \"cp patches/iplib.py src/IPython/iplib.py\" should be removed from spkg-install\n\nI will do all those fixes and provided it installs I will give it a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T19:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A couple remarks:

* no need to add me to the CC - I get email from all tickets anyway
* there is no hg repo in the spkg. I am fixing that
* "cp patches/iplib.py src/IPython/iplib.py" should be removed from spkg-install

I will do all those fixes and provided it installs I will give it a positive review.

Cheers,

Michael



---

archive/issue_comments_005558.json:
```json
{
    "body": "I did all the above cleanups in \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ipython-0.8.2.p0.spkg\n\nPositive review since it install and doctests pass. Let's hope we didn't break anything else.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T19:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I did all the above cleanups in 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha0/ipython-0.8.2.p0.spkg

Positive review since it install and doctests pass. Let's hope we didn't break anything else.

Cheers,

Michael



---

archive/issue_comments_005559.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T19:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005560.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T19:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/905#issuecomment-5560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0
