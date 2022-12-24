# Issue 7681: R pexpect interface seems to keep data around

archive/issues_007681.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  schilly\n\nKeywords: pexpect, interface, R\n\nFor instance:\n\n```\nsage: r.length([1,2,3,4])\n[1] 4\nsage: r.vector('c(1,2,3,4,3)')\n[1] 4\nsage: r.length([1,2,3,4])\n[1] 4\nsage: r.vector('c(1,2,3,4,3)')\n[1] 4\nsage: r.vector('c(1,2,3,4,3)')\n[1] 2\nsage: r.vector('c(1,2,3,4,3)')\n[1] 1 2 3 4 3\nsage: r.vector('c(1,2,3,4,3)')\n[1] 1 2 3 4 3\nsage: r.vector('c(1,2,3,4,3)')\nError: object 'sage49' not found\n```\n\nSomehow the R interface is keeping stuff from previous calls and returning it, and then at some point choking.   Incidentally, in the above session, after trying many other R commands this way and always getting similar errors, all of a sudden \n\n```\n[1] 1 2 3 4 3\n```\n\nshowed up - as the answer to something else!  Where it had been hiding, I can only guess.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7681\n\n",
    "created_at": "2009-12-14T19:43:23Z",
    "labels": [
        "packages",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "R pexpect interface seems to keep data around",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7681",
    "user": "kcrisman"
}
```
Assignee: tbd

CC:  schilly

Keywords: pexpect, interface, R

For instance:

```
sage: r.length([1,2,3,4])
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 4
sage: r.length([1,2,3,4])
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 2
sage: r.vector('c(1,2,3,4,3)')
[1] 1 2 3 4 3
sage: r.vector('c(1,2,3,4,3)')
[1] 1 2 3 4 3
sage: r.vector('c(1,2,3,4,3)')
Error: object 'sage49' not found
```

Somehow the R interface is keeping stuff from previous calls and returning it, and then at some point choking.   Incidentally, in the above session, after trying many other R commands this way and always getting similar errors, all of a sudden 

```
[1] 1 2 3 4 3
```

showed up - as the answer to something else!  Where it had been hiding, I can only guess.

Issue created by migration from https://trac.sagemath.org/ticket/7681





---

archive/issue_comments_065881.json:
```json
{
    "body": "This interface to R (which is entirely different from the rpy2 python module) is rather hard to do and still needs work. I think the problem is that \"vector\" in R does something differently than you imagine. I.e. an error happens which isn't shown and the pexpect interface is confused.\n\n\n```\nsage: x = r.c(1,2,3)\nsage: r.as_vector(x)\n[1] 1 2 3\nsage: r.is_vector(r.as_vector(x))\n[1] TRUE\n```\n\n\nworks for me.\n\nHere what really happens in R:\n\n\n```\n> length(c(1,2,3,4))\n[1] 4\n> vector(c(1,2,3,4,3))\nError in vector(c(1, 2, 3, 4, 3)) : \n  vector: cannot make a vector of mode '1'.\n> as.vector(c(1,2,3,4,3))\n[1] 1 2 3 4 3\n```\n",
    "created_at": "2009-12-14T20:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65881",
    "user": "schilly"
}
```

This interface to R (which is entirely different from the rpy2 python module) is rather hard to do and still needs work. I think the problem is that "vector" in R does something differently than you imagine. I.e. an error happens which isn't shown and the pexpect interface is confused.


```
sage: x = r.c(1,2,3)
sage: r.as_vector(x)
[1] 1 2 3
sage: r.is_vector(r.as_vector(x))
[1] TRUE
```


works for me.

Here what really happens in R:


```
> length(c(1,2,3,4))
[1] 4
> vector(c(1,2,3,4,3))
Error in vector(c(1, 2, 3, 4, 3)) : 
  vector: cannot make a vector of mode '1'.
> as.vector(c(1,2,3,4,3))
[1] 1 2 3 4 3
```




---

archive/issue_comments_065882.json:
```json
{
    "body": "Okay, now I understand this example.  But clearly the error should be shown, correct?  The current behavior is bizarre, and in general this sort of thing happens a lot when trying to use it.\n\nShould we not use the R interface and use rpy2 instead?  But it looks rather more difficult to use, upon a quick perusal of the documentation.",
    "created_at": "2009-12-14T20:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65882",
    "user": "kcrisman"
}
```

Okay, now I understand this example.  But clearly the error should be shown, correct?  The current behavior is bizarre, and in general this sort of thing happens a lot when trying to use it.

Should we not use the R interface and use rpy2 instead?  But it looks rather more difficult to use, upon a quick perusal of the documentation.



---

archive/issue_comments_065883.json:
```json
{
    "body": "And here's just something randomly annoying:\n\n```\nsage: r([1,1/2,1/2])\n[1] 1.0 0.5 0.5\nsage: r([0,sqrt(3)/2,sqrt(3)/2])\nError: object 'sage10' not found\n```\n\nEven though R knows what sqrt(3) is natively:\n\n```\n> sqrt(3)/2\n[1] 0.8660254\n```\n\nI'm not saying this is really related to the summary of the ticket, but it's not unrelated, either.",
    "created_at": "2009-12-14T20:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65883",
    "user": "kcrisman"
}
```

And here's just something randomly annoying:

```
sage: r([1,1/2,1/2])
[1] 1.0 0.5 0.5
sage: r([0,sqrt(3)/2,sqrt(3)/2])
Error: object 'sage10' not found
```

Even though R knows what sqrt(3) is natively:

```
> sqrt(3)/2
[1] 0.8660254
```

I'm not saying this is really related to the summary of the ticket, but it's not unrelated, either.



---

archive/issue_comments_065884.json:
```json
{
    "body": "yes of course, wrong error handling + hickup is bad. these examples might be useful to track down the bug.\n\n[http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html](http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html) might be helpful when using rpy, though...",
    "created_at": "2009-12-14T20:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65884",
    "user": "schilly"
}
```

yes of course, wrong error handling + hickup is bad. these examples might be useful to track down the bug.

[http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html](http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html) might be helpful when using rpy, though...



---

archive/issue_comments_065885.json:
```json
{
    "body": "Changing summary to be more accurate - hopefully fixing this will fix the issues reported.",
    "created_at": "2010-04-20T13:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65885",
    "user": "kcrisman"
}
```

Changing summary to be more accurate - hopefully fixing this will fix the issues reported.



---

archive/issue_comments_065886.json:
```json
{
    "body": "Okay, the problem is that instead of handling errors, we are ignoring them:\n\n```\n        # don't abort on errors, just raise them! \n        # necessary for non-interactive execution\n        self.eval('options(error = expression(NULL))') \n```\n\nBut see [here](http://stat.ethz.ch/R-manual/R-patched/library/base/html/stop.html) - it turns out that this is R's way of just totally ignoring them, not just 'raising' them.  This should be fixed.",
    "created_at": "2010-04-30T16:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65886",
    "user": "kcrisman"
}
```

Okay, the problem is that instead of handling errors, we are ignoring them:

```
        # don't abort on errors, just raise them! 
        # necessary for non-interactive execution
        self.eval('options(error = expression(NULL))') 
```

But see [here](http://stat.ethz.ch/R-manual/R-patched/library/base/html/stop.html) - it turns out that this is R's way of just totally ignoring them, not just 'raising' them.  This should be fixed.



---

archive/issue_comments_065887.json:
```json
{
    "body": "Changing component from packages to interfaces.",
    "created_at": "2010-04-30T16:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65887",
    "user": "kcrisman"
}
```

Changing component from packages to interfaces.



---

archive/issue_comments_065888.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2010-04-30T16:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65888",
    "user": "kcrisman"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_065889.json:
```json
{
    "body": "Changing keywords from \"pexpect, interface, R\" to \"pexpect, interface, R, r-project\".",
    "created_at": "2012-05-21T13:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7681#issuecomment-65889",
    "user": "kcrisman"
}
```

Changing keywords from "pexpect, interface, R" to "pexpect, interface, R, r-project".
