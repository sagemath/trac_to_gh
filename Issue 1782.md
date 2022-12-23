# Issue 1782: doctests for multi_polynomial_ideal.py not reproducible

archive/issues_001782.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: test doctest multi polynomial ideal reporducible\n\nIn multi_polynomial_ideal.py, the doctests for\n\n* complete_primary_decomposition\n* groebner_basis\n* primary_decomposition\n\nwork under `sage -t` but do not work from the `sage:` prompt.  Presumably there is some singular initialization that is not being reproduced at the prompt?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1782\n\n",
    "created_at": "2008-01-15T18:55:47Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "title": "doctests for multi_polynomial_ideal.py not reproducible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1782",
    "user": "ncalexan"
}
```
Assignee: malb

Keywords: test doctest multi polynomial ideal reporducible

In multi_polynomial_ideal.py, the doctests for

* complete_primary_decomposition
* groebner_basis
* primary_decomposition

work under `sage -t` but do not work from the `sage:` prompt.  Presumably there is some singular initialization that is not being reproduced at the prompt?

Issue created by migration from https://trac.sagemath.org/ticket/1782





---

archive/issue_comments_011282.json:
```json
{
    "body": "Changing keywords from \"test doctest multi polynomial ideal reporducible\" to \"test doctest multi polynomial ideal reproducible\".",
    "created_at": "2008-01-15T18:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11282",
    "user": "ncalexan"
}
```

Changing keywords from "test doctest multi polynomial ideal reporducible" to "test doctest multi polynomial ideal reproducible".



---

archive/issue_comments_011283.json:
```json
{
    "body": "This should be fixed since we compute reduced Gr\u00f6bner bases by default.",
    "created_at": "2008-01-23T21:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11283",
    "user": "malb"
}
```

This should be fixed since we compute reduced Gröbner bases by default.



---

archive/issue_comments_011284.json:
```json
{
    "body": "Nick, as you reported the bug: I claim this is fixed. Could you check?",
    "created_at": "2008-03-28T11:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11284",
    "user": "malb"
}
```

Nick, as you reported the bug: I claim this is fixed. Could you check?



---

archive/issue_comments_011285.json:
```json
{
    "body": "This issue is resolved, I just checked and I can reproduce all doctests. Someone not me please close this ticket :-)",
    "created_at": "2008-04-01T12:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11285",
    "user": "malb"
}
```

This issue is resolved, I just checked and I can reproduce all doctests. Someone not me please close this ticket :-)



---

archive/issue_comments_011286.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T12:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11286",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011287.json:
```json
{
    "body": "Your wish is my command ;)",
    "created_at": "2008-04-01T12:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1782",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1782#issuecomment-11287",
    "user": "mabshoff"
}
```

Your wish is my command ;)
