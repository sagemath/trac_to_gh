# Issue 8316: Remove the Jinja (not Jinja2) package

archive/issues_008316.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  alexghitza cwitty @mwhansen @robertwb @TimDumol\n\nWith #7249 merged, it now seems that no Sage component depends on the \"slightly outdated version\" of [Jinja](http://jinja.pocoo.org/).  If this is indeed true, we can remove `jinja-*.spkg` from the Sage distribution.\n\nOf course, we'll keep the \"awesome version\", `jinja2-*.spkg`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8316\n\n",
    "created_at": "2010-02-20T21:25:03Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Remove the Jinja (not Jinja2) package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8316",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  alexghitza cwitty @mwhansen @robertwb @TimDumol

With #7249 merged, it now seems that no Sage component depends on the "slightly outdated version" of [Jinja](http://jinja.pocoo.org/).  If this is indeed true, we can remove `jinja-*.spkg` from the Sage distribution.

Of course, we'll keep the "awesome version", `jinja2-*.spkg`.

Issue created by migration from https://trac.sagemath.org/ticket/8316





---

archive/issue_comments_073633.json:
```json
{
    "body": "SageNB no longer depends on Jinja.  The Sage library does:\n\n```sh\n$ cd SAGE_ROOT/devel/sage-main/sage\n$ grep jinja `find -name \\*.py\\*` |grep import\n./server/notebook/template.py:import jinja\n./ext/gen_interpreters.py:from jinja import Environment\n./ext/gen_interpreters.py:from jinja.datastructure import ComplainingUndefined\n```\n",
    "created_at": "2010-03-05T00:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73633",
    "user": "https://github.com/qed777"
}
```

SageNB no longer depends on Jinja.  The Sage library does:

```sh
$ cd SAGE_ROOT/devel/sage-main/sage
$ grep jinja `find -name \*.py\*` |grep import
./server/notebook/template.py:import jinja
./ext/gen_interpreters.py:from jinja import Environment
./ext/gen_interpreters.py:from jinja.datastructure import ComplainingUndefined
```




---

archive/issue_comments_073634.json:
```json
{
    "body": "Use Jinja2 instead of Jinja.  sage repo.",
    "created_at": "2010-03-05T02:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73634",
    "user": "https://github.com/qed777"
}
```

Use Jinja2 instead of Jinja.  sage repo.



---

archive/issue_comments_073635.json:
```json
{
    "body": "Attachment [trac_8316-remove_jinja.2.patch](tarball://root/attachments/some-uuid/ticket8316/trac_8316-remove_jinja.2.patch) by @qed777 created at 2010-03-05 02:33:06\n\nUse `myself` instead of `self`.  Replaces previous.",
    "created_at": "2010-03-05T02:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73635",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8316-remove_jinja.2.patch](tarball://root/attachments/some-uuid/ticket8316/trac_8316-remove_jinja.2.patch) by @qed777 created at 2010-03-05 02:33:06

Use `myself` instead of `self`.  Replaces previous.



---

archive/issue_comments_073636.json:
```json
{
    "body": "To do: Update `spkg/install` and `spkg/standard/deps`.  I'll wait for #8306.",
    "created_at": "2010-03-05T02:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73636",
    "user": "https://github.com/qed777"
}
```

To do: Update `spkg/install` and `spkg/standard/deps`.  I'll wait for #8306.



---

archive/issue_comments_073637.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket8316/deps) by @qed777 created at 2010-06-14 06:48:28\n\nUpdated `spkg/standard/deps`.  Based on #8306.",
    "created_at": "2010-06-14T06:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73637",
    "user": "https://github.com/qed777"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket8316/deps) by @qed777 created at 2010-06-14 06:48:28

Updated `spkg/standard/deps`.  Based on #8306.



---

archive/issue_comments_073638.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8316/deps.diff) by @qed777 created at 2010-06-14 06:48:58\n\nDiff of `spkg/standard/deps` vs. #8306.",
    "created_at": "2010-06-14T06:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73638",
    "user": "https://github.com/qed777"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket8316/deps.diff) by @qed777 created at 2010-06-14 06:48:58

Diff of `spkg/standard/deps` vs. #8306.



---

archive/issue_comments_073639.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket8316/install) by @qed777 created at 2010-06-14 06:49:38\n\nUpdated `spkg/install`.  Based on #8306.",
    "created_at": "2010-06-14T06:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73639",
    "user": "https://github.com/qed777"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket8316/install) by @qed777 created at 2010-06-14 06:49:38

Updated `spkg/install`.  Based on #8306.



---

archive/issue_comments_073640.json:
```json
{
    "body": "Diff of `spkg/install` vs. #8306.",
    "created_at": "2010-06-14T06:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73640",
    "user": "https://github.com/qed777"
}
```

Diff of `spkg/install` vs. #8306.



---

archive/issue_comments_073641.json:
```json
{
    "body": "Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8316/install.diff) by @qed777 created at 2010-06-14 08:58:58\n\nWith V1 of the patch, `sage -b` gives\n\n\n```python\n[...]\nBuilding interpreters for fast_callable\nTraceback (most recent call last):\n  File \"setup.py\", line 109, in <module>\n    sage.ext.gen_interpreters.rebuild(SAGE_DEVEL + 'sage/sage/ext/interpreters')\n  File \"/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py\", line 3823, in rebuild\n    build_interp(interp, dir)\n  File \"/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py\", line 3788, in build_interp\n    interp = ig.get_interpreter()\n  File \"/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py\", line 3318, in get_interpreter\n    self.write_interpreter(buff.write)\n  File \"/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py\", line 2974, in write_interpreter\n    \"\"\", s=s, self=self, i=indent_lines))\n  File \"/mnt/usb1/scratch/mpatel/apps/sage-4.4.4.a0/devel/sage-main/sage/ext/gen_interpreters.py\", line 177, in je\n    return tmpl.render(kwargs)\n  File \"<template>\", line 4, in top-level template code\n  File \"/home/mpatel/apps/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg/jinja2/runtime.py\", line 132, in call\n    return __obj(*args, **kwargs)\n  File \"/home/mpatel/apps/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg/jinja2/runtime.py\", line 403, in _fail_with_undefined_error\n    raise self._undefined_exception(hint)\njinja2.exceptions.UndefinedError: 'TemplateReference' object has no attribute 'func_header'\nsage: There was an error installing modified sage library code.\n```\n\nThe docstring for `jinja2.runtime.TemplateReference` is \"The `self` in templates.\"  But I'm not sure why this happens.  Does Jinja2 not allow `self=self`?\n\nV2 of the patch appears to be OK: `sage -b` works, Sage builds from scratch with `SAGE_CHECK`, the long tests pass.  Did I miss any `self` --> `myself` conversions?  Should I run some other tests?\n\nI'm not familiar with `ext/`, so I've included some names from `hg log gen_interpreters.py` in the Cc: list.",
    "created_at": "2010-06-14T08:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73641",
    "user": "https://github.com/qed777"
}
```

Attachment [install.diff](tarball://root/attachments/some-uuid/ticket8316/install.diff) by @qed777 created at 2010-06-14 08:58:58

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

archive/issue_comments_073642.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-06-14T08:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73642",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to minor.



---

archive/issue_comments_073643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-14T08:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73643",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_events_019903.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-22T04:36:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8316#event-19903"
}
```



---

archive/issue_comments_073644.json:
```json
{
    "body": "Milestone sage-4.4.5 deleted",
    "created_at": "2010-06-22T04:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73644",
    "user": "https://github.com/williamstein"
}
```

Milestone sage-4.4.5 deleted



---

archive/issue_comments_073645.json:
```json
{
    "body": "Attachment [4.5.rc1-deps.diff](tarball://root/attachments/some-uuid/ticket8316/4.5.rc1-deps.diff) by cwitty created at 2010-07-16 02:29:54\n\ndeps.diff rebased to 4.5.rc1",
    "created_at": "2010-07-16T02:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73645",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [4.5.rc1-deps.diff](tarball://root/attachments/some-uuid/ticket8316/4.5.rc1-deps.diff) by cwitty created at 2010-07-16 02:29:54

deps.diff rebased to 4.5.rc1



---

archive/issue_comments_073646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T02:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73646",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073647.json:
```json
{
    "body": "Thanks for fixing up gen_interpreters.py, your changes look fine (and the template output from the patched gen_interpreters.py using jinja2 is byte-for-byte identical to the previous output using jinja).\n\nI tested by starting from sage-4.5.rc1.tar, removing the jinja spkg, and applying install.diff and 4.5.rc1-deps.diff (the original deps.diff would no longer apply, so I rebased it).  I then typed \"make\", waited for the build to fail, applied trac_8316-remove_jinja.2.patch, and restarted the build.  The build was successfull, and all (long) tests passed.\n\nPositive review.",
    "created_at": "2010-07-16T02:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73647",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Thanks for fixing up gen_interpreters.py, your changes look fine (and the template output from the patched gen_interpreters.py using jinja2 is byte-for-byte identical to the previous output using jinja).

I tested by starting from sage-4.5.rc1.tar, removing the jinja spkg, and applying install.diff and 4.5.rc1-deps.diff (the original deps.diff would no longer apply, so I rebased it).  I then typed "make", waited for the build to fail, applied trac_8316-remove_jinja.2.patch, and restarted the build.  The build was successfull, and all (long) tests passed.

Positive review.



---

archive/issue_comments_073648.json:
```json
{
    "body": "I'm merging \n\n* [attachment:trac_8316-remove_jinja.2.patch]\n* [attachment:install.diff]\n* [attachment:4.5.rc1-deps.diff]\n\ninto 4.5.3.alpha0.  Thanks for the review and rebasing the latter.",
    "created_at": "2010-08-09T09:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73648",
    "user": "https://github.com/qed777"
}
```

I'm merging 

* [attachment:trac_8316-remove_jinja.2.patch]
* [attachment:install.diff]
* [attachment:4.5.rc1-deps.diff]

into 4.5.3.alpha0.  Thanks for the review and rebasing the latter.



---

archive/issue_comments_073649.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8316#issuecomment-73649",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019904.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:52:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8316#event-19904"
}
```
