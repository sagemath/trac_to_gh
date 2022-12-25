# Issue 6293: conjugacy_classes_representatives is missing in AbelianGroup

archive/issues_006293.json:
```json
{
    "body": "Assignee: joyner\n\nKeywords: AbelianGroup\n\nThe function conjugacy_classes_representatives isn't defined for AbelianGroup. It's possible to simply use the list of elements when G is finite, but it probably be preferable to make sure the order of the conjugacy classes is the same as in gap. Which seems to be the case, but not totally sure. This might be easier to deal with if we can more easily convert between AbelianGroup elements and gap elements, I've opened trac 6292 for this separate issue.\n\n\n```\nsage: G = AbelianGroup([2,2])\nsage: H = gap(G)\nsage: H.ConjugacyClasses()\n[ ConjugacyClass( Group( [ f1, f2 ] ), <identity> of ... ), \n  ConjugacyClass( Group( [ f1, f2 ] ), f1 ), \n  ConjugacyClass( Group( [ f1, f2 ] ), f2 ), \n  ConjugacyClass( Group( [ f1, f2 ] ), f1*f2 ) ]\nsage: G.list()\n[1, f1, f0, f0*f1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6293\n\n",
    "created_at": "2009-06-15T04:14:19Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "conjugacy_classes_representatives is missing in AbelianGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6293",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlefebvre"
}
```
Assignee: joyner

Keywords: AbelianGroup

The function conjugacy_classes_representatives isn't defined for AbelianGroup. It's possible to simply use the list of elements when G is finite, but it probably be preferable to make sure the order of the conjugacy classes is the same as in gap. Which seems to be the case, but not totally sure. This might be easier to deal with if we can more easily convert between AbelianGroup elements and gap elements, I've opened trac 6292 for this separate issue.


```
sage: G = AbelianGroup([2,2])
sage: H = gap(G)
sage: H.ConjugacyClasses()
[ ConjugacyClass( Group( [ f1, f2 ] ), <identity> of ... ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f1 ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f2 ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f1*f2 ) ]
sage: G.list()
[1, f1, f0, f0*f1]
```


Issue created by migration from https://trac.sagemath.org/ticket/6293


