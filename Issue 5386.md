# Issue 5386: [with patch, needs review] simplicial complexes and their homology

Issue created by migration from https://trac.sagemath.org/ticket/5386

Original creator: jhpalmieri

Original creation time: 2009-02-26 16:23:40

Assignee: jhpalmieri

The attached patch implements simplicial complexes, chain complexes, and their homology. Some examples:

```
sage: S = SimplicialComplex(1, [[0], [1]])  # a two-point space
sage: S2 = S*S*S          # its three-fold join with itself; i.e., a 2-sphere
sage: S2
Simplicial complex with 6 vertices and 8 facets
sage: S2.homology()       # the reduced homology of S2
{0: 0, 1: 0, 2: Z}
sage: from sage.homology.examples import matching_complex
sage: M = matching_complex(8)
sage: sum(M.f_vector())   # total number of simplices in M
764
sage: M.homology(2)
Z^132
sage: from sage.homology.examples import torus, klein_bottle
sage: torus()
Simplicial complex with vertex set (0, 1, 2, 3, 4, 5, 6) and 14 facets
sage: klein_bottle()
Simplicial complex with 9 vertices and 18 facets
sage: klein_bottle().cohomology()
{0: 0, 1: Z, 2: C2}
sage: torus().product(klein_bottle())
Simplicial complex with 63 vertices and 1512 facets  
```


The code could be made much faster, I think (for example, by writing some of it in Cython); if anyone wants to undertake this, that would be great.  Otherwise, it might happen during Sage Days 15.



---

Comment by was created at 2009-04-12 08:00:13

Some things changed in sage-3.4.1.rc2, so this needs to be fixed (this is purely due to bitrot, not your fault):

```
wstein@sage:~/build/sage-3.4.1.rc2-ref2$ ./sage -t  devel/sage/sage/homology/simplicial_complex.py
sage -t  "devel/sage/sage/homology/simplicial_complex.py"   
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 863:
    sage: Z = SimplicialComplex(S, S.subsets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[3]>", line 1, in <module>
        Z = SimplicialComplex(S, S.subsets())###line 863:
    sage: Z = SimplicialComplex(S, S.subsets())
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/homology/simplicial_complex.py", line 693, in __init__
        if len(maximal_faces) == 0:
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/combinat/combinat.py", line 869, in __len__
        raise AttributeError, "__len__ has been removed; use .cardinality() instead"
    AttributeError: __len__ has been removed; use .cardinality() instead
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 864:
    sage: Z
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[4]>", line 1, in <module>
        Z###line 864:
    sage: Z
    NameError: name 'Z' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 866:
    sage: Z.n_faces(2)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[5]>", line 1, in <module>
        Z.n_faces(Integer(2))###line 866:
    sage: Z.n_faces(2)
    NameError: name 'Z' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 869:
    sage: Z.n_faces(2, subcomplex=K)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[7]>", line 1, in <module>
        Z.n_faces(Integer(2), subcomplex=K)###line 869:
    sage: Z.n_faces(2, subcomplex=K)
    NameError: name 'Z' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 887:
    sage: Z = SimplicialComplex(S, S.subsets()); Z
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[3]>", line 1, in <module>
        Z = SimplicialComplex(S, S.subsets()); Z###line 887:
    sage: Z = SimplicialComplex(S, S.subsets()); Z
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/homology/simplicial_complex.py", line 693, in __init__
        if len(maximal_faces) == 0:
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/combinat/combinat.py", line 869, in __len__
        raise AttributeError, "__len__ has been removed; use .cardinality() instead"
    AttributeError: __len__ has been removed; use .cardinality() instead
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 889:
    sage: Z.f_vector()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[4]>", line 1, in <module>
        Z.f_vector()###line 889:
    sage: Z.f_vector()
    NameError: name 'Z' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 905:
    sage: Z = SimplicialComplex(S, S.subsets()); Z
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_30[3]>", line 1, in <module>
        Z = SimplicialComplex(S, S.subsets()); Z###line 905:
    sage: Z = SimplicialComplex(S, S.subsets()); Z
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/homology/simplicial_complex.py", line 693, in __init__
        if len(maximal_faces) == 0:
      File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/local/lib/python2.5/site-packages/sage/combinat/combinat.py", line 869, in __len__
        raise AttributeError, "__len__ has been removed; use .cardinality() instead"
    AttributeError: __len__ has been removed; use .cardinality() instead
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage/sage/homology/simplicial_complex.py", line 907:
    sage: [Z._f_dict()[n] for n in range(-1, 4)]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_30[4]>", line 1, in <module>
        [Z._f_dict()[n] for n in range(-Integer(1), Integer(4))]###line 907:
    sage: [Z._f_dict()[n] for n in range(-1, 4)]
    NameError: name 'Z' is not defined
**********************************************************************
3 items had failures:
   4 of   8 in __main__.example_28
   2 of   7 in __main__.example_29
   2 of   7 in __main__.example_30
***Test Failed*** 8 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_simplicial_complex.py
         [3.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/homology/simplicial_complex.py"
Total time for all tests: 3.0 seconds
```



I think there is a bug in stanly_reisener_ring:

```
sage: S = SimplicialComplex(['a', 'b', 'c'], (('a', 'b'), ('a', 'c'), ('b', 'c')))
sage: S.stanley_reisner_ring()
Quotient of Multivariate Polynomial Ring in a, c, b over Integer Ring by the ideal (a*c*b)
sage: S.product(S).stanley_reisner_ring()
...
ValueError: variable names must be alphanumeric, but one is '('b', 'c')' which is not.
```


* It should be easier to get at all the standard examples of complexes, e.g., like with graphs if you do `graphs.<tab>` you get a bunch of graphs.  Could you make it so there is something like `complexes.<tab>` or something like that (which makes senses) and gives examples?

Please ping me once you fix the above, so I can give this _amazing patch_ (!) a positive review.


---

Comment by hivert created at 2009-04-13 09:20:30

Hi there,

Replying to [comment:1 was]:
>     AttributeError: __len__ has been removed; use .cardinality() instead

I found this one by googling through trac... This is due to #5308. See my comments there and on http://wiki.sagemath.org/sage-3.4.1 why we had to raise an error instead of issuing a deprecated warning. 

The fix is simple enough: as said in the error message to compute the number of `maximal_faces` you should ask `maximal_faces.cardinality()` which returns an arbitrary large sage integer and not call `len` which is specified to return a plain machine int.

Cheers,

Florent


---

Comment by jhpalmieri created at 2009-04-13 23:55:07

Here's a new patch, rebased against 3.4.1.rc2.  It passes all tests (with sage -tp -long) for me on sage.math.

I fixed the bug with the Stanley-Reisner ring.  It works now (although it's extremely slow).

> Could you make it so there is something like complexes.<tab> or something like that (which makes senses) and gives examples? 

I decided to use `simplicial_complexes`: since someone may want to add `simplicial_sets` or `CW_complexes` or other related things, having an unambiguous long name seemed better than having a shorter name which might collide with future use.  I also capitalized the examples, since that's how the graph examples work: `simplicial_complexes.Sphere`, etc.

Also, in the interests of full disclosure, the old version had some fishy math in it --  a routine which sped things up but depended on a conjecture. It shouldn't have been there in the first place, and I have excised it.

Florent, thanks for the comment, and even more, thanks for the helpful error message.  (It turns out that I was converting `maximal_faces` into a list anyway, so I just called `len` on that list; that was the easiest fix for my situation.  If someone tries to create a simplicial complex for which the number of maximal faces cannot be represented by a python int, I think this will be the least of their problems. :)


---

Attachment


---

Comment by mabshoff created at 2009-04-15 01:13:02

The new patch applies fine and does pass doctests. I cannot really judge if the bug William pointed out was fixed or not, so he has to take a look. With this patch applied we are at

```
Overall weighted coverage score:  67.8%
Total number of functions:  22931
We need   45 more function to get to 68% coverage.
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 02:06:41

After telling William that the len issue as well as the bug was fixed he gave this a verbal positive review. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 02:38:45

Resolution: fixed


---

Comment by mabshoff created at 2009-04-16 02:38:45

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
