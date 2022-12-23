# Issue 1901: mistake in the documentation for gens for Finite field pari

archive/issues_001901.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: sage.rings.finite_field_ext_pari.FiniteField_ext_pari.gen?\n[...]\nDocstring:\n\n           Return chosen generator of the finite field.  This generator\n           is a root of the defining polynomial of the finite field, and\n           is guaranteed to be a generator for the multiplicative group.\n\n(This is wrong because in this case the generator is not guaranteed to\nbe a generator for the multiplicative group.)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1901\n\n",
    "created_at": "2008-01-24T00:36:11Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "mistake in the documentation for gens for Finite field pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1901",
    "user": "was"
}
```
Assignee: somebody


```
sage: sage.rings.finite_field_ext_pari.FiniteField_ext_pari.gen?
[...]
Docstring:

           Return chosen generator of the finite field.  This generator
           is a root of the defining polynomial of the finite field, and
           is guaranteed to be a generator for the multiplicative group.

(This is wrong because in this case the generator is not guaranteed to
be a generator for the multiplicative group.)
```


Issue created by migration from https://trac.sagemath.org/ticket/1901





---

archive/issue_comments_012031.json:
```json
{
    "body": "Changing assignee from somebody to cremona.",
    "created_at": "2008-03-01T17:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12031",
    "user": "cremona"
}
```

Changing assignee from somebody to cremona.



---

archive/issue_comments_012032.json:
```json
{
    "body": "Attachment\n\nAttached patch 8684.patch corrects the docstring and adds a relevant doctest.",
    "created_at": "2008-03-01T17:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12032",
    "user": "cremona"
}
```

Attachment

Attached patch 8684.patch corrects the docstring and adds a relevant doctest.



---

archive/issue_comments_012033.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-01T17:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12033",
    "user": "cremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012034.json:
```json
{
    "body": "It looks like there's some randomness in `FiniteField_ext_pari(23^20, \"b\")`, such that the proposed doctests will often fail.  Here's one failure mode, with two failing doctests:\n\n```\nsage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************\nFile \"finite_field_ext_pari.py\", line 300:\n    sage: F.gen().multiplicative_order() == F.order()-1\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"finite_field_ext_pari.py\", line 302:\n    sage: F.multiplicative_generator()\nExpected:\n    b + 1\nGot:\n    b\n**********************************************************************\n```\n\n\nAnd here's the other failure mode, with only one failing doctest:\n\n```\nsage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************\nFile \"finite_field_ext_pari.py\", line 302:\n    sage: F.multiplicative_generator()\nExpected:\n    b + 1\nGot:\n    b + 14\n**********************************************************************\n```\n\n\nAnd sometimes both tests pass.",
    "created_at": "2008-03-01T18:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12034",
    "user": "cwitty"
}
```

It looks like there's some randomness in `FiniteField_ext_pari(23^20, "b")`, such that the proposed doctests will often fail.  Here's one failure mode, with two failing doctests:

```
sage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 300:
    sage: F.gen().multiplicative_order() == F.order()-1
Expected:
    False
Got:
    True
**********************************************************************
File "finite_field_ext_pari.py", line 302:
    sage: F.multiplicative_generator()
Expected:
    b + 1
Got:
    b
**********************************************************************
```


And here's the other failure mode, with only one failing doctest:

```
sage -t  devel/sage-review/sage/rings/finite_field_ext_pari.py**********************************************************************
File "finite_field_ext_pari.py", line 302:
    sage: F.multiplicative_generator()
Expected:
    b + 1
Got:
    b + 14
**********************************************************************
```


And sometimes both tests pass.



---

archive/issue_comments_012035.json:
```json
{
    "body": "Apply this after 8684.patch!",
    "created_at": "2008-03-02T17:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12035",
    "user": "cremona"
}
```

Apply this after 8684.patch!



---

archive/issue_comments_012036.json:
```json
{
    "body": "Attachment\n\nThe second patch 8685.patch removes the doctests which are too random to be useful, and also adds to the docstring so that users are referred to multiplicative_generator() and warned that _both_ are random.",
    "created_at": "2008-03-02T17:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12036",
    "user": "cremona"
}
```

Attachment

The second patch 8685.patch removes the doctests which are too random to be useful, and also adds to the docstring so that users are referred to multiplicative_generator() and warned that _both_ are random.



---

archive/issue_comments_012037.json:
```json
{
    "body": "I am setting the Summary field to the old setting. If that is incorrect please change it to something meaningful.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-11T03:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12037",
    "user": "mabshoff"
}
```

I am setting the Summary field to the old setting. If that is incorrect please change it to something meaningful.

Cheers,

Michael



---

archive/issue_comments_012038.json:
```json
{
    "body": "Summary field is fine now -- I wish someone (cwitty?) would give this the thumbs up, otherwise the *wrong* doc sentence will go out with 2.10.3...",
    "created_at": "2008-03-11T09:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12038",
    "user": "cremona"
}
```

Summary field is fine now -- I wish someone (cwitty?) would give this the thumbs up, otherwise the *wrong* doc sentence will go out with 2.10.3...



---

archive/issue_comments_012039.json:
```json
{
    "body": "The changes look good to me, the patches apply cleanly against 2.10.3.rc5, and doctests pass.",
    "created_at": "2008-03-11T15:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12039",
    "user": "AlexGhitza"
}
```

The changes look good to me, the patches apply cleanly against 2.10.3.rc5, and doctests pass.



---

archive/issue_comments_012040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T22:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12040",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012041.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T22:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1901#issuecomment-12041",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
