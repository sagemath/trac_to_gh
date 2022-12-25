# Issue 7135: python always building 32-bit on Solaris

archive/issues_007135.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dimpase\n\nUsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nlooking at the directory $SAGE_HOME/local/bin, we can see that python is being built as 32-bit, despite the fact that SAGE64 was set to \"yes\"\n\n\n```\npython:         ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\npython2.6:      ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\n```\n\n\nThis is **far** from the only package building 32-bit when SAGE64 is set to \"yes\" on Solaris. All of the following do, and I suspect there are many others too. \n\n* zlib #7128\n* libgpg_error #7129\n* libpng #7130\n* libcliquer #7131\n* pari #7133 \n* ntl #7134\n\nmpir currently mixes 32 and 64-bit objects, so do not build at all #7132.\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7135\n\n",
    "created_at": "2009-10-06T00:48:50Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "python always building 32-bit on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7135",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @dimpase

Using

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

looking at the directory $SAGE_HOME/local/bin, we can see that python is being built as 32-bit, despite the fact that SAGE64 was set to "yes"


```
python:         ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
python2.6:      ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
```


This is **far** from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too. 

* zlib #7128
* libgpg_error #7129
* libpng #7130
* libcliquer #7131
* pari #7133 
* ntl #7134

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform. 

Issue created by migration from https://trac.sagemath.org/ticket/7135





---

archive/issue_comments_059042.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7135#issuecomment-59042",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_059043.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7135#issuecomment-59043",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059044.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-08T19:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7135#issuecomment-59044",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007355.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-09T08:26:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7135",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7135#event-7355"
}
```



---

archive/issue_comments_059045.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-09T08:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7135#issuecomment-59045",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
