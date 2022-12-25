# Issue 8780: add the Cephes spkg to Cygwin

archive/issues_008780.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @peterjeremy\n\nOn Cygwin, Sage needs c99 complex support which can be provided by the cephes library from netlib.org / www.moshier.net\n\nThere is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/cephes-2.8.spkg\n\n\nWe need to decide the best way to include this since it is only need on Cygwin (and maybe FreeBSD, etc.).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8780\n\n",
    "created_at": "2010-04-27T06:39:57Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "add the Cephes spkg to Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8780",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  @peterjeremy

On Cygwin, Sage needs c99 complex support which can be provided by the cephes library from netlib.org / www.moshier.net

There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/cephes-2.8.spkg


We need to decide the best way to include this since it is only need on Cygwin (and maybe FreeBSD, etc.).

Issue created by migration from https://trac.sagemath.org/ticket/8780





---

archive/issue_comments_080237.json:
```json
{
    "body": "How about test the OS name in spkg-install, and if it is cygwin, do something, otherwise return successfully without doing anything?",
    "created_at": "2010-04-27T18:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8780#issuecomment-80237",
    "user": "https://github.com/jasongrout"
}
```

How about test the OS name in spkg-install, and if it is cygwin, do something, otherwise return successfully without doing anything?



---

archive/issue_comments_080238.json:
```json
{
    "body": "Is it the same Solaris-only cvxopt problem that was solved (for cvxopt) by adding sun_complex.h there?\nIf yes, then it might be good to include Solaris in the list of architectures for which cephes is installed.",
    "created_at": "2010-04-28T06:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8780#issuecomment-80238",
    "user": "https://github.com/dimpase"
}
```

Is it the same Solaris-only cvxopt problem that was solved (for cvxopt) by adding sun_complex.h there?
If yes, then it might be good to include Solaris in the list of architectures for which cephes is installed.



---

archive/issue_comments_080239.json:
```json
{
    "body": "Sorry, I spoke too soon -- this doesn't quite fix the problem with cvxopt since it doesn't check $SAGE_LOCAL/include.  There is some other cleanup work that needs to be for the cvxopt-1.1.2 spkg as well.\n\nAlso, this is a little different than the Solaris issue since Cygwin doesn't have a complex.h, which is what the spkg provides.",
    "created_at": "2010-04-28T06:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8780#issuecomment-80239",
    "user": "https://github.com/mwhansen"
}
```

Sorry, I spoke too soon -- this doesn't quite fix the problem with cvxopt since it doesn't check $SAGE_LOCAL/include.  There is some other cleanup work that needs to be for the cvxopt-1.1.2 spkg as well.

Also, this is a little different than the Solaris issue since Cygwin doesn't have a complex.h, which is what the spkg provides.



---

archive/issue_comments_080240.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T01:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8780#issuecomment-80240",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_008945.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-05-26T01:15:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8780#event-8945"
}
```



---

archive/issue_comments_080241.json:
```json
{
    "body": "I did what Jason Grout suggests above as a little referee patch, and merged this into 4.4.3.alpha0.",
    "created_at": "2010-05-26T01:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8780",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8780#issuecomment-80241",
    "user": "https://github.com/williamstein"
}
```

I did what Jason Grout suggests above as a little referee patch, and merged this into 4.4.3.alpha0.
