# Issue 9584: Weird timeouts in doctesting generic_graph with 4.5.2.alpha0 on some systems

archive/issues_009584.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @jhpalmieri @nexttime @nathanncohen\n\nKeywords: generic_graph, generic graph, time-out, time out\n\nReported by John Palmieri and Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/da2dfbbe52d9917b#da2dfbbe52d9917b):\n\n```\nOn 07/23/2010 12:18 AM, leif wrote:\n> John H Palmieri wrote:\n>> On iras (ia64-Linux-suse), after continuing the build, one failure:\n>>\n>> sage -t -long \"devel/sage/sage/graphs/genus.pyx\"\n>> **********************************************************************\n>> File \"/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/\n>> genus.pyx\", line 129:\n>>     sage: get_memory_usage(t)\n>> Expected:\n>>     0.0\n>> Got:\n>>     -0.28125\n>> **********************************************************************\n> \n> So whenever you run out of memory on that machine, start a few instances\n> of that program... :D :D :D\n> \n>> Several machines (cleo, iras) get timeouts on generic_graph.py.\n> \n> (Doesn't terminate within an hour here on 32-bit Ubuntu, Pentium 4...)\n```\nThese may be unrelated to each other, however.\n\n---\n\nThe **doctest error** in `sage/graphs/generic_graph.py` on 32-bit systems is now #9594.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9584\n\n",
    "closed_at": "2010-07-27T00:42:21Z",
    "created_at": "2010-07-23T08:12:35Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Weird timeouts in doctesting generic_graph with 4.5.2.alpha0 on some systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9584",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @jhpalmieri @nexttime @nathanncohen

Keywords: generic_graph, generic graph, time-out, time out

Reported by John Palmieri and Leif Leonhardy on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/cc0b1929f66e0658/da2dfbbe52d9917b#da2dfbbe52d9917b):

```
On 07/23/2010 12:18 AM, leif wrote:
> John H Palmieri wrote:
>> On iras (ia64-Linux-suse), after continuing the build, one failure:
>>
>> sage -t -long "devel/sage/sage/graphs/genus.pyx"
>> **********************************************************************
>> File "/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/
>> genus.pyx", line 129:
>>     sage: get_memory_usage(t)
>> Expected:
>>     0.0
>> Got:
>>     -0.28125
>> **********************************************************************
> 
> So whenever you run out of memory on that machine, start a few instances
> of that program... :D :D :D
> 
>> Several machines (cleo, iras) get timeouts on generic_graph.py.
> 
> (Doesn't terminate within an hour here on 32-bit Ubuntu, Pentium 4...)
```
These may be unrelated to each other, however.

---

The **doctest error** in `sage/graphs/generic_graph.py` on 32-bit systems is now #9594.

Issue created by migration from https://trac.sagemath.org/ticket/9584





---

archive/issue_comments_092474.json:
```json
{
    "body": "''Copied from the sage-release thread (slightly beautified):\n''\n  1: `devel/sage/sage/graphs/generic_graph.py`\n  \n    Doesn't terminate at all(?), gets killed even if I test just that file, with `SAGE_TIMEOUT_LONG=3600` (1 hour)!\n\nTesting with `-verbose`, I now experience the same doctest failure John [Cremona]\nreported (and only that):\n\n```\n...\nTrying:\n    P = G.plot(save_pos=True, layout='spring')###line 11577:_sage_    >>> P = G.plot(save_pos=True, layout='spring')\nExpecting nothing\nok\nTrying:\n    G.get_pos()###line 11581:_sage_    >>> G.get_pos()\nExpecting:\n    {0: [1.17..., -0.855...],\n     1: [1.81..., -0.0990...],\n     2: [1.35..., 0.184...],\n     3: [1.51..., 0.644...],\n     4: [2.00..., -0.507...],\n     5: [0.597..., -0.236...],\n     6: [2.04..., 0.687...],\n     7: [1.46..., -0.473...],\n     8: [0.902..., 0.773...],\n     9: [2.48..., -0.119...]}\n**********************************************************************\nFile \"/home/leif/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py\", line 8617, in __main__.example_191\nFailed example:\n    G.get_pos()###line 11581:_sage_    >>> G.get_pos()\nExpected:\n    {0: [1.17..., -0.855...],\n     1: [1.81..., -0.0990...],\n     2: [1.35..., 0.184...],\n     3: [1.51..., 0.644...],\n     4: [2.00..., -0.507...],\n     5: [0.597..., -0.236...],\n     6: [2.04..., 0.687...],\n     7: [1.46..., -0.473...],\n     8: [0.902..., 0.773...],\n     9: [2.48..., -0.119...]}\nGot:\n    {0: [1.1644236010005358, -0.83686858657215979], 1:\n[1.7943839700815074, -0.066920666682206337], 2: [1.2689961125613971,\n0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4:\n[1.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395,\n-0.2204272806589378], 6: [2.0144421480067041, 0.70158250822163282], 7:\n[1.4603696336476519, -0.46717593533332896], 8: [0.90427280509063312,\n0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}\nTrying:\n    T = list(graphs.trees(Integer(7)))###line 11595:_sage_    >>> T = list(graphs.trees(7))\nExpecting nothing\nok\n...\n```\n\nThe following is the last output I get (note that the examples aren't tested in order, i.e. original source line numbers usually aren't monotonic):\n\n```\nTrying:\n    D.connected_component_containing_vertex(Integer(0))###line 3090:_sage_    >>> D.connected_component_containing_vertex(0)\nExpecting:\n    [0, 1, 2, 3]\nok\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    graphs.PetersenGraph().blocks_and_cut_vertices()###line 3117:_sage_    >>> graphs.PetersenGraph().blocks_and_cut_vertices()\nExpecting:\n    ([[6, 4, 9, 7, 5, 8, 3, 2, 1, 0]], [])\nok\nTrying:\n    graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()###line 3119:_sage_    >>> graphs.PathGraph(6).blocks_and_cut_vertices()\nExpecting:\n    ([[5, 4], [*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n\t [3600.9 s]\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long -verbose \"devel/sage/sage/graphs/generic_graph.py\" # Time out\nTotal time for all tests: 3600.9 seconds\n\nreal\t60m1.029s\nuser\t0m2.360s\nsys\t0m0.884s\n```\n*[Note the real/CPU time.]*\n\nThe funny thing is that with `-verbose`, I do not even get the shell prompt back (I redirected stderr to stdout and tee'd it); `./sage -t -long ...` terminates, but I guess its now orphan child (`python /home/leif/.sage//tmp/.doctest_generic_graph.py`[sic], which is actually running - consuming CPU time, in contrast to its two `gap` children, which sleep due to blocking reads) keeps at least one of the file descriptors open...\n\n*[This was on **32-bit** Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code). John Cremona experienced the doctest failure on **32-bit** SuSE...]*",
    "created_at": "2010-07-23T09:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92474",
    "user": "https://github.com/nexttime"
}
```

''Copied from the sage-release thread (slightly beautified):
''
  1: `devel/sage/sage/graphs/generic_graph.py`
  
    Doesn't terminate at all(?), gets killed even if I test just that file, with `SAGE_TIMEOUT_LONG=3600` (1 hour)!

Testing with `-verbose`, I now experience the same doctest failure John [Cremona]
reported (and only that):

```
...
Trying:
    P = G.plot(save_pos=True, layout='spring')###line 11577:_sage_    >>> P = G.plot(save_pos=True, layout='spring')
Expecting nothing
ok
Trying:
    G.get_pos()###line 11581:_sage_    >>> G.get_pos()
Expecting:
    {0: [1.17..., -0.855...],
     1: [1.81..., -0.0990...],
     2: [1.35..., 0.184...],
     3: [1.51..., 0.644...],
     4: [2.00..., -0.507...],
     5: [0.597..., -0.236...],
     6: [2.04..., 0.687...],
     7: [1.46..., -0.473...],
     8: [0.902..., 0.773...],
     9: [2.48..., -0.119...]}
**********************************************************************
File "/home/leif/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 8617, in __main__.example_191
Failed example:
    G.get_pos()###line 11581:_sage_    >>> G.get_pos()
Expected:
    {0: [1.17..., -0.855...],
     1: [1.81..., -0.0990...],
     2: [1.35..., 0.184...],
     3: [1.51..., 0.644...],
     4: [2.00..., -0.507...],
     5: [0.597..., -0.236...],
     6: [2.04..., 0.687...],
     7: [1.46..., -0.473...],
     8: [0.902..., 0.773...],
     9: [2.48..., -0.119...]}
Got:
    {0: [1.1644236010005358, -0.83686858657215979], 1:
[1.7943839700815074, -0.066920666682206337], 2: [1.2689961125613971,
0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4:
[1.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395,
-0.2204272806589378], 6: [2.0144421480067041, 0.70158250822163282], 7:
[1.4603696336476519, -0.46717593533332896], 8: [0.90427280509063312,
0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}
Trying:
    T = list(graphs.trees(Integer(7)))###line 11595:_sage_    >>> T = list(graphs.trees(7))
Expecting nothing
ok
...
```

The following is the last output I get (note that the examples aren't tested in order, i.e. original source line numbers usually aren't monotonic):

```
Trying:
    D.connected_component_containing_vertex(Integer(0))###line 3090:_sage_    >>> D.connected_component_containing_vertex(0)
Expecting:
    [0, 1, 2, 3]
ok
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    graphs.PetersenGraph().blocks_and_cut_vertices()###line 3117:_sage_    >>> graphs.PetersenGraph().blocks_and_cut_vertices()
Expecting:
    ([[6, 4, 9, 7, 5, 8, 3, 2, 1, 0]], [])
ok
Trying:
    graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()###line 3119:_sage_    >>> graphs.PathGraph(6).blocks_and_cut_vertices()
Expecting:
    ([[5, 4], [*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [3600.9 s]

----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 3600.9 seconds

real	60m1.029s
user	0m2.360s
sys	0m0.884s
```
*[Note the real/CPU time.]*

The funny thing is that with `-verbose`, I do not even get the shell prompt back (I redirected stderr to stdout and tee'd it); `./sage -t -long ...` terminates, but I guess its now orphan child (`python /home/leif/.sage//tmp/.doctest_generic_graph.py`[sic], which is actually running - consuming CPU time, in contrast to its two `gap` children, which sleep due to blocking reads) keeps at least one of the file descriptors open...

*[This was on **32-bit** Ubuntu 9.04 (P4 Prescott 3.2GHz, gcc 4.3.3, native code). John Cremona experienced the doctest failure on **32-bit** SuSE...]*



---

archive/issue_comments_092475.json:
```json
{
    "body": "Replying to [comment:1 leif]:\n> \n\n{{{\n...\nreal\t60m1.029s\nuser\t0m2.360s\nsys\t0m0.884s\n}}}\n> *[Note the real/CPU time.]*\n\n\nShould read *\"**user**/CPU time\"*; i.e. the process does idle/sleep/wait most of the first hour. After gotten \"killed\", gets busy somehow... :)",
    "created_at": "2010-07-23T09:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92475",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 leif]:
> 

{{{
...
real	60m1.029s
user	0m2.360s
sys	0m0.884s
}}}
> *[Note the real/CPU time.]*


Should read *"**user**/CPU time"*; i.e. the process does idle/sleep/wait most of the first hour. After gotten "killed", gets busy somehow... :)



---

archive/issue_comments_092476.json:
```json
{
    "body": "What are the relevant tickets which were merged since 4.5.1? Looking at the list on the Roadmap, under graph theory, none of them really look like they could cause something like this...\n\nIf I try running the command last printed above on geom.math, I instantly get:\n\n```\nsage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()\n([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])\n```\n\nHmmm...",
    "created_at": "2010-07-24T11:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92476",
    "user": "https://github.com/rlmill"
}
```

What are the relevant tickets which were merged since 4.5.1? Looking at the list on the Roadmap, under graph theory, none of them really look like they could cause something like this...

If I try running the command last printed above on geom.math, I instantly get:

```
sage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()
([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])
```

Hmmm...



---

archive/issue_comments_092477.json:
```json
{
    "body": "Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?",
    "created_at": "2010-07-24T11:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92477",
    "user": "https://github.com/rlmill"
}
```

Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?



---

archive/issue_comments_092478.json:
```json
{
    "body": "Replying to [comment:3 rlm]:\n> If I try running the command last printed above on geom.math, I instantly get:\n\n{{{\nsage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()\n([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])\n}}}\n> \n> Hmmm...\n\nI've added some flushs in `ncadoctest.py`, now the log ends with:\n\n```\nTrying:\n    g = graphs.RandomGNP(Integer(30),RealNumber('.5'))###line 3276:_sage_    >>> g = graphs.RandomGNP(30,.5)\nExpecting nothing\nok\nTrying:\n    st = g.steiner_tree(g.vertices()[:Integer(5)])###line 3277:_sage_    >>> st = g.steiner_tree(g.vertices()[:5])\nExpecting nothing\nok\nTrying:\n    st.is_tree()###line 3278:_sage_    >>> st.is_tree()\nExpecting:\n    True\nok\nTrying:\n    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])\nExpecting:\n    True\nok\nTrying:\n    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()\nExpecting nothing\nok\nTrying:\n    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])\nExpecting:\n    Traceback (most recent call last):\n    ...\n    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !\nok\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n\t [1801.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -verbose \"devel/sage/sage/graphs/generic_graph.py\" # Time out\nTotal time for all tests: 1801.4 seconds\n\nreal\t30m1.590s\nuser\t0m1.912s\nsys\t0m0.536s\n^C\nleif@californication:~/sage-4.5.2.alpha0-j6$ \n```\n(Note that again I don't get a shell prompt, and `python`, `gap` and `sage-cleaner` are still \"running\", only `python .../.doctest_generic_graph.py` consumes CPU time. I've decreased `SAGE_TIMEOUT_LONG` to half an hour, the shown tests take much shorter, about 55 seconds.)",
    "created_at": "2010-07-24T14:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92478",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 rlm]:
> If I try running the command last printed above on geom.math, I instantly get:

{{{
sage: graphs.PathGraph(Integer(6)).blocks_and_cut_vertices()
([[5, 4], [4, 3], [3, 2], [2, 1], [1, 0]], [4, 3, 2, 1])
}}}
> 
> Hmmm...

I've added some flushs in `ncadoctest.py`, now the log ends with:

```
Trying:
    g = graphs.RandomGNP(Integer(30),RealNumber('.5'))###line 3276:_sage_    >>> g = graphs.RandomGNP(30,.5)
Expecting nothing
ok
Trying:
    st = g.steiner_tree(g.vertices()[:Integer(5)])###line 3277:_sage_    >>> st = g.steiner_tree(g.vertices()[:5])
Expecting nothing
ok
Trying:
    st.is_tree()###line 3278:_sage_    >>> st.is_tree()
Expecting:
    True
ok
Trying:
    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])
Expecting:
    True
ok
Trying:
    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()
Expecting nothing
ok
Trying:
    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !
ok
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [1801.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 1801.4 seconds

real	30m1.590s
user	0m1.912s
sys	0m0.536s
^C
leif@californication:~/sage-4.5.2.alpha0-j6$ 
```
(Note that again I don't get a shell prompt, and `python`, `gap` and `sage-cleaner` are still "running", only `python .../.doctest_generic_graph.py` consumes CPU time. I've decreased `SAGE_TIMEOUT_LONG` to half an hour, the shown tests take much shorter, about 55 seconds.)



---

archive/issue_comments_092479.json:
```json
{
    "body": "Ooops, I just noticed the log above is even **without** `-long`, so I actually *increased* `SAGE_TIMEOUT`, and did not include the long tests (that was yesterday). The behavior is samewhat similar though.",
    "created_at": "2010-07-24T14:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92479",
    "user": "https://github.com/nexttime"
}
```

Ooops, I just noticed the log above is even **without** `-long`, so I actually *increased* `SAGE_TIMEOUT`, and did not include the long tests (that was yesterday). The behavior is samewhat similar though.



---

archive/issue_comments_092480.json:
```json
{
    "body": "**With** `-long` (and `SAGE_TIMEOUT_LONG` decreased to 15 minutes):\n\n```sh\nTrying:\n    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])\nExpecting:\n    True\nok\nTrying:\n    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()\nExpecting nothing\nok\nTrying:\n    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])\nExpecting:\n    Traceback (most recent call last):\n    ...\n    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !\nok\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n\t [900.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long -verbose \"devel/sage/sage/graphs/generic_graph.py\" # Time out\nTotal time for all tests: 900.9 seconds\n\nreal\t15m1.016s\nuser\t0m1.084s\nsys\t0m0.360s\n^C\nleif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ \n```\nI simply forgot it was the same; the shown tests take roughly 2 minutes and a few seconds.",
    "created_at": "2010-07-24T15:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92480",
    "user": "https://github.com/nexttime"
}
```

**With** `-long` (and `SAGE_TIMEOUT_LONG` decreased to 15 minutes):

```sh
Trying:
    all([v in st for v in g.vertices()[:Integer(5)] ])###line 3283:_sage_    >>> all([v in st for v in g.vertices()[:5] ])
Expecting:
    True
ok
Trying:
    g = Integer(2) * graphs.PetersenGraph()###line 3290:_sage_    >>> g = 2 * graphs.PetersenGraph()
Expecting nothing
ok
Trying:
    st = g.steiner_tree([Integer(5),Integer(15)])###line 3291:_sage_    >>> st = g.steiner_tree([5,15])
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: The given vertices do not all belong to the same connected component. This problem has no solution !
ok
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [900.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 900.9 seconds

real	15m1.016s
user	0m1.084s
sys	0m0.360s
^C
leif@californication:~/sage-4.5.2.alpha0-j6/devel/sage-9590$ 
```
I simply forgot it was the same; the shown tests take roughly 2 minutes and a few seconds.



---

archive/issue_comments_092481.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?\n\n\nToday the doctest is passing for me.  I don't know why.  (A few days ago it failed with \"make ptestlong\", and then it failed repeatedly from the command line.)  If you want to try it yourself, I think my account on skynet is now readable: look in `/home/palmieri/cleo/sage-4.5.2.alpha0/`.\n\nI'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)",
    "created_at": "2010-07-24T15:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92481",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:4 rlm]:
> Also, when trying to reproduce this on cleo, sage fails to start (this is the one in wstein's build dir), and I can't copy all the bits because of permission issues. Has anyone else tried to isolate the command causing this on cleo?


Today the doctest is passing for me.  I don't know why.  (A few days ago it failed with "make ptestlong", and then it failed repeatedly from the command line.)  If you want to try it yourself, I think my account on skynet is now readable: look in `/home/palmieri/cleo/sage-4.5.2.alpha0/`.

I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)



---

archive/issue_comments_092482.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)\n\n\nAlso on cicero (32-bit)?",
    "created_at": "2010-07-24T16:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92482",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 jhpalmieri]:
> I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)


Also on cicero (32-bit)?



---

archive/issue_comments_092483.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Replying to [comment:8 jhpalmieri]:\n> > I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)\n\n> \n> Also on cicero (32-bit)?\n\nOr did all tests (except #9554) pass on that machine? (I haven't seen a report.)",
    "created_at": "2010-07-24T16:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92483",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:9 leif]:
> Replying to [comment:8 jhpalmieri]:
> > I'm trying generic_graph.py again with longer values for SAGE_TIMEOUT_LONG.  Back in a few hours :)

> 
> Also on cicero (32-bit)?

Or did all tests (except #9554) pass on that machine? (I haven't seen a report.)



---

archive/issue_comments_092484.json:
```json
{
    "body": "On cicero, I get the failure reported by John Cremona on sage-release:\n\n```\nsage -t  -long \"devel/sage/sage/graphs/generic_graph.py\"\n**********************************************************************\nFile \"/home/palmieri/cicero/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py\", line 11581\\\n:\n    sage: G.get_pos()\nExpected:\n    {0: [1.17..., -0.855...],\n     1: [1.81..., -0.0990...],\n     2: [1.35..., 0.184...],\n     3: [1.51..., 0.644...],\n     4: [2.00..., -0.507...],\n     5: [0.597..., -0.236...],\n     6: [2.04..., 0.687...],\n     7: [1.46..., -0.473...],\n     8: [0.902..., 0.773...],\n     9: [2.48..., -0.119...]}\nGot:\n    {0: [1.1644236010005358, -0.83686858657215979], 1: [1.7943839700815074, -0.066920666682206337]\\\n, 2: [1.2689961125613971, 0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4: [1\\\n.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395, -0.2204272806589378], 6: [2.014\\\n4421480067041, 0.70158250822163282], 7: [1.4603696336476519, -0.46717593533332896], 8: [0.90427280\\\n509063312, 0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}\n**********************************************************************\n```\nIs there a separate ticket for this one?  Testing completes in under 5 minutes: no timeout.\n\nI get the timeout on iras, and I've started that test again now, too.",
    "created_at": "2010-07-24T16:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92484",
    "user": "https://github.com/jhpalmieri"
}
```

On cicero, I get the failure reported by John Cremona on sage-release:

```
sage -t  -long "devel/sage/sage/graphs/generic_graph.py"
**********************************************************************
File "/home/palmieri/cicero/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 11581\
:
    sage: G.get_pos()
Expected:
    {0: [1.17..., -0.855...],
     1: [1.81..., -0.0990...],
     2: [1.35..., 0.184...],
     3: [1.51..., 0.644...],
     4: [2.00..., -0.507...],
     5: [0.597..., -0.236...],
     6: [2.04..., 0.687...],
     7: [1.46..., -0.473...],
     8: [0.902..., 0.773...],
     9: [2.48..., -0.119...]}
Got:
    {0: [1.1644236010005358, -0.83686858657215979], 1: [1.7943839700815074, -0.066920666682206337]\
, 2: [1.2689961125613971, 0.14359096356381118], 3: [1.511860539628787, 0.59162048325984706], 4: [1\
.9941403734258905, -0.53845815492480542], 5: [0.59110867097474395, -0.2204272806589378], 6: [2.014\
4421480067041, 0.70158250822163282], 7: [1.4603696336476519, -0.46717593533332896], 8: [0.90427280\
509063312, 0.79073173670301911], 9: [2.4603584159299983, -0.097675067576871527]}
**********************************************************************
```
Is there a separate ticket for this one?  Testing completes in under 5 minutes: no timeout.

I get the timeout on iras, and I've started that test again now, too.



---

archive/issue_comments_092485.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> On cicero, I get the failure reported by John Cremona on sage-release:\n\n<snip>\n> Is there a separate ticket for this one?\n\n\nNot that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).\n\nShould we split off one of the issues? The doctest failure is likely to get fixed quicker I think.",
    "created_at": "2010-07-24T17:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92485",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 jhpalmieri]:
> On cicero, I get the failure reported by John Cremona on sage-release:

<snip>
> Is there a separate ticket for this one?


Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).

Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.



---

archive/issue_comments_092486.json:
```json
{
    "body": "Just curious: Cicero runs Fedora 12 I think, what version is gcc?",
    "created_at": "2010-07-24T18:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92486",
    "user": "https://github.com/nexttime"
}
```

Just curious: Cicero runs Fedora 12 I think, what version is gcc?



---

archive/issue_comments_092487.json:
```json
{
    "body": "All of the skynet machines run gcc 4.5.0.",
    "created_at": "2010-07-24T18:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92487",
    "user": "https://github.com/jhpalmieri"
}
```

All of the skynet machines run gcc 4.5.0.



---

archive/issue_comments_092488.json:
```json
{
    "body": "(See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)",
    "created_at": "2010-07-24T18:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92488",
    "user": "https://github.com/jhpalmieri"
}
```

(See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)



---

archive/issue_comments_092489.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> (See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)\n\nSorry, missed that... :)",
    "created_at": "2010-07-24T18:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92489",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 jhpalmieri]:
> (See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet).)

Sorry, missed that... :)



---

archive/issue_comments_092490.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> Replying to [comment:11 jhpalmieri]:\n> > On cicero, I get the failure reported by John Cremona on sage-release:\n\n> <snip>\n> > Is there a separate ticket for this one?\n\n> \n> Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).\n> \n> Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.\n\n\nCarl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.",
    "created_at": "2010-07-24T20:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92490",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 leif]:
> Replying to [comment:11 jhpalmieri]:
> > On cicero, I get the failure reported by John Cremona on sage-release:

> <snip>
> > Is there a separate ticket for this one?

> 
> Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).
> 
> Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.


Carl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.



---

archive/issue_comments_092491.json:
```json
{
    "body": "I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.  On iras I ran it \"verbose\", and it stalled at this point:\n\n```\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)\nExpecting nothing\n```\nBut that command works fine from the command line, and I'm not flushing any buffers.  Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?",
    "created_at": "2010-07-24T20:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92491",
    "user": "https://github.com/jhpalmieri"
}
```

I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.  On iras I ran it "verbose", and it stalled at this point:

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
```
But that command works fine from the command line, and I'm not flushing any buffers.  Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?



---

archive/issue_comments_092492.json:
```json
{
    "body": "Attachment [TICKET_UNRELATED-ncadoctest-flush_output_in_verbose_mode-scripts_repo.patch](tarball://root/attachments/some-uuid/ticket9584/TICKET_UNRELATED-ncadoctest-flush_output_in_verbose_mode-scripts_repo.patch) by @nexttime created at 2010-07-24 20:28:38\n\nAs the name says... Apply to scripts repo.",
    "created_at": "2010-07-24T20:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92492",
    "user": "https://github.com/nexttime"
}
```

Attachment [TICKET_UNRELATED-ncadoctest-flush_output_in_verbose_mode-scripts_repo.patch](tarball://root/attachments/some-uuid/ticket9584/TICKET_UNRELATED-ncadoctest-flush_output_in_verbose_mode-scripts_repo.patch) by @nexttime created at 2010-07-24 20:28:38

As the name says... Apply to scripts repo.



---

archive/issue_comments_092493.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.\nWow... ;-) (Single test? Sysload?)\n\n> On iras I ran it \"verbose\", and it stalled at this point:\n\n{{{\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)\nExpecting nothing\n}}}\n> But that command works fine from the command line, and I'm not flushing any buffers.\n\nI don't think this is the point where it really starts hanging.\n\n> Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?\n\n\nIMO yes; I've uploaded a patch to `ncadoctest.py` (which I think could be merged into Sage anyway, since if at all it slows down only doctesting in verbose mode).\n\nBtw, you could look for Python and GAP orphans after the test has timed out. (GAP processes should be the children of the orphaned Python doctest process.)",
    "created_at": "2010-07-24T20:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92493",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 jhpalmieri]:
> I've set SAGE_TIMEOUT_LONG to 10000, and on both cleo and iras the test is still timing out.
Wow... ;-) (Single test? Sysload?)

> On iras I ran it "verbose", and it stalled at this point:

{{{
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
}}}
> But that command works fine from the command line, and I'm not flushing any buffers.

I don't think this is the point where it really starts hanging.

> Is it worth pursuing this further?  If so, how should I modify ncadoctest to flush buffers appropriately?


IMO yes; I've uploaded a patch to `ncadoctest.py` (which I think could be merged into Sage anyway, since if at all it slows down only doctesting in verbose mode).

Btw, you could look for Python and GAP orphans after the test has timed out. (GAP processes should be the children of the orphaned Python doctest process.)



---

archive/issue_comments_092494.json:
```json
{
    "body": "Changing keywords from \"\" to \"generic_graph, generic graph, time-out, time out\".",
    "created_at": "2010-07-24T20:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92494",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "generic_graph, generic graph, time-out, time out".



---

archive/issue_comments_092495.json:
```json
{
    "body": "schilly did **not** get time-outs on 32-bit Ubuntu 8.10 (gcc 4.3.2), with a **64-bit** CPU (Core2 quad) though...",
    "created_at": "2010-07-24T21:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92495",
    "user": "https://github.com/nexttime"
}
```

schilly did **not** get time-outs on 32-bit Ubuntu 8.10 (gcc 4.3.2), with a **64-bit** CPU (Core2 quad) though...



---

archive/issue_comments_092496.json:
```json
{
    "body": "I'm only seeing the timeout problem on cleo and iras, both itanium machines.  All of the other skynet linux machines finish doctesting in a sane amount of time.",
    "created_at": "2010-07-24T21:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92496",
    "user": "https://github.com/jhpalmieri"
}
```

I'm only seeing the timeout problem on cleo and iras, both itanium machines.  All of the other skynet linux machines finish doctesting in a sane amount of time.



---

archive/issue_comments_092497.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> Replying to [comment:12 leif]:\n> > Replying to [comment:11 jhpalmieri]:\n> > > On cicero, I get the failure reported by John Cremona on sage-release:\n\n> > <snip>\n> > > Is there a separate ticket for this one?\n\n\nI've now opened #9594 (as a 4.5.2 blocker) for the failing doctest.\n\n> > Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).\n> > \n> > Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.\n\n> \n> Carl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.\n\n\nCarl's ticket is intended to address reproducible spring layout in general, not the current doctest error.",
    "created_at": "2010-07-24T23:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92497",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:17 leif]:
> Replying to [comment:12 leif]:
> > Replying to [comment:11 jhpalmieri]:
> > > On cicero, I get the failure reported by John Cremona on sage-release:

> > <snip>
> > > Is there a separate ticket for this one?


I've now opened #9594 (as a 4.5.2 blocker) for the failing doctest.

> > Not that I know of; it's also in my [first comment above](http://trac.sagemath.org/sage_trac/ticket/9584#comment:1).
> > 
> > Should we split off one of the issues? The doctest failure is likely to get fixed quicker I think.

> 
> Carl Witty has opened #9593, which doesn't (yet) focus on the doctest error though, but seems to be adequate for fixing the numeric noise which causes it, too.


Carl's ticket is intended to address reproducible spring layout in general, not the current doctest error.



---

archive/issue_comments_092498.json:
```json
{
    "body": "John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?\n\nIf so, we should open yet another ticket for that one.",
    "created_at": "2010-07-24T23:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92498",
    "user": "https://github.com/nexttime"
}
```

John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?

If so, we should open yet another ticket for that one.



---

archive/issue_comments_092499.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?\n\n\nI'm seeing it now, while iras is also running the doctest on generic_graph.py.  Maybe it only pops up when the system is sufficiently loaded.",
    "created_at": "2010-07-24T23:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92499",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:25 leif]:
> John, did you face the funny doctest error in `sage/graphs/genus.pyx` again?


I'm seeing it now, while iras is also running the doctest on generic_graph.py.  Maybe it only pops up when the system is sufficiently loaded.



---

archive/issue_comments_092500.json:
```json
{
    "body": "Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):\n\n```\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)\nExpecting nothing\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [10000.8 s]\n```\niras is still going, but I expect it to behave the same way.",
    "created_at": "2010-07-25T01:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92500",
    "user": "https://github.com/jhpalmieri"
}
```

Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):

```
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [10000.8 s]
```
iras is still going, but I expect it to behave the same way.



---

archive/issue_comments_092501.json:
```json
{
    "body": "Replying to [comment:27 jhpalmieri]:\n> Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):\n\n{{{\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)\nExpecting nothing\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [10000.8 s]\n}}}\n\nI get exactly that far if I run the doctest file *\"manually\"* with `./sage -python ~/.sage/tmp/.doctest_generic_graph.py`, without the time-out messages of course. (The file itself looks ok to me.)",
    "created_at": "2010-07-25T01:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92501",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:27 jhpalmieri]:
> Here's cleo (verbose doctesting, version of ncadoctest which has been patched with the attached patch):

{{{
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k)###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k)
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
         [10000.8 s]
}}}

I get exactly that far if I run the doctest file *"manually"* with `./sage -python ~/.sage/tmp/.doctest_generic_graph.py`, without the time-out messages of course. (The file itself looks ok to me.)



---

archive/issue_comments_092502.json:
```json
{
    "body": "I'll leave it running for the moment, and wait if it ever terminates... ;-)\n\nWhile the GAP process sleeps (waiting for input), the Python process eagerly does *something*, I just wonder what.",
    "created_at": "2010-07-25T01:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92502",
    "user": "https://github.com/nexttime"
}
```

I'll leave it running for the moment, and wait if it ever terminates... ;-)

While the GAP process sleeps (waiting for input), the Python process eagerly does *something*, I just wonder what.



---

archive/issue_comments_092503.json:
```json
{
    "body": "I applied this patch on cleo and on iras:\n\n```diff\ndiff -r af5f40a73eda sage/graphs/generic_graph.py\n--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700\n+++ b/sage/graphs/generic_graph.py      Sun Jul 25 01:50:04 2010 -0400\n@@ -3424,14 +3424,6 @@\n         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint\n         arborescences, regardless of the root we pick::\n \n-            sage: g = digraphs.RandomDirectedGNP(30,.3)\n-            sage: k = Integer(g.edge_connectivity())\n-            sage: arborescences = g.edge_disjoint_spanning_trees(k)\n-            sage: all([a.is_directed_acyclic() for a in arborescences])\n-            True\n-            sage: all([a.is_connected() for a in arborescences])\n-            True            \n-\n         In the undirected case, we can only ensure half of it::\n \n             sage: g = graphs.RandomGNP(30,.3)\n```\nAfterwards, doctesting finished in under three minutes with one failure:\n\n```\nsage -t -long \"devel/sage/sage/graphs/generic_graph.py\"\n**********************************************************************\nFile \"/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py\", line 11573:\n    sage: G.get_pos()\nExpected:\n    {0: [1.17..., -0.855...],\n     1: [1.81..., -0.0990...],\n     2: [1.35..., 0.184...],\n     3: [1.51..., 0.644...],\n     4: [2.00..., -0.507...],\n     5: [0.597..., -0.236...],\n     6: [2.04..., 0.687...],\n     7: [1.46..., -0.473...],\n     8: [0.902..., 0.773...],\n     9: [2.48..., -0.119...]}\nGot:\n    {0: [1.1721936005708948, -0.85595703323182004], 1: [1.8124415978053314, -0.098957722760544126], 2: [1.3556834715997623, 0.18555735660955996], 3: [1.5071993658897154, 0.64583234825810909], 4: [2.0052086204051096, -0.50880746601197047], 5: [0.59719922887682242, -0.23674243624132649], 6: [2.0421969942849465, 0.68675223944817765], 7: [1.4629031375326151, -0.47198785673207005], 8: [0.90114500185020652, 0.77411663137336129], 9: [2.4857090090237808, -0.11980606071147699]}\n**********************************************************************\n```\n(Exactly the same failure on both machines.)\n\nCompletely deleting the doctests is too drastic, I think, but it certainly suggests where the problem lies.",
    "created_at": "2010-07-25T05:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92503",
    "user": "https://github.com/jhpalmieri"
}
```

I applied this patch on cleo and on iras:

```diff
diff -r af5f40a73eda sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700
+++ b/sage/graphs/generic_graph.py      Sun Jul 25 01:50:04 2010 -0400
@@ -3424,14 +3424,6 @@
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::
 
-            sage: g = digraphs.RandomDirectedGNP(30,.3)
-            sage: k = Integer(g.edge_connectivity())
-            sage: arborescences = g.edge_disjoint_spanning_trees(k)
-            sage: all([a.is_directed_acyclic() for a in arborescences])
-            True
-            sage: all([a.is_connected() for a in arborescences])
-            True            
-
         In the undirected case, we can only ensure half of it::
 
             sage: g = graphs.RandomGNP(30,.3)
```
Afterwards, doctesting finished in under three minutes with one failure:

```
sage -t -long "devel/sage/sage/graphs/generic_graph.py"
**********************************************************************
File "/home/palmieri/iras/sage-4.5.2.alpha0/devel/sage/sage/graphs/generic_graph.py", line 11573:
    sage: G.get_pos()
Expected:
    {0: [1.17..., -0.855...],
     1: [1.81..., -0.0990...],
     2: [1.35..., 0.184...],
     3: [1.51..., 0.644...],
     4: [2.00..., -0.507...],
     5: [0.597..., -0.236...],
     6: [2.04..., 0.687...],
     7: [1.46..., -0.473...],
     8: [0.902..., 0.773...],
     9: [2.48..., -0.119...]}
Got:
    {0: [1.1721936005708948, -0.85595703323182004], 1: [1.8124415978053314, -0.098957722760544126], 2: [1.3556834715997623, 0.18555735660955996], 3: [1.5071993658897154, 0.64583234825810909], 4: [2.0052086204051096, -0.50880746601197047], 5: [0.59719922887682242, -0.23674243624132649], 6: [2.0421969942849465, 0.68675223944817765], 7: [1.4629031375326151, -0.47198785673207005], 8: [0.90114500185020652, 0.77411663137336129], 9: [2.4857090090237808, -0.11980606071147699]}
**********************************************************************
```
(Exactly the same failure on both machines.)

Completely deleting the doctests is too drastic, I think, but it certainly suggests where the problem lies.



---

archive/issue_comments_092504.json:
```json
{
    "body": "Hmmmm.... :-/\n\nThen perhaps setting the number of vertices to 20 instead of 30 ? With CPLEX as a solver, this test is actually much faster, this may be why I originally put a 30 there, which may be too big for GLPK.\n\n```\nsage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())\nsage: %timeit T(digraphs.RandomDirectedGNP(30,.3))\n5 loops, best of 3: 6.03 s per loop\n```\n\n```\nsage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity(), solver= \"CPLEX\")\nsage: %timeit T(digraphs.RandomDirectedGNP(30,.3))\n5 loops, best of 3: 668 ms per loop\n```\n\nIn this case, though, we should increase the probability, lest we find non-strongly-connected graphs, but this still takes a lot of time \n\n```\n\nsage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())\nsage: %timeit T(digraphs.RandomDirectedGNP(20,.5))\n5 loops, best of 3: 4.52 s per loop\n```\n\nAs I still haven't found a way to write #7303, perhaps the following would be a good alternative :\n\nWe build a directed circulant graph on n vertices by linking the i th vertex to i+1, i+2, ... , i+k, thus ensuring our graph is k-connected. Then, by Edmond's theorem, we know this graph has `k` edge-disjoint spanning arborescences\n\n```\nsage: n = 20\nsage: k = 3\nsage: g = DiGraph()\nsage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1,k+1) )\nsage: k == g.edge_connectivity()\nTrue\nsage: arborescences = g.edge_disjoint_spanning_trees(k)\nsage: all([a.is_directed_acyclic() for a in arborescences])\nTrue\nsage: all([a.is_connected() for a in arborescences]) \nTrue\n``` \n\nIt is nicer now :\n\n```\nsage: %timeit g.edge_disjoint_spanning_trees(k)\n5 loops, best of 3: 283 ms per loop\n```\n\nPlus it is a bit \"cleaner\" without the random graphs in this case, methinks :-)\n\nSorry for the trouble !!!!!!!!!!!!!!!!!!\n\nNathann",
    "created_at": "2010-07-25T07:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92504",
    "user": "https://github.com/nathanncohen"
}
```

Hmmmm.... :-/

Then perhaps setting the number of vertices to 20 instead of 30 ? With CPLEX as a solver, this test is actually much faster, this may be why I originally put a 30 there, which may be too big for GLPK.

```
sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())
sage: %timeit T(digraphs.RandomDirectedGNP(30,.3))
5 loops, best of 3: 6.03 s per loop
```

```
sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity(), solver= "CPLEX")
sage: %timeit T(digraphs.RandomDirectedGNP(30,.3))
5 loops, best of 3: 668 ms per loop
```

In this case, though, we should increase the probability, lest we find non-strongly-connected graphs, but this still takes a lot of time 

```

sage:  T = lambda x: x.edge_disjoint_spanning_trees(x.edge_connectivity())
sage: %timeit T(digraphs.RandomDirectedGNP(20,.5))
5 loops, best of 3: 4.52 s per loop
```

As I still haven't found a way to write #7303, perhaps the following would be a good alternative :

We build a directed circulant graph on n vertices by linking the i th vertex to i+1, i+2, ... , i+k, thus ensuring our graph is k-connected. Then, by Edmond's theorem, we know this graph has `k` edge-disjoint spanning arborescences

```
sage: n = 20
sage: k = 3
sage: g = DiGraph()
sage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1,k+1) )
sage: k == g.edge_connectivity()
True
sage: arborescences = g.edge_disjoint_spanning_trees(k)
sage: all([a.is_directed_acyclic() for a in arborescences])
True
sage: all([a.is_connected() for a in arborescences]) 
True
``` 

It is nicer now :

```
sage: %timeit g.edge_disjoint_spanning_trees(k)
5 loops, best of 3: 283 ms per loop
```

Plus it is a bit "cleaner" without the random graphs in this case, methinks :-)

Sorry for the trouble !!!!!!!!!!!!!!!!!!

Nathann



---

archive/issue_comments_092505.json:
```json
{
    "body": "Well, I wouldn't mind if it only took very long... It simply *does not terminate* on some systems, i.e. there must be some bug in the underlying code that only shows up with specific CPU/compiler/OS constellations, but don't ask *me* which and why. ;-)",
    "created_at": "2010-07-25T07:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92505",
    "user": "https://github.com/nexttime"
}
```

Well, I wouldn't mind if it only took very long... It simply *does not terminate* on some systems, i.e. there must be some bug in the underlying code that only shows up with specific CPU/compiler/OS constellations, but don't ask *me* which and why. ;-)



---

archive/issue_comments_092506.json:
```json
{
    "body": "Oh. Actually, I do not know what Sage is doing during the doctests. The \"timeit\" method may say it only takes 6 seconds, but if you type the commands I gave you will wait much, much longer to get the answer (and not only 5 times this -- the number of loop). Is it really computer-specific ? There is still the probability that the given graph is not strongly connected, but it should be *veeeeeeeery* low !!!\n\nNathann",
    "created_at": "2010-07-25T08:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92506",
    "user": "https://github.com/nathanncohen"
}
```

Oh. Actually, I do not know what Sage is doing during the doctests. The "timeit" method may say it only takes 6 seconds, but if you type the commands I gave you will wait much, much longer to get the answer (and not only 5 times this -- the number of loop). Is it really computer-specific ? There is still the probability that the given graph is not strongly connected, but it should be *veeeeeeeery* low !!!

Nathann



---

archive/issue_comments_092507.json:
```json
{
    "body": "Hi Nathann,\n\n> Sorry for the trouble !!!!!!!!!!!!!!!!!!\n\n\nI cc'ed you on the ticket not because I thought you caused trouble, but because I knew you had worked on the file and could suggest ways to fix it.\n\nSo are you suggesting this patch?  It seems to work for me.\n\n```diff\ndiff -r af5f40a73eda sage/graphs/generic_graph.py\n--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700\n+++ b/sage/graphs/generic_graph.py      Sun Jul 25 10:53:22 2010 -0400\n@@ -3424,13 +3424,17 @@\n         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint\n         arborescences, regardless of the root we pick::\n\n-            sage: g = digraphs.RandomDirectedGNP(30,.3)\n-            sage: k = Integer(g.edge_connectivity())\n+            sage: n = 20\n+            sage: k = 3\n+            sage: g = DiGraph()\n+            sage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1\n,k+1))\n+            sage: k == g.edge_connectivity()\n+            True\n             sage: arborescences = g.edge_disjoint_spanning_trees(k)\n             sage: all([a.is_directed_acyclic() for a in arborescences])\n             True\n             sage: all([a.is_connected() for a in arborescences])\n-            True\n+            True\n\n         In the undirected case, we can only ensure half of it::\n```",
    "created_at": "2010-07-25T14:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92507",
    "user": "https://github.com/jhpalmieri"
}
```

Hi Nathann,

> Sorry for the trouble !!!!!!!!!!!!!!!!!!


I cc'ed you on the ticket not because I thought you caused trouble, but because I knew you had worked on the file and could suggest ways to fix it.

So are you suggesting this patch?  It seems to work for me.

```diff
diff -r af5f40a73eda sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py      Wed Jul 21 20:13:55 2010 -0700
+++ b/sage/graphs/generic_graph.py      Sun Jul 25 10:53:22 2010 -0400
@@ -3424,13 +3424,17 @@
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::

-            sage: g = digraphs.RandomDirectedGNP(30,.3)
-            sage: k = Integer(g.edge_connectivity())
+            sage: n = 20
+            sage: k = 3
+            sage: g = DiGraph()
+            sage: g.add_edges( (Integer(i),Integer(Mod(i+j,n))) for i in range(n) for j in range(1
,k+1))
+            sage: k == g.edge_connectivity()
+            True
             sage: arborescences = g.edge_disjoint_spanning_trees(k)
             sage: all([a.is_directed_acyclic() for a in arborescences])
             True
             sage: all([a.is_connected() for a in arborescences])
-            True
+            True

         In the undirected case, we can only ensure half of it::
```



---

archive/issue_comments_092508.json:
```json
{
    "body": "With this patch, does the docstring still make sense as a whole?  That is, does the new doctest fit with the ones before and after?",
    "created_at": "2010-07-25T15:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92508",
    "user": "https://github.com/jhpalmieri"
}
```

With this patch, does the docstring still make sense as a whole?  That is, does the new doctest fit with the ones before and after?



---

archive/issue_comments_092509.json:
```json
{
    "body": "The following works *for me*:\n\n```patch\ndiff --git a/sage/graphs/generic_graph.py b/sage/graphs/generic_graph.py\n--- a/sage/graphs/generic_graph.py\n+++ b/sage/graphs/generic_graph.py\n@@ -3424,7 +3424,7 @@\n         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint\n         arborescences, regardless of the root we pick::\n \n-            sage: g = digraphs.RandomDirectedGNP(30,.3)\n+            sage: g = digraphs.RandomDirectedGNP(28,.3) # reduced from 30, cf. #9584\n             sage: k = Integer(g.edge_connectivity())\n             sage: arborescences = g.edge_disjoint_spanning_trees(k)\n             sage: all([a.is_directed_acyclic() for a in arborescences])\n```\nSo I've simply changed the size of the random graph, not the doctest in principle. Someone should look at the code though, since it seems to run into an infinite loop under some circumstances. (I also tried 20, 25, 27 and 29; the latter again did not terminate; I've not yet tried *larger* values, which *might* work as well...)\n\nWith the above change (and the patch at #9594), all doctests pass in reasonable time:\n\n```sh\nleif@californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t devel/sage/sage/graphs/      \nsage -t  \"devel/sage/sage/graphs/digraph_generators.py\"     \n\t [13.8 s]\nsage -t  \"devel/sage/sage/graphs/cliquer.pyx\"               \n\t [3.5 s]\n...\nsage -t  \"devel/sage/sage/graphs/graph_coloring.py\"         \n\t [18.4 s]\nsage -t  \"devel/sage/sage/graphs/bipartite_graph.py\"        \n\t [7.5 s]\nsage -t  \"devel/sage/sage/graphs/digraph.py\"                \n\t [9.8 s]\nsage -t  \"devel/sage/sage/graphs/chrompoly.pyx\"             \n\t [13.4 s]\nsage -t  \"devel/sage/sage/graphs/graph_generators.py\"       \n\t [87.4 s]\nsage -t  \"devel/sage/sage/graphs/generic_graph.py\"          \n\t [72.1 s]\nsage -t  \"devel/sage/sage/graphs/trees.pyx\"                 \n\t [10.9 s]\n...\nsage -t  \"devel/sage/sage/graphs/dot2tex_utils.py\"          \n\t [3.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 383.5 seconds\n\nreal\t6m23.599s\nuser\t6m2.251s\nsys\t0m18.253s\nleif@californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t -long devel/sage/sage/graphs/\nsage -t -long \"devel/sage/sage/graphs/digraph_generators.py\"\n\t [22.5 s]\nsage -t -long \"devel/sage/sage/graphs/cliquer.pyx\"          \n\t [3.5 s]\n...\nsage -t -long \"devel/sage/sage/graphs/graph_coloring.py\"    \n\t [18.4 s]\nsage -t -long \"devel/sage/sage/graphs/bipartite_graph.py\"   \n\t [7.5 s]\nsage -t -long \"devel/sage/sage/graphs/digraph.py\"           \n\t [9.8 s]\nsage -t -long \"devel/sage/sage/graphs/chrompoly.pyx\"        \n\t [13.4 s]\nsage -t -long \"devel/sage/sage/graphs/graph_generators.py\"  \n\t [228.7 s]\nsage -t -long \"devel/sage/sage/graphs/generic_graph.py\"     \n\t [148.5 s]\nsage -t -long \"devel/sage/sage/graphs/trees.pyx\"            \n\t [10.8 s]\n...\nsage -t -long \"devel/sage/sage/graphs/genus.pyx\"            \n\t [49.3 s]\nsage -t -long \"devel/sage/sage/graphs/graph_database.py\"    \n\t [3.4 s]\nsage -t -long \"devel/sage/sage/graphs/dot2tex_utils.py\"     \n\t [3.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 655.7 seconds\n\nreal\t10m55.784s\nuser\t10m55.949s\nsys\t0m19.829s\n```\n(Pentium 4 Prescott 3.2GHz)\n\nI've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...",
    "created_at": "2010-07-25T18:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92509",
    "user": "https://github.com/nexttime"
}
```

The following works *for me*:

```patch
diff --git a/sage/graphs/generic_graph.py b/sage/graphs/generic_graph.py
--- a/sage/graphs/generic_graph.py
+++ b/sage/graphs/generic_graph.py
@@ -3424,7 +3424,7 @@
         By Edmond's theorem, a graph which is `k`-connected always has `k` edge-disjoint
         arborescences, regardless of the root we pick::
 
-            sage: g = digraphs.RandomDirectedGNP(30,.3)
+            sage: g = digraphs.RandomDirectedGNP(28,.3) # reduced from 30, cf. #9584
             sage: k = Integer(g.edge_connectivity())
             sage: arborescences = g.edge_disjoint_spanning_trees(k)
             sage: all([a.is_directed_acyclic() for a in arborescences])
```
So I've simply changed the size of the random graph, not the doctest in principle. Someone should look at the code though, since it seems to run into an infinite loop under some circumstances. (I also tried 20, 25, 27 and 29; the latter again did not terminate; I've not yet tried *larger* values, which *might* work as well...)

With the above change (and the patch at #9594), all doctests pass in reasonable time:

```sh
leif@californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t devel/sage/sage/graphs/      
sage -t  "devel/sage/sage/graphs/digraph_generators.py"     
	 [13.8 s]
sage -t  "devel/sage/sage/graphs/cliquer.pyx"               
	 [3.5 s]
...
sage -t  "devel/sage/sage/graphs/graph_coloring.py"         
	 [18.4 s]
sage -t  "devel/sage/sage/graphs/bipartite_graph.py"        
	 [7.5 s]
sage -t  "devel/sage/sage/graphs/digraph.py"                
	 [9.8 s]
sage -t  "devel/sage/sage/graphs/chrompoly.pyx"             
	 [13.4 s]
sage -t  "devel/sage/sage/graphs/graph_generators.py"       
	 [87.4 s]
sage -t  "devel/sage/sage/graphs/generic_graph.py"          
	 [72.1 s]
sage -t  "devel/sage/sage/graphs/trees.pyx"                 
	 [10.9 s]
...
sage -t  "devel/sage/sage/graphs/dot2tex_utils.py"          
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 383.5 seconds

real	6m23.599s
user	6m2.251s
sys	0m18.253s
leif@californication:~/sage-4.5.2.alpha0-j6$ time ./sage -t -long devel/sage/sage/graphs/
sage -t -long "devel/sage/sage/graphs/digraph_generators.py"
	 [22.5 s]
sage -t -long "devel/sage/sage/graphs/cliquer.pyx"          
	 [3.5 s]
...
sage -t -long "devel/sage/sage/graphs/graph_coloring.py"    
	 [18.4 s]
sage -t -long "devel/sage/sage/graphs/bipartite_graph.py"   
	 [7.5 s]
sage -t -long "devel/sage/sage/graphs/digraph.py"           
	 [9.8 s]
sage -t -long "devel/sage/sage/graphs/chrompoly.pyx"        
	 [13.4 s]
sage -t -long "devel/sage/sage/graphs/graph_generators.py"  
	 [228.7 s]
sage -t -long "devel/sage/sage/graphs/generic_graph.py"     
	 [148.5 s]
sage -t -long "devel/sage/sage/graphs/trees.pyx"            
	 [10.8 s]
...
sage -t -long "devel/sage/sage/graphs/genus.pyx"            
	 [49.3 s]
sage -t -long "devel/sage/sage/graphs/graph_database.py"    
	 [3.4 s]
sage -t -long "devel/sage/sage/graphs/dot2tex_utils.py"     
	 [3.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 655.7 seconds

real	10m55.784s
user	10m55.949s
sys	0m19.829s
```
(Pentium 4 Prescott 3.2GHz)

I've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...



---

archive/issue_comments_092510.json:
```json
{
    "body": "Using `g = digraphs.RandomDirectedGNP(28,.3)` works for me too: doctesting generic_graph.py finishes in under 180 seconds on both cleo and iras.  Maybe the problem is indeed that 30 vertices is too many for GLPK, as ncohen suggested.\n\nI'm more or less happy with this patch: it doesn't change the doctests in any qualitative way, so it isn't very intrusive.  The only problem is that we still don't know what the underlying issue is.  CPLEX is not installed on any skynet machine as far as I can tell, so I have no way of testing whether it might work in this case.  So how should we proceed?",
    "created_at": "2010-07-25T19:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92510",
    "user": "https://github.com/jhpalmieri"
}
```

Using `g = digraphs.RandomDirectedGNP(28,.3)` works for me too: doctesting generic_graph.py finishes in under 180 seconds on both cleo and iras.  Maybe the problem is indeed that 30 vertices is too many for GLPK, as ncohen suggested.

I'm more or less happy with this patch: it doesn't change the doctests in any qualitative way, so it isn't very intrusive.  The only problem is that we still don't know what the underlying issue is.  CPLEX is not installed on any skynet machine as far as I can tell, so I have no way of testing whether it might work in this case.  So how should we proceed?



---

archive/issue_comments_092511.json:
```json
{
    "body": "Replying to [comment:36 leif]:\n> I've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...\n\n\nFunny, that machine has just passed `generic_graph.py` in 281 seconds, with only the `get_pos()` graph layout doctest error (#9594). (I'm testing vanilla 4.5.2.alpha0 first.)",
    "created_at": "2010-07-25T22:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92511",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:36 leif]:
> I've also built Sage 4.5.2.alpha0 on an older Pentium 4 (Northwood, 2.66GHz; only 768MB RAM, Ubuntu 7.10 x86 with rebuilt gcc/g++/gfortran 4.2.1, new gmp and mpfr); `make testlong` is still running...


Funny, that machine has just passed `generic_graph.py` in 281 seconds, with only the `get_pos()` graph layout doctest error (#9594). (I'm testing vanilla 4.5.2.alpha0 first.)



---

archive/issue_comments_092512.json:
```json
{
    "body": "Just for the record: I've verified that the random graph is exactly the same on the 32-bit system (where `edge_disjoint_spanning_trees()` does not terminate).",
    "created_at": "2010-07-26T20:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92512",
    "user": "https://github.com/nexttime"
}
```

Just for the record: I've verified that the random graph is exactly the same on the 32-bit system (where `edge_disjoint_spanning_trees()` does not terminate).



---

archive/issue_comments_092513.json:
```json
{
    "body": "Attachment [trac_9584-generic_graph.patch](tarball://root/attachments/some-uuid/ticket9584/trac_9584-generic_graph.patch) by @jhpalmieri created at 2010-07-26 20:58:16",
    "created_at": "2010-07-26T20:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92513",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9584-generic_graph.patch](tarball://root/attachments/some-uuid/ticket9584/trac_9584-generic_graph.patch) by @jhpalmieri created at 2010-07-26 20:58:16



---

archive/issue_comments_092514.json:
```json
{
    "body": "Here's Leif's patch, which I will review positively.",
    "created_at": "2010-07-26T20:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92514",
    "user": "https://github.com/jhpalmieri"
}
```

Here's Leif's patch, which I will review positively.



---

archive/issue_comments_092515.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-26T20:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92515",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092516.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-26T20:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92516",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092517.json:
```json
{
    "body": "Well, this is just an ugly work-around to make the doctest pass, so we should (change the ticket's title and) address the cause on another one...",
    "created_at": "2010-07-26T21:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92517",
    "user": "https://github.com/nexttime"
}
```

Well, this is just an ugly work-around to make the doctest pass, so we should (change the ticket's title and) address the cause on another one...



---

archive/issue_comments_092518.json:
```json
{
    "body": "On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.  So a work-around seems like an acceptable solution right now.\n\nHave you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.",
    "created_at": "2010-07-26T21:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92518",
    "user": "https://github.com/jhpalmieri"
}
```

On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.  So a work-around seems like an acceptable solution right now.

Have you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.



---

archive/issue_comments_092519.json:
```json
{
    "body": "Replying to [comment:43 jhpalmieri]:\n> On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.\n\n\nNothing is out of my control... ;-)\n\nI mean we should try to find the reason. If it's outside of Sage, fine, and we can at least document it, whether it lies in GLPK or some OS/compiler specifics.\n\nAnd the \"failing\" doctest, i.e. the behavior after timing out, in addition shows (again) that something's wrong with the doctesting framework, to also be addressed on another ticket.\n\n> So a work-around seems like an acceptable solution right now.\n\n\nI'm ok with merging this work-around at this moment.\n\n \n> Have you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.\n\n\nNot yet, currently trying to track this issue (with 30 vertices) further down.\n\nPlease cc me if anyone opens a follow-up.",
    "created_at": "2010-07-26T22:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92519",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:43 jhpalmieri]:
> On the one hand, that's true.  On the other, we were only hitting this problem on one or two platforms.  So it might be a bug in some component of Sage (like GLPK?), but it might be something out of our control entirely.


Nothing is out of my control... ;-)

I mean we should try to find the reason. If it's outside of Sage, fine, and we can at least document it, whether it lies in GLPK or some OS/compiler specifics.

And the "failing" doctest, i.e. the behavior after timing out, in addition shows (again) that something's wrong with the doctesting framework, to also be addressed on another ticket.

> So a work-around seems like an acceptable solution right now.


I'm ok with merging this work-around at this moment.

 
> Have you tried setting the number of vertices higher on other machines, to try to replicate the issue elsewhere?  I just tried with 40 instead of 30 on sage.math, and it worked just fine.  50 vertices took a while, but it finished, too.


Not yet, currently trying to track this issue (with 30 vertices) further down.

Please cc me if anyone opens a follow-up.



---

archive/issue_comments_092520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-27T00:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92520",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_events_023865.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-27T00:42:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9584#event-23865"
}
```



---

archive/issue_comments_092521.json:
```json
{
    "body": "Merged trac_9584-generic_graph.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-27T00:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92521",
    "user": "https://github.com/dandrake"
}
```

Merged trac_9584-generic_graph.patch in 4.5.2.alpha1.



---

archive/issue_comments_092522.json:
```json
{
    "body": "Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add \"verbosity = 2\" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)\n\nNathann",
    "created_at": "2010-07-27T00:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92522",
    "user": "https://github.com/nathanncohen"
}
```

Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add "verbosity = 2" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)

Nathann



---

archive/issue_comments_092523.json:
```json
{
    "body": "Replying to [comment:46 ncohen]:\n> Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add \"verbosity = 2\" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)\n\n\nLOL, I'm currently hacking it, with `log=3`... (and trying to write out MPS files to test on the other machine, but two of them seem to be invalid?!)",
    "created_at": "2010-07-27T00:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92523",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:46 ncohen]:
> Oh, by the way : when you are trying to work on long linear programs like this one, you may find useful too add "verbosity = 2" or higher to the edge_disjoint_spanning_trees method. It will give you some idea of what GLPK is doing :-)


LOL, I'm currently hacking it, with `log=3`... (and trying to write out MPS files to test on the other machine, but two of them seem to be invalid?!)



---

archive/issue_comments_092524.json:
```json
{
    "body": "Nathann, do you open a new ticket?",
    "created_at": "2010-07-27T00:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92524",
    "user": "https://github.com/nexttime"
}
```

Nathann, do you open a new ticket?



---

archive/issue_comments_092525.json:
```json
{
    "body": "> Nathann, do you open a new ticket?\n\nWell, I've never been able to produce this error on my computer actually ... :-/\n\nThis being said, if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way : to solve it, Sage first feeds it to GLPK using method A, then calls \"solve\". To export it, Sage first feeds it to GLPK using method A, then calls the export method from GLPK.\n\nSo if the files are invalid, that's a very bad news indeed !!\n\nNathann",
    "created_at": "2010-07-27T00:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92525",
    "user": "https://github.com/nathanncohen"
}
```

> Nathann, do you open a new ticket?

Well, I've never been able to produce this error on my computer actually ... :-/

This being said, if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way : to solve it, Sage first feeds it to GLPK using method A, then calls "solve". To export it, Sage first feeds it to GLPK using method A, then calls the export method from GLPK.

So if the files are invalid, that's a very bad news indeed !!

Nathann



---

archive/issue_comments_092526.json:
```json
{
    "body": "Replying to [comment:49 ncohen]:\n> [...] if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way [...]\n\n\nWell, Sage does not run `glpsol` on a generated file, but uses the library interface, so there's a slight difference, and: names are only set when calling `write_mps()` or `write_lp()` - which goes wrong somehow in at least two cases. (I'm calling both `p.write_mps()` and `p.write_lp()` right before `p.solve()` in `GenericGraph.edge_disjoint_spanning_trees()`, and afterwards run `glpsol (--freemps|--lp)` on those files.)\n\n```\n$ local/bin/glpsol --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps\nGLPSOL: GLPK LP/MIP Solver, v4.44\nParameter(s) specified in the command line:\n --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps\nReading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.mps'...\n../trac_9584-edge_disjoint_spanning_trees-5.mps:8: warning: missing model name in field 3\nObjective: R0000000\n../trac_9584-edge_disjoint_spanning_trees-5.mps:1735: duplicate coefficient in row `R0000001'\nMPS file processing error\n$ local/bin/glpsol --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp\nGLPSOL: GLPK LP/MIP Solver, v4.44\nParameter(s) specified in the command line:\n --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp\nReading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.lp'...\n../trac_9584-edge_disjoint_spanning_trees-5.lp:7: multiple use of variable `V0(None)((0,_1))' not allowed\nCPLEX LP file processing error\n```\n\n\n> So if the files are invalid, that's a very bad news indeed !!\n\n\nIndeed, though the GLPK *library* works on th 64-bit system. On the 32-bit system where the doctest did not terminate, it's actually the solver that runs \"forever\" (trying to find a solution) - I do not yet know why... :(",
    "created_at": "2010-07-27T03:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92526",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:49 ncohen]:
> [...] if Sage is exporting invalid linear programs, that's a very bad news, as it does it using GLPK. So if the problem stored in the file is invalid, then the problem solved by GLPK should be too, as they behave the same way [...]


Well, Sage does not run `glpsol` on a generated file, but uses the library interface, so there's a slight difference, and: names are only set when calling `write_mps()` or `write_lp()` - which goes wrong somehow in at least two cases. (I'm calling both `p.write_mps()` and `p.write_lp()` right before `p.solve()` in `GenericGraph.edge_disjoint_spanning_trees()`, and afterwards run `glpsol (--freemps|--lp)` on those files.)

```
$ local/bin/glpsol --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --freemps ../trac_9584-edge_disjoint_spanning_trees-5.mps
Reading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.mps'...
../trac_9584-edge_disjoint_spanning_trees-5.mps:8: warning: missing model name in field 3
Objective: R0000000
../trac_9584-edge_disjoint_spanning_trees-5.mps:1735: duplicate coefficient in row `R0000001'
MPS file processing error
$ local/bin/glpsol --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --lp ../trac_9584-edge_disjoint_spanning_trees-5.lp
Reading problem data from `../trac_9584-edge_disjoint_spanning_trees-5.lp'...
../trac_9584-edge_disjoint_spanning_trees-5.lp:7: multiple use of variable `V0(None)((0,_1))' not allowed
CPLEX LP file processing error
```


> So if the files are invalid, that's a very bad news indeed !!


Indeed, though the GLPK *library* works on th 64-bit system. On the 32-bit system where the doctest did not terminate, it's actually the solver that runs "forever" (trying to find a solution) - I do not yet know why... :(



---

archive/issue_comments_092527.json:
```json
{
    "body": "If I run the doctest on iras with \"sage -t -verbose\" and with the argument \"log=3\", I get this:\n\n```\n\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k, log=Integer(3))###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k, log=3)\nExpecting nothing\nGLPK Integer Optimizer, v4.44\n1719 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\nPreprocessing...\n1670 rows, 3605 columns, 9790 non-zeros\n1325 integer variables, all of which are binary\nScaling...\n A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00\nProblem data seem to be well scaled\nConstructing initial basis...\nSize of triangular part = 1670\nSolving LP relaxation...\nGLPK Simplex Optimizer, v4.44\n1670 rows, 3605 columns, 9790 non-zeros\n      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)\n   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)\n*  1589: obj =   0.000000000e+00  infeas =  0.000e+00 (0)\nOPTIMAL SOLUTION FOUND\nInteger optimization begins...\n+  1589: mip =     not found yet <=              +inf        (1; 0)\n+  3341: mip =     not found yet <=   0.000000000e+00        (12; 0)\n+  4583: mip =     not found yet <=   0.000000000e+00        (25; 0)\n+  5915: mip =     not found yet <=   0.000000000e+00        (39; 0)\n+  7295: mip =     not found yet <=   0.000000000e+00        (53; 0)\n+  9064: mip =     not found yet <=   0.000000000e+00        (68; 0)\n+ 10470: mip =     not found yet <=   0.000000000e+00        (86; 0)\n+ 12453: mip =     not found yet <=   0.000000000e+00        (104; 0)\n+ 15172: mip =     not found yet <=   0.000000000e+00        (122; 0)\n+ 19359: mip =     not found yet <=   0.000000000e+00        (143; 1)\n+ 25674: mip =     not found yet <=   0.000000000e+00        (147; 19)\n+ 30995: mip =     not found yet <=   0.000000000e+00        (156; 40)\nTime used: 60.0 secs.  Memory used: 4.5 Mb.\n+ 36038: mip =     not found yet <=   0.000000000e+00        (178; 73)\n+ 41514: mip =     not found yet <=   0.000000000e+00        (188; 126)\n+ 45778: mip =     not found yet <=   0.000000000e+00        (213; 179)\n+ 51616: mip =     not found yet <=   0.000000000e+00        (232; 244)\n+ 56429: mip =     not found yet <=   0.000000000e+00        (215; 395)\n+ 61588: mip =     not found yet <=   0.000000000e+00        (220; 483)\n+ 66918: mip =     not found yet <=   0.000000000e+00        (219; 610)\n+ 71927: mip =     not found yet <=   0.000000000e+00        (225; 691)\n+ 77942: mip =     not found yet <=   0.000000000e+00        (218; 802)\n+ 82716: mip =     not found yet <=   0.000000000e+00        (219; 910)\n+ 87340: mip =     not found yet <=   0.000000000e+00        (216; 1034)\n+ 92302: mip =     not found yet <=   0.000000000e+00        (215; 1149)\nTime used: 120.0 secs.  Memory used: 5.1 Mb.\n+ 98199: mip =     not found yet <=   0.000000000e+00        (216; 1267)\n+103543: mip =     not found yet <=   0.000000000e+00        (209; 1380)\n+109695: mip =     not found yet <=   0.000000000e+00        (205; 1475)\n+115375: mip =     not found yet <=   0.000000000e+00        (194; 1626)\n+120734: mip =     not found yet <=   0.000000000e+00        (191; 1775)\n+126850: mip =     not found yet <=   0.000000000e+00        (192; 1890)\n+132308: mip =     not found yet <=   0.000000000e+00        (195; 1994)\n+137437: mip =     not found yet <=   0.000000000e+00        (200; 2119)\n+142222: mip =     not found yet <=   0.000000000e+00        (185; 2285)\n+147918: mip =     not found yet <=   0.000000000e+00        (194; 2358)\n+152167: mip =     not found yet <=   0.000000000e+00        (211; 2444)\n+157139: mip =     not found yet <=   0.000000000e+00        (188; 2631)\nTime used: 180.0 secs.  Memory used: 5.2 Mb.\n+162974: mip =     not found yet <=   0.000000000e+00        (194; 2717)\n+167746: mip =     not found yet <=   0.000000000e+00        (185; 2875)\n+173860: mip =     not found yet <=   0.000000000e+00        (189; 2945)\n+179993: mip =     not found yet <=   0.000000000e+00        (185; 3036)\n+184852: mip =     not found yet <=   0.000000000e+00        (186; 3167)\n+190815: mip =     not found yet <=   0.000000000e+00        (184; 3260)\n+195443: mip =     not found yet <=   0.000000000e+00        (191; 3340)\n+200019: mip =     not found yet <=   0.000000000e+00        (199; 3441)\n+205299: mip =     not found yet <=   0.000000000e+00        (193; 3550)\n+211558: mip =     not found yet <=   0.000000000e+00        (190; 3643)\n+217128: mip =     not found yet <=   0.000000000e+00        (205; 3721)\n+222749: mip =     not found yet <=   0.000000000e+00        (193; 3851)\nTime used: 240.1 secs.  Memory used: 5.2 Mb.\n+228284: mip =     not found yet <=   0.000000000e+00        (192; 3966)\n+234369: mip =     not found yet <=   0.000000000e+00        (187; 4068)\n+239753: mip =     not found yet <=   0.000000000e+00        (186; 4177)\n+245044: mip =     not found yet <=   0.000000000e+00        (203; 4260)\n+251418: mip =     not found yet <=   0.000000000e+00        (191; 4393)\n+257305: mip =     not found yet <=   0.000000000e+00        (184; 4511)\n+262969: mip =     not found yet <=   0.000000000e+00        (192; 4590)\n+268135: mip =     not found yet <=   0.000000000e+00        (187; 4714)\n+274100: mip =     not found yet <=   0.000000000e+00        (192; 4792)\n+279175: mip =     not found yet <=   0.000000000e+00        (185; 4929)\n+285635: mip =     not found yet <=   0.000000000e+00        (177; 5033)\n+291442: mip =     not found yet <=   0.000000000e+00        (189; 5090)\nTime used: 300.1 secs.  Memory used: 5.2 Mb.\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n```\nIncreasing the timeout threshold just lets this continue longer.",
    "created_at": "2010-07-27T03:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92527",
    "user": "https://github.com/jhpalmieri"
}
```

If I run the doctest on iras with "sage -t -verbose" and with the argument "log=3", I get this:

```

Trying:
    arborescences = g.edge_disjoint_spanning_trees(k, log=Integer(3))###line 3429:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k, log=3)
Expecting nothing
GLPK Integer Optimizer, v4.44
1719 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet <=              +inf        (1; 0)
+  3341: mip =     not found yet <=   0.000000000e+00        (12; 0)
+  4583: mip =     not found yet <=   0.000000000e+00        (25; 0)
+  5915: mip =     not found yet <=   0.000000000e+00        (39; 0)
+  7295: mip =     not found yet <=   0.000000000e+00        (53; 0)
+  9064: mip =     not found yet <=   0.000000000e+00        (68; 0)
+ 10470: mip =     not found yet <=   0.000000000e+00        (86; 0)
+ 12453: mip =     not found yet <=   0.000000000e+00        (104; 0)
+ 15172: mip =     not found yet <=   0.000000000e+00        (122; 0)
+ 19359: mip =     not found yet <=   0.000000000e+00        (143; 1)
+ 25674: mip =     not found yet <=   0.000000000e+00        (147; 19)
+ 30995: mip =     not found yet <=   0.000000000e+00        (156; 40)
Time used: 60.0 secs.  Memory used: 4.5 Mb.
+ 36038: mip =     not found yet <=   0.000000000e+00        (178; 73)
+ 41514: mip =     not found yet <=   0.000000000e+00        (188; 126)
+ 45778: mip =     not found yet <=   0.000000000e+00        (213; 179)
+ 51616: mip =     not found yet <=   0.000000000e+00        (232; 244)
+ 56429: mip =     not found yet <=   0.000000000e+00        (215; 395)
+ 61588: mip =     not found yet <=   0.000000000e+00        (220; 483)
+ 66918: mip =     not found yet <=   0.000000000e+00        (219; 610)
+ 71927: mip =     not found yet <=   0.000000000e+00        (225; 691)
+ 77942: mip =     not found yet <=   0.000000000e+00        (218; 802)
+ 82716: mip =     not found yet <=   0.000000000e+00        (219; 910)
+ 87340: mip =     not found yet <=   0.000000000e+00        (216; 1034)
+ 92302: mip =     not found yet <=   0.000000000e+00        (215; 1149)
Time used: 120.0 secs.  Memory used: 5.1 Mb.
+ 98199: mip =     not found yet <=   0.000000000e+00        (216; 1267)
+103543: mip =     not found yet <=   0.000000000e+00        (209; 1380)
+109695: mip =     not found yet <=   0.000000000e+00        (205; 1475)
+115375: mip =     not found yet <=   0.000000000e+00        (194; 1626)
+120734: mip =     not found yet <=   0.000000000e+00        (191; 1775)
+126850: mip =     not found yet <=   0.000000000e+00        (192; 1890)
+132308: mip =     not found yet <=   0.000000000e+00        (195; 1994)
+137437: mip =     not found yet <=   0.000000000e+00        (200; 2119)
+142222: mip =     not found yet <=   0.000000000e+00        (185; 2285)
+147918: mip =     not found yet <=   0.000000000e+00        (194; 2358)
+152167: mip =     not found yet <=   0.000000000e+00        (211; 2444)
+157139: mip =     not found yet <=   0.000000000e+00        (188; 2631)
Time used: 180.0 secs.  Memory used: 5.2 Mb.
+162974: mip =     not found yet <=   0.000000000e+00        (194; 2717)
+167746: mip =     not found yet <=   0.000000000e+00        (185; 2875)
+173860: mip =     not found yet <=   0.000000000e+00        (189; 2945)
+179993: mip =     not found yet <=   0.000000000e+00        (185; 3036)
+184852: mip =     not found yet <=   0.000000000e+00        (186; 3167)
+190815: mip =     not found yet <=   0.000000000e+00        (184; 3260)
+195443: mip =     not found yet <=   0.000000000e+00        (191; 3340)
+200019: mip =     not found yet <=   0.000000000e+00        (199; 3441)
+205299: mip =     not found yet <=   0.000000000e+00        (193; 3550)
+211558: mip =     not found yet <=   0.000000000e+00        (190; 3643)
+217128: mip =     not found yet <=   0.000000000e+00        (205; 3721)
+222749: mip =     not found yet <=   0.000000000e+00        (193; 3851)
Time used: 240.1 secs.  Memory used: 5.2 Mb.
+228284: mip =     not found yet <=   0.000000000e+00        (192; 3966)
+234369: mip =     not found yet <=   0.000000000e+00        (187; 4068)
+239753: mip =     not found yet <=   0.000000000e+00        (186; 4177)
+245044: mip =     not found yet <=   0.000000000e+00        (203; 4260)
+251418: mip =     not found yet <=   0.000000000e+00        (191; 4393)
+257305: mip =     not found yet <=   0.000000000e+00        (184; 4511)
+262969: mip =     not found yet <=   0.000000000e+00        (192; 4590)
+268135: mip =     not found yet <=   0.000000000e+00        (187; 4714)
+274100: mip =     not found yet <=   0.000000000e+00        (192; 4792)
+279175: mip =     not found yet <=   0.000000000e+00        (185; 4929)
+285635: mip =     not found yet <=   0.000000000e+00        (177; 5033)
+291442: mip =     not found yet <=   0.000000000e+00        (189; 5090)
Time used: 300.1 secs.  Memory used: 5.2 Mb.
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
```
Increasing the timeout threshold just lets this continue longer.



---

archive/issue_comments_092528.json:
```json
{
    "body": "Replying to [comment:51 jhpalmieri]:\n> Increasing the timeout threshold just lets this continue longer.\n\n\nI'm at 9500s+ and it keeps writing to the screen, though `sage -t ...` has already terminated... :D",
    "created_at": "2010-07-27T04:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92528",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:51 jhpalmieri]:
> Increasing the timeout threshold just lets this continue longer.


I'm at 9500s+ and it keeps writing to the screen, though `sage -t ...` has already terminated... :D



---

archive/issue_comments_092529.json:
```json
{
    "body": "Well, it is not a surprise that such LP can run for a long time... Right now, a LP has been running on one of our lab's machine (Something like 8 CPU, some fearful amount of RAM) for more that 2 days straight. And there is some hope it will finish ! That's one of the things I accept coming from LP. Sometimes, they are too slow ;-)\n\nNathann",
    "created_at": "2010-07-27T08:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92529",
    "user": "https://github.com/nathanncohen"
}
```

Well, it is not a surprise that such LP can run for a long time... Right now, a LP has been running on one of our lab's machine (Something like 8 CPU, some fearful amount of RAM) for more that 2 days straight. And there is some hope it will finish ! That's one of the things I accept coming from LP. Sometimes, they are too slow ;-)

Nathann



---

archive/issue_comments_092530.json:
```json
{
    "body": "Replying to [comment:53 ncohen]:\n> Well, it is not a surprise that such LP can run for a long time...\n\n\nAs mentioned above, the whole test (`-long`) of `generic_graph.py` - with *in theory* **the same** LP program (30 vertices) - took 281 seconds on a much slower machine.\n\nI still don't know if the GLPK library or the Sage interface/code that builds the LP program structure is broken on the other (very similar, btw) machine.\n\n(I've killed the Python process running the solver after 42138+ seconds, which was still searching for a solution.)\n\nNathann, could you take a look at the variable name generation which causes the MPS and LP file errors? (These should be reproducible on all systems I think, at least I've met them on a 64-bit system, running Ubuntu 9.04.)",
    "created_at": "2010-07-27T16:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92530",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:53 ncohen]:
> Well, it is not a surprise that such LP can run for a long time...


As mentioned above, the whole test (`-long`) of `generic_graph.py` - with *in theory* **the same** LP program (30 vertices) - took 281 seconds on a much slower machine.

I still don't know if the GLPK library or the Sage interface/code that builds the LP program structure is broken on the other (very similar, btw) machine.

(I've killed the Python process running the solver after 42138+ seconds, which was still searching for a solution.)

Nathann, could you take a look at the variable name generation which causes the MPS and LP file errors? (These should be reproducible on all systems I think, at least I've met them on a 64-bit system, running Ubuntu 9.04.)



---

archive/issue_comments_092531.json:
```json
{
    "body": "The corresponding ticket is #9617 . Thank you for finding this one ! :-)\n\nNathann",
    "created_at": "2010-07-28T03:10:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92531",
    "user": "https://github.com/nathanncohen"
}
```

The corresponding ticket is #9617 . Thank you for finding this one ! :-)

Nathann



---

archive/issue_comments_092532.json:
```json
{
    "body": "The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.",
    "created_at": "2010-12-05T14:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92532",
    "user": "https://github.com/jdemeyer"
}
```

The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.



---

archive/issue_comments_092533.json:
```json
{
    "body": "Replying to [comment:56 jdemeyer]:\n> The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.\n\n\nPlease see #9863 for this problem.",
    "created_at": "2010-12-05T14:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9584#issuecomment-92533",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:56 jdemeyer]:
> The error in the ticket (negative `get_memory_usage()`) still occurs today on the Skynet machine iras with sage-4.6.1.alpha3.


Please see #9863 for this problem.
