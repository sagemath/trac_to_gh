# Issue 6547: deprecate the use of all.py instead of __init__.py

archive/issues_006547.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @kini\n\nFor historical reasons, we are using `foo.all.py` instead of `foo.__init__.py`. This is not Pythonic and we should change that (gradually).\n\nAlso, the developer's guide needs an update reflecting this change:\n\nhttp://www.sagemath.org/doc/developer/coding_in_python.html#creating-a-new-directory\n\nThis was discussed on [sage-devel]: http://groups.google.com/group/sage-devel/browse_thread/thread/1112fcc8345ecfd2\n\nIssue created by migration from https://trac.sagemath.org/ticket/6547\n\n",
    "closed_at": "2021-11-20T23:57:15Z",
    "created_at": "2009-07-17T09:51:16Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "deprecate the use of all.py instead of __init__.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6547",
    "user": "https://github.com/malb"
}
```
Assignee: cwitty

CC:  @kini

For historical reasons, we are using `foo.all.py` instead of `foo.__init__.py`. This is not Pythonic and we should change that (gradually).

Also, the developer's guide needs an update reflecting this change:

http://www.sagemath.org/doc/developer/coding_in_python.html#creating-a-new-directory

This was discussed on [sage-devel]: http://groups.google.com/group/sage-devel/browse_thread/thread/1112fcc8345ecfd2

Issue created by migration from https://trac.sagemath.org/ticket/6547





---

archive/issue_comments_053283.json:
```json
{
    "body": "One thing that we need to watch out for is importing an object into `foo/__init__.py` with the same name as a module in `foo/`.  Something like:\n\n```\nmike@mike-laptop:~/src/test_init$ ls foo\nbar.py  bar.pyc  __init__.py  __init__.pyc\nmike@mike-laptop:~/src/test_init$ cat foo/__init__.py\nfrom bar import bar\nmike@mike-laptop:~/src/test_init$ cat foo/bar.py\nbar = 200\n```\n\nThen, things like `foo.bar.bar` won't work.",
    "created_at": "2009-07-17T20:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53283",
    "user": "https://github.com/mwhansen"
}
```

One thing that we need to watch out for is importing an object into `foo/__init__.py` with the same name as a module in `foo/`.  Something like:

```
mike@mike-laptop:~/src/test_init$ ls foo
bar.py  bar.pyc  __init__.py  __init__.pyc
mike@mike-laptop:~/src/test_init$ cat foo/__init__.py
from bar import bar
mike@mike-laptop:~/src/test_init$ cat foo/bar.py
bar = 200
```

Then, things like `foo.bar.bar` won't work.



---

archive/issue_comments_053284.json:
```json
{
    "body": "A more specific objection:\n\nCurrently in Sage, we have\n\n```\nsage: type(sage.plot.plot)\n<type 'module'>\nsage: type(sage.plot.all.plot)\n<type 'function'>\n```\n\nIf we get rid of `all.py`, what should `sage.plot.plot` be?",
    "created_at": "2009-10-01T04:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53284",
    "user": "https://github.com/mwhansen"
}
```

A more specific objection:

Currently in Sage, we have

```
sage: type(sage.plot.plot)
<type 'module'>
sage: type(sage.plot.all.plot)
<type 'function'>
```

If we get rid of `all.py`, what should `sage.plot.plot` be?



---

archive/issue_comments_053285.json:
```json
{
    "body": "`sage.plot.plot.plot` or wherever it is implemented? I don't see the problem.",
    "created_at": "2009-10-01T07:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53285",
    "user": "https://github.com/malb"
}
```

`sage.plot.plot.plot` or wherever it is implemented? I don't see the problem.



---

archive/issue_comments_053286.json:
```json
{
    "body": "If `plot` the function is imported in `sage/plot/__init__.py`, then `sage.plot.plot` will be the function.  If someone happens to import `sage/plot/plot.py`, then `sage.plot.plot` becomes the module and not the function.  I'm not convinced that this won't cause troubles.",
    "created_at": "2009-10-01T07:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53286",
    "user": "https://github.com/mwhansen"
}
```

If `plot` the function is imported in `sage/plot/__init__.py`, then `sage.plot.plot` will be the function.  If someone happens to import `sage/plot/plot.py`, then `sage.plot.plot` becomes the module and not the function.  I'm not convinced that this won't cause troubles.



---

archive/issue_comments_053287.json:
```json
{
    "body": "To me the benefits of following the standard outweights the problems. But we should raise the issue on [sage-devel] and see what happens.",
    "created_at": "2009-10-01T09:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53287",
    "user": "https://github.com/malb"
}
```

To me the benefits of following the standard outweights the problems. But we should raise the issue on [sage-devel] and see what happens.



---

archive/issue_comments_053288.json:
```json
{
    "body": "Any news here? I'm not sure I fully understand Mike's objection, but can't we treat this as a deprecation, i.e. tell people that the usage `sage.plot.all.whatever` is deprecated?",
    "created_at": "2011-06-14T19:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53288",
    "user": "https://github.com/kini"
}
```

Any news here? I'm not sure I fully understand Mike's objection, but can't we treat this as a deprecation, i.e. tell people that the usage `sage.plot.all.whatever` is deprecated?



---

archive/issue_comments_053289.json:
```json
{
    "body": "After the switch to using native namespace packages (#29705), we cannot use `__init__.py` any more to populate packages. The modularization effort will certainly require us to think what to do with the `sage....all` packages, but moving stuff to `__init__.py` won't be it. So I am proposing to close this ticket as outdated.",
    "created_at": "2021-09-07T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53289",
    "user": "https://github.com/mkoeppe"
}
```

After the switch to using native namespace packages (#29705), we cannot use `__init__.py` any more to populate packages. The modularization effort will certainly require us to think what to do with the `sage....all` packages, but moving stuff to `__init__.py` won't be it. So I am proposing to close this ticket as outdated.



---

archive/issue_events_015444.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-09-07T07:47:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6547#event-15444"
}
```



---

archive/issue_comments_053290.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-09-07T07:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53290",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053291.json:
```json
{
    "body": "I agree that the aim of this ticket is not compatible with the modularization effort.",
    "created_at": "2021-11-15T12:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53291",
    "user": "https://github.com/kwankyu"
}
```

I agree that the aim of this ticket is not compatible with the modularization effort.



---

archive/issue_comments_053292.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-11-15T12:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53292",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053293.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-11-20T23:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6547#issuecomment-53293",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_015445.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-11-20T23:57:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6547",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6547#event-15445"
}
```
