# Issue 7227: Improving factor complexity of words functions

Issue created by migration from https://trac.sagemath.org/ticket/7227

Original creator: slabbe

Original creation time: 2009-10-15 14:28:38

Assignee: slabbe

CC:  vdelecroix

Keywords: factor complexity

Improving the word complexity functions by
 - caching palindromic_lacunas_study
 - caching suffix_tree
 - caching suffix_trie
 - allowing factor_set to take an integer as input
 - adding rauzy_graph function for finite word



---

Attachment


---

Comment by slabbe created at 2009-10-15 14:37:46

Here are some examples of the improvements made by the patch :


BEFORE:


```
sage: t = words.ThueMorseWord()
sage: w = t[:10000]
sage: time _ = [w.number_of_factors(i) for i in range(20)]
CPU times: user 4.19 s, sys: 0.00 s, total: 4.19 s
Wall time: 4.19 s
sage: time _ = [w.number_of_factors(i) for i in range(50)]
CPU times: user 10.28 s, sys: 0.00 s, total: 10.28 s
Wall time: 10.28 s
```


AFTER:


```
sage: t = words.ThueMorseWord()
sage: w = t[:10000]
sage: time _ = [w.number_of_factors(i) for i in range(20)]
CPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s
Wall time: 0.30 s
sage: time _ = [w.number_of_factors(i) for i in range(50)]
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
sage: time _ = [w.number_of_factors(i) for i in range(100)]
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
sage: time _ = [w.number_of_factors(i) for i in range(1000)]
CPU times: user 4.90 s, sys: 0.00 s, total: 4.90 s
Wall time: 4.90 s
sage: time _ = [w.number_of_factors(i) for i in range(1001)]
CPU times: user 4.85 s, sys: 0.00 s, total: 4.85 s
Wall time: 4.85 s
sage: time _ = [w.number_of_factors(i) for i in range(2000)]
CPU times: user 27.64 s, sys: 0.00 s, total: 27.64 s
Wall time: 27.64 s
```



I should also add some Rauzy graphs examples and some timing improvements on palindrome complexity as well.


---

Comment by slabbe created at 2009-10-15 14:37:46

Changing status from new to needs_review.


---

Attachment


---

Comment by slabbe created at 2009-10-20 11:31:50

I added a patch that improves the rauzy graph function (adds the labels to the edges).

Still needs review!


---

Comment by vdelecroix created at 2009-10-28 18:37:00

rauzy_graph : why don't you use DiGraph method for the creation of edges ?

The rest is OK.


---

Comment by slabbe created at 2009-10-29 01:23:35

Replying to [comment:3 vdelecroix]:
> rauzy_graph : why don't you use DiGraph method for the creation of edges ?

You mean the add_edge method? I don't know. Is it faster?


---

Comment by vdelecroix created at 2009-10-29 12:42:09

Replying to [comment:5 slabbe]:
> Replying to [comment:3 vdelecroix]:
> > rauzy_graph : why don't you use DiGraph method for the creation of edges ?
> 
> You mean the add_edge method? I don't know. Is it faster?

At least it is not slower and I find it clearer:

```
sage: timeit('G = DiGraph(loops=True)\nfor i in range(200):\n  for j in range(200):\n    d.add_edge(i,j)')
5 loops, best of 3: 248 ms per loop
sage: timeit('d = {}\nfor i in range(200):\n  d[i]=[]\n  for j in range(200):\n    d[i].append(j)\nG=DiGraph(d,loops=True)')
5 loops, best of 3: 266 ms per loop
```



---

Attachment

Applies over the precedent 2 patches.


---

Comment by slabbe created at 2009-10-29 17:08:43

Thanks for the suggestion Vincent. I did the changes. I also changed the behavior for n=0 to agree with what is currently done in `digraphs.DeBruijn()` (see #7246).

Needs review!


---

Comment by vdelecroix created at 2009-10-29 20:07:16

Positive review.

Remark for future: the graph rendering is quite bad because word renders "word: xxxx"


---

Comment by vdelecroix created at 2009-10-29 20:07:16

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2009-10-30 18:09:00

> Remark for future: the graph rendering is quite bad because word renders "word: xxxx"

One way to avoid the `word: ` identifier is to set it empty using 


```
sage: WordOptions(identifier='')
sage: Word(range(10))
0123456789
```


but it affects not only the vertices of the Rauzy graph but every single print of a word which might not be exactly what you want...


---

Comment by mhansen created at 2009-10-31 15:42:50

Resolution: fixed
