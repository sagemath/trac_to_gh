# Issue 2035: sage-2.10.1.rc5: transform.pyx is now broken (probably caused by other fixes)

archive/issues_002035.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     **********************************************************************\nFile \"transform.pyx\", line 212:\n    sage: m\nExpected: \n    [                                       (1 - cos(theta))*x^2 + cos(theta) (-sin(theta)*abs(z)^3 - (cos(theta) - 1)*x*z^2*sqrt(-z^2 - x^2 + 1))/z^2  (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z)^3 + (1 - cos(theta))*x*z^4)/z^3]\n    [             sin(theta)*abs(z) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                          (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1     (-sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z]\n    [    (-sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) - (cos(theta) - 1)*x*z^2)/z      (sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z                                        (1 - cos(theta))*z^2 + cos(th\neta)]\nGot:\n    [                                              (1 - cos(theta))*x^2 + cos(theta)                  (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1) - sin(theta)*sqrt(z^2)          (sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) + \n(1 - cos(theta))*x*z^2)/z]\n    [                 sin(theta)*sqrt(z^2) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                                 (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1 (-(cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - \nsin(theta)*x*z)/sqrt(z^2)]\n    [        (-sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - (cos(theta) - 1)*x*z^2)/z  (sin(theta)*x*z - (cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2))/sqrt(z^2)                                               (1 - cos\n(theta))*z^2 + cos(theta)]\n**********************************************************************\n1 items had failures:\n   1 of  25 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_transform.pyx\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2035\n\n",
    "created_at": "2008-02-03T00:14:24Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "title": "sage-2.10.1.rc5: transform.pyx is now broken (probably caused by other fixes)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2035",
    "user": "was"
}
```
Assignee: was


```
sage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     **********************************************************************
File "transform.pyx", line 212:
    sage: m
Expected: 
    [                                       (1 - cos(theta))*x^2 + cos(theta) (-sin(theta)*abs(z)^3 - (cos(theta) - 1)*x*z^2*sqrt(-z^2 - x^2 + 1))/z^2  (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z)^3 + (1 - cos(theta))*x*z^4)/z^3]
    [             sin(theta)*abs(z) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                          (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1     (-sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z]
    [    (-sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) - (cos(theta) - 1)*x*z^2)/z      (sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z                                        (1 - cos(theta))*z^2 + cos(th
eta)]
Got:
    [                                              (1 - cos(theta))*x^2 + cos(theta)                  (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1) - sin(theta)*sqrt(z^2)          (sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) + 
(1 - cos(theta))*x*z^2)/z]
    [                 sin(theta)*sqrt(z^2) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                                 (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1 (-(cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - 
sin(theta)*x*z)/sqrt(z^2)]
    [        (-sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - (cos(theta) - 1)*x*z^2)/z  (sin(theta)*x*z - (cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2))/sqrt(z^2)                                               (1 - cos
(theta))*z^2 + cos(theta)]
**********************************************************************
1 items had failures:
   1 of  25 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_transform.pyx
```


Issue created by migration from https://trac.sagemath.org/ticket/2035





---

archive/issue_comments_013170.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-03T00:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2035#issuecomment-13170",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_013171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-03T00:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2035#issuecomment-13171",
    "user": "was"
}
```

Resolution: fixed
