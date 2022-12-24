# Issue 9352: givaro spkg: trivial typo in spkg-check

archive/issues_009352.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby\n\nThe file spkg-check in the givaro spkg prints the following if testing fails: \"Error while running the R testsuite ... exiting\".  The new spkg changes \"R\" to \"Givaro\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9352\n\n",
    "created_at": "2010-06-27T17:18:32Z",
    "labels": [
        "spkg-check",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "givaro spkg: trivial typo in spkg-check",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9352",
    "user": "jhpalmieri"
}
```
Assignee: tbd

CC:  drkirkby

The file spkg-check in the givaro spkg prints the following if testing fails: "Error while running the R testsuite ... exiting".  The new spkg changes "R" to "Givaro".


Issue created by migration from https://trac.sagemath.org/ticket/9352





---

archive/issue_comments_088780.json:
```json
{
    "body": "Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket9352/givaro.patch) by jhpalmieri created at 2010-06-27 17:20:11",
    "created_at": "2010-06-27T17:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88780",
    "user": "jhpalmieri"
}
```

Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket9352/givaro.patch) by jhpalmieri created at 2010-06-27 17:20:11



---

archive/issue_comments_088781.json:
```json
{
    "body": "I've attaching the output from \"hg diff\".  The new spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg).",
    "created_at": "2010-06-27T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88781",
    "user": "jhpalmieri"
}
```

I've attaching the output from "hg diff".  The new spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg).



---

archive/issue_comments_088782.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-27T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88782",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-27T17:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88783",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088784.json:
```json
{
    "body": "Positive review of course. \n\nDave",
    "created_at": "2010-06-27T17:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88784",
    "user": "drkirkby"
}
```

Positive review of course. 

Dave



---

archive/issue_comments_088785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88785",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_088786.json:
```json
{
    "body": "Could it be that the version number really should have been\n\n```\ngivaro-3.2.13rc1.p2.spkg\n```\n\ninstead of\n\n```\ngivaro-3.2.13rc2.p2.spkg\n}}}?",
    "created_at": "2011-12-12T09:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88786",
    "user": "jdemeyer"
}
```

Could it be that the version number really should have been

```
givaro-3.2.13rc1.p2.spkg
```

instead of

```
givaro-3.2.13rc2.p2.spkg
}}}?
