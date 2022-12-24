# Issue 2696: octave -- implement handling of multiple return values of functions

archive/issues_002696.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n\nOn Mon, Mar 24, 2008 at 8:26 AM, Michael <michael.delamaza@gmail.com> wrote:\n> \n>  What is the recommended way to handle Octave functions with multiple\n>  return values in Sage?\n\nI wrote the Sage/Octave interface, but I didn't think of everything.   In particular,\nI completely forgot about multiple return values.    The recommend way to handle\nthem would be to implement something similar to what the Magma interface\ncurrently does, then use that.  :-)\n\n>  Like Magma, Octave functions can return multiple values.  Working with\n>  such Magma functions is documented in the Sage documentation (http://\n>  modular.math.washington.edu/sage/doc/html/ref/node125.html), but I\n>  cannot find similar documentation for Octave.\n>  \n>  Here is how it works in Octave -- foo is a function that returns two\n>  values:\n>  \n>  octave:4> function [a b] = foo() a=1; b=2; endfunction\n>  octave:5> foo()\n>  ans = 1\n>  octave:6> [c,d] = foo()\n>  c = 1\n>  d = 2\n>  \n>  \n>  This code transliterated into Sage is shown below.   What is the\n>  correct way to do this?\n>  \n>  ----------------------------------------------------------------------\n>  | SAGE Version 2.10.3, Release Date: 2008-03-11                      |\n>  | Type notebook() for the GUI, and license() for information.        |\n>  ----------------------------------------------------------------------\n>  \n>  sage: octave.eval(\"function [a b] = foo() a=1; b=2; endfunction\")\n>  ''\n>  sage: octave.foo()\n>   1\n>  sage: [c, d] = octave.foo()\n>  ---------------------------------------------------------------------------\n>  <type 'exceptions.NotImplementedError'>   Traceback (most recent call\n>  last)\n>  \n>  /home/login/<ipython console> in <module>()\n>  \n>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/\n>  expect.py in __iter__(self)\n>    1013\n>    1014     def __iter__(self):\n>  -> 1015         for i in range(1, len(self)+1):\n>    1016             yield self[i]\n>    1017\n>  \n>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/\n>  expect.py in __len__(self)\n>    1017\n>    1018     def __len__(self):\n>  -> 1019         raise NotImplementedError\n>    1020\n>    1021     def __reduce__(self):\n>  \n>  <type 'exceptions.NotImplementedError'>:\n>  sage:\n>  \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2696\n\n",
    "created_at": "2008-03-28T07:05:59Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "octave -- implement handling of multiple return values of functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2696",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```

On Mon, Mar 24, 2008 at 8:26 AM, Michael <michael.delamaza@gmail.com> wrote:
> 
>  What is the recommended way to handle Octave functions with multiple
>  return values in Sage?

I wrote the Sage/Octave interface, but I didn't think of everything.   In particular,
I completely forgot about multiple return values.    The recommend way to handle
them would be to implement something similar to what the Magma interface
currently does, then use that.  :-)

>  Like Magma, Octave functions can return multiple values.  Working with
>  such Magma functions is documented in the Sage documentation (http://
>  modular.math.washington.edu/sage/doc/html/ref/node125.html), but I
>  cannot find similar documentation for Octave.
>  
>  Here is how it works in Octave -- foo is a function that returns two
>  values:
>  
>  octave:4> function [a b] = foo() a=1; b=2; endfunction
>  octave:5> foo()
>  ans = 1
>  octave:6> [c,d] = foo()
>  c = 1
>  d = 2
>  
>  
>  This code transliterated into Sage is shown below.   What is the
>  correct way to do this?
>  
>  ----------------------------------------------------------------------
>  | SAGE Version 2.10.3, Release Date: 2008-03-11                      |
>  | Type notebook() for the GUI, and license() for information.        |
>  ----------------------------------------------------------------------
>  
>  sage: octave.eval("function [a b] = foo() a=1; b=2; endfunction")
>  ''
>  sage: octave.foo()
>   1
>  sage: [c, d] = octave.foo()
>  ---------------------------------------------------------------------------
>  <type 'exceptions.NotImplementedError'>   Traceback (most recent call
>  last)
>  
>  /home/login/<ipython console> in <module>()
>  
>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/
>  expect.py in __iter__(self)
>    1013
>    1014     def __iter__(self):
>  -> 1015         for i in range(1, len(self)+1):
>    1016             yield self[i]
>    1017
>  
>  /usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/
>  expect.py in __len__(self)
>    1017
>    1018     def __len__(self):
>  -> 1019         raise NotImplementedError
>    1020
>    1021     def __reduce__(self):
>  
>  <type 'exceptions.NotImplementedError'>:
>  sage:
>  
```


Issue created by migration from https://trac.sagemath.org/ticket/2696





---

archive/issue_comments_018562.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2696#issuecomment-18562",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018563.json:
```json
{
    "body": "Changing component from interfaces to interfaces: optional.",
    "created_at": "2015-06-23T13:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2696#issuecomment-18563",
    "user": "@jdemeyer"
}
```

Changing component from interfaces to interfaces: optional.



---

archive/issue_comments_018564.json:
```json
{
    "body": "Changing keywords from \"\" to \"octave\".",
    "created_at": "2015-09-16T13:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2696#issuecomment-18564",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "octave".



---

archive/issue_comments_018565.json:
```json
{
    "body": "See also #19502 for a possibly related bug (or possibly not).",
    "created_at": "2015-10-29T19:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2696#issuecomment-18565",
    "user": "@kcrisman"
}
```

See also #19502 for a possibly related bug (or possibly not).
