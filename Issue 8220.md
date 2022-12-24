# Issue 8220: Improve consistency and docs for finite fields creation

archive/issues_008220.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nFor the Givaro and the NTL implementations, one can use modulus='random' but not for the Pari implementation.\nMoreover, according to the documentation in finite_field.py, modulus must be a polynomial, but in fact it can also be a string.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8220\n\n",
    "created_at": "2010-02-09T15:30:48Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Improve consistency and docs for finite fields creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8220",
    "user": "ylchapuy"
}
```
Assignee: AlexGhitza

For the Givaro and the NTL implementations, one can use modulus='random' but not for the Pari implementation.
Moreover, according to the documentation in finite_field.py, modulus must be a polynomial, but in fact it can also be a string.

Issue created by migration from https://trac.sagemath.org/ticket/8220





---

archive/issue_comments_072544.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T15:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72544",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072545.json:
```json
{
    "body": "The provided patch:\n\n* cleans the code and the documentation for finite field creation;\n* make modulus = 'conway' and modulus = 'random' available for all implementations;\n* make modulus = 'minimal_weight' is available for all binary fields;\n* adds modulus = 'first_lexicographic' for all binary fields.\n\nYann",
    "created_at": "2010-02-09T15:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72545",
    "user": "ylchapuy"
}
```

The provided patch:

* cleans the code and the documentation for finite field creation;
* make modulus = 'conway' and modulus = 'random' available for all implementations;
* make modulus = 'minimal_weight' is available for all binary fields;
* adds modulus = 'first_lexicographic' for all binary fields.

Yann



---

archive/issue_comments_072546.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T15:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72546",
    "user": "ylchapuy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072547.json:
```json
{
    "body": "needs #8212",
    "created_at": "2010-02-09T16:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72547",
    "user": "ylchapuy"
}
```

needs #8212



---

archive/issue_comments_072548.json:
```json
{
    "body": "Attachment [trac_8220-finite_field_creation.patch](tarball://root/attachments/some-uuid/ticket8220/trac_8220-finite_field_creation.patch) by ylchapuy created at 2010-02-09 16:23:39",
    "created_at": "2010-02-09T16:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72548",
    "user": "ylchapuy"
}
```

Attachment [trac_8220-finite_field_creation.patch](tarball://root/attachments/some-uuid/ticket8220/trac_8220-finite_field_creation.patch) by ylchapuy created at 2010-02-09 16:23:39



---

archive/issue_comments_072549.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-09T16:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72549",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072550.json:
```json
{
    "body": "There's one doctest that needs modifying after this patch is applied:\n\n```\nsage -t  \"devel/sage/sage/structure/factory.pyx\"            \n**********************************************************************\nFile \"/Users/mafwc/sage-4.3.2/devel/sage/sage/structure/factory.pyx\", line 234:\n    sage: key, _ = GF.create_key_and_extra_args(27, 'k'); key\nExpected:\n    (27, ('k',), None, None, '{}')\nGot:\n    (27, ('k',), 'conway', None, '{}')\n**********************************************************************\n```\n\nOtherwise it seems fine.",
    "created_at": "2010-02-11T08:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72550",
    "user": "fwclarke"
}
```

There's one doctest that needs modifying after this patch is applied:

```
sage -t  "devel/sage/sage/structure/factory.pyx"            
**********************************************************************
File "/Users/mafwc/sage-4.3.2/devel/sage/sage/structure/factory.pyx", line 234:
    sage: key, _ = GF.create_key_and_extra_args(27, 'k'); key
Expected:
    (27, ('k',), None, None, '{}')
Got:
    (27, ('k',), 'conway', None, '{}')
**********************************************************************
```

Otherwise it seems fine.



---

archive/issue_comments_072551.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T08:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72551",
    "user": "fwclarke"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072552.json:
```json
{
    "body": "Attachment [trac_8220-review.patch](tarball://root/attachments/some-uuid/ticket8220/trac_8220-review.patch) by ylchapuy created at 2010-02-11 08:40:15",
    "created_at": "2010-02-11T08:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72552",
    "user": "ylchapuy"
}
```

Attachment [trac_8220-review.patch](tarball://root/attachments/some-uuid/ticket8220/trac_8220-review.patch) by ylchapuy created at 2010-02-11 08:40:15



---

archive/issue_comments_072553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-11T08:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72553",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072554.json:
```json
{
    "body": "Replying to [comment:4 fwclarke]:\n> There's one doctest that needs modifying after this patch is applied\n\nOups, sorry, I don't knw how I missed that one...\nI made a tiny patch to correct this.",
    "created_at": "2010-02-11T08:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72554",
    "user": "ylchapuy"
}
```

Replying to [comment:4 fwclarke]:
> There's one doctest that needs modifying after this patch is applied

Oups, sorry, I don't knw how I missed that one...
I made a tiny patch to correct this.



---

archive/issue_comments_072555.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T20:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72555",
    "user": "fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072556.json:
```json
{
    "body": "It's okay now.",
    "created_at": "2010-02-11T20:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72556",
    "user": "fwclarke"
}
```

It's okay now.



---

archive/issue_comments_072557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72557",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_072558.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8220-finite_field_creation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-finite_field_creation.patch) --- I put in the ticket number for this patch.\n2. [trac_8220-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-review.patch) --- I put in a sensible commit message with the ticket number for this patch.",
    "created_at": "2010-02-14T14:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8220#issuecomment-72558",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8220-finite_field_creation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-finite_field_creation.patch) --- I put in the ticket number for this patch.
2. [trac_8220-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-review.patch) --- I put in a sensible commit message with the ticket number for this patch.
