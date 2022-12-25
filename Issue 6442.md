# Issue 6442: Random(?) index error with determinant method

archive/issues_006442.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @orlitzky\n\nKeywords: det, determinant, IndexError\n\nOn some occasions, the call A.det() for a matrix A results in an error, namely:\n\n    IndexError: list index out of range\n\nThe error occurs during the dictionary lookup.  It seems that rather than finding no item (and hence creating a new one and then computing determinant), an empty item D is found and indexing into D results in the error.\n\nIf run into this strange problem twice during the SAGE Days 16.  I've attached an example file to this email, which contains a saved matrix.  The code\n\n    sage: A = load(\"DetBugMatrix.sobj\")\n    sage: A.det()\n\nshould trigger the problem.  If I recall correctly, I obtained the matrix from the following code\n\n    sage: R = Zp(p=5,prec=3,type=\"capped-abs\",print_mode=\"series\")\n    sage: A = random_matrix(R, 10, 10)\n\nStrangely enough (although perhaps not that strange after checking that the error happens during the lookup), the call A.copy().det() returns the determinant without any problems.\n\nI have no clue as to how one could systematically reproduce the bug.\n\nIn case it may help, I downloaded SAGE 4.0.2 and built it locally.  The machine used is a Lenovo T500 laptop with two intel centrino, running Ubuntu.  If there's any further information that would help, please let me know.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6442\n\n",
    "created_at": "2009-06-28T18:23:15Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Random(?) index error with determinant method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6442",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```
Assignee: somebody

CC:  @orlitzky

Keywords: det, determinant, IndexError

On some occasions, the call A.det() for a matrix A results in an error, namely:

    IndexError: list index out of range

The error occurs during the dictionary lookup.  It seems that rather than finding no item (and hence creating a new one and then computing determinant), an empty item D is found and indexing into D results in the error.

If run into this strange problem twice during the SAGE Days 16.  I've attached an example file to this email, which contains a saved matrix.  The code

    sage: A = load("DetBugMatrix.sobj")
    sage: A.det()

should trigger the problem.  If I recall correctly, I obtained the matrix from the following code

    sage: R = Zp(p=5,prec=3,type="capped-abs",print_mode="series")
    sage: A = random_matrix(R, 10, 10)

Strangely enough (although perhaps not that strange after checking that the error happens during the lookup), the call A.copy().det() returns the determinant without any problems.

I have no clue as to how one could systematically reproduce the bug.

In case it may help, I downloaded SAGE 4.0.2 and built it locally.  The machine used is a Lenovo T500 laptop with two intel centrino, running Ubuntu.  If there's any further information that would help, please let me know.

Issue created by migration from https://trac.sagemath.org/ticket/6442





---

archive/issue_comments_051656.json:
```json
{
    "body": "Matrix to trigger the IndexError",
    "created_at": "2009-06-28T18:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51656",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Matrix to trigger the IndexError



---

archive/issue_comments_051657.json:
```json
{
    "body": "Attachment [DetBugMatrix.sobj](tarball://root/attachments/some-uuid/ticket6442/DetBugMatrix.sobj) by @loefflerd created at 2009-07-05 08:09:47",
    "created_at": "2009-07-05T08:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51657",
    "user": "https://github.com/loefflerd"
}
```

Attachment [DetBugMatrix.sobj](tarball://root/attachments/some-uuid/ticket6442/DetBugMatrix.sobj) by @loefflerd created at 2009-07-05 08:09:47



---

archive/issue_comments_051658.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-07-05T08:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51658",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_051659.json:
```json
{
    "body": "We've got two charpoly() algorithms at the moment, but back when this bug was reported, I think the hessenberg algorithm was the default. If we try charpoly() on this matrix,\n\n```\nsage: A = load('/home/mjo/DetBugMatrix.sobj')\nsage: A.charpoly(algorithm='hessenberg')\n...\nValueError: element valuation cannot be negative.\n```\n\nIf we look at the code for charpoly(), we see that the empty hash {} is cached before the attempt to compute charpoly(). In matrix2.pyx,\n\n```\nD = self.fetch('charpoly')\n\nif not D is None:\n    if D.has_key(var):\n        return D[var]\nelse:\n    D = {}\n    self.cache('charpoly',D)\n\n<compute the charpoly>\n\n# Cache the result\nD[var] = f\nreturn f  \n```\n\nSo if computation of charpoly() fails, we'll have {} cached, and det() will blow up. A full example:\n\n```\nsage: A = load('/home/mjo/DetBugMatrix.sobj')\nsage: A.charpoly(algorithm='hessenberg')\n...\nValueError: element valuation cannot be negative.\nsage: A.det()\n...\nIndexError: list index out of range\nsage: A.charpoly()\n(1 + O(5^3))*x^10 + (2 + 4*5 + 2*5^2 + O(5^3))*x^9 + (4 + 4*5 + 4*5^2 + O(5^3))*x^8 + (4 + 5^2 + O(5^3))*x^7 + (4*5^2 + O(5^3))*x^6 + (3 + 5 + 5^2 + O(5^3))*x^5 + (1 + 3*5 + 5^2 + O(5^3))*x^4 + (1 + 4*5 + 4*5^2 + O(5^3))*x^3 + (1 + 4*5 + 4*5^2 + O(5^3))*x^2 + (2 + 4*5 + 4*5^2 + O(5^3))*x + (2*5 + 4*5^2 + O(5^3))\nsage: A.det()\n2*5 + 4*5^2 + O(5^3)\n```\n\nSo the solution, I think, is to avoid caching the empty hash until we know we've got a charpoly.",
    "created_at": "2012-01-04T00:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51659",
    "user": "https://github.com/orlitzky"
}
```

We've got two charpoly() algorithms at the moment, but back when this bug was reported, I think the hessenberg algorithm was the default. If we try charpoly() on this matrix,

```
sage: A = load('/home/mjo/DetBugMatrix.sobj')
sage: A.charpoly(algorithm='hessenberg')
...
ValueError: element valuation cannot be negative.
```

If we look at the code for charpoly(), we see that the empty hash {} is cached before the attempt to compute charpoly(). In matrix2.pyx,

```
D = self.fetch('charpoly')

if not D is None:
    if D.has_key(var):
        return D[var]
else:
    D = {}
    self.cache('charpoly',D)

<compute the charpoly>

# Cache the result
D[var] = f
return f  
```

So if computation of charpoly() fails, we'll have {} cached, and det() will blow up. A full example:

```
sage: A = load('/home/mjo/DetBugMatrix.sobj')
sage: A.charpoly(algorithm='hessenberg')
...
ValueError: element valuation cannot be negative.
sage: A.det()
...
IndexError: list index out of range
sage: A.charpoly()
(1 + O(5^3))*x^10 + (2 + 4*5 + 2*5^2 + O(5^3))*x^9 + (4 + 4*5 + 4*5^2 + O(5^3))*x^8 + (4 + 5^2 + O(5^3))*x^7 + (4*5^2 + O(5^3))*x^6 + (3 + 5 + 5^2 + O(5^3))*x^5 + (1 + 3*5 + 5^2 + O(5^3))*x^4 + (1 + 4*5 + 4*5^2 + O(5^3))*x^3 + (1 + 4*5 + 4*5^2 + O(5^3))*x^2 + (2 + 4*5 + 4*5^2 + O(5^3))*x + (2*5 + 4*5^2 + O(5^3))
sage: A.det()
2*5 + 4*5^2 + O(5^3)
```

So the solution, I think, is to avoid caching the empty hash until we know we've got a charpoly.



---

archive/issue_comments_051660.json:
```json
{
    "body": "Here's a patch that should prevent this problem in the future. I used the smallest matrix I could find for the doctest, but I was just creating them randomly. I'd be happy to replace it with a smaller example.",
    "created_at": "2012-01-05T02:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51660",
    "user": "https://github.com/orlitzky"
}
```

Here's a patch that should prevent this problem in the future. I used the smallest matrix I could find for the doctest, but I was just creating them randomly. I'd be happy to replace it with a smaller example.



---

archive/issue_comments_051661.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-05T02:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51661",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051662.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-10T10:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51662",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_051663.json:
```json
{
    "body": "I tried the attached patch on top of 4.7.2 but the problem with the initial matrix still exists:\n\n```\n[zimmerma@coing tmp]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 6442\nsage: A = load (\"DetBugMatrix.sobj\")\nsage: A.det()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n| Sage Version 4.7.2, Release Date: 2011-10-29                       |\n| Type notebook() for the GUI, and license() for information.        |\n/tmp/<ipython console> in <module>()\n\n/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.det (sage/matrix/matrix2.c:8222)()\n\n/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.determinant (sage/matrix/matrix2.c:6889)()\n\nIndexError: list index out of range\n```\nPaul",
    "created_at": "2012-01-10T10:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51663",
    "user": "https://github.com/zimmermann6"
}
```

I tried the attached patch on top of 4.7.2 but the problem with the initial matrix still exists:

```
[zimmerma@coing tmp]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6442
sage: A = load ("DetBugMatrix.sobj")
sage: A.det()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.7.2, Release Date: 2011-10-29                       |
| Type notebook() for the GUI, and license() for information.        |
/tmp/<ipython console> in <module>()

/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.det (sage/matrix/matrix2.c:8222)()

/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.determinant (sage/matrix/matrix2.c:6889)()

IndexError: list index out of range
```
Paul



---

archive/issue_comments_051664.json:
```json
{
    "body": "Changing keywords from \"det, determinant, IndexError\" to \"det, determinant, IndexError, sd35.5\".",
    "created_at": "2012-01-10T10:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51664",
    "user": "https://github.com/zimmermann6"
}
```

Changing keywords from "det, determinant, IndexError" to "det, determinant, IndexError, sd35.5".



---

archive/issue_comments_051665.json:
```json
{
    "body": "The bug wasn't in the saving/loading of matrices, only in the cache code. DetBugMatrix.sobj contains a broken matrix -- one with an empty dictionary cached as the charpoly(). When you load it from file, it's still broken, so some operations won't work on it.\n\nThe patch prevents creating these matrices in the future by fixing the cache bug (hopefully).\n\nThe code from the doctest should work only after the patch, because prior to the patch, it would have created a matrix with the same problem as the one in DetBugMatrix.sobj.",
    "created_at": "2012-01-10T13:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51665",
    "user": "https://github.com/orlitzky"
}
```

The bug wasn't in the saving/loading of matrices, only in the cache code. DetBugMatrix.sobj contains a broken matrix -- one with an empty dictionary cached as the charpoly(). When you load it from file, it's still broken, so some operations won't work on it.

The patch prevents creating these matrices in the future by fixing the cache bug (hopefully).

The code from the doctest should work only after the patch, because prior to the patch, it would have created a matrix with the same problem as the one in DetBugMatrix.sobj.



---

archive/issue_comments_051666.json:
```json
{
    "body": "the doctest example can be simplified to:\n\n```\nA = matrix(z, [ [3 + O(5^1), 4 + O(5^1), 4 + O(5^1)],\n[2*5^2 + O(5^3), 2 + O(5^1), 1 + O(5^1)],\n[5 + O(5^2), 1 + O(5^1), 1 + O(5^1)]])\n```\nPaul",
    "created_at": "2012-01-10T14:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51666",
    "user": "https://github.com/zimmermann6"
}
```

the doctest example can be simplified to:

```
A = matrix(z, [ [3 + O(5^1), 4 + O(5^1), 4 + O(5^1)],
[2*5^2 + O(5^3), 2 + O(5^1), 1 + O(5^1)],
[5 + O(5^2), 1 + O(5^1), 1 + O(5^1)]])
```
Paul



---

archive/issue_comments_051667.json:
```json
{
    "body": "> The bug wasn't in the saving/loading of matrices, only in the cache code [...]\n\n\nok, I put it back to \"needs review\". However the summary is misleading.\n\nPaul",
    "created_at": "2012-01-10T14:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51667",
    "user": "https://github.com/zimmermann6"
}
```

> The bug wasn't in the saving/loading of matrices, only in the cache code [...]


ok, I put it back to "needs review". However the summary is misleading.

Paul



---

archive/issue_comments_051668.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-10T14:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51668",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_051669.json:
```json
{
    "body": "two minor points:\n\n(1) the comment `Cache the result` on line 1465 should be in fact on line 1470. The code at\nline 1465 only initializes an empty cache.\n\n(2) it seems to me that if charpoly is called with the same matrix but different variables, the computation is done twice, whereas it would suffice to substitute the first variable by the second one, no? Maybe this can be in a separate ticket.\n\nPaul",
    "created_at": "2012-01-10T14:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51669",
    "user": "https://github.com/zimmermann6"
}
```

two minor points:

(1) the comment `Cache the result` on line 1465 should be in fact on line 1470. The code at
line 1465 only initializes an empty cache.

(2) it seems to me that if charpoly is called with the same matrix but different variables, the computation is done twice, whereas it would suffice to substitute the first variable by the second one, no? Maybe this can be in a separate ticket.

Paul



---

archive/issue_comments_051670.json:
```json
{
    "body": "Thanks for the simplified test case, I'll be able to update the patch in a bit.\n\nI think you're correct about (2), but I would do that in a separate ticket since it's unrelated to this problem.",
    "created_at": "2012-01-10T14:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51670",
    "user": "https://github.com/orlitzky"
}
```

Thanks for the simplified test case, I'll be able to update the patch in a bit.

I think you're correct about (2), but I would do that in a separate ticket since it's unrelated to this problem.



---

archive/issue_comments_051671.json:
```json
{
    "body": "Updated patch with simpler test case and a better comment.",
    "created_at": "2012-01-10T15:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51671",
    "user": "https://github.com/orlitzky"
}
```

Updated patch with simpler test case and a better comment.



---

archive/issue_comments_051672.json:
```json
{
    "body": "Attachment [sage-trac_6442.patch](tarball://root/attachments/some-uuid/ticket6442/sage-trac_6442.patch) by @orlitzky created at 2012-01-10 15:28:01\n\nI just updated the patch with your test case.\n\nI moved the \"Cache the result\" comment to where it belongs, but also added a comment above the code that creates the dictionary, explaining why it occurs near the end of the function.",
    "created_at": "2012-01-10T15:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51672",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_6442.patch](tarball://root/attachments/some-uuid/ticket6442/sage-trac_6442.patch) by @orlitzky created at 2012-01-10 15:28:01

I just updated the patch with your test case.

I moved the "Cache the result" comment to where it belongs, but also added a comment above the code that creates the dictionary, explaining why it occurs near the end of the function.



---

archive/issue_comments_051673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-11T07:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51673",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051674.json:
```json
{
    "body": "thank you Michael for your changes. All doctests pass. I give a positive review.\n\nPaul",
    "created_at": "2012-01-11T07:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51674",
    "user": "https://github.com/zimmermann6"
}
```

thank you Michael for your changes. All doctests pass. I give a positive review.

Paul



---

archive/issue_comments_051675.json:
```json
{
    "body": "the efficiency issue with the cache is now ticket #12292.\n\nPaul",
    "created_at": "2012-01-11T07:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51675",
    "user": "https://github.com/zimmermann6"
}
```

the efficiency issue with the cache is now ticket #12292.

Paul



---

archive/issue_events_015193.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-15T10:41:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6442#event-15193"
}
```



---

archive/issue_events_015194.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-29T11:17:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6442#event-15194"
}
```



---

archive/issue_comments_051676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-29T11:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6442",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6442#issuecomment-51676",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
