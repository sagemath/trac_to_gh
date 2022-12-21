# Issue 8302: cubical complexes, delta complexes, and more

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-02-19 02:28:51

Assignee: jhpalmieri

CC:  sault bantieau mhampton

The attached patch adds lots of functionality to Sage's algebraic topology capabilities:

 - it implements cubical complexes: complexes constructed from cubes of various dimensions, glued together in prescribed ways.

 - it implements Delta complexes: this is a variant on a simplicial complex which allows for more efficient construction of many spaces.  For example, the minimal triangulation of the torus as a simplicial complex uses 14 triangles, while there is a Delta complex version with only two triangles.  Allen Hatcher uses these in his popular algebraic topology book.

 - it "implements" generic cell complexes, as a parent class to the previous two, and also to simplicial complexes.  This is not intended for use by casual Sage users, but instead for developers who want to add another kind of complex (CW complexes?  Prodsimplicial complexes?)  Many methods in this class are not implemented, but instead provide a template of what should be implemented in any derived class.

 - it modifies simplicial complexes a bit, allowing them to be defined without specifying a vertex set: just list the maximal simplices and it will deduce what the vertex set is.  It also defines `connected_sum` for arbitrary simplicial complexes, not just simplicial surfaces, with a warning that it's not well-defined if you don't call it on manifolds.  It renames `ProjectivePlane` to `RealProjectivePlane` (keeping the old name as an alias for backward compatibility).

 - it provides an interface to CHomP, which is now an experimental spkg for Sage.  CHomP provides programs to compute homology which are faster than anything Sage can do.  See [http://chomp.rutgers.edu/](http://chomp.rutgers.edu/) for more information.

 - it changes how the `homology` and `chain_complex` methods work: these now pass keywords to each other, so it's easy to implement new keywords: just implement it for `ChainComplex.homology`, for instance, and when you compute the homology of any simplicial complex, you can give it the keyword and it will get passed on to this method.


---

Comment by jhpalmieri created at 2010-02-19 02:29:29

Changing status from new to needs_review.


---

Attachment


---

Comment by mhampton created at 2010-02-25 23:24:17

Documentation looks fantastic.

All tests pass, 100% coverage.  Only coverage issue is that a few files bring up a

```
ERROR: Please add a `TestSuite(s).run()` doctest.
```

error from sage -coverage.  Its unclear to me how important that is.

I will test this out a little more before giving a positive review.


---

Comment by mhampton created at 2010-02-26 01:46:12

Changing assignee from jhpalmieri to mhampton.


---

Comment by mhampton created at 2010-02-26 01:46:12

In several modules, instead of INPUT and OUTPUT blocks, "parameter" or "param" is used, or "results".  It would be better if these conformed more to the official conventions.  I don't think this is reason enough to block the inclusion of all this functionality though - the functions are very well described otherwise.


---

Comment by mhampton created at 2010-02-26 01:46:56

Changing assignee from mhampton to jhpalmieri.


---

Comment by jhpalmieri created at 2010-02-26 02:31:11

Replying to [comment:5 mhampton]:
> In several modules, instead of INPUT and OUTPUT blocks, "parameter" or "param" is used, or "results".  It would be better if these conformed more to the official conventions.

Just so you know, the :param: form is the official Sphinx/reST format.  It's mentioned (briefly) in the Sage developer's guide: see the third bullet point [here](http://www.sagemath.org/doc/developer/conventions.html#documentation-strings).


---

Comment by mhampton created at 2010-02-26 03:17:39

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-02-26 03:17:39

Ah, sorry, I had missed that in the developer's guide.  My apologies.  It seems like we should choose one or the other, but that's a debate for another time and place.

I installed CHomP on several machines and encountered no problems.  Didn't try yet on Solaris but if that works OK then maybe it can be moved into optional soon.

I see no reason not to give this a positive review.


---

Comment by mvngu created at 2010-03-02 11:29:29

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-03-02 11:29:29

I got the following doctest failures after applying [Cell_complexes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/Cell_complexes.patch) to Sage 4.3.3:

```sh
[mvngu`@`sage sage-4.3.3]$ ./sage -t -long devel/sage-main/sage/structure/sage_object.pyx
sage -t -long "devel/sage-main/sage/structure/sage_object.pyx"
**********************************************************************
File "/dev/shm/mvngu/release/sage-4.3.3/devel/sage-main/sage/structure/sage_object.pyx", line 1001:
    sage: print "x"; sage.structure.sage_object.unpickle_all(std)
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    ** failed:  _class__sage_homology_examples_SimplicialSurface__.sobj
    Failed:
    _class__sage_homology_examples_SimplicialSurface__.sobj
    Successfully unpickled 570 objects.
    Failed to unpickle 1 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_sage_object.py
	 [5.3 s]
```

I don't know how to explain the above failure. Also note the following failure directly resulting from [Cell_complexes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/Cell_complexes.patch):

```sh
[mvngu`@`sage sage-4.3.3]$ ./sage -t -long devel/sage-main/sage/interfaces/chomp.py
sage -t -long "devel/sage-main/sage/interfaces/chomp.py"    
**********************************************************************
File "/dev/shm/mvngu/release/sage-4.3.3/devel/sage-main/sage/interfaces/chomp.py", line 564:
    sage: homchain(C2, generators=True, base_ring=GF(2))[2]
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/release/sage-4.3.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.3.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.3.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[5]>", line 1, in <module>
        homchain(C2, generators=True, base_ring=GF(Integer(2)))[Integer(2)]###line 564:
    sage: homchain(C2, generators=True, base_ring=GF(2))[2]
      File "/dev/shm/mvngu/release/sage-4.3.3/local/lib/python/site-packages/sage/interfaces/chomp.py", line 584, in homchain
        return CHomP()('homchain', complex, **kwds)
      File "/dev/shm/mvngu/release/sage-4.3.3/local/lib/python/site-packages/sage/interfaces/chomp.py", line 145, in __call__
        raise OSError, "Program %s not found" % program
    OSError: Program homchain not found
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_chomp.py
	 [1.8 s]
```

I think the failure results from a missing "# optional" comment on line 564 of the module `sage/interfaces/chomp.py`. Something like the following change would fix the above failure:

```diff
diff -r 0fa662e0a843 sage/interfaces/chomp.py
--- a/sage/interfaces/chomp.py
+++ b/sage/interfaces/chomp.py
`@``@` -561,7 +561,7 `@``@`
         sage: C2 = delta_complexes.Sphere(2).chain_complex()
         sage: homchain(C2, generators=True)[2]  # optional: need CHomP
         (Z, [(1, -1)])
-        sage: homchain(C2, generators=True, base_ring=GF(2))[2]
+        sage: homchain(C2, generators=True, base_ring=GF(2))[2]  # optional: need CHomP
         (Vector space of dimension 1 over Finite Field of size 2, [(1, 1)])
 
     TESTS:
```



---

Attachment

apply on top of previous patch


---

Comment by mvngu created at 2010-03-02 13:04:00

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-03-02 13:04:00

I have attached a reviewer patch fixing the reported failure where the CHomP spkg is not installed. Only this reviewer patch needs reviewing by anyone but me. 

John: When this ticket is closed, do you also want the CHomP spkg at

http://sage.math.washington.edu/home/palmieri/SPKG/chomp-20100213.p1.spkg

to be uploaded to the experimental spkg repository?


---

Comment by jhpalmieri created at 2010-03-02 17:58:09

Marshall's patch gets a positive review.  I've attached another small patch to deal with the pickling problem.  I had deleted the class `SimplicialSurface` since with the patch it doesn't provide anything extra compared to `SimplicialComplex`.  The new patch just makes `SimplicialSurface` a synonym for `SimplicialComplex`.  This fixes the pickling problem for me.


---

Comment by jhpalmieri created at 2010-03-02 18:01:24

Replying to [comment:10 mvngu]:

> John: When this ticket is closed, do you also want the CHomP spkg at
> 
> http://sage.math.washington.edu/home/palmieri/SPKG/chomp-20100213.p1.spkg
> 
> to be uploaded to the experimental spkg repository?

Yes, that would be good.  William already uploaded an earlier version, so I don't even think it has to wait for this ticket to be closed...


---

Comment by mvngu created at 2010-03-02 19:12:13

With [trac_8302-pickle.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/trac_8302-pickle.patch), the pickling issue reported above is fixed.


---

Comment by mvngu created at 2010-03-02 19:12:13

Changing status from needs_review to positive_review.


---

Attachment

apply on top of other patches


---

Comment by jhpalmieri created at 2010-03-02 19:37:38

I just changed the pickle patch: I just added a comment.  The old version had

```
SimplicialSurface = SimplicialComplex 
```

and the new version has

```
# for backwards compatibility:  
SimplicialSurface = SimplicialComplex 
```

I don't think this needs to be reviewed again...


---

Comment by mvngu created at 2010-03-03 02:19:25

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 02:19:25

Merged in this order:

 1. [Cell_complexes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/Cell_complexes.patch)
 1. [trac_8302-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/trac_8302-reviewer.patch)
 1. [trac_8302-pickle.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8302/trac_8302-pickle.patch)
 1. Merged [chomp-20100213.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/chomp-20100213.p1.spkg) in the experimental spkg repository at http://www.sagemath.org/packages/experimental.


---

Comment by jhpalmieri created at 2010-03-03 02:31:37

By the way, Marshall, thanks for reviewing this!
