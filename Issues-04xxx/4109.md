# Issue 4109: The position dictionary of a graph is not cleared when creating a complement.

archive/issues_004109.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\ng=graphs.PathGraph(6)\ng.show()\nh = g.complement()\nh.show()\n```\nThe last command shows the original P_6, not the complement.  However, calling `h.edges()` seems to return the right results.  Also, `Graph(h).show()` shows the correct thing, I think.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4109\n\n",
    "closed_at": "2008-09-13T18:45:06Z",
    "created_at": "2008-09-13T04:43:20Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "The position dictionary of a graph is not cleared when creating a complement.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4109",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

```
g=graphs.PathGraph(6)
g.show()
h = g.complement()
h.show()
```
The last command shows the original P_6, not the complement.  However, calling `h.edges()` seems to return the right results.  Also, `Graph(h).show()` shows the correct thing, I think.



Issue created by migration from https://trac.sagemath.org/ticket/4109





---

archive/issue_comments_029692.json:
```json
{
    "body": "The possible problem:\n\n```\n[22:40] <rlm_> jason- the position dict of the path graph is set\n[22:40] <rlm_> use layout='spring'\n[22:41] *** rlm_ is now known as rlm|afk.\n[22:42] <jason-> rlm_: okay, so the pos dict just needs to be cleared when creating the complement, I guess.\n```",
    "created_at": "2008-09-13T04:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4109#issuecomment-29692",
    "user": "https://github.com/jasongrout"
}
```

The possible problem:

```
[22:40] <rlm_> jason- the position dict of the path graph is set
[22:40] <rlm_> use layout='spring'
[22:41] *** rlm_ is now known as rlm|afk.
[22:42] <jason-> rlm_: okay, so the pos dict just needs to be cleared when creating the complement, I guess.
```



---

archive/issue_comments_029693.json:
```json
{
    "body": "This was actually a design decision -- if you take the complement, the vertices are in the same position, and you can see where the edges are and are not. Perhaps the path graph should have a more than one dimensional layout...",
    "created_at": "2008-09-13T07:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4109#issuecomment-29693",
    "user": "https://github.com/rlmill"
}
```

This was actually a design decision -- if you take the complement, the vertices are in the same position, and you can see where the edges are and are not. Perhaps the path graph should have a more than one dimensional layout...



---

archive/issue_comments_029694.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-13T18:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4109#issuecomment-29694",
    "user": "https://github.com/rlmill"
}
```

Resolution: wontfix



---

archive/issue_comments_029695.json:
```json
{
    "body": "Since this is a design decision and not a bug, I'm invalidating the ticket. If you think it's a bad design decision, take it to the mailing list. If you think path graphs shouldn't layout in lines, make a new ticket.",
    "created_at": "2008-09-13T18:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4109#issuecomment-29695",
    "user": "https://github.com/rlmill"
}
```

Since this is a design decision and not a bug, I'm invalidating the ticket. If you think it's a bad design decision, take it to the mailing list. If you think path graphs shouldn't layout in lines, make a new ticket.



---

archive/issue_events_009362.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-09-13T18:45:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4109",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4109#event-9362"
}
```
