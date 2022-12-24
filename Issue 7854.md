# Issue 7854: speed up edge_connectivity in easy cases

archive/issues_007854.json:
```json
{
    "body": "Assignee: rlm\n\nThis functions uses LP and has a big overhead because of that... Is many cases, though, the graph is not connected, or not 2-connected.\n\nTo test if a graph is connected, we already have the function is_connected which does the job very efficiently through depth-first-searches.\n\nWe also have a function is_strongly_connected for DiGraphs.\n\nTo test if a Graph is 2-connected, we can first :\n*  compute a strongly_connected_orientation with a linear-time function\n*  check whether the returned graph is strongly-connected ( linear time too )\n\nWithout this, much time is spent over building a useless Linear Program.\n\nNathann\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7854\n\n",
    "created_at": "2010-01-06T12:27:35Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "speed up edge_connectivity in easy cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7854",
    "user": "ncohen"
}
```
Assignee: rlm

This functions uses LP and has a big overhead because of that... Is many cases, though, the graph is not connected, or not 2-connected.

To test if a graph is connected, we already have the function is_connected which does the job very efficiently through depth-first-searches.

We also have a function is_strongly_connected for DiGraphs.

To test if a Graph is 2-connected, we can first :
*  compute a strongly_connected_orientation with a linear-time function
*  check whether the returned graph is strongly-connected ( linear time too )

Without this, much time is spent over building a useless Linear Program.

Nathann



Issue created by migration from https://trac.sagemath.org/ticket/7854





---

archive/issue_comments_068047.json:
```json
{
    "body": "Small modifications, good results :\nBefore :\n\n```\nsage: %timeit graphs.WorldMap().edge_connectivity()\n10 loops, best of 3: 200 ms per loop\n```\n\n\nAfter :\n\n```\nsage: %timeit graphs.WorldMap().edge_connectivity()\n100 loops, best of 3: 4.75 ms per loop\n```\n",
    "created_at": "2010-01-16T16:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68047",
    "user": "ncohen"
}
```

Small modifications, good results :
Before :

```
sage: %timeit graphs.WorldMap().edge_connectivity()
10 loops, best of 3: 200 ms per loop
```


After :

```
sage: %timeit graphs.WorldMap().edge_connectivity()
100 loops, best of 3: 4.75 ms per loop
```




---

archive/issue_comments_068048.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T16:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68048",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068049.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T22:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68049",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_068050.json:
```json
{
    "body": "Nathann, I tried before the patch but got:\n\n```\nsage: %timeit graphs.WorldMap().edge_connectivity()\n...\nValueError: There does not seem to be any Linear Program solver installed. Please visit http://www.sagemath.org/packages/optional/ to install CBC or GLPK.\n```\n\nWhich LP package did you use? CBC or GLPK? Did you check you got a speedup with both?",
    "created_at": "2010-02-25T22:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68050",
    "user": "zimmerma"
}
```

Nathann, I tried before the patch but got:

```
sage: %timeit graphs.WorldMap().edge_connectivity()
...
ValueError: There does not seem to be any Linear Program solver installed. Please visit http://www.sagemath.org/packages/optional/ to install CBC or GLPK.
```

Which LP package did you use? CBC or GLPK? Did you check you got a speedup with both?



---

archive/issue_comments_068051.json:
```json
{
    "body": "Hello !!!!\n\nActually, the patch works with any LP solver which is installed.\nWhat you get is is a totally unrelated \"bug\". After installing the package corresponding to a LP solver, the user has to run \"sage -b\" but has no way to know about it for the moment. There is an update of GLPK waiting for review (#8298) and Cbc will follow (#8171). Sorry for the trouble !\n\nThis patch just avoids the use of LP when it is possible -- when the graph isn't connected, or not 2-connected. The functions used are written in Cython, which makes them almost instantaneous to use. Actually, checking the connectivity for low values this way is even faster than just generating the linear program, so it definitely is good to have :-)\n\nNathann",
    "created_at": "2010-02-26T06:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68051",
    "user": "ncohen"
}
```

Hello !!!!

Actually, the patch works with any LP solver which is installed.
What you get is is a totally unrelated "bug". After installing the package corresponding to a LP solver, the user has to run "sage -b" but has no way to know about it for the moment. There is an update of GLPK waiting for review (#8298) and Cbc will follow (#8171). Sorry for the trouble !

This patch just avoids the use of LP when it is possible -- when the graph isn't connected, or not 2-connected. The functions used are written in Cython, which makes them almost instantaneous to use. Actually, checking the connectivity for low values this way is even faster than just generating the linear program, so it definitely is good to have :-)

Nathann



---

archive/issue_comments_068052.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-26T06:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68052",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_068053.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-26T08:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68053",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068054.json:
```json
{
    "body": "thanks Nathann for your answer.\nI successfully installed the cbc package from http://www.sagemath.org/packages/optional/ in 4.3.3\n(btw, there are several compiler warnings during compilation, on a 64-bit Core 2 Duo).\n*Before* applying your patch, I get:\n\n```\nsage: g = 2 * graphs.PetersenGraph() \nsage: g.edge_connectivity() \n0.0\nsage: g = graphs.PathGraph(10) \nsage: g.edge_connectivity() \n1.0\nsage: g = digraphs.ButterflyGraph(3) \nsage: g.edge_connectivity() \n0.0\nsage: g = 2 * graphs.PetersenGraph() \nsage: g.vertex_connectivity() \n0.0\nsage: g = graphs.PathGraph(10) \nsage:  g.vertex_connectivity() \n1.0\nsage: g = digraphs.ButterflyGraph(3) \nsage: g.vertex_connectivity() \n0.0\n```\n\nthus it seems to me some work is needed, because according to the patch documentation, after\napplying the patch I will get integer values instead of floating-point numbers, which may break\nsome code using those functions.\n\nPaul",
    "created_at": "2010-02-26T08:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68054",
    "user": "zimmerma"
}
```

thanks Nathann for your answer.
I successfully installed the cbc package from http://www.sagemath.org/packages/optional/ in 4.3.3
(btw, there are several compiler warnings during compilation, on a 64-bit Core 2 Duo).
*Before* applying your patch, I get:

```
sage: g = 2 * graphs.PetersenGraph() 
sage: g.edge_connectivity() 
0.0
sage: g = graphs.PathGraph(10) 
sage: g.edge_connectivity() 
1.0
sage: g = digraphs.ButterflyGraph(3) 
sage: g.edge_connectivity() 
0.0
sage: g = 2 * graphs.PetersenGraph() 
sage: g.vertex_connectivity() 
0.0
sage: g = graphs.PathGraph(10) 
sage:  g.vertex_connectivity() 
1.0
sage: g = digraphs.ButterflyGraph(3) 
sage: g.vertex_connectivity() 
0.0
```

thus it seems to me some work is needed, because according to the patch documentation, after
applying the patch I will get integer values instead of floating-point numbers, which may break
some code using those functions.

Paul



---

archive/issue_comments_068055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-26T10:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68055",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068056.json:
```json
{
    "body": "Hello !! \n\nIt was even worse than this... The patch made Sage check manually if the graph was 1- or 2-connected, even if the user requested the weights on the edges to be taken into account, which would clearly have returned wrong results at some point, as the speedup only considered the graph's topology. It now checks this option is set to False. I also set it to False by default, so that the user will be able to enjoy these speed-ups. Anyway, I think it is best not to use the edges'  weights by default. I very frequently deal with graph having tuples as labels to remember a lot of informations, and this function wouldn't like it at all :-)\n\n(several minutes later)\n\nAhem... And I also noticed a bug that had me worried for a while. When testing docstrings, I found that the PappusGraph was only 1-connected instead of 3-connected, and the LP seemed to be in fault. In the end, I just noticed I had called \"g\" the strongly connected orientation, which was the main graph's name !!!!!\n\nBetter this way... ;-)\n\nThank you for your help !\n\nNathann",
    "created_at": "2010-02-26T10:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68056",
    "user": "ncohen"
}
```

Hello !! 

It was even worse than this... The patch made Sage check manually if the graph was 1- or 2-connected, even if the user requested the weights on the edges to be taken into account, which would clearly have returned wrong results at some point, as the speedup only considered the graph's topology. It now checks this option is set to False. I also set it to False by default, so that the user will be able to enjoy these speed-ups. Anyway, I think it is best not to use the edges'  weights by default. I very frequently deal with graph having tuples as labels to remember a lot of informations, and this function wouldn't like it at all :-)

(several minutes later)

Ahem... And I also noticed a bug that had me worried for a while. When testing docstrings, I found that the PappusGraph was only 1-connected instead of 3-connected, and the LP seemed to be in fault. In the end, I just noticed I had called "g" the strongly connected orientation, which was the main graph's name !!!!!

Better this way... ;-)

Thank you for your help !

Nathann



---

archive/issue_comments_068057.json:
```json
{
    "body": "Attachment [trac_7854.patch](tarball://root/attachments/some-uuid/ticket7854/trac_7854.patch) by ncohen created at 2010-02-26 10:27:19",
    "created_at": "2010-02-26T10:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68057",
    "user": "ncohen"
}
```

Attachment [trac_7854.patch](tarball://root/attachments/some-uuid/ticket7854/trac_7854.patch) by ncohen created at 2010-02-26 10:27:19



---

archive/issue_comments_068058.json:
```json
{
    "body": "Now the patch gives floating-point values as before.\nHowever I wonder why those values are floating-point numbers and not integers, since for example\nthe connectivity is an integer according to the reference wikipedia page.\n\n(This might be solved in a further ticket, thus I give a positive review for the present one.)",
    "created_at": "2010-02-27T22:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68058",
    "user": "zimmerma"
}
```

Now the patch gives floating-point values as before.
However I wonder why those values are floating-point numbers and not integers, since for example
the connectivity is an integer according to the reference wikipedia page.

(This might be solved in a further ticket, thus I give a positive review for the present one.)



---

archive/issue_comments_068059.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-27T22:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68059",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068060.json:
```json
{
    "body": "The reason is that this function handles weighted edges, and those edges may be weighted with floating-point values :-)\n\nI am myself only interested by \"topological\" connectivity, in which all edges are weighted with 1, but I do not really mind as long as connectivity() == k works... \n\nThank you very much for your help !!!\n\nNathann",
    "created_at": "2010-02-28T01:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68060",
    "user": "ncohen"
}
```

The reason is that this function handles weighted edges, and those edges may be weighted with floating-point values :-)

I am myself only interested by "topological" connectivity, in which all edges are weighted with 1, but I do not really mind as long as connectivity() == k works... 

Thank you very much for your help !!!

Nathann



---

archive/issue_comments_068061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7854#issuecomment-68061",
    "user": "mvngu"
}
```

Resolution: fixed
