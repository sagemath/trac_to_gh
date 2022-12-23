# Issue 5863: [with patch, needs review] remove some files from sage/algebras

archive/issues_005863.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCoverage of some files in algebras:\n\n```\nalgebra_ideal.py: 0% (0 of 19)\nalgebra_ideal_element.py: 0% (0 of 1)\nalgebra_order.py: 0% (0 of 16)\nalgebra_order_element.py: 0% (0 of 13)\nalgebra_order_frac_ideal.py: 0% (0 of 17)\nalgebra_order_ideal.py: 0% (0 of 21)\nalgebra_order_ideal_element.py: 0% (0 of 1)\n```\n\nFurthermore, these don't seem to be used by any of the rest of the Sage code, so let's delete them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5863\n\n",
    "created_at": "2009-04-23T06:07:02Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] remove some files from sage/algebras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5863",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Coverage of some files in algebras:

```
algebra_ideal.py: 0% (0 of 19)
algebra_ideal_element.py: 0% (0 of 1)
algebra_order.py: 0% (0 of 16)
algebra_order_element.py: 0% (0 of 13)
algebra_order_frac_ideal.py: 0% (0 of 17)
algebra_order_ideal.py: 0% (0 of 21)
algebra_order_ideal_element.py: 0% (0 of 1)
```

Furthermore, these don't seem to be used by any of the rest of the Sage code, so let's delete them.

Issue created by migration from https://trac.sagemath.org/ticket/5863





---

archive/issue_comments_046322.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-23T06:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5863#issuecomment-46322",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_046323.json:
```json
{
    "body": "If anybody wants these to be in Sage, they should revert this patch, then get the coverage to 100% and get everything up to how things work in Sage now (e.g., coercion model, etc.).  Right now they are used nowhere and have no tests.",
    "created_at": "2009-04-23T06:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5863#issuecomment-46323",
    "user": "was"
}
```

If anybody wants these to be in Sage, they should revert this patch, then get the coverage to 100% and get everything up to how things work in Sage now (e.g., coercion model, etc.).  Right now they are used nowhere and have no tests.



---

archive/issue_comments_046324.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5863#issuecomment-46324",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_046325.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T07:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5863#issuecomment-46325",
    "user": "mabshoff"
}
```

Resolution: fixed
