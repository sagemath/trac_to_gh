# Issue 6312: optional doctest failure -- galois_group

Issue created by migration from https://trac.sagemath.org/ticket/6312

Original creator: was

Original creation time: 2009-06-16 14:41:04

Assignee: tbd

CC:  davidloeffler


```
sage -t -long --optional devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/number_field/number_field.py", line 3107:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)    # optional - database_gap
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_69[15]>", line 1, in <module>
        NumberField(x**Integer(3) + Integer(2)*x + Integer(1), 'a').galois_group(pari_group=False)    # optional - database_gap###line 3107:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)    # optional - database_gap
    TypeError: galois_group() got an unexpected keyword argument 'pari_group'
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/number_field/number_field.py", line 3109:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma, , database_gap
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_69[16]>", line 1, in <module>
        NumberField(x**Integer(3) + Integer(2)*x + Integer(1), 'a').galois_group(algorithm='magma')   # optional - magma, , database_gap###line 3109:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma, , database_gap
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3133, in galois_group
        return self._galois_group_cached(type, algorithm, names)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/misc/cachefunc.py", line 242, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 3147, in _galois_group_cached
        return GaloisGroup_v2(self, names)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/galois_group.py", line 183, in __init__
        self._galois_closure, self._gc_map = number_field.galois_closure(names=names, map=True)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5103, in galois_closure
        L, self_into_L = self._galois_closure_and_embedding(names)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 5042, in _galois_closure_and_embedding
        L = K.change_names(names)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4679, in change_names
        return self.absolute_field(names)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 1292, in absolute_field
        K = NumberField(self.defining_polynomial(), names, cache=False)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 380, in NumberField
        raise TypeError, "You must specify the name of the generator."
    TypeError: You must specify the name of the generator.

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
1 items had failures:
   2 of  22 in __main__.example_69
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_number_field.py
	 [20.7 s]
```



---

Comment by fwclarke created at 2009-06-16 18:10:14

The attached patch deals with the first of these. (I don't have magma, so can't see what the problem is for the other failure.)


---

Attachment


---

Comment by fwclarke created at 2009-06-17 06:53:06

I now suspect (but can't check) that the second failure does not lie with 
the use of magma but arises because the type was undefined.  
The doctest comment anyway 
indicates that the type should have been set to 'gap', so I've fixed 
that.  But this needs to be checked by someone with magma.

It turns out that leaving both `type` and `names` as `None` always causes a failure when the field 
is not Galois since no name is then provided for a generator of the 
Galois closure.  This has been fixed in the new patch, and a doctest adjusted appropriately.


---

Attachment


---

Comment by davidloeffler created at 2009-06-17 10:34:17

I concur with fwclarke's diagnosis -- the traceback indicates that magma's not getting called, it's using the new code I wrote (wrapping Pari). This is just a hangover from ticket #5159: I changed the arguments to galois_group, and didn't check I'd fixed the optional doctests (it took about five attempts just to get the non-optional ones to work!). And it looks like nobody else checked them either until now.

The patches look spot on based on browsing the code, but I am at a conference at the moment so don't have time to download and test them (and I don't have Magma either).

David


---

Comment by cremona created at 2009-07-16 07:11:09

I'm at a conference but do have magma so will look at these!


---

Comment by cremona created at 2009-07-16 18:30:26

Review: I applied both patches to 4.1 and ran the test on a machine with magma but (first) without the gap_database installed.  This gave a similar error:

```
sage -t -long --optional "devel/sage/sage/rings/number_field/number_field.py"
**********************************************************************
File "/home/john/sage-4.1/devel/sage/sage/rings/number_field/number_field.py", line 3101:
    sage: NumberField(x^2+2, 'a').galois_group(type="gap")  # optional - database_gap
Expected:
    Galois group Transitive group number 1 of degree 2 of the Number Field in a with defining polynomial x^2 + 2
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 1 of degree 2 of the Number Field in a with defining polynomial x^2 + 2
**********************************************************************
File "/home/john/sage-4.1/devel/sage/sage/rings/number_field/number_field.py", line 3103:
    sage: NumberField(x^3-2, 'a').galois_group(type="gap")  # optional - database_gap
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
**********************************************************************
File "/home/john/sage-4.1/devel/sage/sage/rings/number_field/number_field.py", line 3109:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(type="gap")          # optional - database_gap
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
File "/home/john/sage-4.1/devel/sage/sage/rings/number_field/number_field.py", line 3111:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(type="gap", algorithm="magma")   # optional - magma,  database_gap
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
1 items had failures:
   4 of  23 in __main__.example_69
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/john/sage-4.1/tmp/.doctest_number_field.py
	 [23.7 s]
exit code: 1024
```


I do not know why it is running the test which has the tag  # optional - database_gap.  Is that tag formatted correctly?

Then I installed gap_packages-4.4.10_6.spkg.   and database_gap-4.4.10.spkg.  After that, the tests in that file all pass (with long, with and without optional)

Pass!


---

Comment by mvngu created at 2009-07-19 16:01:46

With both patches, I'm seeing this doctest failure:

```
sage -t -long devel/sage-exp/sage/rings/number_field/galois_group.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/number_field/galois_group.py", line 171:
    sage: NumberField(x^3 - 2, 'b').galois_group()
Expected:
    Traceback (most recent call last):
    ...
    TypeError: You must specify the name of the generator.
Got:
    Galois group of Galois closure in b0 of Number Field in b with defining polynomial x^3 - 2
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_9
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_galois_group.py
	 [6.7 s]
```

Incidentally, after running all doctests a second time, I get a doctest failure in the plotting code:

```
sage -t -long devel/sage-exp/sage/graphs/graph_plot.py
libpng error: Image width or height is zero in IHDR
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/graphs/graph_plot.py", line 758:
    sage: g.graphplot(edge_labels=True, color_by_label=True, edge_style='dashed').plot()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[73]>", line 1, in <module>
        g.graphplot(edge_labels=True, color_by_label=True, edge_style='dashed').plot()###line 758:
    sage: g.graphplot(edge_labels=True, color_by_label=True, edge_style='dashed').plot()
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1346)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 873, in _repr_
        self.show()
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 1360, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 1683, in save
        canvas.print_figure(filename, dpi=dpi)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1453, in print_figure
        **kwargs)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 334, in print_png
        filename_or_obj, self.figure.dpi)
    RuntimeError: Error building image
**********************************************************************
1 items had failures:
   1 of  74 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_graph_plot.py
	 [13.0 s]
```

This failure didn't appear after running all doctests for a third time. Hmmm... strange.


---

Comment by cremona created at 2009-07-19 17:01:13

I added David Loeffler to the CC list since this seems to move into his territory.  

The plotting thing is a a random test failure which has been seen before, isn't it?


---

Comment by cremona created at 2009-07-19 17:01:13

Changing keywords from "" to "Number Field Galois group".


---

Comment by jdemeyer created at 2014-09-02 09:26:04

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2014-09-02 09:26:04

The `optional - database_gap` tests do pass. I don't know about `magma`, but let's assume that these got fixed also.


---

Comment by vbraun created at 2014-09-09 14:53:16

Resolution: fixed
