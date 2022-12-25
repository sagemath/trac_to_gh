# Issue 7409: Partitions(n).random_element() is extremely slow

archive/issues_007409.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nKeywords: random integer partition, placherel measure\n\nIt is currently implemented by building the list !\nHere are some suggestions: Look at \n\n```\nhttp://www.site.uottawa.ca/~ivan/F49-int-part.pdf\n```\n\nThanks to #7408 we have a fast algorithm for generating partitions with Plancherel measure. So I suggest the following interface:\n\n```\nParitions(n).random_element()\n```\n\ndefault to\n\n```\nPartitions(n).random_element_uniform()\n```\n\nand to implement\n\n```\nPartitions(n).random_element_Plancherel()\n```\n\nAny comment about the interface ? \n\nCheers,\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7409\n\n",
    "created_at": "2009-11-08T10:33:58Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Partitions(n).random_element() is extremely slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7409",
    "user": "https://github.com/hivert"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Keywords: random integer partition, placherel measure

It is currently implemented by building the list !
Here are some suggestions: Look at 

```
http://www.site.uottawa.ca/~ivan/F49-int-part.pdf
```

Thanks to #7408 we have a fast algorithm for generating partitions with Plancherel measure. So I suggest the following interface:

```
Paritions(n).random_element()
```

default to

```
Partitions(n).random_element_uniform()
```

and to implement

```
Partitions(n).random_element_Plancherel()
```

Any comment about the interface ? 

Cheers,

Florent

Issue created by migration from https://trac.sagemath.org/ticket/7409





---

archive/issue_comments_062236.json:
```json
{
    "body": "I would think something like \n\n\n```\nPartitions(n).random_element(distribution='uniform') #default\nPartitions(n).random_element(distribution='plancherel')\n```\n",
    "created_at": "2009-11-08T14:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62236",
    "user": "https://github.com/mwhansen"
}
```

I would think something like 


```
Partitions(n).random_element(distribution='uniform') #default
Partitions(n).random_element(distribution='plancherel')
```




---

archive/issue_comments_062237.json:
```json
{
    "body": "Changing assignee from @mwhansen to @hivert.",
    "created_at": "2009-11-13T15:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62237",
    "user": "https://github.com/hivert"
}
```

Changing assignee from @mwhansen to @hivert.



---

archive/issue_comments_062238.json:
```json
{
    "body": "Attachment [trac_7409_random_partitions.patch](tarball://root/attachments/some-uuid/ticket7409/trac_7409_random_partitions.patch) by @hivert created at 2009-11-24 12:50:27\n\nI implemented an algorithm from \"Nijenhuis, Wilf, Combinatorial Algorithms\" which looks reasonably fast. There is certainly room for improvement. However, It will be done later if needed.",
    "created_at": "2009-11-24T12:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62238",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7409_random_partitions.patch](tarball://root/attachments/some-uuid/ticket7409/trac_7409_random_partitions.patch) by @hivert created at 2009-11-24 12:50:27

I implemented an algorithm from "Nijenhuis, Wilf, Combinatorial Algorithms" which looks reasonably fast. There is certainly room for improvement. However, It will be done later if needed.



---

archive/issue_comments_062239.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-24T12:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62239",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062240.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-01T04:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62240",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_events_007634.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-01T04:56:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7409#event-7634"
}
```



---

archive/issue_comments_062241.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T04:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7409#issuecomment-62241",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
