# Issue 3980: Find_root bug

archive/issues_003980.json:
```json
{
    "body": "Assignee: jkantor\n\nThe reciprocal of tangent is not a constant function, but Sage says otherwise.  \n\n```\nsage: z=tan\nsage: z\ntan\nsage: 1/z\n1/tan\nsage: find_root(1/z,1,2)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n<snip>\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/numerical/optimize.py in find_root(f, a, b, xtol, rtol, maxiter, full_output)\n     52     \"\"\"\n     53     try:\n---> 54         return f.find_root(a=a,b=b,xtol=xtol,rtol=rtol,maxiter=maxiter,full_output=full_output)\n     55     except AttributeError:\n     56         pass\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in find_root(self, a, b, var, xtol, rtol, maxiter, full_output)\n   3088                     return a\n   3089                 else:\n-> 3090                     raise RuntimeError, \"no zero in the interval, since constant expression is not 0.\"\n   3091             var = repr(w[0])\n   3092 \n\nRuntimeError: no zero in the interval, since constant expression is not 0.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3980\n\n",
    "created_at": "2008-08-28T20:38:30Z",
    "labels": [
        "component: numerical",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Find_root bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3980",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jkantor

The reciprocal of tangent is not a constant function, but Sage says otherwise.  

```
sage: z=tan
sage: z
tan
sage: 1/z
1/tan
sage: find_root(1/z,1,2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

<snip>

/Applications/sage/local/lib/python2.5/site-packages/sage/numerical/optimize.py in find_root(f, a, b, xtol, rtol, maxiter, full_output)
     52     """
     53     try:
---> 54         return f.find_root(a=a,b=b,xtol=xtol,rtol=rtol,maxiter=maxiter,full_output=full_output)
     55     except AttributeError:
     56         pass

/Applications/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in find_root(self, a, b, var, xtol, rtol, maxiter, full_output)
   3088                     return a
   3089                 else:
-> 3090                     raise RuntimeError, "no zero in the interval, since constant expression is not 0."
   3091             var = repr(w[0])
   3092 

RuntimeError: no zero in the interval, since constant expression is not 0.
```


Issue created by migration from https://trac.sagemath.org/ticket/3980





---

archive/issue_comments_028565.json:
```json
{
    "body": "Changing assignee from jkantor to @burcin.",
    "created_at": "2008-08-31T15:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28565",
    "user": "https://github.com/jicama"
}
```

Changing assignee from jkantor to @burcin.



---

archive/issue_comments_028566.json:
```json
{
    "body": "Changing component from numerical to calculus.",
    "created_at": "2008-08-31T15:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28566",
    "user": "https://github.com/jicama"
}
```

Changing component from numerical to calculus.



---

archive/issue_comments_028567.json:
```json
{
    "body": "I have a less obscure example of this.  \n\n```\nsage: find_root(sin, -1, 1)\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Volumes/Place/anakha/sage-3.1.2.alpha4/<ipython console> in <module>()\n\n/Volumes/Place/anakha/sage-3.1.2.alpha4/local/lib/python2.5/site-packages/sage/numerical/optimize.py in find_root(f, a, b, xtol, rtol, maxiter, full_output)\n     52     \"\"\"\n     53     try:\n---> 54         return f.find_root(a=a,b=b,xtol=xtol,rtol=rtol,maxiter=maxiter,full_output=full_output)\n     55     except AttributeError:\n     56         pass\n\n/Volumes/Place/anakha/sage-3.1.2.alpha4/local/lib/python2.5/site-packages/sage/calculus/calculus.py in find_root(self, a, b, var, xtol, rtol, maxiter, full_output)\n   3120                     return a\n   3121                 else:\n-> 3122                     raise RuntimeError, \"no zero in the interval, since constant expression is not 0.\"\n   3123             var = repr(w[0])\n   3124 \n\nRuntimeError: no zero in the interval, since constant expression is not 0.\n```\n\nAnd I have traced down the bug to this:\n\n```\nsage: sin.variables()\n()\nsage: (1/tan).variables()\n()\n```\n\nSince these expressions contain no variables they are deemed constant and since they are not equal to 0 they have no roots.  You can fix your example by trying:\n\n```\nsage: find_root(1/tan(x), 1, 2)\n1.5707963267948968\n```\n\nAlso note that this works:\n\n```\nsage: (1/tan)(1)\n1/tan(1)\n```\n\nAlthough, technically no variables are there to be replaced.\n\nI don't know if this is really a bug or not, or how to fix it.",
    "created_at": "2008-09-08T20:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28567",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

I have a less obscure example of this.  

```
sage: find_root(sin, -1, 1)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Volumes/Place/anakha/sage-3.1.2.alpha4/<ipython console> in <module>()

/Volumes/Place/anakha/sage-3.1.2.alpha4/local/lib/python2.5/site-packages/sage/numerical/optimize.py in find_root(f, a, b, xtol, rtol, maxiter, full_output)
     52     """
     53     try:
---> 54         return f.find_root(a=a,b=b,xtol=xtol,rtol=rtol,maxiter=maxiter,full_output=full_output)
     55     except AttributeError:
     56         pass

/Volumes/Place/anakha/sage-3.1.2.alpha4/local/lib/python2.5/site-packages/sage/calculus/calculus.py in find_root(self, a, b, var, xtol, rtol, maxiter, full_output)
   3120                     return a
   3121                 else:
-> 3122                     raise RuntimeError, "no zero in the interval, since constant expression is not 0."
   3123             var = repr(w[0])
   3124 

RuntimeError: no zero in the interval, since constant expression is not 0.
```

And I have traced down the bug to this:

```
sage: sin.variables()
()
sage: (1/tan).variables()
()
```

Since these expressions contain no variables they are deemed constant and since they are not equal to 0 they have no roots.  You can fix your example by trying:

```
sage: find_root(1/tan(x), 1, 2)
1.5707963267948968
```

Also note that this works:

```
sage: (1/tan)(1)
1/tan(1)
```

Although, technically no variables are there to be replaced.

I don't know if this is really a bug or not, or how to fix it.



---

archive/issue_comments_028568.json:
```json
{
    "body": "The problem is that find_root is asking the wrong question of its first argument.  It asks \"what are your variables?\"  Instead, it should ask \"do you return a number when called with one argument?\"  I will try to code this up when I get a chance.",
    "created_at": "2008-09-08T22:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28568",
    "user": "https://github.com/jicama"
}
```

The problem is that find_root is asking the wrong question of its first argument.  It asks "what are your variables?"  Instead, it should ask "do you return a number when called with one argument?"  I will try to code this up when I get a chance.



---

archive/issue_comments_028569.json:
```json
{
    "body": "Here's a patch that avoids asking the function what it's variables are.",
    "created_at": "2008-09-09T02:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28569",
    "user": "https://github.com/jicama"
}
```

Here's a patch that avoids asking the function what it's variables are.



---

archive/issue_comments_028570.json:
```json
{
    "body": "Changing assignee from @burcin to @jicama.",
    "created_at": "2008-09-09T02:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28570",
    "user": "https://github.com/jicama"
}
```

Changing assignee from @burcin to @jicama.



---

archive/issue_comments_028571.json:
```json
{
    "body": "Somehow this is now too permissive, since the following should return an error:\n\n```\nsage: var('t')\nsage: find_root(1/t-x,0,2)\n     1.0000000000005\n```",
    "created_at": "2008-09-21T03:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28571",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Somehow this is now too permissive, since the following should return an error:

```
sage: var('t')
sage: find_root(1/t-x,0,2)
     1.0000000000005
```



---

archive/issue_comments_028572.json:
```json
{
    "body": "Attachment [3980.patch](tarball://root/attachments/some-uuid/ticket3980/3980.patch) by @jicama created at 2008-09-29 23:26:41",
    "created_at": "2008-09-29T23:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28572",
    "user": "https://github.com/jicama"
}
```

Attachment [3980.patch](tarball://root/attachments/some-uuid/ticket3980/3980.patch) by @jicama created at 2008-09-29 23:26:41



---

archive/issue_comments_028573.json:
```json
{
    "body": "Good catch mhampton.  I modified the patch to throw a NotImplementedError if self.number_of_variables() is greater than 1.  This is closer to the old behavior.  I added a new test to explicitly check the case you gave above.",
    "created_at": "2008-09-29T23:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28573",
    "user": "https://github.com/jicama"
}
```

Good catch mhampton.  I modified the patch to throw a NotImplementedError if self.number_of_variables() is greater than 1.  This is closer to the old behavior.  I added a new test to explicitly check the case you gave above.



---

archive/issue_comments_028574.json:
```json
{
    "body": "OK, this passes tests and it seems OK.  One thing I noticed, which I think can be considered beyond the scope of this patch, is that \n\n\n```\nvar('t')\nplot(sin(t*x),-1,1)\n```\nquickly fails with \"ValueError: free variable: x\", which is good, but:\n\n```\nplot(lambda t: sin(t*x),-1,1)\n```\ntries to plot 400 values and finally gives \n\n```\nverbose 0 (3585: plot.py, _plot) WARNING: When plotting, failed to evaluate function at 400 points.\nverbose 0 (3585: plot.py, _plot) Last error message: 'float() argument must be a string or a number'\n```\nand an empty plot.  It would be nice to speed up that failure if you know an easy way.",
    "created_at": "2008-10-01T01:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, this passes tests and it seems OK.  One thing I noticed, which I think can be considered beyond the scope of this patch, is that 


```
var('t')
plot(sin(t*x),-1,1)
```
quickly fails with "ValueError: free variable: x", which is good, but:

```
plot(lambda t: sin(t*x),-1,1)
```
tries to plot 400 values and finally gives 

```
verbose 0 (3585: plot.py, _plot) WARNING: When plotting, failed to evaluate function at 400 points.
verbose 0 (3585: plot.py, _plot) Last error message: 'float() argument must be a string or a number'
```
and an empty plot.  It would be nice to speed up that failure if you know an easy way.



---

archive/issue_events_009117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-01T10:32:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3980#event-9117"
}
```



---

archive/issue_comments_028575.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3.",
    "created_at": "2008-10-01T10:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3.



---

archive/issue_comments_028576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-01T10:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3980#issuecomment-28576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-01T10:32:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3980",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3980#event-9118"
}
```
