# Issue 9552: cython.pyx references the old sage notebook code

Issue created by migration from https://trac.sagemath.org/ticket/9552

Original creator: was

Original creation time: 2010-07-19 19:59:21

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



---

Comment by kcrisman created at 2014-08-15 05:41:39

Yeah, I think a lot of that stuff could go elsewhere, it's just support...

In this case the "right" fix is to move the whole Cython stuff somewhere else, probably just to cython.py (which is not a pyx file, at least not any more).


---

Comment by kcrisman created at 2014-08-15 05:46:10

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

Comment by jdemeyer created at 2015-03-25 17:00:00

New commits:


---

Comment by jdemeyer created at 2015-03-25 17:00:00

Changing status from new to needs_review.


---

Comment by git created at 2015-05-05 21:02:18

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by fbissey created at 2015-05-30 11:09:30

Looks good to me.


---

Comment by fbissey created at 2015-05-30 11:09:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-05-30 22:48:30

Resolution: fixed
