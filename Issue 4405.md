# Issue 4405: double/single quotation marks in docstring

archive/issues_004405.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @kcrisman\n\nKeywords: docstring, triple ''', triple \"\"\"\n\nAt this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/1dc6a340db91e7ac) thread, kcrisman reported the following problem with single quotation marks in docstring:\n\n```\nI came across some very strange behavior recently regarding docstrings\nin functions.  In the notebook in 3.2.alpha0 and 3.0.6, putting an\napostrophe in the docstring causes various bugs.  It doesn't have to\nbe in any particular spot, as far as I can tell; in fact, it took a\nlong time to pinpoint this as the source of the problem!\n\nMore precisely, it seems to cause the preparser to turn off or\nsomething, because it disallows the following (in the function\ndefinition):\nf(x)=x^3\nbecause of the f(x), and\nf=x^3\nbecause of the ^ used instead of ** (the error message for the first\nis very mysterious at times, but the second one is always clear when\nyou try to use the function).\n\nI can post a link to a worksheet if it's really necessary, but\nhopefully this will be enough for someone to help.  I checked Sage and\nPython docs about documentation strings, but couldn't find anything\nabout it being bad to have apostrophes; in fact, some Sage docstrings\nhave them (e.g. for declaring variables).  I didn't try this in the\ncommand line, so it is possible it's only a notebook issue.\n```\n\nSome basic experimentation reveals that it's likely to be caused by the use of single quotation marks in docstring from within the console and notebook. However, the reported error as described by kcrisman seems to go away when double quotation marks are used instead of single quotation marks:\n\n```\nOK, here's my experimentation from within the console sage-3.1.4, x86\nmachine, Debian 5.0 Lenny (testing):\n\nYep, I received a similar error as you described:\n\nsage: def foo():\n....:     '''\n....:     What's up with this? x^3\n....:     '''\n....:     f(x) = x^3\n------------------------------------------------------------\n  File \"<ipython console>\", line 5\nSyntaxError: can't assign to function call (<ipython console>, line 5)\n\nJohn's suggestion about replacing the ''' with r''' results in the same error:\n\nsage: def foo():\n....:     r'''\n....:     What's up with this? x^3\n....:     '''\n....:     f(x) = x^3\n------------------------------------------------------------\n  File \"<ipython console>\", line 5\nSyntaxError: can't assign to function call (<ipython console>, line 5)\n\nAs Simon has said, the error seems to go away when I used triple \"\n(double quotation mark, not single quotation mark), which I normally\ndo anyway whenever I write docstring. But using triple ''' with or\nwithout the leading r, and with or without the question mark, resulted\nin a siimilar error:\n\nsage: def foo():\n....:     '''\n....:     What's up with this? x^3\n....:     '''\n....:     f(x) = x^3\n------------------------------------------------------------\n  File \"<ipython console>\", line 5\nSyntaxError: can't assign to function call (<ipython console>, line 5)\n\nsage: def foo():\n....:     r'''\n....:     What's up here x^3\n....:     '''\n....:     f(x) = x^3\n------------------------------------------------------------\n  File \"<ipython console>\", line 5\nSyntaxError: can't assign to function call (<ipython console>, line 5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4405\n\n",
    "created_at": "2008-10-30T19:39:30Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "double/single quotation marks in docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4405",
    "user": "mvngu"
}
```
Assignee: tba

CC:  @kcrisman

Keywords: docstring, triple ''', triple """

At this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/1dc6a340db91e7ac) thread, kcrisman reported the following problem with single quotation marks in docstring:

```
I came across some very strange behavior recently regarding docstrings
in functions.  In the notebook in 3.2.alpha0 and 3.0.6, putting an
apostrophe in the docstring causes various bugs.  It doesn't have to
be in any particular spot, as far as I can tell; in fact, it took a
long time to pinpoint this as the source of the problem!

More precisely, it seems to cause the preparser to turn off or
something, because it disallows the following (in the function
definition):
f(x)=x^3
because of the f(x), and
f=x^3
because of the ^ used instead of ** (the error message for the first
is very mysterious at times, but the second one is always clear when
you try to use the function).

I can post a link to a worksheet if it's really necessary, but
hopefully this will be enough for someone to help.  I checked Sage and
Python docs about documentation strings, but couldn't find anything
about it being bad to have apostrophes; in fact, some Sage docstrings
have them (e.g. for declaring variables).  I didn't try this in the
command line, so it is possible it's only a notebook issue.
```

Some basic experimentation reveals that it's likely to be caused by the use of single quotation marks in docstring from within the console and notebook. However, the reported error as described by kcrisman seems to go away when double quotation marks are used instead of single quotation marks:

```
OK, here's my experimentation from within the console sage-3.1.4, x86
machine, Debian 5.0 Lenny (testing):

Yep, I received a similar error as you described:

sage: def foo():
....:     '''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

John's suggestion about replacing the ''' with r''' results in the same error:

sage: def foo():
....:     r'''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

As Simon has said, the error seems to go away when I used triple "
(double quotation mark, not single quotation mark), which I normally
do anyway whenever I write docstring. But using triple ''' with or
without the leading r, and with or without the question mark, resulted
in a siimilar error:

sage: def foo():
....:     '''
....:     What's up with this? x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)

sage: def foo():
....:     r'''
....:     What's up here x^3
....:     '''
....:     f(x) = x^3
------------------------------------------------------------
  File "<ipython console>", line 5
SyntaxError: can't assign to function call (<ipython console>, line 5)
```


Issue created by migration from https://trac.sagemath.org/ticket/4405





---

archive/issue_comments_032389.json:
```json
{
    "body": "The following seems to show that Sage parsing is bypassed, in some way, when using single-quote marks for docstrings.\n\n\n```\nsage: def foo(x):\n   ....:     \"\"\"\n   ....:     it's a comment.\n   ....:     \"\"\"\n   ....:     return x^2\n   ....: \nsage: foo(3)\n9\nsage: def foo(x):\n   ....:     '''\n   ....:     It's a comment.\n   ....:     '''\n   ....:     return x^2\n   ....: \nsage: foo(3)\n1\n```\n\nIn the first case, \"!^\" is exponentiation; in the second, XOR.",
    "created_at": "2008-10-31T20:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32389",
    "user": "justin"
}
```

The following seems to show that Sage parsing is bypassed, in some way, when using single-quote marks for docstrings.


```
sage: def foo(x):
   ....:     """
   ....:     it's a comment.
   ....:     """
   ....:     return x^2
   ....: 
sage: foo(3)
9
sage: def foo(x):
   ....:     '''
   ....:     It's a comment.
   ....:     '''
   ....:     return x^2
   ....: 
sage: foo(3)
1
```

In the first case, "!^" is exponentiation; in the second, XOR.



---

archive/issue_comments_032390.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T13:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32390",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032391.json:
```json
{
    "body": "Attachment [trac_4405.patch](tarball://root/attachments/some-uuid/ticket4405/trac_4405.patch) by @mwhansen created at 2009-01-23 13:13:13",
    "created_at": "2009-01-23T13:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32391",
    "user": "@mwhansen"
}
```

Attachment [trac_4405.patch](tarball://root/attachments/some-uuid/ticket4405/trac_4405.patch) by @mwhansen created at 2009-01-23 13:13:13



---

archive/issue_comments_032392.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-01-23T13:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32392",
    "user": "@mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_032393.json:
```json
{
    "body": "Note that this depends on #3752.",
    "created_at": "2009-01-24T02:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32393",
    "user": "@mwhansen"
}
```

Note that this depends on #3752.



---

archive/issue_comments_032394.json:
```json
{
    "body": "patch looks good, doctests pass.",
    "created_at": "2009-01-24T07:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32394",
    "user": "@malb"
}
```

patch looks good, doctests pass.



---

archive/issue_comments_032395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32395",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032396.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4405#issuecomment-32396",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael
