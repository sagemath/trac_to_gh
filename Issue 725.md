# Issue 725: memleak in initialization of diagonal Matrix_integer_dense objects

archive/issues_000725.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor the diagonal case, the `__init__` function of `Matrix_integer_dense` contains the following code:\n\n\n```\n            self._zero_out_matrix()\n            j = 0\n            for i from 0 <= i < self._nrows:\n                mpz_init_set(self._entries[j], x.value)\n                j = j + self._nrows + 1\n            self._initialized = True\n```\n\n\nas the _zero_out_matrix function calls mpz_init on self.entries, we should use mpz_set instead of mpz_init_set.\n\nAttached patch fixes this.\n\nThe valgrind output of this error is similar to that of #621, but the example on that ticket uses a different code path. So this is not related.\n\nIssue created by migration from https://trac.sagemath.org/ticket/725\n\n",
    "created_at": "2007-09-21T02:34:04Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "memleak in initialization of diagonal Matrix_integer_dense objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/725",
    "user": "https://github.com/burcin"
}
```
Assignee: @williamstein

For the diagonal case, the `__init__` function of `Matrix_integer_dense` contains the following code:


```
            self._zero_out_matrix()
            j = 0
            for i from 0 <= i < self._nrows:
                mpz_init_set(self._entries[j], x.value)
                j = j + self._nrows + 1
            self._initialized = True
```


as the _zero_out_matrix function calls mpz_init on self.entries, we should use mpz_set instead of mpz_init_set.

Attached patch fixes this.

The valgrind output of this error is similar to that of #621, but the example on that ticket uses a different code path. So this is not related.

Issue created by migration from https://trac.sagemath.org/ticket/725





---

archive/issue_comments_004214.json:
```json
{
    "body": "Attachment [matrix_integer_dense_diagonal_memleak.patch](tarball://root/attachments/some-uuid/ticket725/matrix_integer_dense_diagonal_memleak.patch) by @burcin created at 2007-09-21 02:36:24",
    "created_at": "2007-09-21T02:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/725#issuecomment-4214",
    "user": "https://github.com/burcin"
}
```

Attachment [matrix_integer_dense_diagonal_memleak.patch](tarball://root/attachments/some-uuid/ticket725/matrix_integer_dense_diagonal_memleak.patch) by @burcin created at 2007-09-21 02:36:24



---

archive/issue_comments_004215.json:
```json
{
    "body": "Changing assignee from @williamstein to @burcin.",
    "created_at": "2007-09-21T02:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/725#issuecomment-4215",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @williamstein to @burcin.



---

archive/issue_comments_004216.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-21T02:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/725#issuecomment-4216",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004217.json:
```json
{
    "body": "great work!",
    "created_at": "2007-09-21T02:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/725#issuecomment-4217",
    "user": "https://github.com/williamstein"
}
```

great work!



---

archive/issue_comments_004218.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/725#issuecomment-4218",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
