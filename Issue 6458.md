# Issue 6458: Inverse modulo an ideal in a relative number field

archive/issues_006458.json:
```json
{
    "body": "Assignee: was\n\nThis adds a few lines to get `inverse_mod` working in the ring of integers of a relative field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6458\n\n",
    "created_at": "2009-07-02T13:27:16Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Inverse modulo an ideal in a relative number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6458",
    "user": "davidloeffler"
}
```
Assignee: was

This adds a few lines to get `inverse_mod` working in the ring of integers of a relative field.

Issue created by migration from https://trac.sagemath.org/ticket/6458





---

archive/issue_comments_052188.json:
```json
{
    "body": "patch against 4.1.alpha2",
    "created_at": "2009-07-02T13:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52188",
    "user": "davidloeffler"
}
```

patch against 4.1.alpha2



---

archive/issue_comments_052189.json:
```json
{
    "body": "Attachment [trac_6458-relative_ideal_inverse_mod.patch](tarball://root/attachments/some-uuid/ticket6458/trac_6458-relative_ideal_inverse_mod.patch) by davidloeffler created at 2009-07-02 13:35:14",
    "created_at": "2009-07-02T13:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52189",
    "user": "davidloeffler"
}
```

Attachment [trac_6458-relative_ideal_inverse_mod.patch](tarball://root/attachments/some-uuid/ticket6458/trac_6458-relative_ideal_inverse_mod.patch) by davidloeffler created at 2009-07-02 13:35:14



---

archive/issue_comments_052190.json:
```json
{
    "body": "These doctests don't actually assert that the results are correct.  Could you add the few lines verifying that you're really getting a basis and really getting an inverse?",
    "created_at": "2009-07-14T21:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52190",
    "user": "ncalexan"
}
```

These doctests don't actually assert that the results are correct.  Could you add the few lines verifying that you're really getting a basis and really getting an inverse?



---

archive/issue_comments_052191.json:
```json
{
    "body": "Also, I get a doctest failure on sage.math.  This could be transient -- this is with a slightly out of date sage build.  But there's no way this will work on all architectures, so testing the property will be much better.\n\n\n```\nsage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx\n**********************************************************************\nFile \"/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-main/sage/rings/number_field/number_field_element.pyx\", line 3436:\n    sage: OE(b - a).inverse_mod(17*b)\nExpected:\n    (-25*b + 26)*a + 51*b - 1\nGot:\n    (26*b - 25)*a - 51*b - 1\n```\n",
    "created_at": "2009-07-14T21:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52191",
    "user": "ncalexan"
}
```

Also, I get a doctest failure on sage.math.  This could be transient -- this is with a slightly out of date sage build.  But there's no way this will work on all architectures, so testing the property will be much better.


```
sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-main/sage/rings/number_field/number_field_element.pyx", line 3436:
    sage: OE(b - a).inverse_mod(17*b)
Expected:
    (-25*b + 26)*a + 51*b - 1
Got:
    (26*b - 25)*a - 51*b - 1
```




---

archive/issue_comments_052192.json:
```json
{
    "body": "Attachment [trac_6458-fix.patch](tarball://root/attachments/some-uuid/ticket6458/trac_6458-fix.patch) by davidloeffler created at 2009-07-14 22:04:13\n\napply after previous patch",
    "created_at": "2009-07-14T22:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52192",
    "user": "davidloeffler"
}
```

Attachment [trac_6458-fix.patch](tarball://root/attachments/some-uuid/ticket6458/trac_6458-fix.patch) by davidloeffler created at 2009-07-14 22:04:13

apply after previous patch



---

archive/issue_comments_052193.json:
```json
{
    "body": "Good point; I have uploaded a second patch that adjusts the doctests as you suggest.",
    "created_at": "2009-07-14T22:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52193",
    "user": "davidloeffler"
}
```

Good point; I have uploaded a second patch that adjusts the doctests as you suggest.



---

archive/issue_comments_052194.json:
```json
{
    "body": "Beautiful.",
    "created_at": "2009-07-15T02:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52194",
    "user": "ncalexan"
}
```

Beautiful.



---

archive/issue_comments_052195.json:
```json
{
    "body": "David, the patch `trac_6458-relative_ideal_inverse_mod.patch` doesn't have your username. So I'm committing it in your name. Merged both patches in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T19:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52195",
    "user": "mvngu"
}
```

David, the patch `trac_6458-relative_ideal_inverse_mod.patch` doesn't have your username. So I'm committing it in your name. Merged both patches in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_052196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6458#issuecomment-52196",
    "user": "mvngu"
}
```

Resolution: fixed
