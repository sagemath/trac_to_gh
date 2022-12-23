# Issue 2133: running dimension_modular_forms on weight 0 should return 1 (trivial to fix)

archive/issues_002133.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nIt should say 1, but now says\n\n\n```\nsage: dimension_modular_forms(1, 0)\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/home/ghitza/sage/eigensystems/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_modular_forms(X, k)\n   1004     if congroup.is_GammaH(X):\n   1005         return dimension_modular_forms_H(X, k)\n-> 1006     return dimension_cusp_forms(X, k) + dimension_eis(X, k)\n   1007 \n   1008 def sturm_bound(level, weight):\n\n/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_eis(X, k)\n    939     if k <= 1:\n    940         # TODO\n--> 941         raise NotImplementedError, \"Dimension of weight <= 1 Eisenstein series not yet implemented.\"\n    942     if isinstance(X, (int,long,Integer)):\n    943         if k%2 == 1: return 0\n\n<type 'exceptions.NotImplementedError'>: Dimension of weight <= 1 Eisenstein series not yet implemented.\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2133\n\n",
    "created_at": "2008-02-09T22:44:29Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "title": "running dimension_modular_forms on weight 0 should return 1 (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2133",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

It should say 1, but now says


```
sage: dimension_modular_forms(1, 0)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/ghitza/sage/eigensystems/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_modular_forms(X, k)
   1004     if congroup.is_GammaH(X):
   1005         return dimension_modular_forms_H(X, k)
-> 1006     return dimension_cusp_forms(X, k) + dimension_eis(X, k)
   1007 
   1008 def sturm_bound(level, weight):

/opt/sage/local/lib/python2.5/site-packages/sage/modular/dims.py in dimension_eis(X, k)
    939     if k <= 1:
    940         # TODO
--> 941         raise NotImplementedError, "Dimension of weight <= 1 Eisenstein series not yet implemented."
    942     if isinstance(X, (int,long,Integer)):
    943         if k%2 == 1: return 0

<type 'exceptions.NotImplementedError'>: Dimension of weight <= 1 Eisenstein series not yet implemented.
```




Issue created by migration from https://trac.sagemath.org/ticket/2133





---

archive/issue_comments_013986.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-17T01:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13986",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_013987.json:
```json
{
    "body": "... and the trivial fix is in the attached patch (together with a couple of trivial typos).",
    "created_at": "2008-02-17T01:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13987",
    "user": "AlexGhitza"
}
```

... and the trivial fix is in the attached patch (together with a couple of trivial typos).



---

archive/issue_comments_013988.json:
```json
{
    "body": "Attachment\n\napply this and the previous patch; this just adds a doctest",
    "created_at": "2008-02-19T16:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13988",
    "user": "was"
}
```

Attachment

apply this and the previous patch; this just adds a doctest



---

archive/issue_comments_013989.json:
```json
{
    "body": "Looks great; thanks for fixing the typos too.  I've added a doctest.",
    "created_at": "2008-02-19T16:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13989",
    "user": "was"
}
```

Looks great; thanks for fixing the typos too.  I've added a doctest.



---

archive/issue_comments_013990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T16:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13990",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013991.json:
```json
{
    "body": "Merged both patches in Sage 2.10.2.alpha1",
    "created_at": "2008-02-19T16:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2133#issuecomment-13991",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.2.alpha1
