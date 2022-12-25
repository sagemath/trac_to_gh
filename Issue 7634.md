# Issue 7634: switch default Sage graphs over to c_graph, and split up graph.py and graph_generators.py

archive/issues_007634.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen mvngu @williamstein @robertwb @jasongrout\n\nThis is currently under discussion here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5\n\nI realized that it's probably actually time to switch over, since there are a few other developers working on Sage graphs besides just me now. That way if anything slows down, we are likely to find it out pretty quickly, and get it fixed. And, with the new defaults, things already feel more speedy:\n\nBEFORE:\n\n```\nsage -t  \"devel/sage-main/sage/graphs/graph.py\"             \n [113.1 s]\n```\nAFTER:\n\n```\nsage -t  \"devel/sage-main/sage/graphs/graph.py\"             \n [78.5 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7634\n\n",
    "closed_at": "2010-01-13T04:35:52Z",
    "created_at": "2009-12-09T02:07:02Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "switch default Sage graphs over to c_graph, and split up graph.py and graph_generators.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7634",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

CC:  @nathanncohen mvngu @williamstein @robertwb @jasongrout

This is currently under discussion here:

http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5

I realized that it's probably actually time to switch over, since there are a few other developers working on Sage graphs besides just me now. That way if anything slows down, we are likely to find it out pretty quickly, and get it fixed. And, with the new defaults, things already feel more speedy:

BEFORE:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
 [113.1 s]
```
AFTER:

```
sage -t  "devel/sage-main/sage/graphs/graph.py"             
 [78.5 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/7634





---

archive/issue_comments_065110.json:
```json
{
    "body": "Hmmm... When applying your patch here is what I get :\n\n```\n~/sage/sage-A/sage/graphs$ sage -t graph.py \nsage -t  \"devel/sage-A/sage/graphs/graph.py\"                \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [360.5 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage-A/sage/graphs/graph.py\"\nTotal time for all tests: 360.5 seconds\n```\nI know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? \n\nNathann",
    "created_at": "2009-12-09T10:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65110",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm... When applying your patch here is what I get :

```
~/sage/sage-A/sage/graphs$ sage -t graph.py 
sage -t  "devel/sage-A/sage/graphs/graph.py"                
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [360.5 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-A/sage/graphs/graph.py"
Total time for all tests: 360.5 seconds
```
I know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? 

Nathann



---

archive/issue_comments_065111.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-12-09T10:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65111",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_065112.json:
```json
{
    "body": "Hmmm, it seems to come from the docstring \n\n```\nG = graphs.CubeGraph(8)\nH = G.distance_graph([1,3,5,7])\n```\n\nWhich is *very* long !",
    "created_at": "2009-12-09T11:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65112",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm, it seems to come from the docstring 

```
G = graphs.CubeGraph(8)
H = G.distance_graph([1,3,5,7])
```

Which is *very* long !



---

archive/issue_comments_065113.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> \n> ---\n> The following tests failed:\n> \n> \n>         sage -t  \"devel/sage-A/sage/graphs/graph.py\"\n> Total time for all tests: 360.5 seconds\n> }}}\n> I know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? \n\n\nI would try this :)\n\n```\nsage -t -verbose graph.py\n```",
    "created_at": "2009-12-09T11:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65113",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:2 ncohen]:
> 
> ---
> The following tests failed:
> 
> 
>         sage -t  "devel/sage-A/sage/graphs/graph.py"
> Total time for all tests: 360.5 seconds
> }}}
> I know that this could not give you much information, but I do not know of any way to make -t more verbose... any idea ? 


I would try this :)

```
sage -t -verbose graph.py
```



---

archive/issue_comments_065114.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2009-12-09T11:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65114",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_065115.json:
```json
{
    "body": "Yes, I found it... So stupid of not having checked :-)\n\nBy the way, the problem indeed comes from this distance_graph doctest !\n\nNathann",
    "created_at": "2009-12-09T11:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65115",
    "user": "https://github.com/nathanncohen"
}
```

Yes, I found it... So stupid of not having checked :-)

By the way, the problem indeed comes from this distance_graph doctest !

Nathann



---

archive/issue_comments_065116.json:
```json
{
    "body": "This is because `distance_graph` ultimately relies on `shortest_path`, which uses the networkx graphs. In other words, for each pair of vertices `distance_graphs` calls `shortest_path`, which creates a copy of the graph, calls a NetworkX distance function on it, and discards it. I have created a separate ticket for this issue at #7640.",
    "created_at": "2009-12-09T17:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65116",
    "user": "https://github.com/rlmill"
}
```

This is because `distance_graph` ultimately relies on `shortest_path`, which uses the networkx graphs. In other words, for each pair of vertices `distance_graphs` calls `shortest_path`, which creates a copy of the graph, calls a NetworkX distance function on it, and discards it. I have created a separate ticket for this issue at #7640.



---

archive/issue_comments_065117.json:
```json
{
    "body": "I guess it should be somewhere on the ticket that #7651 should be taken care of first, also.",
    "created_at": "2009-12-10T17:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65117",
    "user": "https://github.com/rlmill"
}
```

I guess it should be somewhere on the ticket that #7651 should be taken care of first, also.



---

archive/issue_comments_065118.json:
```json
{
    "body": "With the patch from #7640, it gives :\n\nBEFORE:\n\n```\nG = graphs.CubeGraph(8)\nsage: time a=G.distance_graph([1,3,5,7])\nCPU times: user 8.15 s, sys: 0.03 s, total: 8.17 s\nWall time: 8.18 s\n```\n\nAFTER:\n\n```\nG = graphs.CubeGraph(8)\nsage: time a=G.distance_graph([1,3,5,7])\nCPU times: user 6.51 s, sys: 0.03 s, total: 6.55 s\nWall time: 6.56 s\n```",
    "created_at": "2009-12-12T18:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65118",
    "user": "https://github.com/nathanncohen"
}
```

With the patch from #7640, it gives :

BEFORE:

```
G = graphs.CubeGraph(8)
sage: time a=G.distance_graph([1,3,5,7])
CPU times: user 8.15 s, sys: 0.03 s, total: 8.17 s
Wall time: 8.18 s
```

AFTER:

```
G = graphs.CubeGraph(8)
sage: time a=G.distance_graph([1,3,5,7])
CPU times: user 6.51 s, sys: 0.03 s, total: 6.55 s
Wall time: 6.56 s
```



---

archive/issue_comments_065119.json:
```json
{
    "body": "Also need to be closed first: #7671 and #7672",
    "created_at": "2009-12-12T19:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65119",
    "user": "https://github.com/rlmill"
}
```

Also need to be closed first: #7671 and #7672



---

archive/issue_comments_065120.json:
```json
{
    "body": "Add #7673 to the list.",
    "created_at": "2009-12-12T20:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65120",
    "user": "https://github.com/rlmill"
}
```

Add #7673 to the list.



---

archive/issue_comments_065121.json:
```json
{
    "body": "sorry, jason, i accidentally removed you from the cc block (not sure what happened there)",
    "created_at": "2009-12-12T20:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65121",
    "user": "https://github.com/rlmill"
}
```

sorry, jason, i accidentally removed you from the cc block (not sure what happened there)



---

archive/issue_comments_065122.json:
```json
{
    "body": "The current patch does not split up graph.py, but the final version will...",
    "created_at": "2009-12-15T18:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65122",
    "user": "https://github.com/rlmill"
}
```

The current patch does not split up graph.py, but the final version will...



---

archive/issue_comments_065123.json:
```json
{
    "body": "Attachment [trac_7634-switchover.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-switchover.patch) by @rlmill created at 2010-01-06 07:25:14\n\ndepends on 4.3.1.alpha1",
    "created_at": "2010-01-06T07:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65123",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7634-switchover.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-switchover.patch) by @rlmill created at 2010-01-06 07:25:14

depends on 4.3.1.alpha1



---

archive/issue_comments_065124.json:
```json
{
    "body": "depends on trac_7634-switchover.patch",
    "created_at": "2010-01-06T07:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65124",
    "user": "https://github.com/rlmill"
}
```

depends on trac_7634-switchover.patch



---

archive/issue_comments_065125.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T07:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65125",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065126.json:
```json
{
    "body": "Attachment [trac_7634-refactor.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-refactor.patch) by @rlmill created at 2010-01-06 07:26:31",
    "created_at": "2010-01-06T07:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65126",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7634-refactor.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-refactor.patch) by @rlmill created at 2010-01-06 07:26:31



---

archive/issue_comments_065127.json:
```json
{
    "body": "Oh boy.  I spent some time yesterday and today adding a few functions and cleaning up some documentation to graph.py. Well, you beat me to being ready, so I guess I'll rebase my patch on top of this one, hoping it gets into 4.3.1 so my patch on top of it can get in too.",
    "created_at": "2010-01-06T07:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65127",
    "user": "https://github.com/jasongrout"
}
```

Oh boy.  I spent some time yesterday and today adding a few functions and cleaning up some documentation to graph.py. Well, you beat me to being ready, so I guess I'll rebase my patch on top of this one, hoping it gets into 4.3.1 so my patch on top of it can get in too.



---

archive/issue_comments_065128.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T09:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65128",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065129.json:
```json
{
    "body": "Well, this one does its jobs, and *finally* splits the graph.py file. c_graphs are now the default ones in Sage, and this patch renames what has to be. \n\nPositive review/Good work/Excellent news !\n\nNathann",
    "created_at": "2010-01-06T09:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65129",
    "user": "https://github.com/nathanncohen"
}
```

Well, this one does its jobs, and *finally* splits the graph.py file. c_graphs are now the default ones in Sage, and this patch renames what has to be. 

Positive review/Good work/Excellent news !

Nathann



---

archive/issue_comments_065130.json:
```json
{
    "body": "based on trac_7634-refactor.patch",
    "created_at": "2010-01-06T14:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65130",
    "user": "https://github.com/rlmill"
}
```

based on trac_7634-refactor.patch



---

archive/issue_comments_065131.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T04:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65131",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_065132.json:
```json
{
    "body": "Attachment [trac_7634-fix-pickle.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-fix-pickle.patch) by @rlmill created at 2010-01-13 04:35:52",
    "created_at": "2010-01-13T04:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7634#issuecomment-65132",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7634-fix-pickle.patch](tarball://root/attachments/some-uuid/ticket7634/trac_7634-fix-pickle.patch) by @rlmill created at 2010-01-13 04:35:52



---

archive/issue_events_018153.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T04:35:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7634",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7634#event-18153"
}
```
