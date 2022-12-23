# Issue 1938: Fast (double) function evaluation for plotting, etc.

archive/issues_001938.json:
```json
{
    "body": "Assignee: somebody\n\nWhen one wishes to plot a 3d surface, one ends up evaluating one or more algebraic expressions several hundreds of times. This is especially slow if maxima is involved via the calculus package. Up until now the solution has been to plot lambda expressions, but this is neither intuitive, Sage-like, nor efficient (compared to operating on raw c doubles).\n\nWe need a way to get a quick-to-evaluate version of a symbolic expression (polynomial, ...) I would imagine this would be useful for optimization problems and simulations as well. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1938\n\n",
    "created_at": "2008-01-26T12:11:19Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Fast (double) function evaluation for plotting, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1938",
    "user": "robertwb"
}
```
Assignee: somebody

When one wishes to plot a 3d surface, one ends up evaluating one or more algebraic expressions several hundreds of times. This is especially slow if maxima is involved via the calculus package. Up until now the solution has been to plot lambda expressions, but this is neither intuitive, Sage-like, nor efficient (compared to operating on raw c doubles).

We need a way to get a quick-to-evaluate version of a symbolic expression (polynomial, ...) I would imagine this would be useful for optimization problems and simulations as well. 

Issue created by migration from https://trac.sagemath.org/ticket/1938





---

archive/issue_comments_012288.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-26T12:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12288",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012289.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2008-01-26T12:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12289",
    "user": "robertwb"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_012290.json:
```json
{
    "body": "Attachment\n\nThe attached bundle builds on and includes #1828 and #1862.",
    "created_at": "2008-01-26T12:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12290",
    "user": "robertwb"
}
```

Attachment

The attached bundle builds on and includes #1828 and #1862.



---

archive/issue_comments_012291.json:
```json
{
    "body": "Hi Robert, \n\nthe patch looks very nice, but I am seeing a massive number of merge conflict against 2.10.1.rc0. Could you take \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/sage-2.10.1.rc0.tar\n\nand rebase the patch? There have been a lot of tricky merges in the plotting code in 2.10.1.x, so it isn't really a surprise that there are problems :(\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T14:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12291",
    "user": "mabshoff"
}
```

Hi Robert, 

the patch looks very nice, but I am seeing a massive number of merge conflict against 2.10.1.rc0. Could you take 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/sage-2.10.1.rc0.tar

and rebase the patch? There have been a lot of tricky merges in the plotting code in 2.10.1.x, so it isn't really a surprise that there are problems :(

Cheers,

Michael



---

archive/issue_comments_012292.json:
```json
{
    "body": "Sure, I'll re-base it. \n\nIs there a repo I could -upgrade from rather than re-building the whole thing from source?",
    "created_at": "2008-01-26T19:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12292",
    "user": "robertwb"
}
```

Sure, I'll re-base it. 

Is there a repo I could -upgrade from rather than re-building the whole thing from source?



---

archive/issue_comments_012293.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Sure, I'll re-base it. \n> \n> Is there a repo I could -upgrade from rather than re-building the whole thing from source? \n\nNope, but it has been suggested a couple time to create a devel repo somewhere on sagemath.org to offer such a way to testbuild. I also saw that R failed to build for you on OSX 10.4 - I am building rc0 now on a 10.4 box to fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T22:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12293",
    "user": "mabshoff"
}
```

Replying to [comment:4 robertwb]:
> Sure, I'll re-base it. 
> 
> Is there a repo I could -upgrade from rather than re-building the whole thing from source? 

Nope, but it has been suggested a couple time to create a devel repo somewhere on sagemath.org to offer such a way to testbuild. I also saw that R failed to build for you on OSX 10.4 - I am building rc0 now on a 10.4 box to fix the issue.

Cheers,

Michael



---

archive/issue_comments_012294.json:
```json
{
    "body": "Here's some timings:\n\n\n```\nsage: f(x,y,z) = sin(z)/(1+x^2+y^2)\nsage: lambda_f = lambda x,y,z: math.sin(z)/(1+x^2+y^2)\nsage: fast_f = f._fast_float_('x','y','z')\n\nsage: sage: A = range(50000)\nsage: sage: time for _ in A: r = f(1.0r, 2.0r, 3.0r)\nCPU times: user 12.47 s, sys: 0.08 s, total: 12.54 s\nWall time: 12.73\n\nsage: sage: time for _ in A: r = lambda_f(1.0r, 2.0r, 3.0r)\nCPU times: user 1.32 s, sys: 0.01 s, total: 1.33 s\nWall time: 1.37\n\nsage: sage: time for _ in A: r = fast_f(1.0r, 2.0r, 3.0r)\nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.04\n```\n",
    "created_at": "2008-01-26T23:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12294",
    "user": "robertwb"
}
```

Here's some timings:


```
sage: f(x,y,z) = sin(z)/(1+x^2+y^2)
sage: lambda_f = lambda x,y,z: math.sin(z)/(1+x^2+y^2)
sage: fast_f = f._fast_float_('x','y','z')

sage: sage: A = range(50000)
sage: sage: time for _ in A: r = f(1.0r, 2.0r, 3.0r)
CPU times: user 12.47 s, sys: 0.08 s, total: 12.54 s
Wall time: 12.73

sage: sage: time for _ in A: r = lambda_f(1.0r, 2.0r, 3.0r)
CPU times: user 1.32 s, sys: 0.01 s, total: 1.33 s
Wall time: 1.37

sage: sage: time for _ in A: r = fast_f(1.0r, 2.0r, 3.0r)
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04
```




---

archive/issue_comments_012295.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-27T10:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12295",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_012296.json:
```json
{
    "body": "The bundle just attached is merged with the plotting code of 2.10.1.rc0. Since William Stein was the other one who worked in this area, he should probably take a look at this as well to make sure I didn't regress anything.",
    "created_at": "2008-01-27T11:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12296",
    "user": "robertwb"
}
```

The bundle just attached is merged with the plotting code of 2.10.1.rc0. Since William Stein was the other one who worked in this area, he should probably take a look at this as well to make sure I didn't regress anything.



---

archive/issue_comments_012297.json:
```json
{
    "body": "Wow, this is amazing compared to before!!!!!!!!!!!!!!!!!  Wow!  This is an awesome patch full of beautiful code.   It will have a major impact on how the calculus code is used in the future, and make things like numerical integration, ode's, etc. way way way faster. \n\nrefereeing:\n\n* The the file morphism.pyx there are a bunch of print statements that shouldn't be there.  They must have been for debugging purposes:\n\n```\n    cdef Element _call_c_impl(self, Element x):\n        print type(self), self\n        print <long>self._call_c\n        print <long>Morphism._call_c\n        print <long>FormalCoercionMorphism._call_c\n        raise NotImplementedError\n\n```\n\n\n* More doctests are needed, e.g., L3096 of calculus.py, has two functions without doctests:\n\n```\n    def fast_float_function(self, vars):\n        return self._fast_float_(vars)\n\n    def _fast_float_(self, *vars):\n        try:\n```\n\n\n* Is ext/ really the right place for fast_eval.pyx?  Maybe.  I'm just not sure...\n\n* I wish there were a few sentences at the top of fast_eval.pyx about what it does. \n\n* There's still a lot in fast_eval.pyx that needs doctests; it's coverage score is only 14%:\n\n```\nteragon:ext was$ sage -coverage fast_eval.pyx\n----------------------------------------------------------------------\nfast_eval.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE fast_eval.pyx: 14% (6 of 41)\n```\n\n\n* This code in fast_eval.pyx is clearly TOTALLY WRONG and would give an infinite loop if it were actually tested: \n\n```\n+    def sec(self):\n+        return ~self.sec()   \n```\n\n\n   \n\nOtherwise it looks good to me.   Fix the above then this patch should get marked with \"positive review\"",
    "created_at": "2008-01-27T16:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12297",
    "user": "was"
}
```

Wow, this is amazing compared to before!!!!!!!!!!!!!!!!!  Wow!  This is an awesome patch full of beautiful code.   It will have a major impact on how the calculus code is used in the future, and make things like numerical integration, ode's, etc. way way way faster. 

refereeing:

* The the file morphism.pyx there are a bunch of print statements that shouldn't be there.  They must have been for debugging purposes:

```
    cdef Element _call_c_impl(self, Element x):
        print type(self), self
        print <long>self._call_c
        print <long>Morphism._call_c
        print <long>FormalCoercionMorphism._call_c
        raise NotImplementedError

```


* More doctests are needed, e.g., L3096 of calculus.py, has two functions without doctests:

```
    def fast_float_function(self, vars):
        return self._fast_float_(vars)

    def _fast_float_(self, *vars):
        try:
```


* Is ext/ really the right place for fast_eval.pyx?  Maybe.  I'm just not sure...

* I wish there were a few sentences at the top of fast_eval.pyx about what it does. 

* There's still a lot in fast_eval.pyx that needs doctests; it's coverage score is only 14%:

```
teragon:ext was$ sage -coverage fast_eval.pyx
----------------------------------------------------------------------
fast_eval.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE fast_eval.pyx: 14% (6 of 41)
```


* This code in fast_eval.pyx is clearly TOTALLY WRONG and would give an infinite loop if it were actually tested: 

```
+    def sec(self):
+        return ~self.sec()   
```


   

Otherwise it looks good to me.   Fix the above then this patch should get marked with "positive review"



---

archive/issue_comments_012298.json:
```json
{
    "body": "OK, I have fixed all the above issues, and added lots more documentation. As for placing it in sage/ext, I'm not sure but I can't think of another place that would be better. \n\nThe most recently attached bundle contains everything.",
    "created_at": "2008-01-29T10:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12298",
    "user": "robertwb"
}
```

OK, I have fixed all the above issues, and added lots more documentation. As for placing it in sage/ext, I'm not sure but I can't think of another place that would be better. 

The most recently attached bundle contains everything.



---

archive/issue_comments_012299.json:
```json
{
    "body": "Attachment\n\nThere are still doctest failures in fast_eval.pyx.  Otherwise this patch is good.\nI've posted a .patch that fixes most of those failures, plus a bunch of roughness in the paragraphs at the top.  But there are three failing doctests left.  Please fix and then this patch will be ready to go.\n\n -- William",
    "created_at": "2008-01-29T13:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12299",
    "user": "was"
}
```

Attachment

There are still doctest failures in fast_eval.pyx.  Otherwise this patch is good.
I've posted a .patch that fixes most of those failures, plus a bunch of roughness in the paragraphs at the top.  But there are three failing doctests left.  Please fix and then this patch will be ready to go.

 -- William



---

archive/issue_comments_012300.json:
```json
{
    "body": "Do not apply the above patch last patch--everything passes on my computer including the lines \n\n\n```\nsage: list(h)\n['push 1.5', 'load 0', 'add', 'call sin(1)']\n```\n\n\ninstead of \n\n\n\n```\nsage: list(h)\n['push 1.5', 'load 0', 'add', 'call 1 0x942acc20']\n```\n\n\nIt looks like you didn't do a sage -b after applying merging the changes.",
    "created_at": "2008-01-29T18:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12300",
    "user": "robertwb"
}
```

Do not apply the above patch last patch--everything passes on my computer including the lines 


```
sage: list(h)
['push 1.5', 'load 0', 'add', 'call sin(1)']
```


instead of 



```
sage: list(h)
['push 1.5', 'load 0', 'add', 'call 1 0x942acc20']
```


It looks like you didn't do a sage -b after applying merging the changes.



---

archive/issue_comments_012301.json:
```json
{
    "body": "do apply this",
    "created_at": "2008-01-30T03:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12301",
    "user": "was"
}
```

do apply this



---

archive/issue_comments_012302.json:
```json
{
    "body": "Attachment\n\nYou're right -- I didn't \"sage -br\" after the merge.  I redid the last patch, with a few fixes to typos and the writing in the paragraph, but without changing any doctests.",
    "created_at": "2008-01-30T03:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12302",
    "user": "was"
}
```

Attachment

You're right -- I didn't "sage -br" after the merge.  I redid the last patch, with a few fixes to typos and the writing in the paragraph, but without changing any doctests.



---

archive/issue_comments_012303.json:
```json
{
    "body": "This is now good to go, I think.  Very nice.",
    "created_at": "2008-01-30T03:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12303",
    "user": "was"
}
```

This is now good to go, I think.  Very nice.



---

archive/issue_comments_012304.json:
```json
{
    "body": "Yes, the documentation fixes are from the new patch should be applied. Thanks.",
    "created_at": "2008-01-30T03:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12304",
    "user": "robertwb"
}
```

Yes, the documentation fixes are from the new patch should be applied. Thanks.



---

archive/issue_comments_012305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T09:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12305",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012306.json:
```json
{
    "body": "Merged 1938-fast-float-fixes.hg and trac-1938-fix_some_docstrings.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T09:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1938#issuecomment-12306",
    "user": "mabshoff"
}
```

Merged 1938-fast-float-fixes.hg and trac-1938-fix_some_docstrings.patch in Sage 2.10.1.rc3
