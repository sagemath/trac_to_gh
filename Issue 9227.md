# Issue 9227: units.length.millimeter missing

archive/issues_009227.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  asjarman@xtra.co.nz\n\na millimeter [mm] is 1/1000 of a meter and very often used by engineers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9227\n\n",
    "created_at": "2010-06-12T12:55:42Z",
    "labels": [
        "component: algebra",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "units.length.millimeter missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9227",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @aghitza

CC:  asjarman@xtra.co.nz

a millimeter [mm] is 1/1000 of a meter and very often used by engineers.

Issue created by migration from https://trac.sagemath.org/ticket/9227





---

archive/issue_comments_086446.json:
```json
{
    "body": "Attachment [trac_9227_mm_and_km_units.patch](tarball://root/attachments/some-uuid/ticket9227/trac_9227_mm_and_km_units.patch) by allmar created at 2010-08-27 23:01:00\n\npatch to add mm and km",
    "created_at": "2010-08-27T23:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86446",
    "user": "https://trac.sagemath.org/admin/accounts/users/allmar"
}
```

Attachment [trac_9227_mm_and_km_units.patch](tarball://root/attachments/some-uuid/ticket9227/trac_9227_mm_and_km_units.patch) by allmar created at 2010-08-27 23:01:00

patch to add mm and km



---

archive/issue_comments_086447.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-29T06:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86447",
    "user": "https://trac.sagemath.org/admin/accounts/users/allmar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086448.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2010-09-02T11:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86448",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_086449.json:
```json
{
    "body": "You mentioned\n\n```\nEqual to 1000 meters.\n```\n\ntwice. You should replace one by a comparison to yards, feet or something else.",
    "created_at": "2011-01-07T09:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86449",
    "user": "https://github.com/a-andre"
}
```

You mentioned

```
Equal to 1000 meters.
```

twice. You should replace one by a comparison to yards, feet or something else.



---

archive/issue_comments_086450.json:
```json
{
    "body": "Attachment [trac_9227_mm_and_km_units.2.patch](tarball://root/attachments/some-uuid/ticket9227/trac_9227_mm_and_km_units.2.patch) by @haikona created at 2011-01-07 22:56:41",
    "created_at": "2011-01-07T22:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86450",
    "user": "https://github.com/haikona"
}
```

Attachment [trac_9227_mm_and_km_units.2.patch](tarball://root/attachments/some-uuid/ticket9227/trac_9227_mm_and_km_units.2.patch) by @haikona created at 2011-01-07 22:56:41



---

archive/issue_comments_086451.json:
```json
{
    "body": "Doctests fail due to there being TAB characters in this patch.\n\nI've added an updated patch, which replaces the TAB characters in the patch with spaces, as well as changing line 650:\n`'kilometer':'Equal to 1000 meters.\\nEqual to 1000 meters.',`\nto\n`'kilometer':'Equal to 1000 meters.\\nEqual to 3280.8399 feet.',`",
    "created_at": "2011-01-07T23:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86451",
    "user": "https://github.com/haikona"
}
```

Doctests fail due to there being TAB characters in this patch.

I've added an updated patch, which replaces the TAB characters in the patch with spaces, as well as changing line 650:
`'kilometer':'Equal to 1000 meters.\nEqual to 1000 meters.',`
to
`'kilometer':'Equal to 1000 meters.\nEqual to 3280.8399 feet.',`



---

archive/issue_comments_086452.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2011-01-10T01:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86452",
    "user": "https://github.com/adeines"
}
```

Looks good to me.



---

archive/issue_comments_086453.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T01:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86453",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086454.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9227",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9227#issuecomment-86454",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
