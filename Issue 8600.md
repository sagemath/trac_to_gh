# Issue 8600: fibonacci tree

archive/issues_008600.json:
```json
{
    "body": "Assignee: rlm\n\nthe fibonacci tree, [wikipedia](http://de.wikipedia.org/wiki/Datei:Fibonacci_Tree_5.svg)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8600\n\n",
    "created_at": "2010-03-24T17:46:29Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "fibonacci tree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8600",
    "user": "schilly"
}
```
Assignee: rlm

the fibonacci tree, [wikipedia](http://de.wikipedia.org/wiki/Datei:Fibonacci_Tree_5.svg)

Issue created by migration from https://trac.sagemath.org/ticket/8600





---

archive/issue_comments_077881.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-24T20:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77881",
    "user": "schilly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077882.json:
```json
{
    "body": "I find the placement of the nodes strange (and even more if the tree is big).\n\nI would prefer an implementation using Fibonacci numbers all over the construction:\n\n\n```\ndef FibonacciTree(n):\n    T = Graph(name=\"Fibonacci-Tree-%d\"%n)\n    if n==1: T.add_vertex(0)\n    if n<2: return T\n\n    F = list(fibonacci_sequence(n + 2))\n    s = 2.0 ** (n / 2.0 - 2)\n    pos = {}\n\n    def fib(level, node, y):\n        pos[node] = (node, y)\n        if level < 2: return\n        level -= 1\n        y -= s\n        diff = F[level]\n        T.add_edge(node, node-diff)\n        if level == 1: # only one child\n            pos[node - diff] = (node, y)\n            return\n        T.add_edge(node, node + diff)\n        fib(level, node - diff, y)\n        fib(level - 1, node + diff, y)\n\n    T.add_vertices(xrange(sum(F[:-1])))\n    fib(n, F[n + 1] - 1, 0)\n    T.set_pos(pos)\n\n    return T\n```\n\n\nbut maybe it's just a matter of taste.\n\nWith `n=7` you obtain the same graph as http://www.delorie.com/gnu/docs/avl/avlmuchbal.png .\nNotice that the name of each node is also it's x-coordinate (except for the only children where I prefer to put them under their father).",
    "created_at": "2010-03-25T17:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77882",
    "user": "ylchapuy"
}
```

I find the placement of the nodes strange (and even more if the tree is big).

I would prefer an implementation using Fibonacci numbers all over the construction:


```
def FibonacciTree(n):
    T = Graph(name="Fibonacci-Tree-%d"%n)
    if n==1: T.add_vertex(0)
    if n<2: return T

    F = list(fibonacci_sequence(n + 2))
    s = 2.0 ** (n / 2.0 - 2)
    pos = {}

    def fib(level, node, y):
        pos[node] = (node, y)
        if level < 2: return
        level -= 1
        y -= s
        diff = F[level]
        T.add_edge(node, node-diff)
        if level == 1: # only one child
            pos[node - diff] = (node, y)
            return
        T.add_edge(node, node + diff)
        fib(level, node - diff, y)
        fib(level - 1, node + diff, y)

    T.add_vertices(xrange(sum(F[:-1])))
    fib(n, F[n + 1] - 1, 0)
    T.set_pos(pos)

    return T
```


but maybe it's just a matter of taste.

With `n=7` you obtain the same graph as http://www.delorie.com/gnu/docs/avl/avlmuchbal.png .
Notice that the name of each node is also it's x-coordinate (except for the only children where I prefer to put them under their father).



---

archive/issue_comments_077883.json:
```json
{
    "body": "Thanks for your example and quick response, I like it! I've modified it a bit, added your name and made some changes so that it fits into the sage library.",
    "created_at": "2010-03-25T18:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77883",
    "user": "schilly"
}
```

Thanks for your example and quick response, I like it! I've modified it a bit, added your name and made some changes so that it fits into the sage library.



---

archive/issue_comments_077884.json:
```json
{
    "body": "Attachment [fibonaccy-graph.patch](tarball://root/attachments/some-uuid/ticket8600/fibonaccy-graph.patch) by schilly created at 2010-03-25 18:41:28",
    "created_at": "2010-03-25T18:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77884",
    "user": "schilly"
}
```

Attachment [fibonaccy-graph.patch](tarball://root/attachments/some-uuid/ticket8600/fibonaccy-graph.patch) by schilly created at 2010-03-25 18:41:28



---

archive/issue_comments_077885.json:
```json
{
    "body": "I like it too, and the golden_ratio is indeed well suited. I would give it a positive review, but I'm not sure if I can anymore as it's mainly my code.",
    "created_at": "2010-03-25T19:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77885",
    "user": "ylchapuy"
}
```

I like it too, and the golden_ratio is indeed well suited. I would give it a positive review, but I'm not sure if I can anymore as it's mainly my code.



---

archive/issue_comments_077886.json:
```json
{
    "body": "Replying to [comment:4 ylchapuy]:\n> I would give it a positive review...\n\ngood! now we just need a third party.",
    "created_at": "2010-03-25T19:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77886",
    "user": "schilly"
}
```

Replying to [comment:4 ylchapuy]:
> I would give it a positive review...

good! now we just need a third party.



---

archive/issue_comments_077887.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-25T20:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77887",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077888.json:
```json
{
    "body": "Is there a reason that the milestone for this is version 5.0 rather than 4.4?  Should we try to merge it in 4.4?",
    "created_at": "2010-04-15T04:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77888",
    "user": "jhpalmieri"
}
```

Is there a reason that the milestone for this is version 5.0 rather than 4.4?  Should we try to merge it in 4.4?



---

archive/issue_comments_077889.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Is there a reason that the milestone for this is version 5.0 rather than 4.4? \n\nNo, I think there was no 4.4 when i created it, that's all. It's really trivial and just a small addition.",
    "created_at": "2010-04-15T08:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77889",
    "user": "schilly"
}
```

Replying to [comment:7 jhpalmieri]:
> Is there a reason that the milestone for this is version 5.0 rather than 4.4? 

No, I think there was no 4.4 when i created it, that's all. It's really trivial and just a small addition.



---

archive/issue_comments_077890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77890",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_077891.json:
```json
{
    "body": "Merged \"fibonaccy-graph.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8600#issuecomment-77891",
    "user": "jhpalmieri"
}
```

Merged "fibonaccy-graph.patch" in 4.4.alpha0
