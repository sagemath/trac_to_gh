# Issue 2658: Matrix from a vector doesn't preserve the vector's parent ring automatically

archive/issues_002658.json:
```json
{
    "body": "Assignee: @williamstein\n\nCreating a matrix from a vector doesn't preserve the vector's parent ring automatically.:\n\n\n```\nsage: v = vector(RR,range(5)) ; v ; v.parent()\n (0.000000000000000, 1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000)\n Vector space of dimension 5 over Real Field with 53 bits of precision\n\nsage: M=matrix(v) ; M ; M.parent()\n [0 1 2 3 4]\n Full MatrixSpace of 1 by 5 dense matrices over Integer Ring\n```\n\n\nThis works if you specify the ring explicitly (ie  `Matrix(RR,v)` ) but I don't see why sage can't do the \"right\" thing automatically.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2658\n\n",
    "created_at": "2008-03-24T03:13:50Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Matrix from a vector doesn't preserve the vector's parent ring automatically",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2658",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

Creating a matrix from a vector doesn't preserve the vector's parent ring automatically.:


```
sage: v = vector(RR,range(5)) ; v ; v.parent()
 (0.000000000000000, 1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000)
 Vector space of dimension 5 over Real Field with 53 bits of precision

sage: M=matrix(v) ; M ; M.parent()
 [0 1 2 3 4]
 Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
```


This works if you specify the ring explicitly (ie  `Matrix(RR,v)` ) but I don't see why sage can't do the "right" thing automatically.

Issue created by migration from https://trac.sagemath.org/ticket/2658





---

archive/issue_comments_018254.json:
```json
{
    "body": "The code tries to call v._matrix_(ZZ) and if this fails, it calls v._matrix_() (which gives the answer you want).\n\nIs there a good reason for the code to call v._matrix_(ZZ) before trying v._matrix_()?",
    "created_at": "2008-03-24T20:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18254",
    "user": "https://github.com/jasongrout"
}
```

The code tries to call v._matrix_(ZZ) and if this fails, it calls v._matrix_() (which gives the answer you want).

Is there a good reason for the code to call v._matrix_(ZZ) before trying v._matrix_()?



---

archive/issue_comments_018255.json:
```json
{
    "body": "This is resolved in the matrix() rewrite in #2651.",
    "created_at": "2008-03-25T21:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18255",
    "user": "https://github.com/jasongrout"
}
```

This is resolved in the matrix() rewrite in #2651.



---

archive/issue_events_002849.json:
```json
{
    "actor": "@jasongrout",
    "created_at": "2008-03-25T21:23:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2658#event-2849"
}
```



---

archive/issue_comments_018256.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-25T21:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18256",
    "user": "https://github.com/jasongrout"
}
```

Resolution: duplicate



---

archive/issue_comments_018257.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-25T23:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_018258.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-25T23:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002850.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-25T23:39:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2658#event-2850"
}
```



---

archive/issue_comments_018259.json:
```json
{
    "body": "This is not a duplicate and not fixed yet. Tickets like this get only closed when the original ticket is close. Reopened.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-25T23:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not a duplicate and not fixed yet. Tickets like this get only closed when the original ticket is close. Reopened.

Cheers,

Michael



---

archive/issue_comments_018260.json:
```json
{
    "body": "I'm glad mabshoff didn't close this. The matrix rewrite (#2651) missed some stuff:\n\n```\nsage: v = vector(IntegerModRing(2),range(5));v.parent()\nVector space of dimension 5 over Ring of integers modulo 2\nsage: M=matrix(v) ;  M.parent()\nFull MatrixSpace of 1 by 5 dense matrices over Integer Ring\n```\n \n\nand :\n\n\n```\nsage: v = vector(QQ,range(5));v.parent()\nVector space of dimension 5 over Rational Field\nsage: M=matrix(v) ;  M.parent()\nFull MatrixSpace of 1 by 5 dense matrices over Integer Ring\n```\n",
    "created_at": "2008-04-14T16:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18260",
    "user": "https://github.com/dfdeshom"
}
```

I'm glad mabshoff didn't close this. The matrix rewrite (#2651) missed some stuff:

```
sage: v = vector(IntegerModRing(2),range(5));v.parent()
Vector space of dimension 5 over Ring of integers modulo 2
sage: M=matrix(v) ;  M.parent()
Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
```
 

and :


```
sage: v = vector(QQ,range(5));v.parent()
Vector space of dimension 5 over Rational Field
sage: M=matrix(v) ;  M.parent()
Full MatrixSpace of 1 by 5 dense matrices over Integer Ring
```




---

archive/issue_comments_018261.json:
```json
{
    "body": "Are you *sure* that the rewrite missed those things?  The rewrite was applied in 3.0alpha0.  You shouldn't get those results after applying #2651.\n\nIn fact, a doctest for the new matrix() rewrite is the following:\n\n\n```\nsage: matrix(vector(RR,[1,2,3])).parent() \nFull MatrixSpace of 1 by 3 dense matrices over Real Field with 53 bits of precision \n```\n\n\nThe fact that this doctest is not failing indicates that this issue is resolved.",
    "created_at": "2008-04-14T18:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18261",
    "user": "https://github.com/jasongrout"
}
```

Are you *sure* that the rewrite missed those things?  The rewrite was applied in 3.0alpha0.  You shouldn't get those results after applying #2651.

In fact, a doctest for the new matrix() rewrite is the following:


```
sage: matrix(vector(RR,[1,2,3])).parent() 
Full MatrixSpace of 1 by 3 dense matrices over Real Field with 53 bits of precision 
```


The fact that this doctest is not failing indicates that this issue is resolved.



---

archive/issue_comments_018262.json:
```json
{
    "body": "Mea culpa :) . I do have 3.0alpha3 installed here, but I must have confused it with my 2.11 copy. Both of these examples above work for me. I think it's safe to close this one.",
    "created_at": "2008-04-14T18:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18262",
    "user": "https://github.com/dfdeshom"
}
```

Mea culpa :) . I do have 3.0alpha3 installed here, but I must have confused it with my 2.11 copy. Both of these examples above work for me. I think it's safe to close this one.



---

archive/issue_comments_018263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T19:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18263",
    "user": "https://github.com/jasongrout"
}
```

Resolution: fixed



---

archive/issue_comments_018264.json:
```json
{
    "body": "Closing this since it has been fixed and doctested by #2651.",
    "created_at": "2008-04-14T19:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2658#issuecomment-18264",
    "user": "https://github.com/jasongrout"
}
```

Closing this since it has been fixed and doctested by #2651.



---

archive/issue_events_002851.json:
```json
{
    "actor": "@jasongrout",
    "created_at": "2008-04-14T19:07:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2658#event-2851"
}
```
