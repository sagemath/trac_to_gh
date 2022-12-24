# Issue 1763: implement norms for matrices

archive/issues_001763.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  harald.schilly@gmail.com\n\nAdd functionality to implement various types of norms on matrices; for starters, see\nhttp://en.wikipedia.org/wiki/Matrix_norm\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1763\n\n",
    "created_at": "2008-01-12T09:30:43Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "implement norms for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1763",
    "user": "@aghitza"
}
```
Assignee: @williamstein

CC:  harald.schilly@gmail.com

Add functionality to implement various types of norms on matrices; for starters, see
http://en.wikipedia.org/wiki/Matrix_norm



Issue created by migration from https://trac.sagemath.org/ticket/1763





---

archive/issue_comments_011133.json:
```json
{
    "body": "Attachment [trac_1763via2512.patch](tarball://root/attachments/some-uuid/ticket1763/trac_1763via2512.patch) by @dfdeshom created at 2008-03-28 22:12:12\n\nThis patch adds the most common norm used for matrices: 1,2,\\inf and Frobenius (and \"entry-wise norm\"). 2 points:\n* I don't believe there's a general formula for the p-norm, although I hear estimations can be computed. I could be wrong though.\n* I stuck this in matrix2.pyx and arbitrarily chose to use convert anything to RDF matrices since RDF matrices actually have a SVD method (which is needed for the 2-norm). I'd like to hear people comments on that.",
    "created_at": "2008-03-28T22:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11133",
    "user": "@dfdeshom"
}
```

Attachment [trac_1763via2512.patch](tarball://root/attachments/some-uuid/ticket1763/trac_1763via2512.patch) by @dfdeshom created at 2008-03-28 22:12:12

This patch adds the most common norm used for matrices: 1,2,\inf and Frobenius (and "entry-wise norm"). 2 points:
* I don't believe there's a general formula for the p-norm, although I hear estimations can be computed. I could be wrong though.
* I stuck this in matrix2.pyx and arbitrarily chose to use convert anything to RDF matrices since RDF matrices actually have a SVD method (which is needed for the 2-norm). I'd like to hear people comments on that.



---

archive/issue_comments_011134.json:
```json
{
    "body": "Attachment [1763-2.patch](tarball://root/attachments/some-uuid/ticket1763/1763-2.patch) by @aghitza created at 2008-04-01 04:45:02\n\napply after the above patch",
    "created_at": "2008-04-01T04:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11134",
    "user": "@aghitza"
}
```

Attachment [1763-2.patch](tarball://root/attachments/some-uuid/ticket1763/1763-2.patch) by @aghitza created at 2008-04-01 04:45:02

apply after the above patch



---

archive/issue_comments_011135.json:
```json
{
    "body": "Hi Didier,\n\nI have a few concerns about the patch:\n\n1. as it is, it only returns an RDF if p=2, and some other type depending on the coefficient of the matrix otherwise; it would be preferable to have a uniform behavior\n\n2. for vectors, the syntax for the inf-norm is norm(Infinity), whereas here it is norm('inf'); it would be better to be consistent about this\n\n3. there are a bunch of trivial typos in the docstring and comments\n\n4. being a number theorist, to me 'frob' is much more suggestive of Frobenius than 'fro'.\n\nSince all of this is fairly straightforward, I went ahead and put up an add-on patch.",
    "created_at": "2008-04-01T04:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11135",
    "user": "@aghitza"
}
```

Hi Didier,

I have a few concerns about the patch:

1. as it is, it only returns an RDF if p=2, and some other type depending on the coefficient of the matrix otherwise; it would be preferable to have a uniform behavior

2. for vectors, the syntax for the inf-norm is norm(Infinity), whereas here it is norm('inf'); it would be better to be consistent about this

3. there are a bunch of trivial typos in the docstring and comments

4. being a number theorist, to me 'frob' is much more suggestive of Frobenius than 'fro'.

Since all of this is fairly straightforward, I went ahead and put up an add-on patch.



---

archive/issue_comments_011136.json:
```json
{
    "body": "This doesn't handle matrices with negative or complex entries correctly, it should be taking absolute values in several places. \n\n+1 to AlexGhitza's changes though.",
    "created_at": "2008-04-06T06:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11136",
    "user": "@robertwb"
}
```

This doesn't handle matrices with negative or complex entries correctly, it should be taking absolute values in several places. 

+1 to AlexGhitza's changes though.



---

archive/issue_comments_011137.json:
```json
{
    "body": "apply instead of the other patches",
    "created_at": "2008-04-09T13:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11137",
    "user": "@aghitza"
}
```

apply instead of the other patches



---

archive/issue_comments_011138.json:
```json
{
    "body": "Attachment [1763-replacement.patch](tarball://root/attachments/some-uuid/ticket1763/1763-replacement.patch) by @aghitza created at 2008-04-09 13:51:35\n\nI modified the previous patches so that norm() works correctly on matrices with negative and/or complex entries.  I also added a conjugate() function for conjugating a complex matrix.\n\n1763-replacement.patch should be applied instead of the previous patches.",
    "created_at": "2008-04-09T13:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11138",
    "user": "@aghitza"
}
```

Attachment [1763-replacement.patch](tarball://root/attachments/some-uuid/ticket1763/1763-replacement.patch) by @aghitza created at 2008-04-09 13:51:35

I modified the previous patches so that norm() works correctly on matrices with negative and/or complex entries.  I also added a conjugate() function for conjugating a complex matrix.

1763-replacement.patch should be applied instead of the previous patches.



---

archive/issue_comments_011139.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-14T22:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11139",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_011140.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T00:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11140",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011141.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T00:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1763#issuecomment-11141",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
