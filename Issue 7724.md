# Issue 7724: breadth/depth first search for c_graphs

archive/issues_007724.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nSome improvement on this side, and so for ther functions like connected components, strongly connected components, etc...\n\n\n```\nsage: g= graphs.RandomGNP(1000,.01)\nsage: h=g.copy(implementation=\"c_graph\")\nsage: timeit(\"list(g.depth_first_search(0))\")\n25 loops, best of 3: 10.9 ms per loop\nsage: timeit(\"list(h.depth_first_search(0))\")\n125 loops, best of 3: 2.03 ms per loop\n```\n\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7724\n\n",
    "created_at": "2009-12-17T17:46:37Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "breadth/depth first search for c_graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7724",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  rlm

Some improvement on this side, and so for ther functions like connected components, strongly connected components, etc...


```
sage: g= graphs.RandomGNP(1000,.01)
sage: h=g.copy(implementation="c_graph")
sage: timeit("list(g.depth_first_search(0))")
25 loops, best of 3: 10.9 ms per loop
sage: timeit("list(h.depth_first_search(0))")
125 loops, best of 3: 2.03 ms per loop
```


Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7724





---

archive/issue_comments_066355.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T14:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66355",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066356.json:
```json
{
    "body": "( small bug fixed : I had forgotten bitset_set_first_n which was quite problematic in a few cases :-) )",
    "created_at": "2009-12-18T15:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66356",
    "user": "ncohen"
}
```

( small bug fixed : I had forgotten bitset_set_first_n which was quite problematic in a few cases :-) )



---

archive/issue_comments_066357.json:
```json
{
    "body": "There's a merging conflict:\n\n```\n-        ALGORITHM: 8.3.8 in [1]. Notice that the termination condition on \n-        line (23) of the algorithm uses \"p[v] == 0\" which in the book \n-        means that the parent is undefined; in this case, v must be the \n+        ALGORITHM: 8.3.8 in [Jungnickel2005]_. Notice that the termination \n+        condition on line (23) of the algorithm uses \"p[v] == 0\" which in\n+        the book means that the parent is undefined; in this case, v must be the \n         root s.  Since our vertex names start with 0, we substitute instead\n         the condition \"v == s\".  This is the terminating condition used \n         in the general Depth First Search tree in Algorithm 8.2.1.\n         \n         REFERENCE:\n \n-        - [1] D. Jungnickel, Graphs, Networks and Algorithms,\n+        .. [Jungnickel2005] D. Jungnickel, Graphs, Networks and Algorithms,\n```\n\n\nThis change already made it into 4.3.rc1, I believe, in #7314. Can you rebase on top of that patch?",
    "created_at": "2009-12-18T22:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66357",
    "user": "rlm"
}
```

There's a merging conflict:

```
-        ALGORITHM: 8.3.8 in [1]. Notice that the termination condition on 
-        line (23) of the algorithm uses "p[v] == 0" which in the book 
-        means that the parent is undefined; in this case, v must be the 
+        ALGORITHM: 8.3.8 in [Jungnickel2005]_. Notice that the termination 
+        condition on line (23) of the algorithm uses "p[v] == 0" which in
+        the book means that the parent is undefined; in this case, v must be the 
         root s.  Since our vertex names start with 0, we substitute instead
         the condition "v == s".  This is the terminating condition used 
         in the general Depth First Search tree in Algorithm 8.2.1.
         
         REFERENCE:
 
-        - [1] D. Jungnickel, Graphs, Networks and Algorithms,
+        .. [Jungnickel2005] D. Jungnickel, Graphs, Networks and Algorithms,
```


This change already made it into 4.3.rc1, I believe, in #7314. Can you rebase on top of that patch?



---

archive/issue_comments_066358.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-18T22:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66358",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066359.json:
```json
{
    "body": "I'm not at home and won't be able to do it today... I should be able to produce it tomorrow morning though :-)",
    "created_at": "2009-12-19T08:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66359",
    "user": "ncohen"
}
```

I'm not at home and won't be able to do it today... I should be able to produce it tomorrow morning though :-)



---

archive/issue_comments_066360.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-20T16:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66360",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066361.json:
```json
{
    "body": "Hello !!\n\nI could not reproduce your merging conflict, though as I had applied the patch I use the occasion to add a few other things... You will find in this new version of the patch\n\n* A function beadth_dirst_search ( with optional arguments ``reverse`` and ``ignore_direction``\n* A function ``depth_first_search`` with the same paremeters\n* A function ``is_connected``\n* A function ``is_strongly_connected``\n* I needed to know inside the graph backend whether the graph was directed or not : I thought for some time about it, and ended up adding to the constructors of ``Graph`` and ``DiGraph`` a line ``self._backend.directed = True/False`` according to the situation.\n* I also modified graph.py so that it would use the functions defined in c_graph whenever possible, and NetworkX otherwise\n\nAnd with this, we should be another step closer.. :-)\n\nNathann",
    "created_at": "2009-12-20T16:35:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66361",
    "user": "ncohen"
}
```

Hello !!

I could not reproduce your merging conflict, though as I had applied the patch I use the occasion to add a few other things... You will find in this new version of the patch

* A function beadth_dirst_search ( with optional arguments ``reverse`` and ``ignore_direction``
* A function ``depth_first_search`` with the same paremeters
* A function ``is_connected``
* A function ``is_strongly_connected``
* I needed to know inside the graph backend whether the graph was directed or not : I thought for some time about it, and ended up adding to the constructors of ``Graph`` and ``DiGraph`` a line ``self._backend.directed = True/False`` according to the situation.
* I also modified graph.py so that it would use the functions defined in c_graph whenever possible, and NetworkX otherwise

And with this, we should be another step closer.. :-)

Nathann



---

archive/issue_comments_066362.json:
```json
{
    "body": "The actual breadth/depth_first_search are generator objects but your new ones are plain lists. Is it a design choice?",
    "created_at": "2009-12-21T00:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66362",
    "user": "ylchapuy"
}
```

The actual breadth/depth_first_search are generator objects but your new ones are plain lists. Is it a design choice?



---

archive/issue_comments_066363.json:
```json
{
    "body": "There is no \"yield\" command available at the moment in Cython... :-)",
    "created_at": "2009-12-21T06:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66363",
    "user": "ncohen"
}
```

There is no "yield" command available at the moment in Cython... :-)



---

archive/issue_comments_066364.json:
```json
{
    "body": "Now using bitset_first to find a vertex in the graph :-)\n\nNathann",
    "created_at": "2009-12-21T07:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66364",
    "user": "ncohen"
}
```

Now using bitset_first to find a vertex in the graph :-)

Nathann



---

archive/issue_comments_066365.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> There is no \"yield\" command available at the moment in Cython... :-)\n\nBut you can still define a iterator class.\n\nThe following patch is based on your work, and defines an iterator. You can choose which one you prefer.",
    "created_at": "2009-12-21T11:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66365",
    "user": "ylchapuy"
}
```

Replying to [comment:7 ncohen]:
> There is no "yield" command available at the moment in Cython... :-)

But you can still define a iterator class.

The following patch is based on your work, and defines an iterator. You can choose which one you prefer.



---

archive/issue_comments_066366.json:
```json
{
    "body": "Well, actually until now Robert Miller just typed : return iter(value)) which was good too... If you prefer to return an iterator instead of alist, perhaps this would be better :-)",
    "created_at": "2009-12-21T11:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66366",
    "user": "ncohen"
}
```

Well, actually until now Robert Miller just typed : return iter(value)) which was good too... If you prefer to return an iterator instead of alist, perhaps this would be better :-)



---

archive/issue_comments_066367.json:
```json
{
    "body": "The way I did it, I don't copy the data, the big list doesn't exist, this can be an advantage. But I let you do the choice, I won't use big graphs anyway.",
    "created_at": "2009-12-21T11:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66367",
    "user": "ylchapuy"
}
```

The way I did it, I don't copy the data, the big list doesn't exist, this can be an advantage. But I let you do the choice, I won't use big graphs anyway.



---

archive/issue_comments_066368.json:
```json
{
    "body": "Well, my view was that if just waiting can prevent us from writing lines of codes that could be replaced by a \"yield\" once it will be available, why not ? :-)\n\nLet's see what Robert thinks about it if he is finally reviewing this ticket .. And thank you again for your help ! :-)\n\nNathann",
    "created_at": "2009-12-21T11:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66368",
    "user": "ncohen"
}
```

Well, my view was that if just waiting can prevent us from writing lines of codes that could be replaced by a "yield" once it will be available, why not ? :-)

Let's see what Robert thinks about it if he is finally reviewing this ticket .. And thank you again for your help ! :-)

Nathann



---

archive/issue_comments_066369.json:
```json
{
    "body": "slight update:\nuse extend instead of append improves performance",
    "created_at": "2009-12-21T15:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66369",
    "user": "ylchapuy"
}
```

slight update:
use extend instead of append improves performance



---

archive/issue_comments_066370.json:
```json
{
    "body": "Attachment [trac_7724_iterator-rebased.patch](tarball://root/attachments/some-uuid/ticket7724/trac_7724_iterator-rebased.patch) by rlm created at 2010-01-02 16:01:11",
    "created_at": "2010-01-02T16:01:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66370",
    "user": "rlm"
}
```

Attachment [trac_7724_iterator-rebased.patch](tarball://root/attachments/some-uuid/ticket7724/trac_7724_iterator-rebased.patch) by rlm created at 2010-01-02 16:01:11



---

archive/issue_comments_066371.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-02T16:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66371",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066372.json:
```json
{
    "body": "1. The iterator patch is preferable, since there are actual speed gains when a loop is terminated early. I've rebased the patch against sage-4.3.\n\n2. There is some confusion as to the function `get_vertex`. This should go from Python objects to ints, and in several places it is used the other way around. The function `vertex_label` will go from int to Python object, and I've switched these in the appropriate places (see `trac_7724-ref.patch`). I've also added an example where the vertex labels aren't integers.\n\n3. I've tested this with #7634 applied, and everything looks good with the fixes mentioned above.",
    "created_at": "2010-01-02T16:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66372",
    "user": "rlm"
}
```

1. The iterator patch is preferable, since there are actual speed gains when a loop is terminated early. I've rebased the patch against sage-4.3.

2. There is some confusion as to the function `get_vertex`. This should go from Python objects to ints, and in several places it is used the other way around. The function `vertex_label` will go from int to Python object, and I've switched these in the appropriate places (see `trac_7724-ref.patch`). I've also added an example where the vertex labels aren't integers.

3. I've tested this with #7634 applied, and everything looks good with the fixes mentioned above.



---

archive/issue_comments_066373.json:
```json
{
    "body": "Attachment [trac_7724-ref.patch](tarball://root/attachments/some-uuid/ticket7724/trac_7724-ref.patch) by rlm created at 2010-01-02 16:18:40",
    "created_at": "2010-01-02T16:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66373",
    "user": "rlm"
}
```

Attachment [trac_7724-ref.patch](tarball://root/attachments/some-uuid/ticket7724/trac_7724-ref.patch) by rlm created at 2010-01-02 16:18:40



---

archive/issue_comments_066374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7724#issuecomment-66374",
    "user": "mhansen"
}
```

Resolution: fixed
