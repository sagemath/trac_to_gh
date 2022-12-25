# Issue 8719: convert RDF/CDF matrices to numpy

archive/issues_008719.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer\n\nThis patch makes the following work:\n\n\n```\n            sage: import numpy\n            sage: m = matrix(RDF, 2, range(6)); m\n            [0.0 1.0 2.0]\n            [3.0 4.0 5.0]\n            sage: numpy.array(m)                  \n            array([[ 0.,  1.,  2.],\n            [ 3.,  4.,  5.]])\n            sage: numpy.array(m).dtype            \n            dtype('float64')\n            sage: m = matrix(CDF, 2, range(6)); m\n            [  0 1.0 2.0]\n            [3.0 4.0 5.0]\n            sage: numpy.array(m)                  \n            array([[ 0.+0.j,  1.+0.j,  2.+0.j],\n            [ 3.+0.j,  4.+0.j,  5.+0.j]])\n            sage: numpy.array(m).dtype            \n            dtype('complex128')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8719\n\n",
    "created_at": "2010-04-20T00:07:17Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "convert RDF/CDF matrices to numpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8719",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @rbeezer

This patch makes the following work:


```
            sage: import numpy
            sage: m = matrix(RDF, 2, range(6)); m
            [0.0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)                  
            array([[ 0.,  1.,  2.],
            [ 3.,  4.,  5.]])
            sage: numpy.array(m).dtype            
            dtype('float64')
            sage: m = matrix(CDF, 2, range(6)); m
            [  0 1.0 2.0]
            [3.0 4.0 5.0]
            sage: numpy.array(m)                  
            array([[ 0.+0.j,  1.+0.j,  2.+0.j],
            [ 3.+0.j,  4.+0.j,  5.+0.j]])
            sage: numpy.array(m).dtype            
            dtype('complex128')
```


Issue created by migration from https://trac.sagemath.org/ticket/8719





---

archive/issue_comments_079462.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T00:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79462",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079463.json:
```json
{
    "body": "Changing assignee from jason, was to @jasongrout.",
    "created_at": "2010-05-03T19:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79463",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from jason, was to @jasongrout.



---

archive/issue_comments_079464.json:
```json
{
    "body": "rbeezer: it seems like you could naturally review this.  It just adds a numpy-specific magic method for conversion.",
    "created_at": "2010-05-03T19:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79464",
    "user": "https://github.com/jasongrout"
}
```

rbeezer: it seems like you could naturally review this.  It just adds a numpy-specific magic method for conversion.



---

archive/issue_comments_079465.json:
```json
{
    "body": "Hi Jason,\n\nSo you have defined a new method \"`__array__`\" for a Sage matrix object.  When somebody calls numpy.array(a) for a Sage matrix  a  then this `__array__` method gets called (and this is in effect just the numpy() method of a Sage matrix)?  In other words, the numpy.array() method has an expanded reportoire and now \"knows\" how to deal with a Sage matrix object?\n\nIf so, could you say so?  The line  `__array__=numpy` all by itself looks really mysterious with no documentation.  And the new doctests say \"you could use numpy\" - when Sage is really doing the heavy-lifting?  It sounds like numpy is doing the work, when this is not a standard behavior of numpy.\n\nSo I'm suggesting maybe this seemingly circular arrrangement (modify Sage matrices, so numpy can deal with them, using a Sage function to convert to a numpy array) could be better explained so nobody messes it up or gets too confused.  With the added code and the added doctests all together, I think I was able to figure this out - otherwise it would have been a head-scratcher.\n\nRob",
    "created_at": "2010-05-04T04:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79465",
    "user": "https://github.com/rbeezer"
}
```

Hi Jason,

So you have defined a new method "`__array__`" for a Sage matrix object.  When somebody calls numpy.array(a) for a Sage matrix  a  then this `__array__` method gets called (and this is in effect just the numpy() method of a Sage matrix)?  In other words, the numpy.array() method has an expanded reportoire and now "knows" how to deal with a Sage matrix object?

If so, could you say so?  The line  `__array__=numpy` all by itself looks really mysterious with no documentation.  And the new doctests say "you could use numpy" - when Sage is really doing the heavy-lifting?  It sounds like numpy is doing the work, when this is not a standard behavior of numpy.

So I'm suggesting maybe this seemingly circular arrrangement (modify Sage matrices, so numpy can deal with them, using a Sage function to convert to a numpy array) could be better explained so nobody messes it up or gets too confused.  With the added code and the added doctests all together, I think I was able to figure this out - otherwise it would have been a head-scratcher.

Rob



---

archive/issue_comments_079466.json:
```json
{
    "body": "Attachment [trac_8719-numpy-conversion.patch](tarball://root/attachments/some-uuid/ticket8719/trac_8719-numpy-conversion.patch) by @jasongrout created at 2010-05-04 05:11:23",
    "created_at": "2010-05-04T05:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79466",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_8719-numpy-conversion.patch](tarball://root/attachments/some-uuid/ticket8719/trac_8719-numpy-conversion.patch) by @jasongrout created at 2010-05-04 05:11:23



---

archive/issue_comments_079467.json:
```json
{
    "body": "I updated the docs.",
    "created_at": "2010-05-04T05:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79467",
    "user": "https://github.com/jasongrout"
}
```

I updated the docs.



---

archive/issue_comments_079468.json:
```json
{
    "body": "Replying to [comment:7 jason]:\n> I updated the docs.\n\nLooks good!  I'll finish this tomorrow night.",
    "created_at": "2010-05-04T06:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79468",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:7 jason]:
> I updated the docs.

Looks good!  I'll finish this tomorrow night.



---

archive/issue_comments_079469.json:
```json
{
    "body": "Looks good, builds and passes all tests, documentation builds without warnings.\n\nThe added documentation looks great.\n\nPositive review.",
    "created_at": "2010-05-05T06:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79469",
    "user": "https://github.com/rbeezer"
}
```

Looks good, builds and passes all tests, documentation builds without warnings.

The added documentation looks great.

Positive review.



---

archive/issue_comments_079470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-05T06:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79470",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8719#issuecomment-79471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008889.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-05-08T22:03:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8719",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8719#event-8889"
}
```
