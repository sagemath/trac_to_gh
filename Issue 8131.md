# Issue 8131: Catalan numbers are integers

archive/issues_008131.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: Catalan numbers\n\nThe patch makes Sage aware of this fact.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8131\n\n",
    "created_at": "2010-01-30T09:40:20Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "title": "Catalan numbers are integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8131",
    "user": "fwclarke"
}
```
Assignee: sage-combinat

Keywords: Catalan numbers

The patch makes Sage aware of this fact.

Issue created by migration from https://trac.sagemath.org/ticket/8131





---

archive/issue_comments_071488.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-30T09:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71488",
    "user": "fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071489.json:
```json
{
    "body": "Attachment [trac_8131.patch](tarball://root/attachments/some-uuid/ticket8131/trac_8131.patch) by fwclarke created at 2010-01-30 09:42:37",
    "created_at": "2010-01-30T09:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71489",
    "user": "fwclarke"
}
```

Attachment [trac_8131.patch](tarball://root/attachments/some-uuid/ticket8131/trac_8131.patch) by fwclarke created at 2010-01-30 09:42:37



---

archive/issue_comments_071490.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-30T21:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71490",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071491.json:
```json
{
    "body": "Thanks for spotting and fixing this!\n\nPlease add an:\n\n```\nOUTPUT: integer\n```\n\nline in the documentation, as per http://www.sagemath.org/doc/developer/conventions.html#documentation-strings, as well an\nexample in the doctests showing/testing that property, and I'll set a positive review!\n\nNote: you may want to use the method divide_knowing_divisible_by on ZZ elements.",
    "created_at": "2010-01-30T21:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71491",
    "user": "nthiery"
}
```

Thanks for spotting and fixing this!

Please add an:

```
OUTPUT: integer
```

line in the documentation, as per http://www.sagemath.org/doc/developer/conventions.html#documentation-strings, as well an
example in the doctests showing/testing that property, and I'll set a positive review!

Note: you may want to use the method divide_knowing_divisible_by on ZZ elements.



---

archive/issue_comments_071492.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\n\nIn the replacement patch I've improved the documentation and added a doctest as suggested.\n\nIn addition, I've simplified an existing doctest and slightly modified another (because `divide_knowing_divisible_by` gives a different error when trying to divide by zero).  I've made one more adjustment to the documentation so that the mathematics displays properly; at least it does in the notebook now.",
    "created_at": "2010-02-06T13:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71492",
    "user": "fwclarke"
}
```

Replying to [comment:2 nthiery]:

In the replacement patch I've improved the documentation and added a doctest as suggested.

In addition, I've simplified an existing doctest and slightly modified another (because `divide_knowing_divisible_by` gives a different error when trying to divide by zero).  I've made one more adjustment to the documentation so that the mathematics displays properly; at least it does in the notebook now.



---

archive/issue_comments_071493.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-06T13:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71493",
    "user": "fwclarke"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071494.json:
```json
{
    "body": "replaces earlier patch, based on 4.3.1",
    "created_at": "2010-02-06T13:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71494",
    "user": "fwclarke"
}
```

replaces earlier patch, based on 4.3.1



---

archive/issue_comments_071495.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-23T23:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71495",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071496.json:
```json
{
    "body": "Attachment [trac_8131-replacement.patch](tarball://root/attachments/some-uuid/ticket8131/trac_8131-replacement.patch) by nborie created at 2010-02-23 23:09:08\n\nIt's look good for code, test and applying. I give this patch a positive review.",
    "created_at": "2010-02-23T23:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71496",
    "user": "nborie"
}
```

Attachment [trac_8131-replacement.patch](tarball://root/attachments/some-uuid/ticket8131/trac_8131-replacement.patch) by nborie created at 2010-02-23 23:09:08

It's look good for code, test and applying. I give this patch a positive review.



---

archive/issue_comments_071497.json:
```json
{
    "body": "Merged [trac_8131-replacement.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8131/trac_8131-replacement.patch).\n\n\n\nFrancis: You should put the ticket number in your commit message.",
    "created_at": "2010-03-02T21:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71497",
    "user": "mvngu"
}
```

Merged [trac_8131-replacement.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8131/trac_8131-replacement.patch).



Francis: You should put the ticket number in your commit message.



---

archive/issue_comments_071498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71498",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071499.json:
```json
{
    "body": "Changing keywords from \"Catalan numbers\" to \"catalan\".",
    "created_at": "2016-12-06T13:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71499",
    "user": "pelegm"
}
```

Changing keywords from "Catalan numbers" to "catalan".



---

archive/issue_comments_071500.json:
```json
{
    "body": "Replying to [comment:6 pelegm]:\n\nThe trouble with using the keyword 'catalan' is that it makes it look as though it concerns the Catalan constant rather than the Catalan numbers:\n\n```\nsage: catalan.n()\n0.915965594177219\nsage: catalan_number(7)\n429\n```\n",
    "created_at": "2016-12-07T14:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8131#issuecomment-71500",
    "user": "fwclarke"
}
```

Replying to [comment:6 pelegm]:

The trouble with using the keyword 'catalan' is that it makes it look as though it concerns the Catalan constant rather than the Catalan numbers:

```
sage: catalan.n()
0.915965594177219
sage: catalan_number(7)
429
```

