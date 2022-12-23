# Issue 3042: [with patch; do not review yet] cyclolinalg -- make a new type for cyclotomic linear algebra

Issue created by migration from https://trac.sagemath.org/ticket/3042

Original creator: was

Original creation time: 2008-04-27 06:59:53

Assignee: was




---

Attachment


---

Comment by was created at 2008-04-27 23:41:39

this implements fast charpoly


---

Attachment


---

Attachment

current working state of code


---

Attachment


---

Attachment

multiply modular matrix multiply


---

Attachment

bring doctest coverage to 100%


---

Comment by craigcitro created at 2008-05-10 10:17:36

Cleaned up the code for submission. 

The code doesn't do everything we plan to do with cyclo linalg, but since William and I are both busy this week, and everything that we have written seems to work, we thought it would be a good idea to just go aheand and get this merged, and then start work on the next steps from here.


---

Comment by craigcitro created at 2008-05-10 10:18:06

single bundle with all patches


---

Attachment

Note: you can just grab the bundle, which has all the patches. (And one more that's not posted.) It applies clean against my 3.0.1.


---

Comment by robertwb created at 2008-05-14 20:48:37

Missing doctest for `matrix_modn_dense._matrix_from_rows_of_matrices()`


---

Comment by robertwb created at 2008-05-14 21:22:07

I noticed the reduction matrices are being cached on a matrix-by-matrix level. These should probably be stored in the parent (or somewhere else) so they don't have to be re-computed for every matrix (and every time the matrix changes). Also, it returns T, T^(-1). Is there any reason the second is not immutable as well (it should be, right?) 

In _echelon_form_multimodular, "This bound is chosen somewhat arbitrarily" is a bit worrisome. What goes wrong when the bound is wrong? An does it raise an, or erroneous results?


---

Comment by robertwb created at 2008-05-15 00:29:53

There appear to be some bugs in _echelon_form_multimodular: 


```
sage: W.<z> = CyclotomicField(13)
sage: A = matrix(W, 2, 3, [10^30*(1-z)^13, 1, 2, 3, 4, z])
sage: A._echelon_classical() == A._echelon_form_multimodular()
False
```


And are there really too few primes to do this one? 

```
sage: A = matrix(W, 2, 3, [(1-z)^13, 1, 2, 3, 4, z])
sage: A._echelon_classical() == A._echelon_form_multimodular()
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "matrix_cyclo_dense.pyx", line 1104, in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._echelon_form_multimodular (sage/matrix/matrix_cyclo_dense.c:7256)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/arith.py", line 811, in previous_prime
    raise ValueError, "no previous prime"
<type 'exceptions.ValueError'>: no previous prime

sage: A._echelon_classical().coefficient_bound()
23871924787556475149274876342835/2849139249552899187470100409441
sage: prod([p for p in primes(sage.ext.multi_modular.MAX_MODULUS) if p % 13 == 1])
3777251513472551076077323413984712447224167316569542746660443790944720456739178915286745295577103781126843302019912907604196976236003485285221719556179669453636811905438085596482829784342235500757320294587185652289723777313788948947369733451014766970786279026669485566707079065839096395383418625335034571612041781143149284913139656831918269059825575397626247469670012336804079354690420785029849300735172919872922995584851129959603354602808170507440635732852441428072064864085334573251785239858798057227493972262022733971317296298233438231746063843070820869647741947994945704743392311057306850712173626823797472600676991389384813525397983257094442271769939948500815064649800826545338433507178316863526248260164740558169380606346386397643686241448460203187163344489411512267768461313446894996332128711504082391842845381862817706825568011992657293783239895846550985331587872871229370080509231654747152558214319423850912597831209116025297512621589982472275725064778846114980865434182930872741392078714627106085706567140725130610336727505828306701243395125605943205970317723705355333081057943485921473543421777195079558251332463089067132625814430722751994806416511608705223132956304800932872260653445011983381010318280042523892109433136662909099512618814172251652083734728665060079588894770231102633396203262744051995844288154934856165892567710398481566838353248537819019736350260710552547235859435174075305752734609243968018456107437630199888147411291639496714704328985408300360076259065500406914330358492243832817365732409549059940799027892958118397298889175369550629228320746277600577874440513085673177629075313539299510189466259436627347127723606624695323564558898279

```



---

Attachment

The code looks good, is well documented, and fast. Aside from the errors in _echelon_form_multimodular it seems to work as advertised. 

I added a patch illustrating what _reduction_matrix actually does, as this seems central to the ideas behind the algorithms. There needs to be at least a paragraph or two at the top explaining the storage format and ideas behind the algorithm (maybe the example I posted belongs there)--if I hadn't had it explained to me it would have probably taken a while to get the "big picture" from the code. 

Once these issues are all solved, I think it's ready.


---

Comment by craigcitro created at 2008-06-02 08:09:18

I'm adding a patch that should address all of the above issues. There were two bugs in multimodular echelon form, which are now both gone. I've added a few new doctests, as well as a (fairly brief) paragraph with a description of the underlying data structure. I think that this code should be ready to merge.


---

Attachment

Warning: I just realized that I didn't have Robert's patch applied when I made mine, so I could cause some merge troubles with my patch. If there are any actual conflicts, let me know and I'll just make one big new bundle.


---

Comment by robertwb created at 2008-06-05 09:56:07

The new patch applies fine on top of mine, and appears to resolve all my issues. Merge

- trac-3042.hg

- 3042-illustrative-doctest.patch

- trac-3042-extra2.patch


---

Comment by mabshoff created at 2008-06-06 05:17:42

Arrg, death to bundles!:

```
<<<<<<< /scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/devel/sage-main/sage/matrix/matrix0.pyx.orig.1332311558
            print self
            print self.nrows()
            print self.dict()
            print self
            print self.nrows()
            print self.dict()
            self.save('/home/was/a')
=======
>>>>>>> /tmp/matrix0.pyx~other.9d-xm6
```

The fix is obvious in this case since the reject was cause by a fix by malb. 
||||||| /tmp/matrix0.pyx~base.rLNaqj
Cheers,

Michael


---

Comment by mabshoff created at 2008-06-06 05:36:36

With the three patches applied I am seeing:

```
sage -t -long devel/sage/sage/graphs/graph.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/graph.py", line 6094:
    sage: M.determinant()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_138[8]>", line 1, in <module>
        M.determinant()###line 6094:
    sage: M.determinant()
      File "matrix2.pyx", line 755, in sage.matrix.matrix2.Matrix.determinant (sage/matrix/matrix2.c:4431)
      File "matrix_cyclo_dense.pyx", line 817, in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense.charpoly (sage/matrix/matrix_cyclo_dense.c:4714)
      File "matrix_cyclo_dense.pyx", line 910, in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._charpoly_multimodular (sage/matrix/matrix_cyclo_dense.c:5505)
    RuntimeError: we ran out of primes in multimodular charpoly algorithm.
**********************************************************************
1 items had failures:
   1 of  30 in __main__.example_138
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/.doctest_graph.py
```

and also

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/tmp/tut.py", line 2461:
    : S.q_expansion_basis(10)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_109[7]>", line 1, in <module>
        S.q_expansion_basis(Integer(10))###line 2461:
    : S.q_expansion_basis(10)
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 548, in q_expansion_basis
        P = self.plus_submodule(compute_dual=True)
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1337, in plus_submodule
        return self.sign_submodule(+1, compute_dual)
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1414, in sign_submodule
        P = self._compute_sign_submodule(sign, compute_dual)
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1363, in _compute_sign_submodule
        Y = self.dual_free_module()
      File "/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 284, in dual_free_module
        V = T.kernel_on(V, poly=f, check=False)
      File "matrix2.pyx", line 1685, in sage.matrix.matrix2.Matrix.kernel_on (sage/matrix/matrix2.c:8517)
      File "matrix2.pyx", line 2249, in sage.matrix.matrix2.Matrix.restrict (sage/matrix/matrix2.c:12994)
      File "matrix0.pyx", line 1624, in sage.matrix.matrix0.Matrix.pivots (sage/matrix/matrix0.c:8826)
    RuntimeError: BUG: matrix pivots should have been set but weren't, matrix parent = 'Full MatrixSpace of 4 by 4 dense matrices over Cyclotomic Field of order 6 and degree 2'
**********************************************************************
```


So, something finishy going on here. This is 3.0.3.alpha1 + the three patches Robert recommended merging:

```
changeset:   9818:7817fe6a0d6e
tag:         tip
user:        Craig Citro <craigcitro@gmail.com>
date:        Mon Jun 02 00:55:24 2008 -0700
summary:     Fix for multimodular echelon over cyclotomic fields (trac #3042).

changeset:   9817:806d207778c7
user:        Robert Bradshaw <robertwb@math.washington.edu>
date:        Wed May 14 17:59:14 2008 -0700
summary:     Clarifying example of reduction matrix.

changeset:   9816:7ddb4a791455
parent:      9806:0af1c676d9e5
parent:      9815:8783f32b83b7
user:        mabshoff@sage.math.washington.edu
date:        Thu Jun 05 22:15:16 2008 -0700
summary:     Merge previous bundle

changeset:   9815:8783f32b83b7
user:        Craig Citro <craigcitro@gmail.com>
date:        Sat May 10 03:14:26 2008 -0700
summary:     Clean up cyclo linalg for submission/review.

changeset:   9814:aef7e4acdb60
user:        William Stein <wstein@gmail.com>
date:        Mon May 05 10:11:25 2008 -0700
summary:     Trac #3042  -- bring doctest coverage for matrix cyclo dense up to 100%

changeset:   9813:1c24dad1f78d
user:        Craig Citro <craigcitro@gmail.com>
date:        Mon May 05 04:50:47 2008 -0700
summary:     cyclo lin alg -- speeding up echelon form snapshot

changeset:   9812:a516cca10e1a
user:        William Stein <wstein@gmail.com>
date:        Thu May 01 22:25:12 2008 -0700
summary:     Some code cleanup.  Implement first FAST mul method for matrices over cyclotomic fields; result is quite good a
lready.

changeset:   9811:6a118d331705
user:        Craig Citro <craigcitro@gmail.com>
date:        Thu May 01 03:07:52 2008 -0700
summary:     Working on cyclotomic linear algebra ...

changeset:   9810:0c692edc3b07
user:        Craig Citro <craigcitro@gmail.com>
date:        Wed Apr 30 17:33:59 2008 -0700
summary:     Current working state of cyclo-linalg.

changeset:   9809:65bba2b67f19
user:        Craig Citro <craigcitro@gmail.com>
date:        Mon Apr 28 05:17:28 2008 -0700
summary:     Working on cyclolinalg

changeset:   9808:a8772459a254
user:        William Stein <wstein@gmail.com>
date:        Sun Apr 27 16:35:36 2008 -0700
summary:     cyclotomic linear algebra -- part 2 -- implement first version of class along with fast multimodular charpoly.

changeset:   9807:f503079549c5
parent:      9669:23d0e6b6a675
user:        William Stein <wstein@gmail.com>
date:        Sat Apr 26 23:53:59 2008 -0700
summary:     cyclotomic linear algebra -- very initial demo type.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-06-06 05:55:39

There are actually a bunch of related failures:

```
        sage -t -long devel/sage/sage/modular/modsym/tests.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modsym/space.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/modform/cuspidal_submodule.py # 7 doctests failed
        sage -t -long devel/sage/sage/modular/modform/space.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/eisenstein_submodule.py # 1 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/modform/element.py # 9 doctests failed
        sage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed
        sage -t -long devel/doc/tut/tut.tex # 1 doctests failed
```

William: feel free to use my build in 

/scratch/mabshoff/release-cycle/sage-3.0.3.alpha2

Cheers,

Michael


---

Comment by robertwb created at 2008-06-06 16:50:41

A note on 


```
    RuntimeError: we ran out of primes in multimodular charpoly algorithm.
```


This sounds a lot like the original bad case I found, which now works but is much slower than the classical echelon. Perhaps there should be a better heuristic falling back to classical? (Or, hopefully, there's still a bug in picking the bound).


---

Comment by mabshoff created at 2008-06-06 19:59:46

Replying to [comment:13 robertwb]:
> A note on 
> 
> {{{
>     RuntimeError: we ran out of primes in multimodular charpoly algorithm.
> }}}
> 
> This sounds a lot like the original bad case I found, which now works but is much slower than the classical echelon. Perhaps there should be a better heuristic falling back to classical? (Or, hopefully, there's still a bug in picking the bound). 


Hi Robert,

my guess would be that the bound then gets miscomputed on a 64 bit box. IIRC all you three authors of the patch set did code and test this patch set in 32 bit mode on OSX. 

Thoughts?

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-06 20:34:03

If no one else wants to deal with this, I'll look at it next Weds when I get to Seattle. I'm happy to take care of it then.


---

Attachment

Merged 

 * trac-3042.hg
 * 3042-illustrative-doctest.patch
 * trac-3042-extra2.patch 
 * trac-3042-edge_cases.patch

in Sage 3.0.3.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-08 22:26:31

Resolution: fixed
