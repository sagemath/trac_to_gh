# Issue 5273: [with patch, needs review] change error message for integer matrices which are too large

archive/issues_005273.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nCC:  cwitty\n\nKeywords: 32-bit, 64-bit, matrix\n\nOn a 32-bit machine:\n\n```\nsage: matrix(ZZ, 100, 2^85)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...\nValueError: number of rows and columns must be less than 2^32 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)\n```\n\nThe attached patch makes this change: if the number of rows or columns is `2^64` or more, it just says the size is too big, it doesn't say anything about a 64-bit computer.  If the number of rows is between `2^32` and `2^64-1` and if the computer is 32-bit, then it gives the above error message.  (The message is also reworded a little bit.)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5273\n\n",
    "created_at": "2009-02-14T16:55:41Z",
    "labels": [
        "linear algebra",
        "trivial",
        "bug"
    ],
    "title": "[with patch, needs review] change error message for integer matrices which are too large",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5273",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

CC:  cwitty

Keywords: 32-bit, 64-bit, matrix

On a 32-bit machine:

```
sage: matrix(ZZ, 100, 2^85)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: number of rows and columns must be less than 2^32 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)
```

The attached patch makes this change: if the number of rows or columns is `2^64` or more, it just says the size is too big, it doesn't say anything about a 64-bit computer.  If the number of rows is between `2^32` and `2^64-1` and if the computer is 32-bit, then it gives the above error message.  (The message is also reworded a little bit.)



Issue created by migration from https://trac.sagemath.org/ticket/5273





---

archive/issue_comments_040476.json:
```json
{
    "body": "Attachment [5273.patch](tarball://root/attachments/some-uuid/ticket5273/5273.patch) by mhansen created at 2009-02-15 02:24:38\n\nLooks good to me.",
    "created_at": "2009-02-15T02:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40476",
    "user": "mhansen"
}
```

Attachment [5273.patch](tarball://root/attachments/some-uuid/ticket5273/5273.patch) by mhansen created at 2009-02-15 02:24:38

Looks good to me.



---

archive/issue_comments_040477.json:
```json
{
    "body": "This ticket fails to import for me:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5273.patch \npatching file sage/matrix/matrix_space.py\nHunk #1 FAILED at 197.\nHunk #2 FAILED at 215.\n2 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix_space.py.rej\n```\n\nNote that Carl Witty already fixed a bug here recently since signed ints were used:\n\n```\n        parent_gens.ParentWithGens.__init__(self, base_ring)\n        if not isinstance(base_ring, ring.Ring):\n            raise TypeError, \"base_ring must be a ring\"\n        if ncols == None: ncols = nrows\n        nrows = int(nrows)\n        ncols = int(ncols)\n        if nrows < 0:\n            raise ArithmeticError, \"nrows must be nonnegative\"\n        if ncols < 0:\n            raise ArithmeticError, \"ncols must be nonnegative\"\n\n        if sage.misc.misc.is_64_bit:\n            if nrows >= 2**63 or ncols >= 2**63:\n                raise ValueError, \"number of rows and columns must be less than 2^63\"\n        else:\n            if nrows >= 2**31 or ncols >= 2**31:\n                raise ValueError, \"number of rows and columns must be less than 2^31 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)\"\n```\n\nThis patch went into 3.3.alpha6 via #5193, so it looks like the problem has already been fixed.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T06:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40477",
    "user": "mabshoff"
}
```

This ticket fails to import for me:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5273.patch 
patching file sage/matrix/matrix_space.py
Hunk #1 FAILED at 197.
Hunk #2 FAILED at 215.
2 out of 2 hunks FAILED -- saving rejects to file sage/matrix/matrix_space.py.rej
```

Note that Carl Witty already fixed a bug here recently since signed ints were used:

```
        parent_gens.ParentWithGens.__init__(self, base_ring)
        if not isinstance(base_ring, ring.Ring):
            raise TypeError, "base_ring must be a ring"
        if ncols == None: ncols = nrows
        nrows = int(nrows)
        ncols = int(ncols)
        if nrows < 0:
            raise ArithmeticError, "nrows must be nonnegative"
        if ncols < 0:
            raise ArithmeticError, "ncols must be nonnegative"

        if sage.misc.misc.is_64_bit:
            if nrows >= 2**63 or ncols >= 2**63:
                raise ValueError, "number of rows and columns must be less than 2^63"
        else:
            if nrows >= 2**31 or ncols >= 2**31:
                raise ValueError, "number of rows and columns must be less than 2^31 (on a 32-bit computer -- use a 64-bit computer for bigger matrices)"
```

This patch went into 3.3.alpha6 via #5193, so it looks like the problem has already been fixed.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_040478.json:
```json
{
    "body": "\n```\n\n[10:28pm] mabs: mhansen: I need to look at John's patch to make 100% sure they \nare both fixing all the same issues (besides John's patch doesn't address the \nsigned int problem)\n[10:31pm] cwitty: I think the point of #5273 is that the error message on a \nmatrix of size 2^80 on a 32-bit computer suggests that it might actually work \non a 64-bit computer.\n[10:31pm] mabs: Yes. That is why I thought something else remains to be done \n[10:32pm] cwitty: But if you're going to worry about that... I'm pretty sure \nthere's no computer in the world that can handle a matrix with even 2^50 \nentries...\n[10:32pm] mabs: cwitty: Can you integrate that change on top of your change.\n[10:33pm] mabs: Well, you can create the MatrixSpace \n[10:33pm] cwitty: True.\n[10:33pm] mabs: Not that it will not blow up if you do anything serious with \nit, but if things are very sparse it should not appear to work\n```\n",
    "created_at": "2009-02-15T06:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40478",
    "user": "mabshoff"
}
```


```

[10:28pm] mabs: mhansen: I need to look at John's patch to make 100% sure they 
are both fixing all the same issues (besides John's patch doesn't address the 
signed int problem)
[10:31pm] cwitty: I think the point of #5273 is that the error message on a 
matrix of size 2^80 on a 32-bit computer suggests that it might actually work 
on a 64-bit computer.
[10:31pm] mabs: Yes. That is why I thought something else remains to be done 
[10:32pm] cwitty: But if you're going to worry about that... I'm pretty sure 
there's no computer in the world that can handle a matrix with even 2^50 
entries...
[10:32pm] mabs: cwitty: Can you integrate that change on top of your change.
[10:33pm] mabs: Well, you can create the MatrixSpace 
[10:33pm] cwitty: True.
[10:33pm] mabs: Not that it will not blow up if you do anything serious with 
it, but if things are very sparse it should not appear to work
```




---

archive/issue_comments_040479.json:
```json
{
    "body": "Here's a version based off 3.3.rc0.",
    "created_at": "2009-02-15T16:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40479",
    "user": "jhpalmieri"
}
```

Here's a version based off 3.3.rc0.



---

archive/issue_comments_040480.json:
```json
{
    "body": "Attachment [5273-rebased.patch](tarball://root/attachments/some-uuid/ticket5273/5273-rebased.patch) by mabshoff created at 2009-02-16 04:06:35\n\nTo make things 100% sure: the rebased patch applies and doctests fine, so an extra positive review for that patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40480",
    "user": "mabshoff"
}
```

Attachment [5273-rebased.patch](tarball://root/attachments/some-uuid/ticket5273/5273-rebased.patch) by mabshoff created at 2009-02-16 04:06:35

To make things 100% sure: the rebased patch applies and doctests fine, so an extra positive review for that patch.

Cheers,

Michael



---

archive/issue_comments_040481.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T04:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40481",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040482.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5273#issuecomment-40482",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
