# Issue 7448: Improve sphinx rendering of categories in reference manual.

Issue created by migration from https://trac.sagemath.org/ticket/7448

Original creator: hivert

Original creation time: 2009-11-12 20:45:17

Assignee: hivert

CC:  mhansen nthiery jhpalmieri

Keywords: Sphinx categories.

Since #7443, categories now appear in the reference manual. But Sphinx rendering in very poor. In particular, I can't manage to get nested class appearing in the doc though I've read that they are supported by Sphinx. Once someone (Mike ?) explain me the solution, I'll be glad to implement it. 

Cheers,

Florent


---

Comment by hivert created at 2009-11-12 20:45:47

Changing status from new to needs_info.


---

Comment by mhansen created at 2009-11-13 06:54:10

See #6664.  We need to figure out how to resolve the issues there.


---

Comment by mpatel created at 2010-02-16 22:04:49

Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).

Is there a minimal example we can submit that reproduces the problem?


---

Comment by hivert created at 2010-02-17 20:31:23

Replying to [comment:3 mpatel]:
> Mistaking inner classes for aliased attributes seems likely to be a Sphinx bug that we should report upstream, e.g., to [sphinx-dev](http://groups.google.com/group/sphinx-dev).
> 
> Is there a minimal example we can submit that reproduces the problem?

I've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed.


---

Comment by hivert created at 2010-02-17 20:32:46

Patch to experiment the interaction Sphinx/NestedMetaclass


---

Attachment

> I've made some experiments. Actually it seems that the problem is a bad interaction between sphinx and the particular metaclass `NestedMetaclass` we have to use to work around the nested class pickling bug of python. If you apply the attached patch, you'll see that `TestParent1` is correctly rendered whereas the other parent are not. I think this is a lead which should be followed. 

More info on this: to workaround python's nested class pickle bug we put any class which contain a nested class into `NestedMetaclass`. The main purpose of this metaclass is to change the class `__name__` with the help of the function
`modify_for_nested_pickle`. As a result sphinx has the impression that the class is an alias. Demonstration: if I comment line 112 of nested_class.py

```
diff --git a/sage/misc/nested_class.py b/sage/misc/nested_class.py
--- a/sage/misc/nested_class.py
+++ b/sage/misc/nested_class.py
@@ -108,7 +108,7 @@ def modify_for_nested_pickle(cls, name_p
             if v.__name__ == name and v.__module__ == module.__name__ and getattr(module, name, None) is not v:
                 # OK, probably this is a nested class.
                 dotted_name = name_prefix + '.' + name
-                v.__name__ = dotted_name
+                # v.__name__ = dotted_name
                 setattr(module, dotted_name, v)
                 modify_for_nested_pickle(v, dotted_name, module)
```

Then everything works fine. Any idea to solve this ?


---

Comment by hivert created at 2010-02-17 22:36:06

Things are progressing with the help of Mike Hansen on irc: The submitted patch to autodoc.py partially solve the problem. Now each nested class is documented twice ! I'm trying to remove one.


---

Comment by hivert created at 2010-02-17 22:36:06

Changing status from needs_info to needs_work.


---

Comment by hivert created at 2010-02-17 23:49:02

This should solve the problem:
Applying

```
autodoc.py.patch
}}} 
to
{{{
Sphinx-0.6.3-py2.6.egg/sphinx/ext/autodoc.py
}}}
and `trac_7448-nested_class_sphinx-fh.patch`
should solve the problem.


---

Comment by hivert created at 2010-02-17 23:54:18

Changing component from categories to documentation.


---

Comment by hivert created at 2010-02-17 23:54:18

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-02-18 00:24:06

Two remarks:

 - Thanks to Mike Hansen for its help on IRC.
 - Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! 

Florent, off to bed :-)


---

Comment by jhpalmieri created at 2010-02-18 04:35:41

Replying to [comment:9 hivert]:
> Since I'm patching the sources of sphinx, I probably need something like rebuilding sphinx spkg. Unfortunately, I don't know how to do this. Help welcome ! 

Here's a new spkg:

 - [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p5.spkg)

(I haven't tested the patch here, just implemented it and built the spkg.  Please check the file autodoc.py to make sure I patched it right.)


---

Comment by jhpalmieri created at 2010-02-18 04:52:41

To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?


---

Comment by hivert created at 2010-02-18 07:41:46

Hi John,

Replying to [comment:12 jhpalmieri]:
> (I haven't tested the patch here, just implemented it and built the spkg. Please check the file autodoc.py to make sure I patched it right.)  

Thank for this. Is this normal that the file

```
./patches/autodoc.py
```

contains the modifications, whereas

```
./src/sphinx/ext/autodoc.py
```

doesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. 

> To test this, do we need to add sage.misc.nested_class and/or sage.misc.nested_class_test to the reference manual?

No you don't ! Moreover, sage.misc.nested_class has already been added since #8250 merged in sage-4.3.3.alpha1. If you want to see the result pick a random file with nested class. They are plenty of them in categories, see eg

```
sage/categories/semigroups.py
```

which has many thing implemented in nested classes. 

Note that now that we do see nested classes, we find out that they are plenty of room for improvement in those docs. It will be the purpose of an (or more probably several) other ticket.


---

Comment by nthiery created at 2010-02-18 10:55:25

Summary of discussion with Florent over the phone:
 - the patch to autodoc could be made more robust and include an analysis of the problem
 - we have an example where Sphinx screws up, with plain Python nested classes (without NestedClassMetaclass), and has no chance to do any better without fixing nested class names as does NestedClassMetaclass.

Florent will post an improved patch, but not right away. So if there is an emergency to get this into 4.4, I give a positive review on that particular patch to get in as is.


---

Comment by jhpalmieri created at 2010-02-18 16:03:19

Replying to [comment:13 hivert]:
> Thank for this. Is this normal that the file ./patches/autodoc.py
> contains the modifications, whereas
> ./src/sphinx/ext/autodoc.py
> doesn't ? It seems that the answer is yes and that the former replace the later during build. Everthing seems to be ok. 

Yes, it's normal: in a typical spkg, the "src" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  

I noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.


---

Comment by hivert created at 2010-02-18 16:35:34

> Yes, it's normal: in a typical spkg, the "src" directory is supposed to contain the original unmodified source, and then it gets patched by running spkg-install.  

So that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? 
 
> I noticed that the nested classes in categories/coxeter_groups seem to be rendered correctly, so I guess that's good evidence that it's working.

Cool !


---

Comment by jhpalmieri created at 2010-02-18 17:13:22

Replying to [comment:16 hivert]:
> So that if I want to update the spkg, I only need to update the file in `patch/autodoc.py` file, commit it with hg and tar the whole thing, am I right ? 

You should update `patches/autodoc.py` and also `patches/autodoc.patch`: this one never gets used, but it's helpful to see how autodoc.py was actually changed.  While in the patches directory, I just do something like `diff -u ../src/sphinx/ext/autodoc.py autodoc.py > autodoc.patch`.

You might also update SPKG.txt, which includes the change log.  I put your name down for the new patch to autodoc.py, for example.  You also need to decide if you need to bump the patch level up: just keep the directory as it is, sphinx-0.6.3.p5, or rename it to sphinx-0.6.3.p6.  I think if you're just tinkering with this patch, keep it as "p5".

Finally, going to the directory containing sphinx-0.6.3.p5, you run "sage -pkg sphinx-0.6.3.p5" to create the spkg file.


---

Attachment


---

Comment by hivert created at 2010-02-20 00:06:03

patch to sphinx autodoc.py


---

Attachment

I should have reached a final state for this ticket. I've added a lot of comment explaining what's happening. Please review.

I uploaded a new patch for sphinx and for autodoc.py. Do *not* apply `trac_7448-nested_class_sphinx_exper-fh.patch` which was used for experiments. 

mpatel told on #8258 he will take care or building the spkg. Many thanks to him.


---

Comment by mpatel created at 2010-02-20 21:04:16

Combined patch rebased vs. #8244.  Apply _only_ this patch.  sage repo.


---

Attachment

I've attached a combined patch that's rebased against #8244.  That ticket adds a custom `sage_autodoc` extension to the sage repository.  We don't need to update the Sphinx spkg here.

Please check that I did this correctly.  Thanks!


---

Comment by mpatel created at 2010-02-20 21:12:50

After this ticket is reviewed, I'll rebase #7549.


---

Comment by mpatel created at 2010-02-21 00:19:42

An off-topic note about


```
combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object
combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object
```

I think we can suppress these by using `import random` and calling `random.random()`.


---

Comment by mpatel created at 2010-02-22 06:08:35

Replying to [comment:21 mpatel]:
> I think we can suppress these by using `import random` and calling `random.random()`.
See #8326.


---

Comment by hivert created at 2010-02-23 00:02:41

After some discussion I've found a better logic for raising warning. I'm working again on it.


---

Comment by hivert created at 2010-02-23 00:02:41

Changing status from needs_review to needs_work.


---

Attachment


---

Attachment

Hi there ! I just uploaded what should be the final version of this patch:
`autodoc.py` and `autodoc.py.2.patch` and ` trac_7448-nested_class_sphinx-fh.3.patch`. If you wan't to test the rendering you can comment

```
__all__ = [] # Don't document any parents
}}} 
at the beginning of `nested_class_test.py`.


---

Comment by hivert created at 2010-02-23 20:20:28

Changing keywords from "Sphinx categories." to "Sphinx, nested classes".


---

Comment by hivert created at 2010-02-23 20:21:15

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-24 04:00:41

Rebased for queue in comment.  Apply only this patch.


---

Attachment

V4 is rebased for the following queue:

```
trac_8244-slot_wrapper_argspec.patch
trac_8244-conf-autodoc.2.patch
trac_8244-sagedoc.patch
trac_7448-nested_class_sphinx-fh.4.patch
```

With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].

Questions:

 * Are there objections to making the unpicklable class check optional?  We could add a command-line option. 
 * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:

```diff
diff --git a/doc/common/sage_autodoc.py b/doc/common/sage_autodoc.py
--- a/doc/common/sage_autodoc.py
+++ b/doc/common/sage_autodoc.py
@@ -848,7 +848,9 @@ class ClassDocumenter(ModuleLevelDocumen
         # as data/attribute
         if ret:
             if hasattr(self.object, '__name__'):
-                self.doc_as_attr = (self.objpath[-1] != self.object.__name__)
+                name = self.object.__name__
+                self.doc_as_attr = (self.objpath != name.split('.') and 
+                                    self.check_module())
             else:
                 self.doc_as_attr = True
         return ret
```

  and make it easier to upgrade to newer Sphinx versions.

Note: We have made changes to `environment.py` and `highlighting.py` and other changes to `autodoc.py`.  But Georg Brandl has recently committed a [change](http://bitbucket.org/birkenfeld/sphinx/changeset/ee86e8563c6f/) --- requested by Mike Hansen? --- that should allow us to revert to the upstream `enviroment.py` and `autodoc.py`, modulo this ticket.  Actually, I think we can avoid patching `highlighting.py`, too, if we [subclass Pygments' Python lexer](http://pygments.org/docs/lexerdevelopment/).


---

Comment by hivert created at 2010-02-28 08:55:53

Replying to [comment:26 mpatel]:
> V4 is rebased for the following queue:

```
trac_8244-slot_wrapper_argspec.patch
trac_8244-conf-autodoc.2.patch
trac_8244-sagedoc.patch
trac_7448-nested_class_sphinx-fh.4.patch
```


Thanks for this !
> With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].

What do you mean by refresh here ? 

> Questions:
> 
>  * Are there objections to making the unpicklable class check optional?  We could add a command-line option.

No objection ! Actually I think this has nothing to do with sphinx and it should be tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  

>  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:
>   and make it easier to upgrade to newer Sphinx versions.

Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.


---

Comment by mpatel created at 2010-03-03 00:15:48

Replying to [comment:27 hivert]:
> > With #8244, we don't need to update the `sphinx-*.spkg`, so please refresh [attachment:trac_7448-nested_class_sphinx-fh.4.patch].
> What do you mean by refresh here ? 

Just that I suggest any further changes be updates to that patch, via `hg qrefresh`, if it's appropriate.

> >  * Are there objections to making the unpicklable class check optional?  We could add a command-line option.
> No objection ! Actually I think this has nothing to do with sphinx and it should be 
> tested during the import. I put it here because if a class is detected as unpicklable, there is a very good chance it ends up typeset incorrectly by sphinx.  

Since it doesn't seem to belong in the docbuild system, can we put this check elsewhere, e.g., in the unit/doc-testing system?  And restrict this ticket to nested class rendering?

> >  * Also, is it possible to move the check into a processing function in `conf.py`? Then we could minimize our changes to `autodoc`:
> >   and make it easier to upgrade to newer Sphinx versions.
> Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  

I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.

I may be overreacting.  Thoughts?


---

Comment by mpatel created at 2010-03-05 15:44:01

Only fix rendering of nested classes.


---

Attachment

Replying to [comment:28 mpatel]:
> > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  
> I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.

I've attached V5, which should "just" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.


---

Comment by hivert created at 2010-03-06 10:15:35

Replying to [comment:29 mpatel]:
> Replying to [comment:28 mpatel]:
> > > Sure ! Please do ! I won't have much time working on this so I'll appreciate someone take over those if the architecture is changed.  
> > I tried doing this and didn't have instant success.  But as you suggest, it might be better to do this elsewhere.
> 
> I've attached V5, which should "just" fix Sphinx's rendering of nested classes.  To the extent it counts, my review is positive.  Could someone please review V5 for this ticket?  I've opened #8452 for the nested class pickling check and will make a patch for that.

Hi Mitesh,

Thanks for taking care of this ! I'm Ok with the change you made to my patches so that I suppose I'm allowed to put a positive review on this ticket.


---

Comment by hivert created at 2010-03-06 10:15:35

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 23:55:49

Merged just trac_7448-nested_class_sphinx-fh.5.patch


---

Comment by mhansen created at 2010-03-06 23:55:49

Resolution: fixed
