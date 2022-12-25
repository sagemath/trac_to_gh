# Issue 8451: improve galois representation for elliptic curves

archive/issues_008451.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @williamstein @robertwb @rlmill\n\nKeywords: elliptic curves, galois representation, is_surjective\n\nIn #8118, I have moved Galois representation for elliptic curves into a new file and I have modified the output of `is_surjective`. The function does no longer give a reason.\n\nI wish now to reintroduce this as a new function `image_type()` which will give back a string describing the image as a subgroup in GL_2(F_p).\n\nIn the middle of doing this, I noted the severe bug in `is_surjective`. The code does not check for exceptional images A_4, S_4, and A_5 in PGL_2(F_p). Typically currently, sage claims that the mod-5 representation of 324b1 is surjective.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8451\n\n",
    "created_at": "2010-03-05T23:57:00Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "improve galois representation for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8451",
    "user": "https://github.com/categorie"
}
```
Assignee: @JohnCremona

CC:  @williamstein @robertwb @rlmill

Keywords: elliptic curves, galois representation, is_surjective

In #8118, I have moved Galois representation for elliptic curves into a new file and I have modified the output of `is_surjective`. The function does no longer give a reason.

I wish now to reintroduce this as a new function `image_type()` which will give back a string describing the image as a subgroup in GL_2(F_p).

In the middle of doing this, I noted the severe bug in `is_surjective`. The code does not check for exceptional images A_4, S_4, and A_5 in PGL_2(F_p). Typically currently, sage claims that the mod-5 representation of 324b1 is surjective.

Issue created by migration from https://trac.sagemath.org/ticket/8451





---

archive/issue_comments_075898.json:
```json
{
    "body": "I am working on this. If needed I can produce a quick patch that fixes the bug, but I prefer to work a bit more on the issue to finalise it.",
    "created_at": "2010-03-05T23:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75898",
    "user": "https://github.com/categorie"
}
```

I am working on this. If needed I can produce a quick patch that fixes the bug, but I prefer to work a bit more on the issue to finalise it.



---

archive/issue_comments_075899.json:
```json
{
    "body": "exported against 4.3.4.alpha1",
    "created_at": "2010-03-11T18:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75899",
    "user": "https://github.com/categorie"
}
```

exported against 4.3.4.alpha1



---

archive/issue_comments_075900.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T19:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75900",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075901.json:
```json
{
    "body": "Attachment [trac_8451.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451.patch) by @categorie created at 2010-03-11 19:00:13\n\nThe patch should fix the bug and add plenty of trivial functionality to galois representations attached to elliptic curves. It should also give a new function `image_type` that tries to determine the image. Currently this gives back a string rather than a group. Also, it does not determine it completely in some cases, like when there is an isogeny is only says that the image is contained in the Borel, but does not try to determine if it is the full Borel or not. If someone wants this, we can try to add it later.",
    "created_at": "2010-03-11T19:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75901",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8451.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451.patch) by @categorie created at 2010-03-11 19:00:13

The patch should fix the bug and add plenty of trivial functionality to galois representations attached to elliptic curves. It should also give a new function `image_type` that tries to determine the image. Currently this gives back a string rather than a group. Also, it does not determine it completely in some cases, like when there is an isogeny is only says that the image is contained in the Borel, but does not try to determine if it is the full Borel or not. If someone wants this, we can try to add it later.



---

archive/issue_comments_075902.json:
```json
{
    "body": "The patch applies fine to 4.3.4.alpha1 and tests in the elliptic_curves directory pass.\n\nI think that someone with more knowledge of the theory than I have in my head should look at it too -- robertwb?  rlm?\n\nAs there's a lot of documentation added I checked that the reference manual builds fine, but did not look at the output (since I was testing on a remote machine).",
    "created_at": "2010-03-13T18:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75902",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies fine to 4.3.4.alpha1 and tests in the elliptic_curves directory pass.

I think that someone with more knowledge of the theory than I have in my head should look at it too -- robertwb?  rlm?

As there's a lot of documentation added I checked that the reference manual builds fine, but did not look at the output (since I was testing on a remote machine).



---

archive/issue_comments_075903.json:
```json
{
    "body": "It would be good if this could go in at some point... especially because it fixes bugs that may have an impact on BSD verifications.\n\nAny of the CCs willing to review ?",
    "created_at": "2010-04-08T13:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75903",
    "user": "https://github.com/categorie"
}
```

It would be good if this could go in at some point... especially because it fixes bugs that may have an impact on BSD verifications.

Any of the CCs willing to review ?



---

archive/issue_comments_075904.json:
```json
{
    "body": "I ran long tests, and everything passed. A couple questions:\n\nFor reducible primes, not sure whether you need is_prime(p) -- doesn't isogeny_class only list prime degree isogenies?\n\nCan we get rid of the \"irregardless\" in is_surjective? I hate that non-word!\n\nReplace \"Borel\" with \"Borel subgroup\" in image_type\n\n\nI'm not entirely confident enough to give this a positive review on my own, maybe someone else could look it over too?\n\n\nAlso, a question: if I run over all curves where the code in this ticket gives one of \n\nThe image could not be determined, it is likely that the image in PGL_2 is A_4\n\nThe image could not be determined, it is likely that the image in PGL_2 is S_4\n\nor \n\nThe image could not be determined, it is likely that the image in PGL_2 is A_5\n\nAre these the only cases that would be incorrect with the code as it is now?",
    "created_at": "2010-04-11T22:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75904",
    "user": "https://github.com/rlmill"
}
```

I ran long tests, and everything passed. A couple questions:

For reducible primes, not sure whether you need is_prime(p) -- doesn't isogeny_class only list prime degree isogenies?

Can we get rid of the "irregardless" in is_surjective? I hate that non-word!

Replace "Borel" with "Borel subgroup" in image_type


I'm not entirely confident enough to give this a positive review on my own, maybe someone else could look it over too?


Also, a question: if I run over all curves where the code in this ticket gives one of 

The image could not be determined, it is likely that the image in PGL_2 is A_4

The image could not be determined, it is likely that the image in PGL_2 is S_4

or 

The image could not be determined, it is likely that the image in PGL_2 is A_5

Are these the only cases that would be incorrect with the code as it is now?



---

archive/issue_comments_075905.json:
```json
{
    "body": "Thanks a lot for looking at it.\n\n> For reducible primes, not sure whether you need is_prime(p) -- doesn't isogeny_class only list prime degree isogenies?\n\n\nThat may be redudant, but it does not harm.\n\n> Can we get rid of the \"irregardless\" in is_surjective? I hate that non-word!\n\n\nAgree.\n \n> Replace \"Borel\" with \"Borel subgroup\" in image_type\n\n\nAgreed, too.\n\n> I'm not entirely confident enough to give this a positive review on my own, maybe someone else could look it over too?\n\n\nSure, any candidate in mind ?\n\n> Also, a question: if I run over all curves where the code in this ticket gives one of \n> \n> The image could not be determined, it is likely that the image in PGL_2 is A_4\n> \n> The image could not be determined, it is likely that the image in PGL_2 is S_4\n> \n> or \n> \n> The image could not be determined, it is likely that the image in PGL_2 is A_5\n> \n> Are these the only cases that would be incorrect with the code as it is now?\n\n\nYes, I believe so. It is not a frequent error. I was just puzzled why the original implementation missed this. Had I not rewritten it, I guess no one would have ever found out.\n\nI hope I have time to add a little patch for the above issues by tomorrow.\n\nChris.",
    "created_at": "2010-04-12T18:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75905",
    "user": "https://github.com/categorie"
}
```

Thanks a lot for looking at it.

> For reducible primes, not sure whether you need is_prime(p) -- doesn't isogeny_class only list prime degree isogenies?


That may be redudant, but it does not harm.

> Can we get rid of the "irregardless" in is_surjective? I hate that non-word!


Agree.
 
> Replace "Borel" with "Borel subgroup" in image_type


Agreed, too.

> I'm not entirely confident enough to give this a positive review on my own, maybe someone else could look it over too?


Sure, any candidate in mind ?

> Also, a question: if I run over all curves where the code in this ticket gives one of 
> 
> The image could not be determined, it is likely that the image in PGL_2 is A_4
> 
> The image could not be determined, it is likely that the image in PGL_2 is S_4
> 
> or 
> 
> The image could not be determined, it is likely that the image in PGL_2 is A_5
> 
> Are these the only cases that would be incorrect with the code as it is now?


Yes, I believe so. It is not a frequent error. I was just puzzled why the original implementation missed this. Had I not rewritten it, I guess no one would have ever found out.

I hope I have time to add a little patch for the above issues by tomorrow.

Chris.



---

archive/issue_comments_075906.json:
```json
{
    "body": "From Drew Sutherland, who is an expert on this algorithm:\n\n\"Hi William,\n\nI am in Montreal at the moment preparing for a talk, but I would be happy to take a look at it this weekend when I should have some time. One thing that would be helpful is to be able to see the new version of\n\n  sage/schemes/elliptic_curves/gal_reps.py\n\nin its entirety. Currently, I can browse the old version and look at the diff, but it would be easier to just read linearly through the new version.\n\nA very useful test would be to run the new code on some substantial subset of the Cremona database and compare the results to the answer you get from my code. Is this something that can easily be done now that you have integrated my code into Sage?\n\nDrew\n\np.s. I can say that I agree with the comment that the mod 3 rep is surjective if and only if the 3-division poly has Galois group S_4. Another way to see this is to look at the Galois group of the instantiated modular polynomial Phi_3(X,j(E)), which happens to be isomorphic to the Galois group of the 3-division poly (3 is special in this regard) and is also isomorphic to the image of the mod 3 Galois rep in PGL(2,3).\"\n\nMy response, is that yes, I'm sure we can set you up with everything you want above.",
    "created_at": "2010-04-13T03:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75906",
    "user": "https://github.com/williamstein"
}
```

From Drew Sutherland, who is an expert on this algorithm:

"Hi William,

I am in Montreal at the moment preparing for a talk, but I would be happy to take a look at it this weekend when I should have some time. One thing that would be helpful is to be able to see the new version of

  sage/schemes/elliptic_curves/gal_reps.py

in its entirety. Currently, I can browse the old version and look at the diff, but it would be easier to just read linearly through the new version.

A very useful test would be to run the new code on some substantial subset of the Cremona database and compare the results to the answer you get from my code. Is this something that can easily be done now that you have integrated my code into Sage?

Drew

p.s. I can say that I agree with the comment that the mod 3 rep is surjective if and only if the 3-division poly has Galois group S_4. Another way to see this is to look at the Galois group of the instantiated modular polynomial Phi_3(X,j(E)), which happens to be isomorphic to the Galois group of the 3-division poly (3 is special in this regard) and is also isomorphic to the image of the mod 3 Galois rep in PGL(2,3)."

My response, is that yes, I'm sure we can set you up with everything you want above.



---

archive/issue_comments_075907.json:
```json
{
    "body": "Attachment [trac_8451_2.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_2.patch) by @categorie created at 2010-04-13 14:37:50\n\nscond patch to be applied after the first",
    "created_at": "2010-04-13T14:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75907",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8451_2.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_2.patch) by @categorie created at 2010-04-13 14:37:50

scond patch to be applied after the first



---

archive/issue_comments_075908.json:
```json
{
    "body": "I applied this to sage-4.4.alpha0 and get:\n\n```\nsage: rho = EllipticCurve('225a').galois_representation() \n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()\n\n/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in galois_representation(self)\n   4625             return self.__rho\n   4626         except AttributeError:\n-> 4627             from gal_reps import GaloisRepresentation\n   4628             self.__rho = GaloisRepresentation(self)\n   4629         return self.__rho\n\n/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/gal_reps.py in <module>()\n    133 import sage.misc.misc as misc\n    134 import sage.rings.all as rings\n--> 135 from sage.rings.finite_field import GF\n    136 from sage.rings.all import RealField\n    137 from math import sqrt\n\nImportError: No module named finite_field\nsage: \n```\nThat seems to be a conflict, because there is no finite_field module in sage.rings anymore.    There is:\n\n```\ndevel/sage/sage/rings/finite_rings/\n```\n\nSo this patch needs to be rebased for 4.4 to have finite_field changed to finite_rings... or much better -- *only* use sage.rings.all, which is massively better.   I.e., just do:\n\n```\ndiff -r 35160a4d594a sage/schemes/elliptic_curves/gal_reps.py\n--- a/sage/schemes/elliptic_curves/gal_reps.py  Tue Mar 30 15:26:20 2010 -0700\n+++ b/sage/schemes/elliptic_curves/gal_reps.py  Tue Apr 20 15:04:12 2010 -0700\n@@ -132,8 +132,7 @@\n import sage.rings.arith as arith\n import sage.misc.misc as misc\n import sage.rings.all as rings\n-from sage.rings.finite_field import GF\n-from sage.rings.all import RealField\n+from sage.rings.all import RealField, GF\n```\nand then everything seems fine.  This is trac_8541_3.patch.",
    "created_at": "2010-04-20T22:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75908",
    "user": "https://github.com/williamstein"
}
```

I applied this to sage-4.4.alpha0 and get:

```
sage: rho = EllipticCurve('225a').galois_representation() 
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()

/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in galois_representation(self)
   4625             return self.__rho
   4626         except AttributeError:
-> 4627             from gal_reps import GaloisRepresentation
   4628             self.__rho = GaloisRepresentation(self)
   4629         return self.__rho

/mnt/usb1/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/gal_reps.py in <module>()
    133 import sage.misc.misc as misc
    134 import sage.rings.all as rings
--> 135 from sage.rings.finite_field import GF
    136 from sage.rings.all import RealField
    137 from math import sqrt

ImportError: No module named finite_field
sage: 
```
That seems to be a conflict, because there is no finite_field module in sage.rings anymore.    There is:

```
devel/sage/sage/rings/finite_rings/
```

So this patch needs to be rebased for 4.4 to have finite_field changed to finite_rings... or much better -- *only* use sage.rings.all, which is massively better.   I.e., just do:

```
diff -r 35160a4d594a sage/schemes/elliptic_curves/gal_reps.py
--- a/sage/schemes/elliptic_curves/gal_reps.py  Tue Mar 30 15:26:20 2010 -0700
+++ b/sage/schemes/elliptic_curves/gal_reps.py  Tue Apr 20 15:04:12 2010 -0700
@@ -132,8 +132,7 @@
 import sage.rings.arith as arith
 import sage.misc.misc as misc
 import sage.rings.all as rings
-from sage.rings.finite_field import GF
-from sage.rings.all import RealField
+from sage.rings.all import RealField, GF
```
and then everything seems fine.  This is trac_8541_3.patch.



---

archive/issue_comments_075909.json:
```json
{
    "body": "Attachment [trac_8451_3.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_3.patch) by @williamstein created at 2010-04-20 22:05:58",
    "created_at": "2010-04-20T22:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75909",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8451_3.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_3.patch) by @williamstein created at 2010-04-20 22:05:58



---

archive/issue_comments_075910.json:
```json
{
    "body": "```\n[the point of this is to help get this reviewed promptly]\n\nHi Drew,\n\nIf you look in /scratch/drew you'll find a Sage install I created for you:\n\ndrew@sage:/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux$ pwd\n/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux\n\nIt has both #8617, your code, and http://trac.sagemath.org/sage_trac/ticket/8451 which is the patch you're refereeing. \n\nThe file test.out in that directory will soon contain the output of running the full sage testsuite with those patches applied:\n\ndrew@sage:/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux$ ./sage -tp 20 devel/sage/sage/ > test.out&\n[1] 12438\n\n\nHere's using some code:\n\nsage: rho = EllipticCurve('225a').galois_representation() \nsage: rho.reducible_primes()\n[3]\nsage: rho.is_crystalline(3)\nFalse\nsage: rho.is_crystalline(5)\nFalse\n\nand your code:\n\nsage: E = EllipticCurve('225a')\nsage: E.short_weierstrass_model()\nElliptic Curve defined by y^2 = x^3 + 80 over Rational Field\nsage: galrep = sage.libs.galrep.all.GalRep()\nsage: galrep.non_surjective_primes(0,80)\n[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]\n\nAnother example:\n\nsage: E = EllipticCurve('11a')\nsage: E = E.short_weierstrass_model(); E\nElliptic Curve defined by y^2 = x^3 - 13392*x - 1080432 over Rational Field\nsage: galrep.non_surjective_primes(ZZ(E.a4()), ZZ(E.a6()))\n[5]\nsage: rho = E.galois_representation() \nsage: rho.non_surjective()\n[5]\n```",
    "created_at": "2010-04-20T22:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75910",
    "user": "https://github.com/williamstein"
}
```

```
[the point of this is to help get this reviewed promptly]

Hi Drew,

If you look in /scratch/drew you'll find a Sage install I created for you:

drew@sage:/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux$ pwd
/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux

It has both #8617, your code, and http://trac.sagemath.org/sage_trac/ticket/8451 which is the patch you're refereeing. 

The file test.out in that directory will soon contain the output of running the full sage testsuite with those patches applied:

drew@sage:/scratch/drew/sage-4.4.alpha0-sage.math.washington.edu-x86_64-Linux$ ./sage -tp 20 devel/sage/sage/ > test.out&
[1] 12438


Here's using some code:

sage: rho = EllipticCurve('225a').galois_representation() 
sage: rho.reducible_primes()
[3]
sage: rho.is_crystalline(3)
False
sage: rho.is_crystalline(5)
False

and your code:

sage: E = EllipticCurve('225a')
sage: E.short_weierstrass_model()
Elliptic Curve defined by y^2 = x^3 + 80 over Rational Field
sage: galrep = sage.libs.galrep.all.GalRep()
sage: galrep.non_surjective_primes(0,80)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

Another example:

sage: E = EllipticCurve('11a')
sage: E = E.short_weierstrass_model(); E
Elliptic Curve defined by y^2 = x^3 - 13392*x - 1080432 over Rational Field
sage: galrep.non_surjective_primes(ZZ(E.a4()), ZZ(E.a6()))
[5]
sage: rho = E.galois_representation() 
sage: rho.non_surjective()
[5]
```



---

archive/issue_comments_075911.json:
```json
{
    "body": "The following is from Drew:\n\n\"Hi William,\n\nI spent some time this afternoon testing the new Galois representation code using the test version of Sage that you set up.\n\nI tried out several curves with interesting Galois images and was able to find a number of potential issues in the implementation, and one definitive bug. In several cases the image_type function output the message:\n\n  \"The image could not be determined, it is likely that is a bug\"  (*)\n\nI did not have time to try and trace these through the code, but I have listed some examples that will elicit this message below. I suspect that someone familiar with the code can track these down more quickly than I.\n\nThe only primes where I found problems were 5 and 7.\n\nFor 5, below are two different examples that elicited (*):\n\n Curve                    Mod 5 image\n [0,0,1,-25650,1570826]   Index 2 subgroup of normalizer of split Cartan\n [1,-1,1,-5,2]            Normalizer of non-split Cartan\n\nFor the curve [0,0,0,-56,4848] the image_type function reported that it could not determine the image but that it is likely to be contained in the normalizer of a non-split Cartan. This is probably harmless, but I note that the mod 5 image of this curve has order 32 and is the normalizer of a *split* Cartan.\n\nFor 7 the following examples elicited (*)\n\n Curve                    Mod 7 image\n [1,-1,1,-2680,-50053]    Index 4 subgroup of normalizer of split Cartan\n [1,-1,0,-107,-379]       Index 2 subgroup of normalizer of split Cartan\n\nMore seriously, the image_type function mis-identified the mod 7 image of the curve [0,0,1,2580,549326]. It claims that the image is contained in the normalizer of a non-split Cartan, but this is not true, it lies in the normalizer of a split Cartan. As a proof that it is *not* in the normalizer of a non-split Cartan, I note that for p=19, the factorization pattern of Phi_7(X,j(E)) is 1,1,6, which implies that the mod 7 image of Frobenius has an eigenvalue and is of order 6 in PGL(2,F_7). But no element of the normalizer of a non-split Cartan has this property.\n\nAside from checking these particular exceptional cases, I think it would be very worthwhile to do an automated run through some or all of the Cremona or Stein-Watkins tables and comparing the results of Galois_representation and galrep (at least as to surjectivity). I suspect this is more likely to find problems than further manual testing or code review.\n\nRegards,\n\n\nDrew\"",
    "created_at": "2010-04-22T05:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75911",
    "user": "https://github.com/williamstein"
}
```

The following is from Drew:

"Hi William,

I spent some time this afternoon testing the new Galois representation code using the test version of Sage that you set up.

I tried out several curves with interesting Galois images and was able to find a number of potential issues in the implementation, and one definitive bug. In several cases the image_type function output the message:

  "The image could not be determined, it is likely that is a bug"  (*)

I did not have time to try and trace these through the code, but I have listed some examples that will elicit this message below. I suspect that someone familiar with the code can track these down more quickly than I.

The only primes where I found problems were 5 and 7.

For 5, below are two different examples that elicited (*):

 Curve                    Mod 5 image
 [0,0,1,-25650,1570826]   Index 2 subgroup of normalizer of split Cartan
 [1,-1,1,-5,2]            Normalizer of non-split Cartan

For the curve [0,0,0,-56,4848] the image_type function reported that it could not determine the image but that it is likely to be contained in the normalizer of a non-split Cartan. This is probably harmless, but I note that the mod 5 image of this curve has order 32 and is the normalizer of a *split* Cartan.

For 7 the following examples elicited (*)

 Curve                    Mod 7 image
 [1,-1,1,-2680,-50053]    Index 4 subgroup of normalizer of split Cartan
 [1,-1,0,-107,-379]       Index 2 subgroup of normalizer of split Cartan

More seriously, the image_type function mis-identified the mod 7 image of the curve [0,0,1,2580,549326]. It claims that the image is contained in the normalizer of a non-split Cartan, but this is not true, it lies in the normalizer of a split Cartan. As a proof that it is *not* in the normalizer of a non-split Cartan, I note that for p=19, the factorization pattern of Phi_7(X,j(E)) is 1,1,6, which implies that the mod 7 image of Frobenius has an eigenvalue and is of order 6 in PGL(2,F_7). But no element of the normalizer of a non-split Cartan has this property.

Aside from checking these particular exceptional cases, I think it would be very worthwhile to do an automated run through some or all of the Cremona or Stein-Watkins tables and comparing the results of Galois_representation and galrep (at least as to surjectivity). I suspect this is more likely to find problems than further manual testing or code review.

Regards,


Drew"



---

archive/issue_comments_075912.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-22T05:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75912",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075913.json:
```json
{
    "body": "Many thanks for the detailed review of the patch and the bugs found. I am glad someone with a lot of knowledge has had a look at this.\n\nI juts came back from holidays and I have many other things to do, but I will soon pick it up again.",
    "created_at": "2010-04-23T13:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75913",
    "user": "https://github.com/categorie"
}
```

Many thanks for the detailed review of the patch and the bugs found. I am glad someone with a lot of knowledge has had a look at this.

I juts came back from holidays and I have many other things to do, but I will soon pick it up again.



---

archive/issue_comments_075914.json:
```json
{
    "body": "Attachment [trac_8451_new.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_new.patch) by @categorie created at 2010-09-02 19:36:03\n\nexported against 4.5.2; replaces all previous patches",
    "created_at": "2010-09-02T19:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75914",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8451_new.patch](tarball://root/attachments/some-uuid/ticket8451/trac_8451_new.patch) by @categorie created at 2010-09-02 19:36:03

exported against 4.5.2; replaces all previous patches



---

archive/issue_comments_075915.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-02T19:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75915",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075916.json:
```json
{
    "body": "Six months later I took the time to revise this patch completely. I have rewritten the function image_type. It now never gives a probabilistic answer, but only proven results. The package by Andrew Sutherland #8617 will add a much better probabilistic algorithm anyway.\n\nOne couls go on and implement things better so that a actually group is returned, but I do not want to waste more time on this.\n\nThe above counter-examples now work. (I had programmed it quite badly). See the doctest. Also I added more documentation in the source code.\n\nThere might still be bugs in it. It would be best though to put it in as such and then once #8451 is in and has a good interface, we could run test against it. That would be the best test.\nBy now it already improves a lot (and removes some bugs in is_surjective that have implications to bsd stuff.",
    "created_at": "2010-09-02T19:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75916",
    "user": "https://github.com/categorie"
}
```

Six months later I took the time to revise this patch completely. I have rewritten the function image_type. It now never gives a probabilistic answer, but only proven results. The package by Andrew Sutherland #8617 will add a much better probabilistic algorithm anyway.

One couls go on and implement things better so that a actually group is returned, but I do not want to waste more time on this.

The above counter-examples now work. (I had programmed it quite badly). See the doctest. Also I added more documentation in the source code.

There might still be bugs in it. It would be best though to put it in as such and then once #8451 is in and has a good interface, we could run test against it. That would be the best test.
By now it already improves a lot (and removes some bugs in is_surjective that have implications to bsd stuff.



---

archive/issue_comments_075917.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-10T14:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75917",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075918.json:
```json
{
    "body": "This looks good to me.\n\nIt applies cleanly to sage-4.6, and it passes all doctests.\n\nSince this fixes bugs in is_surjective, I recommend that we merge it ASAP. These bugs have been around for a long time!\n\nSide note, I would be interested to implement a function which says whether the image were as surjective as possible for CM curves, and I've done some computations about this in specific cases, but I'm not sure I would be able to implement a general routine without a lot of thinking...",
    "created_at": "2010-11-10T14:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75918",
    "user": "https://github.com/rlmill"
}
```

This looks good to me.

It applies cleanly to sage-4.6, and it passes all doctests.

Since this fixes bugs in is_surjective, I recommend that we merge it ASAP. These bugs have been around for a long time!

Side note, I would be interested to implement a function which says whether the image were as surjective as possible for CM curves, and I've done some computations about this in specific cases, but I'm not sure I would be able to implement a general routine without a lot of thinking...



---

archive/issue_comments_075919.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-15T23:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8451#issuecomment-75919",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_020282.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-15T23:36:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8451",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8451#event-20282"
}
```
