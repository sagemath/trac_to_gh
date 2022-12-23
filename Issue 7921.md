# Issue 7921: Categories for extension types via __getattr___

Issue created by migration from https://trac.sagemath.org/ticket/7921

Original creator: nthiery

Original creation time: 2010-01-13 16:05:49

Assignee: nthiery

CC:  sage-combinat mhansen robertwb roed

With this patch, all parents and elements can inherit code from categories. This is implemented via __getattr__.


---

Comment by nthiery created at 2010-01-13 23:12:25

All tests seem to pass with it on 4.3; I still need to double check a couple things. It does change things in many places; so the best would be to integrate it in the early phase of 4.3.2 before it rots away.

Early feedback welcome!


---

Comment by nthiery created at 2010-01-13 23:12:25

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-01-14 23:09:02

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-01-14 23:11:35

The patch passes all tests with sage 4.3 + sage-combinat patches merged in 4.3.1 on my machine. I'll run sage -t -long tonight and report.


---

Comment by nthiery created at 2010-01-16 12:40:43

Hi Robert; I improved a bit TestSuite to catch more. Should I add a second patch to this one,
or make it a separate ticket?


---

Comment by nthiery created at 2010-01-17 20:52:35

Robert: please let me know if I should open a separate ticket for the second patch. Florent can probably review it if this can save you some time.


---

Attachment

Patch 2: stronger category tests


---

Comment by robertwb created at 2010-01-19 14:42:52

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

Comment by robertwb created at 2010-01-19 14:42:52

Changing status from needs_review to needs_info.


---

Comment by robertwb created at 2010-01-19 14:49:43

I didn't look much at the second patch, but this should almost certainly be a second ticket.


---

Comment by nthiery created at 2010-01-19 18:11:23

Replying to [comment:8 robertwb]:
> I didn't look much at the second patch, but this should almost certainly be a second ticket. 

Ok, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.


---

Comment by nthiery created at 2010-01-19 18:11:23

Changing status from needs_info to needs_review.


---

Comment by nthiery created at 2010-01-19 18:17:30

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

Comment by nthiery created at 2010-01-19 18:30:51

Replying to [comment:9 nthiery]:
> Replying to [comment:8 robertwb]:
> > I didn't look much at the second patch, but this should almost certainly be a second ticket. 
> 
> Ok, will do. Florent volunteered to review it, since it's mostly about testsuites and categories.

This is now #8001 (darn, missed, that was sooo close from #8000!)


---

Comment by robertwb created at 2010-01-19 20:33:11

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-19 20:33:11

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

Comment by nthiery created at 2010-01-19 23:02:07

Thanks Robert for the quick review! I am looking forward feedback from practical uses :-)

Thanks also for the pointer to #383


---

Comment by nthiery created at 2010-01-22 21:53:54

Rebased and updated one doctest for 4.3.1 + micro fix in the primer. Apply only this one.


---

Comment by mvngu created at 2010-01-22 22:57:33

Resolution: fixed


---

Attachment

Merged [trac_7921-categories_for_extension_types-nt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7921/trac_7921-categories_for_extension_types-nt.patch).


---

Comment by saraedum created at 2014-05-10 19:15:06

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

Comment by nthiery created at 2014-05-10 22:05:55

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

Comment by saraedum created at 2014-05-10 23:07:26

Thanks for your explanation.
