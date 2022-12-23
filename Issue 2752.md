# Issue 2752: Speedup for  all_paths()

archive/issues_002752.json:
```json
{
    "body": "Assignee: rlm\n\nI speeded up the *all_paths()* function for graphs.\n\nThe improvement is mainly based on 'getting rid of the recursion' :-)\n\n\nOn my machine (Pentium M) it's about 5 times faster, without more memory consumption.\n\n-vgermrk-\n\nIssue created by migration from https://trac.sagemath.org/ticket/2752\n\n",
    "created_at": "2008-04-01T13:42:54Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "Speedup for  all_paths()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2752",
    "user": "vgermrk"
}
```
Assignee: rlm

I speeded up the *all_paths()* function for graphs.

The improvement is mainly based on 'getting rid of the recursion' :-)


On my machine (Pentium M) it's about 5 times faster, without more memory consumption.

-vgermrk-

Issue created by migration from https://trac.sagemath.org/ticket/2752





---

archive/issue_comments_018901.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-01T13:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18901",
    "user": "vgermrk"
}
```

Attachment



---

archive/issue_comments_018902.json:
```json
{
    "body": "This looks nice and despite vgermrk mentioning in IRC that the patch introduced more complicated code I think that it is fine [and not too complicated], especially since it removes paths_helper(). I am not sure if we really want to remove that code.\n\nrlm: can you poke take a look? It would also be nice to see some figures of before and after with various graphs. Bonus points if someone  also measured memory consumption before and after.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T14:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18902",
    "user": "mabshoff"
}
```

This looks nice and despite vgermrk mentioning in IRC that the patch introduced more complicated code I think that it is fine [and not too complicated], especially since it removes paths_helper(). I am not sure if we really want to remove that code.

rlm: can you poke take a look? It would also be nice to see some figures of before and after with various graphs. Bonus points if someone  also measured memory consumption before and after.

Cheers,

Michael



---

archive/issue_comments_018903.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-04-02T00:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18903",
    "user": "rlm"
}
```

Changing priority from minor to major.



---

archive/issue_comments_018904.json:
```json
{
    "body": "The code looks good.  Very dense graphs on a small dumber of vertices see a major slowdown with this patch, although performance in the sparse case looks good.\n\nBefore:\n\n```\n  Order\\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000\n     3         0.0000029 0.0000027 0.0000030 0.0000035 0.0000044 0.0000057\n     4         0.0000024 0.0000027 0.0000030 0.0000041 0.0000063 0.0000121\n     5         0.0000023 0.0000028 0.0000034 0.0000053 0.0000084 0.0000257\n     6         0.0000024 0.0000031 0.0000036 0.0000073 0.0000134 0.0000551\n     7         0.0000023 0.0000030 0.0000044 0.0000114 0.0000295 0.0001854\n     8         0.0000023 0.0000033 0.0000056 0.0000151 0.0000718 0.0007517\n     9         0.0000023 0.0000035 0.0000068 0.0000229 0.0001821 0.0026202\n```\n\n\nAfter:\n\n```\n  Order\\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000\n     3         0.0000044 0.0000044 0.0000046 0.0000052 0.0000056 0.0000064\n     4         0.0000041 0.0000044 0.0000048 0.0000057 0.0000070 0.0000100\n     5         0.0000040 0.0000046 0.0000053 0.0000071 0.0000098 0.0000183\n     6         0.0000040 0.0000047 0.0000056 0.0000100 0.0000136 0.0000386\n     7         0.0000039 0.0000049 0.0000065 0.0000118 0.0000241 0.0001069\n     8         0.0000040 0.0000048 0.0000073 0.0000173 0.0000491 0.0003567\n     9         0.0000039 0.0000053 0.0000089 0.0000252 0.0001272 0.0014974\n```\n\n\nTimings for larger, sparser graphs might be on their way.",
    "created_at": "2008-04-02T00:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18904",
    "user": "rlm"
}
```

The code looks good.  Very dense graphs on a small dumber of vertices see a major slowdown with this patch, although performance in the sparse case looks good.

Before:

```
  Order\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000
     3         0.0000029 0.0000027 0.0000030 0.0000035 0.0000044 0.0000057
     4         0.0000024 0.0000027 0.0000030 0.0000041 0.0000063 0.0000121
     5         0.0000023 0.0000028 0.0000034 0.0000053 0.0000084 0.0000257
     6         0.0000024 0.0000031 0.0000036 0.0000073 0.0000134 0.0000551
     7         0.0000023 0.0000030 0.0000044 0.0000114 0.0000295 0.0001854
     8         0.0000023 0.0000033 0.0000056 0.0000151 0.0000718 0.0007517
     9         0.0000023 0.0000035 0.0000068 0.0000229 0.0001821 0.0026202
```


After:

```
  Order\Density0.0100000 0.0500000 0.1000000 0.2000000 0.3000000 0.5000000
     3         0.0000044 0.0000044 0.0000046 0.0000052 0.0000056 0.0000064
     4         0.0000041 0.0000044 0.0000048 0.0000057 0.0000070 0.0000100
     5         0.0000040 0.0000046 0.0000053 0.0000071 0.0000098 0.0000183
     6         0.0000040 0.0000047 0.0000056 0.0000100 0.0000136 0.0000386
     7         0.0000039 0.0000049 0.0000065 0.0000118 0.0000241 0.0001069
     8         0.0000040 0.0000048 0.0000073 0.0000173 0.0000491 0.0003567
     9         0.0000039 0.0000053 0.0000089 0.0000252 0.0001272 0.0014974
```


Timings for larger, sparser graphs might be on their way.



---

archive/issue_comments_018905.json:
```json
{
    "body": "Sorry, the comment about dense small graphs didn't get deleted before going to press - obviously not true :-)",
    "created_at": "2008-04-02T00:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18905",
    "user": "rlm"
}
```

Sorry, the comment about dense small graphs didn't get deleted before going to press - obviously not true :-)



---

archive/issue_comments_018906.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-02T00:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18906",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_018907.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-02T01:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18907",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018908.json:
```json
{
    "body": "Merged all_paths_speedup.patch in Sage 3.0.alpha0. All doctests pass with this patch applied.",
    "created_at": "2008-04-02T01:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2752#issuecomment-18908",
    "user": "mabshoff"
}
```

Merged all_paths_speedup.patch in Sage 3.0.alpha0. All doctests pass with this patch applied.
