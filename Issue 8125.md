# Issue 8125: problem with "text"

archive/issues_008125.json:
```json
{
    "body": "Assignee: was\n\nIn Sage 4.3.2.alpha0:\n\n```\nsage: text(r\"$\\left(2 a=b\\right)$\", (2,3))   # works fine \nsage: text(r\"$(2 \\, a=b)$\", (2,3))   # works fine \nsage: text(r\"$\\left(2 \\, a=b\\right)$\", (2,3))   # error! \nTraceback (click to the left of this block for traceback) \n... \nAttributeError: 'Kern' object has no attribute 'height' \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8125\n\n",
    "created_at": "2010-01-29T21:09:34Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "problem with \"text\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8125",
    "user": "jhpalmieri"
}
```
Assignee: was

In Sage 4.3.2.alpha0:

```
sage: text(r"$\left(2 a=b\right)$", (2,3))   # works fine 
sage: text(r"$(2 \, a=b)$", (2,3))   # works fine 
sage: text(r"$\left(2 \, a=b\right)$", (2,3))   # error! 
Traceback (click to the left of this block for traceback) 
... 
AttributeError: 'Kern' object has no attribute 'height' 
```



Issue created by migration from https://trac.sagemath.org/ticket/8125





---

archive/issue_comments_071430.json:
```json
{
    "body": "This seems to be a bug in matplotlib; I just reported it to the matplotlib-devel mailing list, and I'll report any answers I get.\n\nMeanwhile, this arises in \"real life\" as follows:\n\n```\nsage: var(\"y R\") \nsage: a(y,R) = pi * (2*R - y) * y \nsage: latex(a(y,R))\n{\\left(2 \\, R - y\\right)} \\pi y\n```\n\nTherefore \n\n```\nsage: lbl = text(r\"$\\int \\  \" + latex(a(y,R)) + \"$\",(3,20)) \n```\n\nwon't work with matplotlib.  Should we get rid of the \"\\,\" in the latex output?",
    "created_at": "2010-01-30T01:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71430",
    "user": "jhpalmieri"
}
```

This seems to be a bug in matplotlib; I just reported it to the matplotlib-devel mailing list, and I'll report any answers I get.

Meanwhile, this arises in "real life" as follows:

```
sage: var("y R") 
sage: a(y,R) = pi * (2*R - y) * y 
sage: latex(a(y,R))
{\left(2 \, R - y\right)} \pi y
```

Therefore 

```
sage: lbl = text(r"$\int \  " + latex(a(y,R)) + "$",(3,20)) 
```

won't work with matplotlib.  Should we get rid of the "\," in the latex output?



---

archive/issue_comments_071431.json:
```json
{
    "body": "Any response?",
    "created_at": "2010-07-27T17:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71431",
    "user": "kcrisman"
}
```

Any response?



---

archive/issue_comments_071432.json:
```json
{
    "body": "No response at all.   From python:\n\n```\n>>> import pylab\n>>> pylab.text(0.2, 0.2, r\"$\\left(2a = b\\right)$\")\n<matplotlib.text.Text object at 0x1020aa450>\n>>> pylab.savefig('a.png')\n>>> pylab.text(0.2, 0.2, r\"$(2a \\, = b)$\")\n<matplotlib.text.Text object at 0x101e22a50>\n>>> pylab.savefig('b.png')\n>>> pylab.text(0.2, 0.2, r\"$\\left(2a \\, = b\\right)$\")\n<matplotlib.text.Text object at 0x1020b5750>\n>>> pylab.savefig('c.png')\nBOOM\n```\n\nCombining `\\left(`, `\\right)}]}, and {{{\\,` seems to lead to problems.  So now what?  Do we get rid of the `\\,`?",
    "created_at": "2010-07-27T17:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71432",
    "user": "jhpalmieri"
}
```

No response at all.   From python:

```
>>> import pylab
>>> pylab.text(0.2, 0.2, r"$\left(2a = b\right)$")
<matplotlib.text.Text object at 0x1020aa450>
>>> pylab.savefig('a.png')
>>> pylab.text(0.2, 0.2, r"$(2a \, = b)$")
<matplotlib.text.Text object at 0x101e22a50>
>>> pylab.savefig('b.png')
>>> pylab.text(0.2, 0.2, r"$\left(2a \, = b\right)$")
<matplotlib.text.Text object at 0x1020b5750>
>>> pylab.savefig('c.png')
BOOM
```

Combining `\left(`, `\right)}]}, and {{{\,` seems to lead to problems.  So now what?  Do we get rid of the `\,`?



---

archive/issue_comments_071433.json:
```json
{
    "body": "Changing keywords from \"\" to \"matplotlib\".",
    "created_at": "2010-10-21T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71433",
    "user": "jhpalmieri"
}
```

Changing keywords from "" to "matplotlib".



---

archive/issue_comments_071434.json:
```json
{
    "body": "This is still an issue in Sage 4.6.alpha3: it has not been fixed in matplotlib 1.0.0.",
    "created_at": "2010-10-21T04:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71434",
    "user": "jhpalmieri"
}
```

This is still an issue in Sage 4.6.alpha3: it has not been fixed in matplotlib 1.0.0.



---

archive/issue_comments_071435.json:
```json
{
    "body": "Fixed by this pull request in matplotlib:\n\n[https://github.com/matplotlib/matplotlib/pull/52](https://github.com/matplotlib/matplotlib/pull/52)\n\nThis will make it into the next matplotlib bugfix release.",
    "created_at": "2011-03-23T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71435",
    "user": "mdboom"
}
```

Fixed by this pull request in matplotlib:

[https://github.com/matplotlib/matplotlib/pull/52](https://github.com/matplotlib/matplotlib/pull/52)

This will make it into the next matplotlib bugfix release.



---

archive/issue_comments_071436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-23T23:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71436",
    "user": "mdboom"
}
```

Resolution: fixed



---

archive/issue_comments_071437.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71437",
    "user": "mhansen"
}
```

Changing status from closed to new.



---

archive/issue_comments_071438.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71438",
    "user": "mhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_071439.json:
```json
{
    "body": "We keep tickets open until the fix has actually gone into a Sage release.",
    "created_at": "2011-03-24T00:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71439",
    "user": "mhansen"
}
```

We keep tickets open until the fix has actually gone into a Sage release.



---

archive/issue_comments_071440.json:
```json
{
    "body": "This works now; it must be in matplotlib 1.1.0 (or earlier).  So this ticket can be closed.",
    "created_at": "2012-03-21T21:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71440",
    "user": "jhpalmieri"
}
```

This works now; it must be in matplotlib 1.1.0 (or earlier).  So this ticket can be closed.



---

archive/issue_comments_071441.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-21T21:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71441",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071442.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-21T21:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71442",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071443.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-04-04T13:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8125#issuecomment-71443",
    "user": "jdemeyer"
}
```

Resolution: worksforme
