# Issue 1256: mwrank*.spkg now redundant, included in cremona*.spkg

archive/issues_001256.json:
```json
{
    "body": "Assignee: was\n\nThe code in the new cremona* package contains all of what was in the mwrank* package.  So the latter can be abandoned as soon as the wrappings for mwrank functions have been migrated.  This will only be really serious when I next fix a bug in mwrank -- since from now on I'll only be editing the version which is part of cremona*.\n\nI'm sure this is an easy job for someone who is familiar with the mwrank wrappings (not me, alas, though I suppose I should be).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1256\n\n",
    "created_at": "2007-11-24T21:22:42Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "title": "mwrank*.spkg now redundant, included in cremona*.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1256",
    "user": "cremona"
}
```
Assignee: was

The code in the new cremona* package contains all of what was in the mwrank* package.  So the latter can be abandoned as soon as the wrappings for mwrank functions have been migrated.  This will only be really serious when I next fix a bug in mwrank -- since from now on I'll only be editing the version which is part of cremona*.

I'm sure this is an easy job for someone who is familiar with the mwrank wrappings (not me, alas, though I suppose I should be).


Issue created by migration from https://trac.sagemath.org/ticket/1256





---

archive/issue_comments_007852.json:
```json
{
    "body": "I am taking care of this. The following things need to be done:\n\n```\n[18:17] <was_> Definitely the solution is to (1) remove the mwrank*spkg.\n[18:17] <was_> (2) copy over the mwrank executable which gets build as part of cremona*.spkg\n[18:17] <was_> (3) Change things in setup.py so that all the prober mwrank-related libraries are linked in (it's maybe 4 libraries now instead of 1)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T19:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7852",
    "user": "mabshoff"
}
```

I am taking care of this. The following things need to be done:

```
[18:17] <was_> Definitely the solution is to (1) remove the mwrank*spkg.
[18:17] <was_> (2) copy over the mwrank executable which gets build as part of cremona*.spkg
[18:17] <was_> (3) Change things in setup.py so that all the prober mwrank-related libraries are linked in (it's maybe 4 libraries now instead of 1)
```


Cheers,

Michael



---

archive/issue_comments_007853.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-05T19:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7853",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007854.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-12-05T19:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7854",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_007855.json:
```json
{
    "body": "Ok, the following binaries are installed my mwrank:\n* mwrank\n* tmrank\n* ratpoint\n* findinf\n* tate\n* conductor\n* torsion\n* twist\n* allisog\n* indep\n* tconic",
    "created_at": "2007-12-05T19:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7855",
    "user": "mabshoff"
}
```

Ok, the following binaries are installed my mwrank:
* mwrank
* tmrank
* ratpoint
* findinf
* tate
* conductor
* torsion
* twist
* allisog
* indep
* tconic



---

archive/issue_comments_007856.json:
```json
{
    "body": "Attachment [Sage-2.9.alpha0-mwrank-cremona-transition.patch](tarball://root/attachments/some-uuid/ticket1256/Sage-2.9.alpha0-mwrank-cremona-transition.patch) by mabshoff created at 2007-12-06 01:47:58",
    "created_at": "2007-12-06T01:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7856",
    "user": "mabshoff"
}
```

Attachment [Sage-2.9.alpha0-mwrank-cremona-transition.patch](tarball://root/attachments/some-uuid/ticket1256/Sage-2.9.alpha0-mwrank-cremona-transition.patch) by mabshoff created at 2007-12-06 01:47:58



---

archive/issue_comments_007857.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket1256/install) by mabshoff created at 2007-12-06 01:48:22",
    "created_at": "2007-12-06T01:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7857",
    "user": "mabshoff"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket1256/install) by mabshoff created at 2007-12-06 01:48:22



---

archive/issue_comments_007858.json:
```json
{
    "body": "Ok, I updated cremona.spkg to also install all mwrank binaries. It is at\n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071124.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-12-06T02:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7858",
    "user": "mabshoff"
}
```

Ok, I updated cremona.spkg to also install all mwrank binaries. It is at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p3.spkg

Cheers,

Michael



---

archive/issue_comments_007859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T02:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7859",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007860.json:
```json
{
    "body": "Merged in 2.9.alpha0.",
    "created_at": "2007-12-06T02:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1256#issuecomment-7860",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha0.
