# Issue 7966: Giving some punch to distance computations

archive/issues_007966.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis patch creates a function shortest_path_all_vertices in c_graphs which, given a vertex v, computes a shortest path for each other vertex.\n\nWith small other modifications, it improves the speed of many functions ( which were all calling each other )\n\nBefore :\n\n```\nsage: g = graphs.RandomGNP(50,.3)\nsage: %timeit g.shortest_path_lengths(0)\n100 loops, best of 3: 3.72 ms per loop\nsage: %timeit g.average_distance()\n10 loops, best of 3: 383 ms per loop\nsage: %timeit g.wiener_index()\n10 loops, best of 3: 384 ms per loop\nsage: %timeit g.szeged_index()\n10 loops, best of 3: 325 ms per loop\nsage: %timeit g.eccentricity()\n10 loops, best of 3: 189 ms per loop\nsage: g.sparse6_string()\n':q_OW_CCBb?WcOL@@`_{CGDB@pCGIF``@[WQK_`?w_QIDoo_WSJEBWGOKIDbG?CZ?@@Owwb?@?o_SOMba@X?bA@`OpKhBB@p?kX@Caq@YAACAphWn@B@po{j?@`?o_]QIeGOWMGDCqheEDB@pXMAEBa@GscYLoo__QJEBaxcvBECAPWqYNQ`gwgTKERX}?@@@@Gg[QHdBXt@?BAa@WmYNGWo[OLFCQhqCLFCRPky]POow_SLGCRHw}ca@_w_SLHCq`_u[OGg?GEDBAP_{iUJeBiYKGCbPp_qYMFbyLIea``WoYMFcA`SkXMGS[?MIFCahgw\\\\NP`Ww]VLfSskYMHDApcs[NHSy`R?A@pOkWMGcb@oy]TjGGKOJIEBh|QjUOox?mWLEryHIh___WOaRIDr@cu[MhTauCCBa@Gk]PHdax_w]NhCq\\\\Sm'\n```\n\nAfter\n\n```\nsage: %timeit g.shortest_path_lengths(0)\n10 loops, best of 3: 430 \u00b5s per loop\nsage: %timeit g.average_distance()\n10 loops, best of 3: 22 ms per loop\nsage: %timeit g.wiener_index()\n10 loops, best of 3: 22.1 ms per loop\nsage: %timeit g.szeged_index()\n10 loops, best of 3: 41.5 ms per loop\nsage: %timeit g.eccentricity()\n10 loops, best of 3: 22 ms per loop\n```\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7966\n\n",
    "created_at": "2010-01-17T14:34:20Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Giving some punch to distance computations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7966",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

This patch creates a function shortest_path_all_vertices in c_graphs which, given a vertex v, computes a shortest path for each other vertex.

With small other modifications, it improves the speed of many functions ( which were all calling each other )

Before :

```
sage: g = graphs.RandomGNP(50,.3)
sage: %timeit g.shortest_path_lengths(0)
100 loops, best of 3: 3.72 ms per loop
sage: %timeit g.average_distance()
10 loops, best of 3: 383 ms per loop
sage: %timeit g.wiener_index()
10 loops, best of 3: 384 ms per loop
sage: %timeit g.szeged_index()
10 loops, best of 3: 325 ms per loop
sage: %timeit g.eccentricity()
10 loops, best of 3: 189 ms per loop
sage: g.sparse6_string()
':q_OW_CCBb?WcOL@@`_{CGDB@pCGIF``@[WQK_`?w_QIDoo_WSJEBWGOKIDbG?CZ?@@Owwb?@?o_SOMba@X?bA@`OpKhBB@p?kX@Caq@YAACAphWn@B@po{j?@`?o_]QIeGOWMGDCqheEDB@pXMAEBa@GscYLoo__QJEBaxcvBECAPWqYNQ`gwgTKERX}?@@@@Gg[QHdBXt@?BAa@WmYNGWo[OLFCQhqCLFCRPky]POow_SLGCRHw}ca@_w_SLHCq`_u[OGg?GEDBAP_{iUJeBiYKGCbPp_qYMFbyLIea``WoYMFcA`SkXMGS[?MIFCahgw\\NP`Ww]VLfSskYMHDApcs[NHSy`R?A@pOkWMGcb@oy]TjGGKOJIEBh|QjUOox?mWLEryHIh___WOaRIDr@cu[MhTauCCBa@Gk]PHdax_w]NhCq\\Sm'
```

After

```
sage: %timeit g.shortest_path_lengths(0)
10 loops, best of 3: 430 µs per loop
sage: %timeit g.average_distance()
10 loops, best of 3: 22 ms per loop
sage: %timeit g.wiener_index()
10 loops, best of 3: 22.1 ms per loop
sage: %timeit g.szeged_index()
10 loops, best of 3: 41.5 ms per loop
sage: %timeit g.eccentricity()
10 loops, best of 3: 22 ms per loop
```

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7966





---

archive/issue_comments_069382.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T14:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69382",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069383.json:
```json
{
    "body": "Small modification to distance_graph too:\n\nBefore :\n\n```\nsage: %timeit g.distance_graph([2,8,9])\n10 loops, best of 3: 127 ms per loop\n```\nAfter\n\n```\nsage: %timeit g.distance_graph([2,8,9])\n10 loops, best of 3: 49 ms per loop\n```\n\nNathann",
    "created_at": "2010-01-17T15:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69383",
    "user": "https://github.com/nathanncohen"
}
```

Small modification to distance_graph too:

Before :

```
sage: %timeit g.distance_graph([2,8,9])
10 loops, best of 3: 127 ms per loop
```
After

```
sage: %timeit g.distance_graph([2,8,9])
10 loops, best of 3: 49 ms per loop
```

Nathann



---

archive/issue_comments_069384.json:
```json
{
    "body": "The speedups are great, but I got one extra failure (against 4.3.3 on Fedora 12):\n\n```\nsage -t  graphs/base/c_graph.pyx\nFile \"/usr/local/sage-4.3.3/sage/devel/sage-trac/sage/graphs/base/c_graph.pyx\",\\\n line 1427:\n    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \\\nin g])\nException raised:\n    Traceback (most recent call last):\n      File \"/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py\", line 1231, in \\\nrun_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/usr/local/sage-4.3.3/sage/local/bin/sagedoctest.py\", line 38, in r\\\nun_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compil\\\neflags)\n      File \"/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py\", line 1172, in \\\nrun_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_43[7]>\", line 1, in <module>\n        all([ len(paths[v]) == Integer(0) or len(paths[v])-Integer(1) == g.dist\\\nance(Integer(0),v) for v in g])###line 1427:\n    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \\\nin g])\n    KeyError: 20\n```\nPlease could you look at this?",
    "created_at": "2010-02-26T08:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69384",
    "user": "https://github.com/zimmermann6"
}
```

The speedups are great, but I got one extra failure (against 4.3.3 on Fedora 12):

```
sage -t  graphs/base/c_graph.pyx
File "/usr/local/sage-4.3.3/sage/devel/sage-trac/sage/graphs/base/c_graph.pyx",\
 line 1427:
    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \
in g])
Exception raised:
    Traceback (most recent call last):
      File "/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py", line 1231, in \
run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/usr/local/sage-4.3.3/sage/local/bin/sagedoctest.py", line 38, in r\
un_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compil\
eflags)
      File "/usr/local/sage-4.3.3/sage/local/bin/ncadoctest.py", line 1172, in \
run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[7]>", line 1, in <module>
        all([ len(paths[v]) == Integer(0) or len(paths[v])-Integer(1) == g.dist\
ance(Integer(0),v) for v in g])###line 1427:
    sage: all([ len(paths[v]) == 0 or len(paths[v])-1 == g.distance(0,v) for v \
in g])
    KeyError: 20
```
Please could you look at this?



---

archive/issue_comments_069385.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-26T08:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69385",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069386.json:
```json
{
    "body": "At first, the function associated a path from v to each other vertex, possibly empty if there was none. Then I noticed the other functions in Sage expected the dictionary to only contain keys corresponding to the vertices reachable from v (which was sound, too), and changed the original function, forgetting the docstrings... Fixed now ! \n\nAnd I also removed the (commented) loop which was associating empty paths when needed...\n\nThank you again ! :-)\n\nNathann",
    "created_at": "2010-02-26T10:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69386",
    "user": "https://github.com/nathanncohen"
}
```

At first, the function associated a path from v to each other vertex, possibly empty if there was none. Then I noticed the other functions in Sage expected the dictionary to only contain keys corresponding to the vertices reachable from v (which was sound, too), and changed the original function, forgetting the docstrings... Fixed now ! 

And I also removed the (commented) loop which was associating empty paths when needed...

Thank you again ! :-)

Nathann



---

archive/issue_comments_069387.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-26T10:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69387",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069388.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T11:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69388",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069389.json:
```json
{
    "body": "Attachment [trac_7966.patch](tarball://root/attachments/some-uuid/ticket7966/trac_7966.patch) by @zimmermann6 created at 2010-02-26 11:02:06\n\nwith the new patch `c_graph.pyx` works again:\n\n```\n[zimmerma@coing sage]$ sage -t  graphs/base/c_graph.pyx\nsage -t  \"devel/sage-7966/sage/graphs/base/c_graph.pyx\"     \n         [2.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.5 seconds\n```\nThus a positive review.\n\nPaul",
    "created_at": "2010-02-26T11:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69389",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_7966.patch](tarball://root/attachments/some-uuid/ticket7966/trac_7966.patch) by @zimmermann6 created at 2010-02-26 11:02:06

with the new patch `c_graph.pyx` works again:

```
[zimmerma@coing sage]$ sage -t  graphs/base/c_graph.pyx
sage -t  "devel/sage-7966/sage/graphs/base/c_graph.pyx"     
         [2.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.5 seconds
```
Thus a positive review.

Paul



---

archive/issue_comments_069390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7966#issuecomment-69390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019066.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T14:20:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7966",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7966#event-19066"
}
```
