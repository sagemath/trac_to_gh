# Issue 4609: Sage 3.2.1.a1: Make two optional magma doctests also depend on database_gap

archive/issues_004609.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen running -only_optional=magma without the database_gap.spkg installed we see two failures:\n\n```\nsage -t -only-optional=magma -long devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/number_field.py\", line 2455:\n    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma\nExpected:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\nGot:\n    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\n**********************************************************************\n```\n\nand\n\n```\nsage -t -only-optional=magma -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/polynomial/polynomial_element_generic.py\", line 742:\n    sage: f.galois_group(algorithm='magma')     # optional - magma\nExpected:\n    Transitive group number 5 of degree 4\nGot:\n    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.\n    Transitive group number 5 of degree 4\n**********************************************************************\n```\n\n\nThe fix should be obvious :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4609\n\n",
    "created_at": "2008-11-25T00:34:27Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.1.a1: Make two optional magma doctests also depend on database_gap",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4609",
    "user": "mabshoff"
}
```
Assignee: @williamstein

When running -only_optional=magma without the database_gap.spkg installed we see two failures:

```
sage -t -only-optional=magma -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/number_field.py", line 2455:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
```

and

```
sage -t -only-optional=magma -long devel/sage/sage/rings/polynomial/polynomial_element_generic.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha1/devel/sage/sage/rings/polynomial/polynomial_element_generic.py", line 742:
    sage: f.galois_group(algorithm='magma')     # optional - magma
Expected:
    Transitive group number 5 of degree 4
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Transitive group number 5 of degree 4
**********************************************************************
```


The fix should be obvious :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4609





---

archive/issue_comments_034594.json:
```json
{
    "body": "Attachment [sage-4609.patch](tarball://root/attachments/some-uuid/ticket4609/sage-4609.patch) by @williamstein created at 2008-11-25 05:09:36",
    "created_at": "2008-11-25T05:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4609#issuecomment-34594",
    "user": "@williamstein"
}
```

Attachment [sage-4609.patch](tarball://root/attachments/some-uuid/ticket4609/sage-4609.patch) by @williamstein created at 2008-11-25 05:09:36



---

archive/issue_comments_034595.json:
```json
{
    "body": "Positive review - exactly the fix I suggested.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T11:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4609#issuecomment-34595",
    "user": "mabshoff"
}
```

Positive review - exactly the fix I suggested.

Cheers,

Michael



---

archive/issue_comments_034596.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha1.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T11:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4609#issuecomment-34596",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha1.

Cheers,

Michael



---

archive/issue_comments_034597.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-25T11:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4609#issuecomment-34597",
    "user": "mabshoff"
}
```

Resolution: fixed
