# Issue 9369: make verbose command flush its output

archive/issues_009369.json:
```json
{
    "body": "Assignee: @jasongrout\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9369\n\n",
    "created_at": "2010-06-28T23:43:29Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "make verbose command flush its output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9369",
    "user": "@williamstein"
}
```
Assignee: @jasongrout



Issue created by migration from https://trac.sagemath.org/ticket/9369





---

archive/issue_comments_089003.json:
```json
{
    "body": "Attachment [trac_9369.patch](tarball://root/attachments/some-uuid/ticket9369/trac_9369.patch) by @williamstein created at 2010-06-28 23:49:05",
    "created_at": "2010-06-28T23:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89003",
    "user": "@williamstein"
}
```

Attachment [trac_9369.patch](tarball://root/attachments/some-uuid/ticket9369/trac_9369.patch) by @williamstein created at 2010-06-28 23:49:05



---

archive/issue_comments_089004.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-28T23:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89004",
    "user": "@williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089005.json:
```json
{
    "body": "The point of this is that if you do\n\n\n```\nsage foo.sage > output.out\ntail -f output.out\n```\n\n\nand use verbose(...) in foo.sage, you'll see nothing for a while, which sucks.",
    "created_at": "2010-06-28T23:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89005",
    "user": "@williamstein"
}
```

The point of this is that if you do


```
sage foo.sage > output.out
tail -f output.out
```


and use verbose(...) in foo.sage, you'll see nothing for a while, which sucks.



---

archive/issue_comments_089006.json:
```json
{
    "body": "This might or might not be slightly off topic. Without verbose, it doesn't seem to be flushing at all. I tried the following in a file called `test.sage` with `./sage test.sage > ~/foo.txt` and `tail -f ~/foo.txt` only showed the output once I interrupted the loop.\n\n\n```\nfor E in cremona_optimal_curves(range(10000)):\n    print E.label(), E.sha().an()\n```\n\n\nI remember doing something like this a long time ago and it working. Wassupwiddat?",
    "created_at": "2010-06-29T18:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89006",
    "user": "@rlmill"
}
```

This might or might not be slightly off topic. Without verbose, it doesn't seem to be flushing at all. I tried the following in a file called `test.sage` with `./sage test.sage > ~/foo.txt` and `tail -f ~/foo.txt` only showed the output once I interrupted the loop.


```
for E in cremona_optimal_curves(range(10000)):
    print E.label(), E.sha().an()
```


I remember doing something like this a long time ago and it working. Wassupwiddat?



---

archive/issue_comments_089007.json:
```json
{
    "body": "Also, if I don't stream the output to a file, it does print in real time. Am I missing a linux-ism here?",
    "created_at": "2010-06-29T18:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89007",
    "user": "@rlmill"
}
```

Also, if I don't stream the output to a file, it does print in real time. Am I missing a linux-ism here?



---

archive/issue_comments_089008.json:
```json
{
    "body": "This sort of behaviour is standard in most programming languages for efficiency: whenever the OS is asked to print to a file (and in some cases, also if it is to a terminal), it collects output until some buffer is filled, and this entire buffer is then output in one go. If flushing is needed (e.g. for when output is only produced rarely between heavy computations), it should be explicitly stated.\n\nI am not completely sure if the above usage corresponds well to the intended workflow of the verbose function, but this concern should at least be considered before adding the mandatory flush statement. After all, the flush statement could just have been manually added in foo.sage.",
    "created_at": "2010-07-30T14:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89008",
    "user": "@johanrosenkilde"
}
```

This sort of behaviour is standard in most programming languages for efficiency: whenever the OS is asked to print to a file (and in some cases, also if it is to a terminal), it collects output until some buffer is filled, and this entire buffer is then output in one go. If flushing is needed (e.g. for when output is only produced rarely between heavy computations), it should be explicitly stated.

I am not completely sure if the above usage corresponds well to the intended workflow of the verbose function, but this concern should at least be considered before adding the mandatory flush statement. After all, the flush statement could just have been manually added in foo.sage.



---

archive/issue_comments_089009.json:
```json
{
    "body": "This is definitely an improvement, regardless. Let's get this merged.",
    "created_at": "2011-01-19T06:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89009",
    "user": "@rlmill"
}
```

This is definitely an improvement, regardless. Let's get this merged.



---

archive/issue_comments_089010.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T06:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89010",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9369#issuecomment-89011",
    "user": "@jdemeyer"
}
```

Resolution: fixed
