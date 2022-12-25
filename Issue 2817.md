# Issue 2817: specify options for parts of graphs

archive/issues_002817.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen\n\nSee the post at:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/64b76550609c1019\n\nOne way to handle setting display options for different vertices/edges is to have the following conventions:\n\n* If edge_style is the dictionary **edge_style, pass **edge_style into the arrow() commands\n* If edge_style is a list, then we want to create (possibly different) edge_style dictionaries for each edge.  For each item in the list:\n   * if the item is a dictionary d, then update all edge_style dictionaries with the dictionary d.\n   * if the item is a list L with L[0]=list of edges, L[1]=dictionary d, then for each edge in L[0], update its edge_style with d.\n\nOptimize this so that we create a dictionary for an edge iff it has a different edge style than other edges.  In other words, first have only one edge_style dictionary.  If a list is edges is then specified, then take those out of the default edge_list and update their dictionary, etc.  is there a data structure which efficiently partitions objects (maybe Sage partitions!?)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2817\n\n",
    "created_at": "2008-04-05T22:37:11Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "specify options for parts of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2817",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  @nathanncohen

See the post at:

http://groups.google.com/group/sage-support/browse_thread/thread/64b76550609c1019

One way to handle setting display options for different vertices/edges is to have the following conventions:

* If edge_style is the dictionary **edge_style, pass **edge_style into the arrow() commands
* If edge_style is a list, then we want to create (possibly different) edge_style dictionaries for each edge.  For each item in the list:
   * if the item is a dictionary d, then update all edge_style dictionaries with the dictionary d.
   * if the item is a list L with L[0]=list of edges, L[1]=dictionary d, then for each edge in L[0], update its edge_style with d.

Optimize this so that we create a dictionary for an edge iff it has a different edge style than other edges.  In other words, first have only one edge_style dictionary.  If a list is edges is then specified, then take those out of the default edge_list and update their dictionary, etc.  is there a data structure which efficiently partitions objects (maybe Sage partitions!?)

Issue created by migration from https://trac.sagemath.org/ticket/2817





---

archive/issue_comments_019302.json:
```json
{
    "body": "Changing assignee from @rlmill to @jasongrout.",
    "created_at": "2008-09-10T03:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19302",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @rlmill to @jasongrout.



---

archive/issue_comments_019303.json:
```json
{
    "body": "Nathann, I think this is a duplicate of #13827. If you agree, please put on positive_review.",
    "created_at": "2016-01-04T19:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19303",
    "user": "https://github.com/jm58660"
}
```

Nathann, I think this is a duplicate of #13827. If you agree, please put on positive_review.



---

archive/issue_comments_019304.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-01-04T19:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19304",
    "user": "https://github.com/jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_019305.json:
```json
{
    "body": "Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.\n\nNathann",
    "created_at": "2016-01-04T21:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19305",
    "user": "https://github.com/nathanncohen"
}
```

Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.

Nathann



---

archive/issue_comments_019306.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-01-05T05:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19306",
    "user": "https://github.com/jm58660"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_019307.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.\n\nDone that.\n\n(For now that ticket is kind of waiting for someone to decide if my suggestions are good or not. \u200bPunarbasu Purkayastha suggested other kind of interface.)",
    "created_at": "2016-01-05T05:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19307",
    "user": "https://github.com/jm58660"
}
```

Replying to [comment:4 ncohen]:
> Do you consider #13827 as a ticket which aims at making all options of `Graph.plot` able to take [edge/vertex]-specific instructions? If so, could you update its description before setting this one to `positive_review`? Right now all the description of #13827 says is that it should be possible to provide an alternative text to the vertices' name.

Done that.

(For now that ticket is kind of waiting for someone to decide if my suggestions are good or not. ​Punarbasu Purkayastha suggested other kind of interface.)



---

archive/issue_comments_019308.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2016-01-06T00:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2817#issuecomment-19308",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_003007.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2016-01-06T00:01:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2817#event-3007"
}
```
