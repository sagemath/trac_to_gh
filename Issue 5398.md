# Issue 5398: clone is broken in Sage 3.4.alpha0 due to non-7 bit ASCII characters in docstrings

archive/issues_005398.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @JohnCremona\n\nJohn Cremona reported in http://groups.google.com/group/sage-devel/browse_thread/thread/dc34f1b1f5fc4251\n\n```\nFrom my newly built 3.4.alpha0 I made a clone but it will not run, \ncomplaining about things like this: \n\nSyntaxError: Non-ASCII character '\\xc3' in file \n/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages\n/sage/combinat/sloane_functions.py \n\non line 6381, but no encoding declared; see \nhttp://www.python.org/peps/pep-0263.html for details \n(sloane_functions.py, line 6380) \n\nThat one is Mobius, spelled Mo\"bius (with an o-umlaut character). \nAnd before that I had a problem with Gro\"bner in interfaces/singular.py.\n \nIs this somehow caused by the ReST/Sphinx stuff?  It is hard to \nreview  patches when clones don't run... \n\nJohn \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5398\n\n",
    "created_at": "2009-02-27T21:32:52Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "clone is broken in Sage 3.4.alpha0 due to non-7 bit ASCII characters in docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5398",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

CC:  @JohnCremona

John Cremona reported in http://groups.google.com/group/sage-devel/browse_thread/thread/dc34f1b1f5fc4251

```
From my newly built 3.4.alpha0 I made a clone but it will not run, 
complaining about things like this: 

SyntaxError: Non-ASCII character '\xc3' in file 
/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages
/sage/combinat/sloane_functions.py 

on line 6381, but no encoding declared; see 
http://www.python.org/peps/pep-0263.html for details 
(sloane_functions.py, line 6380) 

That one is Mobius, spelled Mo"bius (with an o-umlaut character). 
And before that I had a problem with Gro"bner in interfaces/singular.py.
 
Is this somehow caused by the ReST/Sphinx stuff?  It is hard to 
review  patches when clones don't run... 

John 
```

Issue created by migration from https://trac.sagemath.org/ticket/5398





---

archive/issue_comments_041604.json:
```json
{
    "body": "Attachment [trac_5398.patch](tarball://root/attachments/some-uuid/ticket5398/trac_5398.patch) by mabshoff created at 2009-03-01 01:55:11",
    "created_at": "2009-03-01T01:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5398.patch](tarball://root/attachments/some-uuid/ticket5398/trac_5398.patch) by mabshoff created at 2009-03-01 01:55:11



---

archive/issue_comments_041605.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2009-03-01T01:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_041606.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T01:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041607.json:
```json
{
    "body": "The patch is excellent!",
    "created_at": "2009-03-01T01:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41607",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

The patch is excellent!



---

archive/issue_comments_041608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-01T02:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T02:05:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5398#event-12576"
}
```



---

archive/issue_comments_041609.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5398#issuecomment-41609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
