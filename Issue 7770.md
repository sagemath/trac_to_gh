# Issue 7770: Implement Tower of Hanoi graph

archive/issues_007770.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: tower of hanoi graph\n\nThe Tower of Hanoi puzzle can be described by a graph whose vertices are possible states of the disks on the pegs, with edges represdenting legitimate moves of a single disk.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7770\n\n",
    "closed_at": "2010-01-03T21:05:01Z",
    "created_at": "2009-12-27T00:02:14Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Implement Tower of Hanoi graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7770",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @rlmill

Keywords: tower of hanoi graph

The Tower of Hanoi puzzle can be described by a graph whose vertices are possible states of the disks on the pegs, with edges represdenting legitimate moves of a single disk.

Issue created by migration from https://trac.sagemath.org/ticket/7770





---

archive/issue_comments_066852.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T00:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66852",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066853.json:
```json
{
    "body": "Some rough timing information on a 3 GHZ Core 2 Duo:\n\n4 pegs, 10 disks, no labels, no layout info\n\n`2^20 = 1,048,576` vertices\n\n3,142,656 edges\n\n240 seconds\n\nDistance between vertex 0 and `(4^10)-1`, ie\n\nthe minimum number of moves to solve the puzzle:\n\n742 ms\n\nI could probably provide timing on sage.math for a release tour (along with a nice graphic).",
    "created_at": "2009-12-27T00:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66853",
    "user": "https://github.com/rbeezer"
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

archive/issue_comments_066854.json:
```json
{
    "body": "Attachment [trac_7770_hanoi_tower_graph.patch](tarball://root/attachments/some-uuid/ticket7770/trac_7770_hanoi_tower_graph.patch) by @rbeezer created at 2009-12-27 00:14:58",
    "created_at": "2009-12-27T00:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66854",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7770_hanoi_tower_graph.patch](tarball://root/attachments/some-uuid/ticket7770/trac_7770_hanoi_tower_graph.patch) by @rbeezer created at 2009-12-27 00:14:58



---

archive/issue_comments_066855.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-30T02:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66855",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066856.json:
```json
{
    "body": "This looks like an interesting patch but \n\n```\nsage -t  \"devel/sage/sage/graphs/graph_generators.py\"\n```\nseems to fail (sage 4.3, imac, 10.6.2).",
    "created_at": "2009-12-30T02:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66856",
    "user": "https://github.com/wdjoyner"
}
```

This looks like an interesting patch but 

```
sage -t  "devel/sage/sage/graphs/graph_generators.py"
```
seems to fail (sage 4.3, imac, 10.6.2).



---

archive/issue_comments_066857.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-30T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66857",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066858.json:
```json
{
    "body": "Replying to [comment:2 wdj]:\n> This looks like an interesting patch but \n> \n> \n> ```\n> sage -t  \"devel/sage/sage/graphs/graph_generators.py\"\n> ```\n> seems to fail (sage 4.3, imac, 10.6.2).\n\n\nArrgghh ... \n\nIgnore this. I'll keep refereeing it.",
    "created_at": "2009-12-30T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66858",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:2 wdj]:
> This looks like an interesting patch but 
> 
> 
> ```
> sage -t  "devel/sage/sage/graphs/graph_generators.py"
> ```
> seems to fail (sage 4.3, imac, 10.6.2).


Arrgghh ... 

Ignore this. I'll keep refereeing it.



---

archive/issue_comments_066859.json:
```json
{
    "body": "Positive review.\n\nInstalls fine on 64bit ubuntu and imac 10.6.2 running sage 4.3. Passes sage -testall on the ubuntu machine and has (I think only) unrelated failures on the imac. Also I check the html output for the reference manual and it looks good.\n\nThanks for this patch Rob! I have used it already in some lecture notes I'm working on for next semester.",
    "created_at": "2009-12-30T12:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66859",
    "user": "https://github.com/wdjoyner"
}
```

Positive review.

Installs fine on 64bit ubuntu and imac 10.6.2 running sage 4.3. Passes sage -testall on the ubuntu machine and has (I think only) unrelated failures on the imac. Also I check the html output for the reference manual and it looks good.

Thanks for this patch Rob! I have used it already in some lecture notes I'm working on for next semester.



---

archive/issue_comments_066860.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T12:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66860",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066861.json:
```json
{
    "body": "Hi David,\n\nThanks for the quick review, and I'm especially glad to hear it is being used *immediately*.  ;-)\n\nI'm going to send you some extra info on the graph off-list. (I don't have permission to post it yet).\n\nRob",
    "created_at": "2009-12-30T17:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66861",
    "user": "https://github.com/rbeezer"
}
```

Hi David,

Thanks for the quick review, and I'm especially glad to hear it is being used *immediately*.  ;-)

I'm going to send you some extra info on the graph off-list. (I don't have permission to post it yet).

Rob



---

archive/issue_comments_066862.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7770#issuecomment-66862",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018589.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T21:05:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7770",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7770#event-18589"
}
```
