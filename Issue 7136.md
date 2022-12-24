# Issue 7136: gp always building 32-bit on Solaris

archive/issues_007136.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  dimpase\n\nUsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nLooking at the directory $SAGE_HOME/local/bin, we can see that *pg* is being built as 32-bit binary, despite the fact that SAGE64 was set to \"yes\"\n\n```\ndrkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file gp\ngp:             ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available\n```\n\n\nThis is **far** from the only package building 32-bit when SAGE64 is set to \"yes\" on Solaris. All of the following do, and I suspect there are many others too.\n\n* zlib #7128\n* libgpg_error #7129\n* libpng #7130\n* libcliquer #7131\n* pari #7133\n* ntl #7134 \n* python #7135\n    \n\nmpir currently mixes 32 and 64-bit objects, so do not build at all #7132.\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7136\n\n",
    "created_at": "2009-10-06T00:53:01Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "gp always building 32-bit on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7136",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  dimpase

Using

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

Looking at the directory $SAGE_HOME/local/bin, we can see that *pg* is being built as 32-bit binary, despite the fact that SAGE64 was set to "yes"

```
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/bin] $ file gp
gp:             ELF 32-bit MSB executable SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped, no debugging information available
```


This is **far** from the only package building 32-bit when SAGE64 is set to "yes" on Solaris. All of the following do, and I suspect there are many others too.

* zlib #7128
* libgpg_error #7129
* libpng #7130
* libcliquer #7131
* pari #7133
* ntl #7134 
* python #7135
    

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.


Issue created by migration from https://trac.sagemath.org/ticket/7136





---

archive/issue_comments_059158.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59158",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059159.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59159",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_059160.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T19:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59160",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059161.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T19:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59161",
    "user": "mjo"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_059162.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59162",
    "user": "chapoton"
}
```

Resolution: invalid



---

archive/issue_comments_059163.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7136",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7136#issuecomment-59163",
    "user": "chapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
