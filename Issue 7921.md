# Issue 7921: Categories for extension types via __getattr___

archive/issues_007921.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @mwhansen @robertwb @roed314\n\nWith this patch, all parents and elements can inherit code from categories. This is implemented via __getattr__.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7921\n\n",
    "created_at": "2010-01-13T16:05:49Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Categories for extension types via __getattr___",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7921",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @mwhansen @robertwb @roed314

With this patch, all parents and elements can inherit code from categories. This is implemented via __getattr__.

Issue created by migration from https://trac.sagemath.org/ticket/7921





---

archive/issue_comments_068792.json:
```json
{
    "body": "All tests seem to pass with it on 4.3; I still need to double check a couple things. It does change things in many places; so the best would be to integrate it in the early phase of 4.3.2 before it rots away.\n\nEarly feedback welcome!",
    "created_at": "2010-01-13T23:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68792",
    "user": "https://github.com/nthiery"
}
```

All tests seem to pass with it on 4.3; I still need to double check a couple things. It does change things in many places; so the best would be to integrate it in the early phase of 4.3.2 before it rots away.

Early feedback welcome!



---

archive/issue_comments_068793.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-13T23:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68793",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068794.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-14T23:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68794",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068795.json:
```json
{
    "body": "The patch passes all tests with sage 4.3 + sage-combinat patches merged in 4.3.1 on my machine. I'll run sage -t -long tonight and report.",
    "created_at": "2010-01-14T23:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68795",
    "user": "https://github.com/nthiery"
}
```

The patch passes all tests with sage 4.3 + sage-combinat patches merged in 4.3.1 on my machine. I'll run sage -t -long tonight and report.



---

archive/issue_comments_068796.json:
```json
{
    "body": "Hi Robert; I improved a bit TestSuite to catch more. Should I add a second patch to this one,\nor make it a separate ticket?",
    "created_at": "2010-01-16T12:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68796",
    "user": "https://github.com/nthiery"
}
```

Hi Robert; I improved a bit TestSuite to catch more. Should I add a second patch to this one,
or make it a separate ticket?



---

archive/issue_comments_068797.json:
```json
{
    "body": "Robert: please let me know if I should open a separate ticket for the second patch. Florent can probably review it if this can save you some time.",
    "created_at": "2010-01-17T20:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68797",
    "user": "https://github.com/nthiery"
}
```

Robert: please let me know if I should open a separate ticket for the second patch. Florent can probably review it if this can save you some time.



---

archive/issue_comments_068798.json:
```json
{
    "body": "Attachment [categories_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket7921/categories_testsuite-nt.patch) by @nthiery created at 2010-01-17 20:59:52\n\nPatch 2: stronger category tests",
    "created_at": "2010-01-17T20:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68798",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories_testsuite-nt.patch](tarball://root/attachments/some-uuid/ticket7921/categories_testsuite-nt.patch) by @nthiery created at 2010-01-17 20:59:52

Patch 2: stronger category tests



---

archive/issue_comments_068799.json:
```json
{
    "body": "The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. \n\nsage/groups/group.pyx\n\n```\n    def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? \n```\n\n\nGroups are not yet converted over to the new coercion model, and are a mess in general. \n\nIn sage/modular/abvar/abvar.py, you removed the method but kept the docstring floating there. Those tests should be kept, but probably not put there. \n\nsage/modules/free_module.py - It'd be good to test the category of non-vector space.\n\nCould you explain the changes to sage/structure/sage_object.pyx?",
    "created_at": "2010-01-19T14:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68799",
    "user": "https://github.com/robertwb"
}
```

The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. 

sage/groups/group.pyx

```
    def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? 
```


Groups are not yet converted over to the new coercion model, and are a mess in general. 

In sage/modular/abvar/abvar.py, you removed the method but kept the docstring floating there. Those tests should be kept, but probably not put there. 

sage/modules/free_module.py - It'd be good to test the category of non-vector space.

Could you explain the changes to sage/structure/sage_object.pyx?



---

archive/issue_comments_068800.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-19T14:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68800",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_068801.json:
```json
{
    "body": "I didn't look much at the second patch, but this should almost certainly be a second ticket.",
    "created_at": "2010-01-19T14:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68801",
    "user": "https://github.com/robertwb"
}
```

I didn't look much at the second patch, but this should almost certainly be a second ticket.



---

archive/issue_comments_068802.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> I didn't look much at the second patch, but this should almost certainly be a second ticket. \n\nOk, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.",
    "created_at": "2010-01-19T18:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68802",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 robertwb]:
> I didn't look much at the second patch, but this should almost certainly be a second ticket. 

Ok, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.



---

archive/issue_comments_068803.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-01-19T18:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68803",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_068804.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. \n\nWell, I actually only added 2/3 of them, mostly as an attempt to catch possible introduced issues. The others were already there, and needed to be updated due to all the new (often failing) tests coming from categories.\n\n> sage/groups/group.pyx\n> {{{\n>     def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? \n> }}}\n> \n> Groups are not yet converted over to the new coercion model, and are a mess in general.\n\nOk. Shouldn't this def be removed, so as not to prevent groups inheriting from Group to progressively get converted to the coercion model? Sure, that should be a separate patch. As for the comment above: I just can't prevent myself from adding comments in the code when I stumble on strange stuff. I can remove it if you prefer.\n\n> In sage/modular/abvar/abvar.py, you removed the method but kept the docstring floating there. Those tests should be kept, but probably not put there. \n\nOops, fixed.\n\n> sage/modules/free_module.py - It'd be good to test the category of non-vector space.\n\nDone.\n\n> Could you explain the changes to sage/structure/sage_object.pyx?\n\nI improved the description on top of the patch, including a comment about this.",
    "created_at": "2010-01-19T18:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68804",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:7 robertwb]:
> The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. 

Well, I actually only added 2/3 of them, mostly as an attempt to catch possible introduced issues. The others were already there, and needed to be updated due to all the new (often failing) tests coming from categories.

> sage/groups/group.pyx
> {{{
>     def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? 
> }}}
> 
> Groups are not yet converted over to the new coercion model, and are a mess in general.

Ok. Shouldn't this def be removed, so as not to prevent groups inheriting from Group to progressively get converted to the coercion model? Sure, that should be a separate patch. As for the comment above: I just can't prevent myself from adding comments in the code when I stumble on strange stuff. I can remove it if you prefer.

> In sage/modular/abvar/abvar.py, you removed the method but kept the docstring floating there. Those tests should be kept, but probably not put there. 

Oops, fixed.

> sage/modules/free_module.py - It'd be good to test the category of non-vector space.

Done.

> Could you explain the changes to sage/structure/sage_object.pyx?

I improved the description on top of the patch, including a comment about this.



---

archive/issue_comments_068805.json:
```json
{
    "body": "Replying to [comment:9 nthiery]:\n> Replying to [comment:8 robertwb]:\n> > I didn't look much at the second patch, but this should almost certainly be a second ticket. \n> \n> Ok, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.\n\nThis is now #8001 (darn, missed, that was sooo close from #8000!)",
    "created_at": "2010-01-19T18:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68805",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 nthiery]:
> Replying to [comment:8 robertwb]:
> > I didn't look much at the second patch, but this should almost certainly be a second ticket. 
> 
> Ok, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.

This is now #8001 (darn, missed, that was sooo close from #8000!)



---

archive/issue_comments_068806.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T20:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68806",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068807.json:
```json
{
    "body": "Replying to [comment:10 nthiery]:\n> Replying to [comment:7 robertwb]:\n> > The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. \n> \n> Well, I actually only added 2/3 of them, mostly as an attempt to catch possible introduced issues. The others were already there, and needed to be updated due to all the new (often failing) tests coming from categories.\n\nOK. \n\n> > sage/groups/group.pyx\n> > {{{\n> >     def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? \n> > }}}\n> > \n> > Groups are not yet converted over to the new coercion model, and are a mess in general.\n> \n> Ok. Shouldn't this def be removed, so as not to prevent groups inheriting from Group to progressively get converted to the coercion model? \n\nEventually, for sure. \n\n> Sure, that should be a separate patch. As for the comment above: I just can't prevent myself from adding comments in the code when I stumble on strange stuff. I can remove it if you prefer.\n\nNo, comments like this are good. I was just somewhat answering your question. \n\n> > Could you explain the changes to sage/structure/sage_object.pyx?\n> \n> I improved the description on top of the patch, including a comment about this.\n\nThanks. Look forward to being able to do stuff like this. On a somewhat related note, you might be interested in the binop decorator at #383.",
    "created_at": "2010-01-19T20:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68807",
    "user": "https://github.com/robertwb"
}
```

Replying to [comment:10 nthiery]:
> Replying to [comment:7 robertwb]:
> > The attribute lookup code looks good. Most of the other changes are minor, though changing loads/dumps to running tests is an independent change is seems. 
> 
> Well, I actually only added 2/3 of them, mostly as an attempt to catch possible introduced issues. The others were already there, and needed to be updated due to all the new (often failing) tests coming from categories.

OK. 

> > sage/groups/group.pyx
> > {{{
> >     def __call__(self, x): # NT: doesn't this get in the way of the coercion mechanism? 
> > }}}
> > 
> > Groups are not yet converted over to the new coercion model, and are a mess in general.
> 
> Ok. Shouldn't this def be removed, so as not to prevent groups inheriting from Group to progressively get converted to the coercion model? 

Eventually, for sure. 

> Sure, that should be a separate patch. As for the comment above: I just can't prevent myself from adding comments in the code when I stumble on strange stuff. I can remove it if you prefer.

No, comments like this are good. I was just somewhat answering your question. 

> > Could you explain the changes to sage/structure/sage_object.pyx?
> 
> I improved the description on top of the patch, including a comment about this.

Thanks. Look forward to being able to do stuff like this. On a somewhat related note, you might be interested in the binop decorator at #383.



---

archive/issue_comments_068808.json:
```json
{
    "body": "Thanks Robert for the quick review! I am looking forward feedback from practical uses :-)\n\nThanks also for the pointer to #383",
    "created_at": "2010-01-19T23:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68808",
    "user": "https://github.com/nthiery"
}
```

Thanks Robert for the quick review! I am looking forward feedback from practical uses :-)

Thanks also for the pointer to #383



---

archive/issue_comments_068809.json:
```json
{
    "body": "Rebased and updated one doctest for 4.3.1 + micro fix in the primer. Apply only this one.",
    "created_at": "2010-01-22T21:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68809",
    "user": "https://github.com/nthiery"
}
```

Rebased and updated one doctest for 4.3.1 + micro fix in the primer. Apply only this one.



---

archive/issue_comments_068810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-22T22:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008135.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-22T22:57:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7921#event-8135"
}
```



---

archive/issue_comments_068811.json:
```json
{
    "body": "Attachment [trac_7921-categories_for_extension_types-nt.patch](tarball://root/attachments/some-uuid/ticket7921/trac_7921-categories_for_extension_types-nt.patch) by mvngu created at 2010-01-22 22:57:33\n\nMerged [trac_7921-categories_for_extension_types-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7921/trac_7921-categories_for_extension_types-nt.patch).",
    "created_at": "2010-01-22T22:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7921-categories_for_extension_types-nt.patch](tarball://root/attachments/some-uuid/ticket7921/trac_7921-categories_for_extension_types-nt.patch) by mvngu created at 2010-01-22 22:57:33

Merged [trac_7921-categories_for_extension_types-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7921/trac_7921-categories_for_extension_types-nt.patch).



---

archive/issue_comments_068812.json:
```json
{
    "body": "I have a question regarding this old ticket. The following fails:\n\n```\nsage: a = ModularForms(11,4).an_element()\nsage: a._test_category()\n```\n\nThe reason for this is that `a` is not an extension class so `_test_category` expects that the type of `a` inherits from `a.parent().category().element_class`. Now if I try to do such inheritance\n\n```\nclass HeckeModuleElement(sage.modules.module_element.ModuleElement, HeckeModules.element_class):\n```\n\nI get a\n\n```\nmetaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its base\n```\n\n\nAnyway, I'm getting the feeling that such inheritance does not happen anywhere (partly because most element classes are extension classes). The methods from the element_class are available anyway (just like for extension classes). So is it safe to remove this check from `_test_category`? I.e. should we change\n\n```\nif not is_extension_type(self.__class__):\n    # For usual Python classes, that should be done with\n    # standard inheritance\n    tester.assert_(isinstance(self, self.parent().category().element_class))\nelse:\n    # For extension types we just check that inheritance\n    # occurs on a dummy attribute of Sets().ElementMethods\n    tester.assert_(hasattr(self, \"_dummy_attribute\"))\n```\n\ninto\n\n```\n    tester.assert_(hasattr(self, \"_dummy_attribute\"))\n```\n",
    "created_at": "2014-05-10T19:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68812",
    "user": "https://github.com/saraedum"
}
```

I have a question regarding this old ticket. The following fails:

```
sage: a = ModularForms(11,4).an_element()
sage: a._test_category()
```

The reason for this is that `a` is not an extension class so `_test_category` expects that the type of `a` inherits from `a.parent().category().element_class`. Now if I try to do such inheritance

```
class HeckeModuleElement(sage.modules.module_element.ModuleElement, HeckeModules.element_class):
```

I get a

```
metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its base
```


Anyway, I'm getting the feeling that such inheritance does not happen anywhere (partly because most element classes are extension classes). The methods from the element_class are available anyway (just like for extension classes). So is it safe to remove this check from `_test_category`? I.e. should we change

```
if not is_extension_type(self.__class__):
    # For usual Python classes, that should be done with
    # standard inheritance
    tester.assert_(isinstance(self, self.parent().category().element_class))
else:
    # For extension types we just check that inheritance
    # occurs on a dummy attribute of Sets().ElementMethods
    tester.assert_(hasattr(self, "_dummy_attribute"))
```

into

```
    tester.assert_(hasattr(self, "_dummy_attribute"))
```




---

archive/issue_comments_068813.json:
```json
{
    "body": "Replying to [comment:15 saraedum]:\n> I have a question regarding this old ticket. The following fails:\n> {{{\n> sage: a = ModularForms(11,4).an_element()\n> sage: a._test_category()\n> }}}\n> The reason for this is that `a` is not an extension class so `_test_category` expects that the type of `a` inherits from `a.parent().category().element_class`. Now if I try to do such inheritance\n> {{{\n> class HeckeModuleElement(sage.modules.module_element.ModuleElement, HeckeModules.element_class):\n> }}}\n> I get a\n> {{{\n> metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its base\n> }}}\n\nIf it's not an extension type, it really should inherit `a.parent().category().element_class`.\nExcept in complicated cases (e.g. parents whose elements can belong to\nseveral classes), this is taken care of automatically if a category is specified to\n`Parent.__init__`; otherwise one needs to use manually\n`_make_element_class`. See sage.categories.primer (better with #10963 applied) and the\ndocumentation of Category for details.\n\nMost likely the issue here is that the category is not specified\nproperly.\n\n> Anyway, I'm getting the feeling that such inheritance does not happen anywhere (partly because most element classes are extension classes).\n\nMost of my bread and butter element classes are *not* extension\nclasses :-) Just for one example:\n\n\n```\nsage: x = CombinatorialFreeModule(QQ, [1,2,3]).an_element()\nsage: x.__class__\n<class 'sage.combinat.free_module.CombinatorialFreeModule_with_category.element_class'>\nsage: x.__class__.__bases__\n(sage.combinat.free_module.CombinatorialFreeModuleElement,\n sage.categories.vector_spaces.VectorSpaces.WithBasis.element_class)\n```\n\n\n> So is it safe to remove this check from `_test_category`?\n\nPlease don't: so far failures here have always pointed to actual bugs.\n\nCheers,\n                            Nicolas",
    "created_at": "2014-05-10T22:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68813",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:15 saraedum]:
> I have a question regarding this old ticket. The following fails:
> {{{
> sage: a = ModularForms(11,4).an_element()
> sage: a._test_category()
> }}}
> The reason for this is that `a` is not an extension class so `_test_category` expects that the type of `a` inherits from `a.parent().category().element_class`. Now if I try to do such inheritance
> {{{
> class HeckeModuleElement(sage.modules.module_element.ModuleElement, HeckeModules.element_class):
> }}}
> I get a
> {{{
> metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its base
> }}}

If it's not an extension type, it really should inherit `a.parent().category().element_class`.
Except in complicated cases (e.g. parents whose elements can belong to
several classes), this is taken care of automatically if a category is specified to
`Parent.__init__`; otherwise one needs to use manually
`_make_element_class`. See sage.categories.primer (better with #10963 applied) and the
documentation of Category for details.

Most likely the issue here is that the category is not specified
properly.

> Anyway, I'm getting the feeling that such inheritance does not happen anywhere (partly because most element classes are extension classes).

Most of my bread and butter element classes are *not* extension
classes :-) Just for one example:


```
sage: x = CombinatorialFreeModule(QQ, [1,2,3]).an_element()
sage: x.__class__
<class 'sage.combinat.free_module.CombinatorialFreeModule_with_category.element_class'>
sage: x.__class__.__bases__
(sage.combinat.free_module.CombinatorialFreeModuleElement,
 sage.categories.vector_spaces.VectorSpaces.WithBasis.element_class)
```


> So is it safe to remove this check from `_test_category`?

Please don't: so far failures here have always pointed to actual bugs.

Cheers,
                            Nicolas



---

archive/issue_comments_068814.json:
```json
{
    "body": "Thanks for your explanation.",
    "created_at": "2014-05-10T23:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7921#issuecomment-68814",
    "user": "https://github.com/saraedum"
}
```

Thanks for your explanation.
