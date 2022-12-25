# Issue 4832: [with patch, needs review] prevent search_src and search_doc from printing the sage banner

archive/issues_004832.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nKeywords: search_src, banner\n\nRight now, running `search_src` from the command line with a single argument prints the sage banner as well as the search results.  If you include more than one argument, then the banner is not printed. (This isn't true if there enough results to feed into the pager.)  The same goes for `search_doc`.  The reason is that these functions all call `sage -grep` which prints the banner, but including an extra argument calls grep on the output, and the banner won't match.  The function `search_def` doesn't have this problem, because it just calls `search_src` with an extra argument \"def\".\n\nHere's an example:\n\n```\nsage: search_src('noncommutative')\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nalgebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and all fields are commutative.\nalgebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and integral domains are commutative (in SAGE).\nmatrix/matrix_space.py:commutative or noncommutative ring.\nmatrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:\nmatrix/matrix0.pyx:        EXAMPLE of scalar multiplication in the noncommutative case:\n| Sage Version 3.2.2.rc1, Release Date: 2008-12-17                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: search_src('noncommutative', 'ring')\nmatrix/matrix_space.py:commutative or noncommutative ring.\nmatrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:\n\n```\n\n\nThe attached patch prevents the banner from printing by temporarily setting the environment variable SAGE_BANNER to be \"no\". \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4832\n\n",
    "created_at": "2008-12-19T16:06:44Z",
    "labels": [
        "component: misc",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] prevent search_src and search_doc from printing the sage banner",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4832",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Keywords: search_src, banner

Right now, running `search_src` from the command line with a single argument prints the sage banner as well as the search results.  If you include more than one argument, then the banner is not printed. (This isn't true if there enough results to feed into the pager.)  The same goes for `search_doc`.  The reason is that these functions all call `sage -grep` which prints the banner, but including an extra argument calls grep on the output, and the banner won't match.  The function `search_def` doesn't have this problem, because it just calls `search_src` with an extra argument "def".

Here's an example:

```
sage: search_src('noncommutative')
----------------------------------------------------------------------
----------------------------------------------------------------------
algebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and all fields are commutative.
algebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and integral domains are commutative (in SAGE).
matrix/matrix_space.py:commutative or noncommutative ring.
matrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:
matrix/matrix0.pyx:        EXAMPLE of scalar multiplication in the noncommutative case:
| Sage Version 3.2.2.rc1, Release Date: 2008-12-17                   |
| Type notebook() for the GUI, and license() for information.        |
sage: search_src('noncommutative', 'ring')
matrix/matrix_space.py:commutative or noncommutative ring.
matrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:

```


The attached patch prevents the banner from printing by temporarily setting the environment variable SAGE_BANNER to be "no". 


Issue created by migration from https://trac.sagemath.org/ticket/4832





---

archive/issue_comments_036554.json:
```json
{
    "body": "Attachment [4832.patch](tarball://root/attachments/some-uuid/ticket4832/4832.patch) by @ncalexan created at 2009-01-21 08:15:58\n\nRead only review -- there's no way this fails :)",
    "created_at": "2009-01-21T08:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4832#issuecomment-36554",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4832.patch](tarball://root/attachments/some-uuid/ticket4832/4832.patch) by @ncalexan created at 2009-01-21 08:15:58

Read only review -- there's no way this fails :)



---

archive/issue_comments_036555.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4832#issuecomment-36555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_036556.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4832#issuecomment-36556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
