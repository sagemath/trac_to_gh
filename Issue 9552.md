# Issue 9552: cython.pyx references the old sage notebook code

archive/issues_009552.json:
```json
{
    "body": "Assignee: jason\n\nCC:  fbissey\n\nI noticed to my surprise that misc/cython.pyx has these lines in it (which should be fixed, of course):\n\n```\n import sage.server.support\n    d = {}\n    sage.server.support.cython_import_all(tmpfile, d,\n                                         verbose=verbose, compile_message=compile_message,\n                                         use_cache=use_cache,\n                                         create_local_c_file=False)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9552\n\n",
    "created_at": "2010-07-19T19:59:21Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "cython.pyx references the old sage notebook code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9552",
    "user": "was"
}
```
Assignee: jason

CC:  fbissey

I noticed to my surprise that misc/cython.pyx has these lines in it (which should be fixed, of course):

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

archive/issue_comments_092068.json:
```json
{
    "body": "Yeah, I think a lot of that stuff could go elsewhere, it's just support...\n\nIn this case the \"right\" fix is to move the whole Cython stuff somewhere else, probably just to cython.py (which is not a pyx file, at least not any more).",
    "created_at": "2014-08-15T05:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92068",
    "user": "kcrisman"
}
```

Yeah, I think a lot of that stuff could go elsewhere, it's just support...

In this case the "right" fix is to move the whole Cython stuff somewhere else, probably just to cython.py (which is not a pyx file, at least not any more).



---

archive/issue_comments_092069.json:
```json
{
    "body": "Indeed, this wouldn't be hard to do.  Worst-case we could move them but leave a deprecation that points to the new location (cython.py seems best).\n\n```\nsage: search_src('cython_import')\nmisc/cython.py:657:    sage.server.support.cython_import_all(tmpfile, d,\nmisc/cython.py:756:    from sage.server.support import cython_import\nmisc/cython.py:757:    return cython_import(file, create_local_c_file=False)\nmisc/cython_c.pyx:61:    sage.server.support.cython_import_all(tmpfile, globals(),\nserver/support.py:425:def cython_import(filename, verbose=False, compile_message=False,\nserver/support.py:452:def cython_import_all(filename, globals, verbose=False, compile_message=False,\nserver/support.py:468:    m = cython_import(filename, verbose=verbose, compile_message=compile_message,\n```\n\nThe notebook already has its own versions of these two functions so that is not a problem, as far as I can tell (though it wouldn't hurt testing it can still Cythonize after doing this).",
    "created_at": "2014-08-15T05:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92069",
    "user": "kcrisman"
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

archive/issue_comments_092070.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-03-25T17:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92070",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_092071.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-25T17:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92071",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092072.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-05-05T21:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92072",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_092073.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2015-05-30T11:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92073",
    "user": "fbissey"
}
```

Looks good to me.



---

archive/issue_comments_092074.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-30T11:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92074",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092075.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-05-30T22:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9552",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9552#issuecomment-92075",
    "user": "vbraun"
}
```

Resolution: fixed
