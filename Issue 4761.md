# Issue 4761: [iwth patch, needs review] global cputime (inclusive some subprocesses like Singular)

archive/issues_004761.json:
```json
{
    "body": "Assignee: @malb\n\nI always found this annoying:\n\n\n```\nsage: t = cputime()\nsage: P = PolynomialRing(QQ,8,'x')\nsage: I = sage.rings.ideal.Katsura(P)\nsage: I.groebner_basis()\nsage: print cputime(t)\n0.217967\n```\n\n\nso here's my proposal for a fix:\n\n\n```\nsage: t = cputime_gobal()\nsage: P = PolynomialRing(QQ,8,'x')\nsage: I = sage.rings.ideal.Katsura(P)\nsage: I.groebner_basis()\nsage: print cputime_global(t)\n5.647973\n```\n\n\nI am not sure if the design is particularly nice though.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4761\n\n",
    "created_at": "2008-12-11T15:34:42Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[iwth patch, needs review] global cputime (inclusive some subprocesses like Singular)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4761",
    "user": "@malb"
}
```
Assignee: @malb

I always found this annoying:


```
sage: t = cputime()
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
sage: print cputime(t)
0.217967
```


so here's my proposal for a fix:


```
sage: t = cputime_gobal()
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
sage: print cputime_global(t)
5.647973
```


I am not sure if the design is particularly nice though.

Issue created by migration from https://trac.sagemath.org/ticket/4761





---

archive/issue_comments_036081.json:
```json
{
    "body": "This needs to be rewritten since it makes the faulty assumption that there is at most one interface to singular/magma, etc., at a given moment, and also ignores many of the interfaces needlessly (?).  To emphasize the first point, if I do:\n\n```\nsage: s = Singular()\nsage: t = Singular()\nsage: s('2+2')\n4\nsage: t('2+2')\n4\n```\n\nthen none of the computations above will be seen by cputime_global(). \n\nRegarding the second point, here is a one liner that allows you to get a list of *all* interface objects:\n\n```\nsage: print [s() for s in sage.interfaces.quit.expect_objects if s()]\n[Mathematica, Singular, Axiom, Gap, Genus2reduction, GP/PARI interpreter, Kash, Lisp Interpreter, Magma, Macaulay2, Maple, Maxima, Matlab, Mupad, Mwrank, Octave, Sage, LiE Interpreter, R Interpreter, Maxima, Maxima, R Interpreter]\n```\n\n\nIf you start more, they get *registered* in the sage.interfaces.quit.expect_objects list. \n\nFor example, this illustrates getting all currently running interface objects:\n\n```\nsage: gp('2+2')\n4\nsage: s = Singular()\nsage: s('2+3')\n5\nsage: magma('5')\n5\nsage: [s() for s in sage.interfaces.quit.expect_objects if s() and s().is_running()]\n[GP/PARI interpreter, Magma, Singular]\n```\n\n\nYou could do this before and after the computation, and for newly started interface objects, the cputime for that one would be the total cputime (i.e., it defaults to 0). \nYou could also just get all interface objects, even ones that aren't yet running, but that is NOT as useful, imho, since calling cputime() on them starts them up (which is terrible)...\n\nAnyway, hopefully the above has enough \"interface fu\" that you can easily write the ultimate version of cputime.  And maybe it should just replace cputime?  I.e., \n\n\n```\nsage: cputime()   # what you write\nsage: cputime(subprocesses=False)  # the original cputime?\n```\n\n\nIt probably depends on how much overhead there is...   I could easily imagine rewriting the cputime methods for each interface so that they are nearly instant *unless* the interface has actually done something -- i.e., put a cached value in the cputime() method for each interface that is cleared precisely when you send code to be evaluated.",
    "created_at": "2008-12-11T23:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36081",
    "user": "@williamstein"
}
```

This needs to be rewritten since it makes the faulty assumption that there is at most one interface to singular/magma, etc., at a given moment, and also ignores many of the interfaces needlessly (?).  To emphasize the first point, if I do:

```
sage: s = Singular()
sage: t = Singular()
sage: s('2+2')
4
sage: t('2+2')
4
```

then none of the computations above will be seen by cputime_global(). 

Regarding the second point, here is a one liner that allows you to get a list of *all* interface objects:

```
sage: print [s() for s in sage.interfaces.quit.expect_objects if s()]
[Mathematica, Singular, Axiom, Gap, Genus2reduction, GP/PARI interpreter, Kash, Lisp Interpreter, Magma, Macaulay2, Maple, Maxima, Matlab, Mupad, Mwrank, Octave, Sage, LiE Interpreter, R Interpreter, Maxima, Maxima, R Interpreter]
```


If you start more, they get *registered* in the sage.interfaces.quit.expect_objects list. 

For example, this illustrates getting all currently running interface objects:

```
sage: gp('2+2')
4
sage: s = Singular()
sage: s('2+3')
5
sage: magma('5')
5
sage: [s() for s in sage.interfaces.quit.expect_objects if s() and s().is_running()]
[GP/PARI interpreter, Magma, Singular]
```


You could do this before and after the computation, and for newly started interface objects, the cputime for that one would be the total cputime (i.e., it defaults to 0). 
You could also just get all interface objects, even ones that aren't yet running, but that is NOT as useful, imho, since calling cputime() on them starts them up (which is terrible)...

Anyway, hopefully the above has enough "interface fu" that you can easily write the ultimate version of cputime.  And maybe it should just replace cputime?  I.e., 


```
sage: cputime()   # what you write
sage: cputime(subprocesses=False)  # the original cputime?
```


It probably depends on how much overhead there is...   I could easily imagine rewriting the cputime methods for each interface so that they are nearly instant *unless* the interface has actually done something -- i.e., put a cached value in the cputime() method for each interface that is cleared precisely when you send code to be evaluated.



---

archive/issue_comments_036082.json:
```json
{
    "body": "Cool. I admit I should have searched a bit longer if there is a list of running interfaces already. Most `cputime()` implementations throw `NotImplementedError` but I assume we can just ignore those cpu times or fix that.",
    "created_at": "2008-12-12T00:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36082",
    "user": "@malb"
}
```

Cool. I admit I should have searched a bit longer if there is a list of running interfaces already. Most `cputime()` implementations throw `NotImplementedError` but I assume we can just ignore those cpu times or fix that.



---

archive/issue_comments_036083.json:
```json
{
    "body": "I updated the patch based on was' comments. Also, the new patch doesn't introduce a new function to the global namespace.",
    "created_at": "2008-12-12T16:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36083",
    "user": "@malb"
}
```

I updated the patch based on was' comments. Also, the new patch doesn't introduce a new function to the global namespace.



---

archive/issue_comments_036084.json:
```json
{
    "body": "REFEREE REPORT:\n* typo -- \"be started an terminated at any given time.\": The \"an\" should be \"and\". \n\n* typo -- \"somehwat random\": should be \"somewhat random\". \n\n* Design issues.  I think if t is output from cputime(subprocesses=True), then cputime(t) should automatically have subprocesses=True, since with it False, isn't it just giving nonsense?  Or is it really giving the Sage part?  If the later, ignore this comment, but please document this in the function.  (Yes, it's the latter.)\n\n* Maybe a sentence that explained that so far at least all we're timing is the pexpect interface subprocesses that have a working cputime method.  That any other subprocess (e.g., gfan) isn't timed.   Then people know exactly what they would have to do to make sure there expect interface gets included.\n\n* The __float__ method for GlobalCputime doesn't have the examples in an EXAMPLES block and they aren't indented properly.",
    "created_at": "2008-12-12T17:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36084",
    "user": "@williamstein"
}
```

REFEREE REPORT:
* typo -- "be started an terminated at any given time.": The "an" should be "and". 

* typo -- "somehwat random": should be "somewhat random". 

* Design issues.  I think if t is output from cputime(subprocesses=True), then cputime(t) should automatically have subprocesses=True, since with it False, isn't it just giving nonsense?  Or is it really giving the Sage part?  If the later, ignore this comment, but please document this in the function.  (Yes, it's the latter.)

* Maybe a sentence that explained that so far at least all we're timing is the pexpect interface subprocesses that have a working cputime method.  That any other subprocess (e.g., gfan) isn't timed.   Then people know exactly what they would have to do to make sure there expect interface gets included.

* The __float__ method for GlobalCputime doesn't have the examples in an EXAMPLES block and they aren't indented properly.



---

archive/issue_comments_036085.json:
```json
{
    "body": "First of all, the patch applies cleanly.\n\nI tested the example from the documentation, and I tested an example involving singular and gap. \n\nWhat I find really amazing: Assume that you did\n\n```\nsage: t=cputime(subprocesses=True)\nsage: s=cputime(subprocesses=False)\n```\n\nand later you do\n\n```\nsage: cputime(t)\nsage: cputime(s)\n```\n\n\nI expected that `cputime(t)` would assume `subprocesses=False`, since its previous usage (in the definition of s) had this option. But `cputime(t)` indeed recognizes that t was defined with `subprocesses=True`. This is a very nice feature.\n\nHowever, something seems to be wrong.\nI did the following:\n\n```\nsage: t=cputime(subprocesses=True)\nsage: s=cputime(subprocesses=False)\nsage: {... some lengthy computation...}\nsage: cputime(t)\n1.440028\nsage: cputime(s)\n0.45202800000000032\nsage: cputime(s,subprocesses=True)\n1.972029\nsage: cputime()\n2.2761420000000001\nsage: cputime(subprocesses=False)\n2.2801420000000001\nsage: cputime(subprocesses=True)\n3.800142\nsage: quit\nExiting SAGE (CPU time 0m0.65s, Wall time 11m49.60s).\nExiting spawned Singular process.\nExiting spawned Gap process.\n```\n\n\nHence, when leaving Sage, it is stated that the CPU time spent is 0.65s, whereas `cputime(subprocesses=False)` claims that it is more than 2 seconds. Therefore, I can not give a positive review yet.",
    "created_at": "2009-01-24T17:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36085",
    "user": "@simon-king-jena"
}
```

First of all, the patch applies cleanly.

I tested the example from the documentation, and I tested an example involving singular and gap. 

What I find really amazing: Assume that you did

```
sage: t=cputime(subprocesses=True)
sage: s=cputime(subprocesses=False)
```

and later you do

```
sage: cputime(t)
sage: cputime(s)
```


I expected that `cputime(t)` would assume `subprocesses=False`, since its previous usage (in the definition of s) had this option. But `cputime(t)` indeed recognizes that t was defined with `subprocesses=True`. This is a very nice feature.

However, something seems to be wrong.
I did the following:

```
sage: t=cputime(subprocesses=True)
sage: s=cputime(subprocesses=False)
sage: {... some lengthy computation...}
sage: cputime(t)
1.440028
sage: cputime(s)
0.45202800000000032
sage: cputime(s,subprocesses=True)
1.972029
sage: cputime()
2.2761420000000001
sage: cputime(subprocesses=False)
2.2801420000000001
sage: cputime(subprocesses=True)
3.800142
sage: quit
Exiting SAGE (CPU time 0m0.65s, Wall time 11m49.60s).
Exiting spawned Singular process.
Exiting spawned Gap process.
```


Hence, when leaving Sage, it is stated that the CPU time spent is 0.65s, whereas `cputime(subprocesses=False)` claims that it is more than 2 seconds. Therefore, I can not give a positive review yet.



---

archive/issue_comments_036086.json:
```json
{
    "body": "Changing keywords from \"\" to \"global cputime subprocesses\".",
    "created_at": "2009-01-24T17:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36086",
    "user": "@simon-king-jena"
}
```

Changing keywords from "" to "global cputime subprocesses".



---

archive/issue_comments_036087.json:
```json
{
    "body": "The behaviour described above is \"normal\" insofar as it is not caused by the patch, compare with the current implementation:\n\n\n```\nsage: cputime()\n0.73999999999999999\nsage: exit\nExiting SAGE (CPU time 0m0.05s, Wall time 0m5.60s).\n```\n\n\nThis should be due to the fact that `cputime()` uses user + sys time while the stuff at exit only uses the CPU time.",
    "created_at": "2009-05-12T02:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36087",
    "user": "@malb"
}
```

The behaviour described above is "normal" insofar as it is not caused by the patch, compare with the current implementation:


```
sage: cputime()
0.73999999999999999
sage: exit
Exiting SAGE (CPU time 0m0.05s, Wall time 0m5.60s).
```


This should be due to the fact that `cputime()` uses user + sys time while the stuff at exit only uses the CPU time.



---

archive/issue_comments_036088.json:
```json
{
    "body": "Correction: the stuff at exit simply doesn't count the initialisation. Is that a positive review then?",
    "created_at": "2009-05-12T02:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36088",
    "user": "@malb"
}
```

Correction: the stuff at exit simply doesn't count the initialisation. Is that a positive review then?



---

archive/issue_comments_036089.json:
```json
{
    "body": "Just a quick note: The docstring formatting should now follow the ReST format.",
    "created_at": "2009-06-08T03:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36089",
    "user": "mvngu"
}
```

Just a quick note: The docstring formatting should now follow the ReST format.



---

archive/issue_comments_036090.json:
```json
{
    "body": "Attachment [cputime_global.patch](tarball://root/attachments/some-uuid/ticket4761/cputime_global.patch) by @malb created at 2009-06-08 10:49:14",
    "created_at": "2009-06-08T10:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36090",
    "user": "@malb"
}
```

Attachment [cputime_global.patch](tarball://root/attachments/some-uuid/ticket4761/cputime_global.patch) by @malb created at 2009-06-08 10:49:14



---

archive/issue_comments_036091.json:
```json
{
    "body": "Thanks Minh, I've updated the patch. Can someone comment on the open issue raised above, i.e. that I don't agree with Simon's `needs work`?",
    "created_at": "2009-06-08T10:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36091",
    "user": "@malb"
}
```

Thanks Minh, I've updated the patch. Can someone comment on the open issue raised above, i.e. that I don't agree with Simon's `needs work`?



---

archive/issue_comments_036092.json:
```json
{
    "body": "I think the existing behaviour is fine.  The patch looks good and seems to work for me.  Positive review.",
    "created_at": "2009-06-19T23:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36092",
    "user": "@ncalexan"
}
```

I think the existing behaviour is fine.  The patch looks good and seems to work for me.  Positive review.



---

archive/issue_comments_036093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4761#issuecomment-36093",
    "user": "@rlmill"
}
```

Resolution: fixed
