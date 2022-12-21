# Issue 8359: Coxeter groups as permutation groups

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-02-25 08:48:26

Assignee: sage-combinat

CC:  sage-combinat

Keywords: Coxeter groups, permutation groups, chevie

Patch in dev on the sage-combinat server


---

Comment by nthiery created at 2010-06-01 20:39:35

Changing status from new to needs_work.


---

Comment by aschilling created at 2013-01-23 15:11:16

This patch was developed and tested on the sage-combinat queue by myself and Mike Hansen. It is ready to go!


---

Comment by aschilling created at 2013-01-23 15:11:46

Changing status from needs_work to needs_review.


---

Comment by aschilling created at 2013-01-23 15:12:02

Changing status from needs_review to positive_review.


---

Comment by aschilling created at 2013-01-25 13:55:24

We made changes to make the doctests pass. Not sure what the problem with the plugins are.


---

Comment by jdemeyer created at 2013-01-26 12:46:24

You should never use `except:` without an exception type, otherwise you would catch some unwanted exceptions.  Catch specific exceptions instead (or `except Exception:` if you want to catch all actual exceptions).


---

Comment by jdemeyer created at 2013-01-26 14:02:00

There is a problem with the documentation:

```
/release/merger/sage-5.7.beta2/local/lib/python2.7/site-packages/sage/combinat/root_system/coxeter_group.py:docstring of sage.combinat.root_system.coxeter_group.CoxeterGroupAsPermutationGroup.Element.has_descent:3: WARNING: more than one target found for cross-reference u'descents': sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ElementMethods.descents, sage.categories.coxeter_groups.CoxeterGroups.ElementMethods.descents, sage.combinat.tableau.Tableau.descents, sage.combinat.sf.ns_macdonald.AugmentedLatticeDiagramFilling.descents, sage.combinat.permutation.Permutation_class.descents, sage.combinat.composition.Composition_class.descents
```



---

Comment by jdemeyer created at 2013-01-26 14:02:00

Changing status from positive_review to needs_work.


---

Comment by aschilling created at 2013-01-26 17:58:38

Both issues fixed!


---

Comment by aschilling created at 2013-01-26 17:58:52

Changing status from needs_work to positive_review.


---

Comment by nthiery created at 2013-02-01 14:38:03

Hi Jeroen,

Should we ignore jehova's patchbot failure (the log and shortlog seem empty)?

Is the plugin.startup failure a suggestion for lazy importing CoxeterGroup?

Thanks!

               Nicolas


---

Comment by aschilling created at 2013-02-02 19:05:49

In consultation with Nicolas, I fixed some failing doctests in /combinat/root_systems/coxeter_group.py for type H3.

Anne


---

Attachment


---

Comment by aschilling created at 2013-02-04 23:07:36

Removed trailing white spaces.

Anne


---

Comment by jdemeyer created at 2013-02-05 08:22:16

Resolution: fixed
