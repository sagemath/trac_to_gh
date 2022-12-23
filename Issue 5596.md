# Issue 5596: [with patch, needs review] refactor coercion to catch fewer exceptions

Issue created by migration from https://trac.sagemath.org/ticket/5596

Original creator: robertwb

Original creation time: 2009-03-24 05:06:32

Assignee: robertwb

CC:  nthiery georgsweber

See discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/d2145cd313f92bb8/c3049a540f91bab3?hl=en&lnk=gst&q=coercion#c3049a540f91bab3


---

Comment by mvngu created at 2009-03-27 06:25:49

Nope, for me the patch failed to apply against Sage 3.4:

```
sage: hg_sage.apply("/home/mvngu/patch/5596/5596-coerce-exceptions.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5596/5596-coerce-exceptions.patch"
applying /home/mvngu/patch/5596/5596-coerce-exceptions.patch
abort: malformed patch a/sage/structure/parent_old.pyx @@ -602,39 +496,4 @@
```



---

Comment by GeorgSWeber created at 2009-03-30 20:43:32

Against 3.4.1.alpha0, the situation gets even worse:

```
applying ../../../patches/5596-coerce-exceptions.patch
patching file sage/rings/infinity.py
Hunk #1 FAILED at 87
Hunk #2 FAILED at 100
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/infinity.py.rej
abort: malformed patch a/sage/structure/parent_old.pyx @@ -602,39 +496,4 @@

```

The content of infinity.py.rej is essentially that now there are "ValueErrors" instead of "TypeErrors" to be exchanged.

I don't know where the "malformed-ness" already noticed by Minh comes from, but it hits me also from the command line (using the hg from Sage-3.4.1.alpha0).


---

Comment by robertwb created at 2009-04-25 07:49:33

OK, I'll try and rebase these for 3.4.2


---

Attachment

Rebased against 4.1.1


---

Comment by robertwb created at 2009-09-24 04:26:24

OK, I finally got around to rebasing this. Don't know what the "malformed-ness" was either, but it's gone.


---

Comment by nthiery created at 2009-09-24 09:48:53

Thanks for working on this. This will be a big step forward in debuggability or coercion problems!
In particular, reducing the amount of poking around "let's try if this method does not break horribly on this element" is
definitely going in the right direction. 

I just went through the patch, and each change sounds sensible. I haven't checked that they are 100% correct, by lack of expertise.
In particular, I haven't checked line by line the big chunks of diffs corresponding to indentation changes (inclusion in a try).

Overall, +1 for setting positive review, but I would prefer if some expert could double check.

I am now on my way to run the tests, and see how this patch interact with the category patches.


One comment:

In Sage-Combinat, we often have operations which are partially defined, and return None when they are not. How does this fit with the
change in the specifications of _mul_ and friends, suggesting to return None rather than raising NotImplemented?

Should "Returning None indicates that this action is not implemented" be replaced by something like:

"Returning None indicates that this action is not defined, or not implemented here, for the given elements"?

Alternatively, I could possibly suggest to instead check that self._lmul (say) is
not the default "NotImplemented" implementation of Element, before actually calling it. I guess I am trying to have an analogue of
the abstract_method idiom for cpdef methods. Would it be possible to attach some sort of "abstract method" flag to a cpdef method,
that we could test without actually having to execute the method?

But I don't mind if this waits for a later patch.


---

Comment by GeorgSWeber created at 2009-09-24 22:36:24

Sorry, but

> Overall, +1 for setting positive review, but I would prefer if some expert could double check.

although it is always a good thing to have "some expert" double checking a patch.
But who else, but you two, could you think of for reviewing this specific patch?

If you could point out to me certain "suspicious" lines, I would be happy to look at these, and listen to your explanations, and learn something from it, but I fear that's all I can do. There are damn few experts around for programming "code doing coercions" ...

Cheers,
Georg


---

Comment by robertwb created at 2009-09-24 23:15:04

Replying to [comment:6 nthiery]:

> I just went through the patch, and each change sounds sensible. I haven't checked that they are 100% correct, by lack of expertise.
> In particular, I haven't checked line by line the big chunks of diffs corresponding to indentation changes (inclusion in a try).
> 
> Overall, +1 for setting positive review, but I would prefer if some expert could double check.

I'll second Georg's comments, you are as much of an "expert" in this area as nearly anyone else (except maybe me, but I can't review it myself...). 

> I am now on my way to run the tests, and see how this patch interact with the category patches.

I saw some tests failing--looks like easy fixes, I'll try and post a patch later tonight. 

> One comment:
> 
> In Sage-Combinat, we often have operations which are partially defined, and return None when they are not. How does this fit with the
> change in the specifications of _mul_ and friends, suggesting to return None rather than raising NotImplemented?
> 
> Should "Returning None indicates that this action is not implemented" be replaced by something like:
> 
> "Returning None indicates that this action is not defined, or not implemented here, for the given elements"?

I'll change that to say "not implemented here."

> Alternatively, I could possibly suggest to instead check that self._lmul (say) is
> not the default "NotImplemented" implementation of Element, before actually calling it. I guess I am trying to have an analogue of
> the abstract_method idiom for cpdef methods. Would it be possible to attach some sort of "abstract method" flag to a cpdef method,
> that we could test without actually having to execute the method?

This can be done, kind of, if one knows the baseclass where the "abstract" method is implemented, though it's a bit hackish. I think you underestimate how fast calling a c(p)def method can be though. 

> But I don't mind if this waits for a later patch.

Yeah, that'd take some thinking, probably best put off 'till later.


---

Comment by robertwb created at 2009-09-25 08:32:02

OK, all doctests should pass now.


---

Comment by nthiery created at 2009-09-30 11:06:42

Replying to [comment:8 robertwb]:
> Replying to [comment:6 nthiery]:
> I'll second Georg's comments, you are as much of an "expert" in this area as nearly anyone else (except maybe me, but I can't review it myself...). 

Fair enough :-)

> > I am now on my way to run the tests, and see how this patch interact with the category patches.
> 
> I saw some tests failing--looks like easy fixes, I'll try and post a patch later tonight. 

Argl. I am always off by one version. I now have to compile a 4.1.2 alpha4

> > Alternatively, I could possibly suggest to instead check that self._lmul (say) is
> > not the default "NotImplemented" implementation of Element, before actually calling it. I guess I am trying to have an analogue of
> > the abstract_method idiom for cpdef methods. Would it be possible to attach some sort of "abstract method" flag to a cpdef method,
> > that we could test without actually having to execute the method?
> 
> This can be done, kind of, if one knows the baseclass where the "abstract" method is implemented, though it's a bit hackish. I think you underestimate how fast calling a c(p)def method can be though. 

Oh, thanks for pointing this.

No, I am not worried at all about speed, but about semantic and lazyness. Let's say we are investigating whether there is an action of A on B. That's (mostly) a mathematical question about the parents A and B. So it's preferable to "ask them", rather than poking around with some of their elements (which could have some special property). Part of it comes from experience with MuPAD telling that lot of trouble can be avoided if a parent does not construct any element unless asked for explicitly; in particular, lazyness helps handling cross-dependent parents. At the same time, a coercion lookup may involve many intermediate parents which will, or not, play a role in the end.

Now: what do I mean by "ask them". That can be using introspection, possibly on their element class. Preferably, it would be by having A and B (or some common boss) declare explicitly the action
to the coercion system. I actually have in my stack of todo's a preliminary implementation of this, as this is needed for symmetric functions and friends.

Hmm, that discussion is becoming long. We should move it to sage-devel.

> Yeah, that'd take some thinking, probably best put off 'till later. 

Ok. So I put a positive review, pending confirmation that all tests pass smoothly on 4.1.2 alpha4.
.


---

Comment by robertwb created at 2009-10-01 07:06:21

BTW, there is a `_get_action_` method on Parents themselves. And I *am* worried about speed, or at least the ability to be fast, as this stuff gets invoked for integer arithmetic, etc. :)


---

Comment by nthiery created at 2009-10-02 20:40:26

Replying to [comment:11 robertwb]:
> BTW, there is a `_get_action_` method on Parents themselves.

Yup.

> And I *am* worried about speed, or at least the ability to be fast, as this stuff gets invoked for integer arithmetic, etc. :)

Sure:-)

 I should have said that my comment about speed was under the assumption that the coercion lookup was cached.


---

Comment by mhansen created at 2009-10-15 07:48:07

I get the following failures against 4.1.2:


```
sage -t  "devel/sage-main/sage/modules/fg_pid/fgp_module.py"
**********************************************************************
File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/devel/sage-main/sage/modules/fg_pid/fgp_module.py", line 1280:
    sage: A._hom_from_smith(Sequence([B.0]), B)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_33[7]>", line 1, in <module>
        A._hom_from_smith(Sequence([B.gen(0)]), B)###line 1280:
    sage: A._hom_from_smith(Sequence([B.0]), B)
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1416)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/modules/fg_pid/fgp_morphism.py", line 131, in _repr_
        list(self.im_gens()))
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/modules/fg_pid/fgp_morphism.py", line 149, in im_gens
        self.__im_gens = tuple([self(x) for x in self.domain().gens()])
      File "<doctest __main__.example_32[2]>", line 3, in gens
    NameError: global name 'tuple' is not defined
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_33
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mhansen/.sage//tmp/.doctest_fgp_module.py
         [7.6 s]
exit code: 1024


sage -t -long "devel/sage-main/sage/calculus/wester.py"     
**********************************************************************
File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/devel/sage-main/sage/calculus/wester.py", line 122:
    sage: bool(f == g)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[36]>", line 1, in <module>
        bool(f == g)###line 122:
    sage: bool(f == g)
      File "expression.pyx", line 1340, in sage.symbolic.expression.Expression.__nonzero__ (sage/symbolic/expression.cpp:7786)
      File "expression.pyx", line 1483, in sage.symbolic.expression.Expression.test_relation (sage/symbolic/expression.cpp:9153)
      File "expression.pyx", line 2807, in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:13840)
      File "element.pyx", line 1177, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:9945)
      File "coerce.pyx", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6096)
      File "coerce.pyx", line 1160, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10589)
      File "coerce.pyx", line 1283, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:11682)
      File "parent.pyx", line 1203, in sage.structure.parent.Parent.get_action (sage/structure/parent.c:10828)
      File "parent_old.pyx", line 478, in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:5974)
      File "parent_old.pyx", line 198, in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2757)
      File "parent_old.pyx", line 210, in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3068)
      File "parent_old.pyx", line 214, in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:3118)
      File "parent.pyx", line 1306, in sage.structure.parent.Parent.discover_action (sage/structure/parent.c:12094)
      File "coerce_actions.pyx", line 92, in sage.structure.coerce_actions.ModuleAction.__init__ (sage/structure/coerce_actions.c:3415)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/categories/pushout.py", line 692, in pushout
        return all(Z)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/categories/pushout.py", line 64, in __call__
        R = c(R)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/categories/pushout.py", line 406, in __call__
        return R.completion(self.p, self.prec, self.extras)
      File "/scratch/mhansen/release/4.2/alpha0/sage-4.2.alpha0/local/lib/python/site-packages/sage/rings/number_field/number_field.py", line 1074, in completion
        return QQ.completion(p, prec, extras).algebraic_closure()
      File "ring.pyx", line 1752, in sage.rings.ring.Field.algebraic_closure (sage/rings/ring.c:9235)
    NotImplementedError: Algebraic closures of general fields not implemented.
**********************************************************************
1 items had failures:
   1 of 194 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mhansen/.sage//tmp/.doctest_wester.py
         [5.3 s]
exit code: 1024
```



---

Comment by mhansen created at 2009-10-15 07:48:07

Changing status from positive_review to needs_work.


---

Comment by robertwb created at 2009-10-15 07:50:08


```
global name 'tuple' is not defined
```


Huh? 

I'll take a look when I upgrade.


---

Comment by mhansen created at 2009-10-16 09:45:45

Yeah, it's very weird.


---

Comment by robertwb created at 2009-10-19 21:37:27

The NotImplementedError is an easy fix. I'll look at the other one later today, hopefully to get this into 4.2.


---

Comment by robertwb created at 2009-10-20 05:26:50

apply on top of previous


---

Attachment

OK, this was one of those weird bugs that was only reproducible in doctests, and an all around pain to track down. Apparently the coercion changes caused some parents to not get garbage collected as eagerly, which exposed a bug when fgp modules are cached and reused. I am still unsure what exactly the bug is (I have a hunch it has to do with parents that are defined in doctests getting reused in other doctests after their environment has been recycled or something) but I have disabled caching for now to get it to work. 

I refreshed the exposure-fixes patch, should work fine now.


---

Comment by robertwb created at 2009-10-20 05:31:11

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mhansen created at 2009-10-21 05:22:11

I added a small patch which just reworked the doctest since the action of the symmetric group on polynomials from the right already exists.

Other than that, everything looks good to me.


---

Comment by mhansen created at 2009-10-21 05:22:11

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-21 05:22:32

Resolution: fixed
