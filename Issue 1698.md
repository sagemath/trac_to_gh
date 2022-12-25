# Issue 1698: PolyBoRi doesn't work at all on Itanium Linux

archive/issues_001698.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @burcin\n\n\n```\n\nHas anybody ever built or used PolyBoRi on Linux *ITANIUM*?  \nBecause I just tried and the simplest\nuse of it from Sage segfaults PolyBoRi.   Since Itanium is \nsupposed to be supported Sage platform this is very\nserious:\n\nsage -t --gdb pbori.pyx\n\nSIGSEGV\nboost::intrusive_ptr<polybori::CCuddCore>::operator-> (this=0x0)\n   at ...intrusive_ptr.hpp:120\n120         return p_;\n\n(this was typed in by me manually just now). \n\nAny ideas?!   If necessary I can loan you the password I  have to an itanium box, but\nhopefully one of you has access to an Itanium Linux machine.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1698\n\n",
    "created_at": "2008-01-06T01:41:04Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "PolyBoRi doesn't work at all on Itanium Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1698",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @burcin


```

Has anybody ever built or used PolyBoRi on Linux *ITANIUM*?  
Because I just tried and the simplest
use of it from Sage segfaults PolyBoRi.   Since Itanium is 
supposed to be supported Sage platform this is very
serious:

sage -t --gdb pbori.pyx

SIGSEGV
boost::intrusive_ptr<polybori::CCuddCore>::operator-> (this=0x0)
   at ...intrusive_ptr.hpp:120
120         return p_;

(this was typed in by me manually just now). 

Any ideas?!   If necessary I can loan you the password I  have to an itanium box, but
hopefully one of you has access to an Itanium Linux machine.
```


Issue created by migration from https://trac.sagemath.org/ticket/1698





---

archive/issue_comments_010744.json:
```json
{
    "body": "Since Kate reported building 2.10 on Linux/Itanium and it passing doctests except #1898 the issue reported above is probably something system specific.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-23T23:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1698#issuecomment-10744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since Kate reported building 2.10 on Linux/Itanium and it passing doctests except #1898 the issue reported above is probably something system specific.

Cheers,

Michael



---

archive/issue_comments_010745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T15:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1698#issuecomment-10745",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001857.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-02-19T15:17:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1698",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1698#event-1857"
}
```
