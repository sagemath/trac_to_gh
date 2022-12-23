# Issue 5180: [with patch, needs review] Improvements to congruence subgroups

Issue created by migration from https://trac.sagemath.org/ticket/5180

Original creator: davidloeffler

Original creation time: 2009-02-04 18:35:29

Assignee: craigcitro

CC:  craigcitro georgsweber

Keywords: congruence subgroups

The attached patch splits up the code for congruence subgroups into several files in a directory sage/modular/congroups. The old file sage/modular/congroup.py still exists, so pickles created with previous versions should unpickle safely under the new one.

I've added a little functionality in the process: congruence subgroups can now calculate the width and regularity of their cusps, and their number of elliptic points.


---

Comment by davidloeffler created at 2009-02-04 18:41:01

Oops, just realised that is the wrong patch -- wait a moment


---

Comment by davidloeffler created at 2009-02-04 18:41:01

Changing assignee from craigcitro to davidloeffler.


---

Comment by davidloeffler created at 2009-02-04 19:07:27

patch against 3.3.alpha3


---

Comment by davidloeffler created at 2009-02-04 19:10:27

Changing status from new to assigned.


---

Attachment

OK, that's the right patch (replacing the old one).


---

Comment by mabshoff created at 2009-02-06 23:02:53

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-03-23 17:33:44

I've rebased this patch against 3.4 and added loads of new functionality. Chris Kurth has given permission for his KFarey package to be incorporated into Sage, and I've started by incorporating the permutation machinery, which gives a way of representing and working with arbitrary finite index subgroups of SL2Z.

Here is a sample (taken from the docstring of one of my new files):


```
sage: a2 = SymmetricGroup(7)([(1,2),(3,4),(5,6)]); a3 = SymmetricGroup(7)([(1,3,5),(2,6,7)])
sage: G = ArithmeticSubgroup_Permutation(a2*a3, ~a2 * ~a3); G
Arithmetic subgroup corresponding to permutations L=(1,6)(2,3,4,5,7), R=(1,7,6,3,4)(2,5)
sage: G.index()
7
sage: G.dimension_cusp_forms(4)
1
sage: G.is_congruence()
False
```


I've also moved most of the dimension-formula code out of sage/modular/dims.py into methods of congruence subgroup objects. Given how tangled the original version was, I consider that an improvement. (Let it suffice to say that there were two separate functions in that file which both calculated the index of Gamma0(N) in SL2Z in essentially the same way.) 

Farey symbols, optimal generators, etc can follow in a later patch if people are interested.

(John and Craig: I'm quite keen to get this merged in quickly, as it changes just about every file in sage/modular and so is extremely vulnerable to bitrotting -- any chance either of you could take a look at this?)

David


---

Attachment

replaces previous patch; rebased to 3.4


---

Comment by davidloeffler created at 2009-03-23 18:04:17

Oops, I forgot that Mercurial doesn't automatically pick up the __init__.py file in new directories, so the above patch doesn't quite work. Here's a micro-patch that adds in that file as well.


---

Comment by davidloeffler created at 2009-03-23 18:38:48

For some reason Mercurial seems to be extremely unwilling to accept me adding a new empty file. I've just spent the last 54 minutes trying to get it to accept an __init__.py file correctly. The new micro-patch seems to work.


---

Attachment

micro-patch: apply on top of previous patch


---

Attachment

Apply over previous two patches


---

Comment by davidloeffler created at 2009-03-25 12:11:24

Just realised that this patch has the same problem as my patch for 5159, that unpickling doesn't work: the third patch above fixes this, so now "sage -t sage/structure/sage_object.py" passes.


---

Attachment

needed before 5180-arithgroup.patch, only then the latter applies cleanly to Sage-3.4.1.alpha0


---

Comment by GeorgSWeber created at 2009-03-31 18:01:03

Looks good to me.

I did a complete "MAKE testlong" on a Sage 3.4.1.alpha0 with these patches, and the only doctest failure was the unrelated "number_field_ideal_rel.py" one, which was expected.

Between 3.4 and 3.4.1.alpha0 one file (congroup.py) changed marginally. In order to make these patches apply cleanly, please apply the four-liner "5180-patch0.patch" first, and only then the other (3.4 based) three patches.


---

Comment by mabshoff created at 2009-03-31 20:49:05

This patch causes three doctest failures in 

```
	sage -t  devel/sage/sage/modular/quatalg/brandt.py # 7 doctests failed
	sage -t  devel/sage/doc/en/bordeaux_2008/modular_forms_and_hecke_operators.rst # 2 doctests failed
	sage -t  devel/sage/doc/en/constructions/modular_forms.rst # 4 doctests failed
```

You might want to wait for 3.4.1.rc0 since the failure in sage/modular/quatalg/brandt.py in introduced via the patches at #5520.

Cheers,

Michael


---

Attachment

apply after the other ones and as well after the trac #5520 ones


---

Comment by GeorgSWeber created at 2009-04-01 20:38:46

The doctest fixes were almost trivial, so I did them myself.
Only this last patch of mine remains to be reviewed.

My time before the two weeks Easter vacation runs out, that's why I didn't wait for 3.4.1.rc0. BTW, it seems that "make testlong" does not include running the doctests of the docs? It's reasonable to exclude the "reference doc" from doctesting (or else these doctests would be run through twice), but what about e.g. the "constructions doc"?

Cheers,
gsw


---

Comment by GeorgSWeber created at 2009-04-01 20:48:39

For the record:

I do not count the last patch as worth mentioning in any release notes, especially all credit for the code should go to Dave. (Errors in the additional patch are completely mine, of course!)

Cheers,
gsw


---

Comment by davidloeffler created at 2009-04-03 13:07:39

For what it's worth, I'm completely happy with Georg's latest patch; and I applied patches 0-4 above and all the quaternion patches from #5520 and #5632 on top of 3.4.1.alpha0 and ran "sage -testall" and there were no failures. (Except, that is, the unrelated one in sage/rings/number_field/number_field_ideal_rel that is fixed by #5159.)

Georg's patch doesn't change any actual code other than fixing one line to restore the exact same behaviour it had before I broke it, so I guess there's no need to have a separate review. (Michael: please correct me if I'm wrong -- I've never been very sure about the etiquette of Sage patch reviewing.) So I'm changing this back to "positive review".


---

Attachment

trac_5180-patch5-overconvergent-import-fix.patch is needed to fix the imports for the overconvergent modular forms of genus 0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 01:08:37

Merged

 * trac_5180-patch0.patch
 * trac_5180-patch1-arithgroups.patch
 * trac_5180-patch2.patch
 * trac_5180-patch3-unpickling.patch
 * trac_5180-patch4-extra-doctests.patch
 * trac_5180-patch5-overconvergent-import-fix.patch

in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 01:08:37

Resolution: fixed
