# Issue 8607: add deprecation option to the plot option rename decorator

archive/issues_008607.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nThis lets people change option names and automatically deprecate the old option name.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8607\n\n",
    "created_at": "2010-03-25T19:05:27Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "add deprecation option to the plot option rename decorator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8607",
    "user": "jason"
}
```
Assignee: was

CC:  mhansen

This lets people change option names and automatically deprecate the old option name.

Issue created by migration from https://trac.sagemath.org/ticket/8607





---

archive/issue_comments_077977.json:
```json
{
    "body": "Attachment [trac-8607-rename-deprecation.patch](tarball://root/attachments/some-uuid/ticket8607/trac-8607-rename-deprecation.patch) by jason created at 2010-03-25 19:12:04",
    "created_at": "2010-03-25T19:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77977",
    "user": "jason"
}
```

Attachment [trac-8607-rename-deprecation.patch](tarball://root/attachments/some-uuid/ticket8607/trac-8607-rename-deprecation.patch) by jason created at 2010-03-25 19:12:04



---

archive/issue_comments_077978.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-30T16:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77978",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077979.json:
```json
{
    "body": "All test passed in `sage/plot/misc.py`. I tested it on a keyword I changed recently and everything works as expected. I tested the sphinx docbuild and no new warning are created... but that is because the doc of the affected file is not generated. To me this is a positive review.\n\nI added a patch where I make use of the `rename_keyword` with deprecation warning and where I fixed some small sphinx syntax. If Jason aggrees with my patch, I allow him to change the status of this ticket to positive review.",
    "created_at": "2010-04-18T20:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77979",
    "user": "slabbe"
}
```

All test passed in `sage/plot/misc.py`. I tested it on a keyword I changed recently and everything works as expected. I tested the sphinx docbuild and no new warning are created... but that is because the doc of the affected file is not generated. To me this is a positive review.

I added a patch where I make use of the `rename_keyword` with deprecation warning and where I fixed some small sphinx syntax. If Jason aggrees with my patch, I allow him to change the status of this ticket to positive review.



---

archive/issue_comments_077980.json:
```json
{
    "body": "Positive review on the documentation changes.  I'm not qualified to comment on the deprecation you did in the word code, though, so I'll let someone else review that deprecation.",
    "created_at": "2010-04-20T04:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77980",
    "user": "jason"
}
```

Positive review on the documentation changes.  I'm not qualified to comment on the deprecation you did in the word code, though, so I'll let someone else review that deprecation.



---

archive/issue_comments_077981.json:
```json
{
    "body": "Attachment [trac_8607_review-sl.patch](tarball://root/attachments/some-uuid/ticket8607/trac_8607_review-sl.patch) by slabbe created at 2010-04-21 09:02:47\n\nApplies over the precedent patch",
    "created_at": "2010-04-21T09:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77981",
    "user": "slabbe"
}
```

Attachment [trac_8607_review-sl.patch](tarball://root/attachments/some-uuid/ticket8607/trac_8607_review-sl.patch) by slabbe created at 2010-04-21 09:02:47

Applies over the precedent patch



---

archive/issue_comments_077982.json:
```json
{
    "body": "I removed the deprecation in the word code from the review patch. I realize more and more that mixing independent things in the same ticket is not a good idea : the review process gets unnecessarily longer. Hence, I kept in the review patch only the documentation changes to the file `sage/plot/misc.py` which was given a positive review by Jason. Therefore, this ticket now deserves a positive review.\n\nSorry again for the first version of the review patch. I hope it will make it into sage-4.4. Thanks again for the idea about this ticket : I like it and will definitively use it ...in later patches!\n\nOne last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.\n\nS\u00e9bastien",
    "created_at": "2010-04-21T09:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77982",
    "user": "slabbe"
}
```

I removed the deprecation in the word code from the review patch. I realize more and more that mixing independent things in the same ticket is not a good idea : the review process gets unnecessarily longer. Hence, I kept in the review patch only the documentation changes to the file `sage/plot/misc.py` which was given a positive review by Jason. Therefore, this ticket now deserves a positive review.

Sorry again for the first version of the review patch. I hope it will make it into sage-4.4. Thanks again for the idea about this ticket : I like it and will definitively use it ...in later patches!

One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.

Sébastien



---

archive/issue_comments_077983.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T09:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77983",
    "user": "slabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077984.json:
```json
{
    "body": "Replying to [comment:4 slabbe]:\n\n> \n> One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.\n> \n\n+1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.",
    "created_at": "2010-04-21T15:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77984",
    "user": "jason"
}
```

Replying to [comment:4 slabbe]:

> 
> One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.
> 

+1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.



---

archive/issue_comments_077985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77985",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_077986.json:
```json
{
    "body": "Merged into 4.4.alpha2:\n- trac-8607-rename-deprecation.patch\n- trac_8607_review-sl.patch",
    "created_at": "2010-04-23T17:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77986",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha2:
- trac-8607-rename-deprecation.patch
- trac_8607_review-sl.patch



---

archive/issue_comments_077987.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> Replying to [comment:4 slabbe]:\n> \n> > \n> > One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.\n> > \n> \n> +1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.\n\nI submitted a patch for this: Trac #9907.\nCheers,\nJohan",
    "created_at": "2010-09-14T18:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8607#issuecomment-77987",
    "user": "jsrn"
}
```

Replying to [comment:5 jason]:
> Replying to [comment:4 slabbe]:
> 
> > 
> > One last idea (for another ticket) since I am thinking about it. Maybe this `rename_keyword` decorator could move up in `sage/misc` because I think it will be used by more than the plot code.
> > 
> 
> +1.  In fact, the other decorators in that file probably ought to be moved up to sage/misc as well.

I submitted a patch for this: Trac #9907.
Cheers,
Johan
