# Issue 7304: [With patch, needs review] Contract edge in graph

archive/issues_007304.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  brunellus lkeough @dcoudert @tscrim stefan yomcat\n\nThis patch contract an edge (u,v) in a graph. In the resulting graph vertex u is merged into vertex v.\n\nThe variables u and v can be passed as variables, a tuple (u,v) or a 3-tuple (u,v,'label'). The last allows us to use an element from G.edges() for contraction.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7304\n\n",
    "created_at": "2009-10-25T20:04:34Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.0",
    "title": "[With patch, needs review] Contract edge in graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7304",
    "user": "https://github.com/haaninjo"
}
```
Assignee: @rlmill

CC:  brunellus lkeough @dcoudert @tscrim stefan yomcat

This patch contract an edge (u,v) in a graph. In the resulting graph vertex u is merged into vertex v.

The variables u and v can be passed as variables, a tuple (u,v) or a 3-tuple (u,v,'label'). The last allows us to use an element from G.edges() for contraction.

Issue created by migration from https://trac.sagemath.org/ticket/7304





---

archive/issue_comments_060802.json:
```json
{
    "body": "Attachment [trac_7304.patch](tarball://root/attachments/some-uuid/ticket7304/trac_7304.patch) by @haaninjo created at 2009-10-25 20:06:41\n\nInitial patch for review",
    "created_at": "2009-10-25T20:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60802",
    "user": "https://github.com/haaninjo"
}
```

Attachment [trac_7304.patch](tarball://root/attachments/some-uuid/ticket7304/trac_7304.patch) by @haaninjo created at 2009-10-25 20:06:41

Initial patch for review



---

archive/issue_comments_060803.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-25T20:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60803",
    "user": "https://github.com/haaninjo"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_060804.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-25T20:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60804",
    "user": "https://github.com/haaninjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060805.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-25T21:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60805",
    "user": "https://github.com/haaninjo"
}
```

Resolution: duplicate



---

archive/issue_events_017298.json:
```json
{
    "actor": "https://github.com/haaninjo",
    "created_at": "2009-10-25T21:05:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17298"
}
```



---

archive/issue_comments_060806.json:
```json
{
    "body": "Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.",
    "created_at": "2009-10-25T21:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60806",
    "user": "https://github.com/haaninjo"
}
```

Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.



---

archive/issue_events_017299.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-26T03:04:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17299"
}
```



---

archive/issue_comments_060807.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2009-10-27T18:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60807",
    "user": "https://github.com/haaninjo"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_060808.json:
```json
{
    "body": "On second thought, reopening.\n\nMerging vertices gives a slightly different result for certain cases that are important in deletion-contraction algorithms, so this function has a place to fill as well.\n\nExample of case that contract_edge() handles differently:\n\nIf we have two vertices A, B, with two parallel edges between them, a merging of A and B results in a single vertex with no edge or loops. If we instead choose to contract one of the two parallel edges (and allow loops), we will end up with a single vertex which has a loop.",
    "created_at": "2009-10-27T18:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60808",
    "user": "https://github.com/haaninjo"
}
```

On second thought, reopening.

Merging vertices gives a slightly different result for certain cases that are important in deletion-contraction algorithms, so this function has a place to fill as well.

Example of case that contract_edge() handles differently:

If we have two vertices A, B, with two parallel edges between them, a merging of A and B results in a single vertex with no edge or loops. If we instead choose to contract one of the two parallel edges (and allow loops), we will end up with a single vertex which has a loop.



---

archive/issue_events_017300.json:
```json
{
    "actor": "https://github.com/haaninjo",
    "created_at": "2009-10-27T18:19:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17300"
}
```



---

archive/issue_events_017301.json:
```json
{
    "actor": "https://github.com/haaninjo",
    "created_at": "2009-10-27T18:19:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17301"
}
```



---

archive/issue_comments_060809.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2009-10-27T18:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60809",
    "user": "https://github.com/haaninjo"
}
```

Changing status from closed to new.



---

archive/issue_events_017302.json:
```json
{
    "actor": "https://github.com/haaninjo",
    "created_at": "2009-10-27T18:19:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17302"
}
```



---

archive/issue_comments_060810.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-27T18:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60810",
    "user": "https://github.com/haaninjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060811.json:
```json
{
    "body": "Replying to [comment:2 AJonsson]:\n> Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.\n\nAnders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.",
    "created_at": "2009-10-28T12:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 AJonsson]:
> Duplicate of #7159 . That ticket is about vertex merging, but it is basically the same thing.

Anders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.



---

archive/issue_comments_060812.json:
```json
{
    "body": "Replying to [comment:6 mvngu]:\n> Anders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.\n\n\nWhoops. Hadn't seen that section. Won't happen again.",
    "created_at": "2009-10-28T19:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60812",
    "user": "https://github.com/haaninjo"
}
```

Replying to [comment:6 mvngu]:
> Anders, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.


Whoops. Hadn't seen that section. Won't happen again.



---

archive/issue_comments_060813.json:
```json
{
    "body": "I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...\n\nNathann",
    "created_at": "2009-10-31T20:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60813",
    "user": "https://github.com/nathanncohen"
}
```

I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...

Nathann



---

archive/issue_comments_060814.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-31T20:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60814",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_060815.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n> I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...\n> \n> Nathann\n\n\nI don't feel too strongly about it. As long as full functionality exists, it matters little to me if it is in one or two functions.",
    "created_at": "2009-11-01T09:52:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60815",
    "user": "https://github.com/haaninjo"
}
```

Replying to [comment:8 ncohen]:
> I understand your point, but do you think it useful to have 2 different functions to merge vertices, instead of having just one with more options ? It could be a bit confusing...
> 
> Nathann


I don't feel too strongly about it. As long as full functionality exists, it matters little to me if it is in one or two functions.



---

archive/issue_comments_060816.json:
```json
{
    "body": "My advice exactly ! \n\nCould you then write a patch to modify #7159 as soon as it will be merged ? You could also directly modify the trac ticket as it is not merged yet, but then we would be looking for someone else to review it, as for #7814...\n\nAs you said, I do not mind as long as the two behaviours exist.. If you think your version of merging should be the default one, it's up to you ! :-)",
    "created_at": "2009-11-01T09:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60816",
    "user": "https://github.com/nathanncohen"
}
```

My advice exactly ! 

Could you then write a patch to modify #7159 as soon as it will be merged ? You could also directly modify the trac ticket as it is not merged yet, but then we would be looking for someone else to review it, as for #7814...

As you said, I do not mind as long as the two behaviours exist.. If you think your version of merging should be the default one, it's up to you ! :-)



---

archive/issue_comments_060817.json:
```json
{
    "body": "Ok, will look closer into a modification of #7159 to be added after that ticket has been merged to Sage.",
    "created_at": "2009-11-01T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60817",
    "user": "https://github.com/haaninjo"
}
```

Ok, will look closer into a modification of #7159 to be added after that ticket has been merged to Sage.



---

archive/issue_comments_060818.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2009-11-01T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60818",
    "user": "https://github.com/haaninjo"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_060819.json:
```json
{
    "body": "should we keep this ticket open, or close it and open a new one with your modification of #7159 ?",
    "created_at": "2009-12-05T09:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60819",
    "user": "https://github.com/nathanncohen"
}
```

should we keep this ticket open, or close it and open a new one with your modification of #7159 ?



---

archive/issue_comments_060820.json:
```json
{
    "body": "Replying to [comment:13 ncohen]:\n> should we keep this ticket open, or close it and open a new one with your modification of #7159 ?\n\n\nLet's keep it open, otherwise we would just open an almost identical ticket. I will see if I get the time to finish the function sometime next week.",
    "created_at": "2009-12-07T00:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60820",
    "user": "https://github.com/haaninjo"
}
```

Replying to [comment:13 ncohen]:
> should we keep this ticket open, or close it and open a new one with your modification of #7159 ?


Let's keep it open, otherwise we would just open an almost identical ticket. I will see if I get the time to finish the function sometime next week.



---

archive/issue_comments_060821.json:
```json
{
    "body": "[\u043a\u0443\u043f\u043b\u044e \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d](http://forum.mobile-shop.kiev.ua/)",
    "created_at": "2010-04-30T14:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60821",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp"
}
```

[куплю мобильный телефон](http://forum.mobile-shop.kiev.ua/)



---

archive/issue_comments_060822.json:
```json
{
    "body": "There's a spam link above here that needs removing.\n\nAs a matroid theorist, I look at deletion and contraction a bit differently. It bothers me that I cannot write something along the lines of\n\nH = G.delete((1,2)).contract([(3,5),(6,7)])\n\nwithout modifying G.",
    "created_at": "2011-04-11T15:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60822",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

There's a spam link above here that needs removing.

As a matroid theorist, I look at deletion and contraction a bit differently. It bothers me that I cannot write something along the lines of

H = G.delete((1,2)).contract([(3,5),(6,7)])

without modifying G.



---

archive/issue_comments_060823.json:
```json
{
    "body": "What would your code do ? Are your pairs edges or vertices ? Right now your have a merge_vertices commands in Graph that lets you contract any set of vertices.\n\nNathann",
    "created_at": "2011-04-11T15:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60823",
    "user": "https://github.com/nathanncohen"
}
```

What would your code do ? Are your pairs edges or vertices ? Right now your have a merge_vertices commands in Graph that lets you contract any set of vertices.

Nathann



---

archive/issue_comments_060824.json:
```json
{
    "body": "My pairs would be edges. In an even more ideal world, I would refer to them by their labels. For comparison, if M is a matroid with elements 'e', 'f', 'g', I currently have some experimental code allowing me to write\n\nN = M / ['e'] \\ ['f', 'g']\n\nresulting in the matroid with e contracted and f,g deleted. From a matroid-theoretic point of view, if you contract an edge, all edges parallel to it should turn into loops. The current merge_vertices doesn't do that, even if I call G.allow_loops(True) first. With this behavior, contracting a loop should probably equal deleting a loop.\n\nAnyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.\n\nReal use case: the other day I was wondering about maximal planar subgraphs of a small graph G. In that case you want to explore: first delete edge 'e', then delete edge 'f', then 'f' and 'g', then 'f' and 'h', and finally only edge 'h'. The current implementation makes such exploration of minors a bit cumbersome: you frequently make copies of G, which you then modify.",
    "created_at": "2011-04-11T19:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60824",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

My pairs would be edges. In an even more ideal world, I would refer to them by their labels. For comparison, if M is a matroid with elements 'e', 'f', 'g', I currently have some experimental code allowing me to write

N = M / ['e'] \ ['f', 'g']

resulting in the matroid with e contracted and f,g deleted. From a matroid-theoretic point of view, if you contract an edge, all edges parallel to it should turn into loops. The current merge_vertices doesn't do that, even if I call G.allow_loops(True) first. With this behavior, contracting a loop should probably equal deleting a loop.

Anyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.

Real use case: the other day I was wondering about maximal planar subgraphs of a small graph G. In that case you want to explore: first delete edge 'e', then delete edge 'f', then 'f' and 'g', then 'f' and 'h', and finally only edge 'h'. The current implementation makes such exploration of minors a bit cumbersome: you frequently make copies of G, which you then modify.



---

archive/issue_comments_060825.json:
```json
{
    "body": "> Anyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.\n\n\nWould you be interested in mixing the two ? Like sometimes calling a delete_edge function which returns a graph, and some other times a method which modifies the graph ?\n\nThe current behaviour is necessary for many functions, and replacing it would mean a huge loss in efficiency. It is possible to add a keyword to all those methods so that a graph will be returned instead of modifying the current graph. I don't quite like this, as it would mean some additional tests for each of all those very fundamental functions, but then again...\nOn the other hand, if you are not interested in mixing the two type of operations, perhaps the best is to work on an immutable graph class. Many people have asked this already, and when working on an immutable graph class having a default behaviour of \"returning an immutable copy of the graph modified as requested\" does not seem too unnatural. What about this then ? `:-)`\n\nNathann",
    "created_at": "2011-04-12T19:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60825",
    "user": "https://github.com/nathanncohen"
}
```

> Anyway, my main point is that I feel there should be methods for deletion and contraction that return a new graph, rather than modifying the graph itself.


Would you be interested in mixing the two ? Like sometimes calling a delete_edge function which returns a graph, and some other times a method which modifies the graph ?

The current behaviour is necessary for many functions, and replacing it would mean a huge loss in efficiency. It is possible to add a keyword to all those methods so that a graph will be returned instead of modifying the current graph. I don't quite like this, as it would mean some additional tests for each of all those very fundamental functions, but then again...
On the other hand, if you are not interested in mixing the two type of operations, perhaps the best is to work on an immutable graph class. Many people have asked this already, and when working on an immutable graph class having a default behaviour of "returning an immutable copy of the graph modified as requested" does not seem too unnatural. What about this then ? `:-)`

Nathann



---

archive/issue_comments_060826.json:
```json
{
    "body": "I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.",
    "created_at": "2011-04-19T15:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60826",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.



---

archive/issue_comments_060827.json:
```json
{
    "body": "> I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.\n\n\nGot it !\n\nThis being said, I understand that's how matroid theory is written \"on the paper\", but do you think it would be possible to write useful code using only those symbols when any of them means copying the whole structure ? But perhaps I do not know how you intend to code it, and how much such operations could cost in memory and time ...\n\nNathann",
    "created_at": "2011-04-19T15:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60827",
    "user": "https://github.com/nathanncohen"
}
```

> I'm not at all in favor of having two different behaviors encoded in one function. One option would be to implement the __div__ and _backslash_ operators to do, respectively, contraction and deletion without changing the object.


Got it !

This being said, I understand that's how matroid theory is written "on the paper", but do you think it would be possible to write useful code using only those symbols when any of them means copying the whole structure ? But perhaps I do not know how you intend to code it, and how much such operations could cost in memory and time ...

Nathann



---

archive/issue_comments_060828.json:
```json
{
    "body": "Replying to [comment:20 Stefan]:\n> I'm not at all in favor of having two different behaviors encoded in one function.\n\n\nThis is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.",
    "created_at": "2011-04-19T18:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60828",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:20 Stefan]:
> I'm not at all in favor of having two different behaviors encoded in one function.


This is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.



---

archive/issue_comments_060829.json:
```json
{
    "body": "Replying to [comment:22 rlm]:\n> Replying to [comment:20 Stefan]:\n> > I'm not at all in favor of having two different behaviors encoded in one function.\n\n> \n> This is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.\n\n\nIndeed it does! I'm not sure that this happens often, but so far I found subgraph() and relabel(). The former defaults to inplace=False; the latter defaults to inplace=True.\n\nIn that case it would be preferable not to have extra methods (the list is quite long enough as it stands). Defining the forward and backslashes might still be a neat addition.\n\nNathann, typical work with matroids is on relatively small ground sets. I don't expect intensive calculations on graphs with more than, say, a few dozen edges. We would wrap the graph in a GraphicMatroid object anyway, so it's easy to compensate for any functionality in the graph code that is not entirely fit for our purpose. So you need not worry about our needs for the time being.\n\nWhat remains is the question of contracting one edge from a parallel pair (see above).",
    "created_at": "2011-04-20T07:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60829",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

Replying to [comment:22 rlm]:
> Replying to [comment:20 Stefan]:
> > I'm not at all in favor of having two different behaviors encoded in one function.

> 
> This is often the case. For example many graph functions in Sage have an `inplace` option, which provides exactly this choice.


Indeed it does! I'm not sure that this happens often, but so far I found subgraph() and relabel(). The former defaults to inplace=False; the latter defaults to inplace=True.

In that case it would be preferable not to have extra methods (the list is quite long enough as it stands). Defining the forward and backslashes might still be a neat addition.

Nathann, typical work with matroids is on relatively small ground sets. I don't expect intensive calculations on graphs with more than, say, a few dozen edges. We would wrap the graph in a GraphicMatroid object anyway, so it's easy to compensate for any functionality in the graph code that is not entirely fit for our purpose. So you need not worry about our needs for the time being.

What remains is the question of contracting one edge from a parallel pair (see above).



---

archive/issue_comments_060830.json:
```json
{
    "body": "So, what do you say to my patch? It provides\n\n1. loops handling (see #9807)\n2. ``contract_edge`` option\n3. ``inplace`` option",
    "created_at": "2012-01-31T14:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60830",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

So, what do you say to my patch? It provides

1. loops handling (see #9807)
2. ``contract_edge`` option
3. ``inplace`` option



---

archive/issue_comments_060831.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-31T14:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60831",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060832.json:
```json
{
    "body": "Apply trac_7304_contract_edge.patch\n\n(for patchbot)",
    "created_at": "2012-03-10T13:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60832",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_7304_contract_edge.patch

(for patchbot)



---

archive/issue_comments_060833.json:
```json
{
    "body": "Brunellus,\n\nThis isn't quite there, and you haven't tested everything.\n\nGraphs have a copy method -- `g = g.copy()` is faster than `g=copy(g)`.  There are two problems with the block\n\n```\n        if vertices and vertices[0] is None: \n\t    vertices[0] = g.add_vertex()\n```\n\nfirst off, this assumes that `g.add_vertex()` returns the label of the added vertex.  It does not.  Second, it modifies `vertices` for no good reason (what if the users passes in a tuple, set, or generator?)",
    "created_at": "2012-03-21T20:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60833",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Brunellus,

This isn't quite there, and you haven't tested everything.

Graphs have a copy method -- `g = g.copy()` is faster than `g=copy(g)`.  There are two problems with the block

```
        if vertices and vertices[0] is None: 
	    vertices[0] = g.add_vertex()
```

first off, this assumes that `g.add_vertex()` returns the label of the added vertex.  It does not.  Second, it modifies `vertices` for no good reason (what if the users passes in a tuple, set, or generator?)



---

archive/issue_comments_060834.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-21T21:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60834",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060835.json:
```json
{
    "body": "Ah, I see that g.add_vertex() indeed returns the label for the current alpha of 5.0.  Please update this to not modify the users's input with\n\n```\n    vertices = list(vertices)\n```\n\nand use `g.copy()` instead of copy, and I'll give this a positive review.",
    "created_at": "2012-03-21T22:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60835",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Ah, I see that g.add_vertex() indeed returns the label for the current alpha of 5.0.  Please update this to not modify the users's input with

```
    vertices = list(vertices)
```

and use `g.copy()` instead of copy, and I'll give this a positive review.



---

archive/issue_comments_060836.json:
```json
{
    "body": "Thanks for the review! I will update the patch right now.",
    "created_at": "2012-05-16T09:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60836",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Thanks for the review! I will update the patch right now.



---

archive/issue_comments_060837.json:
```json
{
    "body": "Attachment [trac_7304_contract_edge.patch](tarball://root/attachments/some-uuid/ticket7304/trac_7304_contract_edge.patch) by brunellus created at 2012-05-16 10:34:37",
    "created_at": "2012-05-16T10:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60837",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Attachment [trac_7304_contract_edge.patch](tarball://root/attachments/some-uuid/ticket7304/trac_7304_contract_edge.patch) by brunellus created at 2012-05-16 10:34:37



---

archive/issue_comments_060838.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-16T10:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60838",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060839.json:
```json
{
    "body": "I have been working on getting the Tutte polynomial into Sage (#1314).  The Tutte polynomial needs contraction with keeping any resulting multiedges and loops (but removing the edge you contracted).  It seems your code does this if you allow multiedges and loops and use the contract_edge feature.\n\nI think they may have had this discussion above, but I can't tell what was concluded:  Would adding an option like \"simplegraph = True\" be a reasonable thing to do?",
    "created_at": "2012-07-15T21:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60839",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

I have been working on getting the Tutte polynomial into Sage (#1314).  The Tutte polynomial needs contraction with keeping any resulting multiedges and loops (but removing the edge you contracted).  It seems your code does this if you allow multiedges and loops and use the contract_edge feature.

I think they may have had this discussion above, but I can't tell what was concluded:  Would adding an option like "simplegraph = True" be a reasonable thing to do?



---

archive/issue_comments_060840.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60840",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_060841.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-11-26T10:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60841",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_060842.json:
```json
{
    "body": "Ok.... Which is the patch that needs to be reviewed ? Is it [attachment:trac_7304_contract_edge.patch] ?\n\nNathann",
    "created_at": "2012-11-26T10:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60842",
    "user": "https://github.com/nathanncohen"
}
```

Ok.... Which is the patch that needs to be reviewed ? Is it [attachment:trac_7304_contract_edge.patch] ?

Nathann



---

archive/issue_events_017303.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17303"
}
```



---

archive/issue_events_017304.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17304"
}
```



---

archive/issue_events_017305.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17305"
}
```



---

archive/issue_events_017306.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17306"
}
```



---

archive/issue_events_017307.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17307"
}
```



---

archive/issue_events_017308.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17308"
}
```



---

archive/issue_events_017309.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17309"
}
```



---

archive/issue_events_017310.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17310"
}
```



---

archive/issue_comments_060843.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-06-22T00:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60843",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_060844.json:
```json
{
    "body": "I ended up writing some new methods for edge contraction. I didn't use either patch here. The first one didn't seem to respect edge labels, and `allow_loops_multiedges` seems redundant since these are intrinsic to the graph, and the second one seemed too complicated to disentangle from `merge_vertices`. I also didn't include an `inplace` option for consistency with `delete_edge`.\n\nThe `contract_edges()` method was tough because if the user inputs a list of edges, the vertices need to be updated dynamically as the contractions occur and vertices are lost. I ended up using nested while loops to accomplish this. Maybe there's a faster way?\n\n---\nNew commits:",
    "created_at": "2017-06-22T00:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60844",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

I ended up writing some new methods for edge contraction. I didn't use either patch here. The first one didn't seem to respect edge labels, and `allow_loops_multiedges` seems redundant since these are intrinsic to the graph, and the second one seemed too complicated to disentangle from `merge_vertices`. I also didn't include an `inplace` option for consistency with `delete_edge`.

The `contract_edges()` method was tough because if the user inputs a list of edges, the vertices need to be updated dynamically as the contractions occur and vertices are lost. I ended up using nested while loops to accomplish this. Maybe there's a faster way?

---
New commits:



---

archive/issue_comments_060845.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-22T00:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60845",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060846.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-22T01:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60846",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060847.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-22T01:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60847",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060848.json:
```json
{
    "body": "Let's wait until I speed up `contract_edges()`.",
    "created_at": "2017-06-22T01:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60848",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Let's wait until I speed up `contract_edges()`.



---

archive/issue_comments_060849.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-06-22T01:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60849",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060850.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-22T05:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60850",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060851.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-22T17:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60851",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060852.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-06-22T17:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60852",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060853.json:
```json
{
    "body": "For the sake of not having two implementations for the same thing, I adapted brunellus's earlier patch and rewrote `contract_edge()` to use `merge_vertices()`. This depends on #23290 to resolve a defect in `merge_vertices()`.",
    "created_at": "2017-06-22T17:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60853",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

For the sake of not having two implementations for the same thing, I adapted brunellus's earlier patch and rewrote `contract_edge()` to use `merge_vertices()`. This depends on #23290 to resolve a defect in `merge_vertices()`.



---

archive/issue_comments_060854.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-23T07:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60854",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060855.json:
```json
{
    "body": "Some comments for `contract_edges`:\n* instead of dropping non-edges, it is better to not add such edge to the list\n* construct the list of vertices at the same time to add edges to the list\n* Instead of implementing your own disjoint set methods, you can use `DisjointSet`\n* If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`",
    "created_at": "2017-06-23T08:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60855",
    "user": "https://github.com/dcoudert"
}
```

Some comments for `contract_edges`:
* instead of dropping non-edges, it is better to not add such edge to the list
* construct the list of vertices at the same time to add edges to the list
* Instead of implementing your own disjoint set methods, you can use `DisjointSet`
* If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`



---

archive/issue_comments_060856.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-25T18:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60856",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060857.json:
```json
{
    "body": "Replying to [comment:52 dcoudert]:\n> Some comments for `contract_edges`:\n> * instead of dropping non-edges, it is better to not add such edge to the list\n> * construct the list of vertices at the same time to add edges to the list\n \nDone.\n> * Instead of implementing your own disjoint set methods, you can use `DisjointSet`\n> * If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`\n \nIt's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.",
    "created_at": "2017-06-25T18:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60857",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Replying to [comment:52 dcoudert]:
> Some comments for `contract_edges`:
> * instead of dropping non-edges, it is better to not add such edge to the list
> * construct the list of vertices at the same time to add edges to the list
 
Done.
> * Instead of implementing your own disjoint set methods, you can use `DisjointSet`
> * If you use `DS = DisjointSet(...)`, you can use `DS.root_to_elements_dict()` instead of `vertices = [v for v in vertices if v!= destination[v]]`
 
It's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.



---

archive/issue_comments_060858.json:
```json
{
    "body": "There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.",
    "created_at": "2017-06-25T19:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60858",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.



---

archive/issue_comments_060859.json:
```json
{
    "body": "> It's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.\n\n\n`vertices = [v for v in vertices if v != DS.find(v)]` should give you non-roots, no?",
    "created_at": "2017-06-25T19:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60859",
    "user": "https://github.com/dcoudert"
}
```

> It's nice that sage already has an implementation of this algorithm, but I find it lacking. If I want a list of non-roots, I can do `vertices = [v for v in vertices if (v not in DS.root_to_elements_dict() )]`, but there doesn't seem to be an analog to my `root()` method. So at the end, when I need to know what the root of a vertex is, I don't see any easy way to do that if I'm using `DisjointSet`.


`vertices = [v for v in vertices if v != DS.find(v)]` should give you non-roots, no?



---

archive/issue_comments_060860.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-25T19:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60860",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060861.json:
```json
{
    "body": "Ah, right. I misread the description of that method.",
    "created_at": "2017-06-25T19:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60861",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Ah, right. I misread the description of that method.



---

archive/issue_comments_060862.json:
```json
{
    "body": "Replying to [comment:55 zgershkoff]:\n> There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.\n\n\nThis is the main difficulty with such method: what's the good answer? what is the user expected ? It is really application dependent. For instance, in some cases you want to contract an edge unless it creates a loop.\\\\\nI would say that as long as the behavior is clearly documented, it's fine. If the user wants something else, he can code his own method.\n\n \n\nOne remark. You could use `edges_incident.extend( self.outgoing_edges(v) )` instead of `out_edges=self.edge_boundary([v])`. You can also use `self.incoming_edges(v)`.",
    "created_at": "2017-06-26T06:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60862",
    "user": "https://github.com/dcoudert"
}
```

Replying to [comment:55 zgershkoff]:
> There's another issue I've been considering: if a user has loops on but multiedges off, then iterated contraction with `contract_edge()` will never create loops, but giving the same input as a list to `contract_edges()` could create loops because it will bypass when the edges are in parallel. On one hand, it seems like it should be consistent, but on the other hand, if a user has loops on and multiedges off, I don't know what business they have contracting edges, so I don't know what their desired output would be.


This is the main difficulty with such method: what's the good answer? what is the user expected ? It is really application dependent. For instance, in some cases you want to contract an edge unless it creates a loop.\\
I would say that as long as the behavior is clearly documented, it's fine. If the user wants something else, he can code his own method.

 

One remark. You could use `edges_incident.extend( self.outgoing_edges(v) )` instead of `out_edges=self.edge_boundary([v])`. You can also use `self.incoming_edges(v)`.



---

archive/issue_comments_060863.json:
```json
{
    "body": "Thanks for the comments. I think if I use both `self.incoming_edges(v)` and `self.outgoing_edges(v)` then I will get loops on `v` twice, so I'm leaving `out_edges=self.edge_boundary([v])` as it is, but I will extend `edges_incident` by `self.incoming_edges(v)`.",
    "created_at": "2017-06-26T20:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60863",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Thanks for the comments. I think if I use both `self.incoming_edges(v)` and `self.outgoing_edges(v)` then I will get loops on `v` twice, so I'm leaving `out_edges=self.edge_boundary([v])` as it is, but I will extend `edges_incident` by `self.incoming_edges(v)`.



---

archive/issue_comments_060864.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-26T21:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60864",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060865.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-26T21:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60865",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060866.json:
```json
{
    "body": "Another round of comments. \n\nIn method `contract_edge`\n- in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.\n- remove the `OUTPUT` block. It is useless here\n- If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.\n- you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.\n\nIn method `contract_edges`:\n- The first line is too long. Usually, the first line is short, and followed with a longer description\n- Again the `OUTPUT` block is useless\n- in the `TESTS` block, you have an indentation problem\n- If we pass a list of 2-tuples but that all edges of the graph have non `None` labels, nothing will happen. If it's expected behavior, it should be documented\n- after the `for e in edges:` loop, you should add a termination test like `if not edge_list: return` or `if not edge_list or not vertices: return`\n- `out_edges=self.edge_boundary([v])` -> `out_edges = self.edge_boundary([v])`\n- `edges_incident = edges_incident + self.edges_incident(v)` -> `edges_incident.extend(self.edges_incident(v))`\n- `for (u, v, label) in edges_incident:` -> `for u, v, label in edges_incident:`.",
    "created_at": "2017-06-27T06:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60866",
    "user": "https://github.com/dcoudert"
}
```

Another round of comments. 

In method `contract_edge`
- in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.
- remove the `OUTPUT` block. It is useless here
- If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.
- you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.

In method `contract_edges`:
- The first line is too long. Usually, the first line is short, and followed with a longer description
- Again the `OUTPUT` block is useless
- in the `TESTS` block, you have an indentation problem
- If we pass a list of 2-tuples but that all edges of the graph have non `None` labels, nothing will happen. If it's expected behavior, it should be documented
- after the `for e in edges:` loop, you should add a termination test like `if not edge_list: return` or `if not edge_list or not vertices: return`
- `out_edges=self.edge_boundary([v])` -> `out_edges = self.edge_boundary([v])`
- `edges_incident = edges_incident + self.edges_incident(v)` -> `edges_incident.extend(self.edges_incident(v))`
- `for (u, v, label) in edges_incident:` -> `for u, v, label in edges_incident:`.



---

archive/issue_comments_060867.json:
```json
{
    "body": "Replying to [comment:63 dcoudert]:\n> Another round of comments. \n> \n> In method `contract_edge`\n> - in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.\n> - remove the `OUTPUT` block. It is useless here\n> - If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.\n\n\nI can't reproduce this. `self.has_edge(u,v)` works the same as `self.has_edge(u,v,None)`. It seems though the last edge it has in memory between `u` and `v` gets contracted.\n\n```\nsage: edgelist = [(0,1,0), (0,1,9), (0,1,2), (0,2,2), (1,2,3)]\nsage: G = Graph(edgelist, loops=True, multiedges=True)\nsage: G.contract_edge(0,1); G.edges()\n[(0, 0, 0), (0, 0, 9), (0, 2, 2), (0, 2, 3)]\nsage: edgelist = [(0,1,0), (0,1,2), (0,1,9), (0,2,2), (1,2,3)]\nsage: G = Graph(edgelist, loops=True, multiedges=True)\nsage: G.contract_edge(0,1); G.edges()\n[(0, 0, 0), (0, 0, 2), (0, 2, 2), (0, 2, 3)]\n```\n\n> - you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.\n\n\nI changed it to `x,y,l` for consistency.\n\nWhy is `x,y,l` preferred over `(x,y,l)`? I don't see anything about this in PEP8, but I've been using the parentheses around the tuple a lot because I think it's easier to read that way.",
    "created_at": "2017-06-27T20:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60867",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Replying to [comment:63 dcoudert]:
> Another round of comments. 
> 
> In method `contract_edge`
> - in the `INPUT` block, some lines are for `contract_edges` and so should be removed from here.
> - remove the `OUTPUT` block. It is useless here
> - If I call `G.contract_edge( (u, v) )` and that the graph has edge `(u, v, 'label')`, then the method will do nothing. Is this the behavior you expect? If so, it should be documented.


I can't reproduce this. `self.has_edge(u,v)` works the same as `self.has_edge(u,v,None)`. It seems though the last edge it has in memory between `u` and `v` gets contracted.

```
sage: edgelist = [(0,1,0), (0,1,9), (0,1,2), (0,2,2), (1,2,3)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1); G.edges()
[(0, 0, 0), (0, 0, 9), (0, 2, 2), (0, 2, 3)]
sage: edgelist = [(0,1,0), (0,1,2), (0,1,9), (0,2,2), (1,2,3)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1); G.edges()
[(0, 0, 0), (0, 0, 2), (0, 2, 2), (0, 2, 3)]
```

> - you may replace `for e in self.edges_incident(v):` with `for x,y,l in self.edges_incident(v):`. I don't know which option is the best.


I changed it to `x,y,l` for consistency.

Why is `x,y,l` preferred over `(x,y,l)`? I don't see anything about this in PEP8, but I've been using the parentheses around the tuple a lot because I think it's easier to read that way.



---

archive/issue_comments_060868.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-27T20:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60868",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060869.json:
```json
{
    "body": "I have a few more questions.\n\n- Is `return` preferred over `return None`? I've changed them to just `return`.\n- Where is the indentation error in `contract_edges()`? Is it the space in front of some of the edges in the output? That matches the output, and it makes the html display correctly.\n- I've noticed that there are problems for `contract_edges()` if the input is a mix of 2-tuples and 3-tuples as the example below shows, but this is kind of a GIGO situation and I don't know if I should bother addressing it.\n\n```\nsage: edgelist = [(0,1,0), (0,1,1), (0,1,2)]\nsage: G = Graph(edgelist, loops=True, multiedges=True)\nsage: G.contract_edges([(0,1,2), (0,1)]); G.edges()\n[(0, 0, 0)]\nsage: G = Graph(edgelist, loops=True, multiedges=True)\nsage: G.contract_edges([(0,1), (0,1,2)]); G.edges()\n[(0, 0, 0), (0, 0, 1)]\n```",
    "created_at": "2017-06-27T20:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60869",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

I have a few more questions.

- Is `return` preferred over `return None`? I've changed them to just `return`.
- Where is the indentation error in `contract_edges()`? Is it the space in front of some of the edges in the output? That matches the output, and it makes the html display correctly.
- I've noticed that there are problems for `contract_edges()` if the input is a mix of 2-tuples and 3-tuples as the example below shows, but this is kind of a GIGO situation and I don't know if I should bother addressing it.

```
sage: edgelist = [(0,1,0), (0,1,1), (0,1,2)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edges([(0,1,2), (0,1)]); G.edges()
[(0, 0, 0)]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edges([(0,1), (0,1,2)]); G.edges()
[(0, 0, 0), (0, 0, 1)]
```



---

archive/issue_comments_060870.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-27T21:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60870",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060871.json:
```json
{
    "body": "Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why\n\n```\nsage: edgelist = [(0,0,'a'), (0,1,'b'), (1,1,'c')]\nsage: G = Graph(edgelist, loops=True, multiedges=True)\nsage: G.contract_edge(0,1,'b'); G.edges()\n[(0, 0, 'a')]\nsage: D = DiGraph(edgelist, loops=True, multiedges=True)\nsage: D.contract_edge(0,1,'b'); D.edges()\n[(0, 0, 'a')]\n```\n\nIn `contract_edges`:\n*`if not edges:` -> `if not edge_list:`\n* indentation of tests `With loops in a digraph::`",
    "created_at": "2017-06-28T07:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60871",
    "user": "https://github.com/dcoudert"
}
```

Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why

```
sage: edgelist = [(0,0,'a'), (0,1,'b'), (1,1,'c')]
sage: G = Graph(edgelist, loops=True, multiedges=True)
sage: G.contract_edge(0,1,'b'); G.edges()
[(0, 0, 'a')]
sage: D = DiGraph(edgelist, loops=True, multiedges=True)
sage: D.contract_edge(0,1,'b'); D.edges()
[(0, 0, 'a')]
```

In `contract_edges`:
*`if not edges:` -> `if not edge_list:`
* indentation of tests `With loops in a digraph::`



---

archive/issue_comments_060872.json:
```json
{
    "body": "Replying to [comment:68 dcoudert]:\n> Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why\n\n\nI think I put those tests in before I rewrote `contract_edge` to use `merge_vertices`. Maybe it's irrelevant to have those tests there now. Now that uses `merge_vertices`, it's dependent on #23290 to keep the loops. I should have been clearer about that, sorry.\n\n> In `contract_edges`:\n> *`if not edges:` -> `if not edge_list:`\n> * indentation of tests `With loops in a digraph::`\n\n\nYes, I see it now. I'll fix those shortly.",
    "created_at": "2017-06-28T07:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60872",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Replying to [comment:68 dcoudert]:
> Something has changed in the tests for method `contract_edge`. Now we are loosing loops. I don't know why


I think I put those tests in before I rewrote `contract_edge` to use `merge_vertices`. Maybe it's irrelevant to have those tests there now. Now that uses `merge_vertices`, it's dependent on #23290 to keep the loops. I should have been clearer about that, sorry.

> In `contract_edges`:
> *`if not edges:` -> `if not edge_list:`
> * indentation of tests `With loops in a digraph::`


Yes, I see it now. I'll fix those shortly.



---

archive/issue_comments_060873.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-28T17:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60873",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060874.json:
```json
{
    "body": "I took the liberty of moving #23290 into this since it's closed. All tests pass now.",
    "created_at": "2017-06-28T18:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60874",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

I took the liberty of moving #23290 into this since it's closed. All tests pass now.



---

archive/issue_comments_060875.json:
```json
{
    "body": "Right, better to rebase on top of #23290.\n\nIn method `contract_edge`, I suggest the following change. Do you agree ?\n\n```\n       if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):\n           # add loops\n           for (x, y, l) in self.edges_incident(v):\n               if set([x, y]) == set([u, v]):\n                   self.add_edge(u, u, l)\n```\n\nIn method `contract_edges`\n- the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)\n- `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.",
    "created_at": "2017-06-28T20:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60875",
    "user": "https://github.com/dcoudert"
}
```

Right, better to rebase on top of #23290.

In method `contract_edge`, I suggest the following change. Do you agree ?

```
       if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):
           # add loops
           for (x, y, l) in self.edges_incident(v):
               if set([x, y]) == set([u, v]):
                   self.add_edge(u, u, l)
```

In method `contract_edges`
- the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)
- `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.



---

archive/issue_comments_060876.json:
```json
{
    "body": "Replying to [comment:72 dcoudert]:\n> Right, better to rebase on top of #23290.\n> \n> In method `contract_edge`, I suggest the following change. Do you agree ?\n> \n> ```\n>        if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):\n>            # add loops\n>            for (x, y, l) in self.edges_incident(v):\n>                if set([x, y]) == set([u, v]):\n>                    self.add_edge(u, u, l)\n> ```\n\nI think sage will fail silently if multiedges are off, but it makes sense in principle to check first. I changed the order of the tests because I figured checking a boolean with `self.allows_multiple_edges()` is probably faster than looking for an edge.\n> In method `contract_edges`\n> - the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)\n> - `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.\n \nThat also makes sense.",
    "created_at": "2017-06-28T20:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60876",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Replying to [comment:72 dcoudert]:
> Right, better to rebase on top of #23290.
> 
> In method `contract_edge`, I suggest the following change. Do you agree ?
> 
> ```
>        if self.allows_loops() and (not self.has_edge(u, u) or self.allows_multiple_edges()):
>            # add loops
>            for (x, y, l) in self.edges_incident(v):
>                if set([x, y]) == set([u, v]):
>                    self.add_edge(u, u, l)
> ```

I think sage will fail silently if multiedges are off, but it makes sense in principle to check first. I changed the order of the tests because I figured checking a boolean with `self.allows_multiple_edges()` is probably faster than looking for an edge.
> In method `contract_edges`
> - the test `if len(set([len(e) for e in edges])) > 1:` is fun ;)
> - `if self.has_edge((u, v, label)):` -> `if self.has_edge(u, v, label):`. This is to avoid guessing the format in method `has_edge`.
 
That also makes sense.



---

archive/issue_comments_060877.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-28T20:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60877",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060878.json:
```json
{
    "body": "It occurs to me that in `contract_edge`, loops will never be created unless there are already multiedges. Thus we only need to check if multiedges are allowed once when adding loops.",
    "created_at": "2017-06-29T04:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60878",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

It occurs to me that in `contract_edge`, loops will never be created unless there are already multiedges. Thus we only need to check if multiedges are allowed once when adding loops.



---

archive/issue_comments_060879.json:
```json
{
    "body": "Nevermind. A digraph can have two arcs in different directions between a pair of vertices and still have multiedges disabled, so contraction can create a loop. I suppose it's better like it is, since if there's already a loop at `u`, it will always be kept with its original label now.",
    "created_at": "2017-06-29T04:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60879",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Nevermind. A digraph can have two arcs in different directions between a pair of vertices and still have multiedges disabled, so contraction can create a loop. I suppose it's better like it is, since if there's already a loop at `u`, it will always be kept with its original label now.



---

archive/issue_comments_060880.json:
```json
{
    "body": "The patch looks good to me, but I'm wondering if we have taken all cases into account (functionality and/or tests)",
    "created_at": "2017-06-29T11:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60880",
    "user": "https://github.com/dcoudert"
}
```

The patch looks good to me, but I'm wondering if we have taken all cases into account (functionality and/or tests)



---

archive/issue_comments_060881.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-29T23:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60881",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060882.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-29T23:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60882",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_017311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/zgershkoff",
    "created_at": "2017-06-29T23:36:15Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17311"
}
```



---

archive/issue_events_017312.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/zgershkoff",
    "created_at": "2017-06-29T23:36:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17312"
}
```



---

archive/issue_comments_060883.json:
```json
{
    "body": "I added tests for labeled edges, and for attempting to contract non-edges. I think that covers it.",
    "created_at": "2017-06-29T23:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60883",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

I added tests for labeled edges, and for attempting to contract non-edges. I think that covers it.



---

archive/issue_comments_060884.json:
```json
{
    "body": "Final comments (sorry for that).\n\nFor method `contract_edge`:\n- at the top of the `generic_graph.py` file, could you ensure that the description of `contract_edge` is the same as in the method. I propose to put: `Contract an edge from `u` to `v``. Note that I use `Contract` and not `Contracts`.\n- Then in the method, split the first line to `Contract an edge from `u` to `v`` and then have a next paragraph with `This method returns silently if the edge does not exist.`\n\nFor method `contract_edges`:\n- at the top of the `generic_graph.py` file, for `contract_edges`: use `Contract` instead of `Contracts`\n- improve the alignment of paragraph `If `e` is an edge that is...`\n- In the `INPUT` block, `- ``edges`` - a list...` -> `- ``edges`` -- a list...`. You will certainly have to put the last word (edges) on the next line to be in 80 columns format.\n- In the `TESTS:` block, just before `With loops in a digraph::`, remove the empty `::` block. I was not able to build the documentation and it took me a while to understand that it was caused by this `::` stuff.\n- I'm not sure the empty line `....:` is useful. You can remove it.\n\nI hope it's the last round of corrections ;)",
    "created_at": "2017-07-01T19:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60884",
    "user": "https://github.com/dcoudert"
}
```

Final comments (sorry for that).

For method `contract_edge`:
- at the top of the `generic_graph.py` file, could you ensure that the description of `contract_edge` is the same as in the method. I propose to put: `Contract an edge from `u` to `v``. Note that I use `Contract` and not `Contracts`.
- Then in the method, split the first line to `Contract an edge from `u` to `v`` and then have a next paragraph with `This method returns silently if the edge does not exist.`

For method `contract_edges`:
- at the top of the `generic_graph.py` file, for `contract_edges`: use `Contract` instead of `Contracts`
- improve the alignment of paragraph `If `e` is an edge that is...`
- In the `INPUT` block, `- ``edges`` - a list...` -> `- ``edges`` -- a list...`. You will certainly have to put the last word (edges) on the next line to be in 80 columns format.
- In the `TESTS:` block, just before `With loops in a digraph::`, remove the empty `::` block. I was not able to build the documentation and it took me a while to understand that it was caused by this `::` stuff.
- I'm not sure the empty line `....:` is useful. You can remove it.

I hope it's the last round of corrections ;)



---

archive/issue_comments_060885.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-02T23:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60885",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060886.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-02T23:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60886",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060887.json:
```json
{
    "body": "Done. Thanks for walking me through it.",
    "created_at": "2017-07-02T23:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60887",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Done. Thanks for walking me through it.



---

archive/issue_comments_060888.json:
```json
{
    "body": "You have used `from 'u' to 'v'` with `'` instead of ```. I think that ``` is more appropriate. It is nicer in the documentation and it avoids confusion with string.\n\nYou have to do the correction both at the top of the file and at the beginning of `contract_edge`.\n\nAfter that you can set the ticket to positive review (or I will do it later).\n\nBest,",
    "created_at": "2017-07-02T23:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60888",
    "user": "https://github.com/dcoudert"
}
```

You have used `from 'u' to 'v'` with `'` instead of ```. I think that ``` is more appropriate. It is nicer in the documentation and it avoids confusion with string.

You have to do the correction both at the top of the file and at the beginning of `contract_edge`.

After that you can set the ticket to positive review (or I will do it later).

Best,



---

archive/issue_comments_060889.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-07-03T00:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60889",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060890.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-07-03T00:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60890",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060891.json:
```json
{
    "body": "I can't personally verify that the documentation builds correctly (perhaps an error with the beta I have installed), but doctests pass, so I'll take your word for it. Thanks for the review.",
    "created_at": "2017-07-03T00:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60891",
    "user": "https://trac.sagemath.org/admin/accounts/users/zgershkoff"
}
```

I can't personally verify that the documentation builds correctly (perhaps an error with the beta I have installed), but doctests pass, so I'll take your word for it. Thanks for the review.



---

archive/issue_comments_060892.json:
```json
{
    "body": "I checked and the documentation looks good. So we are done.",
    "created_at": "2017-07-03T03:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60892",
    "user": "https://github.com/dcoudert"
}
```

I checked and the documentation looks good. So we are done.



---

archive/issue_comments_060893.json:
```json
{
    "body": "If you depend on a pre-git ticket then the release script will never figure out that the dependencies are merged FYI",
    "created_at": "2017-08-14T22:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60893",
    "user": "https://github.com/vbraun"
}
```

If you depend on a pre-git ticket then the release script will never figure out that the dependencies are merged FYI



---

archive/issue_comments_060894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-08-16T18:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7304#issuecomment-60894",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_017313.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-08-16T18:46:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7304#event-17313"
}
```
