# Issue 4505: Boyer's planarity code mishandles graphs with no edges

archive/issues_004505.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ekirkman bober\n\nWe get random segfaults from the planarity code because it doesn't seem to handle graphs with no edges properly.\n\nThe segfaults occur in these lines from sage/graphs/planarity/graphEmbed.c\n\n\n```\n        Jfirst = theGraph->G[I].link[1];\n\n        if (theGraph->G[Jfirst].type == EDGE_FORWARD)\n        {\n\n            /* Find the end of the forward edge list */\n\n            Jnext = Jfirst;\n            while (theGraph->G[Jnext].type == EDGE_FORWARD)\n```\n\n\nThe problem is that when there are no edges, theGraph->G[I].link[1] is -1, Jfirst is -1.  If the random value at theGraph->G[-1].type is 2 (EDGE_FORWARD), then the code in the if block is executed and we get a segfault when trying to access fields inside the if block.\n\nFor now, this patch skirts the issue by checking for the case of no edges explicitly before Boyer's code is called.\n\nI am emailing John Boyer about this as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4505\n\n",
    "created_at": "2008-11-13T00:47:11Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Boyer's planarity code mishandles graphs with no edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4505",
    "user": "jason"
}
```
Assignee: rlm

CC:  ekirkman bober

We get random segfaults from the planarity code because it doesn't seem to handle graphs with no edges properly.

The segfaults occur in these lines from sage/graphs/planarity/graphEmbed.c


```
        Jfirst = theGraph->G[I].link[1];

        if (theGraph->G[Jfirst].type == EDGE_FORWARD)
        {

            /* Find the end of the forward edge list */

            Jnext = Jfirst;
            while (theGraph->G[Jnext].type == EDGE_FORWARD)
```


The problem is that when there are no edges, theGraph->G[I].link[1] is -1, Jfirst is -1.  If the random value at theGraph->G[-1].type is 2 (EDGE_FORWARD), then the code in the if block is executed and we get a segfault when trying to access fields inside the if block.

For now, this patch skirts the issue by checking for the case of no edges explicitly before Boyer's code is called.

I am emailing John Boyer about this as well.

Issue created by migration from https://trac.sagemath.org/ticket/4505





---

archive/issue_comments_033405.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-13T01:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4505#issuecomment-33405",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_033406.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-13T03:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4505#issuecomment-33406",
    "user": "jason"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_033407.json:
```json
{
    "body": "Positive review assuming this passes doctests:\n\n```\n[7:24pm] mabshoff|afk: Is a graph without edges planar?\n[7:24pm] jason--: yep!\n[7:24pm] mabshoff|afk: In that case you would get a positive review \n[7:24pm] jason--: you can easily draw it with no edges crossing\n[7:24pm] jason--: thanks, that was fast too.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T03:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4505#issuecomment-33407",
    "user": "mabshoff"
}
```

Positive review assuming this passes doctests:

```
[7:24pm] mabshoff|afk: Is a graph without edges planar?
[7:24pm] jason--: yep!
[7:24pm] mabshoff|afk: In that case you would get a positive review 
[7:24pm] jason--: you can easily draw it with no edges crossing
[7:24pm] jason--: thanks, that was fast too.
```

Cheers,

Michael



---

archive/issue_comments_033408.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-13T04:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4505#issuecomment-33408",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_comments_033409.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-13T04:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4505#issuecomment-33409",
    "user": "mabshoff"
}
```

Resolution: fixed
