# Issue 9727: RepresentationGraph method that generalizes IntervalGraph

archive/issues_009727.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  ncohen\n\nThis patch creates a new graph constructor called RepresentationGraph. This method generalizes IntervalGraph. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9727\n\n",
    "created_at": "2010-08-11T20:43:30Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "RepresentationGraph method that generalizes IntervalGraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9727",
    "user": "edward.scheinerman"
}
```
Assignee: jason, ncohen, rlm

CC:  ncohen

This patch creates a new graph constructor called RepresentationGraph. This method generalizes IntervalGraph. 

Issue created by migration from https://trac.sagemath.org/ticket/9727





---

archive/issue_comments_095067.json:
```json
{
    "body": "The old IntervalGraph method did not permit the same interval to be used twice for different vertices (and gave an erroneous result in some cases). The new IntervalGraph method in this patch fixes those issues.",
    "created_at": "2010-08-11T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95067",
    "user": "edward.scheinerman"
}
```

The old IntervalGraph method did not permit the same interval to be used twice for different vertices (and gave an erroneous result in some cases). The new IntervalGraph method in this patch fixes those issues.



---

archive/issue_comments_095068.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-12T04:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95068",
    "user": "ncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095069.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-15T20:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95069",
    "user": "edward.scheinerman"
}
```

Attachment



---

archive/issue_comments_095070.json:
```json
{
    "body": "Hello. This latest version of the patch now passes all tests!",
    "created_at": "2010-08-15T20:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95070",
    "user": "edward.scheinerman"
}
```

Hello. This latest version of the patch now passes all tests!



---

archive/issue_comments_095071.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-15T20:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95071",
    "user": "edward.scheinerman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095072.json:
```json
{
    "body": "Hmmm.. I know that I would never had noticed it had I not been working on Sage's graphs for a long time, but it looks like what RepresentationGraph does is already a feature of the Graph constructor : it is illustrated as the third example of `Graph?`. What do you think we should do in this case ? Clearly, this information is not very easy to get, and my method IntervalGraph should just call this constructor instead of doing the same job again (though we can slightly optimise if we know it is an interval graph)... Well, what do you think ? `:-/`\n\nNathann",
    "created_at": "2010-08-23T02:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95072",
    "user": "ncohen"
}
```

Hmmm.. I know that I would never had noticed it had I not been working on Sage's graphs for a long time, but it looks like what RepresentationGraph does is already a feature of the Graph constructor : it is illustrated as the third example of `Graph?`. What do you think we should do in this case ? Clearly, this information is not very easy to get, and my method IntervalGraph should just call this constructor instead of doing the same job again (though we can slightly optimise if we know it is an interval graph)... Well, what do you think ? `:-/`

Nathann



---

archive/issue_comments_095073.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-08-23T02:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95073",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_095074.json:
```json
{
    "body": "Interesting, but the Graph constructor works differently and does not provide all the functionality that GraphRepresentation does. For example, it will not solve the problem of repeated intervals being recognized as separate vertices (but with the same closed neighborhoods). It will also not accept a dictionary instead of a list as we have set up in RepresentationGraph. \n\nOne solution might be to rework the Graph() constructor to accept a [dictionary,function] pair. In that case, the vertices would be the keys of the dictionary. Two vertices would be adjacent if the function, applied to the values associated with two keys, returns True. How difficult would that be? If easy, then that may be a preferable route. If difficult, then I prefer this route.\n\nIt is true that if one sorts the intervals before iterating over pairs, some speed up can be realized (especially for a sparse interval graph); but this efficiency comes at a cost of some generality. Also, for a random interval graph, the speedup will not be so dramatic as these random graphs are dense.\n\nEd",
    "created_at": "2010-08-23T22:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95074",
    "user": "edward.scheinerman"
}
```

Interesting, but the Graph constructor works differently and does not provide all the functionality that GraphRepresentation does. For example, it will not solve the problem of repeated intervals being recognized as separate vertices (but with the same closed neighborhoods). It will also not accept a dictionary instead of a list as we have set up in RepresentationGraph. 

One solution might be to rework the Graph() constructor to accept a [dictionary,function] pair. In that case, the vertices would be the keys of the dictionary. Two vertices would be adjacent if the function, applied to the values associated with two keys, returns True. How difficult would that be? If easy, then that may be a preferable route. If difficult, then I prefer this route.

It is true that if one sorts the intervals before iterating over pairs, some speed up can be realized (especially for a sparse interval graph); but this efficiency comes at a cost of some generality. Also, for a random interval graph, the speedup will not be so dramatic as these random graphs are dense.

Ed



---

archive/issue_comments_095075.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-25T12:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95075",
    "user": "edward.scheinerman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_095076.json:
```json
{
    "body": "I withdraw this ticket. A new version of IntervalGraph is posted as tickect #9862. RepresentationGraph is probably not needed as its functionality is (mostly) available in the Graph() constructor. Modifications to Graph() to accept [dictionary,function] may be forthcoming at a later date.",
    "created_at": "2010-09-06T18:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95076",
    "user": "edward.scheinerman"
}
```

I withdraw this ticket. A new version of IntervalGraph is posted as tickect #9862. RepresentationGraph is probably not needed as its functionality is (mostly) available in the Graph() constructor. Modifications to Graph() to accept [dictionary,function] may be forthcoming at a later date.



---

archive/issue_comments_095077.json:
```json
{
    "body": "Remove assignee jason, ncohen, rlm.",
    "created_at": "2010-09-06T18:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95077",
    "user": "edward.scheinerman"
}
```

Remove assignee jason, ncohen, rlm.



---

archive/issue_comments_095078.json:
```json
{
    "body": "Set assignee to edward.scheinerman.",
    "created_at": "2010-09-07T01:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95078",
    "user": "edward.scheinerman"
}
```

Set assignee to edward.scheinerman.



---

archive/issue_comments_095079.json:
```json
{
    "body": "Remove assignee edward.scheinerman.",
    "created_at": "2010-09-07T01:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95079",
    "user": "edward.scheinerman"
}
```

Remove assignee edward.scheinerman.



---

archive/issue_comments_095080.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-09-08T02:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95080",
    "user": "ddrake"
}
```

Resolution: wontfix



---

archive/issue_comments_095081.json:
```json
{
    "body": "Ed has request that this ticket be closed. He sent an email that said:\n\n\n```\nDear Sage Manager:\n\nA few weeks ago I posted Trac ticket #9727 entitled \"RepresentationGraph method\nthat generalizes IntervalGraph\". Since that time, working with Nathann Cohen, I\nposted an alternative, more focused solution to minor glitches in the\nIntervalGraph method. Further, the RepresentationGraph method functionality is\npartially already present in the Graph() constructor and I am considering a\ndirect enhancement of Graph() at some future time to add a bit more\nfunctionality.\n\nSo, to make a long story short, I would like to cancel my posting of 9727, but I\ndon't see how to do that in Trac. Can you please do this for me?\n\nThanks,\n\nEd Scheinerman\n```\n\n\nI'm setting this as \"wontfix\" since it seems like they, well, won't use this enhancement and work on things later.",
    "created_at": "2010-09-08T02:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9727#issuecomment-95081",
    "user": "ddrake"
}
```

Ed has request that this ticket be closed. He sent an email that said:


```
Dear Sage Manager:

A few weeks ago I posted Trac ticket #9727 entitled "RepresentationGraph method
that generalizes IntervalGraph". Since that time, working with Nathann Cohen, I
posted an alternative, more focused solution to minor glitches in the
IntervalGraph method. Further, the RepresentationGraph method functionality is
partially already present in the Graph() constructor and I am considering a
direct enhancement of Graph() at some future time to add a bit more
functionality.

So, to make a long story short, I would like to cancel my posting of 9727, but I
don't see how to do that in Trac. Can you please do this for me?

Thanks,

Ed Scheinerman
```


I'm setting this as "wontfix" since it seems like they, well, won't use this enhancement and work on things later.
