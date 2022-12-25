# Issue 5180: [with new patch, positive review] Improvements to congruence subgroups

archive/issues_005180.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @craigcitro georgsweber\n\nKeywords: congruence subgroups\n\nThe attached patch splits up the code for congruence subgroups into several files in a directory sage/modular/congroups. The old file sage/modular/congroup.py still exists, so pickles created with previous versions should unpickle safely under the new one.\n\nI've added a little functionality in the process: congruence subgroups can now calculate the width and regularity of their cusps, and their number of elliptic points.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5180\n\n",
    "closed_at": "2009-04-05T01:08:37Z",
    "created_at": "2009-02-04T18:35:29Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with new patch, positive review] Improvements to congruence subgroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5180",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

CC:  @craigcitro georgsweber

Keywords: congruence subgroups

The attached patch splits up the code for congruence subgroups into several files in a directory sage/modular/congroups. The old file sage/modular/congroup.py still exists, so pickles created with previous versions should unpickle safely under the new one.

I've added a little functionality in the process: congruence subgroups can now calculate the width and regularity of their cusps, and their number of elliptic points.

Issue created by migration from https://trac.sagemath.org/ticket/5180





---

archive/issue_comments_039640.json:
```json
{
    "body": "Oops, just realised that is the wrong patch -- wait a moment",
    "created_at": "2009-02-04T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39640",
    "user": "https://github.com/loefflerd"
}
```

Oops, just realised that is the wrong patch -- wait a moment



---

archive/issue_comments_039641.json:
```json
{
    "body": "Changing assignee from @craigcitro to @loefflerd.",
    "created_at": "2009-02-04T18:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39641",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @craigcitro to @loefflerd.



---

archive/issue_comments_039642.json:
```json
{
    "body": "patch against 3.3.alpha3",
    "created_at": "2009-02-04T19:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39642",
    "user": "https://github.com/loefflerd"
}
```

patch against 3.3.alpha3



---

archive/issue_comments_039643.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-04T19:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39643",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039644.json:
```json
{
    "body": "Attachment [congroups.patch](tarball://root/attachments/some-uuid/ticket5180/congroups.patch) by @loefflerd created at 2009-02-04 19:10:27\n\nOK, that's the right patch (replacing the old one).",
    "created_at": "2009-02-04T19:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39644",
    "user": "https://github.com/loefflerd"
}
```

Attachment [congroups.patch](tarball://root/attachments/some-uuid/ticket5180/congroups.patch) by @loefflerd created at 2009-02-04 19:10:27

OK, that's the right patch (replacing the old one).



---

archive/issue_comments_039645.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39645",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_events_011992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T23:02:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5180#event-11992"
}
```



---

archive/issue_comments_039646.json:
```json
{
    "body": "I've rebased this patch against 3.4 and added loads of new functionality. Chris Kurth has given permission for his KFarey package to be incorporated into Sage, and I've started by incorporating the permutation machinery, which gives a way of representing and working with arbitrary finite index subgroups of SL2Z.\n\nHere is a sample (taken from the docstring of one of my new files):\n\n```\nsage: a2 = SymmetricGroup(7)([(1,2),(3,4),(5,6)]); a3 = SymmetricGroup(7)([(1,3,5),(2,6,7)])\nsage: G = ArithmeticSubgroup_Permutation(a2*a3, ~a2 * ~a3); G\nArithmetic subgroup corresponding to permutations L=(1,6)(2,3,4,5,7), R=(1,7,6,3,4)(2,5)\nsage: G.index()\n7\nsage: G.dimension_cusp_forms(4)\n1\nsage: G.is_congruence()\nFalse\n```\n\nI've also moved most of the dimension-formula code out of sage/modular/dims.py into methods of congruence subgroup objects. Given how tangled the original version was, I consider that an improvement. (Let it suffice to say that there were two separate functions in that file which both calculated the index of Gamma0(N) in SL2Z in essentially the same way.) \n\nFarey symbols, optimal generators, etc can follow in a later patch if people are interested.\n\n(John and Craig: I'm quite keen to get this merged in quickly, as it changes just about every file in sage/modular and so is extremely vulnerable to bitrotting -- any chance either of you could take a look at this?)\n\nDavid",
    "created_at": "2009-03-23T17:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39646",
    "user": "https://github.com/loefflerd"
}
```

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

archive/issue_comments_039647.json:
```json
{
    "body": "Attachment [5180-arithgroups.patch](tarball://root/attachments/some-uuid/ticket5180/5180-arithgroups.patch) by @loefflerd created at 2009-03-23 17:34:46\n\nreplaces previous patch; rebased to 3.4",
    "created_at": "2009-03-23T17:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39647",
    "user": "https://github.com/loefflerd"
}
```

Attachment [5180-arithgroups.patch](tarball://root/attachments/some-uuid/ticket5180/5180-arithgroups.patch) by @loefflerd created at 2009-03-23 17:34:46

replaces previous patch; rebased to 3.4



---

archive/issue_comments_039648.json:
```json
{
    "body": "Oops, I forgot that Mercurial doesn't automatically pick up the __init__.py file in new directories, so the above patch doesn't quite work. Here's a micro-patch that adds in that file as well.",
    "created_at": "2009-03-23T18:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39648",
    "user": "https://github.com/loefflerd"
}
```

Oops, I forgot that Mercurial doesn't automatically pick up the __init__.py file in new directories, so the above patch doesn't quite work. Here's a micro-patch that adds in that file as well.



---

archive/issue_comments_039649.json:
```json
{
    "body": "For some reason Mercurial seems to be extremely unwilling to accept me adding a new empty file. I've just spent the last 54 minutes trying to get it to accept an __init__.py file correctly. The new micro-patch seems to work.",
    "created_at": "2009-03-23T18:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39649",
    "user": "https://github.com/loefflerd"
}
```

For some reason Mercurial seems to be extremely unwilling to accept me adding a new empty file. I've just spent the last 54 minutes trying to get it to accept an __init__.py file correctly. The new micro-patch seems to work.



---

archive/issue_comments_039650.json:
```json
{
    "body": "Attachment [5180-patch2.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch2.patch) by @loefflerd created at 2009-03-23 18:39:24\n\nmicro-patch: apply on top of previous patch",
    "created_at": "2009-03-23T18:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39650",
    "user": "https://github.com/loefflerd"
}
```

Attachment [5180-patch2.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch2.patch) by @loefflerd created at 2009-03-23 18:39:24

micro-patch: apply on top of previous patch



---

archive/issue_comments_039651.json:
```json
{
    "body": "Attachment [5180-patch3-unpickling.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch3-unpickling.patch) by @loefflerd created at 2009-03-25 12:09:34\n\nApply over previous two patches",
    "created_at": "2009-03-25T12:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39651",
    "user": "https://github.com/loefflerd"
}
```

Attachment [5180-patch3-unpickling.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch3-unpickling.patch) by @loefflerd created at 2009-03-25 12:09:34

Apply over previous two patches



---

archive/issue_comments_039652.json:
```json
{
    "body": "Just realised that this patch has the same problem as my patch for 5159, that unpickling doesn't work: the third patch above fixes this, so now \"sage -t sage/structure/sage_object.py\" passes.",
    "created_at": "2009-03-25T12:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39652",
    "user": "https://github.com/loefflerd"
}
```

Just realised that this patch has the same problem as my patch for 5159, that unpickling doesn't work: the third patch above fixes this, so now "sage -t sage/structure/sage_object.py" passes.



---

archive/issue_comments_039653.json:
```json
{
    "body": "Attachment [5180-patch0.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch0.patch) by GeorgSWeber created at 2009-03-31 17:53:07\n\nneeded before 5180-arithgroup.patch, only then the latter applies cleanly to Sage-3.4.1.alpha0",
    "created_at": "2009-03-31T17:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39653",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [5180-patch0.patch](tarball://root/attachments/some-uuid/ticket5180/5180-patch0.patch) by GeorgSWeber created at 2009-03-31 17:53:07

needed before 5180-arithgroup.patch, only then the latter applies cleanly to Sage-3.4.1.alpha0



---

archive/issue_comments_039654.json:
```json
{
    "body": "Looks good to me.\n\nI did a complete \"MAKE testlong\" on a Sage 3.4.1.alpha0 with these patches, and the only doctest failure was the unrelated \"number_field_ideal_rel.py\" one, which was expected.\n\nBetween 3.4 and 3.4.1.alpha0 one file (congroup.py) changed marginally. In order to make these patches apply cleanly, please apply the four-liner \"5180-patch0.patch\" first, and only then the other (3.4 based) three patches.",
    "created_at": "2009-03-31T18:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39654",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Looks good to me.

I did a complete "MAKE testlong" on a Sage 3.4.1.alpha0 with these patches, and the only doctest failure was the unrelated "number_field_ideal_rel.py" one, which was expected.

Between 3.4 and 3.4.1.alpha0 one file (congroup.py) changed marginally. In order to make these patches apply cleanly, please apply the four-liner "5180-patch0.patch" first, and only then the other (3.4 based) three patches.



---

archive/issue_events_011993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:01:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5180#event-11993"
}
```



---

archive/issue_events_011994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber",
    "created_at": "2009-03-31T18:01:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5180#event-11994"
}
```



---

archive/issue_comments_039655.json:
```json
{
    "body": "This patch causes three doctest failures in \n\n```\n\tsage -t  devel/sage/sage/modular/quatalg/brandt.py # 7 doctests failed\n\tsage -t  devel/sage/doc/en/bordeaux_2008/modular_forms_and_hecke_operators.rst # 2 doctests failed\n\tsage -t  devel/sage/doc/en/constructions/modular_forms.rst # 4 doctests failed\n```\nYou might want to wait for 3.4.1.rc0 since the failure in sage/modular/quatalg/brandt.py in introduced via the patches at #5520.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T20:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_039656.json:
```json
{
    "body": "Attachment [trac_5180-patch4-extra-doctests.patch](tarball://root/attachments/some-uuid/ticket5180/trac_5180-patch4-extra-doctests.patch) by GeorgSWeber created at 2009-04-01 20:31:28\n\napply after the other ones and as well after the trac #5520 ones",
    "created_at": "2009-04-01T20:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39656",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac_5180-patch4-extra-doctests.patch](tarball://root/attachments/some-uuid/ticket5180/trac_5180-patch4-extra-doctests.patch) by GeorgSWeber created at 2009-04-01 20:31:28

apply after the other ones and as well after the trac #5520 ones



---

archive/issue_comments_039657.json:
```json
{
    "body": "The doctest fixes were almost trivial, so I did them myself.\nOnly this last patch of mine remains to be reviewed.\n\nMy time before the two weeks Easter vacation runs out, that's why I didn't wait for 3.4.1.rc0. BTW, it seems that \"make testlong\" does not include running the doctests of the docs? It's reasonable to exclude the \"reference doc\" from doctesting (or else these doctests would be run through twice), but what about e.g. the \"constructions doc\"?\n\nCheers,\ngsw",
    "created_at": "2009-04-01T20:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39657",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The doctest fixes were almost trivial, so I did them myself.
Only this last patch of mine remains to be reviewed.

My time before the two weeks Easter vacation runs out, that's why I didn't wait for 3.4.1.rc0. BTW, it seems that "make testlong" does not include running the doctests of the docs? It's reasonable to exclude the "reference doc" from doctesting (or else these doctests would be run through twice), but what about e.g. the "constructions doc"?

Cheers,
gsw



---

archive/issue_comments_039658.json:
```json
{
    "body": "For the record:\n\nI do not count the last patch as worth mentioning in any release notes, especially all credit for the code should go to Dave. (Errors in the additional patch are completely mine, of course!)\n\nCheers,\ngsw",
    "created_at": "2009-04-01T20:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39658",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

For the record:

I do not count the last patch as worth mentioning in any release notes, especially all credit for the code should go to Dave. (Errors in the additional patch are completely mine, of course!)

Cheers,
gsw



---

archive/issue_comments_039659.json:
```json
{
    "body": "For what it's worth, I'm completely happy with Georg's latest patch; and I applied patches 0-4 above and all the quaternion patches from #5520 and #5632 on top of 3.4.1.alpha0 and ran \"sage -testall\" and there were no failures. (Except, that is, the unrelated one in sage/rings/number_field/number_field_ideal_rel that is fixed by #5159.)\n\nGeorg's patch doesn't change any actual code other than fixing one line to restore the exact same behaviour it had before I broke it, so I guess there's no need to have a separate review. (Michael: please correct me if I'm wrong -- I've never been very sure about the etiquette of Sage patch reviewing.) So I'm changing this back to \"positive review\".",
    "created_at": "2009-04-03T13:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39659",
    "user": "https://github.com/loefflerd"
}
```

For what it's worth, I'm completely happy with Georg's latest patch; and I applied patches 0-4 above and all the quaternion patches from #5520 and #5632 on top of 3.4.1.alpha0 and ran "sage -testall" and there were no failures. (Except, that is, the unrelated one in sage/rings/number_field/number_field_ideal_rel that is fixed by #5159.)

Georg's patch doesn't change any actual code other than fixing one line to restore the exact same behaviour it had before I broke it, so I guess there's no need to have a separate review. (Michael: please correct me if I'm wrong -- I've never been very sure about the etiquette of Sage patch reviewing.) So I'm changing this back to "positive review".



---

archive/issue_comments_039660.json:
```json
{
    "body": "Attachment [trac_5180-patch5-overconvergent-import-fix.patch](tarball://root/attachments/some-uuid/ticket5180/trac_5180-patch5-overconvergent-import-fix.patch) by mabshoff created at 2009-04-05 01:08:12\n\ntrac_5180-patch5-overconvergent-import-fix.patch is needed to fix the imports for the overconvergent modular forms of genus 0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T01:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5180-patch5-overconvergent-import-fix.patch](tarball://root/attachments/some-uuid/ticket5180/trac_5180-patch5-overconvergent-import-fix.patch) by mabshoff created at 2009-04-05 01:08:12

trac_5180-patch5-overconvergent-import-fix.patch is needed to fix the imports for the overconvergent modular forms of genus 0.

Cheers,

Michael



---

archive/issue_comments_039661.json:
```json
{
    "body": "Merged\n\n* trac_5180-patch0.patch\n* trac_5180-patch1-arithgroups.patch\n* trac_5180-patch2.patch\n* trac_5180-patch3-unpickling.patch\n* trac_5180-patch4-extra-doctests.patch\n* trac_5180-patch5-overconvergent-import-fix.patch\n\nin Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T01:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_039662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-05T01:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5180#issuecomment-39662",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-05T01:08:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5180",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5180#event-11995"
}
```
