# Issue 4648: sparse linear algebra: nonzero_positions is slow

archive/issues_004648.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: sparse\n\nCurrently, generic sparse matrices inherit their nonzero_positions method from matrix0.py.  This should be trivial to fix.\n\n\n```\ndef nonzero_positions(self):\n    return self._entries.keys()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4648\n\n",
    "created_at": "2008-11-29T00:54:49Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "sparse linear algebra: nonzero_positions is slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4648",
    "user": "boothby"
}
```
Assignee: boothby

Keywords: sparse

Currently, generic sparse matrices inherit their nonzero_positions method from matrix0.py.  This should be trivial to fix.


```
def nonzero_positions(self):
    return self._entries.keys()
```


Issue created by migration from https://trac.sagemath.org/ticket/4648





---

archive/issue_comments_034991.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T13:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4648#issuecomment-34991",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_034992.json:
```json
{
    "body": "Not quite so trivial as two lines, but...",
    "created_at": "2009-01-23T13:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4648#issuecomment-34992",
    "user": "rlm"
}
```

Not quite so trivial as two lines, but...



---

archive/issue_comments_034993.json:
```json
{
    "body": "Code looks good. Merge!\n\nHowever, I think that the fact that all three versions of this code are nearly identical means that a new enhancement ticket should be opened to clean up the classes here. In particular, I think the following might be a reasonable plan:\n\n* in `matrix_integer_sparse`, rename `_matrix` to `_rows` for consistency (and clarity -- you're getting a list of rows, not a pointer to the whole matrix)\n* clean up the associated vector classes (in fact, `vector_modn_sparse` isn't even a class right now!), and have them all inherit from an abstract class with the same methods they all share (which could all raise `NotImplementedError`s, for all that matters)\n* make each of the sparse matrix classes have a member `_rows` of type `vector_sparse_generic` or whatever, and then move the `_nonzero_positions_by_row` down to the generic class.\n\nIt would get rid of this code duplication, clean things up, etc.",
    "created_at": "2009-01-24T12:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4648#issuecomment-34993",
    "user": "craigcitro"
}
```

Code looks good. Merge!

However, I think that the fact that all three versions of this code are nearly identical means that a new enhancement ticket should be opened to clean up the classes here. In particular, I think the following might be a reasonable plan:

* in `matrix_integer_sparse`, rename `_matrix` to `_rows` for consistency (and clarity -- you're getting a list of rows, not a pointer to the whole matrix)
* clean up the associated vector classes (in fact, `vector_modn_sparse` isn't even a class right now!), and have them all inherit from an abstract class with the same methods they all share (which could all raise `NotImplementedError`s, for all that matters)
* make each of the sparse matrix classes have a member `_rows` of type `vector_sparse_generic` or whatever, and then move the `_nonzero_positions_by_row` down to the generic class.

It would get rid of this code duplication, clean things up, etc.



---

archive/issue_comments_034994.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4648#issuecomment-34994",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael



---

archive/issue_comments_034995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4648#issuecomment-34995",
    "user": "mabshoff"
}
```

Resolution: fixed
