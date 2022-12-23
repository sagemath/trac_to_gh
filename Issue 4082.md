# Issue 4082: [with patch, needs review] Sage 3.1.2.rc0: numerical noise on OSX/Intel in schemes/elliptic_curves/ell_number_field.py

archive/issues_004082.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1108:\n    sage: E.period_lattice(embs[0])\nExpected:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n    From: Number Field in a with defining polynomial x^2 - 2\n    To:   Real Field with 53 bits of precision\n    Defn: a |--> -1.41421356237310\nGot:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n      From: Number Field in a with defining polynomial x^2 - 2\n      To:   Real Field with 53 bits of precision\n      Defn: a |--> -1.41421356237309\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1113:\n    sage: E.period_lattice(embs[1])\nExpected:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n    From: Number Field in a with defining polynomial x^2 - 2\n    To:   Real Field with 53 bits of precision\n    Defn: a |--> 1.41421356237309\nGot:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n      From: Number Field in a with defining polynomial x^2 - 2\n      To:   Real Field with 53 bits of precision\n      Defn: a |--> 1.41421356237310\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4082\n\n",
    "created_at": "2008-09-09T01:53:21Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Sage 3.1.2.rc0: numerical noise on OSX/Intel in schemes/elliptic_curves/ell_number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4082",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1108:
    sage: E.period_lattice(embs[0])
Expected:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
    From: Number Field in a with defining polynomial x^2 - 2
    To:   Real Field with 53 bits of precision
    Defn: a |--> -1.41421356237310
Got:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
      From: Number Field in a with defining polynomial x^2 - 2
      To:   Real Field with 53 bits of precision
      Defn: a |--> -1.41421356237309
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1113:
    sage: E.period_lattice(embs[1])
Expected:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
    From: Number Field in a with defining polynomial x^2 - 2
    To:   Real Field with 53 bits of precision
    Defn: a |--> 1.41421356237309
Got:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
      From: Number Field in a with defining polynomial x^2 - 2
      To:   Real Field with 53 bits of precision
      Defn: a |--> 1.41421356237310
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4082





---

archive/issue_comments_029450.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-09T01:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29450",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_029451.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-09T01:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29451",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_029452.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T02:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29452",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029453.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T02:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29453",
    "user": "mabshoff"
}
```

Resolution: fixed
