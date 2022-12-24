# Issue 2073: calculus -- get doctest coverage up to 100%

archive/issues_002073.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2073\n\n",
    "created_at": "2008-02-06T09:00:28Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "calculus -- get doctest coverage up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2073",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/2073





---

archive/issue_comments_013408.json:
```json
{
    "body": "Attachment [calculus_doctest_improvements.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements.patch) by was created at 2008-02-06 09:06:00",
    "created_at": "2008-02-06T09:06:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13408",
    "user": "was"
}
```

Attachment [calculus_doctest_improvements.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements.patch) by was created at 2008-02-06 09:06:00



---

archive/issue_comments_013409.json:
```json
{
    "body": "Attachment [calculus_doctest_improvements-part2.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements-part2.patch) by was created at 2008-02-06 09:06:13",
    "created_at": "2008-02-06T09:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13409",
    "user": "was"
}
```

Attachment [calculus_doctest_improvements-part2.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements-part2.patch) by was created at 2008-02-06 09:06:13



---

archive/issue_comments_013410.json:
```json
{
    "body": "Attachment [calculus_doctest_improvements-part3.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements-part3.patch) by was created at 2008-02-06 09:06:28",
    "created_at": "2008-02-06T09:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13410",
    "user": "was"
}
```

Attachment [calculus_doctest_improvements-part3.patch](tarball://root/attachments/some-uuid/ticket2073/calculus_doctest_improvements-part3.patch) by was created at 2008-02-06 09:06:28



---

archive/issue_comments_013411.json:
```json
{
    "body": "Attachment [trac-2073-calculus_coverage_part4.patch](tarball://root/attachments/some-uuid/ticket2073/trac-2073-calculus_coverage_part4.patch) by was created at 2008-02-06 11:33:37\n\nAs of patch four, these are the only remaining public (not underscored) functions without proper documentation in the entire calculus directory:\n\n\n```\n\nMissing documentation:\n         * subs(self, *args, **kwds)\n         * substitute_over_ring(self, in_dict=None, ring=None, **kwds)\n         * str(self, bits=None)\n         * maxima_init(x)\n         * sys_init(x, system)\n         * var_cmp(x,y)\n         * CallableSymbolicExpressionRing(args, check=True)\n         * foo(n)\n         * args(self)\n         * plot(self, *args, **kwds)\n         * tex_needs_braces(self)\n         * simplify(self)\n\n\nMissing doctests:\n         * obj(self)\n         * variables(self, vars=tuple([]))\n         * integral(self, x=None, a=None, b=None)\n         * expression(self)\n```\n",
    "created_at": "2008-02-06T11:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13411",
    "user": "was"
}
```

Attachment [trac-2073-calculus_coverage_part4.patch](tarball://root/attachments/some-uuid/ticket2073/trac-2073-calculus_coverage_part4.patch) by was created at 2008-02-06 11:33:37

As of patch four, these are the only remaining public (not underscored) functions without proper documentation in the entire calculus directory:


```

Missing documentation:
         * subs(self, *args, **kwds)
         * substitute_over_ring(self, in_dict=None, ring=None, **kwds)
         * str(self, bits=None)
         * maxima_init(x)
         * sys_init(x, system)
         * var_cmp(x,y)
         * CallableSymbolicExpressionRing(args, check=True)
         * foo(n)
         * args(self)
         * plot(self, *args, **kwds)
         * tex_needs_braces(self)
         * simplify(self)


Missing doctests:
         * obj(self)
         * variables(self, vars=tuple([]))
         * integral(self, x=None, a=None, b=None)
         * expression(self)
```




---

archive/issue_comments_013412.json:
```json
{
    "body": "this is done and ready to be reviewed",
    "created_at": "2008-02-06T18:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13412",
    "user": "was"
}
```

this is done and ready to be reviewed



---

archive/issue_comments_013413.json:
```json
{
    "body": "Attachment [2073-random-doctests.patch](tarball://root/attachments/some-uuid/ticket2073/2073-random-doctests.patch) by mhansen created at 2008-02-07 09:05:18\n\nPositive review after applying the last patch as well.",
    "created_at": "2008-02-07T09:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13413",
    "user": "mhansen"
}
```

Attachment [2073-random-doctests.patch](tarball://root/attachments/some-uuid/ticket2073/2073-random-doctests.patch) by mhansen created at 2008-02-07 09:05:18

Positive review after applying the last patch as well.



---

archive/issue_comments_013414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T10:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13414",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013415.json:
```json
{
    "body": "Applied all five patches to Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T10:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2073#issuecomment-13415",
    "user": "mabshoff"
}
```

Applied all five patches to Sage 2.10.2.alpha0
