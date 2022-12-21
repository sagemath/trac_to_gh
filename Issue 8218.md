# Issue 8218: Finite Field move

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2010-02-09 03:39:15

Assignee: AlexGhitza

CC:  robertwb

Keywords: finite fields

Moves all of the finite field files, the integer_mod files and the base classes from sage.rings.ring and sage.structure.element into their own folder in sage.rings.  In preparation for more work on finite fields.


---

Attachment

Just moves the files


---

Comment by roed created at 2010-02-09 04:16:01

Changing assignee from AlexGhitza to roed.


---

Comment by roed created at 2010-02-09 04:16:01

The files that are moved into sage.rings.finite_rings are:


```
integer_mod.pyx -> finite_rings/integer_mod.pyx
integer_mod.pxd -> finite_rings/integer_mod.pxd
integer_mod_ring.py -> finite_rings/integer_mod_ring.py
finite_field.py -> finite_rings/constructor.py
finite_field_prime_modn.py -> finite_rings/finite_field_prime_modn.py
finite_field_element.py -> finite_rings/element_ext_pari.py
finite_field_ext_pari.py -> finite_rings/finite_field_ext_pari.py
finite_field_givaro.pyx -> finite_rings/element_givaro.pyx
finite_field_givaro.pxd -> finite_rings/element_givaro.pxd
finite_field_ntl_gf2e.pyx -> finite_rings/finite_field_ntl_gf2e.pyx
finite_field_ntl_gf2e.pxd -> finite_rings/finite_field_ntl_gf2e.pxd
finite_field_morphism.py -> finite_rings/homset.py
part of ring.pyx -> finite_rings/finite_field_base.pyx
part of ring.pxd -> finite_rings/finite_field_base.pxd
part of sage/structure/element.pyx -> sage/rings/finite_rings/element_base.pyx
part of sage/structure/element.pxd -> sage/rings/finite_rings/element_base.pxd
```



---

Comment by robertwb created at 2010-02-09 18:37:46

It would be good to do this as a mercurial bundle, so that the history and other merges will follow correctly.


---

Comment by roed created at 2010-02-09 20:07:11

Bundle replacing trac_8218_move.patch.  This should allow us to keep the repository information.


---

Comment by roed created at 2010-02-09 20:09:08

Changing status from new to needs_review.


---

Attachment

I created the bundle with 

```
sage -hg bundle -r 13801 --base 13800 ~/patches-out/trac_8218_move.bundle
```

I believe this is right, but it's been a while since I used bundles.


---

Comment by roed created at 2010-02-09 20:15:00

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-02-09 20:15:00

Oops.  Forgot to fix pickles.  Doing so now...


---

Attachment

Fixes the imports.


---

Comment by roed created at 2010-02-09 21:38:13

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-02-09 21:38:13

Pickling should work now.


---

Comment by drkirkby created at 2010-02-22 00:45:12

Has this been checked on Solaris? The patches are huge, so there is a good chance this will break on one platform or another. 

There's general information about building on Solaris at

http://wiki.sagemath.org/solaris

Information specifically for 't2' at

http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

Both the source (4.3.0.1 is the latest to build on Solaris) and a binary
which will run on any SPARC can be found at http://www.sagemath.org/download-source.html

Dave


---

Comment by drkirkby created at 2010-02-22 00:45:12

Remove assignee roed.


---

Comment by drkirkby created at 2010-02-22 00:45:22

Changing status from needs_review to needs_info.


---

Comment by robertwb created at 2010-02-22 19:30:14

Changing status from needs_info to needs_review.


---

Comment by robertwb created at 2010-02-22 19:30:14

The content, not the size, of the patches would determine whether there's any platform-dependent code here, and I highly doubt there is. 

What I've looked at so far looks good (I started to do this myself once, but unfortunately there was some hitch and by the time I got to it again rebasing was neigh impossible). I hope to be able to get a review on this soon (just a matter of finding time).


---

Comment by drkirkby created at 2010-02-22 19:46:24

I do realise it is the content, not the size, but small innocuous looking patches have screwed up the build either on not only Solaris, but also Linux and OS X too. 

It's difficult to me to see how we can know unless it is tested.


---

Comment by roed created at 2010-02-23 14:44:52

Rebased against 4.3.3: a bundle including all the moves; should be applied first


---

Attachment

How do I apply a bundle?  Can it be done in queues?


---

Comment by roed created at 2010-03-02 17:34:51

Within the deve/sage directory,

```
sage -hg unbundle trac_8218_move_433.bundle
```



---

Comment by roed created at 2010-03-02 17:50:33

Oh, and it can't be done in queues.  If you want to work with a patch, use `trac_8218_move.patch` instead.  I think that should apply; if not the only thing that patch or the bundle do is move a bunch of files (see a previous comment for the list).  If one of the hunks fails, just use `sage -hg rename`.


---

Comment by cremona created at 2010-03-02 20:02:42

Sorry, still failing.  After I unbundle the bundle I can neither run Sage nor rebuild it nor apply the "fix" patch, and have to delete the entire clone.  The "move" patch does not apply to 4.3.3.

If you could post the exact sequence of commands needs to go from a fresh 4.3.3, starting with (say) sage -clone 8218  and ending with sage -br (or similar), then I'll willingly test it.


---

Comment by roed created at 2010-03-05 20:35:02

Try the following (and let me know if it doesn't work):

```
cd $SAGE-ROOT
sage -clone 8218
cd devel/sage-8218/
sage -hg unbundle trac_8218_move.bundle
sage -hg merge
sage -hg commit -m "Merge"
sage -hg qinit
sage -hg qimport trac_8218_fixes_433.patch
sage -hg qpush
sage -br
```



---

Comment by cremona created at 2010-03-06 22:05:52

OK, I did that (except with the bundle trac_8218_move_433.bundle),  applying it all to 4.3.4.alpha0.  The merge is ok (one piece of fuzz).  The rebuild took a long time.  But sage -br ended up not running properly:

```
AttributeError                            Traceback (most recent call last)

/home/john/sage-current/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/home/john/sage-4.3.4.alpha0/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/home/john/sage-current/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/home/john/sage-current/local/lib/python2.6/site-packages/sage/all.py in <module>()
     70 get_sigs()
     71 
---> 72 from sage.rings.all      import *
     73 from sage.matrix.all     import *
     74 

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/all.py in <module>()
     88 
     89 # Algebraic numbers

---> 90 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     91                    AlgebraicReal, is_AlgebraicReal,
     92                    AlgebraicField, is_AlgebraicField, QQbar,

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/qqbar.py in <module>()
   1410 
   1411 # Cache some commonly-used polynomial rings

-> 1412 QQx = QQ['x']
   1413 QQx_x = QQx.gen()
   1414 QQy = QQ['y']

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2551)()

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):


/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    421 
    422         elif base_ring.is_field(proof = False):
--> 423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)
    424 
    425         elif base_ring.is_integral_domain(proof = False):

/home/john/sage-current/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, element_class, implementation)
   1194         if implementation is None: implementation="NTL"
   1195         if implementation == "NTL" and \
-> 1196                 sage.rings.finite_field.is_FiniteField(base_ring):
   1197             p=base_ring.characteristic()
   1198             from sage.libs.ntl.ntl_ZZ_pEContext import ntl_ZZ_pEContext

AttributeError: 'module' object has no attribute 'finite_field'
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```



---

Comment by cremona created at 2010-03-06 22:05:52

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-03-07 05:17:50

It looks like some additional patches got applied after what I based mine on...  Sorry about that.  I'll update the patch and post a new one soon.

This does illustrate why I'd like to get this reviewed.  :-)


---

Attachment

Rebased against 4.3.3: should be applied after the bundle.


---

Comment by roed created at 2010-03-12 01:03:47

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-03-12 01:03:47

You may need to clear out old files in the $SAGE_ROOT/devel/sage-8218/build directory.


---

Comment by cremona created at 2010-03-13 14:54:16

Sorry about this.  I made a new clone of 4.3.4.alpha1 and followed the instructions to the letter, but the final qpush gave this:

```
applying trac_8218_fixes_433.patch
patching file sage/crypto/util.py
Hunk #1 FAILED at 31
1 out of 1 hunks FAILED -- saving rejects to file sage/crypto/util.py.rej
patching file sage/homology/chain_complex.py
Hunk #1 succeeded at 382 with fuzz 1 (offset 3 lines).
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8218_fixes_433.patch
```


It might be better if someone who had any idea what they were doing took over this review -- I am clearly not competent!  For a start, if I depart in the slightest way from the list of commands then it does not work at all, but I don't understand why.

Meanwhile I'll keep this clone in case sending any of the files will help (but despite the message here, there is nothing left in the "working directory").


---

Comment by davidloeffler created at 2010-03-16 12:39:18

I managed to successfully build this under 4.3.4.alpha1. I had the same failure at the final qpush as John above, but I found the .rej file and merged it by hand. Build was fine, but time-consuming (why doesn't sage -b know about parallel processing?). I got just two doctest failures, one in /sage/crypto/public_key/blum_goldwasser.py and one in doc/en/reference/coercion.rst; both were trivial to fix. 

I will upload a new patch replacing trac_8218_fixes_433.patch, which fixes the merge fuzz problems and corrects the two doctests.


---

Comment by davidloeffler created at 2010-03-16 12:39:18

Set assignee to davidloeffler.


---

Attachment

apply after bundle (instead of trac_8218_fixes_433.patch)


---

Comment by davidloeffler created at 2010-03-16 13:45:38

As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)


---

Comment by davidloeffler created at 2010-03-16 13:45:38

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-16 15:58:45

Replying to [comment:20 davidloeffler]:
> As for drkirkby's comment above: naturally it doesn't have a chance of building on 4.3.0.1 on T2. (I checked, just to make sure). I don't think it's reasonable to expect new patches to apply identically on two increasingly different forks of the Sage code base. (Isn't this what Mercurial's branching and merging tools are supposed to be for?)

There are not two different forks of the code base.  There are no Mercurial branches. 

Be aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. 

Dave


---

Comment by davidloeffler created at 2010-03-16 16:46:09

Replying to [comment:21 drkirkby]:
> There are not two different forks of the code base.  There are no Mercurial branches. 
> 
> Be aware, given 4.3.4.alpha1 builds on Solaris, and passes all the doc tests, so I suspect if this breaks the build it will not be merged. 

Ah! That's a totally different story then. Somehow I had got the incorrect impression that 4.3.0.1 was the latest Solaris version. I will run some tests on T2 and see what happens. Perhaps I had better do the same for the other tickets I have reviewed lately. My apologies!

David


---

Comment by davidloeffler created at 2010-03-16 16:46:09

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-03-16 16:54:25

Changing status from needs_work to needs_info.


---

Comment by davidloeffler created at 2010-03-17 11:56:01

Aargh! 19 hours later, my copy of 4.3.4.alpha1 I was building on T2 for testing is still only half-compiled, and in the meantime 4.3.4.rc0 has come out which is going to break this again!


---

Attachment

apply after bundle + trac_8218_fixes_434alpha1.patch


---

Comment by davidloeffler created at 2010-03-18 15:37:16

Here's a sneaky thing which I only discovered by accident: the reference manual index still points to the removed files in sage/rings that have been moved to sage/rings/finite_rings. This doesn't show up as an error if you install the bundle + patch and then build docs, because the old files are still floating around in the build directory.

I'm putting this back to "needs_review"; once I can get a fully working Sage running on T2 I will test it on that and put it back to "positive review" if it passes.


---

Comment by davidloeffler created at 2010-03-18 15:37:16

Changing status from needs_info to needs_review.


---

Comment by davidloeffler created at 2010-03-21 14:20:42

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-03-21 14:20:42

All seems to be well.


---

Comment by cremona created at 2010-04-03 14:00:13

Replying to [comment:26 davidloeffler]:
> All seems to be well.

David,

Can you list here exactly what needs to be applied (and how)?  I want to start looking at the derivative patches for finite fields, so I have to get a clone with this one installed first -- and as you can see from earlier comments, I have not had much success so far.


---

Comment by davidloeffler created at 2010-04-04 09:32:13

Hi John,

First apply the bundle trac_8218_move_433.bundle, using the commands:

```
hg unbundle http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8218/trac_8218_move_433.bundle
hg merge
hg ci -m "merged finite field bundle"
```

Then use queues in the normal way to import the patches `trac_8218_fixes_434alpha1.patch` and `trac_8218_doc.patch` (in that order). This does work on 4.3.5, I just checked.

But the ball is in David Roe's court as far as the finite field patches are concerned. The sequence is #8218 --> #8332 -> #7880 -> #7883 -> #8333 -> #8334 -> #8335. So far

- #8218 has a positive review
- #7880 has a positive review
- #7883 has been looked at by both me and Rob Bradshaw and we both agree that it needs more work.

Further downstream, #8333 builds independently of #7883, but many things in #8333 are horribly broken unless you also apply #8334, which does _not_ build independently of #7883.

David


---

Comment by cremona created at 2010-04-04 09:43:36

Replying to [comment:28 davidloeffler]:
> Hi John,
> 
...
> 
> David
> 

Thanks!  I saw that some of the later patches had had positive reviews too, so maybe it's a bit late for me to join in.  But I thought that for a complicated interrelated set of patches like this, which non-trivial mathematical content, it would be good to have a small set of people looking at it rather than individuals.


---

Comment by cremona created at 2010-04-04 11:12:24

I built this fine (following David L's instructions above).  Rebuilding the docs produced this:

```
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/finite_field_element.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod.rst:: WARNING: document isn't included in any toctree
/home/john/sage-current/devel/sage/doc/en/reference/sage/rings/integer_mod_ring.rst:: WARNING: document isn't included in any toctree
```

Is this fixed later in the series?  If not, it should be fixed here.  So I am putting this back to "needs work".


---

Comment by cremona created at 2010-04-04 11:12:24

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-04-04 12:28:20

I had this too. I don't think it's a problem with the patch, it is because our documentation build system doesn't do the right thing when source files are removed and produces spurious warnings.


---

Comment by davidloeffler created at 2010-04-04 12:28:20

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-04-04 12:28:46

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 05:18:00

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 05:18:00

Merged in 4.4.alpha0:

 - trac_8218_move_433.bundle
 - trac_8218_fixes_434alpha1.patch
 - trac_8218_doc.patch
