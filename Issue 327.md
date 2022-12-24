# Issue 327: add perl 5.8 dependency for sage

archive/issues_000327.json:
```json
{
    "body": "Assignee: was\n\nIn sage base check of prerequisites should also check for perl 5.8.  According to Kevin \nBuzzard, building maxima using perl 5.6 fails with this error, but upgrading to perl 5.8\nresolves the problem:\n\n```\n\"Unknown open() mode '<:crlf' at ./build_index.pl line 25\".\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/327\n\n",
    "created_at": "2007-03-21T22:38:11Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "add perl 5.8 dependency for sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/327",
    "user": "was"
}
```
Assignee: was

In sage base check of prerequisites should also check for perl 5.8.  According to Kevin 
Buzzard, building maxima using perl 5.6 fails with this error, but upgrading to perl 5.8
resolves the problem:

```
"Unknown open() mode '<:crlf' at ./build_index.pl line 25".
```


Issue created by migration from https://trac.sagemath.org/ticket/327





---

archive/issue_comments_001547.json:
```json
{
    "body": "This will also applies to the optional PolyMakes.spkg once we update to release 2.3 - see ticket #297",
    "created_at": "2007-08-24T13:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/327#issuecomment-1547",
    "user": "mabshoff"
}
```

This will also applies to the optional PolyMakes.spkg once we update to release 2.3 - see ticket #297



---

archive/issue_comments_001548.json:
```json
{
    "body": "I think we do this now.  See line 5825 in prereq-0.7/configure.  Perhaps we can close this ticket?",
    "created_at": "2010-03-09T07:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/327#issuecomment-1548",
    "user": "jhpalmieri"
}
```

I think we do this now.  See line 5825 in prereq-0.7/configure.  Perhaps we can close this ticket?



---

archive/issue_comments_001549.json:
```json
{
    "body": "Yes, it can be closed. The configure script is generated from this bit of code I wrote in configure.ac\n\n\n```\n# The stats program R 2.9.2 needs perl 5.8.0 or later.\n# If anything needs a later version, then this should be updated.\nAC_PATH_PROG([PERL],[perl])\nAX_PROG_PERL_VERSION([5.8.0],[],[AC_MSG_ERROR([Sorry, your version of perl is too old]) ])\n```\n\n\nThe 'AC_MSG_ERROR' will cause the build to terminate at that point. \n\nDave",
    "created_at": "2010-06-09T20:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/327#issuecomment-1549",
    "user": "drkirkby"
}
```

Yes, it can be closed. The configure script is generated from this bit of code I wrote in configure.ac


```
# The stats program R 2.9.2 needs perl 5.8.0 or later.
# If anything needs a later version, then this should be updated.
AC_PATH_PROG([PERL],[perl])
AX_PROG_PERL_VERSION([5.8.0],[],[AC_MSG_ERROR([Sorry, your version of perl is too old]) ])
```


The 'AC_MSG_ERROR' will cause the build to terminate at that point. 

Dave



---

archive/issue_comments_001550.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T22:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/327#issuecomment-1550",
    "user": "drkirkby"
}
```

Resolution: fixed
