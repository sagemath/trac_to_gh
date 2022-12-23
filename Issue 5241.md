# Issue 5241: Matrix Group sometimes assumes base ring is a field

archive/issues_005241.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  joyner\n\nFrom sage-support:\n\n\n```\nsage: M1 = matrix(ZZ,2,[[-1,0],[0,1]]) \nsage: M2 = matrix(ZZ,2,[[1,0],[0,-1]]) \nsage: M3 = matrix(ZZ,2,[[-1,0],[0,-1]]) \nsage: MG = MatrixGroup([M1, M2, M3]) \nsage: MG.order() \n    4 \nsage: MG.list() \n    Traceback (click to the left for traceback) \n    ... \n    AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object \nhas \n    no attribute 'prime_subfield' \n```\n\n\nThe offending code is in groups/matrix_gps/matrix_group.py where the problem is in the list method of MatrixGroup.\n\n\n```\n429        F = self.field_of_definition()\n430        n = F.degree()\n431        p = F.characteristic()\n432        a = F.prime_subfield().multiplicative_generator()\n433        b = F.multiplicative_generator()\n```\n\n\nIn the class definition of MatrixGroup, any base ring is allowed.  But at least this particular method (others?) assume that the base ring is in fact in a field.  \n\nSince a and b above are definitely used later in list(), as this all calls GAP, someone with a good knowledge of GAP should address this - and look for other places it's assumed that the base ring is a field and at least catch that exception with a better error message.  \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5241\n\n",
    "created_at": "2009-02-12T01:40:40Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "Matrix Group sometimes assumes base ring is a field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5241",
    "user": "kcrisman"
}
```
Assignee: joyner

CC:  joyner

From sage-support:


```
sage: M1 = matrix(ZZ,2,[[-1,0],[0,1]]) 
sage: M2 = matrix(ZZ,2,[[1,0],[0,-1]]) 
sage: M3 = matrix(ZZ,2,[[-1,0],[0,-1]]) 
sage: MG = MatrixGroup([M1, M2, M3]) 
sage: MG.order() 
    4 
sage: MG.list() 
    Traceback (click to the left for traceback) 
    ... 
    AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object 
has 
    no attribute 'prime_subfield' 
```


The offending code is in groups/matrix_gps/matrix_group.py where the problem is in the list method of MatrixGroup.


```
429        F = self.field_of_definition()
430        n = F.degree()
431        p = F.characteristic()
432        a = F.prime_subfield().multiplicative_generator()
433        b = F.multiplicative_generator()
```


In the class definition of MatrixGroup, any base ring is allowed.  But at least this particular method (others?) assume that the base ring is in fact in a field.  

Since a and b above are definitely used later in list(), as this all calls GAP, someone with a good knowledge of GAP should address this - and look for other places it's assumed that the base ring is a field and at least catch that exception with a better error message.  


Issue created by migration from https://trac.sagemath.org/ticket/5241





---

archive/issue_comments_040167.json:
```json
{
    "body": "to be applied to sage-3.3.alpha6",
    "created_at": "2009-02-17T02:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40167",
    "user": "wdj"
}
```

to be applied to sage-3.3.alpha6



---

archive/issue_comments_040168.json:
```json
{
    "body": "Attachment\n\nThis passes sage -t but sage -testall has lots of (unrelated I think) failures. It simply fixes the bug reported and adds the required docstring examples.",
    "created_at": "2009-02-17T02:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40168",
    "user": "wdj"
}
```

Attachment

This passes sage -t but sage -testall has lots of (unrelated I think) failures. It simply fixes the bug reported and adds the required docstring examples.



---

archive/issue_comments_040169.json:
```json
{
    "body": "Will this need rebase against 3.4?",
    "created_at": "2009-03-06T15:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40169",
    "user": "kcrisman"
}
```

Will this need rebase against 3.4?



---

archive/issue_comments_040170.json:
```json
{
    "body": "Against 3.4:\n\npatching file sage/groups/matrix_gps/matrix_group.py\nHunk #1 FAILED at 410\n1 out of 3 hunks FAILED -- saving rejects to file sage/groups/matrix_gps/matrix_group.py.rej\nabort: patch failed to apply\n\nThe hunk that didn't apply was the documentation hunk, as it turns out, unsurprisingly.\n\nSo it does need a rebase.  Sorry it took a while to be able to check this; it's sometimes complicated for me to do these things in a timely fashion, particularly with the 3.4 upgrade this was the case.",
    "created_at": "2009-03-16T15:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40170",
    "user": "kcrisman"
}
```

Against 3.4:

patching file sage/groups/matrix_gps/matrix_group.py
Hunk #1 FAILED at 410
1 out of 3 hunks FAILED -- saving rejects to file sage/groups/matrix_gps/matrix_group.py.rej
abort: patch failed to apply

The hunk that didn't apply was the documentation hunk, as it turns out, unsurprisingly.

So it does need a rebase.  Sorry it took a while to be able to check this; it's sometimes complicated for me to do these things in a timely fashion, particularly with the 3.4 upgrade this was the case.



---

archive/issue_comments_040171.json:
```json
{
    "body": "I have rebased the patch against 4.0 and tested it.  Looks good to me.\n\nApply only `trac_5241-rebased.patch`.",
    "created_at": "2009-05-31T13:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40171",
    "user": "AlexGhitza"
}
```

I have rebased the patch against 4.0 and tested it.  Looks good to me.

Apply only `trac_5241-rebased.patch`.



---

archive/issue_comments_040172.json:
```json
{
    "body": "Attachment\n\nrebased against 4.0",
    "created_at": "2009-05-31T13:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40172",
    "user": "AlexGhitza"
}
```

Attachment

rebased against 4.0



---

archive/issue_comments_040173.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T05:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40173",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_040174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T05:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5241#issuecomment-40174",
    "user": "mhansen"
}
```

Resolution: fixed
