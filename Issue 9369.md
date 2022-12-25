# Issue 9369: make verbose command flush its output

archive/issues_009369.json:
```json
{
    "body": "Assignee: @jasongrout\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9369\n\n",
    "created_at": "2010-06-28T23:43:29Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "make verbose command flush its output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9369",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout



Issue created by migration from https://trac.sagemath.org/ticket/9369





---

archive/issue_comments_088863.json:
```json
{
    "body": "Attachment [trac_9369.patch](tarball://root/attachments/some-uuid/ticket9369/trac_9369.patch) by @williamstein created at 2010-06-28 23:49:05",
    "created_at": "2010-06-28T23:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88863",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9369.patch](tarball://root/attachments/some-uuid/ticket9369/trac_9369.patch) by @williamstein created at 2010-06-28 23:49:05



---

archive/issue_comments_088864.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T23:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88864",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088865.json:
```json
{
    "body": "The point of this is that if you do\n\n\n```\nsage foo.sage > output.out\ntail -f output.out\n```\n\n\nand use verbose(...) in foo.sage, you'll see nothing for a while, which sucks.",
    "created_at": "2010-06-28T23:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88865",
    "user": "https://github.com/williamstein"
}
```

The point of this is that if you do


```
sage foo.sage > output.out
tail -f output.out
```


and use verbose(...) in foo.sage, you'll see nothing for a while, which sucks.



---

archive/issue_comments_088866.json:
```json
{
    "body": "This might or might not be slightly off topic. Without verbose, it doesn't seem to be flushing at all. I tried the following in a file called `test.sage` with `./sage test.sage > ~/foo.txt` and `tail -f ~/foo.txt` only showed the output once I interrupted the loop.\n\n\n```\nfor E in cremona_optimal_curves(range(10000)):\n    print E.label(), E.sha().an()\n```\n\n\nI remember doing something like this a long time ago and it working. Wassupwiddat?",
    "created_at": "2010-06-29T18:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88866",
    "user": "https://github.com/rlmill"
}
```

This might or might not be slightly off topic. Without verbose, it doesn't seem to be flushing at all. I tried the following in a file called `test.sage` with `./sage test.sage > ~/foo.txt` and `tail -f ~/foo.txt` only showed the output once I interrupted the loop.


```
for E in cremona_optimal_curves(range(10000)):
    print E.label(), E.sha().an()
```


I remember doing something like this a long time ago and it working. Wassupwiddat?



---

archive/issue_comments_088867.json:
```json
{
    "body": "Also, if I don't stream the output to a file, it does print in real time. Am I missing a linux-ism here?",
    "created_at": "2010-06-29T18:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88867",
    "user": "https://github.com/rlmill"
}
```

Also, if I don't stream the output to a file, it does print in real time. Am I missing a linux-ism here?



---

archive/issue_comments_088868.json:
```json
{
    "body": "This sort of behaviour is standard in most programming languages for efficiency: whenever the OS is asked to print to a file (and in some cases, also if it is to a terminal), it collects output until some buffer is filled, and this entire buffer is then output in one go. If flushing is needed (e.g. for when output is only produced rarely between heavy computations), it should be explicitly stated.\n\nI am not completely sure if the above usage corresponds well to the intended workflow of the verbose function, but this concern should at least be considered before adding the mandatory flush statement. After all, the flush statement could just have been manually added in foo.sage.",
    "created_at": "2010-07-30T14:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88868",
    "user": "https://github.com/johanrosenkilde"
}
```

This sort of behaviour is standard in most programming languages for efficiency: whenever the OS is asked to print to a file (and in some cases, also if it is to a terminal), it collects output until some buffer is filled, and this entire buffer is then output in one go. If flushing is needed (e.g. for when output is only produced rarely between heavy computations), it should be explicitly stated.

I am not completely sure if the above usage corresponds well to the intended workflow of the verbose function, but this concern should at least be considered before adding the mandatory flush statement. After all, the flush statement could just have been manually added in foo.sage.



---

archive/issue_comments_088869.json:
```json
{
    "body": "This is definitely an improvement, regardless. Let's get this merged.",
    "created_at": "2011-01-19T06:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88869",
    "user": "https://github.com/rlmill"
}
```

This is definitely an improvement, regardless. Let's get this merged.



---

archive/issue_comments_088870.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T06:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88870",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088871.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-88871",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_023111.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:21:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9369#event-23111"
}
```
