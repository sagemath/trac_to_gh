# Issue 209: sageinspect bug on 64-bit linux?

archive/issues_000209.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nage -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************\\\n************************\nFile \"sageinspect.py\", line 65:\n    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)###line 65:\n    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 121, \\\nin _sage_getargspec_sagex\n        raise ValueError, \"Could not parse sagex argspec\"\n    ValueError: Could not parse sagex argspec\n**********************************************************************\nFile \"sageinspect.py\", line 67:\n    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)###line 67:\n    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 121, \\\nin _sage_getargspec_sagex\n        raise ValueError, \"Could not parse sagex argspec\"\n    ValueError: Could not parse sagex argspec\n**********************************************************************\n**********************************************************************\nFile \"sageinspect.py\", line 134:\n    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[0]>\", line 1, in <module>\n        sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)###line 134:\n    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)\n      File \"/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 154, \\\nin sage_getargspec\n        raise TypeError, 'arg is not a Python or a Sagex function'\n    TypeError: arg is not a Python or a Sagex function\n**********************************************************************\nFile \"sageinspect.py\", line 166:\n    sage: sage.misc.sageinspect.sage_getdef(sage.rings.rational.make_rational, obj_name='mr')\nExpected:\n    'mr(s)'\nGot:\n    'mr( ... )'\n**********************************************************************\n**********************************************************************\nFile \"sageinspect.py\", line 168:\n    sage: sage.misc.sageinspect.sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')\nExpected:\n    \"factor(algorithm='pari')\"\nGot:\n    'factor( ... )'\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/209\n\n",
    "created_at": "2007-01-23T18:49:10Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "sageinspect bug on 64-bit linux?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/209",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
age -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************\
************************
File "sageinspect.py", line 65:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)###line 65:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.integer.Integer.factor)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 121, \
in _sage_getargspec_sagex
        raise ValueError, "Could not parse sagex argspec"
    ValueError: Could not parse sagex argspec
**********************************************************************
File "sageinspect.py", line 67:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)###line 67:
    sage: sage.misc.sageinspect._sage_getargspec_sagex(sage.rings.rational.make_rational)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 121, \
in _sage_getargspec_sagex
        raise ValueError, "Could not parse sagex argspec"
    ValueError: Could not parse sagex argspec
**********************************************************************
**********************************************************************
File "sageinspect.py", line 134:
    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[0]>", line 1, in <module>
        sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)###line 134:
    sage: sage.misc.sageinspect.sage_getargspec(sage.rings.integer.Integer.factor)
      File "/home/was/tmp/sage-1.8/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 154, \
in sage_getargspec
        raise TypeError, 'arg is not a Python or a Sagex function'
    TypeError: arg is not a Python or a Sagex function
**********************************************************************
File "sageinspect.py", line 166:
    sage: sage.misc.sageinspect.sage_getdef(sage.rings.rational.make_rational, obj_name='mr')
Expected:
    'mr(s)'
Got:
    'mr( ... )'
**********************************************************************
**********************************************************************
File "sageinspect.py", line 168:
    sage: sage.misc.sageinspect.sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')
Expected:
    "factor(algorithm='pari')"
Got:
    'factor( ... )'
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/209





---

archive/issue_comments_000935.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-25T07:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/209#issuecomment-935",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000936.json:
```json
{
    "body": "It disappeared with sage-1.8.2.1",
    "created_at": "2007-01-25T07:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/209#issuecomment-936",
    "user": "https://github.com/williamstein"
}
```

It disappeared with sage-1.8.2.1



---

archive/issue_events_000220.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-25T07:08:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/209",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/209#event-220"
}
```
