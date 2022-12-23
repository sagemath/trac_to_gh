# Issue 6102: cohomology ring of simplicial complexes

Issue created by migration from https://trac.sagemath.org/ticket/6102

Original creator: bantieau

Original creation time: 2009-05-21 03:47:14

Assignee: bantieau

CC:  jhpalmieri fbreuer tscrim chapoton

Add functionality in sage to compute the cohomology ring of a simplicial complex.

This relies on #6099, #6100, #6101, and #5882.

These will be examples of graded alebras, finite as modules over their bases, that are graded-commutative.


---

Comment by jhpalmieri created at 2012-01-04 23:59:42

The following code was posted by Felix Breuer on [sage-support](https://groups.google.com/d/topic/sage-support/mdEKXfBTHOY/discussion)

```
def cup_product(X,c1,dim1,c2,dim2):
    d = dim1 + dim2 
    faces1 = list(X.n_faces(dim1))
    faces2 = list(X.n_faces(dim2))
    faces = list(X.n_faces(d))
    res = []
    for sigma in faces:
        sigma1 = Simplex(sigma[0:dim1+1])
        sigma2 = Simplex(sigma[dim1:d+1])
        index1 = faces1.index(sigma1)
        index2 = faces2.index(sigma2)
        coeff1 = c1[index1]
        coeff2 = c2[index2]
        coeff = coeff1 * coeff2
        res.append(coeff)
    return vector(tuple(res))
```

To use it on the Torus, for example, you can do this:

```
X = simplicial_complexes.Torus()
C = X.chain_complex(cochain=True)
H = C.homology(generators=True)
gen1 = H[1][1][0]
gen2 = H[1][1][1]
d1 = C.differential()[1]
q = cup_product(X,gen1,1,gen1,1)
print q
print d1.solve_right(q)
p = cup_product(X,gen1,1,gen2,1)
print p
print d1.solve_right(p) #error
```



---

Comment by jhpalmieri created at 2015-09-10 02:30:15

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2015-09-10 02:30:15

Here is an initial attempt. 
----
New commits:


---

Comment by git created at 2015-09-10 15:24:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jhpalmieri created at 2015-09-10 22:08:35

Changing priority from minor to major.


---

Comment by git created at 2015-09-11 18:24:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-09-12 16:24:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jhpalmieri created at 2015-09-12 16:30:55

#18246 broke the default hashing of chain homotopies, so I've added a `__hash__` method, and also one for chain maps. This is necessary so that we can cache the methods `algebraic_topological_model`, `homology_basis`, and `cohomology_ring` in `cell_complex`.


---

Comment by git created at 2015-09-14 15:17:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jhpalmieri created at 2015-09-23 18:04:22

An update: I have a new version of `algebraic_topological_model.py`, which is the key to everything here. I'm calling it `AT_model.py`, and I'll attach it to the ticket. The good news:

- it works for Delta complexes
- it's faster with mod 2 coefficients:

```
sage: from sage.homology.algebraic_topological_model import algebraic_topological_model
sage: from sage.homology.AT_model import AT_model
sage: RP3 = simplicial_complexes.RealProjectiveSpace(3)
sage: %time phi, H = algebraic_topological_model(RP3, GF(2)) # old version
CPU times: user 813 ms, sys: 150 ms, total: 963 ms
Wall time: 852 ms
sage: %time phi, H = AT_model(RP3, GF(2))     # new version
CPU times: user 345 ms, sys: 32.3 ms, total: 377 ms
Wall time: 354 ms
```

The bad news: it's _much_ slower with rational coefficients, and I have no idea why:

```
sage: %time phi, H = algebraic_topological_model(RP3, QQ)   # old version
CPU times: user 1.27 s, sys: 138 ms, total: 1.41 s
Wall time: 1.35 s
sage: %time phi, H = AT_model(RP3, QQ)      # new version
CPU times: user 23.9 s, sys: 69.6 ms, total: 24 s
Wall time: 24 s
```

Profiling the code with `%prun` was not illuminating to me, and I couldn't run `%crun` because I couldn't get [the Google performance analysis tools](https://github.com/gperftools/gperftools) to install on my machine. Optimizing code is not my strong suit, in any case.

Because of this, I haven't tried to implement cup products for Delta complexes. I think I know how to do that, but it hasn't felt worth it yet.


---

Attachment

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-10-08 18:20:11

I think the issue comes from the fact that a category pushout is being done. This doesn't seem to happen in the finite fields of prime order cases, but it does show up for prime powers. However, for `GF(4, 'a')`, it took a non-trivial amount of time (over 2 seconds on my machine).

From doing a line by line profiling, here's the lines that take the longest over `QQ`:

```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   210       182       745504   4096.2      5.8              c_bar = c - phi_old * diff * c
   211       182       452404   2485.7      3.5              pi_bdry_c_bar = pi_old * diff * c_bar 
   236      5321     10852810   2039.6     84.1                      eta_ij = (pi_old * c_j)[u_idx]
   244        90       323096   3590.0      2.5                  phi_old = MS_phi_t.matrix(phi_old_cols).transpose()
   290         1        27459  27459.0      0.2      phi = ChainContraction(phi_data, pi, iota)
```

where the time is given in microseconds. Over `GF(2)`, these operations are significantly faster per call.


---

Comment by jhpalmieri created at 2015-10-08 22:31:30

That's helpful. The change

```diff
--- Dropbox/prog/sage/Math/Simplicial/homotopies/AT_model.py	2015-09-23 10:44:42.000000000 -0700
+++ Desktop/AT_model.py	2015-10-08 14:14:33.000000000 -0700
@@ -233,7 +233,7 @@
                 pi_cols.append(zero_vector)
                 for c_j_idx, c_j in enumerate(old_cells):
                     # eta_ij = <u, pi(c_j)>:
-                    eta_ij = (pi_old * c_j)[u_idx]
+                    eta_ij = pi_old.row(u_idx).dot_product(c_j)
 
                     if eta_ij:
                         # Adjust phi(c_j).
```

cuts the time for `AT_model(RP3, QQ)` from about 20 seconds to about 3 seconds. Still too long, but better. (At the moment, I'm getting about 7/10 of a second for the old version, just under 3 seconds with this modified new version.)

For rational matrices with lots of zero entries, it seems to be faster to multiply sparse matrices than dense ones, so I am trying to replace some of the matrices by sparse versions. I found [this bug](http://trac.sagemath.org/ticket/19377) by doing this. Good times.


---

Comment by jhpalmieri created at 2015-10-08 23:21:16

Another new bug: #19378.


---

Comment by tscrim created at 2015-10-09 03:16:10

(I like this line-profiler, it's very useful.) A lot of time seems to be lost with (dense?) matrix operations over `QQ`:

```
   210       182       741358   4073.4     33.0              c_bar = c - phi_old * diff * c
   211       182       458238   2517.8     20.4              pi_bdry_c_bar = pi_old * diff * c_bar


   244        90       280498   3116.6     12.5                  phi_old = MS_phi_t.matrix(phi_old_cols).transpose()
   245      3402         4290      1.3      0.2                  indices = [i for i in range(pi_nrows) if i not in to_be_deleted]
   246        90        16370    181.9      0.7                  keep = vector(base_ring, pi_nrows, {i:1 for i in indices})
   247      5411       204965     37.9      9.1                  cols = [v.pairwise_product(keep) for v in pi_cols_old]
   248        90       258909   2876.8     11.5                  pi_old = MS_pi_t.matrix(cols).transpose()
```

I know we have many specialized algorithms for doing matrix manipulations over finite fields, so perhaps we are also seeing some of that here too. I'm wondering if the difference is just the number of matrix operations is just higher...(perhaps sparse matrices will work better...).

FYI - in the old implementation, this was the line taking the majority of the time

```
   246      5321       727375    136.7     65.8                      c_j_vec = vector(base_ring, old_rank, {c_j_idx: 1})
```



---

Comment by jhpalmieri created at 2015-10-09 04:11:15

Regarding lines like `c_bar = c - phi_old * diff * c`, it seems that matrix-vector multiplication is faster over `QQ` (compared to matrix-matrix multiplication) but slower over finite fields, so over `QQ` I have changed this to `c_bar = c - phi_old * (diff * c)`. I'll look at the other slow parts to see what I can do there, too.

How do you run the line-profiler?


---

Comment by jhpalmieri created at 2015-10-09 04:13:20

By the way, I now have: old timing 0.7 seconds, new timing 1.7 seconds over the rationals. Over finite fields, the new version takes about half the time (0.43 seconds compared to 0.2 seconds over `GF(2)`, not quite as good an improvement when working over other prime fields).


---

Comment by tscrim created at 2015-10-09 04:15:48

See http://doc.sagemath.org/html/en/thematic_tutorials/profiling.html#python-level-line-by-line-profiling-lprun


---

Comment by jhpalmieri created at 2015-10-09 04:34:25

Thanks. I'm not sure how I knew about `%prun` but not `%lprun`. `%lprun` looks much more helpful, at least in this case.


---

Comment by tscrim created at 2015-10-10 15:21:54

So do you think you'll switch to the new model? It's roughly a 2x slowdown (to which I'm fairly certain it is just because you are doing more matrix multiplications), but it does offer greater flexibility. The other option would be to include both methods and choose the old one for `QQ` over simplicial complexes...


---

Comment by jhpalmieri created at 2015-10-10 16:30:11

My current plan is indeed to use both methods. By using your `%lprun` analysis (and mine, too), I have managed to speed up both the old and new methods. Over finite fields, the _old_ method is now about 20 times faster than it used to be: on one machine, computing `algebraic_topological_model(RP3, GF(2))` used to take over 400 ms, and now takes about 20 ms, and similarly over other prime fields. Over the rationals, it used to take about 700 ms, and now takes just under 300. The new method is now faster than it used to be, but slower over all fields (about 200 ms over `GF(2)`, 1500 ms over `QQ`).

So the plan is to include both and use the old one for cubical and simplicial complexes, the new one only for Delta complexes. I want to figure out if I can actually implement the cup product for Delta complexes without rewriting the whole class of complexes, providing an actual class for its cells. I will try to update the branch soon in any case.


---

Comment by git created at 2015-10-10 17:55:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-10-10 19:01:01

Those are some very good improvements.

I really don't like this:

```python
# diff is sparse and low density. Dense matrices are faster
# over finite fields, but for low density matrices, sparse
# matrices are faster over the rationals.
if base_ring != QQ:
    diff = diff.dense_matrix()
```

It's not a blocker for this to get a positive review, but it bugs me. Plus the extra time to convert it to a dense matrix...

I did some quick digging and there is apparently a slew of tickets on improving sparse or modn vectors/matrices: #19076 (and therein), #18231, #15104, #10312, #18312, #2705.

Was there anything in your timings to suggest a good place to go look for just using sparse matrices? Did you also test with my fixes for #19377 and #19378 (and forcing sparse matrices, or are they even necessary)?

Is there anything else you'd like to do to this before I set it to positive review?


---

Comment by jhpalmieri created at 2015-10-10 20:10:41

Replying to [comment:30 tscrim]:
> Those are some very good improvements.
> 
> I really don't like this:
> {{{#!python
> # diff is sparse and low density. Dense matrices are faster
> # over finite fields, but for low density matrices, sparse
> # matrices are faster over the rationals.
> if base_ring != QQ:
>     diff = diff.dense_matrix()
> }}}
> It's not a blocker for this to get a positive review, but it bugs me. Plus the extra time to convert it to a dense matrix...

On my computer, if I do

```
sage: from sage.homology.algebraic_topological_model import algebraic_topological_model
sage: RP3 = simplicial_complexes.RealProjectiveSpace(3)
sage: %timeit algebraic_topological_model(RP3, GF(2))
```

then without this change, it takes 104 ms per loop; with the change it takes 19.5 ms per loop. (Similar over `GF(31)`, to pick a random other finite field.) So the time for converting to a dense matrix is outweighed by the speed when multiplying dense vs. sparse matrices and vectors.

> I did some quick digging and there is apparently a slew of tickets on improving sparse or modn vectors/matrices: #19076 (and therein), #18231, #15104, #10312, #18312, #2705.
> 
> Was there anything in your timings to suggest a good place to go look for just using sparse matrices? Did you also test with my fixes for #19377 and #19378 (and forcing sparse matrices, or are they even necessary)?

The fixes for #19377 and #19378 won't make much of a difference, because I think the main bottlenecks are matrix-matrix multiplication and matrix-vector multiplication. For #19378, it's easy enough to bypass the whole issue by testing whether the appropriate matrix is `nx0`. #18231 could help, since at least with the Delta-complex version, some of the slowest parts are constructing matrices.

I don't know where to look in the linear algebra code to improve the timings. I ran tests of the form

```
%timeit random_matrix(QQ, 40, density=0.1, sparse=True) * random_vector(QQ, 40, density=0.1, sparse=False)
```

and similarly with the second factor being a vector, and then I varied which factors were sparse. I tried with different coefficient fields, also. Over the rationals, as the density decreases, the timing for dense matrices stays pretty constant, but it speeds up for sparse matrices. (This is without even taking into account the fact that it is slower to construct random sparse matrices: see #2705.) Over finite fields, it's constant both ways, and slower for sparse matrices.

> Is there anything else you'd like to do to this before I set it to positive review?

I think that cup products for Delta complexes can come on a separate ticket, if anyone ever figures it out. I'll see what I can do, but I don't want it to hold up this ticket.


---

Comment by tscrim created at 2015-10-10 22:31:43

I made some reviewer changes, and it's mostly tweaking docstrings and copying your sparse/dense hack to get another ~20% in the "new" version.

Ffrom taking a closer look at things, I bet we could get further speedups by not taking the transpose of the `phi_old` and `pi_old` matrices in the inner loops and using `v * M` multiplication instead of `M' * v`. I tried to do this, but I don't think I understand the interworkings of the code to get this to work (at least for the "new" version). Have you tried to do this?

Also I noticed that `HomologyVectorSpaceWithBasis` represents a graded piece of the (co)homology space. Would you be opposed to me rewriting that such that it becomes the full (co)homology space/ring? I think it would simplify the overall code structure, allow easier extensions to infinite simplicial/cell complexes, and give a better interpretation of `cup_product` as being the product in the cohomology ring. (Also with #18175, we could then give work towards a cap product for manifolds.)

If you would prefer one/both of these things to be pushed to later tickets, we can do that, but I'd rather get the latter done now.
----
New commits:


---

Comment by tscrim created at 2015-10-10 22:38:57

Replying to [comment:31 jhpalmieri]:
> On my computer, if I do
> {{{
> sage: from sage.homology.algebraic_topological_model import algebraic_topological_model
> sage: RP3 = simplicial_complexes.RealProjectiveSpace(3)
> sage: %timeit algebraic_topological_model(RP3, GF(2))
> }}}
> then without this change, it takes 104 ms per loop; with the change it takes 19.5 ms per loop. (Similar over `GF(31)`, to pick a random other finite field.) So the time for converting to a dense matrix is outweighed by the speed when multiplying dense vs. sparse matrices and vectors.

I didn't mean to imply that it wasn't a significant speedup and I apologize if I did. However that is a much larger difference than I really expected. Eeek!

> The fixes for #19377 and #19378 won't make much of a difference, because I think the main bottlenecks are matrix-matrix multiplication and matrix-vector multiplication. For #19378, it's easy enough to bypass the whole issue by testing whether the appropriate matrix is `nx0`. #18231 could help, since at least with the Delta-complex version, some of the slowest parts are constructing matrices.
> I don't know where to look in the linear algebra code to improve the timings. I ran tests of the form
> {{{
> %timeit random_matrix(QQ, 40, density=0.1, sparse=True) * random_vector(QQ, 40, density=0.1, sparse=False)
> }}}
> and similarly with the second factor being a vector, and then I varied which factors were sparse. I tried with different coefficient fields, also. Over the rationals, as the density decreases, the timing for dense matrices stays pretty constant, but it speeds up for sparse matrices. (This is without even taking into account the fact that it is slower to construct random sparse matrices: see #2705.) Over finite fields, it's constant both ways, and slower for sparse matrices.

It sounds like #2705 will help for the sparse case, but I can dig around in the sparse matrix code and try to find out ways I can squeeze speed out of the matrix operations (and use hints from the tickets I cited) if you think it's worth it for this ticket. See also my previous replay


---

Comment by jhpalmieri created at 2015-10-11 02:16:19

Replying to [comment:32 tscrim]:
> I made some reviewer changes, and it's mostly tweaking docstrings and copying your sparse/dense hack to get another ~20% in the "new" version.

Great.
 
> From taking a closer look at things, I bet we could get further speedups by not taking the transpose of the `phi_old` and `pi_old` matrices in the inner loops and using `v * M` multiplication instead of `M' * v`. I tried to do this, but I don't think I understand the interworkings of the code to get this to work (at least for the "new" version). Have you tried to do this?

Good idea. I just tried it and it led to no improvement, surprisingly, over the rationals, and a slow-down in characteristic 2. Maybe the lack of improvement is not that surprising, since I had already moved the slow matrix constructions out of the inner-most loops, so they don't get executed as much. And maybe taking the transpose is not slow compared to the rest of matrix construction.

> Also I noticed that `HomologyVectorSpaceWithBasis` represents a graded piece of the (co)homology space. Would you be opposed to me rewriting that such that it becomes the full (co)homology space/ring? I think it would simplify the overall code structure, allow easier extensions to infinite simplicial/cell complexes, and give a better interpretation of `cup_product` as being the product in the cohomology ring. (Also with #18175, we could then give work towards a cap product for manifolds.)

I think that it is natural to want both structures, the cohomology in a single degree and the cohomology in total. If you want to rewrite this part, that's okay with me. If you want to think about the most natural way to access cohomology classes, too, go ahead. I am not completely satisfied with

```
sage: a,b,c,d = X.cohomology_with_basis(1, QQ).gens()
```

Maybe

```
sage: H.<x> = X.cohomology_with_basis(1, QQ)
```

will define `x0`, ..., `x3` if the cohomology is 4-dimensional? Or x10, ..., x13? (The problem with the angle-bracket notation is that we shouldn't have to know how many generators there are ahead of time.)

> I didn't mean to imply that it wasn't a significant speedup and I apologize if I did. However that is a much larger difference than I really expected. Eeek!

No need to apologize, you had a reasonable question. And it is surprising how much difference that single change makes.


---

Comment by tscrim created at 2015-10-11 03:36:37

Replying to [comment:34 jhpalmieri]:
> Replying to [comment:32 tscrim]:
> > From taking a closer look at things, I bet we could get further speedups by not taking the transpose of the `phi_old` and `pi_old` matrices in the inner loops and using `v * M` multiplication instead of `M' * v`. I tried to do this, but I don't think I understand the interworkings of the code to get this to work (at least for the "new" version). Have you tried to do this?
> 
> Good idea. I just tried it and it led to no improvement, surprisingly, over the rationals, and a slow-down in characteristic 2. Maybe the lack of improvement is not that surprising, since I had already moved the slow matrix constructions out of the inner-most loops, so they don't get executed as much. And maybe taking the transpose is not slow compared to the rest of matrix construction.

Yea, I confirm that there is not much time being spent on the transpose by just pulling that part out to a separate line (which I should have done beforehand, sorry). So the way to optimize this further is to speed up the matrix construction, which might depend upon the input data, and then also the dot product is the 3rd slowest line. I think we've gotten to a good point that we should just let it be for now (at least I'm not going to try and optimize it further because I will be doing the refactoring below).

> > Also I noticed that `HomologyVectorSpaceWithBasis` represents a graded piece of the (co)homology space. Would you be opposed to me rewriting that such that it becomes the full (co)homology space/ring? I think it would simplify the overall code structure, allow easier extensions to infinite simplicial/cell complexes, and give a better interpretation of `cup_product` as being the product in the cohomology ring. (Also with #18175, we could then give work towards a cap product for manifolds.)
> 
> I think that it is natural to want both structures, the cohomology in a single degree and the cohomology in total. If you want to rewrite this part, that's okay with me.

There is a way to access the part in a single degree with the `basis` function by passing in an integer:

```
sage: s = SymmetricFunctions(QQ).s()
sage: list(s.basis(3))
[s[3], s[2, 1], s[1, 1, 1]]
```

This unfortunately doesn't work for most of the infinite dimensional CFM's, but there should be a generic method that works for all objects in `FiniteDimensionalModulesWithBasis`. At which point, we can use the `submodule` to construct the degree part (which also should have a dedicated method):

```
sage: s.submodule(list(s.basis(3)), already_echelonized=True)
Free module generated by {0, 1, 2} over Rational Field
```


> If you want to think about the most natural way to access cohomology classes, too, go ahead. I am not completely satisfied with
> {{{
> sage: a,b,c,d = X.cohomology_with_basis(1, QQ).gens()
> }}}
> Maybe
> {{{
> sage: H.<x> = X.cohomology_with_basis(1, QQ)
> }}}
> will define `x0`, ..., `x3` if the cohomology is 4-dimensional? Or x10, ..., x13? (The problem with the angle-bracket notation is that we shouldn't have to know how many generators there are ahead of time.)

What we could do is specify variable names and then could use the `inject_variables` method. I will think more about this tomorrow when I work on the above refactoring.


---

Comment by jhpalmieri created at 2015-10-12 19:05:38

Turns out that cup products for Delta complexes weren't too hard to implement, so I did that.
----
New commits:


---

Comment by git created at 2015-10-12 20:40:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-10-13 00:50:40

I'm still working on my refactoring, but I did #19397 for getting the degree `d` components.


---

Comment by tscrim created at 2015-10-13 20:33:07

Done. I spent so much time trying to get the `cup_product` to iterate over cohomology, but I realized that it was support to be over homology... Anyways, it works now. With the category framework, I was able to remove `__pow__` (at a small cost of a not correct error for negative powers, at least for now I didn't want to muck with the `AlgebrasWithBasis` code). So if you're happy with my changes, then you can set a positive review.
----
New commits:


---

Comment by jhpalmieri created at 2015-10-14 23:05:57

I will have some reviewer's changes on top of your changes soon. Meanwhile, I noticed that you removed the code related to the `FiniteDimensionalAlgebra` class. I don't know much about that class, and I don't mind the removal of that code. We could also reinstate it as a method for the class `CohomologyRing` ("exporting" it as a `FiniteDimensionalAlgebra`). Is that worth doing?


---

Comment by tscrim created at 2015-10-15 02:52:59

No, the `CohomologyRing` class takes the place of the `FiniteDimensionalAlgebra`. Was there something in that class that you were using that this version can't do? If there was, it is probably something we should generalize (on a followup ticket).


---

Comment by jhpalmieri created at 2015-10-15 04:30:35

There isn't anything that I was using, but it has some methods (`cardinality`, `is_unitary`, `is_commutative`) that I suppose some people might want.


---

Comment by tscrim created at 2015-10-15 13:08:39

The `cardinality` should work, but it is not there and is something we should implement in generality. A default `is_unitary` that returns `True` could perhaps go in `UnitalAlgebras`, but the cohomology ring is unital as the sum of the 0-th degree components, correct (you had this in your `__pow__` method too)? There should be a generic `is_commutative` test for finite dimensional algebras with basis. I will open up a separate ticket when I get to my office.


---

Comment by tscrim created at 2015-10-15 14:29:18

This is now #19416.


---

Comment by jhpalmieri created at 2015-10-15 18:57:15

Okay, your turn again. If you're happy with these changes, set it to positive review. A summary of my changes:

- various documentation fixes: some docstrings didn't get changed in your refactoring, some cross-references didn't work, etc.
- I moved several instances of `if base_ring is None` to the methods in `cell_complex.py`. Before, some were there but some were in `algebraic_topological_model.py`.
- I removed the explicit check about immutability for simplicial complexes because it wasn't being used: once we cache the method, immutability is checked as soon as the method is called, so checking again in the method is redundant. (And if we ever decide that the method should not be cached, there is no reason to check immutability.)


---

Comment by tscrim created at 2015-10-15 19:19:26

Then it is a positive review. This is a very nice addition to Sage which I'm hoping to get some good use from (especially once #18175 and more of SageManifolds gets merged in). Thanks for all your work.


---

Comment by tscrim created at 2015-10-15 19:20:04

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2015-10-15 19:50:06

Great! Thanks very much.


---

Comment by vbraun created at 2015-10-18 12:06:14

Resolution: fixed
