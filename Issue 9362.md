# Issue 9362: Invalidate None as a vertex label.

Issue created by migration from https://trac.sagemath.org/ticket/9362

Original creator: boothby

Original creation time: 2010-06-28 19:27:02

Assignee: jason, mvngu, ncohen, rlm

CC:  brunellus

The following indicates to me a huge problem:


```
sage: G = Graph()
sage: G.add_edge(None, 1)
sage: G.show()
```


the resulting plot has three vertices, one blank, one labeled "1" and the other labeled "None".  The blank vertex is floating off in space, and the None and 1 vertices are bunched together.

This indicates to me that we should not accept "None" as a valid vertex label.

Other places where a vertex labeled None will obviously cause problems:

`spanning_trees_count`, `add_vertex`, `add_edge`, `delete_edge`, `has_edge`, `edge_label`, `eccentricity`, `layout_tree`

this is not an exhaustive list; I merely read method definitions to look where a vertex argument defaults to None (and later uses the condition `if v is None`).


---

Comment by dsm created at 2011-12-14 15:33:51

It definitely makes sense to forbid None as a vertex label.  add_vertex(), which it makes sense to think of as the fundamental spec, already forbids the use of None, both explicitly in the docstring ("cannot be None") and implicitly in practice because it uses the default None to mean "next unused integer".  So that you can sneak it in as one through a back channel is a bad thing given the widespread use of None as a special value, just like the OP says.


---

Comment by brunellus created at 2011-12-31 01:04:00

I am not sure whether this patch catches every possible way a None-labeled vertex can sneak in, but I tried to go through the code and repair such cases.

Please, apply first the patch from #11739 before testing.

During testing I noticed that


```
sage: G=Graph(); G.add_edge(None, 4); G.vertices()
[0, 4]
sage: G=Graph(); G.add_edge(5, None)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/root/Sage/sageNoneVertex/devel/sage-main/sage/graphs/<ipython console> in <module>()

/root/Sage/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in add_edge(self, u, v, label)
   7556                     u, v, label = u
   7557                 except:
-> 7558                     u, v = u
   7559                     label = None
   7560         else:

TypeError: 'sage.rings.integer.Integer' object is not iterable
```


That is unpleasant asymmetry, don't you think? So I modified the code a little and now it works as expected.


```
sage: G=Graph(); G.add_edge(5, None); G.vertices()
[0, 5]
```



---

Comment by brunellus created at 2011-12-31 01:04:00

Changing status from new to needs_review.


---

Attachment


---

Comment by zimmerma created at 2012-01-10 08:58:01

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2012-01-10 08:58:01

if #11739 is needed, please add it in the dependencies.

I thought from the summary that using None would be forbidden and would raise an exception, but
comment [comment:4] seems to still use None as a vertex. Is that wanted?

Paul Zimmermann


---

Comment by zimmerma created at 2012-01-10 10:43:33

Changing keywords from "" to "sd35.5".


---

Comment by brunellus created at 2012-01-10 14:03:14

Replying to [comment:5 zimmerma]:
> I thought from the summary that using None would be forbidden and would raise an exception, but
> comment [comment:4] seems to still use None as a vertex. Is that wanted?

Sorry that I didn't discuss this. What do you think? Using None as a special value for "create a new vertex" is consistent with add_vertex (that is especially nice in merge_vertices -- maybe that function should return a new vertex name in the [None, ...] case?), but it can make some errors harder to find. I don't have a strong opinion.


---

Comment by brunellus created at 2012-01-10 14:41:35

BTW: I'm not sure how slow is exception handling in Python, but isn't it little unfortunate that this is used so extensively in the add_edge function? Every call add_edge((u, v)) raises an exception that is immediately caught.


```
sage: G=Graph(multiedge=True)
sage: timeit("G.add_edge(1, 2)")
625 loops, best of 3: 8.21 µs per loop
sage: timeit("G.add_edge((1, 2))")
625 loops, best of 3: 12.2 µs per loop
```



---

Comment by zimmerma created at 2012-01-11 12:26:15

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2012-01-11 12:26:15

ok, I agree that using None as special value in `add_edge` makes sense, and is consistent
with `add_vertex`. Thus I put it back to needs review.

Paul


---

Comment by zimmerma created at 2012-01-11 12:28:13

All doctests pass, and this is fine for me. Good work!

Paul


---

Comment by zimmerma created at 2012-01-11 12:28:13

Changing status from needs_review to positive_review.


---

Comment by brunellus created at 2012-01-31 14:04:25

Changing status from positive_review to needs_work.


---

Comment by brunellus created at 2012-01-31 14:04:25

I'm sorry -- the current version isn't compatible with changes in #11739. Would you be so kind to look at this one last time (hopefully)? :-)


---

Attachment


---

Comment by brunellus created at 2012-01-31 14:05:18

Changing status from needs_work to needs_review.


---

Comment by brunellus created at 2012-01-31 14:28:56

(I just removed this part:


```
- self._nxg.add_nodes_from(vertices) 
+ for v in vertices: 
+     self.add_vertex(v) 
```


. #11739 takes care what happens there.)


---

Comment by zimmerma created at 2012-02-02 07:23:32

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-02-02 07:23:32

positive review, all doctests still pass with Sage 4.8 (except a timeout in
`sandpiles/sandpile.py` which already happened before this patch).

Paul


---

Comment by jdemeyer created at 2012-02-22 10:44:08

Resolution: fixed
