# Issue 9285: Challenge: iterating through E8 in 5 minutes

archive/issues_009285.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: Coxeter groups, Chevie\n\nThe current code for iterating trough all elements of a Coxeter group is currently ridiculously slow. For E8, it should take no more than a couple minutes, as Franck Lubeck's reported was possible in GAP.\n\nThere are several routes to this end, which all deserve to be explored:\n\n* Using GAP's code; this will require at least fixing a `select` issue in GAP's interface (TODO: add ticket), if not using libGAP\n\n* Optimizing the underlying CombinatorialFreeModule's code\n\n* Optimizing the generic Coxeter group code\n\n* Using properly Coxeter 3\n\nIssue created by migration from https://trac.sagemath.org/ticket/9285\n\n",
    "created_at": "2010-06-20T21:05:43Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Challenge: iterating through E8 in 5 minutes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9285",
    "user": "nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: Coxeter groups, Chevie

The current code for iterating trough all elements of a Coxeter group is currently ridiculously slow. For E8, it should take no more than a couple minutes, as Franck Lubeck's reported was possible in GAP.

There are several routes to this end, which all deserve to be explored:

* Using GAP's code; this will require at least fixing a `select` issue in GAP's interface (TODO: add ticket), if not using libGAP

* Optimizing the underlying CombinatorialFreeModule's code

* Optimizing the generic Coxeter group code

* Using properly Coxeter 3

Issue created by migration from https://trac.sagemath.org/ticket/9285





---

archive/issue_comments_087457.json:
```json
{
    "body": "Instead of taking the nomenclature [\"E\",8], if we take  Cartan matrix of E8 manually\ncm= CartanMatrix([\n [2,-1,0,0,0,0,0,0],\n [-1,2,-1,0,0,0,0,0],\n [0,-1,2,-1,0,0,0,0],\n [0,0,-1,2,-1,0,0,0],\n [0,0,0,-1,2,-1,0,-1],\n [0,0,0,0,-1,2,-1,0],\n [0,0,0,0,0,-1,2,0],\n [0,0,0,0,-1,0,0,2]],cartan_type_check = False);cm\nR=RootSystem(cm).root_lattice()\nalpha = R.simple_roots();alpha\nW = R.weyl_group(prefix=\"s\")\nfor w in W:\n w.action(alpha[2]) ==alpha[4] :\n  print w\nthen we are able to act weyl group action on any element with a reasonable time.\nAlthough it is taking more time. it is not showing now error insufficient memory).",
    "created_at": "2015-09-05T04:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9285#issuecomment-87457",
    "user": "bransingh"
}
```

Instead of taking the nomenclature ["E",8], if we take  Cartan matrix of E8 manually
cm= CartanMatrix([
 [2,-1,0,0,0,0,0,0],
 [-1,2,-1,0,0,0,0,0],
 [0,-1,2,-1,0,0,0,0],
 [0,0,-1,2,-1,0,0,0],
 [0,0,0,-1,2,-1,0,-1],
 [0,0,0,0,-1,2,-1,0],
 [0,0,0,0,0,-1,2,0],
 [0,0,0,0,-1,0,0,2]],cartan_type_check = False);cm
R=RootSystem(cm).root_lattice()
alpha = R.simple_roots();alpha
W = R.weyl_group(prefix="s")
for w in W:
 w.action(alpha[2]) ==alpha[4] :
  print w
then we are able to act weyl group action on any element with a reasonable time.
Although it is taking more time. it is not showing now error insufficient memory).



---

archive/issue_comments_087458.json:
```json
{
    "body": "On my Asus with i7 quad-core (hyperthreaded to 8) and 8GB RAM and #19821 (and doing other things), I get the following running serially (on 1 thread):\n\n```\nsage: W = CoxeterGroup(['E',6], base_ring=ZZ)\nsage: %time for x in W: pass\nCPU times: user 11.2 s, sys: 32 ms, total: 11.2 s\nWall time: 11.2 s\n\nsage: W = CoxeterGroup(['E',7], base_ring=ZZ)\nsage: %time for x in W: pass\nCPU times: user 5min 47s, sys: 14.4 ms, total: 5min 47s\nWall time: 5min 46s\n```\n\nSince E<sub>8</sub> is 240 times larger than E<sub>7</sub>, I expect it to take roughly 240 times longer (although from E<sub>6</sub> to E<sub>7</sub>, it only took 31x longer whereas there is a 56x size difference). That is roughly 23 hours... (in reality, it is probably a lot less, but still on the order of hours).",
    "created_at": "2016-01-03T10:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9285#issuecomment-87458",
    "user": "tscrim"
}
```

On my Asus with i7 quad-core (hyperthreaded to 8) and 8GB RAM and #19821 (and doing other things), I get the following running serially (on 1 thread):

```
sage: W = CoxeterGroup(['E',6], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 11.2 s, sys: 32 ms, total: 11.2 s
Wall time: 11.2 s

sage: W = CoxeterGroup(['E',7], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 5min 47s, sys: 14.4 ms, total: 5min 47s
Wall time: 5min 46s
```

Since E<sub>8</sub> is 240 times larger than E<sub>7</sub>, I expect it to take roughly 240 times longer (although from E<sub>6</sub> to E<sub>7</sub>, it only took 31x longer whereas there is a 56x size difference). That is roughly 23 hours... (in reality, it is probably a lot less, but still on the order of hours).



---

archive/issue_comments_087459.json:
```json
{
    "body": "With the recent changes to #19821, I now get:\n\n```\nsage: sage: W = CoxeterGroup(['E',6], base_ring=ZZ)\nsage: sage: %time for x in W: pass\nCPU times: user 4.28 s, sys: 36.1 ms, total: 4.31 s\nWall time: 4.23 s\n\nsage: sage: W = CoxeterGroup(['E',7], base_ring=ZZ)\nsage: %time for x in W: pass\nCPU times: user 4min 28s, sys: 20 ms, total: 4min 28s\nWall time: 4min 28s\n```\n",
    "created_at": "2016-01-03T11:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9285#issuecomment-87459",
    "user": "tscrim"
}
```

With the recent changes to #19821, I now get:

```
sage: sage: W = CoxeterGroup(['E',6], base_ring=ZZ)
sage: sage: %time for x in W: pass
CPU times: user 4.28 s, sys: 36.1 ms, total: 4.31 s
Wall time: 4.23 s

sage: sage: W = CoxeterGroup(['E',7], base_ring=ZZ)
sage: %time for x in W: pass
CPU times: user 4min 28s, sys: 20 ms, total: 4min 28s
Wall time: 4min 28s
```




---

archive/issue_comments_087460.json:
```json
{
    "body": "With #11187, on my laptop (see comment:4) I get\n\n```\nsage: W = ReflectionGroup(['E',8])\nsage: %time for x in W.iteration('depth', False): pas\nCPU times: user 8min 44s, sys: 38.2 ms, total: 8min 44s\nWall time: 8min 43s\n```\n\nThere are a number of changes from #11187 (the cythonization) that could be lifted up to be used for the general Coxeter group iteration.",
    "created_at": "2016-04-10T13:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9285#issuecomment-87460",
    "user": "tscrim"
}
```

With #11187, on my laptop (see comment:4) I get

```
sage: W = ReflectionGroup(['E',8])
sage: %time for x in W.iteration('depth', False): pas
CPU times: user 8min 44s, sys: 38.2 ms, total: 8min 44s
Wall time: 8min 43s
```

There are a number of changes from #11187 (the cythonization) that could be lifted up to be used for the general Coxeter group iteration.



---

archive/issue_comments_087461.json:
```json
{
    "body": "With Gap3 in Sage, it took 6m20s to go through E<sub>8</sub> on my laptop (serially, comment:4):\n\n```\ngap> i:=0;;\ngap> W:=CoxeterGroup(\"E\",7);;\ngap> ForEachElement(W,function(x)i:=i+1;end);\n```\n",
    "created_at": "2016-04-10T18:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9285#issuecomment-87461",
    "user": "tscrim"
}
```

With Gap3 in Sage, it took 6m20s to go through E<sub>8</sub> on my laptop (serially, comment:4):

```
gap> i:=0;;
gap> W:=CoxeterGroup("E",7);;
gap> ForEachElement(W,function(x)i:=i+1;end);
```

