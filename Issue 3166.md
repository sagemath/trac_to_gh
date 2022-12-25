# Issue 3166: Problems with echelon_form over ComplexField

archive/issues_003166.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor certain well-conditioned floating-point matrices with entries in ComplexField, echelon_form can return matrices which are not in (approximate) echelon_form.   This breaks methods like rank(), right_solve() and inverse().  I've attached a sample matrix which illustrates this \n\n```\nsage: A = load(\"./prob-sol.sobj\")\nsage: A.parent()\nFull MatrixSpace of 5 by 5 dense matrices over Complex Field with 1010 bits of precision\nsage: matrix(CDF, A.echelon_form())\n\n[                              1.0                                 0                            -3.5*I                                 0                    -20.0 + 12.0*I]\n[                                0                               1.0                               1.0                                 0                      -4.0 + 1.0*I]\n[                                0                                 0        1.0 + 4.55695126222e-305*I                                 0 -2.33592727654 + 0.497614402099*I]\n[                                0                                 0                              -4.0                               1.0                              -2.0]\n[                                0                                 0                              -2.0                                 0                                 0]\nsage: CC(A.det())\n76.1312551138321 - 5.28799080668534*I\nsage: A.rank()\n4\n```\n\n\nThis bug is probably related to #2256 and #1132 but there the problem with echelon_form is more subtle (1 entries on the diagonal which aren't quite 1), which is why I opened this new ticket.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/3166\n\n",
    "created_at": "2008-05-12T00:49:27Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Problems with echelon_form over ComplexField",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3166",
    "user": "https://github.com/NathanDunfield"
}
```
Assignee: @williamstein

For certain well-conditioned floating-point matrices with entries in ComplexField, echelon_form can return matrices which are not in (approximate) echelon_form.   This breaks methods like rank(), right_solve() and inverse().  I've attached a sample matrix which illustrates this 

```
sage: A = load("./prob-sol.sobj")
sage: A.parent()
Full MatrixSpace of 5 by 5 dense matrices over Complex Field with 1010 bits of precision
sage: matrix(CDF, A.echelon_form())

[                              1.0                                 0                            -3.5*I                                 0                    -20.0 + 12.0*I]
[                                0                               1.0                               1.0                                 0                      -4.0 + 1.0*I]
[                                0                                 0        1.0 + 4.55695126222e-305*I                                 0 -2.33592727654 + 0.497614402099*I]
[                                0                                 0                              -4.0                               1.0                              -2.0]
[                                0                                 0                              -2.0                                 0                                 0]
sage: CC(A.det())
76.1312551138321 - 5.28799080668534*I
sage: A.rank()
4
```


This bug is probably related to #2256 and #1132 but there the problem with echelon_form is more subtle (1 entries on the diagonal which aren't quite 1), which is why I opened this new ticket.  

Issue created by migration from https://trac.sagemath.org/ticket/3166





---

archive/issue_comments_021894.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-05-12T00:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3166#issuecomment-21894",
    "user": "https://github.com/NathanDunfield"
}
```

Resolution: duplicate



---

archive/issue_events_007150.json:
```json
{
    "actor": "https://github.com/NathanDunfield",
    "created_at": "2008-05-12T00:54:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3166",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3166#event-7150"
}
```
