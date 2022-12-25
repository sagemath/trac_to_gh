# Issue 8288: Depth/Breadth improvement for SearchForest

archive/issues_008288.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat @nthiery\n\nKeywords: enumeration depth breadth forest children\n\nThe goal of this patch is to include breadth enumeration method for SearchForest...\n\nThe interested is for enumerated Set defined by a set of roots and a children function. For a finite set of roots but infinite set (infinite depth of the tree), the breadth method is a necessity.\n\nThe breadth method is also a need to define properly indices of infinite Graded algebra (but finite degree by degree). The patch contains method returning iterator of all element of given depth.\n\nUsing extra argument : father and next_brother method, it is possible to enumerate not starting from the roots of trees. a _iter_from_to method build an iterator keeping nothing in memory than the first and the last point.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8288\n\n",
    "created_at": "2010-02-16T22:17:26Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "Depth/Breadth improvement for SearchForest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8288",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: sage-combinat

CC:  sage-combinat @nthiery

Keywords: enumeration depth breadth forest children

The goal of this patch is to include breadth enumeration method for SearchForest...

The interested is for enumerated Set defined by a set of roots and a children function. For a finite set of roots but infinite set (infinite depth of the tree), the breadth method is a necessity.

The breadth method is also a need to define properly indices of infinite Graded algebra (but finite degree by degree). The patch contains method returning iterator of all element of given depth.

Using extra argument : father and next_brother method, it is possible to enumerate not starting from the roots of trees. a _iter_from_to method build an iterator keeping nothing in memory than the first and the last point.

Issue created by migration from https://trac.sagemath.org/ticket/8288





---

archive/issue_comments_073261.json:
```json
{
    "body": "One more time, my english is still bad... Feel free to point <my langage mistakes> and thus, make my english increasing....",
    "created_at": "2010-02-16T22:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73261",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

One more time, my english is still bad... Feel free to point <my langage mistakes> and thus, make my english increasing....



---

archive/issue_comments_073262.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T22:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73262",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073263.json:
```json
{
    "body": "Hello !! I know nothing about the file sage/combinat/backtrack.py, and I intend to read it as soon as possible but I saw on TRAC the same of this patch, and I was convinced it woukd be using the Graph library : in sage/graphs/base/c_graph.pyx are written iterators for depth/breadth-first-search in general graphs.. Wouldn't it be better for this class to use such functions, are they are written in Cython and should be more efficient ? Or directly use the Graph structure, as it would automatically call these functions.. :-)\n\nNathann",
    "created_at": "2010-02-17T07:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73263",
    "user": "https://github.com/nathanncohen"
}
```

Hello !! I know nothing about the file sage/combinat/backtrack.py, and I intend to read it as soon as possible but I saw on TRAC the same of this patch, and I was convinced it woukd be using the Graph library : in sage/graphs/base/c_graph.pyx are written iterators for depth/breadth-first-search in general graphs.. Wouldn't it be better for this class to use such functions, are they are written in Cython and should be more efficient ? Or directly use the Graph structure, as it would automatically call these functions.. :-)

Nathann



---

archive/issue_comments_073264.json:
```json
{
    "body": "Nathann, using the code the graphs code is not appropriate here as that would require the entire search tree to be created/known beforehand.",
    "created_at": "2010-02-17T07:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73264",
    "user": "https://github.com/mwhansen"
}
```

Nathann, using the code the graphs code is not appropriate here as that would require the entire search tree to be created/known beforehand.



---

archive/issue_comments_073265.json:
```json
{
    "body": "while it is not... Ok, I got it, then you can forget what I said :-)",
    "created_at": "2010-02-17T07:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73265",
    "user": "https://github.com/nathanncohen"
}
```

while it is not... Ok, I got it, then you can forget what I said :-)



---

archive/issue_comments_073266.json:
```json
{
    "body": "As discussed with Nicolas on irc. the patch needs some cleanup.",
    "created_at": "2010-03-04T23:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73266",
    "user": "https://github.com/hivert"
}
```

As discussed with Nicolas on irc. the patch needs some cleanup.



---

archive/issue_comments_073267.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-04T23:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73267",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073268.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-05T00:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73268",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073269.json:
```json
{
    "body": "Discussed on trac: there is an algorithmic problem:\nHere is my tests example:\n\n```\n    I = SearchForest([[3]], lambda l: (l+[i] for i in range(l[-1])))\n```\n\nDo you have an easy father function for this tree ?\nYes : `lambda l -> l[:-1]`\nIt simply generate strictly decreasing lists starting with 3.\nFor me a call to\n\n```\n    list(I.element_of_depth_iterator(2, \"Children\"))\n```\n\nraise a `StopIteration` ...\nWhereas:\n\n```\n    sage: list(I.element_of_depth_iterator(2))\n    [[3, 1, 0], [3, 2, 0], [3, 2, 1]]\n```\n",
    "created_at": "2010-03-05T10:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73269",
    "user": "https://github.com/hivert"
}
```

Discussed on trac: there is an algorithmic problem:
Here is my tests example:

```
    I = SearchForest([[3]], lambda l: (l+[i] for i in range(l[-1])))
```

Do you have an easy father function for this tree ?
Yes : `lambda l -> l[:-1]`
It simply generate strictly decreasing lists starting with 3.
For me a call to

```
    list(I.element_of_depth_iterator(2, "Children"))
```

raise a `StopIteration` ...
Whereas:

```
    sage: list(I.element_of_depth_iterator(2))
    [[3, 1, 0], [3, 2, 0], [3, 2, 1]]
```




---

archive/issue_comments_073270.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-05T10:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73270",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073271.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-05T17:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73271",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073272.json:
```json
{
    "body": "Attachment [search_forest_depth_and_breath_improvement-nb.patch](tarball://root/attachments/some-uuid/ticket8288/search_forest_depth_and_breath_improvement-nb.patch) by nborie created at 2010-03-05 17:23:14\n\nOne more time, my english is still bad... Feel free to point them and thus, make my english increasing....",
    "created_at": "2010-03-05T17:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73272",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [search_forest_depth_and_breath_improvement-nb.patch](tarball://root/attachments/some-uuid/ticket8288/search_forest_depth_and_breath_improvement-nb.patch) by nborie created at 2010-03-05 17:23:14

One more time, my english is still bad... Feel free to point them and thus, make my english increasing....



---

archive/issue_comments_073273.json:
```json
{
    "body": "Attachment [trac_8288-reviewer.patch](tarball://root/attachments/some-uuid/ticket8288/trac_8288-reviewer.patch) by mvngu created at 2010-04-19 02:52:24",
    "created_at": "2010-04-19T02:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8288-reviewer.patch](tarball://root/attachments/some-uuid/ticket8288/trac_8288-reviewer.patch) by mvngu created at 2010-04-19 02:52:24



---

archive/issue_comments_073274.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-19T02:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073275.json:
```json
{
    "body": "Don't use the keyword \"method\" to specify the algorithm to be used. Instead use \"algorithm\". See #6094 and #7971 for two attempts to get rid of using \"method\" for specifying the algorithm to be used. My reviewer patch makes this change to your implementation.\n\n\n\nFor any argument that can take more than one value, provide all the possible values. For example, if possible, list all the possible values for the argument \"algorithm\".\n\n\n\nThere is a slight bug in the method `search_forest_iterator()`. If `method=\"depth\"`, then we would use depth-first search. But to get `search_forest_iterator()` to use breadth-first search, we could assign any value to the keyword `method`:\n\n\n```\nsage: from sage.combinat.backtrack import search_forest_iterator\nsage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method=\"breadth\"))\n[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]\nsage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method=None))\n[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]\nsage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method=\"some sanity\"))\n[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]\n```\n\n\nTo remedy this bug, we could explicitly test for \"breadth\" and \"depth\" and set the value `position` accordingly. For any other value assigned to `algorithm`, we raise an exception. The reviewer patch implements this fix.\n\n\n\nThere is a slight bug in the method `element_of_depth_iterator()`. From your example given for that method, we can do this:\n\n\n```\nsage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)\nsage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)\nsage: list(I.element_of_depth_iterator(10, method=\"father\"))\n[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]\n```\n\n\nBut then, we could assign the keyword `method` with any value and get the same result as above:\n\n\n```\nsage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)\nsage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)\nsage: list(I.element_of_depth_iterator(10, method=\"mother\"))\n[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]\nsage: list(I.element_of_depth_iterator(10, method=\"grandma\"))\n[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]\nsage: list(I.element_of_depth_iterator(10, method=\"abc\"))\n[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]\n```\n\n\nOne way to fix this is to make `full_generation` into a boolean keyword. If `full_generation=True`, the search starts from the root and generate all elements until the given depth is reached. If `full_generation=False`, the search algorithm makes use of the `father` and `next_brother` methods. My reviewer patch makes this change.\n\n\n\n\nOther general remarks:\n\n* Whenever possible, avoid going over 79 characters per line.\n* When testing for `None`, don't use \"!=\". Instead use \"is not\", which is much faster than \"!=\". The same remark applies when testing for equality of an object with `None`.\n* For the method `first_element_of_depth()`, I don't understand what is the purpose of the keyword \"father_with_depth\". You need to document that keyword.\n* Some stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).\n\nI have provided a reviewer patch that implements some changes on top of nborie's patch. Someone needs to review the technical aspect of the features implemented by nborie's patch.",
    "created_at": "2010-04-19T02:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Don't use the keyword "method" to specify the algorithm to be used. Instead use "algorithm". See #6094 and #7971 for two attempts to get rid of using "method" for specifying the algorithm to be used. My reviewer patch makes this change to your implementation.



For any argument that can take more than one value, provide all the possible values. For example, if possible, list all the possible values for the argument "algorithm".



There is a slight bug in the method `search_forest_iterator()`. If `method="depth"`, then we would use depth-first search. But to get `search_forest_iterator()` to use breadth-first search, we could assign any value to the keyword `method`:


```
sage: from sage.combinat.backtrack import search_forest_iterator
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method="breadth"))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method=None))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
sage: list(search_forest_iterator([[]], lambda l: [l+[0], l+[1]] if len(l) < 3 else [], method="some sanity"))
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
```


To remedy this bug, we could explicitly test for "breadth" and "depth" and set the value `position` accordingly. For any other value assigned to `algorithm`, we raise an exception. The reviewer patch implements this fix.



There is a slight bug in the method `element_of_depth_iterator()`. From your example given for that method, we can do this:


```
sage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)
sage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)
sage: list(I.element_of_depth_iterator(10, method="father"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
```


But then, we could assign the keyword `method` with any value and get the same result as above:


```
sage: father = lambda t: (t[0]-1,0) if t[1] == 0 else (t[0],t[1]-1)
sage: I = SearchForest([(0,0)], lambda l: [(l[0]+1, l[1]), (l[0], 1)] if l[1] == 0 else [(l[0], l[1]+1)], father=father)
sage: list(I.element_of_depth_iterator(10, method="mother"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
sage: list(I.element_of_depth_iterator(10, method="grandma"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
sage: list(I.element_of_depth_iterator(10, method="abc"))
[(10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9), (0, 10)]
```


One way to fix this is to make `full_generation` into a boolean keyword. If `full_generation=True`, the search starts from the root and generate all elements until the given depth is reached. If `full_generation=False`, the search algorithm makes use of the `father` and `next_brother` methods. My reviewer patch makes this change.




Other general remarks:

* Whenever possible, avoid going over 79 characters per line.
* When testing for `None`, don't use "!=". Instead use "is not", which is much faster than "!=". The same remark applies when testing for equality of an object with `None`.
* For the method `first_element_of_depth()`, I don't understand what is the purpose of the keyword "father_with_depth". You need to document that keyword.
* Some stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).

I have provided a reviewer patch that implements some changes on top of nborie's patch. Someone needs to review the technical aspect of the features implemented by nborie's patch.



---

archive/issue_comments_073276.json:
```json
{
    "body": "Hi Nicolas,\n\nI'm currently using search forest and I run into some troubles... I also want\nto suggest some improvements in the code:\n\n- please define method `_repr_` (Sage way) rather than `__repr__`\n  (Python's way).\n\n- when you need to link a class in the same file you don't have to give the\n  full path for exampe `:class:`SearchForest`` is sufficient compared to\n  `:class:`~sage.combinat.backtrack.SearchForest``\n\n- please make sure and **document** that a common intended use of\n  `SearchForest` is to inherit from it, calling only\n  `Parent.__init__` and overload the methods \n  `roots, children, post_process` rather than passing them to the constructors. \n  Please make sure to specify their result type (iterable vs. iterator).\n  By the way, should'nt those methods be private methods (eg: `_roots`\n  vs. `roots`. I don't expect the user to call them in my use-case.\n\nThanks for all this ! I'm using it...\n\nFlorent",
    "created_at": "2010-06-02T14:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73276",
    "user": "https://github.com/hivert"
}
```

Hi Nicolas,

I'm currently using search forest and I run into some troubles... I also want
to suggest some improvements in the code:

- please define method `_repr_` (Sage way) rather than `__repr__`
  (Python's way).

- when you need to link a class in the same file you don't have to give the
  full path for exampe `:class:`SearchForest`` is sufficient compared to
  `:class:`~sage.combinat.backtrack.SearchForest``

- please make sure and **document** that a common intended use of
  `SearchForest` is to inherit from it, calling only
  `Parent.__init__` and overload the methods 
  `roots, children, post_process` rather than passing them to the constructors. 
  Please make sure to specify their result type (iterable vs. iterator).
  By the way, should'nt those methods be private methods (eg: `_roots`
  vs. `roots`. I don't expect the user to call them in my use-case.

Thanks for all this ! I'm using it...

Florent



---

archive/issue_comments_073277.json:
```json
{
    "body": "I upload a patch for this ticket to be discussed on http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/fbedf039a549c68b\n\nThanks for your comments Florent.\n\nNicolas.",
    "created_at": "2010-06-02T15:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73277",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I upload a patch for this ticket to be discussed on http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/fbedf039a549c68b

Thanks for your comments Florent.

Nicolas.



---

archive/issue_comments_073278.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-04T14:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73278",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073279.json:
```json
{
    "body": "Replying to [comment:13 nborie]:\n\nSome more remarks: please check your sphinx markup:\n\n- ``...`` is for mathematic ie is set up by TeX\n- ```...``` is for Sage/Python code. There are some ``__init__`` which doesn't compile.",
    "created_at": "2010-06-07T16:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73279",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:13 nborie]:

Some more remarks: please check your sphinx markup:

- ``...`` is for mathematic ie is set up by TeX
- ```...``` is for Sage/Python code. There are some ``__init__`` which doesn't compile.



---

archive/issue_comments_073280.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-07T16:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73280",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073281.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-13T16:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73281",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073282.json:
```json
{
    "body": "the last trac_8288_search_forest_depth_and_breath_improvement-nb.patch is ready from my side...",
    "created_at": "2010-07-13T16:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73282",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

the last trac_8288_search_forest_depth_and_breath_improvement-nb.patch is ready from my side...



---

archive/issue_comments_073283.json:
```json
{
    "body": "rebased for 4.5.1",
    "created_at": "2010-08-01T23:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73283",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

rebased for 4.5.1



---

archive/issue_comments_073284.json:
```json
{
    "body": "I put a patch up with some minor changes on the patch server.  Do you want to fold them into your patch.\n\nFlorent, what is the status of this ticket?",
    "created_at": "2010-11-26T02:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73284",
    "user": "https://github.com/mwhansen"
}
```

I put a patch up with some minor changes on the patch server.  Do you want to fold them into your patch.

Florent, what is the status of this ticket?



---

archive/issue_comments_073285.json:
```json
{
    "body": "Thanks Mike for yours changes.\n\nI folded your patch in mine and uploaded it to the trac. I also just checked (one more time) it apply well on 4.6, that all the tests pass and the doc seems fine to me (accordingly I am a bad English language reviewer).\n\nIt will be fine to finalize this work... (Was this point in your TODO list Nicolas ?)",
    "created_at": "2010-11-26T10:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73285",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Thanks Mike for yours changes.

I folded your patch in mine and uploaded it to the trac. I also just checked (one more time) it apply well on 4.6, that all the tests pass and the doc seems fine to me (accordingly I am a bad English language reviewer).

It will be fine to finalize this work... (Was this point in your TODO list Nicolas ?)



---

archive/issue_comments_073286.json:
```json
{
    "body": "Yes: we should just take 1/2 hour shortly to finalize this together.",
    "created_at": "2010-11-29T13:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73286",
    "user": "https://github.com/nthiery"
}
```

Yes: we should just take 1/2 hour shortly to finalize this together.



---

archive/issue_comments_073287.json:
```json
{
    "body": "Sorry for this post but with some hope that the buildbot take in care :\n\napply trac_8288_search_forest_depth_and_breath_improvement-nb.patch",
    "created_at": "2011-01-19T11:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73287",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Sorry for this post but with some hope that the buildbot take in care :

apply trac_8288_search_forest_depth_and_breath_improvement-nb.patch



---

archive/issue_comments_073288.json:
```json
{
    "body": "Hi Nicolas,\n\nI just made a couple minor improvements to the documentation on the sage-combinat patch server (directly in your patch). Please have a quick look, upload the new version to trac, and set a positive review on my behalf if you agree with my changes.\n\nCheers,\n                Nicolas",
    "created_at": "2011-03-24T11:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73288",
    "user": "https://github.com/nthiery"
}
```

Hi Nicolas,

I just made a couple minor improvements to the documentation on the sage-combinat patch server (directly in your patch). Please have a quick look, upload the new version to trac, and set a positive review on my behalf if you agree with my changes.

Cheers,
                Nicolas



---

archive/issue_comments_073289.json:
```json
{
    "body": "Attachment [trac_8288_search_forest_depth_and_breath_improvement-nb.patch](tarball://root/attachments/some-uuid/ticket8288/trac_8288_search_forest_depth_and_breath_improvement-nb.patch) by nborie created at 2011-03-24 16:41:17",
    "created_at": "2011-03-24T16:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73289",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_8288_search_forest_depth_and_breath_improvement-nb.patch](tarball://root/attachments/some-uuid/ticket8288/trac_8288_search_forest_depth_and_breath_improvement-nb.patch) by nborie created at 2011-03-24 16:41:17



---

archive/issue_comments_073290.json:
```json
{
    "body": "It is ok with your changes. Let it go in!",
    "created_at": "2011-03-24T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73290",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

It is ok with your changes. Let it go in!



---

archive/issue_comments_073291.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-24T17:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73291",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073292.json:
```json
{
    "body": "Oh my GOD `O_O`\n\nThis ticket is reviewed !! `O_O`\n\nWell done `:-)`\n\nNathann",
    "created_at": "2011-03-24T17:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73292",
    "user": "https://github.com/nathanncohen"
}
```

Oh my GOD `O_O`

This ticket is reviewed !! `O_O`

Well done `:-)`

Nathann



---

archive/issue_comments_073293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-07T13:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8288#issuecomment-73293",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
