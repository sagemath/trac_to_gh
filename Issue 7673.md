# Issue 7673: implement Dijkstra's algorithm for C graphs

archive/issues_007673.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ncohen\n\nAs a follow up of #7640.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7673\n\n",
    "created_at": "2009-12-12T19:51:21Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "implement Dijkstra's algorithm for C graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7673",
    "user": "rlm"
}
```
Assignee: rlm

CC:  ncohen

As a follow up of #7640.

Issue created by migration from https://trac.sagemath.org/ticket/7673





---

archive/issue_comments_065759.json:
```json
{
    "body": "To write it I could need an implementation of heaps in Cython ( I would need top keep a list sorted through the execution of the algorithm, with insertion/deletions ). If anybody knows about such a thing, please tell me :-)",
    "created_at": "2009-12-12T21:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65759",
    "user": "ncohen"
}
```

To write it I could need an implementation of heaps in Cython ( I would need top keep a list sorted through the execution of the algorithm, with insertion/deletions ). If anybody knows about such a thing, please tell me :-)



---

archive/issue_comments_065760.json:
```json
{
    "body": "I think these are implemented in \nhttp://trac.sagemath.org/sage_trac/attachment/ticket/6452/trac_6452-ring-codes.patch\nHowever, the patch was rejected due to memory errors. The author has not fixed them\nyet.\n\nPlease be my guest:-)",
    "created_at": "2009-12-12T22:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65760",
    "user": "wdj"
}
```

I think these are implemented in 
http://trac.sagemath.org/sage_trac/attachment/ticket/6452/trac_6452-ring-codes.patch
However, the patch was rejected due to memory errors. The author has not fixed them
yet.

Please be my guest:-)



---

archive/issue_comments_065761.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-13T13:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65761",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065762.json:
```json
{
    "body": "Here is one version using heapq from Python.... Once we will have a good Cython implementation of heaps, it will take something like 20 seconds to update it ! :-)",
    "created_at": "2009-12-13T13:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65762",
    "user": "ncohen"
}
```

Here is one version using heapq from Python.... Once we will have a good Cython implementation of heaps, it will take something like 20 seconds to update it ! :-)



---

archive/issue_comments_065763.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-14T02:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65763",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065764.json:
```json
{
    "body": "This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?",
    "created_at": "2009-12-14T02:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65764",
    "user": "rlm"
}
```

This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?



---

archive/issue_comments_065765.json:
```json
{
    "body": "rebased on 4.3.rc0 + #7640",
    "created_at": "2009-12-14T02:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65765",
    "user": "rlm"
}
```

rebased on 4.3.rc0 + #7640



---

archive/issue_comments_065766.json:
```json
{
    "body": "Attachment [trac_7673.patch](tarball://root/attachments/some-uuid/ticket7673/trac_7673.patch) by rlm created at 2009-12-14 02:54:06\n\nReplying to [comment:4 rlm]:\n> This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?\n\nOK, I've posted a new patch.",
    "created_at": "2009-12-14T02:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65766",
    "user": "rlm"
}
```

Attachment [trac_7673.patch](tarball://root/attachments/some-uuid/ticket7673/trac_7673.patch) by rlm created at 2009-12-14 02:54:06

Replying to [comment:4 rlm]:
> This is going to conflict with the patch at #7640. Can you rebase this patch on 4.3.rc0 + #7640?

OK, I've posted a new patch.



---

archive/issue_comments_065767.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T02:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65767",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065768.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-14T03:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65768",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065769.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-14T09:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65769",
    "user": "ylchapuy"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065770.json:
```json
{
    "body": "Hi,\nI'm sorry, but this implementation is buggy...\n\n```\nsage: G = Graph()\nsage: G.add_edge(0,1,9)\nsage: G.add_edge(0,2,8)\nsage: G.add_edge(1,2,7)\nsage: G.shortest_path(0,1,by_weight=True)\n[0, 1]\nsage: G.shortest_path_length(0,1,by_weight=True)\n9\nsage: Gc = G.copy(implementation='c_graph')\nsage: Gc.shortest_path(0,1,by_weight=True)\n[0, 2, 1]\nsage: Gc.shortest_path_length(0,1,by_weight=True)\n15\n```\n",
    "created_at": "2009-12-14T09:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65770",
    "user": "ylchapuy"
}
```

Hi,
I'm sorry, but this implementation is buggy...

```
sage: G = Graph()
sage: G.add_edge(0,1,9)
sage: G.add_edge(0,2,8)
sage: G.add_edge(1,2,7)
sage: G.shortest_path(0,1,by_weight=True)
[0, 1]
sage: G.shortest_path_length(0,1,by_weight=True)
9
sage: Gc = G.copy(implementation='c_graph')
sage: Gc.shortest_path(0,1,by_weight=True)
[0, 2, 1]
sage: Gc.shortest_path_length(0,1,by_weight=True)
15
```




---

archive/issue_comments_065771.json:
```json
{
    "body": "Clearly, it is !! Thank you for taking a lot at it :-)\n\nWell, the only bugfix I can think about is to keep in memory the vertex v such that dist_y[v] + dist_x[v] is minimal, and only build the path when the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have been explored. It clearly fixes your counter-example, and I think it should solve all others, but I woud be glad to write a nicer solution... Any idea ? :-)\n\nThank you very much again ! :-)\n\nNathann",
    "created_at": "2009-12-14T11:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65771",
    "user": "ncohen"
}
```

Clearly, it is !! Thank you for taking a lot at it :-)

Well, the only bugfix I can think about is to keep in memory the vertex v such that dist_y[v] + dist_x[v] is minimal, and only build the path when the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have been explored. It clearly fixes your counter-example, and I think it should solve all others, but I woud be glad to write a nicer solution... Any idea ? :-)

Thank you very much again ! :-)

Nathann



---

archive/issue_comments_065772.json:
```json
{
    "body": "I don't know if it's nicer, but did you look at how it's done in networkx? \n\nReplying to [comment:9 ncohen]:\n> I woud be glad to write a nicer solution... Any idea ? :-)",
    "created_at": "2009-12-14T11:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65772",
    "user": "ylchapuy"
}
```

I don't know if it's nicer, but did you look at how it's done in networkx? 

Replying to [comment:9 ncohen]:
> I woud be glad to write a nicer solution... Any idea ? :-)



---

archive/issue_comments_065773.json:
```json
{
    "body": "Replying to [comment:9 ncohen]:\n> Clearly, it is !! Thank you for taking a lot at it :-)\n> \n> Well, the only bugfix I can think about is to keep in memory the vertex v such \n> that dist_y[v] + dist_x[v] is minimal, and only build the path when \n> the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have \n> been explored. It clearly fixes your counter-example, and I think it \n\n\nMaybe this is related to the \"piority queue\" in Demaine's descrition\nof the algorithm in\n\n\n```\nhttp://ocw.mit.edu/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/651C0FC9-55D1-4404-A801-A9D0392A668C/0/lec17.pdf\n```\n\nat\n\n```\nhttp://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/VideoLectures/detail/embed17.htm\n```\n\n\n\n> should solve all others, but I woud be glad to write a nicer solution... \n> Any idea ? :-)\n> \n> Thank you very much again ! :-)\n> \n> Nathann",
    "created_at": "2009-12-14T12:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65773",
    "user": "wdj"
}
```

Replying to [comment:9 ncohen]:
> Clearly, it is !! Thank you for taking a lot at it :-)
> 
> Well, the only bugfix I can think about is to keep in memory the vertex v such 
> that dist_y[v] + dist_x[v] is minimal, and only build the path when 
> the neighborhoods of x and y at distance 2*(dist_y[v] + dist_x[v]) have 
> been explored. It clearly fixes your counter-example, and I think it 


Maybe this is related to the "piority queue" in Demaine's descrition
of the algorithm in


```
http://ocw.mit.edu/NR/rdonlyres/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/651C0FC9-55D1-4404-A801-A9D0392A668C/0/lec17.pdf
```

at

```
http://ocw.mit.edu/OcwWeb/Electrical-Engineering-and-Computer-Science/6-046JFall-2005/VideoLectures/detail/embed17.htm
```



> should solve all others, but I woud be glad to write a nicer solution... 
> Any idea ? :-)
> 
> Thank you very much again ! :-)
> 
> Nathann



---

archive/issue_comments_065774.json:
```json
{
    "body": "Here is a fixed version :-)",
    "created_at": "2009-12-14T12:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65774",
    "user": "ncohen"
}
```

Here is a fixed version :-)



---

archive/issue_comments_065775.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T12:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65775",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065776.json:
```json
{
    "body": "Attachment [trac_7673.2.patch](tarball://root/attachments/some-uuid/ticket7673/trac_7673.2.patch) by ncohen created at 2009-12-14 12:33:00\n\nI do not think so, this bug just came from the fact that this version of dijkstra is bidirectional, and I wrongly assumed that as in the simple version of it, the first path found was the correct path. Obviously ( see your example ) it is not, and I expect this version of the algorithm to be correct :-)\n\nNathann",
    "created_at": "2009-12-14T12:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65776",
    "user": "ncohen"
}
```

Attachment [trac_7673.2.patch](tarball://root/attachments/some-uuid/ticket7673/trac_7673.2.patch) by ncohen created at 2009-12-14 12:33:00

I do not think so, this bug just came from the fact that this version of dijkstra is bidirectional, and I wrongly assumed that as in the simple version of it, the first path found was the correct path. Obviously ( see your example ) it is not, and I expect this version of the algorithm to be correct :-)

Nathann



---

archive/issue_comments_065777.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-14T21:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65777",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065778.json:
```json
{
    "body": "Sorry I missed that mistake! :o\n\nThe new patch looks good.",
    "created_at": "2009-12-14T21:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65778",
    "user": "rlm"
}
```

Sorry I missed that mistake! :o

The new patch looks good.



---

archive/issue_comments_065779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-15T16:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7673#issuecomment-65779",
    "user": "mhansen"
}
```

Resolution: fixed
