# Issue 8671: FieldElement.quo_rem broken

archive/issues_008671.json:
```json
{
    "body": "Assignee: @burcin\n\n```\nsage: P.<n> = QQ[]\nsage: F = P.fraction_field()\nsage: P.one_element()//F.one_element()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n.../sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__floordiv__ (sage/rings/polynomial/polynomial_element.c:14608)()\n\n.../sage/structure/element.so in sage.structure.element.NamedBinopMethod.__call__ (sage/structure/element.c:22812)()\n\n.../sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:16670)()\n\n...\nAttributeError: 'sage.rings.fraction_field_element.FractionFieldElement' object has no attribute '_parent'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8671\n\n",
    "created_at": "2010-04-11T12:19:05Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "FieldElement.quo_rem broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8671",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

```
sage: P.<n> = QQ[]
sage: F = P.fraction_field()
sage: P.one_element()//F.one_element()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

.../sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.__floordiv__ (sage/rings/polynomial/polynomial_element.c:14608)()

.../sage/structure/element.so in sage.structure.element.NamedBinopMethod.__call__ (sage/structure/element.c:22812)()

.../sage/structure/element.so in sage.structure.element.FieldElement.quo_rem (sage/structure/element.c:16670)()

...
AttributeError: 'sage.rings.fraction_field_element.FractionFieldElement' object has no attribute '_parent'
```

Issue created by migration from https://trac.sagemath.org/ticket/8671





---

archive/issue_comments_078780.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-11T12:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78780",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078781.json:
```json
{
    "body": "Attachment [trac_8671-field_element_quo_rem.patch](tarball://root/attachments/some-uuid/ticket8671/trac_8671-field_element_quo_rem.patch) by @burcin created at 2010-04-11 12:29:32",
    "created_at": "2010-04-11T12:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78781",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8671-field_element_quo_rem.patch](tarball://root/attachments/some-uuid/ticket8671/trac_8671-field_element_quo_rem.patch) by @burcin created at 2010-04-11 12:29:32



---

archive/issue_comments_078782.json:
```json
{
    "body": "I'm worried by the fact that right._parent fails while parent(right) succeeds.",
    "created_at": "2010-04-25T16:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78782",
    "user": "https://github.com/JohnCremona"
}
```

I'm worried by the fact that right._parent fails while parent(right) succeeds.



---

archive/issue_comments_078783.json:
```json
{
    "body": "`_parent` is a cdef'd attribute. At the point this code is used, Cython doesn't know that `right` is an `Element`, so it generates code to look for a python attribute `_parent` which fails.\n\nOne solution would be to use a type cast by writing `(<Element>right)._parent`, but we'd have to handle python types like `int` manually before this. The function `parent()`, which in turn calls `sage.structure.parent.parent_c` is used exactly for this purpose.\n\nCalling parent_c directly would be faster, but that is not exported in `sage/structure/parent.pxd`.",
    "created_at": "2010-05-05T03:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78783",
    "user": "https://github.com/burcin"
}
```

`_parent` is a cdef'd attribute. At the point this code is used, Cython doesn't know that `right` is an `Element`, so it generates code to look for a python attribute `_parent` which fails.

One solution would be to use a type cast by writing `(<Element>right)._parent`, but we'd have to handle python types like `int` manually before this. The function `parent()`, which in turn calls `sage.structure.parent.parent_c` is used exactly for this purpose.

Calling parent_c directly would be faster, but that is not exported in `sage/structure/parent.pxd`.



---

archive/issue_comments_078784.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-16T15:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78784",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078785.json:
```json
{
    "body": "That makes sense.\n\nPatch applies fine to 4.4.2.rc0 and tests in sage/structure and sage/rings/ pass.  So, positive review.",
    "created_at": "2010-05-16T15:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78785",
    "user": "https://github.com/JohnCremona"
}
```

That makes sense.

Patch applies fine to 4.4.2.rc0 and tests in sage/structure and sage/rings/ pass.  So, positive review.



---

archive/issue_comments_078786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8671#issuecomment-78786",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021021.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T01:20:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8671",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8671#event-21021"
}
```
