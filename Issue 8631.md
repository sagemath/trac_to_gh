# Issue 8631: Make a graph-input interact control

archive/issues_008631.json:
```json
{
    "body": "Assignee: @itolkov\n\nCC:  rkirov @williamstein kevinc\n\nKeywords: graph editor\n\nShould be able to use the graph editor as an input widget for interacts.  \n\nPreliminary proposal on sage-devel:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/f5b850969340bc37/\n\nCurrent state of graph editor:  #8222\n\nIssue created by migration from https://trac.sagemath.org/ticket/8631\n\n",
    "created_at": "2010-03-30T14:54:01Z",
    "labels": [
        "component: interact"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make a graph-input interact control",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8631",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @itolkov

CC:  rkirov @williamstein kevinc

Keywords: graph editor

Should be able to use the graph editor as an input widget for interacts.  

Preliminary proposal on sage-devel:
http://groups.google.com/group/sage-devel/browse_thread/thread/f5b850969340bc37/

Current state of graph editor:  #8222

Issue created by migration from https://trac.sagemath.org/ticket/8631





---

archive/issue_comments_078129.json:
```json
{
    "body": "Good idea.  If we do this, we might want to also have an interact control that gives a nice interactive way of choosing a graph from the family of all graphs. This would be what graphs.[tab] gives, but more graphical.\n\nI wonder if interact controls should be rewritten to somehow be as easy to make as `@`interact's themselves?  It would cool to abstract out the whole idea of interact controls so that users could just make them on the fly.",
    "created_at": "2010-03-30T17:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78129",
    "user": "https://github.com/williamstein"
}
```

Good idea.  If we do this, we might want to also have an interact control that gives a nice interactive way of choosing a graph from the family of all graphs. This would be what graphs.[tab] gives, but more graphical.

I wonder if interact controls should be rewritten to somehow be as easy to make as `@`interact's themselves?  It would cool to abstract out the whole idea of interact controls so that users could just make them on the fly.



---

archive/issue_comments_078130.json:
```json
{
    "body": "Similarly to what Rob tried. I opened interact.py and started editing (this is probably the longest .py file I ever worked with).\n\nSo far I can make the virtual interact and it can try to start the embedded graph editor. But i run into a weird thing where my injected graph data gets transformed as follows all \" , \" -> \" ,=\"\" \".\n\nAnyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.",
    "created_at": "2010-04-12T00:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78130",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Similarly to what Rob tried. I opened interact.py and started editing (this is probably the longest .py file I ever worked with).

So far I can make the virtual interact and it can try to start the embedded graph editor. But i run into a weird thing where my injected graph data gets transformed as follows all " , " -> " ,="" ".

Anyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.



---

archive/issue_comments_078131.json:
```json
{
    "body": "Replying to [comment:2 rkirov]:\n> Anyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.\n\nDefinitely.  I'll try to recover what I worked up before and post it here in the next couple days.  My work on this got a bit jumbled, which stopped me a few days ago on a final review of the editor itself at #8222.  \n\nSo I'll tackle both of these in one shot.\n\nRob",
    "created_at": "2010-04-12T00:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78131",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 rkirov]:
> Anyways, if anybody else is working on this, we should exchange some patches even if they are very incomplete.

Definitely.  I'll try to recover what I worked up before and post it here in the next couple days.  My work on this got a bit jumbled, which stopped me a few days ago on a final review of the editor itself at #8222.  

So I'll tackle both of these in one shot.

Rob



---

archive/issue_comments_078132.json:
```json
{
    "body": "Attachment [8631.sagenb.patch](tarball://root/attachments/some-uuid/ticket8631/8631.sagenb.patch) by rkirov created at 2010-04-29 02:20:36\n\npatch for sagenb - depends on #8222",
    "created_at": "2010-04-29T02:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78132",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Attachment [8631.sagenb.patch](tarball://root/attachments/some-uuid/ticket8631/8631.sagenb.patch) by rkirov created at 2010-04-29 02:20:36

patch for sagenb - depends on #8222



---

archive/issue_comments_078133.json:
```json
{
    "body": "Attachment [8631.sage.patch](tarball://root/attachments/some-uuid/ticket8631/8631.sage.patch) by rkirov created at 2010-04-29 02:30:57\n\ntiny sage patch to avoid a circular import",
    "created_at": "2010-04-29T02:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78133",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Attachment [8631.sage.patch](tarball://root/attachments/some-uuid/ticket8631/8631.sage.patch) by rkirov created at 2010-04-29 02:30:57

tiny sage patch to avoid a circular import



---

archive/issue_comments_078134.json:
```json
{
    "body": "the graph interact is ready. The patches depends on the newest graph_editor which is #8222.\n\nNeeds work because i haven't done doctests and haven't decided how to incorporate the overlapping code with the graph_editor into one js graph library (right now i just copied it into a new file graph_interact.js and modified).\n\nIn any case it is working for anyone who wants to see how eigenvalues or chromatic numbers change dynamically (as you throw in or throw out vertices and edges). Enjoy!",
    "created_at": "2010-04-29T02:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78134",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

the graph interact is ready. The patches depends on the newest graph_editor which is #8222.

Needs work because i haven't done doctests and haven't decided how to incorporate the overlapping code with the graph_editor into one js graph library (right now i just copied it into a new file graph_interact.js and modified).

In any case it is working for anyone who wants to see how eigenvalues or chromatic numbers change dynamically (as you throw in or throw out vertices and edges). Enjoy!



---

archive/issue_comments_078135.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-29T02:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78135",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_078136.json:
```json
{
    "body": "Rado,\n\nVery nice!  This works for me - I'll upload a screenshot next.\n\nFor anybody else testing, you just need a line like\n\n`G=Graph(...)`\n\nin the argument list of the function you are using as the interact.  It seems that you need to specify the initial graph as something other than a null graph, and whatever this graph might be, the routine expects to find position information.  \n\nNice work!\n\nRob",
    "created_at": "2010-04-29T05:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78136",
    "user": "https://github.com/rbeezer"
}
```

Rado,

Very nice!  This works for me - I'll upload a screenshot next.

For anybody else testing, you just need a line like

`G=Graph(...)`

in the argument list of the function you are using as the interact.  It seems that you need to specify the initial graph as something other than a null graph, and whatever this graph might be, the routine expects to find position information.  

Nice work!

Rob



---

archive/issue_comments_078137.json:
```json
{
    "body": "Screenshot of graph editor interact control",
    "created_at": "2010-04-29T05:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78137",
    "user": "https://github.com/rbeezer"
}
```

Screenshot of graph editor interact control



---

archive/issue_comments_078138.json:
```json
{
    "body": "Attachment [graph-interact.png](tarball://root/attachments/some-uuid/ticket8631/graph-interact.png) by @jasongrout created at 2010-04-30 01:09:36\n\nNice!\n\nIt looks like in the patch that there is a huge section of code that is commented out that should be just deleted.",
    "created_at": "2010-04-30T01:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78138",
    "user": "https://github.com/jasongrout"
}
```

Attachment [graph-interact.png](tarball://root/attachments/some-uuid/ticket8631/graph-interact.png) by @jasongrout created at 2010-04-30 01:09:36

Nice!

It looks like in the patch that there is a huge section of code that is commented out that should be just deleted.



---

archive/issue_comments_078139.json:
```json
{
    "body": "#30540 has made a graph editor available",
    "created_at": "2022-04-03T18:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78139",
    "user": "https://github.com/mkoeppe"
}
```

#30540 has made a graph editor available



---

archive/issue_comments_078140.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-04-03T18:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78140",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078141.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-04-25T07:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78141",
    "user": "https://github.com/jfraymond"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078142.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-05-11T02:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8631#issuecomment-78142",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_008800.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-05-11T02:14:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8631",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8631#event-8800"
}
```
