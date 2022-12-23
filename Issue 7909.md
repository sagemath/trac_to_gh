# Issue 7909: Replace $MKDIR with 'mkdir' in sage-spkg

archive/issues_007909.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  jsp\n\nsage-env has $MKDIR in one place, which will cause problems with an updated 'sage-env' which no longer defines MKDIR. \n\nI'm attaching a copy of the revised sage-env, and also a Mercurial patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7909\n\n",
    "created_at": "2010-01-12T16:15:32Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Replace $MKDIR with 'mkdir' in sage-spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7909",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  jsp

sage-env has $MKDIR in one place, which will cause problems with an updated 'sage-env' which no longer defines MKDIR. 

I'm attaching a copy of the revised sage-env, and also a Mercurial patch.

Issue created by migration from https://trac.sagemath.org/ticket/7909





---

archive/issue_comments_068778.json:
```json
{
    "body": "Attachment\n\nA complete copy of the revised sage-env",
    "created_at": "2010-01-12T16:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68778",
    "user": "drkirkby"
}
```

Attachment

A complete copy of the revised sage-env



---

archive/issue_comments_068779.json:
```json
{
    "body": "Mercurial patch for sage-env",
    "created_at": "2010-01-12T16:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68779",
    "user": "drkirkby"
}
```

Mercurial patch for sage-env



---

archive/issue_comments_068780.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-12T16:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68780",
    "user": "drkirkby"
}
```

Attachment



---

archive/issue_comments_068781.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T16:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68781",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068782.json:
```json
{
    "body": "Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?\n\nThe patch is simple and looks good.\n\n\nJaap",
    "created_at": "2010-01-12T16:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68782",
    "user": "jsp"
}
```

Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?

The patch is simple and looks good.


Jaap



---

archive/issue_comments_068783.json:
```json
{
    "body": "Replying to [comment:2 jsp]:\n> Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?\n> \n> The patch is simple and looks good.\n> \n> \n> Jaap\n> \n\nIt is really in sage-spkg!!  I changed the description.\n\nWaiting for the mercurial patch.\n\nJaap",
    "created_at": "2010-01-12T17:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68783",
    "user": "jsp"
}
```

Replying to [comment:2 jsp]:
> Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?
> 
> The patch is simple and looks good.
> 
> 
> Jaap
> 

It is really in sage-spkg!!  I changed the description.

Waiting for the mercurial patch.

Jaap



---

archive/issue_comments_068784.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T17:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68784",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068785.json:
```json
{
    "body": "The \"mercurial patch\" is ok. sage-spkg looks good. So positive review.\n\nJaap",
    "created_at": "2010-01-12T17:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68785",
    "user": "jsp"
}
```

The "mercurial patch" is ok. sage-spkg looks good. So positive review.

Jaap



---

archive/issue_comments_068786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T03:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68786",
    "user": "rlm"
}
```

Resolution: fixed
