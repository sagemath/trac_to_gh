# Issue 1306: [graphs] Bundles of graphs

archive/issues_001306.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: graphs\n\nFrom Chris Godsil's wishlist (reply by Jason Grout, second reply by Robert Miller)\n\n\n```\n>>> (e) Bundles: Start with a base graph G with vertices {1, . . . , n}.\n>>> For each\n>>> vertex i we are given a graph Ci . For each edge ij we are given a\n>>> bipartite\n>>> graph joining V (Ci ) to V (Cj ). (There is an implicit orientation here.)\n>>> Some examples:\n>>> (i) The Petersen graph: n = 2, C1 is the 5-cycle, C2 is its complement\n>>> and the bipartite graph is a 5-matching.\n>>> (ii) The Hoffman-Singleton graph can be constructed with n = 2, where\n>>> C1 is an independent set on 15 vertices, C2 is a nice distance regular\n>>> graph on 35 vertices,. . .\n>>> (iii) Covering graphs. Here the graphs Ci are empty on r vertices, and\n>>> each bipartite graphs is either an r-matching or is empty.\n>> Huh, I used this idea extensively in my dissertation and a research\n>> paper. I used the \"blowup graph\" terminology, though, from extremal\n>> graph theory. Is anyone working on this? If not, I'll make a trac ticket.\n> Nobody I know of. If you did this type of stuff in your dissertation,\n> then I nominate you! Create a ticket.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1306\n\n",
    "created_at": "2007-11-28T19:53:26Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[graphs] Bundles of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1306",
    "user": "jason"
}
```
Assignee: mhansen

Keywords: graphs

From Chris Godsil's wishlist (reply by Jason Grout, second reply by Robert Miller)


```
>>> (e) Bundles: Start with a base graph G with vertices {1, . . . , n}.
>>> For each
>>> vertex i we are given a graph Ci . For each edge ij we are given a
>>> bipartite
>>> graph joining V (Ci ) to V (Cj ). (There is an implicit orientation here.)
>>> Some examples:
>>> (i) The Petersen graph: n = 2, C1 is the 5-cycle, C2 is its complement
>>> and the bipartite graph is a 5-matching.
>>> (ii) The Hoffman-Singleton graph can be constructed with n = 2, where
>>> C1 is an independent set on 15 vertices, C2 is a nice distance regular
>>> graph on 35 vertices,. . .
>>> (iii) Covering graphs. Here the graphs Ci are empty on r vertices, and
>>> each bipartite graphs is either an r-matching or is empty.
>> Huh, I used this idea extensively in my dissertation and a research
>> paper. I used the "blowup graph" terminology, though, from extremal
>> graph theory. Is anyone working on this? If not, I'll make a trac ticket.
> Nobody I know of. If you did this type of stuff in your dissertation,
> then I nominate you! Create a ticket.
```


Issue created by migration from https://trac.sagemath.org/ticket/1306





---

archive/issue_comments_008214.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8214",
    "user": "rlm"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008215.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"\".",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8215",
    "user": "rlm"
}
```

Changing keywords from "graphs" to "".



---

archive/issue_comments_008216.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8216",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_008217.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-21T03:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8217",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_008218.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T03:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8218",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008219.json:
```json
{
    "body": "Depends on #1874.",
    "created_at": "2008-01-21T03:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8219",
    "user": "rlm"
}
```

Depends on #1874.



---

archive/issue_comments_008220.json:
```json
{
    "body": "Applies and passes for me after 1874.",
    "created_at": "2008-01-21T04:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8220",
    "user": "mhansen"
}
```

Applies and passes for me after 1874.



---

archive/issue_comments_008221.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T04:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8221",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_008222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8222",
    "user": "mabshoff"
}
```

Resolution: fixed
