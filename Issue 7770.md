# Issue 7770: Implement Tower of Hanoi graph

archive/issues_007770.json:
```json
{
    "body": "Assignee: rlm\n\nKeywords: tower of hanoi graph\n\nThe Tower of Hanoi puzzle can be described by a graph whose vertices are possible states of the disks on the pegs, with edges represdenting legitimate moves of a single disk.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7770\n\n",
    "created_at": "2009-12-27T00:02:14Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "Implement Tower of Hanoi graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7770",
    "user": "rbeezer"
}
```
Assignee: rlm

Keywords: tower of hanoi graph

The Tower of Hanoi puzzle can be described by a graph whose vertices are possible states of the disks on the pegs, with edges represdenting legitimate moves of a single disk.

Issue created by migration from https://trac.sagemath.org/ticket/7770





---

archive/issue_comments_066968.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T00:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66968",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066969.json:
```json
{
    "body": "Some rough timing information on a 3 GHZ Core 2 Duo:\n\n4 pegs, 10 disks, no labels, no layout info\n\n`2^20 = 1,048,576` vertices\n\n3,142,656 edges\n\n240 seconds\n\nDistance between vertex 0 and `(4^10)-1`, ie\n\nthe minimum number of moves to solve the puzzle:\n\n742 ms\n\nI could probably provide timing on sage.math for a release tour (along with a nice graphic).",
    "created_at": "2009-12-27T00:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66969",
    "user": "rbeezer"
}
```

Some rough timing information on a 3 GHZ Core 2 Duo:

4 pegs, 10 disks, no labels, no layout info

`2^20 = 1,048,576` vertices

3,142,656 edges

240 seconds

Distance between vertex 0 and `(4^10)-1`, ie

the minimum number of moves to solve the puzzle:

742 ms

I could probably provide timing on sage.math for a release tour (along with a nice graphic).



---

archive/issue_comments_066970.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-12-27T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66970",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_066971.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-30T02:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66971",
    "user": "wdj"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066972.json:
```json
{
    "body": "This looks like an interesting patch but \n\n\n```\nsage -t  \"devel/sage/sage/graphs/graph_generators.py\"\n```\n\nseems to fail (sage 4.3, imac, 10.6.2).",
    "created_at": "2009-12-30T02:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66972",
    "user": "wdj"
}
```

This looks like an interesting patch but 


```
sage -t  "devel/sage/sage/graphs/graph_generators.py"
```

seems to fail (sage 4.3, imac, 10.6.2).



---

archive/issue_comments_066973.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-30T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66973",
    "user": "wdj"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066974.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> This looks like an interesting patch but \n> \n> {{{\n> sage -t  \"devel/sage/sage/graphs/graph_generators.py\"\n> }}}\n> seems to fail (sage 4.3, imac, 10.6.2).\n\nArrgghh ... \n\nIgnore this. I'll keep refereeing it.",
    "created_at": "2009-12-30T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66974",
    "user": "wdj"
}
```

Replying to [comment:2 wdj]:
> This looks like an interesting patch but 
> 
> {{{
> sage -t  "devel/sage/sage/graphs/graph_generators.py"
> }}}
> seems to fail (sage 4.3, imac, 10.6.2).

Arrgghh ... 

Ignore this. I'll keep refereeing it.



---

archive/issue_comments_066975.json:
```json
{
    "body": "Positive review.\n\nInstalls fine on 64bit ubuntu and imac 10.6.2 running sage 4.3. Passes sage -testall on the ubuntu machine and has (I think only) unrelated failures on the imac. Also I check the html output for the reference manual and it looks good.\n\nThanks for this patch Rob! I have used it already in some lecture notes I'm working on for next semester.",
    "created_at": "2009-12-30T12:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66975",
    "user": "wdj"
}
```

Positive review.

Installs fine on 64bit ubuntu and imac 10.6.2 running sage 4.3. Passes sage -testall on the ubuntu machine and has (I think only) unrelated failures on the imac. Also I check the html output for the reference manual and it looks good.

Thanks for this patch Rob! I have used it already in some lecture notes I'm working on for next semester.



---

archive/issue_comments_066976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T12:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66976",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066977.json:
```json
{
    "body": "Hi David,\n\nThanks for the quick review, and I'm especially glad to hear it is being used *immediately*.  ;-)\n\nI'm going to send you some extra info on the graph off-list. (I don't have permission to post it yet).\n\nRob",
    "created_at": "2009-12-30T17:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66977",
    "user": "rbeezer"
}
```

Hi David,

Thanks for the quick review, and I'm especially glad to hear it is being used *immediately*.  ;-)

I'm going to send you some extra info on the graph off-list. (I don't have permission to post it yet).

Rob



---

archive/issue_comments_066978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66978",
    "user": "mhansen"
}
```

Resolution: fixed
