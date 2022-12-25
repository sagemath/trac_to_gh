# Issue 4367: plot gamma bug

archive/issues_004367.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n   sage: plot(gamma(x),(x,1,5))\n```\n\n\nGives error.  \n\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/jvoight/.sage/sage_notebook/worksheets/jvoight/10/code/18.py\", line 6, in <module>\n    plot(gamma(x),(x,Integer(1),Integer(5)))\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/transcendental.py\", line 106, in gamma\n    return CC(s).gamma()\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py\", line 211, in __call__\n    return x._complex_mpfr_field_( self )\n  File \"/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1451, in _complex_mpfr_field_\n    raise TypeError\nTypeError\n```\n\n\nThere seems to be some confusing type error in coercion between floats and complex numbers.\n\nJV\n\nIssue created by migration from https://trac.sagemath.org/ticket/4367\n\n",
    "created_at": "2008-10-25T18:54:40Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "plot gamma bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4367",
    "user": "https://github.com/jvoight"
}
```
Assignee: @williamstein


```
   sage: plot(gamma(x),(x,1,5))
```


Gives error.  


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jvoight/.sage/sage_notebook/worksheets/jvoight/10/code/18.py", line 6, in <module>
    plot(gamma(x),(x,Integer(1),Integer(5)))
  File "/usr/local/sage/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/transcendental.py", line 106, in gamma
    return CC(s).gamma()
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py", line 211, in __call__
    return x._complex_mpfr_field_( self )
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1451, in _complex_mpfr_field_
    raise TypeError
TypeError
```


There seems to be some confusing type error in coercion between floats and complex numbers.

JV

Issue created by migration from https://trac.sagemath.org/ticket/4367





---

archive/issue_comments_032026.json:
```json
{
    "body": "This has been resolved with #4432.",
    "created_at": "2008-12-19T07:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32026",
    "user": "https://github.com/robertwb"
}
```

This has been resolved with #4432.



---

archive/issue_comments_032027.json:
```json
{
    "body": "If we have a doctest in tree we can close this ticket, if not we should add a doctest and then close this ticket after merging it.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-19T07:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If we have a doctest in tree we can close this ticket, if not we should add a doctest and then close this ticket after merging it.

Cheers,

Michael



---

archive/issue_comments_032028.json:
```json
{
    "body": "will do",
    "created_at": "2008-12-19T07:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32028",
    "user": "https://github.com/robertwb"
}
```

will do



---

archive/issue_comments_032029.json:
```json
{
    "body": "Attachment [4367-gamma-plot.patch](tarball://root/attachments/some-uuid/ticket4367/4367-gamma-plot.patch) by @robertwb created at 2008-12-19 07:48:34\n\nTrivial doctest patch up.",
    "created_at": "2008-12-19T07:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32029",
    "user": "https://github.com/robertwb"
}
```

Attachment [4367-gamma-plot.patch](tarball://root/attachments/some-uuid/ticket4367/4367-gamma-plot.patch) by @robertwb created at 2008-12-19 07:48:34

Trivial doctest patch up.



---

archive/issue_comments_032030.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-20T21:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_032031.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T12:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_032032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T12:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4367#issuecomment-32032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004612.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-21T12:22:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4367",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4367#event-4612"
}
```
