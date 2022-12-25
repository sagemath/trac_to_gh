# Issue 4082: [with patch, needs review] Sage 3.1.2.rc0: numerical noise on OSX/Intel in schemes/elliptic_curves/ell_number_field.py

archive/issues_004082.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1108:\n    sage: E.period_lattice(embs[0])\nExpected:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n    From: Number Field in a with defining polynomial x^2 - 2\n    To:   Real Field with 53 bits of precision\n    Defn: a |--> -1.41421356237310\nGot:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n      From: Number Field in a with defining polynomial x^2 - 2\n      To:   Real Field with 53 bits of precision\n      Defn: a |--> -1.41421356237309\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1113:\n    sage: E.period_lattice(embs[1])\nExpected:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n    From: Number Field in a with defining polynomial x^2 - 2\n    To:   Real Field with 53 bits of precision\n    Defn: a |--> 1.41421356237309\nGot:\n    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:\n      From: Number Field in a with defining polynomial x^2 - 2\n      To:   Real Field with 53 bits of precision\n      Defn: a |--> 1.41421356237310\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4082\n\n",
    "created_at": "2008-09-09T01:53:21Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] Sage 3.1.2.rc0: numerical noise on OSX/Intel in schemes/elliptic_curves/ell_number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_029391.json:
```json
{
    "body": "Attachment [trac_4082.patch](tarball://root/attachments/some-uuid/ticket4082/trac_4082.patch) by mabshoff created at 2008-09-09 01:54:43",
    "created_at": "2008-09-09T01:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4082.patch](tarball://root/attachments/some-uuid/ticket4082/trac_4082.patch) by mabshoff created at 2008-09-09 01:54:43



---

archive/issue_comments_029392.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-09T01:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29392",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_029393.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T02:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029394.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T02:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4082#issuecomment-29394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
