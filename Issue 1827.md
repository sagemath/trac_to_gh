# Issue 1827: plot3d/transform.pyx test failure

archive/issues_001827.json:
```json
{
    "body": "Assignee: @williamstein\n\nFailure on make check\n\nsage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     \ufffd[?1034h**********************************************************************\nFile \"transform.pyx\", line 213:\n    sage: m\nExpected:\n    [                                                                                                                                        (x<sup>2*z</sup>2 - (cos(theta)*x^2 - cos(theta))*z<sup>2)/z</sup>2                                                                                                          (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*abs(z) - x*abs(z)) - sin(theta)*z^2)/abs(z)                                                                                                (-cos(theta)*x*z^2*abs(z) + x*z^2*abs(z) + sin(theta)*z<sup>2*sqrt(-z</sup>2 - x^2 + 1))/(z*abs(z))]\n    [                                                                                                            (sin(theta)*z^2*abs(z) - sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*z^2 - x*z<sup>2))/z</sup>2                                              ((-(x^2 + cos(theta) - 1)*z^2 - x^4 + 2*x^2 - 1)*abs(z) - (-cos(theta)*x<sup>2*z</sup>2 - cos(theta)*x^4 + cos(theta)*x<sup>2)*abs(z))/((x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x<sup>2*z</sup>2*abs(z) + (-x^2 - cos(theta) + 1)*z^2*abs(z)) + sin(theta)*x*z^4 - z<sup>2*(sin(theta)*x*z</sup>2 + sin(theta)*x^3 - sin(theta)*x))/((x^2 - 1)*z*abs(z))]\n    [                                                                                                               (-sin(theta)*z*sqrt(-z^2 - x^2 + 1)*abs(z) - cos(theta)*x*z^3 + x*z<sup>3)/z</sup>2                                               (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x^2*z*abs(z) + (-x^2 - cos(theta) + 1)*z*abs(z)) - (sin(theta)*x - sin(theta)*x<sup>3)*z)/((x</sup>2 - 1)*abs(z))                                                                        (((x^2 + cos(theta) - 1)*z^2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z))/((x^2 - 1)*abs(z))]\nGot:\n    [                                                                                                                                                                                                              sage17*cos(theta)*sqrt(1 - x^2) + sage13*sage76                                                                                                                                                                               (sqrt(-z^2 - x^2 + 1)*(sage76*abs(z) - cos(theta)*x*z) - sin(theta)*z*abs(z))/z                                                                                                                                                                               (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) + sage76*z*abs(z) - cos(theta)*x*z^2)/z]\n    [                                                                                                                 (sqrt(1 - x<sup>2)*sqrt(-z</sup>2 - x^2 + 1)*(sage17*cos(theta)*x*abs(z) + sage13*sage80*z) - sage17*sin(theta)*sqrt(1 - x<sup>2)*z</sup>2)/((x^2 - 1)*abs(z))                                          (-sqrt(1 - x<sup>2)*((-cos(theta)*x</sup>2*z^2 - cos(theta)*x^4 + cos(theta)*x^2)*abs(z) + cos(theta)*z^2*abs(z)) - ((sage80 - sage80*x<sup>2)*z</sup>2 - sage80*x^4 + 2*sage80*x^2 - sage80)*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z^2*abs(z) - cos(theta)*z^2*abs(z)) + (sage80*x^2 - sage80)*z^2*abs(z)) - sqrt(1 - x<sup>2)*(z</sup>2*(sin(theta)*x*z^2 + sin(theta)*x^3 - sin(theta)*x) - sin(theta)*x*z^4))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*z*abs(z))]\n    [                                                                                                               (sqrt(1 - x^2)*(sage17*cos(theta)*x*z*abs(z) + sage13*sage80*z^2) + sage17*sin(theta)*sqrt(1 - x<sup>2)*z*sqrt(-z</sup>2 - x^2 + 1))/((x^2 - 1)*abs(z))                                                   (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z*abs(z) - cos(theta)*z*abs(z)) + (sage80*x^2 - sage80)*z*abs(z)) - sqrt(1 - x^2)*(sin(theta)*x - sin(theta)*x^3)*z)/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))                                                                                       (sqrt(1 - x<sup>2)*((cos(theta)*z</sup>2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z)) + (sage80 - sage80*x<sup>2)*z</sup>2*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))]\n**********************************************************************\n\nSystem is 64 bit gentoo, gcc 4.2.2\n\nIssue created by migration from https://trac.sagemath.org/ticket/1827\n\n",
    "created_at": "2008-01-18T05:46:27Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "plot3d/transform.pyx test failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1827",
    "user": "@garyfurnish"
}
```
Assignee: @williamstein

Failure on make check

sage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     �[?1034h**********************************************************************
File "transform.pyx", line 213:
    sage: m
Expected:
    [                                                                                                                                        (x<sup>2*z</sup>2 - (cos(theta)*x^2 - cos(theta))*z<sup>2)/z</sup>2                                                                                                          (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*abs(z) - x*abs(z)) - sin(theta)*z^2)/abs(z)                                                                                                (-cos(theta)*x*z^2*abs(z) + x*z^2*abs(z) + sin(theta)*z<sup>2*sqrt(-z</sup>2 - x^2 + 1))/(z*abs(z))]
    [                                                                                                            (sin(theta)*z^2*abs(z) - sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*z^2 - x*z<sup>2))/z</sup>2                                              ((-(x^2 + cos(theta) - 1)*z^2 - x^4 + 2*x^2 - 1)*abs(z) - (-cos(theta)*x<sup>2*z</sup>2 - cos(theta)*x^4 + cos(theta)*x<sup>2)*abs(z))/((x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x<sup>2*z</sup>2*abs(z) + (-x^2 - cos(theta) + 1)*z^2*abs(z)) + sin(theta)*x*z^4 - z<sup>2*(sin(theta)*x*z</sup>2 + sin(theta)*x^3 - sin(theta)*x))/((x^2 - 1)*z*abs(z))]
    [                                                                                                               (-sin(theta)*z*sqrt(-z^2 - x^2 + 1)*abs(z) - cos(theta)*x*z^3 + x*z<sup>3)/z</sup>2                                               (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x^2*z*abs(z) + (-x^2 - cos(theta) + 1)*z*abs(z)) - (sin(theta)*x - sin(theta)*x<sup>3)*z)/((x</sup>2 - 1)*abs(z))                                                                        (((x^2 + cos(theta) - 1)*z^2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z))/((x^2 - 1)*abs(z))]
Got:
    [                                                                                                                                                                                                              sage17*cos(theta)*sqrt(1 - x^2) + sage13*sage76                                                                                                                                                                               (sqrt(-z^2 - x^2 + 1)*(sage76*abs(z) - cos(theta)*x*z) - sin(theta)*z*abs(z))/z                                                                                                                                                                               (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) + sage76*z*abs(z) - cos(theta)*x*z^2)/z]
    [                                                                                                                 (sqrt(1 - x<sup>2)*sqrt(-z</sup>2 - x^2 + 1)*(sage17*cos(theta)*x*abs(z) + sage13*sage80*z) - sage17*sin(theta)*sqrt(1 - x<sup>2)*z</sup>2)/((x^2 - 1)*abs(z))                                          (-sqrt(1 - x<sup>2)*((-cos(theta)*x</sup>2*z^2 - cos(theta)*x^4 + cos(theta)*x^2)*abs(z) + cos(theta)*z^2*abs(z)) - ((sage80 - sage80*x<sup>2)*z</sup>2 - sage80*x^4 + 2*sage80*x^2 - sage80)*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z^2*abs(z) - cos(theta)*z^2*abs(z)) + (sage80*x^2 - sage80)*z^2*abs(z)) - sqrt(1 - x<sup>2)*(z</sup>2*(sin(theta)*x*z^2 + sin(theta)*x^3 - sin(theta)*x) - sin(theta)*x*z^4))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*z*abs(z))]
    [                                                                                                               (sqrt(1 - x^2)*(sage17*cos(theta)*x*z*abs(z) + sage13*sage80*z^2) + sage17*sin(theta)*sqrt(1 - x<sup>2)*z*sqrt(-z</sup>2 - x^2 + 1))/((x^2 - 1)*abs(z))                                                   (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z*abs(z) - cos(theta)*z*abs(z)) + (sage80*x^2 - sage80)*z*abs(z)) - sqrt(1 - x^2)*(sin(theta)*x - sin(theta)*x^3)*z)/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))                                                                                       (sqrt(1 - x<sup>2)*((cos(theta)*z</sup>2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z)) + (sage80 - sage80*x<sup>2)*z</sup>2*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))]
**********************************************************************

System is 64 bit gentoo, gcc 4.2.2

Issue created by migration from https://trac.sagemath.org/ticket/1827





---

archive/issue_comments_011568.json:
```json
{
    "body": "Changing component from graphics to doctest.",
    "created_at": "2008-01-18T05:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11568",
    "user": "mabshoff"
}
```

Changing component from graphics to doctest.



---

archive/issue_comments_011569.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2008-01-18T05:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11569",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_comments_011570.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-01-18T05:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11570",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_011571.json:
```json
{
    "body": "Attachment [trac-1827.patch](tarball://root/attachments/some-uuid/ticket1827/trac-1827.patch) by @williamstein created at 2008-01-18 22:54:11\n\nthis should completely fix the problem.  But I've only tested it on one 32-bit linux system.  it needs more testing",
    "created_at": "2008-01-18T22:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11571",
    "user": "@williamstein"
}
```

Attachment [trac-1827.patch](tarball://root/attachments/some-uuid/ticket1827/trac-1827.patch) by @williamstein created at 2008-01-18 22:54:11

this should completely fix the problem.  But I've only tested it on one 32-bit linux system.  it needs more testing



---

archive/issue_comments_011572.json:
```json
{
    "body": "For _an_element_impl, it should return a very generic element. If it returns zero, then it may mess up the coercion model!",
    "created_at": "2008-01-19T04:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11572",
    "user": "@robertwb"
}
```

For _an_element_impl, it should return a very generic element. If it returns zero, then it may mess up the coercion model!



---

archive/issue_comments_011573.json:
```json
{
    "body": "Hi Robert,\n\ncan you provide a doctest that exposes the issue you describe?\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T04:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11573",
    "user": "mabshoff"
}
```

Hi Robert,

can you provide a doctest that exposes the issue you describe?

Cheers,

Michael



---

archive/issue_comments_011574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T13:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11574",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_011575.json:
```json
{
    "body": "OK, I take this back. \n\nIt used to be that some multiplication code was written as \n\n\n```\ndef _lmul_(self, other):\n    if not other:\n        return other\n    ...\n```\n\n\nThis would succeed when other was ANY type with bool(other) == False, and an_element was used to construct `other` to pass in and try it out (in the action detection code) which would cause it to succeed and this \"valid\" action would get cached (resulting in a error or segfault when a non-zero `other` was passed. \n\nIt now forces other to be an element of self.parent().base_ring(), which solves this problem.",
    "created_at": "2008-01-19T19:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1827#issuecomment-11575",
    "user": "@robertwb"
}
```

OK, I take this back. 

It used to be that some multiplication code was written as 


```
def _lmul_(self, other):
    if not other:
        return other
    ...
```


This would succeed when other was ANY type with bool(other) == False, and an_element was used to construct `other` to pass in and try it out (in the action detection code) which would cause it to succeed and this "valid" action would get cached (resulting in a error or segfault when a non-zero `other` was passed. 

It now forces other to be an element of self.parent().base_ring(), which solves this problem.
