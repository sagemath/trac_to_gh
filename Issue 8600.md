# Issue 8600: fibonacci tree

Issue created by migration from https://trac.sagemath.org/ticket/8600

Original creator: schilly

Original creation time: 2010-03-24 17:46:29

Assignee: rlm

the fibonacci tree, [wikipedia](http://de.wikipedia.org/wiki/Datei:Fibonacci_Tree_5.svg)


---

Comment by schilly created at 2010-03-24 20:13:02

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-03-25 17:52:57

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

Comment by schilly created at 2010-03-25 18:40:58

Thanks for your example and quick response, I like it! I've modified it a bit, added your name and made some changes so that it fits into the sage library.


---

Attachment


---

Comment by ylchapuy created at 2010-03-25 19:30:44

I like it too, and the golden_ratio is indeed well suited. I would give it a positive review, but I'm not sure if I can anymore as it's mainly my code.


---

Comment by schilly created at 2010-03-25 19:58:26

Replying to [comment:4 ylchapuy]:
> I would give it a positive review...

good! now we just need a third party.


---

Comment by rlm created at 2010-03-25 20:08:58

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 04:31:45

Is there a reason that the milestone for this is version 5.0 rather than 4.4?  Should we try to merge it in 4.4?


---

Comment by schilly created at 2010-04-15 08:57:42

Replying to [comment:7 jhpalmieri]:
> Is there a reason that the milestone for this is version 5.0 rather than 4.4? 

No, I think there was no 4.4 when i created it, that's all. It's really trivial and just a small addition.


---

Comment by jhpalmieri created at 2010-04-16 18:51:42

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:51:42

Merged "fibonaccy-graph.patch" in 4.4.alpha0
