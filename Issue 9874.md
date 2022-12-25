# Issue 9874: Can't upload from a notebook link, only from a .sws file

archive/issues_009874.json:
```json
{
    "body": "Assignee: jason, was\n\nTrying to upload using the dialogue and feeding a link to a sage notebook directory (such as `x.sagenb.org/home/username/3/` causes an error - you can only upload sws files.  I think this should be considered a bug, though, since it means you have to actually click on the file instead of just the link in `/pub/`.  \n\nAlternately, creating a link directly to the .sws on each worksheet list (including `/pub/`) would be ok, but I think that's inferior and less elegant.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9875\n\n",
    "created_at": "2010-09-08T15:12:26Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Can't upload from a notebook link, only from a .sws file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9874",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

Trying to upload using the dialogue and feeding a link to a sage notebook directory (such as `x.sagenb.org/home/username/3/` causes an error - you can only upload sws files.  I think this should be considered a bug, though, since it means you have to actually click on the file instead of just the link in `/pub/`.  

Alternately, creating a link directly to the .sws on each worksheet list (including `/pub/`) would be ok, but I think that's inferior and less elegant.

Issue created by migration from https://trac.sagemath.org/ticket/9875





---

archive/issue_comments_097536.json:
```json
{
    "body": "Can you be more clear in your description?  I'm really confused by your description.",
    "created_at": "2010-09-08T15:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97536",
    "user": "https://github.com/jasongrout"
}
```

Can you be more clear in your description?  I'm really confused by your description.



---

archive/issue_comments_097537.json:
```json
{
    "body": "Better?",
    "created_at": "2010-09-08T16:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97537",
    "user": "https://github.com/kcrisman"
}
```

Better?



---

archive/issue_comments_097538.json:
```json
{
    "body": "Much better.  I agree that putting in the URL of a published worksheet would be nice to work.",
    "created_at": "2010-09-08T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97538",
    "user": "https://github.com/jasongrout"
}
```

Much better.  I agree that putting in the URL of a published worksheet would be nice to work.



---

archive/issue_comments_097539.json:
```json
{
    "body": "Is this a duplicate of #7441?\n\nRelated ticket #10652 (shameless plug)",
    "created_at": "2011-01-18T13:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97539",
    "user": "https://github.com/nthiery"
}
```

Is this a duplicate of #7441?

Related ticket #10652 (shameless plug)



---

archive/issue_comments_097540.json:
```json
{
    "body": "I think you're right that it is a duplicate of #7441",
    "created_at": "2011-01-18T13:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97540",
    "user": "https://github.com/jasongrout"
}
```

I think you're right that it is a duplicate of #7441



---

archive/issue_comments_097541.json:
```json
{
    "body": "I've asked some questions on #7441 to verify whether this issue is also taken care of by the patches at #7441.  The description of #7441 is a dup, but the patches might not do exactly what this asks (namely, allowing *old* published worksheets to be uploaded from some server, and not needing the html ending).",
    "created_at": "2011-01-18T14:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97541",
    "user": "https://github.com/kcrisman"
}
```

I've asked some questions on #7441 to verify whether this issue is also taken care of by the patches at #7441.  The description of #7441 is a dup, but the patches might not do exactly what this asks (namely, allowing *old* published worksheets to be uploaded from some server, and not needing the html ending).



---

archive/issue_comments_097542.json:
```json
{
    "body": "It's conceivable that this is resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56), but not necessarily, since the file ending might not be taken care of.",
    "created_at": "2012-07-06T00:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97542",
    "user": "https://github.com/kcrisman"
}
```

It's conceivable that this is resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56), but not necessarily, since the file ending might not be taken care of.



---

archive/issue_comments_097543.json:
```json
{
    "body": "I believe this request did indeed take care of it!  At least, in Sage 5.6 I can confirm that just entering a link of the form\n\n```\nhttp://sage....edu/home/pub/73/\n```\n\nworked nicely.  Jason, can you try this?  I'd like to have dual confirmation that I'm not crazy.",
    "created_at": "2013-06-14T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97543",
    "user": "https://github.com/kcrisman"
}
```

I believe this request did indeed take care of it!  At least, in Sage 5.6 I can confirm that just entering a link of the form

```
http://sage....edu/home/pub/73/
```

worked nicely.  Jason, can you try this?  I'd like to have dual confirmation that I'm not crazy.



---

archive/issue_comments_097544.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-14T17:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97544",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097545.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-18T21:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97545",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097546.json:
```json
{
    "body": "Okay, it was actually [this commit of Dan Drake's](https://github.com/sagemath/sagenb/commit/1b3b2c6793c621032e088e3093c99e87fd55ce07#sagenb/data/sage/html/upload.html).  Yay!",
    "created_at": "2013-06-18T21:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97546",
    "user": "https://github.com/kcrisman"
}
```

Okay, it was actually [this commit of Dan Drake's](https://github.com/sagemath/sagenb/commit/1b3b2c6793c621032e088e3093c99e87fd55ce07#sagenb/data/sage/html/upload.html).  Yay!



---

archive/issue_events_010003.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-06-19T12:17:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9874#event-10003"
}
```



---

archive/issue_comments_097547.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-06-19T12:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9874#issuecomment-97547",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
