# Issue 3698: [with patch; needs review] add multinomial_coefficients and binomial_coefficients to sage.

archive/issues_003698.json:
```json
{
    "body": "Assignee: somebody\n\nPearu Peterson (sympycore guy) wrote some really fast pure python code for computing multinomial coefficients, e.g.,\n\n```\n14:20 < wstein> sage: R.<x,y,z> = QQ[]\n14:20 < wstein> sage: timeit('(x+y+z)^50')\n14:20 < wstein> 25 loops, best of 3: 20.8 ms per loop\n14:20 < wstein> sage: timeit('w = multinomial_coefficients(3r,50r)')\n14:20 < wstein> 25 loops, best of 3: 10.3 ms per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3698\n\n",
    "created_at": "2008-07-21T21:28:22Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch; needs review] add multinomial_coefficients and binomial_coefficients to sage.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3698",
    "user": "was"
}
```
Assignee: somebody

Pearu Peterson (sympycore guy) wrote some really fast pure python code for computing multinomial coefficients, e.g.,

```
14:20 < wstein> sage: R.<x,y,z> = QQ[]
14:20 < wstein> sage: timeit('(x+y+z)^50')
14:20 < wstein> 25 loops, best of 3: 20.8 ms per loop
14:20 < wstein> sage: timeit('w = multinomial_coefficients(3r,50r)')
14:20 < wstein> 25 loops, best of 3: 10.3 ms per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/3698





---

archive/issue_comments_026238.json:
```json
{
    "body": "Attachment [sage-3698.patch](tarball://root/attachments/some-uuid/ticket3698/sage-3698.patch) by was created at 2008-07-21 21:28:45",
    "created_at": "2008-07-21T21:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26238",
    "user": "was"
}
```

Attachment [sage-3698.patch](tarball://root/attachments/some-uuid/ticket3698/sage-3698.patch) by was created at 2008-07-21 21:28:45



---

archive/issue_comments_026239.json:
```json
{
    "body": "+1 from me, nice docstrings and a simple test for each method.",
    "created_at": "2008-07-21T21:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26239",
    "user": "certik"
}
```

+1 from me, nice docstrings and a simple test for each method.



---

archive/issue_comments_026240.json:
```json
{
    "body": "Attachment [sage-3698-part2.patch](tarball://root/attachments/some-uuid/ticket3698/sage-3698-part2.patch) by was created at 2008-07-21 21:53:54",
    "created_at": "2008-07-21T21:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26240",
    "user": "was"
}
```

Attachment [sage-3698-part2.patch](tarball://root/attachments/some-uuid/ticket3698/sage-3698-part2.patch) by was created at 2008-07-21 21:53:54



---

archive/issue_comments_026241.json:
```json
{
    "body": "\n```\n14:56 < wstein> pearu -- ar eyou giving 3698 a positive review?\n14:57 < pearu> wstein, yes, it looks good, I presume you have tested that the code works:)\n14:57 < wstein> yes\n```\n",
    "created_at": "2008-07-21T22:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26241",
    "user": "was"
}
```


```
14:56 < wstein> pearu -- ar eyou giving 3698 a positive review?
14:57 < pearu> wstein, yes, it looks good, I presume you have tested that the code works:)
14:57 < wstein> yes
```




---

archive/issue_comments_026242.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha0",
    "created_at": "2008-07-31T00:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26242",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.1.alpha0



---

archive/issue_comments_026243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T00:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3698",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3698#issuecomment-26243",
    "user": "mabshoff"
}
```

Resolution: fixed
