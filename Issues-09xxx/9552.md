# Issue 9552: cython.py references the old sage notebook code

archive/issues_009552.json:
```json
{
    "body": "Assignee: @jasongrout\n\nCC:  @kiwifb\n\n I noticed to my surprise that misc/cython.py has these lines in it (which should be fixed, of course):\n\n```\n import sage.server.support\n    d = {}\n    sage.server.support.cython_import_all(tmpfile, d,\n                                         verbose=verbose, compile_message=compile_message,\n                                         use_cache=use_cache,\n                                         create_local_c_file=False)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9552\n\n",
    "closed_at": "2015-05-30T22:48:30Z",
    "created_at": "2010-07-19T19:59:21Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "cython.py references the old sage notebook code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9552",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout

CC:  @kiwifb

 I noticed to my surprise that misc/cython.py has these lines in it (which should be fixed, of course):

```
 import sage.server.support
    d = {}
    sage.server.support.cython_import_all(tmpfile, d,
                                         verbose=verbose, compile_message=compile_message,
                                         use_cache=use_cache,
                                         create_local_c_file=False)
```

Issue created by migration from https://trac.sagemath.org/ticket/9552





---

archive/issue_events_023767.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23767"
}
```



---

archive/issue_events_023768.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23768"
}
```



---

archive/issue_events_023769.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23769"
}
```



---

archive/issue_events_023770.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23770"
}
```



---

archive/issue_events_023771.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23771"
}
```



---

archive/issue_events_023772.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23772"
}
```



---

archive/issue_events_023773.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23773"
}
```



---

archive/issue_comments_091914.json:
```json
{
    "body": "Yeah, I think a lot of that stuff could go elsewhere, it's just support...\n\nIn this case the \"right\" fix is to move the whole Cython stuff somewhere else, probably just to cython.py (which is not a pyx file, at least not any more).",
    "created_at": "2014-08-15T05:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91914",
    "user": "https://github.com/kcrisman"
}
```

Yeah, I think a lot of that stuff could go elsewhere, it's just support...

In this case the "right" fix is to move the whole Cython stuff somewhere else, probably just to cython.py (which is not a pyx file, at least not any more).



---

archive/issue_comments_091915.json:
```json
{
    "body": "Indeed, this wouldn't be hard to do.  Worst-case we could move them but leave a deprecation that points to the new location (cython.py seems best).\n\n```\nsage: search_src('cython_import')\nmisc/cython.py:657:    sage.server.support.cython_import_all(tmpfile, d,\nmisc/cython.py:756:    from sage.server.support import cython_import\nmisc/cython.py:757:    return cython_import(file, create_local_c_file=False)\nmisc/cython_c.pyx:61:    sage.server.support.cython_import_all(tmpfile, globals(),\nserver/support.py:425:def cython_import(filename, verbose=False, compile_message=False,\nserver/support.py:452:def cython_import_all(filename, globals, verbose=False, compile_message=False,\nserver/support.py:468:    m = cython_import(filename, verbose=verbose, compile_message=compile_message,\n```\nThe notebook already has its own versions of these two functions so that is not a problem, as far as I can tell (though it wouldn't hurt testing it can still Cythonize after doing this).",
    "created_at": "2014-08-15T05:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91915",
    "user": "https://github.com/kcrisman"
}
```

Indeed, this wouldn't be hard to do.  Worst-case we could move them but leave a deprecation that points to the new location (cython.py seems best).

```
sage: search_src('cython_import')
misc/cython.py:657:    sage.server.support.cython_import_all(tmpfile, d,
misc/cython.py:756:    from sage.server.support import cython_import
misc/cython.py:757:    return cython_import(file, create_local_c_file=False)
misc/cython_c.pyx:61:    sage.server.support.cython_import_all(tmpfile, globals(),
server/support.py:425:def cython_import(filename, verbose=False, compile_message=False,
server/support.py:452:def cython_import_all(filename, globals, verbose=False, compile_message=False,
server/support.py:468:    m = cython_import(filename, verbose=verbose, compile_message=compile_message,
```
The notebook already has its own versions of these two functions so that is not a problem, as far as I can tell (though it wouldn't hurt testing it can still Cythonize after doing this).



---

archive/issue_comments_091916.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-03-25T17:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91916",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_091917.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-25T17:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91917",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023774.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-03-25T17:00:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23774"
}
```



---

archive/issue_events_023775.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-03-25T17:00:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23775"
}
```



---

archive/issue_comments_091918.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-05-05T21:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91918",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_events_023776.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-05-30T07:51:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23776"
}
```



---

archive/issue_events_023777.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-05-30T07:51:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23777"
}
```



---

archive/issue_comments_091919.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2015-05-30T11:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91919",
    "user": "https://github.com/kiwifb"
}
```

Looks good to me.



---

archive/issue_comments_091920.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-30T11:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91920",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-05-30T22:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-91921",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_023778.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-05-30T22:48:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9552#event-23778"
}
```
