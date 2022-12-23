# Issue 9383: Adding quadratic_forms Code to the Reference Manual

Issue created by migration from https://trac.sagemath.org/ticket/9383

Original creator: annahaensch

Original creation time: 2010-06-29 21:02:50

Assignee: mvngu




---

Attachment

quadratic_forms reference manual docbuild


---

Comment by annahaensch created at 2010-07-01 05:28:56

This is half of the quadratic_forms documentation, I'll post the second half in an updated patch tomorrow.


---

Comment by annahaensch created at 2010-07-01 05:28:56

Changing priority from major to minor.


---

Comment by annahaensch created at 2010-07-01 20:44:42

Use instead of trac_9383.patch


---

Attachment

This patch should complete the reference documentation for quadratic forms.  It's still returning a warning that the file is not contained in a toctree.  Ideas?


---

Comment by annahaensch created at 2010-07-01 20:54:40

Changing status from new to needs_review.


---

Attachment

Use in place of all previous patches


---

Comment by davidloeffler created at 2010-07-28 19:20:43

It looks to me like you forgot to do "hg add" on your new file doc/en/reference/quadratic_forms.rst. Hence when I apply the patch to a new clone and build, I get an error 
`/storage/masiao/sage-4.5.2.alpha1/devel/sage/doc/en/reference/index.rst:40: (WARNING/2) toctree references unknown document u'quadratic_forms'`
and nothing new appears in the ref manual.

David


---

Comment by davidloeffler created at 2010-07-28 19:20:43

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-07-28 19:23:01

BTW: the reference manual building code can behave very oddly when files have been deleted -- because of the way that the Sphinx parser caches its environment, it's next to impossible to squash the "document not included in any toctree" error, except by creating a new clean clone and applying your patch to that.


---

Attachment

replaces all previous patches


---

Comment by davidloeffler created at 2010-08-03 13:58:29

Changing priority from minor to major.


---

Comment by davidloeffler created at 2010-08-03 13:58:29

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-08-03 13:58:29

Changing keywords from "" to "quadratic forms".


---

Comment by davidloeffler created at 2010-08-03 14:01:37

Here's a new patch, against 4.5.2.rc0, incorporating Anna's work and extending it by adding the modules `count_local_2` and `special_values`. 

The results are a little scruffy in places, but that will be much easier to sort out once the modules have been added and people can see the results!


---

Comment by mvngu created at 2010-09-21 07:50:02

I'm OK with the attachment [attachment:trac_9383_v4.patch]. Note that it adds the following modules to the reference manual:


```
sage/quadratic_forms/quadratic_form 
sage/quadratic_forms/binary_qf 
sage/quadratic_forms/constructions 
sage/quadratic_forms/random_quadraticform 
sage/quadratic_forms/special_values 
sage/quadratic_forms/count_local_2
```


The attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:


```
sage/quadratic_forms/quadratic_form__automorphisms.py
sage/quadratic_forms/quadratic_form__count_local_2.py
sage/quadratic_forms/quadratic_form__equivalence_testing.py
sage/quadratic_forms/quadratic_form__genus.py
sage/quadratic_forms/quadratic_form__local_density_congruence.py
sage/quadratic_forms/quadratic_form__local_density_interfaces.py
sage/quadratic_forms/quadratic_form__local_field_invariants.py
sage/quadratic_forms/quadratic_form__local_normal_form.py
sage/quadratic_forms/quadratic_form__local_representation_conditions.py
sage/quadratic_forms/quadratic_form__mass.py
sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py
sage/quadratic_forms/quadratic_form__neighbors.py
sage/quadratic_forms/quadratic_form__reduction_theory.py
sage/quadratic_forms/quadratic_form__siegel_product.py
sage/quadratic_forms/quadratic_form__split_local_covering.py
sage/quadratic_forms/quadratic_form__ternary_Tornaria.py
sage/quadratic_forms/quadratic_form__theta.py
sage/quadratic_forms/quadratic_form__variable_substitutions.py
```


The [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.


---

Comment by mvngu created at 2010-09-21 07:50:02

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-21 15:21:11

Replying to [comment:7 mvngu]:
> The attachment make numerous ReST changes to the following modules, but does not add them to the reference manual:
> 
> {{{
> sage/quadratic_forms/quadratic_form__automorphisms.py
> sage/quadratic_forms/quadratic_form__count_local_2.py
> sage/quadratic_forms/quadratic_form__equivalence_testing.py
> sage/quadratic_forms/quadratic_form__genus.py
> sage/quadratic_forms/quadratic_form__local_density_congruence.py
> sage/quadratic_forms/quadratic_form__local_density_interfaces.py
> sage/quadratic_forms/quadratic_form__local_field_invariants.py
> sage/quadratic_forms/quadratic_form__local_normal_form.py
> sage/quadratic_forms/quadratic_form__local_representation_conditions.py
> sage/quadratic_forms/quadratic_form__mass.py
> sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py
> sage/quadratic_forms/quadratic_form__mass__Siegel_densities.py
> sage/quadratic_forms/quadratic_form__neighbors.py
> sage/quadratic_forms/quadratic_form__reduction_theory.py
> sage/quadratic_forms/quadratic_form__siegel_product.py
> sage/quadratic_forms/quadratic_form__split_local_covering.py
> sage/quadratic_forms/quadratic_form__ternary_Tornaria.py
> sage/quadratic_forms/quadratic_form__theta.py
> sage/quadratic_forms/quadratic_form__variable_substitutions.py
> }}}
> 
> The [attachment:trac_9383_v4.patch] receives a positive review as is. If you want, you could open another ticket to add the missing modules to the reference manual.

No, there is no need to do this. The functions from those modules are all imported into quadratic__form.py; they are divided into separate modules solely in order to keep the size of the top-level file manageable. The ReST parser follows these imports, so adding the separate files to the manual as well would just mean everything was in there twice.

Thanks for the review, anyway!

David


---

Comment by mpatel created at 2010-09-28 09:10:53

Resolution: fixed
