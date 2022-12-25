# Issue 7694: change pickle jar doctest to make it a bit more robust and flexible...

archive/issues_007694.json:
```json
{
    "body": "Assignee: tbd\n\nChange the pickle jar doctest in devel/sage/sage/structure/sage_object.pyx to:\n\n\n```\nsage: print \"x\"; sage.structure.sage_object.unpickle_all(std)\nx...\nFailed to unpickle 0 objects.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7694\n\n",
    "created_at": "2009-12-15T23:47:06Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "change pickle jar doctest to make it a bit more robust and flexible...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7694",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Change the pickle jar doctest in devel/sage/sage/structure/sage_object.pyx to:


```
sage: print "x"; sage.structure.sage_object.unpickle_all(std)
x...
Failed to unpickle 0 objects.
```


Issue created by migration from https://trac.sagemath.org/ticket/7694





---

archive/issue_comments_065896.json:
```json
{
    "body": "I'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7694#issuecomment-65896",
    "user": "https://github.com/williamstein"
}
```

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_comments_065897.json:
```json
{
    "body": "Moved to Sage 5.0.   This still needs a patch...",
    "created_at": "2010-04-23T04:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7694#issuecomment-65897",
    "user": "https://github.com/jhpalmieri"
}
```

Moved to Sage 5.0.   This still needs a patch...



---

archive/issue_comments_065898.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7694#issuecomment-65898",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_065899.json:
```json
{
    "body": "Interestingly, I just looked in sage-4.4.3.alpha2, and this is already fixed:\n\n```\n\n\n    ::\n\n        sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'\n        sage: print \"x\"; sage.structure.sage_object.unpickle_all(std)\n        x...\n        Successfully unpickled ... objects.\n        Failed to unpickle 0 objects.\n```\n\nCool.",
    "created_at": "2010-06-03T04:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7694#issuecomment-65899",
    "user": "https://github.com/williamstein"
}
```

Interestingly, I just looked in sage-4.4.3.alpha2, and this is already fixed:

```


    ::

        sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
        sage: print "x"; sage.structure.sage_object.unpickle_all(std)
        x...
        Successfully unpickled ... objects.
        Failed to unpickle 0 objects.
```

Cool.
