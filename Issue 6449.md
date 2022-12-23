# Issue 6449: Additive abelian groups

Issue created by migration from https://trac.sagemath.org/ticket/6449

Original creator: davidloeffler

Original creation time: 2009-06-30 12:10:53

Assignee: joyner

CC:  jhpalmieri mhansen

This is the results of the Abelian groups project at SD16. This is not really finished, but I am going to be pretty busy for the next few weeks so I am posting it here anyway in the hope that somebody else will chip in and finish it off.

This relies on all of the patches at #5882.

The new functionality:

- A new class for additive abelian groups. This is very similar to the finitely presented modules class, but with a slightly different print representation. This is mostly finished (although the string representation of morphisms needs a little work).

- A class for "additive abelian groups embedded in an arbitrary parent". Think rational points on an elliptic curve, for instance, which should be able to derive from this class and transparently inherit code for things like morphisms and subgroups. This is a lot less complete.


---

Comment by davidloeffler created at 2009-06-30 16:43:27

Here are three patches: the first is the new classes, and the second make alterations to the two places where abelian groups are used "in an additive way" in the Sage library to convert them over (which I did chiefly in order to get a feel for how well it would owrk in practice).


---

Comment by jlefebvre created at 2009-07-05 17:01:52

I raised this issue in http://trac.sagemath.org/sage_trac/ticket/6291 , that abelian group has different interface that other groups. In particular, they have no identity function, as opposed to all other groups I've tried in Sage. It's a minor thing, but it makes it annoying when you have code that works with arbitrary group. I've looked at the patch, and it doesn't seem to implement it. I figured I should just complain about it now instead of later :)


---

Comment by cremona created at 2009-12-28 17:45:26

Changing keywords from "" to "abelian group".


---

Comment by cremona created at 2009-12-28 17:45:26

I'm hoping that we can sort this out and get it finished!

Comments on the patches:
    1. Lines 47-53 of patch 1.  Not sure I understand the issue here.  Isn't each coordinate just reduced modulo the appropriate integer (if positive)?
    2. Some functionality (e.g. annihilator()) is presumably inherited from one of the base classes.  I think it would help if this was written down explicitly in comments, especially as there is more than one base class.
    3. As well as an is_multiplicative() returning False, should tere not be an is_additive() returning True?  Or does that exist already from a base class?
    4. You mention a black-box discrete log would be desirable.  We have that in sage/groups/generic.py -- does that do what is needed here?  Or is the problem that that only deals with the cyclic case?
    5. Patch 2 looks quite simple, I have not looked at it in detail.
    6. Patch 3 is mainly changes on doctest output, but also shows how some code can be simplified using the new framework, which is good.

Now I'll actually try applying the patches to 4.3 and see how it looks.


---

Comment by cremona created at 2010-06-27 03:25:22

We (Jim Stankewicz and John Cremona) have applied all three patches to sage-4.4.4.  A very small amount of rebasing was needed.  We have so far tested all of additive_abelian_groups, homology, and elliptic_curves;  some more fixing was needed which is in the 4th patch.  Some of the changes in this last patch were just fixing some mistakes made in rebasing manually.

We are now testing the whole Sage library, but the ticket is ready for review (again!)


---

Comment by cremona created at 2010-06-27 03:25:22

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-06-27 05:17:17

Positive review on John Cremona's patch, and the rest (that I looked at) looks good too.


---

Comment by robertwb created at 2010-06-27 05:17:17

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-30 17:38:16

Can you upload your rebased versions of the patches?


---

Comment by cremona created at 2010-06-30 17:56:23

Replying to [comment:9 davidloeffler]:
> Can you upload your rebased versions of the patches?

I think the 4th (review) patch does what is necessary.  Does it?  I remember doing some manual editing after applying the first three (there were some hunks rejected), and that would be reflected in the last patch.

If that does not work, ask again.  I still have that queue on my laptop.


---

Comment by davidloeffler created at 2010-06-30 18:04:29

I don't think it works like that. Perhaps the best thing is if you qfold what you've got on your laptop into a single new rebased patch.


---

Comment by cremona created at 2010-06-30 19:46:37

Replying to [comment:11 davidloeffler]:
> I don't think it works like that. Perhaps the best thing is if you qfold what you've got on your laptop into a single new rebased patch.

Sorry, this will have to wait, as I am falling asleep and it has not worked so far.


---

Comment by cremona created at 2010-07-01 09:50:17

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-07-01 09:50:17

Sorry about that.  There was only trivial rebasing needed to the first patch (it fixed some small bugs in mrange, and those had already been fixed elsewhere, so it was possible to just ignore the failing hunks).  The patch named trac_6449-1a-abgps.patch can therefore replace the one named trac_6449-1-abgps.patch, followed by -2, -3 and -review.  These apply to 4.5.alpha0 (and probably also to 4.4.4, but my 4.4.4 build is currently devoted to the pari upgrade).  I am currently testing the whole sage library -- done (see below).

If a single folded patch is still required I should be able to do that, but applying 4 patches is not as bad as on some tickets (and they are logically separate).

There is one doctest failure:

```
File "/storage/jec/sage-4.5.alpha0/devel/sage-6449/sage/groups/abelian_gps/abelian_group.py", line 538:
    sage: bool(T) # indirect doctest
Expected:
    False
Got:
    True
```

I suggest changing the code of that one-line function to 

```
return self.order()>1
```

but I don't actually know what is going on there as it's an indirect doctest!


---

Comment by davidloeffler created at 2010-07-01 10:19:44

Replying to [comment:13 cremona]:
> Sorry about that.  There was only trivial rebasing needed to the first patch (it fixed some small bugs in mrange, and those had already been fixed elsewhere, so it was possible to just ignore the failing hunks).  

Yes, that part of the patch got factored out as #6561.

> There is one doctest failure [...]
> but I don't actually know what is going on there as it's an indirect doctest!

Hmm. I see what's happening: that doctest assumes that elliptic curve torsion subgroups are an instance of the old `AbelianGroup` class, while the new patch makes them an instance of my new `AdditiveAbelianGroup`. Patch coming up.

David


---

Comment by davidloeffler created at 2010-07-01 10:28:59

Here's a patch. I haven't dealt with the more general problem of checking that `__nonzero__` is consistently implemented -- that's a matter for another ticket, if anybody cares -- but with this patch the offending doctest does pass.


---

Comment by davidloeffler created at 2010-07-01 10:28:59

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-07-01 10:36:54

Looks good, so I am putting this back to positive review (originally positively reviewed by Robert Bradshaw).


---

Comment by cremona created at 2010-07-01 10:36:54

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-01 12:10:49

I actually made that last patch without the other patches applied :-) So I've now realised that there is a problem with applying those patches; whatever I do it won't apply cleanly. If I apply

```
trac_6449-1a-abgps.patch
trac_6449-2-homology.patch
trac_6449-3-elliptic.patch
```

then I get a bunch of rejects. If I just delete the .rej files and apply `trac_6449-review.patch` I get even more rejects, and a whole load of doctests fail in elliptic curves. I spent a while fixing them -- most were trivial (although tedious), but one stubborn failure in BSD.py required me to add half a dozen lines of new code to get the coercion system to behave itself; this isn't something that can be left to the release manager!

So I urge you to go through your personal patch stack, check that everything's qrefreshed, qfold the lot, check it applies 100% cleanly and upload it. (Make sure you don't qpop patches that applied with rejects without qrefreshing them first, even if you didn't make any changes yourself before creating/applying the next patch -- you need to qrefresh so hg knows you've dealt with the rejects. I just made that mistake.) 

Alternatively, I can fold and upload what I've got here, and point you to the minor change I had to make to get BSD.py to pass.

David


---

Comment by davidloeffler created at 2010-07-01 12:10:49

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-07-01 12:39:16

This does not make any sense at all.   I took a fresh clone of 4.5.alpha0 and applied the four patches with rejects and all relevant tests (except that little one) passed.  Can you try again with a pristine build?

Since Jim and I already went through those minor doctest failures fixing them, it's a great pity that you repeated the work.


---

Comment by davidloeffler created at 2010-07-01 12:53:57

I made a completely fresh clone. Here's what happened:

```
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel$ cd sage-abgp/
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449-1a-abgps.patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449-2-homology.patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449-3-elliptic.patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449-review.patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449-doctest_fix.patch                             
adding trac_6449-1a-abgps.patch to series file                                                                
adding trac_6449-2-homology.patch to series file                                                              
adding trac_6449-3-elliptic.patch to series file                                                              
adding trac_6449-review.patch to series file                                                                  
adding trac_6449-doctest_fix.patch to series file                                                             
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qpush                               
applying trac_6449-1a-abgps.patch                                                                             
now at: trac_6449-1a-abgps.patch                                                                              
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qpush                               
applying trac_6449-2-homology.patch                                                                           
now at: trac_6449-2-homology.patch                                                                            
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qpush                               
applying trac_6449-3-elliptic.patch                                                                           
patching file sage/schemes/elliptic_curves/ell_finite_field.py                                                
Hunk #3 FAILED at 1205                                                                                        
Hunk #5 FAILED at 1295                                                                                        
2 out of 6 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_finite_field.py.rej        
patching file sage/schemes/elliptic_curves/ell_torsion.py                                                     
Hunk #6 succeeded at 102 with fuzz 2 (offset 0 lines).                                                        
Hunk #7 succeeded at 149 with fuzz 2 (offset 0 lines).                                                        
patching file sage/schemes/elliptic_curves/padics.py                                                          
Hunk #2 FAILED at 611                                                                                         
1 out of 2 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/padics.py.rej                  
patch failed, unable to continue (try -v)                                                                     
patch failed, rejects left in working dir                                                                     
errors during apply, please fix and refresh trac_6449-3-elliptic.patch                                        
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ find -name "*.rej" | xargs rm; mysage -hg qrefresh                  
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qpush
applying trac_6449-review.patch                                                
patching file sage/schemes/elliptic_curves/ell_finite_field.py                 
Hunk #1 FAILED at 1418                                                         
Hunk #2 FAILED at 1444                                                         
2 out of 2 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_finite_field.py.rej
patch failed, unable to continue (try -v)                                                             
patch failed, rejects left in working dir                                                             
errors during apply, please fix and refresh trac_6449-review.patch                                    
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ find -name "*.rej" | xargs rm; mysage -hg qrefresh                                                                                                           
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -hg qpushapplying trac_6449-doctest_fix.patch                                           
now at: trac_6449-doctest_fix.patch                                            
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ find -name "*.rej" | xargs rm; mysage -hg qrefresh                                                                                                           
rm: missing operand                                                                                           
Try `rm --help' for more information.                                                                         
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$ mysage -b; mysage -tp 16 sage/schemes/elliptic_curves/                                                                                                       

----------------------------------------------------------
sage: Building and installing modified Sage library files.
[snip]
Testing that Sage starts...
Yes, Sage starts.          
Global iterations: 1       
File iterations: 1         
Using cached timings to run longest doctests first.
Doctesting 38 files doing 16 jobs in parallel      
sage -t  sage/schemes/elliptic_curves/__init__.py  
         [0.1 s]                                   
sage -t  sage/schemes/elliptic_curves/ec_database.py
         [2.5 s]                                    
sage -t  sage/schemes/elliptic_curves/all.py        
         [2.7 s]                                    
sage -t  sage/schemes/elliptic_curves/cm.py         
         [2.8 s]
sage -t  sage/schemes/elliptic_curves/ell_padic_field.py
         [2.9 s]                                        
sage -t  sage/schemes/elliptic_curves/ell_local_data.py 
         [5.8 s]                                        
sage -t  sage/schemes/elliptic_curves/ell_wp.py         
         [3.9 s]                                        
sage -t  sage/schemes/elliptic_curves/ell_field.py
         [8.8 s]
sage -t  sage/schemes/elliptic_curves/descent_two_isogeny.pyx
         [9.1 s]                                             
sage -t  sage/schemes/elliptic_curves/ell_tate_curve.py      
         [9.3 s]                                             
sage -t  sage/schemes/elliptic_curves/gp_simon.py            
         [3.8 s]                                             
sage -t  sage/schemes/elliptic_curves/ell_torsion.py         
         [10.5 s]                                            
sage -t  sage/schemes/elliptic_curves/gp_cremona.py          
         [4.9 s]                                             
sage -t  sage/schemes/elliptic_curves/gal_reps.py            
         [7.3 s]                                             
sage -t  sage/schemes/elliptic_curves/kodaira_symbol.py      
         [2.4 s]                                             
sage -t  sage/schemes/elliptic_curves/mod5family.py          
         [2.9 s]                                             
sage -t  sage/schemes/elliptic_curves/modular_parametrization.py
         [3.6 s]                                                
sage -t  sage/schemes/elliptic_curves/monsky_washnitzer.py      
         [4.0 s]                                                
sage -t  sage/schemes/elliptic_curves/padic_height.py           
         [3.2 s]                                                
sage -t  sage/schemes/elliptic_curves/BSD.py                    
Exception raised by doctesting framework. Use -verbose for details.
         [20.7 s]                                                  
sage -t  sage/schemes/elliptic_curves/lseries_ell.py               
         [9.0 s]                                                   
sage -t  sage/schemes/elliptic_curves/sea.py                       
         [2.1 s]                                                   
sage -t  sage/schemes/elliptic_curves/weierstrass_morphism.py      
         [3.6 s]                                                   
sage -t  sage/schemes/elliptic_curves/constructor.py
         [29.8 s]
sage -t  sage/schemes/elliptic_curves/ell_finite_field.py
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py", line 1421:                                                                                                         
    sage: E.abelian_group()                                                                                   
Expected:                                                                                                     
    (Multiplicative Abelian Group isomorphic to C10, ...                                                      
Got:                                                                                                          
    Additive abelian group isomorphic to Z/10 embedded in Abelian group of points on Elliptic Curve defined by y^2 = x^3 + 2*x + 5 over Finite Field of size 11                                                             
**********************************************************************                                        
File "/storage/masiao/sage-4.5.alpha1/devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py", line 1427:                                                                                                         
    sage: E.abelian_group()                                                                                   
Expected:                                                                                                     
    (Multiplicative Abelian Group isomorphic to C22 x C2, ...                                                 
Got:                                                                                                          
    Additive abelian group isomorphic to Z/2 + Z/22 embedded in Abelian group of points on Elliptic Curve defined by y^2 = x^3 + 2*x + 5 over Finite Field of size 41                                                       
**********************************************************************                                        
File "/storage/masiao/sage-4.5.alpha1/devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py", line 1434:                                                                                                         
    sage: E.abelian_group()                                                                                   
Expected:                                                                                                     
    (Multiplicative Abelian Group isomorphic to C26 x C26, ...                                                
Got:                                                                                                          
    Additive abelian group isomorphic to Z/26 + Z/26 embedded in Abelian group of points on Elliptic Curve defined by y^2 = x^3 + (a^4+a^3+2*a^2+2*a)*x + (2*a^5+2*a^3+2*a^2+1) over Finite Field in a of size 3^6          
**********************************************************************                                        
File "/storage/masiao/sage-4.5.alpha1/devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py", line 1441:                                                                                                         
    sage: E.abelian_group()                                                                                   
Expected:                                                                                                     
    (Multiplicative Abelian Group isomorphic to C1031352, ...                                                 
Got:                                                                                                          
    Additive abelian group isomorphic to Z/1031352 embedded in Abelian group of points on Elliptic Curve defined by y^2 = x^3 + (2*a^2+48*a+27)*x + (89*a^2+76*a+24) over Finite Field in a of size 101^3                   
**********************************************************************                                        
File "/storage/masiao/sage-4.5.alpha1/devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py", line 1447:                                                                                                         
    sage: E.abelian_group()                                                                                   
Expected:                                                                                                     
    (Trivial Abelian Group, ())                                                                               
Got:                                                                                                          
    Trivial group embedded in Abelian group of points on Elliptic Curve defined by y^2 + y = x^3 + x + 1 over Finite Field of size 2                                                                                        
**********************************************************************                                        
1 items had failures:                                                                                         
   5 of  24 in __main__.example_24                                                                            
***Test Failed*** 5 failures.                                                                                 
For whitespace errors, see the file /home/masiao/.sage//tmp/.doctest_ell_finite_field.py                      
         [34.9 s]                                                                                             
sage -t  sage/schemes/elliptic_curves/period_lattice.py                                                       
         [18.6 s]                                                                                             
sage -t  sage/schemes/elliptic_curves/formal_group.py                                                         
         [33.2 s]                                                                                             
sage -t  sage/schemes/elliptic_curves/ell_modular_symbols.py                                                  
         [39.3 s]                                                                                             
sage -t  sage/schemes/elliptic_curves/padics.py
         [21.6 s]
sage -t  sage/schemes/elliptic_curves/ell_egros.py
         [41.1 s]
sage -t  sage/schemes/elliptic_curves/ell_curve_isogeny.py
         [45.4 s]
sage -t  sage/schemes/elliptic_curves/ell_generic.py
         [48.5 s]
sage -t  sage/schemes/elliptic_curves/ell_point.py
         [51.0 s]
sage -t  sage/schemes/elliptic_curves/padic_lseries.py
         [42.0 s]
sage -t  sage/schemes/elliptic_curves/ell_rational_field.py
         [62.7 s]
sage -t  sage/schemes/elliptic_curves/ell_number_field.py
         [67.5 s]
sage -t  sage/schemes/elliptic_curves/sha_tate.py
         [55.0 s]
sage -t  sage/schemes/elliptic_curves/heegner.py
         [97.1 s]

----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage-abgp/sage/schemes/elliptic_curves/BSD.py # Exception from doctest framework
        sage -t  devel/sage-abgp/sage/schemes/elliptic_curves/ell_finite_field.py # 5 doctests failed
        
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 109.3 seconds
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgp$
```


The only explanation I can come up with is that this has something to do with #9127, which was more or less the only non-graph-theory patch merged in 4.5.alpha1.

David


---

Comment by cremona created at 2010-07-01 13:08:44

I can't be #9127 -- all that does is add three dots to a doctest output!

I'll try again with alpha1, but I am seeing tutees all afternoon.


---

Comment by davidloeffler created at 2010-07-01 15:19:10

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-07-01 15:19:10

I guess the moral here is that one can't rely on an old outdated patch always failing in exactly the same way, i.e. the selection of exactly which hunks apply and which don't seems to be a bit random. 

Anyway: another issue here is the danger of conflicts with other positively-reviewed patches which touch elliptic curves. Right now there are 13 of these from 11 tickets: 7930, 8680, 9087, 9110, 9266, 9287, 9302, 9313, 9324, 9342 and 9372. 

So I downloaded all of these, applied the patches from this ticket (including the review patch), and cleaned up the mess, and everything was fine except for one thing: there wasn't a coercion from the torsion subgroup of an elliptic curve to the full M-W group, and more generally from an additive abelian group wrapper to its "universe", which causes the doctest failure in BSD.py reported in my previous message. I added an UnwrappingMorphism class to additive_abelian_wrapper which does exactly that. With that change, all doctests seem to pass.

It turns out that the patch thus obtained actually doesn't conflict with any of the other positively reviewed patches above except #9278, but you need that one installed. It passes doctests both with and without the other 10 tickets. If someone could quickly check that the new UnwrappingMorphism looks plausible, then I think this will finally be ready to merge.


---

Attachment

Qfolded patch. Applies to 4.5.alpha1 with the patches from #9287.


---

Comment by cremona created at 2010-07-01 15:36:26

I'm very grateful to the time you have spent on this.  I guess it is not surprising that there are lots of e.c. patches in the pipeline given that we are nearing the end of a 2-week Sage Days on Computing with Elliptic Curves.

I'm about to look through those patches, which I am re-listing here: #7930, #8680, #9087, #9110, #9266, #9287, #9302, #9313, #9324, #9342 and #9372 so that trac can make links to make the job easier!


---

Comment by cremona created at 2010-07-01 16:17:18

Well:   on my newly built 4.5.alpha1 and in a new clone:

```
jec@selmer%pwd
/home/jec/storage/sage-4.5.alpha1
jec@selmer%cd devel/sage-6449/
jec@selmer%hg qinit
jec@selmer%hg qimp ~/trac_6449-1a-abgps.patch 
adding trac_6449-1a-abgps.patch to series file
jec@selmer%hg qpush
applying trac_6449-1a-abgps.patch
now at: trac_6449-1a-abgps.patch
jec@selmer%hg qimp ~/trac_6449-2-homology.patch 
adding trac_6449-2-homology.patch to series file
jec@selmer%hg qpush
applying trac_6449-2-homology.patch
now at: trac_6449-2-homology.patch
jec@selmer%hg qimp ~/trac_6449-3-elliptic.patch 
adding trac_6449-3-elliptic.patch to series file
jec@selmer%hg qpush
applying trac_6449-3-elliptic.patch
now at: trac_6449-3-elliptic.patch
jec@selmer%hg qimp ~/trac_6449-review.patch 
adding trac_6449-review.patch to series file
jec@selmer%hg qpush
applying trac_6449-review.patch
now at: trac_6449-review.patch
jec@selmer%sage -b
```

which I am now testing.  Then I'll try again with the new folded patch!


---

Comment by cremona created at 2010-07-01 16:38:36

The alpha1 test showed up these:

```
	sage -t  devel/sage-6449/sage/groups/abelian_gps/abelian_group.py # 1 doctests failed
	sage -t  devel/sage-6449/sage/schemes/elliptic_curves/BSD.py # Exception from doctest framework
	sage -t  devel/sage-6449/sage/tests/book_stein_ent.py # 4 doctests failed
	sage -t  devel/sage-6449/sage/modular/modsym/space.py # 3 doctests failed
```

where the first one is the little one fixed by youur doctest patch and the others are trivialities caused by the different output of torsion groups now.

Next I'll test the new folded patch... applies ok, starting to test.


---

Comment by davidloeffler created at 2010-07-01 17:35:30

The folded patch should deal with the first two. I also saw the other two you mention, which are both coming from the fact that `invariants` now returns a tuple instead of a string; and if you test the docs as well I imagine you will see a failure in `constructions/elliptic_curves.rst`. These remaining issues should be fixed by the patch I am about to upload.


---

Attachment

Apply on top of #9287 and trac_6449_everything.patch


---

Comment by cremona created at 2010-07-01 22:04:16

Strangely, when I applied the combined (folded) patch to 4.5.alpha1 (which applied cleanly) and then ran sage -t on everything there were thousands or errors including many totally unrelated.  I don't think that is a trustworthy test and will try again tomorrow.


---

Comment by cremona created at 2010-07-02 11:18:30

OK, did sage -ba and then a complete test (this is with the big folded patch but not the ones-that-got-away) and found only these:

```
	sage -t  devel/sage-6449/sage/all.py # 0 doctests failed
	sage -t  devel/sage-6449/sage/tests/book_stein_ent.py # 4 doctests failed
	sage -t  devel/sage-6449/sage/modular/modsym/space.py # 3 doctests failed
```

of which the first can be ignored, the second and third are treated by ones-that-got-away.

But applying the ones-that-got-away fails as follows:

```
applying trac_6449_ones_that_got_away.patch
patching file sage/modular/modsym/space.py
Hunk #1 FAILED at 2203
Hunk #2 FAILED at 2213
Hunk #3 FAILED at 2226
3 out of 3 hunks FAILED -- saving rejects to file sage/modular/modsym/space.py.rej
```

which is odd.  Still, we are nearly there.


---

Comment by davidloeffler created at 2010-07-02 11:28:06

Oops, sorry. Mea culpa. I forgot to mention that I made the ones-that-got-away patch with the sage library patch from #8680 in place -- RLM has promised that nothing else will get merged until #8680 does. If you apply that before ones-that-got-away, the latter should apply fully cleanly.


---

Comment by cremona created at 2010-07-02 12:00:42

apply instead of previous one


---

Attachment

OK, I will try that -- in which case we might ignore trac_6449_ones_that_got_away.1.patch which I just uploaded.


---

Comment by cremona created at 2010-07-02 13:26:58

Please list exactly which patches one needs to apply, in order, to 4.5.alpha1, including those on the other ticket.  It's not clear from the above whether the tabs patches need applying before all these or in between or what: I found no order in which everything works, except when I ignore the tabs patches and apply just 

trac_6449_everything.patch
trac_6449_ones_that_got_away.1.patch


---

Comment by davidloeffler created at 2010-07-02 17:53:51

I'm mystified that it's not working for you. I just created yet another new clone on selmer, downloading the patches afresh from trac, and it works fine there too. See session transcript below.

One order of patches that works (for me) is:

```
trac_9287.coverage_for_elliptic_curves_part1.patch                            
trac_9287.coverage_for_elliptic_curves_part2.patch                            
trac_6449_everything.patch                                                    
trac_8680-untabify-4.5.alpha1.patch                                           
trac_8680-tinyfix.patch                                                       
trac_6449_ones_that_got_away.patch                                            
```


#8680 can also come earlier in the sequence -- everything except trac_6449_ones_that_got_away.patch is independent of it.


```
david@rockhopper:~> ssh selmer.warwick.ac.uk
[...]                           
Last login: Fri Jul  2 09:42:07 2010 from 92.17.192.129
masiao@selmer:~$ cd /storage/masiao/sage-4.5.alpha1/
masiao@selmer:/storage/masiao/sage-4.5.alpha1$ ./sage -b main
[...]
masiao@selmer:/storage/masiao/sage-4.5.alpha1$ ./sage -clone abgps
[...]
masiao@selmer:/storage/masiao/sage-4.5.alpha1$ cd devel/sage-abgps
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgps$ ../../sage -hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9287/trac_9287.coverage_for_elliptic_curves_part1.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9287/trac_9287.coverage_for_elliptic_curves_part2.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449_everything.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8680/trac_8680-untabify-4.5.alpha1.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8680/trac_8680-tinyfix.patch \
http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6449/trac_6449_ones_that_got_away.patch                                                                                        
adding trac_9287.coverage_for_elliptic_curves_part1.patch to series file                                      
adding trac_9287.coverage_for_elliptic_curves_part2.patch to series file                                      
adding trac_6449_everything.patch to series file                                                              
adding trac_8680-untabify-4.5.alpha1.patch to series file                                                     
adding trac_8680-tinyfix.patch to series file                                                                 
adding trac_6449_ones_that_got_away.patch to series file                                                      
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgps$ ../../sage -hg qpush -a
applying trac_9287.coverage_for_elliptic_curves_part1.patch                            
applying trac_9287.coverage_for_elliptic_curves_part2.patch                            
applying trac_6449_everything.patch                                                    
applying trac_8680-untabify-4.5.alpha1.patch                                           
applying trac_8680-tinyfix.patch                                                       
applying trac_6449_ones_that_got_away.patch                                            
now at: trac_6449_ones_that_got_away.patch                                             
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgps$ export MAKE="make -j16"; ../../sage -b
[builds with no errors]
masiao@selmer:/storage/masiao/sage-4.5.alpha1/devel/sage-abgps$
```



---

Comment by jhpalmieri created at 2010-07-02 22:14:28

Replying to [comment:31 davidloeffler]:
> I'm mystified that it's not working for you. I just created yet another new clone on selmer, downloading the patches afresh from trac, and it works fine there too. See session transcript below.
> 
> One order of patches that works (for me) is:

```
trac_9287.coverage_for_elliptic_curves_part1.patch                            
trac_9287.coverage_for_elliptic_curves_part2.patch                            
trac_6449_everything.patch                                                    
trac_8680-untabify-4.5.alpha1.patch                                           
trac_8680-tinyfix.patch                                                       
trac_6449_ones_that_got_away.patch                                            
```


For what it's worth, this worked for me on a fresh install of 4.5.alpha1 on two different machines.  All tests pass on sage.math.


---

Comment by cremona created at 2010-07-05 17:03:21

OK, so I rebuilt my 4.5.alpha1 from scratch and now the patches do apply ok in the order you give.  I'll test too but do not expect any surprises.

However, I definitely think it is unacceptable (to the release manager, for a start) for the patches on one ticket to have to be applied with two patches from another ticket *in between* them!  That will surely cause a delay.


---

Comment by jhpalmieri created at 2010-07-05 18:00:41

#8680 has now been merged, and in one of my tests, I applied both of the patches from #8680 before both of the patches here, and it worked fine.  So I think at this point just merging the patches from #9287 before the patches here should be good enough.  No need to merge patches from any ticket in between two of the patches from another one.

John (Cremona): I'll leave this to you to restore to "positive review" if your tests pass.


---

Comment by cremona created at 2010-07-05 19:32:39

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-07-05 19:32:39

My tests passed , so let's roll.


---

Comment by mhansen created at 2010-07-11 01:31:00

What about all of the functions in additive_abelian_wrapper.py with no doctests?


---

Comment by cremona created at 2010-07-11 11:09:43

Replying to [comment:36 mhansen]:
> What about all of the functions in additive_abelian_wrapper.py with no doctests?

Good point.  David, any chance you could oblige?


---

Attachment

Here's a patch with the missing doctests. The current situation is that one needs to apply:

- the #9287 patches
- trac_6449_everything.patch
- trac_6449_ones_that_got_away.patch
- trac_6449_more_doctests.patch

If someone with trac admin rights could delete all the other patches that would be helpful.

David


---

Comment by cremona created at 2010-07-11 20:32:41

I checked that the patches as specified by David, and repeated here:

    1. trac_9287.coverage_for_elliptic_curves_part1.patch
    2. trac_9287.coverage_for_elliptic_curves_part2.patch
    3. trac_6449_everything.patch
    4. trac_6449_ones_that_got_away.patch
    5. trac_6449_more_doctests.patch

apply ok to 4.5.alpha4.  The new doctests look fine and pass, and coverage in this directory is now 100%.

I have therefore left the tag as "positive review" and hope that mhansen is now happy!


---

Comment by mpatel created at 2010-07-20 07:09:01

Resolution: fixed


---

Comment by mpatel created at 2010-07-20 07:12:04

Replying to [comment:39 cremona]:
> I checked that the patches as specified by David, and repeated here:
> 
>     1. trac_9287.coverage_for_elliptic_curves_part1.patch
>     2. trac_9287.coverage_for_elliptic_curves_part2.patch
>     3. trac_6449_everything.patch
>     4. trac_6449_ones_that_got_away.patch
>     5. trac_6449_more_doctests.patch
> 
> apply ok to 4.5.alpha4.  The new doctests look fine and pass, and coverage in this directory is now 100%.
> 
> I have therefore left the tag as "positive review" and hope that mhansen is now happy!

For the record, I did _not_ apply [attachment:trac_6449_ones_that_got_away.1.patch] to 4.5.2.alpha0.
