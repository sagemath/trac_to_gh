# Issue 4266: overflow error in SR approx

archive/issues_004266.json:
```json
{
    "body": "Assignee: @burcin\n\n```\nsage: round(sqrt(Integer('1'*500)))\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 865, in round\n    except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 6164, in __float__\n    return float(f._approx_(float(g)))\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 7941, in _approx_\n    return math.sqrt(x)\nOverflowError: math range error\n```\n\nApprox should fall back to mpfr if float fails. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4266\n\n",
    "created_at": "2008-10-11T14:06:33Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "overflow error in SR approx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4266",
    "user": "https://github.com/robertwb"
}
```
Assignee: @burcin

```
sage: round(sqrt(Integer('1'*500)))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/functional.py", line 865, in round
    except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6164, in __float__
    return float(f._approx_(float(g)))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 7941, in _approx_
    return math.sqrt(x)
OverflowError: math range error
```

Approx should fall back to mpfr if float fails. 

Issue created by migration from https://trac.sagemath.org/ticket/4266





---

archive/issue_events_009635.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-18T19:49:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4266#event-9635"
}
```



---

archive/issue_comments_031050.json:
```json
{
    "body": "This is related to #188...",
    "created_at": "2008-10-30T22:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31050",
    "user": "https://github.com/robertwb"
}
```

This is related to #188...



---

archive/issue_comments_031051.json:
```json
{
    "body": "Attachment [4266-sr-round.patch](tarball://root/attachments/some-uuid/ticket4266/4266-sr-round.patch) by @robertwb created at 2008-10-30 22:16:29\n\nI assume there is good reason that \"always return an RDF\" is enforced. SR elements should probably implement round() themselves.",
    "created_at": "2008-10-30T22:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31051",
    "user": "https://github.com/robertwb"
}
```

Attachment [4266-sr-round.patch](tarball://root/attachments/some-uuid/ticket4266/4266-sr-round.patch) by @robertwb created at 2008-10-30 22:16:29

I assume there is good reason that "always return an RDF" is enforced. SR elements should probably implement round() themselves.



---

archive/issue_comments_031052.json:
```json
{
    "body": "Actually, I don't know of a good reason that \"always return as RDF\" is enforced.  It seems like floor, round, and ceiling should return Integers where possible.  There is a trac ticket by Nick Alexander that does this for some objects.",
    "created_at": "2008-11-21T17:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31052",
    "user": "https://github.com/mwhansen"
}
```

Actually, I don't know of a good reason that "always return as RDF" is enforced.  It seems like floor, round, and ceiling should return Integers where possible.  There is a trac ticket by Nick Alexander that does this for some objects.



---

archive/issue_comments_031053.json:
```json
{
    "body": "REFEREE REPORT:\n\nThe attached patch fixes the reported problem.\n\nI agree that changing round, etc., to not return RDF's makes perfect sense, but I think that should be an entirely new trac ticket. \n\nI doctested only the calculus tree after applying this patch, and all was good.",
    "created_at": "2008-11-27T17:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31053",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

The attached patch fixes the reported problem.

I agree that changing round, etc., to not return RDF's makes perfect sense, but I think that should be an entirely new trac ticket. 

I doctested only the calculus tree after applying this patch, and all was good.



---

archive/issue_comments_031054.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T07:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031055.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T07:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4266#issuecomment-31055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_events_009636.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T07:32:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4266",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4266#event-9636"
}
```
