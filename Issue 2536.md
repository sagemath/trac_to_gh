# Issue 2536: get rid of SageObject.db and SageObject.version everywhere -- these turned out to "not catch on"

archive/issues_002536.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @mkoeppe\n\nHi,\n\nI wrote db and version methods that all SageObjects have.  It seemed like a good idea at the time.  They didn't catch on -- nobody finds this interesting, etc.  I vote for completely removing them from Sage. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2536\n\n",
    "created_at": "2008-03-16T00:57:20Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.5",
    "title": "get rid of SageObject.db and SageObject.version everywhere -- these turned out to \"not catch on\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2536",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  @mkoeppe

Hi,

I wrote db and version methods that all SageObjects have.  It seemed like a good idea at the time.  They didn't catch on -- nobody finds this interesting, etc.  I vote for completely removing them from Sage. 

Issue created by migration from https://trac.sagemath.org/ticket/2536





---

archive/issue_comments_017257.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17257",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_017258.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-01-11T22:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17258",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_017259.json:
```json
{
    "body": "I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?",
    "created_at": "2015-02-03T01:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17259",
    "user": "https://github.com/kcrisman"
}
```

I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?



---

archive/issue_comments_017260.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-07T23:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17260",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017261.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?\nAdded doctests.",
    "created_at": "2015-02-07T23:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17261",
    "user": "https://github.com/a-andre"
}
```

Replying to [comment:7 kcrisman]:
> I realize this seems silly for something no one uses, but perhaps we should doctest these deprecations?
Added doctests.



---

archive/issue_comments_017262.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-12T03:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17262",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_017263.json:
```json
{
    "body": "I'm a little surprised that doctest works since it does return a value, but I guess the `:...` covers that instead of the usual `:...:`.    Running doctests again but hopefully all is well.",
    "created_at": "2015-02-12T03:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17263",
    "user": "https://github.com/kcrisman"
}
```

I'm a little surprised that doctest works since it does return a value, but I guess the `:...` covers that instead of the usual `:...:`.    Running doctests again but hopefully all is well.



---

archive/issue_comments_017264.json:
```json
{
    "body": "\n```\nExpected:\n    Help on FiniteWordPath_2d_str in module sage.combinat.words.paths object:\n    ...\n    Methods inherited from FiniteWordPath_2d:\n    ...\n    Methods inherited from FiniteWordPath_all:\n    ...\n    This only works on Python classes that derive from SageObject.\nGot:\n<stuff ending with>\n     |      This only works on Python classes that derive from SageObject.\n     |      \n     |      TESTS::\n     |      \n     |          sage: v = DiGraph().version()\n     |          doctest:... DeprecationWarning: version() is deprecated.\n     |          See http://trac.sagemath.org/2536 for details.\n\n----------------------------------------------------------------------\nsage -t src/sage/combinat/words/paths.py  # 1 doctest failed\n```\n\nOtherwise all is well.  I guess this is my fault for asking for the deprecation warning after you did your long doctests, my apologies.",
    "created_at": "2015-02-12T04:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17264",
    "user": "https://github.com/kcrisman"
}
```


```
Expected:
    Help on FiniteWordPath_2d_str in module sage.combinat.words.paths object:
    ...
    Methods inherited from FiniteWordPath_2d:
    ...
    Methods inherited from FiniteWordPath_all:
    ...
    This only works on Python classes that derive from SageObject.
Got:
<stuff ending with>
     |      This only works on Python classes that derive from SageObject.
     |      
     |      TESTS::
     |      
     |          sage: v = DiGraph().version()
     |          doctest:... DeprecationWarning: version() is deprecated.
     |          See http://trac.sagemath.org/2536 for details.

----------------------------------------------------------------------
sage -t src/sage/combinat/words/paths.py  # 1 doctest failed
```

Otherwise all is well.  I guess this is my fault for asking for the deprecation warning after you did your long doctests, my apologies.



---

archive/issue_comments_017265.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-02-12T04:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17265",
    "user": "https://github.com/kcrisman"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_017266.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-13T15:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17266",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_017267.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-13T15:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17267",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_017268.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-13T18:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17268",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002717.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-02-17T19:28:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2536#event-2717"
}
```



---

archive/issue_comments_017269.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-17T19:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17269",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_017270.json:
```json
{
    "body": "#20376 uses `db()` for purposes of logging/debugging...",
    "created_at": "2016-05-03T19:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2536#issuecomment-17270",
    "user": "https://github.com/dimpase"
}
```

#20376 uses `db()` for purposes of logging/debugging...
