# Issue 769: Matrix_mod2_dense._echelon_strassen gives fals results sometimes

archive/issues_000769.json:
```json
{
    "body": "Assignee: @williamstein\n\nEven though this method is probably not be used anyway, it is worth noticing that it gives False results from time to time:\n\n```\nsage: for i in range(10): \n....:   A = random_matrix(GF(2),20,20);\n....:   B = A.echelon_form();\n....:   A._clear_cache(); \n....:   A._echelon_strassen(cutoff=10); \n....:   A == B\nFalse\nTrue\nTrue\nFalse\nTrue\nFalse\nTrue\nTrue\nTrue\nFalse\n```\n\n\n\n```\nsage: for i in range(10): \n....:   A = random_matrix(GF(7),20,20);\n....:   B = A.echelon_form();\n....:   A._clear_cache(); \n....:   A._echelon_strassen(cutoff=10); \n....:   A == B\nTrue\nTrue\nTrue\nFalse\nTrue\nTrue\nTrue\nTrue\nTrue\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/769\n\n",
    "created_at": "2007-10-01T04:21:25Z",
    "labels": [
        "component: algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "Matrix_mod2_dense._echelon_strassen gives fals results sometimes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/769",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Even though this method is probably not be used anyway, it is worth noticing that it gives False results from time to time:

```
sage: for i in range(10): 
....:   A = random_matrix(GF(2),20,20);
....:   B = A.echelon_form();
....:   A._clear_cache(); 
....:   A._echelon_strassen(cutoff=10); 
....:   A == B
False
True
True
False
True
False
True
True
True
False
```



```
sage: for i in range(10): 
....:   A = random_matrix(GF(7),20,20);
....:   B = A.echelon_form();
....:   A._clear_cache(); 
....:   A._echelon_strassen(cutoff=10); 
....:   A == B
True
True
True
False
True
True
True
True
True
True
```


Issue created by migration from https://trac.sagemath.org/ticket/769





---

archive/issue_comments_004552.json:
```json
{
    "body": "I tested 1000 STrassen echelons over QQ with no problems.  I tested 100 over GF(389), i.e., a fairly big\nprime, and even there it fails.  It must be that either:\n    (1) matrix windows are buggy mod p, or\n    (2) the echelon algorithm itself is wrong mod p.\n\nI just tested with *generic* windows, and the *algorithm* is buggy, not the implementation of windows. \n\n--- \n\nI have modified \n\nWilliam",
    "created_at": "2007-10-04T15:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4552",
    "user": "https://github.com/williamstein"
}
```

I tested 1000 STrassen echelons over QQ with no problems.  I tested 100 over GF(389), i.e., a fairly big
prime, and even there it fails.  It must be that either:
    (1) matrix windows are buggy mod p, or
    (2) the echelon algorithm itself is wrong mod p.

I just tested with *generic* windows, and the *algorithm* is buggy, not the implementation of windows. 

--- 

I have modified 

William



---

archive/issue_comments_004553.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T15:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4553",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000870.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-04T15:54:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/769#event-870"
}
```



---

archive/issue_comments_004554.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-10-04T21:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4554",
    "user": "https://github.com/robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_004555.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-04T21:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4555",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000871.json:
```json
{
    "actor": "@robertwb",
    "created_at": "2007-10-04T21:22:51Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/769#event-871"
}
```



---

archive/issue_comments_004556.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2007-10-04T21:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4556",
    "user": "https://github.com/robertwb"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_004557.json:
```json
{
    "body": "I fixed the algorithm, it was forgetting to clear some pivots in some cases on full rank (where it was jumping to the end 'cause it knew it everything but the diagonal was 0's) \n\nI have tested this on 1000's of matrices of varying sizes and primes.",
    "created_at": "2007-10-04T21:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4557",
    "user": "https://github.com/robertwb"
}
```

I fixed the algorithm, it was forgetting to clear some pivots in some cases on full rank (where it was jumping to the end 'cause it knew it everything but the diagonal was 0's) 

I have tested this on 1000's of matrices of varying sizes and primes.



---

archive/issue_events_000872.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-05T02:16:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/769#event-872"
}
```



---

archive/issue_comments_004558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-05T02:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4558",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_004559.json:
```json
{
    "body": "Attachment [strassen-fix.patch](tarball://root/attachments/some-uuid/ticket769/strassen-fix.patch) by @williamstein created at 2007-10-05 02:16:07",
    "created_at": "2007-10-05T02:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4559",
    "user": "https://github.com/williamstein"
}
```

Attachment [strassen-fix.patch](tarball://root/attachments/some-uuid/ticket769/strassen-fix.patch) by @williamstein created at 2007-10-05 02:16:07



---

archive/issue_comments_004560.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-10-05T02:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/769",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/769#issuecomment-4560",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to linear algebra.
