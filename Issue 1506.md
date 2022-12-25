# Issue 1506: ntl spkg -- dumb intentional error during the build

archive/issues_001506.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is dumb:\n\n\n```\ndmharvey: i'm building sage-2.9alpha7, and there's a problem in the build log with the NTL build, but the rest of it seems to be going okay (for the moment)\n[06:49am] dmharvey: i686-apple-darwin8-g++-4.0.1: unrecognized option '-shared'\n[06:49am] dmharvey: _main\n[06:49am] dmharvey: ___gmpn_add_n\n[06:49am] dmharvey: ___gmpn_addmul_1\n[06:49am] dmharvey: ___gmpn_divrem_1\n[06:49am] dmharvey: ___gmpn_gcd\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1506\n\n",
    "created_at": "2007-12-14T17:11:11Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "ntl spkg -- dumb intentional error during the build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1506",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is dumb:


```
dmharvey: i'm building sage-2.9alpha7, and there's a problem in the build log with the NTL build, but the rest of it seems to be going okay (for the moment)
[06:49am] dmharvey: i686-apple-darwin8-g++-4.0.1: unrecognized option '-shared'
[06:49am] dmharvey: _main
[06:49am] dmharvey: ___gmpn_add_n
[06:49am] dmharvey: ___gmpn_addmul_1
[06:49am] dmharvey: ___gmpn_divrem_1
[06:49am] dmharvey: ___gmpn_gcd
```


Issue created by migration from https://trac.sagemath.org/ticket/1506





---

archive/issue_comments_009620.json:
```json
{
    "body": "New spkg at \n\n http://sage.math.washington.edu/home/was/tmp/ntl-5.4.1.p8.spkg",
    "created_at": "2007-12-14T17:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1506#issuecomment-9620",
    "user": "https://github.com/williamstein"
}
```

New spkg at 

 http://sage.math.washington.edu/home/was/tmp/ntl-5.4.1.p8.spkg



---

archive/issue_comments_009621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T22:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1506#issuecomment-9621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009622.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-14T22:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1506#issuecomment-9622",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_001660.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-14T22:28:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1506",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1506#event-1660"
}
```
