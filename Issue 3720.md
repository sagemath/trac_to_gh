# Issue 3720: stupid bug in elliptic curves caused by refactoring

archive/issues_003720.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: EllipticCurve([0,0,0,-193^2,0]).sha().an()\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)\n    157         eps = E.root_number()\n    158         if eps == 1:\n--> 159             L1_over_omega = E.lseries().L_ratio()\n    160             if L1_over_omega == 0:\n    161                 return self.an_numerical(use_database=use_database)\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell.py in L_ratio(self)\n    695                 quo = Q(n) / Q(C)\n    696                 self.__lratio = quo / self.__E.real_components()\n    697                 return self.__lratio\n    698             k += sqrtN\n--> 699             misc.verbose(\"Increasing precision to %s terms.\"%k)\n\nNameError: global name 'misc' is not defined\n```\n\n\nthis was reported by Nils Bruin and John Cremona.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3720\n\n",
    "created_at": "2008-07-24T11:31:34Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "stupid bug in elliptic curves caused by refactoring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3720",
    "user": "was"
}
```
Assignee: was


```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)
    157         eps = E.root_number()
    158         if eps == 1:
--> 159             L1_over_omega = E.lseries().L_ratio()
    160             if L1_over_omega == 0:
    161                 return self.an_numerical(use_database=use_database)

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell.py in L_ratio(self)
    695                 quo = Q(n) / Q(C)
    696                 self.__lratio = quo / self.__E.real_components()
    697                 return self.__lratio
    698             k += sqrtN
--> 699             misc.verbose("Increasing precision to %s terms."%k)

NameError: global name 'misc' is not defined
```


this was reported by Nils Bruin and John Cremona.

Issue created by migration from https://trac.sagemath.org/ticket/3720





---

archive/issue_comments_026399.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-24T11:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3720#issuecomment-26399",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_026400.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-07-25T16:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3720#issuecomment-26400",
    "user": "cremona"
}
```

Resolution: duplicate



---

archive/issue_comments_026401.json:
```json
{
    "body": "This is a duplicate of #3651 which has already been fixed in 3.0.6.rc0, hence this one can be closed as a duplicate.",
    "created_at": "2008-07-25T16:44:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3720#issuecomment-26401",
    "user": "cremona"
}
```

This is a duplicate of #3651 which has already been fixed in 3.0.6.rc0, hence this one can be closed as a duplicate.
