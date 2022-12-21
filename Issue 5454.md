# Issue 5454: [with patch, needs review] Add coercion documentation to the reference manual

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-03-07 19:18:38

Assignee: tba

CC:  robertwb




---

Attachment


---

Comment by robertwb created at 2009-03-07 22:00:20

sage/structure/coerce* should probably still be in the reference manual.


---

Comment by mhansen created at 2009-03-07 22:01:10

They are under the coercion section at the bottom.


---

Comment by robertwb created at 2009-03-07 22:23:44

/me should read the patch more carefully. I haven't applied it, but it looks good. 

Just as an aside, based on some conversations with people, I'm thinking about getting rid of _l_action_ and _r_action_ (replacing with _act_on_ and _acted_upon_). Thoughts?


---

Comment by mhansen created at 2009-03-07 22:27:59

Something other than _l_action_ and _r_action_!  I don't know if _act_on_ and _acted_upon_ are better though.  In every case I've ever used it, I'm always defining how things act on my element from the left or the right (modules) in which case _l_action_ and _r_action_ are reversed.


---

Comment by robertwb created at 2009-03-07 22:45:20

_act_on_ would be self acting on something, _acted_upon_ would be something acting on self. They would both take a self_on_left argument. I'm open for other names, but haven't come up with any yet. 

BTW, thanks for rebasing those other patches.


---

Comment by mhansen created at 2009-03-07 22:48:59

That convention sounds good to me, but we would then have to tell people to only implement one of them.


---

Comment by robertwb created at 2009-03-12 02:53:48

BTW, the only reason I haven't given this a positive review is because of the potential renaming of _l_action_.


---

Comment by davidloeffler created at 2009-06-10 10:27:03

rebased to 4.0.1


---

Attachment

It looks like the proposed renaming of _l_action_ etc hasn't yet happened, and we *seriously need* some documentation for the coercion model -- I've written or contributed to dozens of sage parent/element classes and I never knew half of this stuff, I learnt loads just from a five-minute skim-read of the new docs. We must get this into a release ASAP.

It's a great shame that this patch has been in limbo for three months just because our hackish use of text search for "positive review" in the summary field missed it due to a typo.


---

Comment by robertwb created at 2009-06-10 16:05:14

Yes, it is a shame. I got busy with other stuff, like working on my thesis... Here's the renaming patch #5597. The categories patch is holding up lots of good examples.


---

Comment by ncalexan created at 2009-06-13 20:08:57

Unfortunately:


```
sage -t -long devel/sage/doc/en/reference/coercion.rst
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 206:
    age: cm = sage.structure.element.get_coercion_model()
Expected:
    <sage.structure.coerce.CoercionModel_cache_maps object at 0x2f65960>
Got nothing
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 235:
    age: cm.bin_op(77, 9, gcd)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        cm.bin_op(Integer(77), Integer(9), gcd)###line 235:
    age: cm.bin_op(77, 9, gcd)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 244:
    age: cm.explain(ZZ['x'], ZZ, operator.mul)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        cm.explain(ZZ['x'], ZZ, operator.mul)###line 244:
    age: cm.explain(ZZ['x'], ZZ, operator.mul)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 250:
    age: cm.explain(ZZ['x'], ZZ, operator.div)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/ncalexan/sage-4.0.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        cm.explain(ZZ['x'], ZZ, operator.div)###line 250:
    age: cm.explain(ZZ['x'], ZZ, operator.div)
    NameError: name 'cm' is not defined
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-nca/doc/en/reference/coercion.rst", line 631:
    age: sage.categories.pushout.pushout(Frac(ZZ['x,y,z']), QQ['z, t'])
Expected:
    Fraction Field of Multivariate Polynomial Ring in x, y, z, t over Rational Field
Got:
    Univariate Polynomial Ring in t over Fraction Field of Multivariate Polynomial Ring in x, y, z over Rational Field
**********************************************************************
4 items had failures:
   1 of   6 in __main__.example_2
   1 of   3 in __main__.example_3
   2 of  11 in __main__.example_4
   1 of   3 in __main__.example_6
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/ncalexan/sage-4.0.2.alpha1/tmp/.doctest_coercion.py
         [1.2 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/doc/en/reference/coercion.rst # 5 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1.5 seconds
Tests failed!
```



---

Comment by davidloeffler created at 2009-06-14 10:45:54

apply over trac_5454_rebase.patch


---

Attachment

I've fixed the above problems, which were all due to trivial typos/thinkos in the doctests. Silly of me not to have run the tests when I was reviewing. Can I just reinstate the positive review, or do we need a second opinion?


---

Comment by ncalexan created at 2009-06-14 21:30:16

Resolution: fixed
