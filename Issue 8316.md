# Issue 8316: Remove the Jinja (not Jinja2) package

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-20 21:25:03

Assignee: tbd

CC:  alexghitza cwitty mhansen robertwb timdumol

With #7249 merged, it now seems that no Sage component depends on the "slightly outdated version" of [Jinja](http://jinja.pocoo.org/).  If this is indeed true, we can remove `jinja-*.spkg` from the Sage distribution.

Of course, we'll keep the "awesome version", `jinja2-*.spkg`.


---

Comment by mpatel created at 2010-03-05 00:40:59

SageNB no longer depends on Jinja.  The Sage library does:

```sh
$ cd SAGE_ROOT/devel/sage-main/sage
$ grep jinja `find -name \*.py\*` |grep import
./server/notebook/template.py:import jinja
./ext/gen_interpreters.py:from jinja import Environment
./ext/gen_interpreters.py:from jinja.datastructure import ComplainingUndefined
```



---

Comment by mpatel created at 2010-03-05 02:07:42

Use Jinja2 instead of Jinja.  sage repo.


---

Attachment

Use `myself` instead of `self`.  Replaces previous.


---

Comment by mpatel created at 2010-03-05 02:34:34

To do: Update `spkg/install` and `spkg/standard/deps`.  I'll wait for #8306.


---

Attachment

Updated `spkg/standard/deps`.  Based on #8306.


---

Attachment

Diff of `spkg/standard/deps` vs. #8306.


---

Attachment

Updated `spkg/install`.  Based on #8306.


---

Comment by mpatel created at 2010-06-14 06:50:01

Diff of `spkg/install` vs. #8306.


---

Attachment

With V1 of the patch, `sage -b` gives


```python
[...]
Building interpreters for fast_callable
Traceback (most recent call last):
  File "setup.py", line 109, in <module>
    sage.ext.gen_interpreters.rebuild(SAGE_DEVEL + 'sage/sage/ext/interpreters')
  File "/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py", line 3823, in rebuild
    build_interp(interp, dir)
  File "/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py", line 3788, in build_interp
    interp = ig.get_interpreter()
  File "/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py", line 3318, in get_interpreter
    self.write_interpreter(buff.write)
  File "/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py", line 2974, in write_interpreter
    """, s=s, self=self, i=indent_lines))
  File "/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py", line 177, in je
    return tmpl.render(kwargs)
  File "<template>", line 4, in top-level template code
  File "/home/mpatel/apps/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg/jinja2/runtime.py", line 132, in call
    return __obj(*args, **kwargs)
  File "/home/mpatel/apps/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg/jinja2/runtime.py", line 403, in _fail_with_undefined_error
    raise self._undefined_exception(hint)
jinja2.exceptions.UndefinedError: 'TemplateReference' object has no attribute 'func_header'
sage: There was an error installing modified sage library code.
```

The docstring for `jinja2.runtime.TemplateReference` is "The `self` in templates."  But I'm not sure why this happens.  Does Jinja2 not allow `self=self`?

V2 of the patch appears to be OK: `sage -b` works, Sage builds from scratch with `SAGE_CHECK`, the long tests pass.  Did I miss any `self` --> `myself` conversions?  Should I run some other tests?

I'm not familiar with `ext/`, so I've included some names from `hg log gen_interpreters.py` in the Cc: list.


---

Comment by mpatel created at 2010-06-14 08:58:58

Changing priority from major to minor.


---

Comment by mpatel created at 2010-06-14 08:58:58

Changing status from new to needs_review.


---

Comment by was created at 2010-06-22 04:36:54

Milestone sage-4.4.5 deleted


---

Attachment

deps.diff rebased to 4.5.rc1


---

Comment by cwitty created at 2010-07-16 02:57:56

Changing status from needs_review to positive_review.


---

Comment by cwitty created at 2010-07-16 02:57:56

Thanks for fixing up gen_interpreters.py, your changes look fine (and the template output from the patched gen_interpreters.py using jinja2 is byte-for-byte identical to the previous output using jinja).

I tested by starting from sage-4.5.rc1.tar, removing the jinja spkg, and applying install.diff and 4.5.rc1-deps.diff (the original deps.diff would no longer apply, so I rebased it).  I then typed "make", waited for the build to fail, applied trac_8316-remove_jinja.2.patch, and restarted the build.  The build was successfull, and all (long) tests passed.

Positive review.


---

Comment by mpatel created at 2010-08-09 09:52:55

I'm merging 

 * [attachment:trac_8316-remove_jinja.2.patch]
 * [attachment:install.diff]
 * [attachment:4.5.rc1-deps.diff]

into 4.5.3.alpha0.  Thanks for the review and rebasing the latter.


---

Comment by mpatel created at 2010-08-09 09:52:55

Resolution: fixed
