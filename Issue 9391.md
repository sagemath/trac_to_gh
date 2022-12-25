# Issue 9391: kolyvagin_cohomology_class() method differs from doc

archive/issues_009391.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: kolyvagin classes\n\nIf P is a 'kolyvagin_point' created from an elliptic curve, the doc string says\n\n```\nDefinition: P.kolyvagin_cohomology_class(self, n=None)\nDocstring:\n       INPUT:\n    \n          * n -- positive integer that divides the gcd of a_p and p+1 for\n            all p dividing the conductor.  If n is None, choose the\n            largest valid n.\n```\nIn fact, if \"n\" is None, a ValueError is thrown.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9391\n\n",
    "created_at": "2010-06-30T05:27:57Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "title": "kolyvagin_cohomology_class() method differs from doc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9391",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @JohnCremona

Keywords: kolyvagin classes

If P is a 'kolyvagin_point' created from an elliptic curve, the doc string says

```
Definition: P.kolyvagin_cohomology_class(self, n=None)
Docstring:
       INPUT:
    
          * n -- positive integer that divides the gcd of a_p and p+1 for
            all p dividing the conductor.  If n is None, choose the
            largest valid n.
```
In fact, if "n" is None, a ValueError is thrown.


Issue created by migration from https://trac.sagemath.org/ticket/9391





---

archive/issue_comments_089272.json:
```json
{
    "body": "The problem happens when the conductor is 1.\n\n```\nsage: y = EllipticCurve('389a').heegner_point(-7,1)\nsage: y.conductor()\n1\nsage: P=y.kolyvagin_cohomology_class()\nBOOM\n```\nThis is because the gcd of the empty list is 0. I do not know what to do to solve the issue.",
    "created_at": "2014-03-06T16:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9391#issuecomment-89272",
    "user": "https://github.com/fchapoton"
}
```

The problem happens when the conductor is 1.

```
sage: y = EllipticCurve('389a').heegner_point(-7,1)
sage: y.conductor()
1
sage: P=y.kolyvagin_cohomology_class()
BOOM
```
This is because the gcd of the empty list is 0. I do not know what to do to solve the issue.
