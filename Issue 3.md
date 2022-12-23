# Issue 3: py3: bug with canonical_label

The following doctest of `petersen_family` in `families.py` fails with with Python3:

```
        sage: F1 = graphs.petersen_family(generate=False)
        sage: F2 = graphs.petersen_family(generate=True)
        sage: F1 = [g.canonical_label().graph6_string() for g in F1]
        sage: F2 = [g.canonical_label().graph6_string() for g in F2]
        sage: set(F1) == set(F2)
        True
```


Some investigation suggests that the issue comes from `canonical_label`. Consider the following example (part of the code of `petersen_family`).

```
sage: def YDeltaTrans(G, v):
....:     """
....:     Apply a Y-Delta transformation to a given vertex v of G.
....:     """
....:     G = G.copy()
....:     a, b, c = G.neighbors(v)
....:     G.delete_vertex(v)
....:     G.add_cycle([a, b, c])
....:     return G.canonical_label()
....: 
sage: P = graphs.PetersenGraph()
sage: Q = YDeltaTrans(P, 0)
sage: for v in P:
....:     g = YDeltaTrans(P, v)
....:     print(g.graph6_string(), g.is_isomorphic(Q))
```

With Python 2, we get:

```
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
('HY_[aSf', True)
```

With Python 3, we get:

```
HleAPWU True
HlbAPWU True
Hl`BPWU True
Hl`@PwU True
Hl`@OyU True
HhdDCkM True
Hhe@IhJ True
Hhea?km True
HheQhGJ True
HheAP[U True
```

so the `canonical_label` method seems broken with Python 3.

Issue created by migration from https://trac.sagemath.org/ticket/26800




---

Changing keywords from "" to "py3, graph".


---

Ouch..

This may also explain why the code in cluster_quiver fails so badly..


---

We must investigate deeper to find the cause of the issue. Do we have an expert in this part of the code ?


---

on the other hand, in python3:

```
sage: [YDeltaTrans(P, i).canonical_label().graph6_string() for i in range(10)]
['HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb',
 'HKN?Yeb']
```



---

Let's summarize:

```
sage: P = graphs.PetersenGraph()
sage: H = P.copy()
sage: a, b, c = H.neighbors(1)
sage: H.delete_vertex(1)
sage: H.add_cycle([a, b, c])
sage: H.canonical_label().graph6_string()
'HlbAPWU'
sage: H.canonical_label().canonical_label().graph6_string()
'HKN?Yeb'
```

So the canonical label works after the second application. 

*EDIT*:
But the edges are not changed:

```
sage: sorted(H.canonical_label().edges())==sorted(H.canonical_label().canonical_label().edges())
True
```


*EDIT*:
And the graphs are indeed the same

```
sage: H1 = H.canonical_label()
sage: H2 = H.canonical_label().canonical_label()
sage: H1 == H2
True
```



---

This is really weird.


---

Maybe an issue in graph6_string...

```
sage: H1._bit_vector()==H2._bit_vector()
False
```



---

With py3, we have

```
sage: list(H1)
[7, 8, 5, 4, 1, 6, 2, 3, 0]
sage: list(H2)
[0, 1, 2, 3, 4, 5, 6, 7, 8]
```

So the mapping `v_to_int = {v: i for i, v in enumerate(self)}` in `_bit_vector` is not the same :(

But with py2, the 2 mappings are the same.

I suspect that the order in which vertices are added to the graph is not the same. May be a loop over the keys of a dictionary as this order is not necessarily the same in py2 and in py3?
If you check method `iterator_verts` in `c_graph.pyx`, it iterates over the keys of dictionary `vertex_ints`...


---

Looks like it could (maybe) be fixed (or disappear in some way) by using Python 3.7 (#25680)...


---

Let's hope so.


---

I've done some investigation. The issue seems to be that in Python 3.6+ dictionaries are iterated over in 'insertion order' rather than in the Python 2.7 '(hash of) key order'. In the above code the problem arises in the `CGraph.iterator_verts` method where there is iteration over the `dict` called `CGraph.vertex_ints` (see `sage/graphs/base/c_graph.pyx`). 

This bug indicates that at least some sage graph code silently relies on Python 2.7-style dict iteration rather than 'insertion order' as in Python 3.6+. The new behaviour was standardised for 3.7 so I don't think the bug will magically disappear in the future.

I think it is probably too costly in time/memory to sort every time vertices are iterated over (by adding `sorted` in line 1747 of `c_graph.pyx` in the `iterator_verts` method). 
We could reimplement a dictionary type that retains key order naturally and use it for `CGraph.vertex_ints`, or carefully pin down which code needs sorted iteration and modify accordingly. For example, it suffices to change only the `relabel` method on the extension class `CGraph` to fix this bug: replacing 

```python
self.vertex_ints = new_vx_ints
}}} 
with
{{{#!python
self.vertex_ints = dict(sorted(new_vx_ints.items()))
}}}
on line 1965 of `c_graph.pyx` seems to fix this ticket for me, and perhaps paying the sorting cost upon relabelling is OK. Note that to support both Python 2.7 and 3.6+ one needs to consider `iteritems` vs `items` in this fix (and know about `__future__` or `six`, which I do not).


---

Replying to [comment:12 gh-ed359]:
> {{{#!python
> self.vertex_ints = dict(sorted(new_vx_ints.items()))
> }}}
We cannot do that. The keys of dictionary `new_vx_ints` can be of any hashable type, and we cannot sort a list of items of different types in py3.


---

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)


---

#27695 seems to fix this as well. Shall we close this ticket or is there any
more work to be done here?


---

Changing status from new to needs_review.


---

We can close this one.


---

Changing status from needs_review to positive_review.


---

Resolution: duplicate
