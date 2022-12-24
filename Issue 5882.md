# Issue 5882: implement general package for finitely generated not-necessarily free R-modules

archive/issues_005882.json:
```json
{
    "body": "Assignee: was\n\nCC:  jhpalmieri davidloeffler bantieau\n\nI *really* need this for my research.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5882\n\n",
    "created_at": "2009-04-24T00:20:20Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "implement general package for finitely generated not-necessarily free R-modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5882",
    "user": "was"
}
```
Assignee: was

CC:  jhpalmieri davidloeffler bantieau

I *really* need this for my research.

Issue created by migration from https://trac.sagemath.org/ticket/5882





---

archive/issue_comments_046476.json:
```json
{
    "body": "NOTE: trac_5882-part2.patch (which I'll post soon) fixes numerous *major* bugs in matrix_morphism.py, e.g., in restrict_domain and restrict_codomain.  I noticed these issues while reading the code and thinking about what it did...",
    "created_at": "2009-05-01T01:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46476",
    "user": "was"
}
```

NOTE: trac_5882-part2.patch (which I'll post soon) fixes numerous *major* bugs in matrix_morphism.py, e.g., in restrict_domain and restrict_codomain.  I noticed these issues while reading the code and thinking about what it did...



---

archive/issue_comments_046477.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-05-02T08:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46477",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_046478.json:
```json
{
    "body": "This is likely ready for review, but I want to do some additional testing before labeling it as such.",
    "created_at": "2009-05-02T09:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46478",
    "user": "was"
}
```

This is likely ready for review, but I want to do some additional testing before labeling it as such.



---

archive/issue_comments_046479.json:
```json
{
    "body": "I've changed this back to \"not ready for review\", since I think it's more likely to be higher quality code if I implement something nontrivial on top of it first, and fix any issues I find.  So I'm doing #5969 first.   Once that's done and I fixed all issues that crop up, then #5882 will be ready for review.",
    "created_at": "2009-05-03T06:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46479",
    "user": "was"
}
```

I've changed this back to "not ready for review", since I think it's more likely to be higher quality code if I implement something nontrivial on top of it first, and fix any issues I find.  So I'm doing #5969 first.   Once that's done and I fixed all issues that crop up, then #5882 will be ready for review.



---

archive/issue_comments_046480.json:
```json
{
    "body": "The one remaining problem: Some of the bug fixes in linear algebra included in this patch (or possibly, but unlikely, the dependency patches), cause a serious performance regression:\n\nIN SAGE-3.4.1:\n\n```\nsage: time EllipticCurve('858k2').sha().an_padic(Integer(7))\nCPU times: user 8.65 s, sys: 0.37 s, total: 9.02 s\n```\n\n\nAfter these patches the same takes much much longer (many minutes).  Using `set_verbose(2)` one sees that the codepaths are different.\n\nIt's not surprising that fixing bugs would uncover other buggy code and major performance issues, since buggy code is often very fast :-).",
    "created_at": "2009-05-04T14:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46480",
    "user": "was"
}
```

The one remaining problem: Some of the bug fixes in linear algebra included in this patch (or possibly, but unlikely, the dependency patches), cause a serious performance regression:

IN SAGE-3.4.1:

```
sage: time EllipticCurve('858k2').sha().an_padic(Integer(7))
CPU times: user 8.65 s, sys: 0.37 s, total: 9.02 s
```


After these patches the same takes much much longer (many minutes).  Using `set_verbose(2)` one sees that the codepaths are different.

It's not surprising that fixing bugs would uncover other buggy code and major performance issues, since buggy code is often very fast :-).



---

archive/issue_comments_046481.json:
```json
{
    "body": "With these patches and dependencies installed, make ptestlong:\n\n```\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 331.9 seconds\nwstein@sage:~/build/sage-3.4.2.rc0$ \n```\n",
    "created_at": "2009-05-04T15:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46481",
    "user": "was"
}
```

With these patches and dependencies installed, make ptestlong:

```
All tests passed!
Timings have been updated.
Total time for all tests: 331.9 seconds
wstein@sage:~/build/sage-3.4.2.rc0$ 
```




---

archive/issue_comments_046482.json:
```json
{
    "body": "It turns out there is a bug in 5882 still.  In the following example, computing the kernel of f is wrong, because f somehow gets defined by a map on free modules V-->V that doesn't preserve the W's that we're quotienting out by.   Trac 5882 is basically the ultimate generalization of that round2 problem everybody was confused by in 583 last quarter -- it's hard to get right!\n\n```\nsage: V = span([[1/14,3/14],[0,1/2]],ZZ); W = ZZ^2\nsage: Q = V/W\nsage: f = Q.hom([Q([1,11]), Q([1,3])])\nsage: f\nMorphism from module over Integer Ring with invariants (2, 14) to module with invariants (2, 14) that sends the generators to [(1, 11), (1, 3)]\nsage: f.kernel()\nFinitely generated module V/W over Integer Ring with invariants (14)\nsage: f.image()\nFinitely generated module V/W over Integer Ring with invariants (14)\nsage: f._phi\nFree module morphism defined by the matrix\n[ 11 -10]\n[  3  -2]\nDomain: Free module of degree 2 and rank 2 over Integer Ring\nUser basis ...\nCodomain: Free module of degree 2 and rank 2 over Integer Ring\nEchelon ...\nsage: R = Q.optimized()[0]; R\nFinitely generated module V/W over Integer Ring with invariants (2, 14)\nsage: f._phi(R.W()).is_submodule(W)\nFalse\n```\n",
    "created_at": "2009-05-05T15:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46482",
    "user": "was"
}
```

It turns out there is a bug in 5882 still.  In the following example, computing the kernel of f is wrong, because f somehow gets defined by a map on free modules V-->V that doesn't preserve the W's that we're quotienting out by.   Trac 5882 is basically the ultimate generalization of that round2 problem everybody was confused by in 583 last quarter -- it's hard to get right!

```
sage: V = span([[1/14,3/14],[0,1/2]],ZZ); W = ZZ^2
sage: Q = V/W
sage: f = Q.hom([Q([1,11]), Q([1,3])])
sage: f
Morphism from module over Integer Ring with invariants (2, 14) to module with invariants (2, 14) that sends the generators to [(1, 11), (1, 3)]
sage: f.kernel()
Finitely generated module V/W over Integer Ring with invariants (14)
sage: f.image()
Finitely generated module V/W over Integer Ring with invariants (14)
sage: f._phi
Free module morphism defined by the matrix
[ 11 -10]
[  3  -2]
Domain: Free module of degree 2 and rank 2 over Integer Ring
User basis ...
Codomain: Free module of degree 2 and rank 2 over Integer Ring
Echelon ...
sage: R = Q.optimized()[0]; R
Finitely generated module V/W over Integer Ring with invariants (2, 14)
sage: f._phi(R.W()).is_submodule(W)
False
```




---

archive/issue_comments_046483.json:
```json
{
    "body": "Any chance you could combine the 7 (!) patches into one?  That will make it a lot easier to read & judge, and to apply, of course!",
    "created_at": "2009-05-06T21:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46483",
    "user": "cremona"
}
```

Any chance you could combine the 7 (!) patches into one?  That will make it a lot easier to read & judge, and to apply, of course!



---

archive/issue_comments_046484.json:
```json
{
    "body": "> Any chance you could combine the 7 (!) patches into one? That will make it a \n> lot easier to read & judge, and to apply, of course! \n\nYes, I will, when it is ready for review.\n\nAlso, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.",
    "created_at": "2009-05-06T23:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46484",
    "user": "was"
}
```

> Any chance you could combine the 7 (!) patches into one? That will make it a 
> lot easier to read & judge, and to apply, of course! 

Yes, I will, when it is ready for review.

Also, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.



---

archive/issue_comments_046485.json:
```json
{
    "body": "I like what I see in this patch. Especially the ability to lift an element of a quotient. Using this, one can create the long exact sequence associated to an exact sequence of chain complexes.",
    "created_at": "2009-05-21T04:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46485",
    "user": "bantieau"
}
```

I like what I see in this patch. Especially the ability to lift an element of a quotient. Using this, one can create the long exact sequence associated to an exact sequence of chain complexes.



---

archive/issue_comments_046486.json:
```json
{
    "body": "Attachment [trac_5882.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882.patch) by was created at 2009-06-18 23:06:09\n\nthis one patch is based against 4.0.2.rc3.  it replaces the 8 patches from before.",
    "created_at": "2009-06-18T23:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46486",
    "user": "was"
}
```

Attachment [trac_5882.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882.patch) by was created at 2009-06-18 23:06:09

this one patch is based against 4.0.2.rc3.  it replaces the 8 patches from before.



---

archive/issue_comments_046487.json:
```json
{
    "body": "OK, this should get reviewed.  I think it's probably quite *slow* right now -- I make no claims to speed at all.  But as far as I know it is right.",
    "created_at": "2009-06-18T23:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46487",
    "user": "was"
}
```

OK, this should get reviewed.  I think it's probably quite *slow* right now -- I make no claims to speed at all.  But as far as I know it is right.



---

archive/issue_comments_046488.json:
```json
{
    "body": "Since underscore methods don't show up under ReST documentation, I think all the documentation which falls under `__init__` methods should be either moved or copied to the class level documentation.",
    "created_at": "2009-06-19T09:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46488",
    "user": "rlm"
}
```

Since underscore methods don't show up under ReST documentation, I think all the documentation which falls under `__init__` methods should be either moved or copied to the class level documentation.



---

archive/issue_comments_046489.json:
```json
{
    "body": "Some typos maybe: Should \"optimization representation\" be \"optimized representation?\"",
    "created_at": "2009-06-19T09:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46489",
    "user": "rlm"
}
```

Some typos maybe: Should "optimization representation" be "optimized representation?"



---

archive/issue_comments_046490.json:
```json
{
    "body": "Applied to Sage-4.0.2, all doctests pass with `-long`.",
    "created_at": "2009-06-19T17:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46490",
    "user": "rlm"
}
```

Applied to Sage-4.0.2, all doctests pass with `-long`.



---

archive/issue_comments_046491.json:
```json
{
    "body": "Maybe this is silly, but when I do:\n\n```\nsage: F = FreeModule(ZZ, 10)\nsage: K = F.span([F.0 + 4*F.1,5*F.2,3*F.3])\nsage: X = F/K\nsage: X.<tab>\n```\n\nI don't see Hom, V and W, because they are the *only* capitalized methods listed at all, and so they come before all the underscore stuff, and I automatically don't look at the beginning of the list because I'm never looking for underscore methods. As far as I know, all methods of classes are lowercase. Also, `V` and `W` seem like maybe bad choices of names. As soon as you do `sage: X.V?`, you immediately see what it is, but if you're scanning over what you get from tab completion, you might completely ignore it...",
    "created_at": "2009-06-19T17:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46491",
    "user": "rlm"
}
```

Maybe this is silly, but when I do:

```
sage: F = FreeModule(ZZ, 10)
sage: K = F.span([F.0 + 4*F.1,5*F.2,3*F.3])
sage: X = F/K
sage: X.<tab>
```

I don't see Hom, V and W, because they are the *only* capitalized methods listed at all, and so they come before all the underscore stuff, and I automatically don't look at the beginning of the list because I'm never looking for underscore methods. As far as I know, all methods of classes are lowercase. Also, `V` and `W` seem like maybe bad choices of names. As soon as you do `sage: X.V?`, you immediately see what it is, but if you're scanning over what you get from tab completion, you might completely ignore it...



---

archive/issue_comments_046492.json:
```json
{
    "body": "Replying to [comment:14 was]:\n>\n> Also, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.\n> \n\nIt looks like this didn't happen...",
    "created_at": "2009-06-19T17:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46492",
    "user": "jhpalmieri"
}
```

Replying to [comment:14 was]:
>
> Also, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.
> 

It looks like this didn't happen...



---

archive/issue_comments_046493.json:
```json
{
    "body": "OK, and how about lowercase c and r instead of uppercase?",
    "created_at": "2009-06-19T18:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46493",
    "user": "rlm"
}
```

OK, and how about lowercase c and r instead of uppercase?



---

archive/issue_comments_046494.json:
```json
{
    "body": "Random comments while various people (like rlm (I hope) and me) work on more thorough reviews:\n\n- the new files should be added to the reference manual, and there is some misformatted reST, which the attached patch fixes.  It also moves docs from the `__init__` methods to the classes, as rlm suggests.\n\n- I don't understand the point (or maybe the documentation) for M.optimized():\n {{{\n This has the advantage that any homomorphism from self extends to a homomorphism from V\n }}}\n If I have a map f: V/W --> Z, then I certainly get a map g: V --> Z: just compose the quotient map V --> V/W with f.\n\n- the argument \"check\" should be documented: I can see what it does by reading the source code, but it should be described in `FGP_module` and `FGP_Module_class.__init__` (or actually in `FGP_Module_class`), and wherever else it's used.",
    "created_at": "2009-06-20T03:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46494",
    "user": "jhpalmieri"
}
```

Random comments while various people (like rlm (I hope) and me) work on more thorough reviews:

- the new files should be added to the reference manual, and there is some misformatted reST, which the attached patch fixes.  It also moves docs from the `__init__` methods to the classes, as rlm suggests.

- I don't understand the point (or maybe the documentation) for M.optimized():
 {{{
 This has the advantage that any homomorphism from self extends to a homomorphism from V
 }}}
 If I have a map f: V/W --> Z, then I certainly get a map g: V --> Z: just compose the quotient map V --> V/W with f.

- the argument "check" should be documented: I can see what it does by reading the source code, but it should be described in `FGP_module` and `FGP_Module_class.__init__` (or actually in `FGP_Module_class`), and wherever else it's used.



---

archive/issue_comments_046495.json:
```json
{
    "body": "Attachment [ref_5882.patch](tarball://root/attachments/some-uuid/ticket5882/ref_5882.patch) by jhpalmieri created at 2009-06-20 03:11:12\n\nreferee's patch -- reST fixes",
    "created_at": "2009-06-20T03:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46495",
    "user": "jhpalmieri"
}
```

Attachment [ref_5882.patch](tarball://root/attachments/some-uuid/ticket5882/ref_5882.patch) by jhpalmieri created at 2009-06-20 03:11:12

referee's patch -- reST fixes



---

archive/issue_comments_046496.json:
```json
{
    "body": "> the new files should be added to the reference manual, and there is some \n> misformatted reST, which the attached patch fixes. It also moves docs from \n> the __init__ methods to the classes, as rlm suggests. \n\nThanks for ading ref_5882.patch to fix this!\n\n> I don't understand the point (or maybe the documentation) for M.optimized():\n> \"This has the advantage that any homomorphism from self extends to a homomorphism from V\"\n\nYes, I should change that, since of course any homomorphism extends.  The point is that with M.optimized() it *trivially extends* because\nthe gens for M.optimized().V() are *exactly the same* as the gens for M.  Also, the dimension of M.optimized().V() is the same as the rank of M.\n\n> the argument \"check\" should be documented:\n\nI can't disagree with that -- all options should be documented with examples. \n\n\n>>     Also, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.\n\n> It looks like this didn't happen... \n\nI was going to change them, but realized it will break compatibility with quotients of vector spaces, which have used V and W for a year now.  I prefer instead just adding two new methods \"cover()\" and \"relations()\" that just return V() and W(), both to fgp modules and to quotients of vector spaces.  Then everything is backward compatible and old code doesn't break.",
    "created_at": "2009-06-20T10:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46496",
    "user": "was"
}
```

> the new files should be added to the reference manual, and there is some 
> misformatted reST, which the attached patch fixes. It also moves docs from 
> the __init__ methods to the classes, as rlm suggests. 

Thanks for ading ref_5882.patch to fix this!

> I don't understand the point (or maybe the documentation) for M.optimized():
> "This has the advantage that any homomorphism from self extends to a homomorphism from V"

Yes, I should change that, since of course any homomorphism extends.  The point is that with M.optimized() it *trivially extends* because
the gens for M.optimized().V() are *exactly the same* as the gens for M.  Also, the dimension of M.optimized().V() is the same as the rank of M.

> the argument "check" should be documented:

I can't disagree with that -- all options should be documented with examples. 


>>     Also, I'll rename the V, W methods to cover and relations, with C() and R() as aliases.

> It looks like this didn't happen... 

I was going to change them, but realized it will break compatibility with quotients of vector spaces, which have used V and W for a year now.  I prefer instead just adding two new methods "cover()" and "relations()" that just return V() and W(), both to fgp modules and to quotients of vector spaces.  Then everything is backward compatible and old code doesn't break.



---

archive/issue_comments_046497.json:
```json
{
    "body": "> OK, and how about lowercase c and r instead of uppercase? \n\nI don't like that more, because they are modules.  In mathematics, modules are usually upper case and *elements* of modules are lower case.",
    "created_at": "2009-06-20T10:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46497",
    "user": "was"
}
```

> OK, and how about lowercase c and r instead of uppercase? 

I don't like that more, because they are modules.  In mathematics, modules are usually upper case and *elements* of modules are lower case.



---

archive/issue_comments_046498.json:
```json
{
    "body": "Attachment [trac_5882-final_referee_followup.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-final_referee_followup.patch) by was created at 2009-06-20 16:09:02",
    "created_at": "2009-06-20T16:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46498",
    "user": "was"
}
```

Attachment [trac_5882-final_referee_followup.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-final_referee_followup.patch) by was created at 2009-06-20 16:09:02



---

archive/issue_comments_046499.json:
```json
{
    "body": "A partial review; I've looked at the files *not* in the fg_pid directory, and I'm happy with them except for the minor comments below about free_module_morphism.py.  I'm now working through the files in the fg_pid directory, and I'm about halfway through fgp_module.py.\n\n*******************************************\n\nIn free_module_morphism.py: \n\nin `inverse_image`, is there any speed gain if you check whether the rank of the homomorphism is zero at the beginning?  that is, change\n\n```\n  if self.domain().rank() == 0:\n     return self.domain() \n```\n\nto\n\n```\n  if self.domain().rank() == 0 or self.rank() == 0:\n     return self.domain() \n```\n\nor even to\n\n```\n  if self.rank() == 0:\n     return self.domain() \n```\n\n\nA very minor issue: In `inverse_image`, in the lines\n\n```\n     if R.is_field(): \n           # By solving, find lifts of each of the basis elements of V. \n           # Each row of Y gives a linear combination of the basis for the domain \n           # that maps to one of the basis elements V. \n           C = A.solve_left(B) \n```\n\nchange \"Each row of Y\" to \"Each row of C\"?\n\n*******************************************\n\nfgp_module.py:\n\nthe function FGP_Module: documentation should say what it returns: V/W as a f.g. R-module.  For the inputs, V and W need to be free R-modules.\n\n_coerce_map_from_: I think that V/W should have a coercion from V, so testing isinstance(S, FGP_Module_class) won't work.  More generally, you should have coercions from anything of the form V/W' to V/W, as long as W' is contained in W: that is, you should have coercions not just from submodules, but also from modules with canonical surjections onto V/W.  (There may be many maps from V to V/W, but there is one *canonical* map, so I think there should be a coercion map.)\n\nin free_module.py, there is a `__cmp__` method but not an `__eq__` method, and here it's the other way around.  Is this an issue?  Do we have a policy about which one to use?\n\nHere's a problem with is_submodule:\n\n```\nsage: V = FreeModule(ZZ, 1)\nsage: W = V.submodule([0*V.0])\nsage: W2 = V.submodule([2*V.0])\nsage: V/W  # isomorphic to Z\nFinitely generated module V/W over Integer Ring with invariants (0)\nsage: V/W2  # isomorphic to Z/2Z\nFinitely generated module V/W over Integer Ring with invariants (2)\nsage: (V/W).is_submodule(V/W2)\nTrue\n```\n\nThis is because the implementation is wrong: if you want V/W to be a submodule of V'/W', then you want V to be a submodule of V', and the inclusion map should induce a surjection of W onto W' (hence an isomorphism between W and W' -- given an injection V --> V' which induces a map W --> W', the induced map must be an injection also).  Should you change the end from\n\n```\n        return self.V().is_submodule(A.V()) and self.W().is_submodule(A.W())\n```\n\nto\n\n```\n        return self.V().is_submodule(A.V()) and self.W() == A.W()\n```\n\nThe docstring should be changed to reflect this, as should the doctests; in the existing doctests, I don't think that A is actually a submodule of Q.  In the simpler (but somewhat analogous) situation of Z/2Z and Z/4Z, then although abstractly Z/2Z is a submodule of Z/4Z, the identity map Z --> Z does not induce the inclusion.  The identity map Z --> Z induces an inclusion 4Z --> 2Z, which then induces a *surjection* Z/4Z --> Z/2Z.\n\nAlso, the first sentence of the docstring is wrong: it says \"Return True if A is a submodule of self\", and it should be \"Return True if self is a submodule of A\".\n\nbase_ring: delete the comment (`# this will be done in __init__`)?\n\n`_smith_form_`: document the form of the output, or at least give a reference to smith_form from matrix2.pyx.\n\ninvariants needs a docstring, not just doctests.  (The term \"invariants\" is used frequently in fgp_module.py, but is never defined.)  Document the argument \"include_ones\"?\n\ngens: in the docstring, change \"lements\" to \"elements\".  Change it to \"elements g0,...,gn of self\"?  (Add \"of self\"?)\n\nis it worth changing \"isinstance(x, FGP_Module_class)\" to \"is_FGP_Module(x)\" many places in this file?  (Otherwise, is \"is_FGP_Module\" used anywhere?  We could delete it...)\n\n\nI'm still working on this file, and I haven't looked at fgp_morphism or fgp_element in any detail yet (except to note that the in the docstring for FGP_Morphism, the comment \"where the morphism doesn't extend to V1\" needs to be rephrased).  I'm going on a family trip tomorrow, though, so I may not have time to work on this for a few days.",
    "created_at": "2009-06-20T22:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46499",
    "user": "jhpalmieri"
}
```

A partial review; I've looked at the files *not* in the fg_pid directory, and I'm happy with them except for the minor comments below about free_module_morphism.py.  I'm now working through the files in the fg_pid directory, and I'm about halfway through fgp_module.py.

*******************************************

In free_module_morphism.py: 

in `inverse_image`, is there any speed gain if you check whether the rank of the homomorphism is zero at the beginning?  that is, change

```
  if self.domain().rank() == 0:
     return self.domain() 
```

to

```
  if self.domain().rank() == 0 or self.rank() == 0:
     return self.domain() 
```

or even to

```
  if self.rank() == 0:
     return self.domain() 
```


A very minor issue: In `inverse_image`, in the lines

```
     if R.is_field(): 
           # By solving, find lifts of each of the basis elements of V. 
           # Each row of Y gives a linear combination of the basis for the domain 
           # that maps to one of the basis elements V. 
           C = A.solve_left(B) 
```

change "Each row of Y" to "Each row of C"?

*******************************************

fgp_module.py:

the function FGP_Module: documentation should say what it returns: V/W as a f.g. R-module.  For the inputs, V and W need to be free R-modules.

_coerce_map_from_: I think that V/W should have a coercion from V, so testing isinstance(S, FGP_Module_class) won't work.  More generally, you should have coercions from anything of the form V/W' to V/W, as long as W' is contained in W: that is, you should have coercions not just from submodules, but also from modules with canonical surjections onto V/W.  (There may be many maps from V to V/W, but there is one *canonical* map, so I think there should be a coercion map.)

in free_module.py, there is a `__cmp__` method but not an `__eq__` method, and here it's the other way around.  Is this an issue?  Do we have a policy about which one to use?

Here's a problem with is_submodule:

```
sage: V = FreeModule(ZZ, 1)
sage: W = V.submodule([0*V.0])
sage: W2 = V.submodule([2*V.0])
sage: V/W  # isomorphic to Z
Finitely generated module V/W over Integer Ring with invariants (0)
sage: V/W2  # isomorphic to Z/2Z
Finitely generated module V/W over Integer Ring with invariants (2)
sage: (V/W).is_submodule(V/W2)
True
```

This is because the implementation is wrong: if you want V/W to be a submodule of V'/W', then you want V to be a submodule of V', and the inclusion map should induce a surjection of W onto W' (hence an isomorphism between W and W' -- given an injection V --> V' which induces a map W --> W', the induced map must be an injection also).  Should you change the end from

```
        return self.V().is_submodule(A.V()) and self.W().is_submodule(A.W())
```

to

```
        return self.V().is_submodule(A.V()) and self.W() == A.W()
```

The docstring should be changed to reflect this, as should the doctests; in the existing doctests, I don't think that A is actually a submodule of Q.  In the simpler (but somewhat analogous) situation of Z/2Z and Z/4Z, then although abstractly Z/2Z is a submodule of Z/4Z, the identity map Z --> Z does not induce the inclusion.  The identity map Z --> Z induces an inclusion 4Z --> 2Z, which then induces a *surjection* Z/4Z --> Z/2Z.

Also, the first sentence of the docstring is wrong: it says "Return True if A is a submodule of self", and it should be "Return True if self is a submodule of A".

base_ring: delete the comment (`# this will be done in __init__`)?

`_smith_form_`: document the form of the output, or at least give a reference to smith_form from matrix2.pyx.

invariants needs a docstring, not just doctests.  (The term "invariants" is used frequently in fgp_module.py, but is never defined.)  Document the argument "include_ones"?

gens: in the docstring, change "lements" to "elements".  Change it to "elements g0,...,gn of self"?  (Add "of self"?)

is it worth changing "isinstance(x, FGP_Module_class)" to "is_FGP_Module(x)" many places in this file?  (Otherwise, is "is_FGP_Module" used anywhere?  We could delete it...)


I'm still working on this file, and I haven't looked at fgp_morphism or fgp_element in any detail yet (except to note that the in the docstring for FGP_Morphism, the comment "where the morphism doesn't extend to V1" needs to be rephrased).  I'm going on a family trip tomorrow, though, so I may not have time to work on this for a few days.



---

archive/issue_comments_046500.json:
```json
{
    "body": "My next installment: this finishes up with the file fgp_module.py.\n\ncoordinate_vector:\n\n```\nself.optimized() # computes T as side effect -- see above\n```\n\nShould say \"see below\", I think.\n\noptimize: in the comments\n\n```\n        # Compute matrix X of linear transformation from self._V to V.\n        # This matrix X gives each basis element of self._V in terms\n        # of our new optimized V, modulo the W's.\n```\n\nMaybe \"X\" should be replaced by \"T\".  If not, then \"T\" should be described, since it's cached, and so is presumably important.\n\nhom: if `len(im_gens) == 0`, then we can't use `M.hom(...)` to define the zero map to another module.  Should we be able to?  That is, should we be able to specify the codomain explicitly instead of the method using `N = im_gens.universe()`?\n\nrandom_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?\n\nright before random_fgp_module: ZZ has already been imported\n\nrandom_fgp_module: say that ``R`` is optional, default ZZ\n\n***********************\n\nA general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs?  This should be documented somewhere so interested people know what to work on.\n\n***********************\n\nI hope to get to the last two files soon.",
    "created_at": "2009-06-21T02:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46500",
    "user": "jhpalmieri"
}
```

My next installment: this finishes up with the file fgp_module.py.

coordinate_vector:

```
self.optimized() # computes T as side effect -- see above
```

Should say "see below", I think.

optimize: in the comments

```
        # Compute matrix X of linear transformation from self._V to V.
        # This matrix X gives each basis element of self._V in terms
        # of our new optimized V, modulo the W's.
```

Maybe "X" should be replaced by "T".  If not, then "T" should be described, since it's cached, and so is presumably important.

hom: if `len(im_gens) == 0`, then we can't use `M.hom(...)` to define the zero map to another module.  Should we be able to?  That is, should we be able to specify the codomain explicitly instead of the method using `N = im_gens.universe()`?

random_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?

right before random_fgp_module: ZZ has already been imported

random_fgp_module: say that ``R`` is optional, default ZZ

***********************

A general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs?  This should be documented somewhere so interested people know what to work on.

***********************

I hope to get to the last two files soon.



---

archive/issue_comments_046501.json:
```json
{
    "body": "Replying to [comment:30 jhpalmieri]:\n> ***********************\n> \n> A general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs?  This should be documented somewhere so interested people know what to work on.\n> \n> ***********************\n\nTo my understanding, it is the lack of an implementation of Hermite normal form for general PIDs.",
    "created_at": "2009-06-21T12:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46501",
    "user": "rlm"
}
```

Replying to [comment:30 jhpalmieri]:
> ***********************
> 
> A general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs?  This should be documented somewhere so interested people know what to work on.
> 
> ***********************

To my understanding, it is the lack of an implementation of Hermite normal form for general PIDs.



---

archive/issue_comments_046502.json:
```json
{
    "body": "Replying to [comment:31 rlm]:\n> \n> To my understanding, it is the lack of an implementation of Hermite normal form for general PIDs.\n\nWe have this now -- see ticket #6178.",
    "created_at": "2009-06-22T06:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46502",
    "user": "davidloeffler"
}
```

Replying to [comment:31 rlm]:
> 
> To my understanding, it is the lack of an implementation of Hermite normal form for general PIDs.

We have this now -- see ticket #6178.



---

archive/issue_comments_046503.json:
```json
{
    "body": "I just downloaded the patches, installed, built, and tried it out. One of the first things that I tried was `ngens()` -- I wanted to know if a module defined as a quotient of something of rank 2 counted as having 2 generators or 1. I got this:\n\n\n```\nsage: A = QQ**2\nsage: B = A.span([[1,2], [5, 1/17]])\nsage: C = A.span([[2,4],[5,1/17]],ZZ)\nsage: Q = B/C; Q\nFinitely generated module V/W over Integer Ring with invariants (2)\nsage: Q.ngens()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/david/.sage/temp/groke/6867/_home_david__sage_init_sage_0.py in <module>()\n\n/home/david/sage-4.0.2/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.ngens (sage/structure/parent_gens.c:2383)()                         \n\n/home/david/sage-4.0.2/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.check_old_coerce (sage/structure/parent_gens.c:1140)()                             \n\nRuntimeError: Finitely generated module V/W over Integer Ring with invariants (2) still using old coercion framework\n```\n",
    "created_at": "2009-06-23T17:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46503",
    "user": "davidloeffler"
}
```

I just downloaded the patches, installed, built, and tried it out. One of the first things that I tried was `ngens()` -- I wanted to know if a module defined as a quotient of something of rank 2 counted as having 2 generators or 1. I got this:


```
sage: A = QQ**2
sage: B = A.span([[1,2], [5, 1/17]])
sage: C = A.span([[2,4],[5,1/17]],ZZ)
sage: Q = B/C; Q
Finitely generated module V/W over Integer Ring with invariants (2)
sage: Q.ngens()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/david/.sage/temp/groke/6867/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.0.2/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.ngens (sage/structure/parent_gens.c:2383)()                         

/home/david/sage-4.0.2/local/lib/python2.5/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.check_old_coerce (sage/structure/parent_gens.c:1140)()                             

RuntimeError: Finitely generated module V/W over Integer Ring with invariants (2) still using old coercion framework
```




---

archive/issue_comments_046504.json:
```json
{
    "body": "(sorry, there is a ZZ missing in the second line of the example, I cut + pasted wrongly)",
    "created_at": "2009-06-23T17:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46504",
    "user": "davidloeffler"
}
```

(sorry, there is a ZZ missing in the second line of the example, I cut + pasted wrongly)



---

archive/issue_comments_046505.json:
```json
{
    "body": "Another bug:\n\n```\nsage: A = ZZ**1\nsage: Q3 = A / A.span([[3]])\nsage: Q6 = A / A.span([[6]])\nsage: Q6.is_submodule(Q3)\nTrue\n```\n\n\nI am currently doing a proof-of-concept abelian groups implementation using your code, and this has involved making a few minor changes anyway, so I'll do a fix for is_submodule as part of that (and add an is_quotient method).",
    "created_at": "2009-06-24T09:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46505",
    "user": "davidloeffler"
}
```

Another bug:

```
sage: A = ZZ**1
sage: Q3 = A / A.span([[3]])
sage: Q6 = A / A.span([[6]])
sage: Q6.is_submodule(Q3)
True
```


I am currently doing a proof-of-concept abelian groups implementation using your code, and this has involved making a few minor changes anyway, so I'll do a fix for is_submodule as part of that (and add an is_quotient method).



---

archive/issue_comments_046506.json:
```json
{
    "body": "OK, I've now read the docstrings and it looks like that was the intended behaviour; but I really don't like the idea of Z/6 being a submodule of Z/3. I suggest we have a new method called something like \"maps_into\" which does what \"is_submodule\" previously did, and reserve \"is_submodule\" for cases where the obvious map both exists and is injective.",
    "created_at": "2009-06-24T09:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46506",
    "user": "davidloeffler"
}
```

OK, I've now read the docstrings and it looks like that was the intended behaviour; but I really don't like the idea of Z/6 being a submodule of Z/3. I suggest we have a new method called something like "maps_into" which does what "is_submodule" previously did, and reserve "is_submodule" for cases where the obvious map both exists and is injective.



---

archive/issue_comments_046507.json:
```json
{
    "body": "Okay, I'm done with my review.  Earlier, I discussed everything except the files \"fgp_element.py\" and \"fgp_morphism.py\".  The file \"fgp_element.py\" looks good to me.  The file \"fgp_morphism.py\" is mostly good, but I have a few comments:\n\nFGP_Morphism: as mentioned avove, need to fix the part of the docstring which says \"where the morphism doesn't extend to V1\"\n\nFGP_Morphism, `__init__`: can we delete the line\n\n```\n    from sage.matrix.all import diagonal_matrix\n```\n\n\nAlso in `__init__`: Do you expect the error messages like \"domain of phi must be V for MO\" to ever appear?  They are pretty cryptic -- if you haven't read the code, you won't know what \"V for MO\" means.\n\nIn `__call__`: when x is an FGP_Module, should you check that x is a submodule of self.domain() and return an appropriate error if not?\n\nI note that in \"image\", you call FGP_Module with `check=False`, but you don't have this in \"kernel\".  Should you use `check=False` there, too?\n\nShould \"preimage\" be a synonym for \"lift\"?  Or should there be a method \"preimage\" which acts like \"lift\" on elements, but also works on submodules?\n\nIn `_coerce_map_from_`: should there be a coercion from Hom(X,Y) to Hom(X,Z) if there is a coercion from Y to Z?  Should there be a coercion from Hom(X,Y) to Hom(W,Y) if there is a coercion from W to X?\n\n\nOverall, this is very impressive, and it will be great to have this as part of Sage.",
    "created_at": "2009-06-26T16:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46507",
    "user": "jhpalmieri"
}
```

Okay, I'm done with my review.  Earlier, I discussed everything except the files "fgp_element.py" and "fgp_morphism.py".  The file "fgp_element.py" looks good to me.  The file "fgp_morphism.py" is mostly good, but I have a few comments:

FGP_Morphism: as mentioned avove, need to fix the part of the docstring which says "where the morphism doesn't extend to V1"

FGP_Morphism, `__init__`: can we delete the line

```
    from sage.matrix.all import diagonal_matrix
```


Also in `__init__`: Do you expect the error messages like "domain of phi must be V for MO" to ever appear?  They are pretty cryptic -- if you haven't read the code, you won't know what "V for MO" means.

In `__call__`: when x is an FGP_Module, should you check that x is a submodule of self.domain() and return an appropriate error if not?

I note that in "image", you call FGP_Module with `check=False`, but you don't have this in "kernel".  Should you use `check=False` there, too?

Should "preimage" be a synonym for "lift"?  Or should there be a method "preimage" which acts like "lift" on elements, but also works on submodules?

In `_coerce_map_from_`: should there be a coercion from Hom(X,Y) to Hom(X,Z) if there is a coercion from Y to Z?  Should there be a coercion from Hom(X,Y) to Hom(W,Y) if there is a coercion from W to X?


Overall, this is very impressive, and it will be great to have this as part of Sage.



---

archive/issue_comments_046508.json:
```json
{
    "body": "I have been working on this as part of a Sage Days 16 project to reimplement abelian groups. The above patch:\n\n- adds new methods `_element_class` and `_subquotient_class` which can be overridden by derived classes\n\n- adds a new method `has_canonical_map_to` which does what `is_submodule` previously did, and changes `is_submodule` so it is true if and only if the canonical map exists *and is injective*.\n\n- adjusts some things relating to `gens`, so derived classes can have generators which are not necessarily in Smith form, and made the necessary corresponding changes to `hom`. There are now separate methods `smithform_gens` and `gens`, and the \"internal\" uses of generators all call `smithform_gens`, so it is safe for derived classes to override `gens`.\n\nI *haven't* changed the printing code, as I threatened to do last week -- on reflection I decided that elements comparing as equal and printing as unequal was just too confusing.\n\nDavid",
    "created_at": "2009-06-30T09:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46508",
    "user": "davidloeffler"
}
```

I have been working on this as part of a Sage Days 16 project to reimplement abelian groups. The above patch:

- adds new methods `_element_class` and `_subquotient_class` which can be overridden by derived classes

- adds a new method `has_canonical_map_to` which does what `is_submodule` previously did, and changes `is_submodule` so it is true if and only if the canonical map exists *and is injective*.

- adjusts some things relating to `gens`, so derived classes can have generators which are not necessarily in Smith form, and made the necessary corresponding changes to `hom`. There are now separate methods `smithform_gens` and `gens`, and the "internal" uses of generators all call `smithform_gens`, so it is safe for derived classes to override `gens`.

I *haven't* changed the printing code, as I threatened to do last week -- on reflection I decided that elements comparing as equal and printing as unequal was just too confusing.

David



---

archive/issue_comments_046509.json:
```json
{
    "body": "> adds new methods _element_class and _subquotient_class which can be overridden by derived classes\n\nIn the docstring for `_element_class`, should \"creating subquotients\" say \"creating elements\"?\n\n> changes is_submodule\n\nI like your change, but I would like `is_submodule` to have more documentation, saying (for example) that it returns True if self.V() is a submodule of A.V(), with self.W() equal to A.W().\n\nI don't have much of an opinion about this either way, but do you want to rename `smithform_gens` to `_smithform_gens` so it's less visible?\n\nFor `annihilator`: the first line of the docstring ends a bit abruptly.  Should this method return an actual ideal, not just an element of the ring?",
    "created_at": "2009-06-30T20:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46509",
    "user": "jhpalmieri"
}
```

> adds new methods _element_class and _subquotient_class which can be overridden by derived classes

In the docstring for `_element_class`, should "creating subquotients" say "creating elements"?

> changes is_submodule

I like your change, but I would like `is_submodule` to have more documentation, saying (for example) that it returns True if self.V() is a submodule of A.V(), with self.W() equal to A.W().

I don't have much of an opinion about this either way, but do you want to rename `smithform_gens` to `_smithform_gens` so it's less visible?

For `annihilator`: the first line of the docstring ends a bit abruptly.  Should this method return an actual ideal, not just an element of the ring?



---

archive/issue_comments_046510.json:
```json
{
    "body": "Thanks for looking at this. I agree with your observations about the docstrings. \n\nWith `smithform_gens`, the motivation is that I really want both gens and smithform_gens to be accessible to the user in cases where they're not automatically the same -- this is one of the most annoying features of the Gap-based abelian groups implementation we have now. If you create C2 x C3 x C5 x C7, then `elementary_divisors` tells you that it is cyclic of order 210, but there's no way to find an element of order 210. But perhaps it is better to have these as private methods in `FGP_Module_class`, and then have public methods in `AdditiveAbelianGroup` that call them.\n\nFor `annihilator`, essentially it is just there so I can use it to do `exponent` for abelian groups, so I do want it to return an element.",
    "created_at": "2009-07-01T08:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46510",
    "user": "davidloeffler"
}
```

Thanks for looking at this. I agree with your observations about the docstrings. 

With `smithform_gens`, the motivation is that I really want both gens and smithform_gens to be accessible to the user in cases where they're not automatically the same -- this is one of the most annoying features of the Gap-based abelian groups implementation we have now. If you create C2 x C3 x C5 x C7, then `elementary_divisors` tells you that it is cyclic of order 210, but there's no way to find an element of order 210. But perhaps it is better to have these as private methods in `FGP_Module_class`, and then have public methods in `AdditiveAbelianGroup` that call them.

For `annihilator`, essentially it is just there so I can use it to do `exponent` for abelian groups, so I do want it to return an element.



---

archive/issue_comments_046511.json:
```json
{
    "body": "Great, that all makes sense.  For annihilator, then, you could the docstring from \"Return the ideal\" to \"Return the generator of the ideal\".",
    "created_at": "2009-07-01T14:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46511",
    "user": "jhpalmieri"
}
```

Great, that all makes sense.  For annihilator, then, you could the docstring from "Return the ideal" to "Return the generator of the ideal".



---

archive/issue_comments_046512.json:
```json
{
    "body": "Attachment [trac_5882-additions.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-additions.patch) by davidloeffler created at 2009-07-02 12:49:09\n\nI've uploaded a new patch taking into account John's suggestions.",
    "created_at": "2009-07-02T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46512",
    "user": "davidloeffler"
}
```

Attachment [trac_5882-additions.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-additions.patch) by davidloeffler created at 2009-07-02 12:49:09

I've uploaded a new patch taking into account John's suggestions.



---

archive/issue_comments_046513.json:
```json
{
    "body": "RESPONSE TO ALL REFEREE COMMENTS IN WHICH EVERYTHING IS ADDRESSED.  A patch will be posted in a moment too.\n\n> in inverse_image, is there any speed gain if you check whether the rank of the homomorphism is zero at the beginning? that is, change\n\n\nDONE\n\n\n> A very minor issue: In inverse_image, in the lines\n>     if R.is_field(): \n>           # By solving, find lifts of each of the basis elements of V. \n>           # Each row of Y gives a linear combination of the basis for the domain \n>           # that maps to one of the basis elements V. \n>           C = A.solve_left(B) \n> change \"Each row of Y\" to \"Each row of C\"?\n\nDONE\n\n> \n> *******************************************\n> \n> fgp_module.py:\n> \n> the function FGP_Module: documentation should say what it returns: V/W as a f.g. R-module. For the inputs, V and W need to be free R-modules.\n\nDONE\n\n> _coerce_map_from_: I think that V/W should have a coercion from V, so testing isinstance(S, FGP_Module_class) won't work. More generally, you should have coercions from anything of the form V/W' to V/W, as long as W' is contained in W: that is, you should have coercions not just from submodules, but also from modules with canonical surjections onto V/W. (There may be many maps from V to V/W, but there is one *canonical* map, so I think there should be a coercion map.)\n\nDONE\n\n> in free_module.py, there is a __cmp__ method but not an __eq__ method, and here it's the other way around. Is this an issue? Do we have a policy about which one to use?\n\nI think __eq__ is better since A < B suggest to a lot of people that\n\"A is contained in B\", which isn't the case at all.  But I don't want\nto potentially break the API of the general free_module code in this\npatch.\n\n> Here's a problem with is_submodule:\n> \n> sage: V = FreeModule(ZZ, 1)\n> sage: W = V.submodule([0*V.0])\n> sage: W2 = V.submodule([2*V.0])\n> sage: V/W  # isomorphic to Z\n> Finitely generated module V/W over Integer Ring with invariants (0)\n> sage: V/W2  # isomorphic to Z/2Z\n> Finitely generated module V/W over Integer Ring with invariants (2)\n> sage: (V/W).is_submodule(V/W2)\n> True\n> \n> This is because the implementation is wrong: if you want V/W to be a submodule of V'/W', then you want V to be a submodule of V', and the inclusion map should induce a surjection of W onto W' (hence an isomorphism between W and W' -- given an injection V --> V' which induces a map W --> W', the induced map must be an injection also). Should you change the end from\n> \n>         return self.V().is_submodule(A.V()) and self.W().is_submodule(A.W())\n> \n> to\n> \n>         return self.V().is_submodule(A.V()) and self.W() == A.W()\n\nDONE -- good change.  David Loeffler also found this issue and \"fixed\"\nthe code, but his fix was wrong too (it basically ignored the V's).\n\nBy the way, after making the above fix then running doctests, the\nautomated randomized testing code *did* find a bug in the image\ncommand.  I fixed that by changing\n\n        V = self._phi.image()\n\nto\n\n        V = self._phi.image() + self.codomain().W()\n\nin the image method in fgp_morphism.py\n\n> The docstring should be changed to reflect this, as should the doctests; in the existing doctests, I don't think that A is actually a submodule of Q. In the simpler (but somewhat analogous) situation of Z/2Z and Z/4Z, then although abstractly Z/2Z is a submodule of Z/4Z, the identity map Z --> Z does not induce the inclusion. The identity map Z --> Z induces an inclusion 4Z --> 2Z, which then induces a *surjection* Z/4Z --> Z/2Z.\n> \n> Also, the first sentence of the docstring is wrong: it says \"Return True if A is a submodule of self\", and it should be \"Return True if self is a submodule of A\".\n\nDONE\n\n> \n> base_ring: delete the comment (# this will be done in __init__)?\n\nDONE\n\n> \n> _smith_form_: document the form of the output, or at least give a reference to smith_form from matrix2.pyx.\n\nDONE.\n\nAlso, I changed all the smithform's to smith_form's, which David L. introduced. \n\n> invariants needs a docstring, not just doctests. (The term \"invariants\" is used frequently in fgp_module.py, but is never defined.) Document the argument \"include_ones\"?\n\ndone.\n\n> \n> gens: in the docstring, change \"lements\" to \"elements\". Change it to \"elements g0,...,gn of self\"? (Add \"of self\"?)\n\nDONE\n\n> \n> is it worth changing \"isinstance(x, FGP_Module_class)\" to \"is_FGP_Module(x)\" many places in this file? (Otherwise, is \"is_FGP_Module\" used anywhere? We could delete it...)\n\nYes, DONE.\n\n> I'm still working on this file, and I haven't looked at fgp_morphism or fgp_element in any detail yet (except to note that the in the docstring for FGP_Morphism, the comment \"where the morphism doesn't extend to V1\" needs to be rephrased). I'm going on a family trip tomorrow, though, so I may not have time to work on this for a few days.\n\ndone.\n\n\n\n\n> My next installment: this finishes up with the file fgp_module.py.\n> \n> coordinate_vector:\n> \n> self.optimized() # computes T as side effect -- see above\n> \n> Should say \"see below\", I think.\n\nDONE\n\n> \n> optimize: in the comments\n> \n>         # Compute matrix X of linear transformation from self._V to V.\n>         # This matrix X gives each basis element of self._V in terms\n>         # of our new optimized V, modulo the W's.\n> \n> Maybe \"X\" should be replaced by \"T\". If not, then \"T\" should be described, since it's cached, and so is presumably important.\n\nDONE.  I called it X at one point, e.g., in my doodles, but changed to T.\n\n> hom: if len(im_gens) == 0, then we can't use M.hom(...) to define the zero map to another module. Should we be able to? That is, should we be able to specify the codomain explicitly instead of the method using N = im_gens.universe()?\n\nDONE -- You're right, yes, we should be able to.  I implemented hom wrong,\nsince hom should have an optional codomain parameter.  Fixed. \n\n> random_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?\n\nI'm really not sure.  Conceptually if one constructs A = V/W, then it\nis easiest to think of random_element as \"Create a random element of\nself=V/W, by creating a random element of V and reducing it modulo W.\"\nThe optimized() thing doesn't seem so canonical in terms of the given\ninput.  So I'm definitely not so sure.  Why do you think that would be\nbetter? Efficiency?\n\n> \n> right before random_fgp_module: ZZ has already been imported\n\nDONE.\n\n\n> random_fgp_module: say that R is optional, default ZZ\n\nDONE\n\n> ***********************\n> \n> A general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs? This should be documented somewhere so interested people know what to work on.\n> \n\nDONE - in the very top of fgp_module.py\n\n> ***********************\n> \n> I hope to get to the last two files soon.\n\n\n\n\n\n> Okay, I'm done with my review. Earlier, I discussed everything except the files \"fgp_element.py\" and \"fgp_morphism.py\". The file \"fgp_element.py\" looks good to me. The file \"fgp_morphism.py\" is mostly good, but I have a few comments:\n> \n> FGP_Morphism: as mentioned avove, need to fix the part of the docstring which says \"where the morphism doesn't extend to V1\"\n\nDONE\n\n> FGP_Morphism, __init__: can we delete the line\n> \n>     from sage.matrix.all import diagonal_matrix\n\nDONE\n\n> \n> Also in __init__: Do you expect the error messages like \"domain of phi must be V for MO\" to ever appear? They are pretty cryptic -- if you haven't read the code, you won't know what \"V for MO\" means.\n\nDONE.\n\n> In __call__: when x is an FGP_Module, should you check that x is a submodule of self.domain() and return an appropriate error if not?\n\nDONE, and I added some doctests. \n\n> I note that in \"image\", you call FGP_Module with check=False, but you don't have this in \"kernel\". Should you use check=False there, too?\n\nDONE -- I've changed all the \"internal checks\" (not things passed in by the\nuser) to use the DEBUG flag in fgp_module.py.  Then one can uniformly\nturn them all on/off.  I think it is best to leave all the checks on\nfor now, but turn them off after the code has been out in the wild for\na while, and work has gone into optimizing it (so far 0 work has gone\ninto optimization).\n\n> \n> Should \"preimage\" be a synonym for \"lift\"? Or should there be a method \"preimage\" which acts like \"lift\" on elements, but also works on submodules?\n> \n\nHmm.  Actually, we should have at least inverse_image as a method on\nmorphisms of fgp modules, since that isn't there at all!  It was\nimportant to add this method to fg modules, and should be easy on fgp\nmodules.  This provides the same functionality as preimage.  I think\npreimage would be good to add, but then it should be added for fg free\nmodules too, so it's best to wait for another ticket and do it right. \n\n> In _coerce_map_from_: should there be a coercion from Hom(X,Y) to Hom(X,Z) if there is a coercion from Y to Z? Should there be a coercion from Hom(X,Y) to Hom(W,Y) if there is a coercion from W to X?\n>\n\nYes, yes, but I don't know if this will work, since at least currently\nthat function returns bool rather than the actual map. Also, the same\nshould be added to free modules.  I think this would be better to do\non another ticket.\n\n> Overall, this is very impressive, and it will be great to have this as part of Sage.\n\n\nFOR NEW TICKETS:\n\n* Add a method \"preimage\" that acts like \"lift\" on elements, but also works on submodules.\n\n* There should be a coercion from Hom(X,Y) to Hom(X,Z) if there is a\n  coercion from Y to Z. There should there be a coercion from Hom(X,Y) to\n  Hom(W,Y) if there is a coercion from W to X.\n\n\nFrom David Loeffler:\n\n> I have been working on this as part of a Sage Days 16 project to reimplement abelian groups. The above patch:\n> \n> - adds new methods _element_class and _subquotient_class which can be overridden by derived classes\n\nLooks good to me. \n\n> - adds a new method has_canonical_map_to which does what is_submodule previously did, and changes is_submodule so it is true if and only if the canonical map exists *and is injective*.\n\ngood\n\n> - adjusts some things relating to gens, so derived classes can have generators which are not necessarily in Smith form, and made the necessary corresponding changes to hom. There are now separate methods smithform_gens and gens, and the \"internal\" uses of generators all call smithform_gens, so it is safe for derived classes to override gens.\n>\ngood, except I changed it to smith_form_gens (!)\n\n> I *haven't* changed the printing code, as I threatened to do last week -- on reflection I decided that elements comparing as equal and printing as unequal was just too confusing.\n\nYep.\n\n\nFrom John:\n\n>     adds new methods _element_class and _subquotient_class which can be overridden by derived classes\n> \n> In the docstring for _element_class, should \"creating subquotients\" say \"creating elements\"?\n\nDONE\n\n> \n>     changes is_submodule\n> \n> I like your change, but I would like is_submodule to have more documentation, saying (for example) that it returns True if self.V() is a submodule of A.V(), with self.W() equal to A.W().\n\n\nDONE\n\n> I don't have much of an opinion about this either way, but do you want to rename smithform_gens to _smithform_gens so it's less visible?\n\nAfter hearing how say Henri Cohen thinks about abelian groups, I think\nit is probably a good idea having smith_form_gens be user-visible.\nIt's an important function, and pretty canonical, and will be used\nfrom outside the class (that was the motivation for introducing it).\n\n> \n> For annihilator: the first line of the docstring ends a bit abruptly. Should this method return an actual ideal, not just an element of the ring?\n\nDONE, and added another doctest that illustrates the case when the\nannihilator is 0.  Yes, it should return an ideal, and I fixed it so\nit will.\n\nDavid said:\n> For annihilator, essentially it is just there so I can use it to do\n>  exponent for abelian groups, so I do want it to return an element.\n\nWell in the docstring you wrote *ideal*.  And it straightforward to\nget the generator of an ideal, so I made it an ideal.\n\nWe're going to generalize all this soon enough to general commutative\nbase rings (singular supports this sort of thing well, actually), and\nwhen we do so as much as possible we'll want to have a consistent API.\nSo we should make annihilator return an ideal.",
    "created_at": "2009-07-02T16:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46513",
    "user": "was"
}
```

RESPONSE TO ALL REFEREE COMMENTS IN WHICH EVERYTHING IS ADDRESSED.  A patch will be posted in a moment too.

> in inverse_image, is there any speed gain if you check whether the rank of the homomorphism is zero at the beginning? that is, change


DONE


> A very minor issue: In inverse_image, in the lines
>     if R.is_field(): 
>           # By solving, find lifts of each of the basis elements of V. 
>           # Each row of Y gives a linear combination of the basis for the domain 
>           # that maps to one of the basis elements V. 
>           C = A.solve_left(B) 
> change "Each row of Y" to "Each row of C"?

DONE

> 
> *******************************************
> 
> fgp_module.py:
> 
> the function FGP_Module: documentation should say what it returns: V/W as a f.g. R-module. For the inputs, V and W need to be free R-modules.

DONE

> _coerce_map_from_: I think that V/W should have a coercion from V, so testing isinstance(S, FGP_Module_class) won't work. More generally, you should have coercions from anything of the form V/W' to V/W, as long as W' is contained in W: that is, you should have coercions not just from submodules, but also from modules with canonical surjections onto V/W. (There may be many maps from V to V/W, but there is one *canonical* map, so I think there should be a coercion map.)

DONE

> in free_module.py, there is a __cmp__ method but not an __eq__ method, and here it's the other way around. Is this an issue? Do we have a policy about which one to use?

I think __eq__ is better since A < B suggest to a lot of people that
"A is contained in B", which isn't the case at all.  But I don't want
to potentially break the API of the general free_module code in this
patch.

> Here's a problem with is_submodule:
> 
> sage: V = FreeModule(ZZ, 1)
> sage: W = V.submodule([0*V.0])
> sage: W2 = V.submodule([2*V.0])
> sage: V/W  # isomorphic to Z
> Finitely generated module V/W over Integer Ring with invariants (0)
> sage: V/W2  # isomorphic to Z/2Z
> Finitely generated module V/W over Integer Ring with invariants (2)
> sage: (V/W).is_submodule(V/W2)
> True
> 
> This is because the implementation is wrong: if you want V/W to be a submodule of V'/W', then you want V to be a submodule of V', and the inclusion map should induce a surjection of W onto W' (hence an isomorphism between W and W' -- given an injection V --> V' which induces a map W --> W', the induced map must be an injection also). Should you change the end from
> 
>         return self.V().is_submodule(A.V()) and self.W().is_submodule(A.W())
> 
> to
> 
>         return self.V().is_submodule(A.V()) and self.W() == A.W()

DONE -- good change.  David Loeffler also found this issue and "fixed"
the code, but his fix was wrong too (it basically ignored the V's).

By the way, after making the above fix then running doctests, the
automated randomized testing code *did* find a bug in the image
command.  I fixed that by changing

        V = self._phi.image()

to

        V = self._phi.image() + self.codomain().W()

in the image method in fgp_morphism.py

> The docstring should be changed to reflect this, as should the doctests; in the existing doctests, I don't think that A is actually a submodule of Q. In the simpler (but somewhat analogous) situation of Z/2Z and Z/4Z, then although abstractly Z/2Z is a submodule of Z/4Z, the identity map Z --> Z does not induce the inclusion. The identity map Z --> Z induces an inclusion 4Z --> 2Z, which then induces a *surjection* Z/4Z --> Z/2Z.
> 
> Also, the first sentence of the docstring is wrong: it says "Return True if A is a submodule of self", and it should be "Return True if self is a submodule of A".

DONE

> 
> base_ring: delete the comment (# this will be done in __init__)?

DONE

> 
> _smith_form_: document the form of the output, or at least give a reference to smith_form from matrix2.pyx.

DONE.

Also, I changed all the smithform's to smith_form's, which David L. introduced. 

> invariants needs a docstring, not just doctests. (The term "invariants" is used frequently in fgp_module.py, but is never defined.) Document the argument "include_ones"?

done.

> 
> gens: in the docstring, change "lements" to "elements". Change it to "elements g0,...,gn of self"? (Add "of self"?)

DONE

> 
> is it worth changing "isinstance(x, FGP_Module_class)" to "is_FGP_Module(x)" many places in this file? (Otherwise, is "is_FGP_Module" used anywhere? We could delete it...)

Yes, DONE.

> I'm still working on this file, and I haven't looked at fgp_morphism or fgp_element in any detail yet (except to note that the in the docstring for FGP_Morphism, the comment "where the morphism doesn't extend to V1" needs to be rephrased). I'm going on a family trip tomorrow, though, so I may not have time to work on this for a few days.

done.




> My next installment: this finishes up with the file fgp_module.py.
> 
> coordinate_vector:
> 
> self.optimized() # computes T as side effect -- see above
> 
> Should say "see below", I think.

DONE

> 
> optimize: in the comments
> 
>         # Compute matrix X of linear transformation from self._V to V.
>         # This matrix X gives each basis element of self._V in terms
>         # of our new optimized V, modulo the W's.
> 
> Maybe "X" should be replaced by "T". If not, then "T" should be described, since it's cached, and so is presumably important.

DONE.  I called it X at one point, e.g., in my doodles, but changed to T.

> hom: if len(im_gens) == 0, then we can't use M.hom(...) to define the zero map to another module. Should we be able to? That is, should we be able to specify the codomain explicitly instead of the method using N = im_gens.universe()?

DONE -- You're right, yes, we should be able to.  I implemented hom wrong,
since hom should have an optional codomain parameter.  Fixed. 

> random_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?

I'm really not sure.  Conceptually if one constructs A = V/W, then it
is easiest to think of random_element as "Create a random element of
self=V/W, by creating a random element of V and reducing it modulo W."
The optimized() thing doesn't seem so canonical in terms of the given
input.  So I'm definitely not so sure.  Why do you think that would be
better? Efficiency?

> 
> right before random_fgp_module: ZZ has already been imported

DONE.


> random_fgp_module: say that R is optional, default ZZ

DONE

> ***********************
> 
> A general question: What's the obstruction to implementing this for modules over k[x], for k a field, or for general PIDs? This should be documented somewhere so interested people know what to work on.
> 

DONE - in the very top of fgp_module.py

> ***********************
> 
> I hope to get to the last two files soon.





> Okay, I'm done with my review. Earlier, I discussed everything except the files "fgp_element.py" and "fgp_morphism.py". The file "fgp_element.py" looks good to me. The file "fgp_morphism.py" is mostly good, but I have a few comments:
> 
> FGP_Morphism: as mentioned avove, need to fix the part of the docstring which says "where the morphism doesn't extend to V1"

DONE

> FGP_Morphism, __init__: can we delete the line
> 
>     from sage.matrix.all import diagonal_matrix

DONE

> 
> Also in __init__: Do you expect the error messages like "domain of phi must be V for MO" to ever appear? They are pretty cryptic -- if you haven't read the code, you won't know what "V for MO" means.

DONE.

> In __call__: when x is an FGP_Module, should you check that x is a submodule of self.domain() and return an appropriate error if not?

DONE, and I added some doctests. 

> I note that in "image", you call FGP_Module with check=False, but you don't have this in "kernel". Should you use check=False there, too?

DONE -- I've changed all the "internal checks" (not things passed in by the
user) to use the DEBUG flag in fgp_module.py.  Then one can uniformly
turn them all on/off.  I think it is best to leave all the checks on
for now, but turn them off after the code has been out in the wild for
a while, and work has gone into optimizing it (so far 0 work has gone
into optimization).

> 
> Should "preimage" be a synonym for "lift"? Or should there be a method "preimage" which acts like "lift" on elements, but also works on submodules?
> 

Hmm.  Actually, we should have at least inverse_image as a method on
morphisms of fgp modules, since that isn't there at all!  It was
important to add this method to fg modules, and should be easy on fgp
modules.  This provides the same functionality as preimage.  I think
preimage would be good to add, but then it should be added for fg free
modules too, so it's best to wait for another ticket and do it right. 

> In _coerce_map_from_: should there be a coercion from Hom(X,Y) to Hom(X,Z) if there is a coercion from Y to Z? Should there be a coercion from Hom(X,Y) to Hom(W,Y) if there is a coercion from W to X?
>

Yes, yes, but I don't know if this will work, since at least currently
that function returns bool rather than the actual map. Also, the same
should be added to free modules.  I think this would be better to do
on another ticket.

> Overall, this is very impressive, and it will be great to have this as part of Sage.


FOR NEW TICKETS:

* Add a method "preimage" that acts like "lift" on elements, but also works on submodules.

* There should be a coercion from Hom(X,Y) to Hom(X,Z) if there is a
  coercion from Y to Z. There should there be a coercion from Hom(X,Y) to
  Hom(W,Y) if there is a coercion from W to X.


From David Loeffler:

> I have been working on this as part of a Sage Days 16 project to reimplement abelian groups. The above patch:
> 
> - adds new methods _element_class and _subquotient_class which can be overridden by derived classes

Looks good to me. 

> - adds a new method has_canonical_map_to which does what is_submodule previously did, and changes is_submodule so it is true if and only if the canonical map exists *and is injective*.

good

> - adjusts some things relating to gens, so derived classes can have generators which are not necessarily in Smith form, and made the necessary corresponding changes to hom. There are now separate methods smithform_gens and gens, and the "internal" uses of generators all call smithform_gens, so it is safe for derived classes to override gens.
>
good, except I changed it to smith_form_gens (!)

> I *haven't* changed the printing code, as I threatened to do last week -- on reflection I decided that elements comparing as equal and printing as unequal was just too confusing.

Yep.


From John:

>     adds new methods _element_class and _subquotient_class which can be overridden by derived classes
> 
> In the docstring for _element_class, should "creating subquotients" say "creating elements"?

DONE

> 
>     changes is_submodule
> 
> I like your change, but I would like is_submodule to have more documentation, saying (for example) that it returns True if self.V() is a submodule of A.V(), with self.W() equal to A.W().


DONE

> I don't have much of an opinion about this either way, but do you want to rename smithform_gens to _smithform_gens so it's less visible?

After hearing how say Henri Cohen thinks about abelian groups, I think
it is probably a good idea having smith_form_gens be user-visible.
It's an important function, and pretty canonical, and will be used
from outside the class (that was the motivation for introducing it).

> 
> For annihilator: the first line of the docstring ends a bit abruptly. Should this method return an actual ideal, not just an element of the ring?

DONE, and added another doctest that illustrates the case when the
annihilator is 0.  Yes, it should return an ideal, and I fixed it so
it will.

David said:
> For annihilator, essentially it is just there so I can use it to do
>  exponent for abelian groups, so I do want it to return an element.

Well in the docstring you wrote *ideal*.  And it straightforward to
get the generator of an ideal, so I made it an ideal.

We're going to generalize all this soon enough to general commutative
base rings (singular supports this sort of thing well, actually), and
when we do so as much as possible we'll want to have a consistent API.
So we should make annihilator return an ideal.



---

archive/issue_comments_046514.json:
```json
{
    "body": "Attachment [trac_5882-full_ref_report-comments_addressed.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-full_ref_report-comments_addressed.patch) by was created at 2009-07-02 16:53:00",
    "created_at": "2009-07-02T16:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46514",
    "user": "was"
}
```

Attachment [trac_5882-full_ref_report-comments_addressed.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-full_ref_report-comments_addressed.patch) by was created at 2009-07-02 16:53:00



---

archive/issue_comments_046515.json:
```json
{
    "body": "Okay, this is great.  Positive review.\n\nThe ticket is a bit of a mess, though: davidloeffler's and was's most recent patches conflict.  I've taken the liberty of creating a single patch, containing all of the others, and merging the few differences between these two conflicting patches.  (I'm taking William's side on `annihilator` -- it should return an ideal.)  My patch also includes a few trivial fixes: two typos, and a rewording of the annihilator docstring so that the second line takes into account that it returns an ideal, not an element.  You can see my changes in \"trac_5882_delta.patch\"; this is for reference only.\n\nI think that the \"Author\" and \"Reviewer\" fields are filled in accurately.\n\nApply only \"trac_5882-all-in-one.patch\".",
    "created_at": "2009-07-02T22:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46515",
    "user": "jhpalmieri"
}
```

Okay, this is great.  Positive review.

The ticket is a bit of a mess, though: davidloeffler's and was's most recent patches conflict.  I've taken the liberty of creating a single patch, containing all of the others, and merging the few differences between these two conflicting patches.  (I'm taking William's side on `annihilator` -- it should return an ideal.)  My patch also includes a few trivial fixes: two typos, and a rewording of the annihilator docstring so that the second line takes into account that it returns an ideal, not an element.  You can see my changes in "trac_5882_delta.patch"; this is for reference only.

I think that the "Author" and "Reviewer" fields are filled in accurately.

Apply only "trac_5882-all-in-one.patch".



---

archive/issue_comments_046516.json:
```json
{
    "body": "Attachment [trac_5882-delta.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-delta.patch) by jhpalmieri created at 2009-07-02 22:00:44\n\nfor reference only",
    "created_at": "2009-07-02T22:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46516",
    "user": "jhpalmieri"
}
```

Attachment [trac_5882-delta.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-delta.patch) by jhpalmieri created at 2009-07-02 22:00:44

for reference only



---

archive/issue_comments_046517.json:
```json
{
    "body": "apply only this patch!",
    "created_at": "2009-07-02T22:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46517",
    "user": "jhpalmieri"
}
```

apply only this patch!



---

archive/issue_comments_046518.json:
```json
{
    "body": "Attachment [trac_5882-all-in-one.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-all-in-one.patch) by rlm created at 2009-07-02 22:15:52\n\nThere is one doctest failure:\n\n```\nsage -t  sage/modules/fg_pid/fgp_module.py\n**********************************************************************\nFile \"/space/rlm/sage-4.1.alpha3/devel/sage-main/sage/modules/fg_pid/fgp_module.py\", line 1453:\n    sage: hash(A)\nExpected nothing\nGot:\n    -7071641102956720018\n**********************************************************************\n```\n",
    "created_at": "2009-07-02T22:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46518",
    "user": "rlm"
}
```

Attachment [trac_5882-all-in-one.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882-all-in-one.patch) by rlm created at 2009-07-02 22:15:52

There is one doctest failure:

```
sage -t  sage/modules/fg_pid/fgp_module.py
**********************************************************************
File "/space/rlm/sage-4.1.alpha3/devel/sage-main/sage/modules/fg_pid/fgp_module.py", line 1453:
    sage: hash(A)
Expected nothing
Got:
    -7071641102956720018
**********************************************************************
```




---

archive/issue_comments_046519.json:
```json
{
    "body": "Sorry, that's what I get for only doctesting on a 32-bit machine.  Here's a patch.",
    "created_at": "2009-07-02T22:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46519",
    "user": "jhpalmieri"
}
```

Sorry, that's what I get for only doctesting on a 32-bit machine.  Here's a patch.



---

archive/issue_comments_046520.json:
```json
{
    "body": "Attachment [trac_5882_hash.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882_hash.patch) by jhpalmieri created at 2009-07-02 22:38:14",
    "created_at": "2009-07-02T22:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46520",
    "user": "jhpalmieri"
}
```

Attachment [trac_5882_hash.patch](tarball://root/attachments/some-uuid/ticket5882/trac_5882_hash.patch) by jhpalmieri created at 2009-07-02 22:38:14



---

archive/issue_comments_046521.json:
```json
{
    "body": "Re William's comments:\n\n>> random_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?\n>\n> I'm really not sure. Conceptually if one constructs A = V/W, then it is easiest to think of random_element as \"Create a random element of self=V/W, by creating a random element of V and reducing it modulo W.\" The optimized() thing doesn't seem so canonical in terms of the given input. So I'm definitely not so sure. Why do you think that would be better? Efficiency?\n\nBecause when I wrote that, I was having a mathematical brain freeze.  It's fine the way it is.\n\nThe documentation builds fine, by the way.",
    "created_at": "2009-07-02T22:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46521",
    "user": "jhpalmieri"
}
```

Re William's comments:

>> random_element: wouldn't it be better to pick a random element from self.optimized()[0]._V?
>
> I'm really not sure. Conceptually if one constructs A = V/W, then it is easiest to think of random_element as "Create a random element of self=V/W, by creating a random element of V and reducing it modulo W." The optimized() thing doesn't seem so canonical in terms of the given input. So I'm definitely not so sure. Why do you think that would be better? Efficiency?

Because when I wrote that, I was having a mathematical brain freeze.  It's fine the way it is.

The documentation builds fine, by the way.



---

archive/issue_comments_046522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T23:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5882#issuecomment-46522",
    "user": "rlm"
}
```

Resolution: fixed
