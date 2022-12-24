# Issue 4813: [with patch, needs review] contribution to the tests/ directory

archive/issues_004813.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :\n\n> Note that you could also submit a patch to Sage with the code you're doctesting.\n> I did that with all the tests from both of the books I published, and\n> I encourage you and many others to do the same with the code from your\n> article.  The code would go in a file\n>\n>    devel/sage/sage/tests/\n>\n> like the file devel/sage/sage/tests/book_stein_modform.py\n>\n> In fact, I could imagine having dozens of files in that directory, and\n> when doctests break there, we could notify the authors before\n> releasing the version of Sage that breaks their doctests for feedback\n> -- then they could update their papers or Sage.\n\nHere's the code from a preprint I just posted. I tried to follow \"official\" style in writing the code -- comments about the style and so on are welcome.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4813\n\n",
    "created_at": "2008-12-16T13:48:57Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] contribution to the tests/ directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4813",
    "user": "@dandrake"
}
```
Assignee: mabshoff

From http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :

> Note that you could also submit a patch to Sage with the code you're doctesting.
> I did that with all the tests from both of the books I published, and
> I encourage you and many others to do the same with the code from your
> article.  The code would go in a file
>
>    devel/sage/sage/tests/
>
> like the file devel/sage/sage/tests/book_stein_modform.py
>
> In fact, I could imagine having dozens of files in that directory, and
> when doctests break there, we could notify the authors before
> releasing the version of Sage that breaks their doctests for feedback
> -- then they could update their papers or Sage.

Here's the code from a preprint I just posted. I tried to follow "official" style in writing the code -- comments about the style and so on are welcome.

Issue created by migration from https://trac.sagemath.org/ticket/4813





---

archive/issue_comments_036487.json:
```json
{
    "body": "Attachment [arxiv_0812_2725_code.patch](tarball://root/attachments/some-uuid/ticket4813/arxiv_0812_2725_code.patch) by @dandrake created at 2008-12-16 13:49:13",
    "created_at": "2008-12-16T13:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36487",
    "user": "@dandrake"
}
```

Attachment [arxiv_0812_2725_code.patch](tarball://root/attachments/some-uuid/ticket4813/arxiv_0812_2725_code.patch) by @dandrake created at 2008-12-16 13:49:13



---

archive/issue_comments_036488.json:
```json
{
    "body": "Is this code too specialized to go into the Sage library?\n\nCheers,\n\nMichael",
    "created_at": "2008-12-16T13:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36488",
    "user": "mabshoff"
}
```

Is this code too specialized to go into the Sage library?

Cheers,

Michael



---

archive/issue_comments_036489.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> Is this code too specialized to go into the Sage library?\n\nSome of it definitely is; there's a function that computes columns of the tables in the paper. OTOH, I've been meaning to add support for complete matchings to Sage, and this code includes a function to generate complete matchings.\n\nEither way, I would like this code to get put into the tests/ directory; William above mentioned \"when doctests break there, we could notify the authors before releasing the version of Sage that breaks their doctests for feedback -- then they could update their papers or Sage.\" The paper is on the arXiv and will remain there forever (for some value of \"forever\"...) and I'd like to have this mechanism in place to make sure the code accompanying the paper always works.",
    "created_at": "2008-12-18T03:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36489",
    "user": "@dandrake"
}
```

Replying to [comment:1 mabshoff]:
> Is this code too specialized to go into the Sage library?

Some of it definitely is; there's a function that computes columns of the tables in the paper. OTOH, I've been meaning to add support for complete matchings to Sage, and this code includes a function to generate complete matchings.

Either way, I would like this code to get put into the tests/ directory; William above mentioned "when doctests break there, we could notify the authors before releasing the version of Sage that breaks their doctests for feedback -- then they could update their papers or Sage." The paper is on the arXiv and will remain there forever (for some value of "forever"...) and I'd like to have this mechanism in place to make sure the code accompanying the paper always works.



---

archive/issue_comments_036490.json:
```json
{
    "body": "Attachment [trac_4813-2.patch](tarball://root/attachments/some-uuid/ticket4813/trac_4813-2.patch) by @mwhansen created at 2009-01-24 03:00:48\n\nI think this is good to go in.  I've added a patch which does some minor formatting issues.  \n\nDan: Could you just give my little patch a positive review?",
    "created_at": "2009-01-24T03:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36490",
    "user": "@mwhansen"
}
```

Attachment [trac_4813-2.patch](tarball://root/attachments/some-uuid/ticket4813/trac_4813-2.patch) by @mwhansen created at 2009-01-24 03:00:48

I think this is good to go in.  I've added a patch which does some minor formatting issues.  

Dan: Could you just give my little patch a positive review?



---

archive/issue_comments_036491.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> Dan: Could you just give my little patch a positive review?\n\nCertainly. Thanks for recommending this go in!",
    "created_at": "2009-01-25T13:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36491",
    "user": "@dandrake"
}
```

Replying to [comment:3 mhansen]:
> Dan: Could you just give my little patch a positive review?

Certainly. Thanks for recommending this go in!



---

archive/issue_comments_036492.json:
```json
{
    "body": "Dan,\n\nplease chose a much more descriptive summary for a patch like this next time.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T16:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36492",
    "user": "mabshoff"
}
```

Dan,

please chose a much more descriptive summary for a patch like this next time.

Cheers,

Michael



---

archive/issue_comments_036493.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T16:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36493",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036494.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T16:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4813#issuecomment-36494",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael
