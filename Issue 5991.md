# Issue 5991: Add as tandard constructor for dynamic classes

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-05 22:04:01

Assignee: nthiery

CC:  sage-combinat saliola roed

Keywords: dynamic classes, pickling, unique representation

This patch implements sage.structure.dynamic_class.dynamic_class, for constructing dynamically new python classes. The constructed classes can be pickled, and have unique representation.

Depends on #5985 for the pickling and #5120

Used by the upcoming category framework #5891, (and sage-words?)


---

Comment by nthiery created at 2009-05-08 23:19:15

Patch updated for new version of #5120
Please ignore  dynamic_class-5991-submitted.2.patch


---

Comment by nthiery created at 2009-05-19 06:26:23

Changing status from new to assigned.


---

Attachment


---

Comment by roed created at 2009-05-21 09:04:44

Looks good.  Doctests pass.


---

Comment by ncalexan created at 2009-06-13 22:00:57

Since this depends on #5985 which does not have a positive review it will have to wait.


---

Comment by boothby created at 2009-06-24 18:34:40

Doctest failures:


```
sage -t -long devel/sage/sage/structure/dynamic_class.py
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/dynamic_class.py", line 210:
    sage: loads(dumps(BarFoo))
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[23]>", line 1, in <module>
        loads(dumps(BarFoo))###line 210:
    sage: loads(dumps(BarFoo))
      File "sage_object.pyx", line 604, in sage.structure.sage_object.dumps (sage/structure/sage_ob$
        return comp.compress(cPickle.dumps(obj, protocol=2))
    PicklingError: Can't pickle <class '__main__.BarFoo'>: attribute lookup __main__.BarFoo failed
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/dynamic_class.py", line 224:
    sage: import sage.misc.cPickle as cPickle
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[30]>", line 1, in <module>
        import sage.misc.cPickle as cPickle###line 224:
    sage: import sage.misc.cPickle as cPickle
    ImportError: No module named cPickle
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/dynamic_class.py", line 225:
    sage: cPickle.loads(cPickle.dumps(FooBar)) == FooBar
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[31]>", line 1, in <module>
        cPickle.loads(cPickle.dumps(FooBar)) == FooBar###line 225:
    sage: cPickle.loads(cPickle.dumps(FooBar)) == FooBar
    NameError: name 'cPickle' is not defined
**********************************************************************
File "/space/boothby/sage-4.0.3/devel/sage-main/sage/structure/dynamic_class.py", line 238:
    sage: loads(dumps(FooUnique)) is FooUnique
Exception raised:
    Traceback (most recent call last):
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/boothby/sage-4.0.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[35]>", line 1, in <module>
        loads(dumps(FooUnique)) is FooUnique###line 238:
    sage: loads(dumps(FooUnique)) is FooUnique
      File "sage_object.pyx", line 604, in sage.structure.sage_object.dumps (sage/structure/sage_ob$
        return comp.compress(cPickle.dumps(obj, protocol=2))
    PicklingError: Can't pickle <class '__main__.Foo'>: it's not the same object as __main__.Foo
**********************************************************************
1 items had failures:
   4 of  36 in __main__.example_1
***Test Failed*** 4 failures.
```



---

Comment by nthiery created at 2009-06-24 20:38:26

Yeah: it depends on #5985, but otherwise is ready.

Should there be a new field in the trac server for listing systematically the other tickets the ticket depends on?


---

Attachment

The two added patches, by David and myself improve introspection.
I give a positive review on David's. David, can you double check mine?


---

Attachment

Replying to [comment:11 nthiery]:
> The two added patches, by David and myself improve introspection.
> I give a positive review on David's. David, can you double check mine?

The updated referee patch by myself adds a copyright header, and fixes a warning in sage -docbuild.

David: please double check!


---

Attachment

Fix reduction after David's referee patch


---

Comment by nthiery created at 2009-07-17 22:40:36

Fold of all the patches above. Apply only this one


---

Attachment

David: can you have a quick look at my latest addition, and set a positive review (pending #5985)


---

Comment by roed created at 2009-07-18 07:12:32

So, I approve the changes.  I don't have time right now to run doctests though: the release manager (or someone) should make sure to do so.


---

Comment by nthiery created at 2009-07-18 09:02:03

Replying to [comment:14 roed]:
> So, I approve the changes.  I don't have time right now to run doctests though: the release manager (or someone) should make sure to do so.

Thanks! All the doctest pass on my machine, but yes, a triple check would be good.


---

Comment by nthiery created at 2009-10-11 08:52:16

If #5985 is ready on time to get integrated in 4.1.2, it would be great to have this on go in too.


---

Comment by was created at 2009-10-14 03:45:48

NOTE to self -- the change to sageinspect needs to be ported into the separated notebook when this is merged.


---

Attachment


---

Comment by mhansen created at 2009-10-15 07:15:24

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 07:15:24

I had to make the change to the way cPickle is imported as in #5985.  I'll make a new ticket for sageinspect in the separated notebook.
