# Issue 9016: make morphisms hashable

Issue created by migration from https://trac.sagemath.org/ticket/9016

Original creator: burcin

Original creation time: 2010-05-22 15:36:30

Assignee: AlexGhitza

CC:  robertwb

Attached patch makes morphisms hashable in a reasonably fast way by defining the following:


```
    def __hash__(self):
        return hash((self._domain, self._codomain))
```


It also defines specialized methods for `sage.rings.morphism.RingHomomorphism_im_gens` and `sage.rings.morphism.RingHomomorphism_from_quotient`.

While testing the code for `im_gens`, I fixed a confusing error message in `sage.structure.sequence.Sequence.__hash__()` as well.


---

Attachment


---

Comment by burcin created at 2010-05-22 15:43:23

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-22 15:43:23

There seems to be a problem with inheriting `__hash__()` methods. The class `sage.categories.morphism.SetMorphism` derives from `sage.categories.morphism.Morphism` which in turn derives from `sage.categories.map.Map`.

Even after adding a `__hash__()` method to `sage.categories.map.Map`, instances of `SetMorphism` are not hashable:


```
sage: from sage.categories.morphism import SetMorphism
sage: X.<x> = ZZ[]
sage: Y = ZZ
sage: phi = SetMorphism(Hom(X, Y, Rings()), lambda p: p[0])
sage: hash(phi)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/burcin/sage/sage-4.4.1.alpha2-patched/<ipython console> in <module>()

TypeError: unhashable type: 'sage.categories.morphism.SetMorphism'
```


Note also that `sage.categories.map.Map` derives from `sage.structure.element.Element` which also has a `__hash__()` method.

Any hints?


---

Comment by robertwb created at 2010-05-22 15:51:48

`__hash__` must be redefined if `__cmp__` or `__richcmp__` is, as it is an all or none thing with their inheritance. Not my design decision, but that's the way it is. 

See http://docs.python.org/c-api/typeobj.html


---

Comment by robertwb created at 2010-06-05 09:16:25

Changing type from defect to enhancement.


---

Comment by robertwb created at 2010-06-22 20:49:12

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-01 08:12:21

This patch causes a doctest failure on vanilla Sage 4.5.alpha1: 

```
sage -t  "devel/sage-reviewing/sage/modules/fg_pid/fgp_module.py"
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/modules/fg_pid/fgp_module.py", line 383:
    sage: Q._coerce_map_from_(V.scale(2))
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[11]>", line 1, in <module>
        Q._coerce_map_from_(V.scale(Integer(2)))###line 383:
    sage: Q._coerce_map_from_(V.scale(2))
      File "/storage/masiao/sage-4.5.alpha1/local/lib/python/site-packages/sage/modules/fg_pid/fgp_module.py", line 388, in _coerce_map_from_
        return bool(self._V._coerce_map_from_(S))
      File "element.pyx", line 741, in sage.structure.element.Element.__nonzero__ (sage/structure/element.c:5731)
      File "element.pyx", line 863, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7107)
      File "element.pyx", line 835, in sage.structure.element.Element._richcmp (sage/structure/element.c:6989)
      File "/storage/masiao/sage-4.5.alpha1/local/lib/python/site-packages/sage/modules/matrix_morphism.py", line 111, in __cmp__
        return cmp(self.matrix(), other.matrix())
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)
      File "parent.pyx", line 268, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2602)
    AttributeError: 'sage.categories.morphism.CallMorphism' object has no attribute 'matrix'
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_7
***Test Failed*** 1 failures.
```



---

Comment by davidloeffler created at 2010-07-01 08:12:21

Changing status from positive_review to needs_work.


---

Comment by AlexGhitza created at 2010-09-02 10:58:30

Changing component from algebra to categories.


---

Comment by burcin created at 2010-09-13 10:18:18

apply only this patch


---

Attachment

Replying to [comment:5 davidloeffler]:
> This patch causes a doctest failure on vanilla Sage 4.5.alpha1: 

I uploaded a new patch which fixes this.

attachment:trac_9016-morphishm_hash.take2.patch also adds `__hash__()` methods to all the classes defined in `sage/{categories/map.pyx,rings/morphism.pyx}` which also define `__cmp__()` or `__richcmp__()` methods, in line with Robert's remarks in comment:2.

Robert, can you take a look at this again?


---

Comment by burcin created at 2010-09-13 10:22:41

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2011-03-22 19:37:13

rebased to 4.7.alpha1


---

Attachment

Apparently someone else fixed the problem in `sage/structure/sequence.py`. I rebased the patch to 4.7.alpha1.

Apply trac_9016-morphishm_hash.take3.patch


---

Comment by robertwb created at 2011-05-12 19:17:22

I'm not so sure this is a good generic hash function--it means that all morphism has to the same thing.


---

Comment by burcin created at 2011-05-30 20:45:25

Replying to [comment:9 robertwb]:
> I'm not so sure this is a good generic hash function--it means that all morphism has to the same thing. 

I looked over the patch once more. The hash functions defined here use all the information I see in the class. Do you have any specific suggestions for improvement?


---

Comment by robertwb created at 2011-05-31 04:00:53

Hashing the string representation is preferable, or the image of the generators of the codomain (caching the result if the performance isn't sufficient). Either that or raising an error and requiring all specific subclasses (that have the information to distinguish between distinct elements) implement this.


---

Comment by robertwb created at 2011-05-31 04:00:53

Changing status from needs_review to needs_info.


---

Comment by burcin created at 2011-05-31 09:03:54

I don't see how the string representation could provide more information than the data stored in the class. I would be happy to add such data to the tuple that is hashed if you point it out.

The current patch uses the hash of the images of the generators when the morphism class contains this information. See line 1103 of `sage/rings/morphism.pyx` for example. In order to implement your suggestion we would also have to change the comparison functions, which compare the same data this patch hashes.

<rant>
Robert, even though you chose to mark this as an enhancement in comment:3, it is actually a bug that effects my work. The category framework relies heavily on cached functions, which in turn need the arguments of these to be hashable. For example, I need unique parents that also depend on a morphism/map (difference/differential rings). I opened this ticket when I ran into this problem a year ago. I know I haven't really pushed it through, but it still is a shame that it takes so long for such a small change to get into a release.
</rant>


---

Comment by robertwb created at 2011-05-31 16:33:41

Replying to [comment:12 burcin]:
> I don't see how the string representation could provide more information than the data stored in the class. I would be happy to add such data to the tuple that is hashed if you point it out.

The string representation is more often overridden to be distinct for distinct morphisms 

> The current patch uses the hash of the images of the generators when the morphism class contains this information. See line 1103 of `sage/rings/morphism.pyx` for example. In order to implement your suggestion we would also have to change the comparison functions, which compare the same data this patch hashes.

Are you saying that any two morphisms in the same homset compare equal? That is a bug for sure. I'd rather not be able to compare such morphisms. 

> <rant>
> Robert, even though you chose to mark this as an enhancement in comment:3, it is actually a bug that effects my work. The category framework relies heavily on cached functions, which in turn need the arguments of these to be hashable. For example, I need unique parents that also depend on a morphism/map (difference/differential rings). I opened this ticket when I ran into this problem a year ago. 

Happy to change it back given the context. 

> I know I haven't really pushed it through, but it still is a shame that it takes so long for such a small change to get into a release.
> </rant>

I know this all to well--too much bureaucracy and churn in the code among other things. That was one of my primary motivations for the patchbot, so hopefully simple changes could get approved quickly.


---

Comment by robertwb created at 2011-05-31 16:33:41

Changing type from enhancement to defect.


---

Comment by tscrim created at 2012-11-18 08:20:00

This looks good for the most part. I think Robert was thinking the `hash((domain, codomaim))` was the hash for the individual morphism, as opposed to that being the hash for the homset (as it currently is). The morphism's hash is from the image of the generators which I believe is sufficient. (This breaks down if you look at a large amount of maps from different domains to the same image in the same codomain and same number of generators, but this seems like something extremely unlikely to occur in practice. We could also hash in the parent to take care of this...)

However this does not pass the doctests on my (virtual) machine which runs with 32-bit instead of 64-bit (which the patchbot runs on). Here are my hash values:

```
rings/morphism.pyx
 line 542: 1975065480
 line 959: 467020541
 line 1147: -664373037
 line 1554: -644670332
 line 1699: 1917770400

categories/map.pyx
 line 1047: 433071207
 line 1290: -1460497211
```

Also, I don't believe you need `# indirect doctest` for the `hash()`, but this isn't that important.


---

Attachment


---

Comment by burcin created at 2012-11-19 03:39:57

Thanks for reviewing this ticket!

New patch up at [attachment:trac_9016-morphishm_hash.take4.patch] with 32-bit hash values. I removed the `# indirect doctest` messages as well. Perhaps the coverage script improved in the mean time to avoid complaints about not using the name of the function in the tests.


---

Comment by burcin created at 2012-11-19 03:39:57

Changing status from needs_info to needs_review.


---

Comment by tscrim created at 2012-11-19 04:29:30

Looks much better now. Two more minor things (sorry for not noticing this earlier):

- Move the `from copy import copy` from the header of `morphism.pyx` to
  {{{
  if not im_gens.is_immutable(): 
      from copy import copy
      im_gens = copy(im_gens)
      im_gens.set_immutable() 
  }}}
  (or perhaps a `lazy_import`)
  This should make the startup plugin happy.

- Could you add a (short) description such as `Return the hash of ``self``` to each `__hash__()` function.

After this, that should be it. Thank you.


---

Attachment

apply only this patch


---

Comment by burcin created at 2012-11-19 11:21:07

Replying to [comment:16 tscrim]:
> Looks much better now. Two more minor things (sorry for not noticing this earlier):

Thanks for the quick feedback. I attached [attachment:trac_9016-morphishm_hash.take5.patch a new patch] fixing the two issues mentioned above.

Patchbot, apply trac_9016-morphishm_hash.take5.patch

I guess it's too late to fix the horrific typo in the file name. :)


---

Comment by tscrim created at 2012-11-19 16:09:16

No, its not too late to change the name. However there is a change since the last patch in one of the hash values (line 1050 in `categories/map.pyx`) and it's different than what the patchbot returns (I can't reproduce it since I'm using a 32-bit system). Is that the hash value that you get?


---

Comment by burcin created at 2012-11-19 19:02:01

apply only this patch


---

Attachment

I had some other patches applied. One of them might have changed the hash value. Corrected patch attached. Just to make sure there is no random error, I ran the tests in these two files 100 times. :)

Apply trac_9016-morphism_hash.patch


---

Comment by robertwb created at 2012-11-19 19:40:31

I would argue that in general it's better to avoid having these arbitrary values for hash tested exactly at all (unless they're meaningful, like hash(ZZ(2)) == 2), especially when they vary for 64 and 32-bit values.  Better to test it functionally, like


```
sage: { phi: 'yes' }[phi]
'yes'
```


or even


```
hash(phi) == hash(phi)
True
hash(phi) == hash(rho)
False
```



---

Comment by tscrim created at 2012-11-20 03:32:17

For the most part, I would almost argue against doing that, in particular, it does not make sure that hash values do not change in different sage sessions and machines (since the tests are run multiple times generally). For example, say we create an object `O` and use it as a key it in a dictionary `D` (e.g. `D[O] = 5`) and then pickle `D`. Then on another session/machine (with the same bit architecture) we unpickle `D` and to do `D[O]` safely; we want to make sure via doctests that the hashes match.

Actually on that note, I wonder if we need to (much less how) send a warning to the users when hash values change from one version to another. In that context, I would argue that these tests are how we should do everything and never update a hash value unless the structure of a class changes. Granted, I am making an assumption about python pickles dictionaries: that python does not recreate the object then reinsert it into the hash table but instead creates the object in the desired location. I have a test in mind that I will run tonight. I hope all of the above makes sense.

However I do see your point since the underlying hash values can change and makes the doctests of certain classes harder to maintain. Also I do somewhat like the `hash(phi) == hash(phi)` test since the hash is run multiple times and it checks to make sure the object is hashable.


---

Comment by robertwb created at 2012-11-20 04:35:55

This is getting a bit off topic, but if you have pickling that depends on hash values then it's already broken (e.g. 32-bit vs 64-bit). And, no, hashes do not need to be consistent to pickle dictionaries. All that we need is that hashes are consistent within a given Python session. (On that note, the fix of http://bugs.python.org/issue13703 is to make hashes completely unpredictable between sessions, which will break any hard-coded hash we have that (transitively) depends on something that hashes a string.)

<rant>
Aside from this, I've also been bitten several times from changing a hash (to making it faster, e.g. not simply doing `hash(str(self))`) hand having to change random values all over the library, as well as the nuisance of having to find a 32-bit computer to test on to get the new 32-bit value (because the tests pass just fine for me), both of which provide near zero actual value. 
</rant>


---

Comment by tscrim created at 2012-11-20 16:13:56

Hmm..interesting. Also good to know about the dictionary pickling. I cannot disagree at all with your rant; I use the patchbot to get my 64-bit hash values >_<. So would you agree to hash tests of the form:

```
sage: hash(phi) == hash(phi)
True
```

?

Thanks,

Travis


---

Attachment

apply only this patch


---

Comment by burcin created at 2012-11-20 16:39:36

I attached a new patch replacing the doctests with `hash(f) == hash(f)` and `{f: 1}[f]` as Robert suggests.

Apply [attachment:trac_9016-morphism_hash.take7.patch].


---

Comment by tscrim created at 2012-11-20 20:04:02

Looks good to me. Robert?


---

Comment by robertwb created at 2012-11-21 05:07:43

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2012-11-21 05:07:43

Looks good to me too. My only comment would be that perhaps `hash((self._domain, self._codomain))` could be pulled to a higher superclass, but I've got no problems with the way it is now.


---

Comment by jdemeyer created at 2012-12-21 09:32:03

Resolution: fixed
