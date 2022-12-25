# Issue 2977: [with patch, needs review] wronskian is broken on constants

archive/issues_002977.json:
```json
{
    "body": "Assignee: @williamstein\n\nHi,\n\nHere's something unpleasant that occurs in sage-3.0.rc0:\n\n\n```\nsage: wronskian(1, e^(-x), e^(2*x))\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/root/<ipython console> in <module>()\n\n/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in wronskian(*args)\n     80             # if the last argument isn't a variable, just run\n     81             # .derivative on everything \n     82             fs = args\n     83             row = lambda n: map(lambda f: f.derivative(n), fs)\n---> 84         return matrix(map(row, range(len(fs)))).determinant()\n\n/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(n)\n     80             # if the last argument isn't a variable, just run\n     81             # .derivative on everything \n     82             fs = args\n---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)\n     84         return matrix(map(row, range(len(fs)))).determinant()\n\n/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(f)\n     80             # if the last argument isn't a variable, just run\n     81             # .derivative on everything \n     82             fs = args\n---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)\n     84         return matrix(map(row, range(len(fs)))).determinant()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute 'derivative'\n```\n\n\nThere is an easy fix, see the patch.  I have also removed \"differentiate\" as an alias for \"derivative\", since I seem to remember that the consensus on sage-devel was to keep only \"derivative\" and \"diff\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2977\n\n",
    "created_at": "2008-04-21T00:35:15Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] wronskian is broken on constants",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2977",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Hi,

Here's something unpleasant that occurs in sage-3.0.rc0:


```
sage: wronskian(1, e^(-x), e^(2*x))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/root/<ipython console> in <module>()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in wronskian(*args)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
     83             row = lambda n: map(lambda f: f.derivative(n), fs)
---> 84         return matrix(map(row, range(len(fs)))).determinant()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(n)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)
     84         return matrix(map(row, range(len(fs)))).determinant()

/opt/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/calculus/functions.py in <lambda>(f)
     80             # if the last argument isn't a variable, just run
     81             # .derivative on everything 
     82             fs = args
---> 83             row = lambda n: map(lambda f: f.derivative(n), fs)
     84         return matrix(map(row, range(len(fs)))).determinant()

<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute 'derivative'
```


There is an easy fix, see the patch.  I have also removed "differentiate" as an alias for "derivative", since I seem to remember that the consensus on sage-devel was to keep only "derivative" and "diff".


Issue created by migration from https://trac.sagemath.org/ticket/2977





---

archive/issue_comments_020463.json:
```json
{
    "body": "Attachment [wronskian_constants.patch](tarball://root/attachments/some-uuid/ticket2977/wronskian_constants.patch) by @mwhansen created at 2008-04-21 02:02:32\n\nLooks good to me.",
    "created_at": "2008-04-21T02:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2977#issuecomment-20463",
    "user": "https://github.com/mwhansen"
}
```

Attachment [wronskian_constants.patch](tarball://root/attachments/some-uuid/ticket2977/wronskian_constants.patch) by @mwhansen created at 2008-04-21 02:02:32

Looks good to me.



---

archive/issue_comments_020464.json:
```json
{
    "body": "Merged in Sage 3.0.rc1",
    "created_at": "2008-04-21T02:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2977#issuecomment-20464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.rc1



---

archive/issue_comments_020465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T02:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2977#issuecomment-20465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
