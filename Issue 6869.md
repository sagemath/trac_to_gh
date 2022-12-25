# Issue 6869: [with patch, needs work] LP and MIP Solvers in Sage ( with symbolics )

archive/issues_006869.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @haraldschilly @wdjoyner mvngu\n\nHello everybody !!!\n\nAfter the work done in #6502 I rewrote the whole class taking into account the fact that some people may want to use this class too, instead of just focusing on the fact I needed it quickly to write Graph-Theoretic functions.\n\nHere is the new numerical.MIP class, using symbolics, I hope sufficiently documented and tested, and everything... Thank you for your help !! This should be the last run ;-)\n\nTo use it, you have to install either GLPK from ticket #6867 or Coin-OR CBC from #6868 ( if you have installed a former version, they won't be compatible ! )\n\nThe class and the doctests, though, should behave peacefully if none of them is installed ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/6869\n\n",
    "created_at": "2009-09-02T17:39:06Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs work] LP and MIP Solvers in Sage ( with symbolics )",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6869",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: jkantor

CC:  @haraldschilly @wdjoyner mvngu

Hello everybody !!!

After the work done in #6502 I rewrote the whole class taking into account the fact that some people may want to use this class too, instead of just focusing on the fact I needed it quickly to write Graph-Theoretic functions.

Here is the new numerical.MIP class, using symbolics, I hope sufficiently documented and tested, and everything... Thank you for your help !! This should be the last run ;-)

To use it, you have to install either GLPK from ticket #6867 or Coin-OR CBC from #6868 ( if you have installed a former version, they won't be compatible ! )

The class and the doctests, though, should behave peacefully if none of them is installed ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/6869





---

archive/issue_comments_056583.json:
```json
{
    "body": "This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).\n\nRunning more tests...",
    "created_at": "2009-09-08T14:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56583",
    "user": "https://github.com/wdjoyner"
}
```

This applies fine to 4.1.2.a0 and passes testall without any other packages installed (no glpk, etc).

Running more tests...



---

archive/issue_comments_056584.json:
```json
{
    "body": "The module `sage/numerical/mip.pyx` should have 100% doctest coverage, given that it's being added to the Sage library:\n\n```\n[mvngu@sage numerical]$ sage -coverage mip.pyx \n----------------------------------------------------------------------\nmip.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE mip.pyx: 62% (18 of 29)\n\nMissing documentation:\n         * __init__(self, value):\n         * __str__(self):\n         * __getitem__(self,i):\n         * keys(self):\n         * items(self):\n         * depth(self):\n         * values(self):\n\n\nMissing doctests:\n         * __init__(self,sense=1):\n         * _NormalForm(self,exp):\n         * _addElementToRing(self):\n         * __init__(self,x,f,dim=1):\n\n----------------------------------------------------------------------\n```\n",
    "created_at": "2009-09-09T12:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The module `sage/numerical/mip.pyx` should have 100% doctest coverage, given that it's being added to the Sage library:

```
[mvngu@sage numerical]$ sage -coverage mip.pyx 
----------------------------------------------------------------------
mip.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE mip.pyx: 62% (18 of 29)

Missing documentation:
         * __init__(self, value):
         * __str__(self):
         * __getitem__(self,i):
         * keys(self):
         * items(self):
         * depth(self):
         * values(self):


Missing doctests:
         * __init__(self,sense=1):
         * _NormalForm(self,exp):
         * _addElementToRing(self):
         * __init__(self,x,f,dim=1):

----------------------------------------------------------------------
```




---

archive/issue_comments_056585.json:
```json
{
    "body": "Done !",
    "created_at": "2009-09-09T17:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56585",
    "user": "https://github.com/nathanncohen"
}
```

Done !



---

archive/issue_comments_056586.json:
```json
{
    "body": "Attachment [MIP-now-symbolic.patch](tarball://root/attachments/some-uuid/ticket6869/MIP-now-symbolic.patch) by @nathanncohen created at 2009-09-09 17:53:08",
    "created_at": "2009-09-09T17:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56586",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [MIP-now-symbolic.patch](tarball://root/attachments/some-uuid/ticket6869/MIP-now-symbolic.patch) by @nathanncohen created at 2009-09-09 17:53:08



---

archive/issue_comments_056587.json:
```json
{
    "body": "ncohen asked this question in IRC:\n\n```\n10:45 < ncohen> mvngu: do you know what this is ?\n10:45 < ncohen> ERROR: Please define a s == loads(dumps(s)) doctest.\n```\n\nThis is encouraging you to define an equality method `__eq__()` for each of the three classes `MIP`, `MIPSolverException`, and `MIPVariable`. Say you have instantiated two objects of the class `MIPVariable`. How can you test to see whether or not they are the same object? In Python, this is usually implemented in the method `__equ__()` of a class. If a class defines this method, you can compare two objects of that class using the double-equal operator `==`. For example:\n\n```\nsage: a1 = AlphabeticStrings()\nsage: a2 = AlphabeticStrings()\nsage: a1 == a2\nTrue\n```\n\nTake the case of writing the method `__eq__()` for the class `MIPVariable`. Are there criteria to tell us that two objects of the class `MIPVariable` are the same? If `m1` and `m2` are two such objects, you can define them to be the same object if their corresponding attributes have the same values. Each object of `MIPVariable` has these attributes: `dim`, `dict`, `x`, `f`. One way to write the `__eq__()` method for `MIPVariable` is this:\n\n```\ndef __eq__(self, other):\n    r\"\"\"\n    <insert lengthy documentation here, with examples>\n    \"\"\"\n    return self.dim == other.dim and self.dict == other.dict and self.x == other.x and self.f == other.f\n```\n\nIn the \"EXAMPLES\" section of that method, you should have an example as follows with appropriate values for `x`, `f`, and `dim`:\n\n```\nsage: m = MIPVariable(someX, someF, someDim)\nsage: m == loads(dumps(m))\nTrue\n```\n\nwhich should return True when you actually doctest the MIP module. Define a similar equality method for the other two classes.\n\n\n\nOne thing I dislike in code is to see it squashed together. This makes it more difficult to read, taking into account also that other people need to understand what that code does, its logical flow, and they might have been spending all day reading code. Good coding style is a plus here if you want your code to be as easily understandable as possible. Instead of doing this:\n\n```\nself.dim=dim \nself.dict={} \nself.x=x \nself.f=f\n```\n\ndo this:\n\n```\nself.dim = dim \nself.dict = {} \nself.x = x \nself.f = f\n```\n\n\n\n\nAnother issue is global namespace pollution. What I mean is that you should try to avoid as much as possible injecting your module, class, or function names into the global namespace when Sage loads itself. This is what you're currently doing with this code:\n\n```\nfrom sage.numerical.mip import *\n```\n\nWhat this means is that when you load Sage, all the class and function names defined in the module mip.pyx are loaded into the global namespace. An advantage to this is that a user doesn't have to first import the relevant class or function prior to using it. With the above import statement, I can do this\n\n```\nsage: m = MIPVariable(x,f)\n```\n\nWithout the import statement, I would need to do this:\n\n```\nsage: from sage.numerical.mip import MIPVariable\nsage: m = MIPVariable(x,f)\n```\n\nI can see that importing stuff when Sage is being loaded saves a lot of time explicitly importing that stuff. But a downside is that the global namespace is being polluted with module, class or function names that are not really necessary to load at the start. As more names are put into the global namespace, it takes longer and longer to load Sage.",
    "created_at": "2009-09-09T18:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56587",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

ncohen asked this question in IRC:

```
10:45 < ncohen> mvngu: do you know what this is ?
10:45 < ncohen> ERROR: Please define a s == loads(dumps(s)) doctest.
```

This is encouraging you to define an equality method `__eq__()` for each of the three classes `MIP`, `MIPSolverException`, and `MIPVariable`. Say you have instantiated two objects of the class `MIPVariable`. How can you test to see whether or not they are the same object? In Python, this is usually implemented in the method `__equ__()` of a class. If a class defines this method, you can compare two objects of that class using the double-equal operator `==`. For example:

```
sage: a1 = AlphabeticStrings()
sage: a2 = AlphabeticStrings()
sage: a1 == a2
True
```

Take the case of writing the method `__eq__()` for the class `MIPVariable`. Are there criteria to tell us that two objects of the class `MIPVariable` are the same? If `m1` and `m2` are two such objects, you can define them to be the same object if their corresponding attributes have the same values. Each object of `MIPVariable` has these attributes: `dim`, `dict`, `x`, `f`. One way to write the `__eq__()` method for `MIPVariable` is this:

```
def __eq__(self, other):
    r"""
    <insert lengthy documentation here, with examples>
    """
    return self.dim == other.dim and self.dict == other.dict and self.x == other.x and self.f == other.f
```

In the "EXAMPLES" section of that method, you should have an example as follows with appropriate values for `x`, `f`, and `dim`:

```
sage: m = MIPVariable(someX, someF, someDim)
sage: m == loads(dumps(m))
True
```

which should return True when you actually doctest the MIP module. Define a similar equality method for the other two classes.



One thing I dislike in code is to see it squashed together. This makes it more difficult to read, taking into account also that other people need to understand what that code does, its logical flow, and they might have been spending all day reading code. Good coding style is a plus here if you want your code to be as easily understandable as possible. Instead of doing this:

```
self.dim=dim 
self.dict={} 
self.x=x 
self.f=f
```

do this:

```
self.dim = dim 
self.dict = {} 
self.x = x 
self.f = f
```




Another issue is global namespace pollution. What I mean is that you should try to avoid as much as possible injecting your module, class, or function names into the global namespace when Sage loads itself. This is what you're currently doing with this code:

```
from sage.numerical.mip import *
```

What this means is that when you load Sage, all the class and function names defined in the module mip.pyx are loaded into the global namespace. An advantage to this is that a user doesn't have to first import the relevant class or function prior to using it. With the above import statement, I can do this

```
sage: m = MIPVariable(x,f)
```

Without the import statement, I would need to do this:

```
sage: from sage.numerical.mip import MIPVariable
sage: m = MIPVariable(x,f)
```

I can see that importing stuff when Sage is being loaded saves a lot of time explicitly importing that stuff. But a downside is that the global namespace is being polluted with module, class or function names that are not really necessary to load at the start. As more names are put into the global namespace, it takes longer and longer to load Sage.



---

archive/issue_comments_056588.json:
```json
{
    "body": "This applies fine to 4.1.2.a0 on an ubuntu 9.04 machine and passes sage -testall (with no packages, eg glpk, applied). The docstrings look fine (as before).\n\nI then applies glpk and reran sage -testall. All tests passes sage -testall except this:\n\n\n```\n\nwdj@tinah:~/sagefiles/sage-4.1.2.alpha0$ ./sage -t  \"devel/sage/sage/server/notebook/cell.py\"\nsage -t  \"devel/sage/sage/server/notebook/cell.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [366.5 s]\nexit code: 1024\n```\n\n\nI doubt this is related, so giving this a positive review.",
    "created_at": "2009-09-09T21:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56588",
    "user": "https://github.com/wdjoyner"
}
```

This applies fine to 4.1.2.a0 on an ubuntu 9.04 machine and passes sage -testall (with no packages, eg glpk, applied). The docstrings look fine (as before).

I then applies glpk and reran sage -testall. All tests passes sage -testall except this:


```

wdj@tinah:~/sagefiles/sage-4.1.2.alpha0$ ./sage -t  "devel/sage/sage/server/notebook/cell.py"
sage -t  "devel/sage/sage/server/notebook/cell.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [366.5 s]
exit code: 1024
```


I doubt this is related, so giving this a positive review.



---

archive/issue_comments_056589.json:
```json
{
    "body": "See #6913 for a follow-up to this ticket. It addresses the issue of writing those `__eq__()` methods.",
    "created_at": "2009-09-10T11:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56589",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6913 for a follow-up to this ticket. It addresses the issue of writing those `__eq__()` methods.



---

archive/issue_events_007101.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-10T11:36:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6869#event-7101"
}
```



---

archive/issue_comments_056590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-10T11:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56590",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056591.json:
```json
{
    "body": "After going through this patch, I think it would be best to revert it before 4.1.2 is released.  There is still a lot of things that need to be done to get it cleaned up.  Some of the things,\n\n1. Almost all of the docstrings are incorrectly formatted.\n\n2. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython.  It just makes Sage slower to compile and things harder to debug.\n\n3. Some of the naming conventions do not match Sage's conventions. (isbinary vs. is_binary).  Also, names like the more explicit MixedIntegerProgram are preferred over the shortened MIP.\n\n4. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk).  This is not the right way to do things and will eventually break.  I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.\n\nI have some code that addresses some of these things that I'll put up shortly.",
    "created_at": "2009-09-25T07:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56591",
    "user": "https://github.com/mwhansen"
}
```

After going through this patch, I think it would be best to revert it before 4.1.2 is released.  There is still a lot of things that need to be done to get it cleaned up.  Some of the things,

1. Almost all of the docstrings are incorrectly formatted.

2. This module should _definitely_ not be a Cython module as it does not gain any benefit from Cython.  It just makes Sage slower to compile and things harder to debug.

3. Some of the naming conventions do not match Sage's conventions. (isbinary vs. is_binary).  Also, names like the more explicit MixedIntegerProgram are preferred over the shortened MIP.

4. The optional spkgs should not install modules into the sage.* namespace (sage.numerical.mipGlpk).  This is not the right way to do things and will eventually break.  I think it also makes sense to use (and contribute to) something like ctypes-glpk to allow greater functionality and not reinvent the wheel.

I have some code that addresses some of these things that I'll put up shortly.



---

archive/issue_comments_056592.json:
```json
{
    "body": "See #7012 for a follow up to this ticket. It addresses mhansen's suggestions.",
    "created_at": "2009-09-25T08:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6869#issuecomment-56592",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #7012 for a follow up to this ticket. It addresses mhansen's suggestions.
