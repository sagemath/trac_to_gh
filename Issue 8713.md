# Issue 8713: Prepare the ground for moving Parent._an_element_ to Sets().ParentMethods

archive/issues_008713.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: an_element\n\nAs stated in the documentation of Parent._an_element_, this method\nneed not be blazingly fast since an_element is cached anyway. Also,\nhaving it implemented in Parent, rather than in the categories makes\nit impossible for categories to override this default implementation\nwith something more meaningful. Therefore it would be best moved to\nthe ParentMethods of Sets().\n\nThis first patch is a step in that direction. It just makes\n_an_element_ a def method rather than a cpdef method. This little\nchange by itself causes the recompilation of a big part of Sage, which\nmakes it completely impractical to work on a patch containing it (or\nin a patch queue containing it). So it would be nice to have this\npatch merged in Sage 4.4, so that we can start working comfortably on\nthe moving of _an_element_ once it has been merged in.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8713\n\n",
    "created_at": "2010-04-18T21:23:04Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "title": "Prepare the ground for moving Parent._an_element_ to Sets().ParentMethods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8713",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: an_element

As stated in the documentation of Parent._an_element_, this method
need not be blazingly fast since an_element is cached anyway. Also,
having it implemented in Parent, rather than in the categories makes
it impossible for categories to override this default implementation
with something more meaningful. Therefore it would be best moved to
the ParentMethods of Sets().

This first patch is a step in that direction. It just makes
_an_element_ a def method rather than a cpdef method. This little
change by itself causes the recompilation of a big part of Sage, which
makes it completely impractical to work on a patch containing it (or
in a patch queue containing it). So it would be nice to have this
patch merged in Sage 4.4, so that we can start working comfortably on
the moving of _an_element_ once it has been merged in.

Issue created by migration from https://trac.sagemath.org/ticket/8713





---

archive/issue_comments_079502.json:
```json
{
    "body": "Attachment [trac_8713-an_element-nt.patch](tarball://root/attachments/some-uuid/ticket8713/trac_8713-an_element-nt.patch) by nthiery created at 2010-04-18 21:45:57",
    "created_at": "2010-04-18T21:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79502",
    "user": "nthiery"
}
```

Attachment [trac_8713-an_element-nt.patch](tarball://root/attachments/some-uuid/ticket8713/trac_8713-an_element-nt.patch) by nthiery created at 2010-04-18 21:45:57



---

archive/issue_comments_079503.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-18T21:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79503",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079504.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-04-18T21:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79504",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_079505.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-19T21:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79505",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079506.json:
```json
{
    "body": "According to Robert Bradshaw:\n> Don't have time to review it, but sounds reasonable to me.\n\nMoreover patch look good and all tests are ok !",
    "created_at": "2010-04-19T21:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79506",
    "user": "hivert"
}
```

According to Robert Bradshaw:
> Don't have time to review it, but sounds reasonable to me.

Moreover patch look good and all tests are ok !



---

archive/issue_comments_079507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79507",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_079508.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8713#issuecomment-79508",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha2.
