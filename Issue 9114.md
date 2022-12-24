# Issue 9114: Improve documentation of infinite polynomial rings

archive/issues_009114.json:
```json
{
    "body": "Assignee: Simon King\n\nKeywords: documentation, infinite polyonomial ring, symmetric reduction\n\nAt #9108, it was reported that the doc tests for symmetric ideals time out on some machines. As a quick solution, it was suggested to simply mark them as 'long'.\n\nHere, I replace the offensive test (it is only one) by something more easy, that is still instructive.\n\nAt this occasion, I tried to improve other aspects of the doc strings as well, e.g., I tried to shorten the lines and to adhere to the standards in describing optional arguments.\n\nThe attached patch is relative to #9108, which already has a positive review. The new patch replaces the doc test that was marked 'long' in #9108.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9114\n\n",
    "created_at": "2010-06-02T11:01:58Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Improve documentation of infinite polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9114",
    "user": "SimonKing"
}
```
Assignee: Simon King

Keywords: documentation, infinite polyonomial ring, symmetric reduction

At #9108, it was reported that the doc tests for symmetric ideals time out on some machines. As a quick solution, it was suggested to simply mark them as 'long'.

Here, I replace the offensive test (it is only one) by something more easy, that is still instructive.

At this occasion, I tried to improve other aspects of the doc strings as well, e.g., I tried to shorten the lines and to adhere to the standards in describing optional arguments.

The attached patch is relative to #9108, which already has a positive review. The new patch replaces the doc test that was marked 'long' in #9108.

Issue created by migration from https://trac.sagemath.org/ticket/9114





---

archive/issue_comments_084795.json:
```json
{
    "body": "Shorter doc test (avoiding a time out on some systems), better doc formatting.",
    "created_at": "2010-06-02T11:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84795",
    "user": "SimonKing"
}
```

Shorter doc test (avoiding a time out on some systems), better doc formatting.



---

archive/issue_comments_084796.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-02T11:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84796",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084797.json:
```json
{
    "body": "Attachment [9114_doc_infinite_polynomial.patch](tarball://root/attachments/some-uuid/ticket9114/9114_doc_infinite_polynomial.patch) by SimonKing created at 2010-06-02 11:04:27",
    "created_at": "2010-06-02T11:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84797",
    "user": "SimonKing"
}
```

Attachment [9114_doc_infinite_polynomial.patch](tarball://root/attachments/some-uuid/ticket9114/9114_doc_infinite_polynomial.patch) by SimonKing created at 2010-06-02 11:04:27



---

archive/issue_comments_084798.json:
```json
{
    "body": "Attachment [trac_9114-reviewer.patch](tarball://root/attachments/some-uuid/ticket9114/trac_9114-reviewer.patch) by davidloeffler created at 2010-06-14 12:14:38\n\napply over previous patch",
    "created_at": "2010-06-14T12:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84798",
    "user": "davidloeffler"
}
```

Attachment [trac_9114-reviewer.patch](tarball://root/attachments/some-uuid/ticket9114/trac_9114-reviewer.patch) by davidloeffler created at 2010-06-14 12:14:38

apply over previous patch



---

archive/issue_comments_084799.json:
```json
{
    "body": "Looks fine to me; it builds and passes tests under 4.4.4.alpha0, the tests pass in a reasonable length of time (25 seconds on my machine, as opposed to 17 seconds without \"-long\" and a ridiculously long time with \"-long\"). Documentation builds OK and looks good.\n\nThere is one minor problem: quite a few doctests are marked with \"# indirect doc test\" (with space), while the coverage script looks for \"# indirect doctest\". I have fixed these and added a few more doctests. (I also streamlined the `__contains__` methods slightly, since all they did was try to convert x into self and then test equality, which the coercion framework does automatically anyway.) All four files relating to infinite polynomial rings now pass `sage -coverage` with no complaints.\n\nSimon: if you are happy with the changes in my reviewer patch, then feel free to put the status to \"positive review\".",
    "created_at": "2010-06-14T12:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84799",
    "user": "davidloeffler"
}
```

Looks fine to me; it builds and passes tests under 4.4.4.alpha0, the tests pass in a reasonable length of time (25 seconds on my machine, as opposed to 17 seconds without "-long" and a ridiculously long time with "-long"). Documentation builds OK and looks good.

There is one minor problem: quite a few doctests are marked with "# indirect doc test" (with space), while the coverage script looks for "# indirect doctest". I have fixed these and added a few more doctests. (I also streamlined the `__contains__` methods slightly, since all they did was try to convert x into self and then test equality, which the coercion framework does automatically anyway.) All four files relating to infinite polynomial rings now pass `sage -coverage` with no complaints.

Simon: if you are happy with the changes in my reviewer patch, then feel free to put the status to "positive review".



---

archive/issue_comments_084800.json:
```json
{
    "body": "Replying to [comment:2 davidloeffler]:\n> ...\n> \n> Simon: if you are happy with the changes in my reviewer patch, then feel free to put the status to \"positive review\".\n\nI am happy with it! So, I changed that status to \"positive review\", and inserted your name as reviewer.\n\nBest regards,\nSimon",
    "created_at": "2010-06-14T13:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84800",
    "user": "SimonKing"
}
```

Replying to [comment:2 davidloeffler]:
> ...
> 
> Simon: if you are happy with the changes in my reviewer patch, then feel free to put the status to "positive review".

I am happy with it! So, I changed that status to "positive review", and inserted your name as reviewer.

Best regards,
Simon



---

archive/issue_comments_084801.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-14T13:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84801",
    "user": "SimonKing"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084802.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9114#issuecomment-84802",
    "user": "mpatel"
}
```

Resolution: fixed
