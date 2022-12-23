# Issue 4301: [with patch, needs review] lookup generic methods on category

archive/issues_004301.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  mhansen\n\nNo caching is done yet, but it shouldn't be too hard to add at some point. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4301\n\n",
    "created_at": "2008-10-15T16:24:55Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] lookup generic methods on category",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4301",
    "user": "robertwb"
}
```
Assignee: robertwb

CC:  mhansen

No caching is done yet, but it shouldn't be too hard to add at some point. 

Issue created by migration from https://trac.sagemath.org/ticket/4301





---

archive/issue_comments_031449.json:
```json
{
    "body": "Attachment\n\nSo this patch looks good -- I believe that the code does what it claims to. \n\nHowever, there are no doctests. \n\nSo if you say \"there are no categories that implement anything like this yet,\" I believe you -- but let's add one, and put it in the docstring, so that we can use this as an example.",
    "created_at": "2008-11-27T08:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31449",
    "user": "craigcitro"
}
```

Attachment

So this patch looks good -- I believe that the code does what it claims to. 

However, there are no doctests. 

So if you say "there are no categories that implement anything like this yet," I believe you -- but let's add one, and put it in the docstring, so that we can use this as an example.



---

archive/issue_comments_031450.json:
```json
{
    "body": "See http://sagetrac.org/sage_trac/wiki/CategoriesRoadMap",
    "created_at": "2009-05-18T21:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31450",
    "user": "robertwb"
}
```

See http://sagetrac.org/sage_trac/wiki/CategoriesRoadMap



---

archive/issue_comments_031451.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-19T17:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31451",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_031452.json:
```json
{
    "body": "I'm going to go ahead and close this as invalid since we decided on another approach for handling these generic method lookups.",
    "created_at": "2009-10-19T17:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31452",
    "user": "mhansen"
}
```

I'm going to go ahead and close this as invalid since we decided on another approach for handling these generic method lookups.



---

archive/issue_comments_031453.json:
```json
{
    "body": "The other method doesn't work for Cython elements or parents.",
    "created_at": "2009-10-19T17:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31453",
    "user": "robertwb"
}
```

The other method doesn't work for Cython elements or parents.



---

archive/issue_comments_031454.json:
```json
{
    "body": "Hmm... I must have been confused.  I thought we had worked that out in the categories code.\n\nIs this patch still current / relevant?",
    "created_at": "2009-10-19T18:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31454",
    "user": "mhansen"
}
```

Hmm... I must have been confused.  I thought we had worked that out in the categories code.

Is this patch still current / relevant?



---

archive/issue_comments_031455.json:
```json
{
    "body": "The combinat way of doing things was to make all elements and parents into dynamically generated classes with one half coming from their category and the other half from their implementation. Of course, this makes them Python types, which would be an unacceptable speed regression for, e.g. Integer, so we need some manual lookup in that case. \n\nWhat we haven't done is figured out how the these two different approaches would interact, and this should be worked out before applying (some variation of) the above patch.",
    "created_at": "2009-10-20T05:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4301#issuecomment-31455",
    "user": "robertwb"
}
```

The combinat way of doing things was to make all elements and parents into dynamically generated classes with one half coming from their category and the other half from their implementation. Of course, this makes them Python types, which would be an unacceptable speed regression for, e.g. Integer, so we need some manual lookup in that case. 

What we haven't done is figured out how the these two different approaches would interact, and this should be worked out before applying (some variation of) the above patch.
