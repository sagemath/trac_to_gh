# Issue 920: integrate doesn't handle divergent case correctly

archive/issues_000920.json:
```json
{
    "body": "Assignee: was\n\nThe following integral should be divergent, but sage (and maxima?) gives an answer.\n\nsage: integrate(1/x^3,x,-1,3)\n4/9\nsage: version()\n'SAGE Version 2.8.7, Release Date: 2007-10-15'\n\nIssue created by migration from https://trac.sagemath.org/ticket/920\n\n",
    "created_at": "2007-10-18T17:18:07Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "integrate doesn't handle divergent case correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/920",
    "user": "jason"
}
```
Assignee: was

The following integral should be divergent, but sage (and maxima?) gives an answer.

sage: integrate(1/x^3,x,-1,3)
4/9
sage: version()
'SAGE Version 2.8.7, Release Date: 2007-10-15'

Issue created by migration from https://trac.sagemath.org/ticket/920





---

archive/issue_comments_005638.json:
```json
{
    "body": "That's supposed to say:\n\n\n```\nsage: integrate(1/x^3,x,-1,3) \n4/9 \nsage: version() \n'SAGE Version 2.8.7, Release Date: 2007-10-15' \n```\n",
    "created_at": "2007-10-18T17:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5638",
    "user": "jason"
}
```

That's supposed to say:


```
sage: integrate(1/x^3,x,-1,3) 
4/9 
sage: version() 
'SAGE Version 2.8.7, Release Date: 2007-10-15' 
```




---

archive/issue_comments_005639.json:
```json
{
    "body": "This is due to Maxima:\n\n```\n(%i3) integrate(1/x^3,x,-1,3);\nPrincipal Value                                       4\n(%o3)                                  -\n                                       9\n\n```\n\n\nI'm not quite sure what to do about it at the moment.",
    "created_at": "2007-10-18T21:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5639",
    "user": "mhansen"
}
```

This is due to Maxima:

```
(%i3) integrate(1/x^3,x,-1,3);
Principal Value                                       4
(%o3)                                  -
                                       9

```


I'm not quite sure what to do about it at the moment.



---

archive/issue_comments_005640.json:
```json
{
    "body": "I've attached a patch which makes \"Principal Value\" output in Maxima raise an error so that sage does not return the wrong answer.  Here is the behavior after the patch.\n\n\n```\nsage: integrate(1/x^3,x,-1,3)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/opt/sage/devel/sage-calc/sage/calculus/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)\n    175         return f.integral(*args, **kwds)\n    176     except ValueError, err:\n--> 177         raise err\n    178     except AttributeError:\n    179         pass\n\n<type 'exceptions.ValueError'>: Integral is divergent.\n```\n\n\nThis patch should be applied after the patch for #921 is applied.",
    "created_at": "2007-10-24T00:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5640",
    "user": "mhansen"
}
```

I've attached a patch which makes "Principal Value" output in Maxima raise an error so that sage does not return the wrong answer.  Here is the behavior after the patch.


```
sage: integrate(1/x^3,x,-1,3)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage/devel/sage-calc/sage/calculus/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    175         return f.integral(*args, **kwds)
    176     except ValueError, err:
--> 177         raise err
    178     except AttributeError:
    179         pass

<type 'exceptions.ValueError'>: Integral is divergent.
```


This patch should be applied after the patch for #921 is applied.



---

archive/issue_comments_005641.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T00:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5641",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005642.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-10-24T00:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5642",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_005643.json:
```json
{
    "body": "Looks, good though:\n\n```\n19:15 < wstein> re: 920.  I've never seen a line like this before:\n19:15 < wstein> if \"divergent\" in s or 'Principal Value': \n19:16 < wstein> It actually works as claimed.\n19:16 < wstein> It's surprising to me that it is equivalent to: if \"divergent\" in (s + 'Principal Value')\n```\n",
    "created_at": "2007-10-24T02:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5643",
    "user": "was"
}
```

Looks, good though:

```
19:15 < wstein> re: 920.  I've never seen a line like this before:
19:15 < wstein> if "divergent" in s or 'Principal Value': 
19:16 < wstein> It actually works as claimed.
19:16 < wstein> It's surprising to me that it is equivalent to: if "divergent" in (s + 'Principal Value')
```




---

archive/issue_comments_005644.json:
```json
{
    "body": "Attachment [920.patch](tarball://root/attachments/some-uuid/ticket920/920.patch) by malb created at 2007-10-24 19:24:49\n\napplied to 2.8.9.alpha1",
    "created_at": "2007-10-24T19:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5644",
    "user": "malb"
}
```

Attachment [920.patch](tarball://root/attachments/some-uuid/ticket920/920.patch) by malb created at 2007-10-24 19:24:49

applied to 2.8.9.alpha1



---

archive/issue_comments_005645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/920",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/920#issuecomment-5645",
    "user": "malb"
}
```

Resolution: fixed
