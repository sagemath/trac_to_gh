# Issue 8967: Make extensions of general rings work in the same way as they do for number fields

archive/issues_008967.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @mstreng\n\n\n```\nsage: P.<t> = GF(5)[]\nsage: GF(5).extension(t^2 - 2, name='a')\nUnivariate Quotient Polynomial Ring in a over Finite Field of size 5 with modulus a^2 + 3\nsage: F.<a> = GF(5).extension(t^2 - 2)\nTraceback (most recent call last)\n...\nValueError: variable names must be alphanumeric, but one is '('a' which is not.\n```\n\nand\n\n\n```\nsage: GF(5).extension(x^2 - 2, name='a')\nTraceback (most recent call last)\n...\nAttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'list'\n```\n\nThe patch solves both these problems, and provides a more useful error  message for mistakes like `GF(5).extension(\"not_a_poly\", name='a'),` by  splicing in code from the number field version.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8967\n\n",
    "created_at": "2010-05-14T18:28:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Make extensions of general rings work in the same way as they do for number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8967",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: @aghitza

CC:  @mstreng


```
sage: P.<t> = GF(5)[]
sage: GF(5).extension(t^2 - 2, name='a')
Univariate Quotient Polynomial Ring in a over Finite Field of size 5 with modulus a^2 + 3
sage: F.<a> = GF(5).extension(t^2 - 2)
Traceback (most recent call last)
...
ValueError: variable names must be alphanumeric, but one is '('a' which is not.
```

and


```
sage: GF(5).extension(x^2 - 2, name='a')
Traceback (most recent call last)
...
AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'list'
```

The patch solves both these problems, and provides a more useful error  message for mistakes like `GF(5).extension("not_a_poly", name='a'),` by  splicing in code from the number field version.

Issue created by migration from https://trac.sagemath.org/ticket/8967





---

archive/issue_comments_082508.json:
```json
{
    "body": "Attachment [trac_8967.patch](tarball://root/attachments/some-uuid/ticket8967/trac_8967.patch) by fwclarke created at 2010-05-14 18:35:25",
    "created_at": "2010-05-14T18:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82508",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Attachment [trac_8967.patch](tarball://root/attachments/some-uuid/ticket8967/trac_8967.patch) by fwclarke created at 2010-05-14 18:35:25



---

archive/issue_comments_082509.json:
```json
{
    "body": "Is this ready for review?",
    "created_at": "2010-05-15T02:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is this ready for review?



---

archive/issue_comments_082510.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T06:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82510",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082511.json:
```json
{
    "body": "Yes",
    "created_at": "2010-05-15T06:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82511",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Yes



---

archive/issue_comments_082512.json:
```json
{
    "body": "This patch does what it says. It did however take over a bad habit of \"extension\" for number fields. See the examples below, where I think the behavior of QQ is preferred.\n\n```\nsage: QQ.extension(x^2-2, ('a', 'b'))\nIndexError: the number of names must equal the number of generators\nsage: GF(3).extension(x^2-2, ('a', 'b'))\nUnivariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1\nsage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', 'b'))\nNumber Field in a with defining polynomial x^2 - 2 over its base field\n\nsage: QQ.extension(x^2 - 2, ('a', QQ))\nValueError: variable names must be alphanumeric, but one is 'Rational Field' which is not.\nsage: GF(3).extension(x^2 - 2, ('a', QQ))\nUnivariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1\nsage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', QQ))\nNumber Field in a with defining polynomial x^2 - 2 over its base field\n```\n",
    "created_at": "2010-07-12T14:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82512",
    "user": "https://github.com/mstreng"
}
```

This patch does what it says. It did however take over a bad habit of "extension" for number fields. See the examples below, where I think the behavior of QQ is preferred.

```
sage: QQ.extension(x^2-2, ('a', 'b'))
IndexError: the number of names must equal the number of generators
sage: GF(3).extension(x^2-2, ('a', 'b'))
Univariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1
sage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', 'b'))
Number Field in a with defining polynomial x^2 - 2 over its base field

sage: QQ.extension(x^2 - 2, ('a', QQ))
ValueError: variable names must be alphanumeric, but one is 'Rational Field' which is not.
sage: GF(3).extension(x^2 - 2, ('a', QQ))
Univariate Quotient Polynomial Ring in a over Finite Field of size 3 with modulus a^2 + 1
sage: QuadraticField(-1, 'i').extension(x^2 - 2, ('a', QQ))
Number Field in a with defining polynomial x^2 - 2 over its base field
```




---

archive/issue_comments_082513.json:
```json
{
    "body": "All tests pass, and as I said before: the patch does what it claims. I've tried a couple more examples and everything seems fine.\n\nThe bad behavior in my previous comment was there for number fields already and I don't consider it to be a blocker for this patch.",
    "created_at": "2010-07-12T15:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82513",
    "user": "https://github.com/mstreng"
}
```

All tests pass, and as I said before: the patch does what it claims. I've tried a couple more examples and everything seems fine.

The bad behavior in my previous comment was there for number fields already and I don't consider it to be a blocker for this patch.



---

archive/issue_comments_082514.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-12T15:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82514",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082515.json:
```json
{
    "body": "I've updated the Author(s) and Reviewer(s) fields, which should contain full names.  Please correct the fields, if I'm wrong.",
    "created_at": "2010-07-20T09:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82515",
    "user": "https://github.com/qed777"
}
```

I've updated the Author(s) and Reviewer(s) fields, which should contain full names.  Please correct the fields, if I'm wrong.



---

archive/issue_comments_082516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8967#issuecomment-82516",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009117.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-20T09:25:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8967",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8967#event-9117"
}
```
