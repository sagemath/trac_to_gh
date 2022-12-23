# Issue 7918: log(float(_)) is really slow

archive/issues_007918.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nKeywords: log\n\nSomewhere between 4.1 and 4.3, log(x) got really slow when x is a float.\n\nExample:\n\n\n\n```\nsage: version()\n'Sage Version 4.3, Release Date: 2009-12-24'\nsage: x = float(5)\nsage: x\n5.0\nsage: timeit('log(x)')\n625 loops, best of 3: 362 \u00b5s per loop\n```\n\n\n\n```\nsage: version()\n'Sage Version 4.1, Release Date: 2009-07-09'\nsage: x = float(5)\nsage: timeit('log(x)')\n625 loops, best of 3: 7.26 \u00b5s per loop\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7918\n\n",
    "created_at": "2010-01-13T06:55:34Z",
    "labels": [
        "performance",
        "major",
        "bug"
    ],
    "title": "log(float(_)) is really slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7918",
    "user": "bober"
}
```
Assignee: tbd

CC:  mvngu

Keywords: log

Somewhere between 4.1 and 4.3, log(x) got really slow when x is a float.

Example:



```
sage: version()
'Sage Version 4.3, Release Date: 2009-12-24'
sage: x = float(5)
sage: x
5.0
sage: timeit('log(x)')
625 loops, best of 3: 362 µs per loop
```



```
sage: version()
'Sage Version 4.1, Release Date: 2009-07-09'
sage: x = float(5)
sage: timeit('log(x)')
625 loops, best of 3: 7.26 µs per loop
```




Issue created by migration from https://trac.sagemath.org/ticket/7918





---

archive/issue_comments_068899.json:
```json
{
    "body": "Although it is not the same issue, this will be fixed by #7822. I have a new patch for that problem which brings the timings back to comparable values.",
    "created_at": "2010-01-13T09:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7918#issuecomment-68899",
    "user": "burcin"
}
```

Although it is not the same issue, this will be fixed by #7822. I have a new patch for that problem which brings the timings back to comparable values.



---

archive/issue_comments_068900.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-19T11:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7918#issuecomment-68900",
    "user": "burcin"
}
```

Resolution: fixed



---

archive/issue_comments_068901.json:
```json
{
    "body": "I'm closing this since #7822 was merged and it addresses this issue.",
    "created_at": "2010-02-19T11:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7918#issuecomment-68901",
    "user": "burcin"
}
```

I'm closing this since #7822 was merged and it addresses this issue.
