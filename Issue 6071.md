# Issue 6071: Weight 1 Eisenstein series

archive/issues_006071.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  was\n\nComputing weight 1 cusp forms is hard (cf. #2330), but computing weight 1 Eisenstein series isn't; only very slight modifications are needed to the code we already have.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6071\n\n",
    "created_at": "2009-05-18T15:20:16Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Weight 1 Eisenstein series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6071",
    "user": "davidloeffler"
}
```
Assignee: davidloeffler

CC:  was

Computing weight 1 cusp forms is hard (cf. #2330), but computing weight 1 Eisenstein series isn't; only very slight modifications are needed to the code we already have.

Issue created by migration from https://trac.sagemath.org/ticket/6071





---

archive/issue_comments_048323.json:
```json
{
    "body": "patch against 4.0.alpha0",
    "created_at": "2009-05-18T15:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48323",
    "user": "davidloeffler"
}
```

patch against 4.0.alpha0



---

archive/issue_comments_048324.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-18T15:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48324",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048325.json:
```json
{
    "body": "Attachment [trac_6071.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071.patch) by davidloeffler created at 2009-05-18 15:23:12",
    "created_at": "2009-05-18T15:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48325",
    "user": "davidloeffler"
}
```

Attachment [trac_6071.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071.patch) by davidloeffler created at 2009-05-18 15:23:12



---

archive/issue_comments_048326.json:
```json
{
    "body": "Changing keywords from \"\" to \"eisenstein series\".",
    "created_at": "2009-05-18T15:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48326",
    "user": "davidloeffler"
}
```

Changing keywords from "" to "eisenstein series".



---

archive/issue_comments_048327.json:
```json
{
    "body": "I think I am too ignorant about weight 1 forms to review this honestly.  All I can say is that there's a typo on line 285 of the patch (in a comment) -- chi <--> psi?",
    "created_at": "2009-05-30T16:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48327",
    "user": "cremona"
}
```

I think I am too ignorant about weight 1 forms to review this honestly.  All I can say is that there's a typo on line 285 of the patch (in a comment) -- chi <--> psi?



---

archive/issue_comments_048328.json:
```json
{
    "body": "You are right about the comment typo, I will do a micro-patch to fix it when the pile of exam scripts on my desk has decreased far enough.\n\nI am adding William to the CC list, since he certainly knows about weight 1 forms.",
    "created_at": "2009-06-08T08:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48328",
    "user": "davidloeffler"
}
```

You are right about the comment typo, I will do a micro-patch to fix it when the pile of exam scripts on my desk has decreased far enough.

I am adding William to the CC list, since he certainly knows about weight 1 forms.



---

archive/issue_comments_048329.json:
```json
{
    "body": "REFEREE REPORT:\n\nThere is not a single example in this patch of computing an Eisenstein series of weight 1.  Can you add some examples?\n\n\nAlso, this seems very very wrong to me:\n\n```\n \t361\t        try: \n \t362\t            d = self.dimension() \n \t363\t        except NotImplementedError: \n \t364\t            d = self._dim_eisenstein() \n \t365\t        self.__module = free_module.VectorSpace(self.base_ring(), d) \n```\n\n\nYou've changed the dimension for *ambient* modular forms spaces to return the dimension of the Eisenstein subspace in case the dimension function isn't implemented.  What if I take a space with both a cuspidal and eisenstein part -- it'll just say the dimension of the whole space is the dimension of the eisenstein subspace. Somehow I have the feeling you made this change to get things to work in a special case of interest to you, not worrying that you might break other cases.",
    "created_at": "2009-06-20T14:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48329",
    "user": "was"
}
```

REFEREE REPORT:

There is not a single example in this patch of computing an Eisenstein series of weight 1.  Can you add some examples?


Also, this seems very very wrong to me:

```
 	361	        try: 
 	362	            d = self.dimension() 
 	363	        except NotImplementedError: 
 	364	            d = self._dim_eisenstein() 
 	365	        self.__module = free_module.VectorSpace(self.base_ring(), d) 
```


You've changed the dimension for *ambient* modular forms spaces to return the dimension of the Eisenstein subspace in case the dimension function isn't implemented.  What if I take a space with both a cuspidal and eisenstein part -- it'll just say the dimension of the whole space is the dimension of the eisenstein subspace. Somehow I have the feeling you made this change to get things to work in a special case of interest to you, not worrying that you might break other cases.



---

archive/issue_comments_048330.json:
```json
{
    "body": "Fair point; I will add some more examples.\n\nFor your second point: if you install the patch and try it out, you'll see that (for instance) ModularForms(Gamma1(23), 1) will raise a NotImplementedError, as it should, but EisensteinForms(Gamma1(23),1) will work. The thing that you describe as \"very very wrong\" is forced by the general design we have for modular forms spaces, which insists that Eisenstein forms are always a subspace of an ambient ModularForms space spanned by the *last* few basis vectors. The point of the workaround above is that when we can't find the dimension of the wt 1 cusp forms, we pretend that there aren't any for the purposes of working with Eisenstein series, but intercept any attempt to create the whole modular forms space (or its cuspidal part) by raising an error.\n\nEven once we have proper code for calculating weight 1 cusp forms this will still be an issue, since for large N calculating dim S_1(Gamma_1(N)) is a serious and time-consuming calculation that we don't want to be forced to do solely in order to know how many zeros to stick at the front of the Eisenstein series.",
    "created_at": "2009-06-20T20:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48330",
    "user": "davidloeffler"
}
```

Fair point; I will add some more examples.

For your second point: if you install the patch and try it out, you'll see that (for instance) ModularForms(Gamma1(23), 1) will raise a NotImplementedError, as it should, but EisensteinForms(Gamma1(23),1) will work. The thing that you describe as "very very wrong" is forced by the general design we have for modular forms spaces, which insists that Eisenstein forms are always a subspace of an ambient ModularForms space spanned by the *last* few basis vectors. The point of the workaround above is that when we can't find the dimension of the wt 1 cusp forms, we pretend that there aren't any for the purposes of working with Eisenstein series, but intercept any attempt to create the whole modular forms space (or its cuspidal part) by raising an error.

Even once we have proper code for calculating weight 1 cusp forms this will still be an issue, since for large N calculating dim S_1(Gamma_1(N)) is a serious and time-consuming calculation that we don't want to be forced to do solely in order to know how many zeros to stick at the front of the Eisenstein series.



---

archive/issue_comments_048331.json:
```json
{
    "body": "For what it's worth: that sounds like a good explanation.  Perhaps when you put the examples in you can include some which illustrate those points too.",
    "created_at": "2009-06-20T21:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48331",
    "user": "cremona"
}
```

For what it's worth: that sounds like a good explanation.  Perhaps when you put the examples in you can include some which illustrate those points too.



---

archive/issue_comments_048332.json:
```json
{
    "body": "Attachment [trac_6071-weight1_eisenstein.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071-weight1_eisenstein.patch) by davidloeffler created at 2009-06-25 21:40:41\n\nReplaces previous patch",
    "created_at": "2009-06-25T21:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48332",
    "user": "davidloeffler"
}
```

Attachment [trac_6071-weight1_eisenstein.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071-weight1_eisenstein.patch) by davidloeffler created at 2009-06-25 21:40:41

Replaces previous patch



---

archive/issue_comments_048333.json:
```json
{
    "body": "REFEREE REPORT:\n\n* This comment must be changed, and I've changed it in the attached referee patch:\n\n\n```\nFile:           /scratch/wstein/build/sage-4.1/local/lib/python2.6/site-packages/sage/modular/modform/ambient.py\nDefinition:     M.module(self)\nDocstring:\n    \n            Return the underlying free module corresponding to this space of\n            modular forms. This is a free module (viewed as a tuple space) of\n            the same dimension as this space over the same base ring.\n```\n\nThis is because of the following example:\n\n```\nsage: M = ModularForms(Gamma1(23), 1,prec=20); M\nModular Forms space of dimension (unknown) for Congruence Subgroup Gamma1(23) of weight 1 over Rational Field\nsage: M.module()\nVector space of dimension 11 over Rational Field\n```\n\nso it is now no longer the case that `M.module().dimension() == M.dimension()` as is stated in the docstring.\nThe change should just be to state that \"If the dimension of M can be computed, then [same as before].  Otherwise, the dimension of M.module() may be smaller.  E.g., in the case of weight 1 forms...\"  Then include an example in the docstring that illustrates this. \n\n\nThis ticket should be changed to \"[with patch; positive review]\" as soon as somebody else signs off on the referee patch I've attached.",
    "created_at": "2009-07-21T04:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48333",
    "user": "was"
}
```

REFEREE REPORT:

* This comment must be changed, and I've changed it in the attached referee patch:


```
File:           /scratch/wstein/build/sage-4.1/local/lib/python2.6/site-packages/sage/modular/modform/ambient.py
Definition:     M.module(self)
Docstring:
    
            Return the underlying free module corresponding to this space of
            modular forms. This is a free module (viewed as a tuple space) of
            the same dimension as this space over the same base ring.
```

This is because of the following example:

```
sage: M = ModularForms(Gamma1(23), 1,prec=20); M
Modular Forms space of dimension (unknown) for Congruence Subgroup Gamma1(23) of weight 1 over Rational Field
sage: M.module()
Vector space of dimension 11 over Rational Field
```

so it is now no longer the case that `M.module().dimension() == M.dimension()` as is stated in the docstring.
The change should just be to state that "If the dimension of M can be computed, then [same as before].  Otherwise, the dimension of M.module() may be smaller.  E.g., in the case of weight 1 forms..."  Then include an example in the docstring that illustrates this. 


This ticket should be changed to "[with patch; positive review]" as soon as somebody else signs off on the referee patch I've attached.



---

archive/issue_comments_048334.json:
```json
{
    "body": "Attachment [trac_6071-referee.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071-referee.patch) by davidloeffler created at 2009-07-21 07:55:17\n\nFair point. The new patch looks fine to me, so positive review.",
    "created_at": "2009-07-21T07:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48334",
    "user": "davidloeffler"
}
```

Attachment [trac_6071-referee.patch](tarball://root/attachments/some-uuid/ticket6071/trac_6071-referee.patch) by davidloeffler created at 2009-07-21 07:55:17

Fair point. The new patch looks fine to me, so positive review.



---

archive/issue_comments_048335.json:
```json
{
    "body": "Merged:\n1. `trac_6071-weight1_eisenstein.patch`\n2. `trac_6071-referee.patch`",
    "created_at": "2009-07-23T03:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48335",
    "user": "mvngu"
}
```

Merged:
1. `trac_6071-weight1_eisenstein.patch`
2. `trac_6071-referee.patch`



---

archive/issue_comments_048336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T03:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6071",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6071#issuecomment-48336",
    "user": "mvngu"
}
```

Resolution: fixed
