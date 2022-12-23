# Issue 5048: congruence subgroups are not integrated into the coercion model

Issue created by migration from https://trac.sagemath.org/ticket/5048

Original creator: ncalexan

Original creation time: 2009-01-21 08:00:00

Assignee: was

CC:  georgsweber

Keywords: congruence subgroup coercion


```
sage: Gamma0(10).1 * Gamma0(5).2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/4030/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7375)()
    849 
    850 
--> 851 
    852 
    853 

TypeError: unsupported operand parent(s) for '*': 'Congruence Subgroup Gamma0(10)' and 'Congruence Subgroup Gamma0(5)'
```



---

Comment by AlexGhitza created at 2009-01-23 07:07:44

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-21 08:22:29

Changing assignee from was to craigcitro.


---

Comment by davidloeffler created at 2009-07-21 08:22:29

Changing component from number theory to modular forms.


---

Attachment

patch against 4.6.1.alpha3


---

Comment by davidloeffler created at 2010-12-09 20:56:48

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-12-09 20:56:48

Here's a patch. I thought the simplest solution was to arrange that the parent of all congruence subgroup elements was always the (globally unique) SL2Z object, i.e. to make the various subgroup classes "facade parents" (like the prime integers example in the category docs).


---

Attachment

Version that will apply happily after #10452


---

Comment by davidloeffler created at 2010-12-09 21:11:33

I just realised that the patch I just uploaded conflicts, in a rather trivial way, with the patch at #10452. The second patch will apply on top of the patch at #10452. The two patches are identical other than one line of diff context.


---

Comment by davidloeffler created at 2010-12-11 16:16:33

Oh dear, it looks like the trac buildbot is trying to apply both patches at once, hence the red light! But it seems to have done one successful run with only the first patch installed.


---

Comment by davidloeffler created at 2010-12-31 14:51:26

Apply trac_5048-sl2z_coercion-rebased_for_10452.patch
Depends on #10452


---

Comment by davidloeffler created at 2011-01-25 15:40:58

Changing priority from major to minor.


---

Comment by davidloeffler created at 2011-07-15 15:27:59

version rebased to 4.7.1.alpha4 + #11422


---

Attachment

I've uploaded a version that is rebased to apply happily over the positively-reviewed patch #11422. This is intended to form part of a series #10335 - #11422 - #11598 - this ticket - #10453 -
 #11601; but the patch itself is **independent** of #11598 and of the tickets later in the series.


---

Comment by davidloeffler created at 2011-07-17 10:14:34

I'm raising the priority of this to "major" since it is a prerequisite for the (much more significant) patch #11601.


---

Comment by davidloeffler created at 2011-07-17 10:14:34

Changing priority from minor to major.


---

Comment by GeorgSWeber created at 2011-08-10 18:21:00

Hmmm,
is there a quick and easy explanation for the change in the last line of the patch (file "sage/modular/modform/constructor.py")?

- 87	 	         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class'>, 

+ 87	         <class 'sage.modular.arithgroup.congroup_gamma0.Gamma0_class_with_category'>, 


I mean, this might be necessary, but due to the rest of this patch or due to some earlier patch??


---

Comment by davidloeffler created at 2011-08-22 08:15:54

It is necessary because the arithmetic subgroup init routine now calls ` Group.__init__ `, which was not previously the case. The group init routine subsequently calls various other init routines that link arithmetic subgroups into Sage's category framework, with all of its baroque subtleties involving dynamic classes etc.


---

Comment by davidloeffler created at 2011-09-19 12:17:39

Georg: did you get any chance to look at this again? Since #11422 is still waiting around, I've clarified the description to point out that both the pre-#11422 and post-#11422 patches exist and are equally valid.


---

Comment by johanbosman created at 2011-12-17 15:55:09

Changing status from needs_review to positive_review.


---

Comment by johanbosman created at 2011-12-17 15:55:09

The patch still applies to 4.8.alpha4, the code looks sound, and all tests in sage.modular pass.


---

Comment by GeorgSWeber created at 2011-12-17 20:51:57

Hi Johan,
thanks for looking at this one (I guess you're on SD 35 --- if so, I do envy you)!!

I dimly remember that this patch introduced a function with a missing doctest in "sage/modular/arithgroup/congroup_sl2z.py":

 	96	    def __call__(self, x, check=True): 
 	97	        r""" 
 	98	        Create an element of self from x. If check=True (the default), check 
 	99	        that x really defines a 2x2 integer matrix of det 1. 
 	100	        """ 
 	101	        return ArithmeticSubgroupElement(self, x, check=check) 
 	102	 


I'm sorry I never got round to poke David about that (otherwise, the changes were OK for me) --- could you please have second look and check that independently ("sage --coverage ...modular/arithgroups/" or the like should show it)?

Thanks a lot in advance!


Cheers,
Georg


---

Comment by davidloeffler created at 2011-12-17 22:34:13

Good catch, Georg! I will upload a patch shortly with the missing doctest, bringing doctest coverage in sage/modular back up to 100%. Georg, Johan: would either of you mind taking a quick look at the new patch?


---

Comment by davidloeffler created at 2011-12-17 22:34:13

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2011-12-17 22:34:38

apply over previous patch


---

Comment by davidloeffler created at 2011-12-17 22:35:40

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

NOT NEEDED! See comments


---

Comment by davidloeffler created at 2011-12-17 22:43:17

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2011-12-17 22:43:17

Hang on a minute.

It is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. 

So: *ignore* the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.


---

Comment by johanbosman created at 2011-12-17 22:51:36

Replying to [comment:20 davidloeffler]:
> Hang on a minute.
> 
> It is true that there is a doctest missing for this call method, but the missing doctest gets added in the next patch in the series (#11601). So I think we can ignore it here, since #11601 has a positive review; and I can safely reinstate Johan's positive review. 
> 
> So: *ignore* the patch(es) I just uploaded -- it is not needed. I tried to obliterate the first patch by uploading a new blank patch on top of it, but made a hash of that. Perhaps it's time I went to bed.
Indeed.  I was about to mention the same thing, but your comment crossed mine. :).


---

Comment by saraedum created at 2011-12-21 15:26:48

Changing keywords from "congruence subgroup coercion" to "congruence subgroup coercion, sd35".


---

Comment by jdemeyer created at 2012-01-15 21:55:36

Resolution: fixed


---

Comment by davidloeffler created at 2012-03-10 14:17:07

Apply trac_5048-rebased_for_11422.patch

(for the patchbot, so it can understand the prerequisites for #11709)
