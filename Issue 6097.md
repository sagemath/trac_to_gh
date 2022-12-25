# Issue 6097: Implements a mantra for declaring abstract methods

archive/issues_006097.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: abstract methods\n\nThis patch implements a decorator tha can be used to declare a method\nthat should be implemented by derived classes. This declaration should\ntypically include documentation for the specification for this method.\n\nThe purpose is to enforce a consistent and visual mantra for such\ndeclarations. In the long run, this will be used for automated\nsystematic signature checks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6097\n\n",
    "created_at": "2009-05-21T01:19:28Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Implements a mantra for declaring abstract methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6097",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: abstract methods

This patch implements a decorator tha can be used to declare a method
that should be implemented by derived classes. This declaration should
typically include documentation for the specification for this method.

The purpose is to enforce a consistent and visual mantra for such
declarations. In the long run, this will be used for automated
systematic signature checks.

Issue created by migration from https://trac.sagemath.org/ticket/6097





---

archive/issue_comments_048514.json:
```json
{
    "body": "> Feedback and suggestion for improvement on this policy are welcome! \n\n\n```\nsage: x = A() \nsage: x.my_method?\nBOOM!\n```\n\nThis must be fixed by improving sageinspect.  That should be easy.\n\n1) Trick to catch.\n\n2) How do you get the docs on my_method though?",
    "created_at": "2009-05-21T02:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48514",
    "user": "https://github.com/williamstein"
}
```

> Feedback and suggestion for improvement on this policy are welcome! 


```
sage: x = A() 
sage: x.my_method?
BOOM!
```

This must be fixed by improving sageinspect.  That should be easy.

1) Trick to catch.

2) How do you get the docs on my_method though?



---

archive/issue_comments_048515.json:
```json
{
    "body": "Attachment [abstract_method-6097-nt.patch](tarball://root/attachments/some-uuid/ticket6097/abstract_method-6097-nt.patch) by @nthiery created at 2009-05-21 23:41:43",
    "created_at": "2009-05-21T23:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48515",
    "user": "https://github.com/nthiery"
}
```

Attachment [abstract_method-6097-nt.patch](tarball://root/attachments/some-uuid/ticket6097/abstract_method-6097-nt.patch) by @nthiery created at 2009-05-21 23:41:43



---

archive/issue_comments_048516.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-21T23:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48516",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048517.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> > Feedback and suggestion for improvement on this policy are welcome! \n\n> \n> {{{\n> sage: x = A() \n> sage: x.my_method?\n> BOOM!\n> }}}\n> \n> This must be fixed by improving sageinspect.  That should be easy.\n> \n> 1) Trick to catch.\n> \n> 2) How do you get the docs on my_method though?\n\n\nI commented on those in the patch.\nI vote for integrating the code now, and improve it later when we will have more experience.",
    "created_at": "2009-05-21T23:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48517",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:1 was]:
> > Feedback and suggestion for improvement on this policy are welcome! 

> 
> {{{
> sage: x = A() 
> sage: x.my_method?
> BOOM!
> }}}
> 
> This must be fixed by improving sageinspect.  That should be easy.
> 
> 1) Trick to catch.
> 
> 2) How do you get the docs on my_method though?


I commented on those in the patch.
I vote for integrating the code now, and improve it later when we will have more experience.



---

archive/issue_comments_048518.json:
```json
{
    "body": "Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.",
    "created_at": "2009-06-06T05:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48518",
    "user": "https://github.com/ncalexan"
}
```

Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.



---

archive/issue_comments_048519.json:
```json
{
    "body": "Replying to [comment:5 ncalexan]:\n> Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.\n\n\nThanks for the feedback!\n\nNote that this is an exceptional situation: in principle, users are not supposed to encounter this situation\n(in a compiled language, the code would not even compile). In any cases, this will be trivial to change later.\n\nDo you see any strong reason not to merge this patch as is, until we accumulate enough experience?\n(there are 20 patches piling upon this one).",
    "created_at": "2009-06-10T05:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48519",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 ncalexan]:
> Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.


Thanks for the feedback!

Note that this is an exceptional situation: in principle, users are not supposed to encounter this situation
(in a compiled language, the code would not even compile). In any cases, this will be trivial to change later.

Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?
(there are 20 patches piling upon this one).



---

archive/issue_comments_048520.json:
```json
{
    "body": "> Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?\n\n\nYes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.",
    "created_at": "2009-06-10T05:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48520",
    "user": "https://github.com/ncalexan"
}
```

> Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?


Yes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.



---

archive/issue_comments_048521.json:
```json
{
    "body": "Replying to [comment:7 ncalexan]:\n> > Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?\n\n> \n> Yes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.\n\n\nSo what? The class of this object is broken in the first place.\n\nOn the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).\n\nMy point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.",
    "created_at": "2009-06-10T06:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48521",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:7 ncalexan]:
> > Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?

> 
> Yes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.


So what? The class of this object is broken in the first place.

On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).

My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.



---

archive/issue_comments_048522.json:
```json
{
    "body": "> My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.\n\n\nWait, what is the rush?\n\n> So what? The class of this object is broken in the first place.\n\n\nI think there is a significant difference between broken *functionality* and an object in the system that cannot be *interrogated* by the system.\n\n> On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).\n\n\nThis is often true.  Can you guarantee that such a poisoned object can only be created by a user who \"works hard\" to do so?  If that's the case then I remove whatever objections I have.",
    "created_at": "2009-06-10T06:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48522",
    "user": "https://github.com/ncalexan"
}
```

> My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.


Wait, what is the rush?

> So what? The class of this object is broken in the first place.


I think there is a significant difference between broken *functionality* and an object in the system that cannot be *interrogated* by the system.

> On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).


This is often true.  Can you guarantee that such a poisoned object can only be created by a user who "works hard" to do so?  If that's the case then I remove whatever objections I have.



---

archive/issue_comments_048523.json:
```json
{
    "body": "Replying to [comment:9 ncalexan]:\n> > My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.\n\n> \n> Wait, what is the rush?\n\n\nThe category patches + followers depend on this. Total 22 patches = 1.3 Mb :-)\n\n> > So what? The class of this object is broken in the first place.\n\n> \n> I think there is a significant difference between broken *functionality* and an object in the system that cannot be *interrogated* by the system.\n\n\nFair enough.\n\n> > On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).\n\n> \n> This is often true.  Can you guarantee that such a poisoned object can only be created by a user who \"works hard\" to do so?  If that's the case then I remove whatever objections I have.\n\n\nIn principle, such objects can only be created by:\n- Instantiating an instance of an abstract class (which should not be permitted in the first place)\n- Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class\n- Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.\n\nI don't know how much \"hard word\" is the first point.\n\nThe second point can only occur if:\n- either the user wrote the class himself (which sounds hard enough work)\n- or if a developer did not do his job (or worst, the code went into sage through refereeing!)\n\nNote that the category code includes checking methods that complains if a parent does not implement all the mandatory abstract methods.\nI plan to lift this up to SageObject.\n\nThat being said, as a dev, I got caught myself at least once. So it's all a question of balance between two annoyances.",
    "created_at": "2009-06-10T07:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48523",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:9 ncalexan]:
> > My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.

> 
> Wait, what is the rush?


The category patches + followers depend on this. Total 22 patches = 1.3 Mb :-)

> > So what? The class of this object is broken in the first place.

> 
> I think there is a significant difference between broken *functionality* and an object in the system that cannot be *interrogated* by the system.


Fair enough.

> > On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).

> 
> This is often true.  Can you guarantee that such a poisoned object can only be created by a user who "works hard" to do so?  If that's the case then I remove whatever objections I have.


In principle, such objects can only be created by:
- Instantiating an instance of an abstract class (which should not be permitted in the first place)
- Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class
- Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.

I don't know how much "hard word" is the first point.

The second point can only occur if:
- either the user wrote the class himself (which sounds hard enough work)
- or if a developer did not do his job (or worst, the code went into sage through refereeing!)

Note that the category code includes checking methods that complains if a parent does not implement all the mandatory abstract methods.
I plan to lift this up to SageObject.

That being said, as a dev, I got caught myself at least once. So it's all a question of balance between two annoyances.



---

archive/issue_comments_048524.json:
```json
{
    "body": ">  - Instantiating an instance of an abstract class (which should not be permitted in the first place)\n\n\nWhy not make __init__ (or __new__) raise NotImplementedError?\n\n>  - Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class\n>  - Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.\n\n\nThese two can never be prevented against.  So I'm more okay with this than I was.",
    "created_at": "2009-06-10T07:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48524",
    "user": "https://github.com/ncalexan"
}
```

>  - Instantiating an instance of an abstract class (which should not be permitted in the first place)


Why not make __init__ (or __new__) raise NotImplementedError?

>  - Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class
>  - Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.


These two can never be prevented against.  So I'm more okay with this than I was.



---

archive/issue_comments_048525.json:
```json
{
    "body": "Replying to [comment:11 ncalexan]:\n> >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)\n \n> \n> Why not make __init__ (or __new__) raise NotImplementedError?\n\n\nBecause abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...\n\n> >  - Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class\n> >  - Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.\n \n> \n> These two can never be prevented against.  So I'm more okay with this than I was.",
    "created_at": "2009-06-10T08:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48525",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:11 ncalexan]:
> >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)
 
> 
> Why not make __init__ (or __new__) raise NotImplementedError?


Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...

> >  - Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class
> >  - Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.
 
> 
> These two can never be prevented against.  So I'm more okay with this than I was.



---

archive/issue_comments_048526.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\n> Replying to [comment:11 ncalexan]:\n> > >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)\n \n> > \n> > Why not make __init__ (or __new__) raise NotImplementedError?\n\n> \n> Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...\n\n\nThis seems wrong to me.  __init__ is only called on instance creation.  Raising NotImplementedError in instance creation just means you can't create an instance.  How does this have anything to do with abstract methods or introspection?",
    "created_at": "2009-06-10T08:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48526",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:12 nthiery]:
> Replying to [comment:11 ncalexan]:
> > >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)
 
> > 
> > Why not make __init__ (or __new__) raise NotImplementedError?

> 
> Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...


This seems wrong to me.  __init__ is only called on instance creation.  Raising NotImplementedError in instance creation just means you can't create an instance.  How does this have anything to do with abstract methods or introspection?



---

archive/issue_comments_048527.json:
```json
{
    "body": "Replying to [comment:13 ncalexan]:\n> Replying to [comment:12 nthiery]:\n> > Replying to [comment:11 ncalexan]:\n> > > >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)\n \n> > > \n> > > Why not make __init__ (or __new__) raise NotImplementedError?\n\n> > \n> > Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...\n\n> \n> This seems wrong to me.  __init__ is only called on instance creation.  Raising NotImplementedError in instance creation just means you can't create an instance.  How does this have anything to do with abstract methods or introspection?\n\n\nOh, sorry, I got completely confused. I though you were speaking about the __init__ of the AbstractMethod class.\n\nYes, adding an __init__ or __new__ to abstract classes, so as to prevent element creation would sound reasonable.\nAnd we typically would want to do this by having and `@`abstract_class decorator. To be kept in mind for the future.",
    "created_at": "2009-06-10T15:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48527",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:13 ncalexan]:
> Replying to [comment:12 nthiery]:
> > Replying to [comment:11 ncalexan]:
> > > >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)
 
> > > 
> > > Why not make __init__ (or __new__) raise NotImplementedError?

> > 
> > Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...

> 
> This seems wrong to me.  __init__ is only called on instance creation.  Raising NotImplementedError in instance creation just means you can't create an instance.  How does this have anything to do with abstract methods or introspection?


Oh, sorry, I got completely confused. I though you were speaking about the __init__ of the AbstractMethod class.

Yes, adding an __init__ or __new__ to abstract classes, so as to prevent element creation would sound reasonable.
And we typically would want to do this by having and `@`abstract_class decorator. To be kept in mind for the future.



---

archive/issue_comments_048528.json:
```json
{
    "body": "Here is a second opinion.\n\nI really, really like the idea of adding such a decorator! And for the\nrecord, under normal circumstances, I would have asked for a full design\ndiscussion to take place on sage-devel since I share many of the above\nconcerns and because I think that there are many subtle design issues\nthat need to be addressed. (We'll have to have that discussion later,\nit seems.) However, in light of the decision to get the category theory\ncode into Sage quickly, I am going to reluctantly suggest it be\nincluded in Sage as is. \n\nHere is a list of things that I don't like (most have been mentioned above):\n\n- raising `NotImplementedError` when an abstract method is accessed\n- the error message is not useful\n- returning `NotImplemented` for an optional abstract class\n- can't access the documentation for an abstract method\n- that `hasattr(x, 'my_method')` returns False for abstract methods\n  and True for optional abstract methods\n- can't determine what the undefined abstract methods of an object are\n\nNone of these are strong reasons against inclusion, I guess, since it might be just a matter of opinion, or that I haven't thought enough about the subtleties.",
    "created_at": "2009-06-22T22:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48528",
    "user": "https://github.com/saliola"
}
```

Here is a second opinion.

I really, really like the idea of adding such a decorator! And for the
record, under normal circumstances, I would have asked for a full design
discussion to take place on sage-devel since I share many of the above
concerns and because I think that there are many subtle design issues
that need to be addressed. (We'll have to have that discussion later,
it seems.) However, in light of the decision to get the category theory
code into Sage quickly, I am going to reluctantly suggest it be
included in Sage as is. 

Here is a list of things that I don't like (most have been mentioned above):

- raising `NotImplementedError` when an abstract method is accessed
- the error message is not useful
- returning `NotImplemented` for an optional abstract class
- can't access the documentation for an abstract method
- that `hasattr(x, 'my_method')` returns False for abstract methods
  and True for optional abstract methods
- can't determine what the undefined abstract methods of an object are

None of these are strong reasons against inclusion, I guess, since it might be just a matter of opinion, or that I haven't thought enough about the subtleties.



---

archive/issue_comments_048529.json:
```json
{
    "body": "Replying to [comment:15 saliola]:\n> Here is a second opinion.\n> I really, really like the idea of adding such a decorator! And for the\n> record, under normal circumstances, I would have asked for a full design\n> discussion to take place on sage-devel since I share many of the above\n> concerns and because I think that there are many subtle design issues\n> that need to be addressed. (We'll have to have that discussion later,\n> it seems.) \n\n\nI tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.\n\n> However, in light of the decision to get the category theory\n> code into Sage quickly, I am going to reluctantly suggest it be\n> included in Sage as is. \n\n\nThanks.\n\n> Here is a list of things that I don't like (most have been mentioned above):\n> \n> - raising `NotImplementedError` when an abstract method is accessed\n> - the error message is not useful\n> - returning `NotImplemented` for an optional abstract class\n> - can't access the documentation for an abstract method\n> - that `hasattr(x, 'my_method')` returns False for abstract methods\n>   and True for optional abstract methods\n> - can't determine what the undefined abstract methods of an object are\n\n\nThanks for the feedback! I am also not yet happy about the current state.\nSo do you have suggestions for what to return in both cases?\nWhat mantra would you like to see to test whether an optional abstract method has, or not,\nbeen implemented?\n\nFeel free to include those suggestions in the doc via a reviewers patch, so that users run into them in the future.",
    "created_at": "2009-06-23T04:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48529",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:15 saliola]:
> Here is a second opinion.
> I really, really like the idea of adding such a decorator! And for the
> record, under normal circumstances, I would have asked for a full design
> discussion to take place on sage-devel since I share many of the above
> concerns and because I think that there are many subtle design issues
> that need to be addressed. (We'll have to have that discussion later,
> it seems.) 


I tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.

> However, in light of the decision to get the category theory
> code into Sage quickly, I am going to reluctantly suggest it be
> included in Sage as is. 


Thanks.

> Here is a list of things that I don't like (most have been mentioned above):
> 
> - raising `NotImplementedError` when an abstract method is accessed
> - the error message is not useful
> - returning `NotImplemented` for an optional abstract class
> - can't access the documentation for an abstract method
> - that `hasattr(x, 'my_method')` returns False for abstract methods
>   and True for optional abstract methods
> - can't determine what the undefined abstract methods of an object are


Thanks for the feedback! I am also not yet happy about the current state.
So do you have suggestions for what to return in both cases?
What mantra would you like to see to test whether an optional abstract method has, or not,
been implemented?

Feel free to include those suggestions in the doc via a reviewers patch, so that users run into them in the future.



---

archive/issue_comments_048530.json:
```json
{
    "body": "Hello,\n\nReplying to [comment:16 nthiery]:\n> Replying to [comment:15 saliola]:\n> > Here is a second opinion.\n> > I really, really like the idea of adding such a decorator! And for the\n> > record, under normal circumstances, I would have asked for a full design\n> > discussion to take place on sage-devel since I share many of the above\n> > concerns and because I think that there are many subtle design issues\n> > that need to be addressed. (We'll have to have that discussion later,\n> > it seems.) \n\n> \n> I tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.\n\n\nI definitely missed this. I'm behind in reading the sage-devel emails.\n\n> > Here is a list of things that I don't like (most have been mentioned above):\n> > \n> > - raising `NotImplementedError` when an abstract method is accessed\n> > - the error message is not useful\n> > - returning `NotImplemented` for an optional abstract class\n> > - can't access the documentation for an abstract method\n> > - that `hasattr(x, 'my_method')` returns False for abstract methods\n> >   and True for optional abstract methods\n> > - can't determine what the undefined abstract methods of an object are\n\n> \n> Thanks for the feedback! I am also not yet happy about the current state.\n\n\nYou mentioned that in the doc and in the above comments, and I must admit\nthat this is one of the things that makes me more comfortable with\nincluding this into Sage. I know that you'll be around to improve it in the\nfuture, and that the design isn't complete yet.\n\n> So do you have suggestions for what to return in both cases?\n> What mantra would you like to see to test whether an optional abstract method has, or not,\n> been implemented?\n\n\nYou can't really tell from what I wrote in my last comment, but I spent\nalmost 3 hours looking at this last night. \n\nI thought about what I like and dislike about the existence of such a\ndecorator. I really like the idea, but found myself wondering how much\nbetter is this, really, than good documentation? Will this encourage a\ndeveloper to be lazy in documenting what needs to be implemented by\nsubclasses? I strongly suspect this will be the case, which is fine as long\nas there is support for easily determining which methods of a class need to\nbe implemented (I don't want to have to grep for `abstract_method` in\nthe source). I wondered how I would use this as a developer of a subclass?\nI mean, given an object `x`, is there a way to tell which abstract\nmethods of `x` need to be implemented without grepping the source? This\nis where introspection would normally come in (see below). And, as the\ndeveloper of the subclass, it would be best to have `x.my_method?`\nreturn a docstring that says what the implementation should do (this is\nalready mentioned in the docstring as a future improvement).\n\nI wondered about, as ncalexan suggested, checking whether abstract methods\nare implemented at instance creation. This is exactly what happens now with\n`CombinatorialAlgebra(QQ)`, but I find that this puts too much power in\nthe hands of the developer since a user might want to use a class for\nsomething that doesn't require a particular abstract method at all.\n\nI wondered about different mantras. If no error is returned on accessing\nelements, then one can use introspection to find all the abstract methods\nof an object.\n\n```\nsage: [meth for meth in dir(x) if type(x.meth, AbstractMethod)]\n```\n(The above currently doesn't work because `x.my_method` raises an error.) \n\nI also wondered whether some methods might be decorated with\n`abstract_method`, but have a default implementation. I'm thinking of a\ndecorator that signals to the user/developer that even though that\nparticular method is implemented, it would be vastly better (for\nspeed/memory/...) to provide a better implementation if one exists. I'm\nthink about some of the methods of\n`CombinatorialClass`/`EnumeratedSet`, in particular. Perhaps this\nis beyond the scope of this decorator though, since an abstract method\nseems to be just dummy code usually.\n\nPersonally, I am leaning towards the idea of raising a\n`NotImplementedError` upon calling the method instead of upon accessing\nit, together with a good error message that tells the user that this method\nneeds to be defined in order for what they just asked for to work. I\nhaven't thought through this enough to be convinced that this is my\npreferred approach, and there might be some fine points I haven't thought\nof that makes this unappealing.\n\nSo, lots of thoughts, not many conclusions. \n\nI decided to keep my last post short and to the point because I knew this\ntype of post would be lengthy, but you asked!\n\n> Feel free to include those suggestions in the doc via a reviewers patch, so that users run into them in the future.\n\n\nI think it isn't necessary since you have adequately stated in the\ndocumentation that it is just the beginning. And it also lists several\ntodo's, one of which is to scour the web for other implementations/ideas\nand merge them. Anyhow, as I said above, I have arrived at no conclusions\nyet, just preferences.",
    "created_at": "2009-06-23T08:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48530",
    "user": "https://github.com/saliola"
}
```

Hello,

Replying to [comment:16 nthiery]:
> Replying to [comment:15 saliola]:
> > Here is a second opinion.
> > I really, really like the idea of adding such a decorator! And for the
> > record, under normal circumstances, I would have asked for a full design
> > discussion to take place on sage-devel since I share many of the above
> > concerns and because I think that there are many subtle design issues
> > that need to be addressed. (We'll have to have that discussion later,
> > it seems.) 

> 
> I tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.


I definitely missed this. I'm behind in reading the sage-devel emails.

> > Here is a list of things that I don't like (most have been mentioned above):
> > 
> > - raising `NotImplementedError` when an abstract method is accessed
> > - the error message is not useful
> > - returning `NotImplemented` for an optional abstract class
> > - can't access the documentation for an abstract method
> > - that `hasattr(x, 'my_method')` returns False for abstract methods
> >   and True for optional abstract methods
> > - can't determine what the undefined abstract methods of an object are

> 
> Thanks for the feedback! I am also not yet happy about the current state.


You mentioned that in the doc and in the above comments, and I must admit
that this is one of the things that makes me more comfortable with
including this into Sage. I know that you'll be around to improve it in the
future, and that the design isn't complete yet.

> So do you have suggestions for what to return in both cases?
> What mantra would you like to see to test whether an optional abstract method has, or not,
> been implemented?


You can't really tell from what I wrote in my last comment, but I spent
almost 3 hours looking at this last night. 

I thought about what I like and dislike about the existence of such a
decorator. I really like the idea, but found myself wondering how much
better is this, really, than good documentation? Will this encourage a
developer to be lazy in documenting what needs to be implemented by
subclasses? I strongly suspect this will be the case, which is fine as long
as there is support for easily determining which methods of a class need to
be implemented (I don't want to have to grep for `abstract_method` in
the source). I wondered how I would use this as a developer of a subclass?
I mean, given an object `x`, is there a way to tell which abstract
methods of `x` need to be implemented without grepping the source? This
is where introspection would normally come in (see below). And, as the
developer of the subclass, it would be best to have `x.my_method?`
return a docstring that says what the implementation should do (this is
already mentioned in the docstring as a future improvement).

I wondered about, as ncalexan suggested, checking whether abstract methods
are implemented at instance creation. This is exactly what happens now with
`CombinatorialAlgebra(QQ)`, but I find that this puts too much power in
the hands of the developer since a user might want to use a class for
something that doesn't require a particular abstract method at all.

I wondered about different mantras. If no error is returned on accessing
elements, then one can use introspection to find all the abstract methods
of an object.

```
sage: [meth for meth in dir(x) if type(x.meth, AbstractMethod)]
```
(The above currently doesn't work because `x.my_method` raises an error.) 

I also wondered whether some methods might be decorated with
`abstract_method`, but have a default implementation. I'm thinking of a
decorator that signals to the user/developer that even though that
particular method is implemented, it would be vastly better (for
speed/memory/...) to provide a better implementation if one exists. I'm
think about some of the methods of
`CombinatorialClass`/`EnumeratedSet`, in particular. Perhaps this
is beyond the scope of this decorator though, since an abstract method
seems to be just dummy code usually.

Personally, I am leaning towards the idea of raising a
`NotImplementedError` upon calling the method instead of upon accessing
it, together with a good error message that tells the user that this method
needs to be defined in order for what they just asked for to work. I
haven't thought through this enough to be convinced that this is my
preferred approach, and there might be some fine points I haven't thought
of that makes this unappealing.

So, lots of thoughts, not many conclusions. 

I decided to keep my last post short and to the point because I knew this
type of post would be lengthy, but you asked!

> Feel free to include those suggestions in the doc via a reviewers patch, so that users run into them in the future.


I think it isn't necessary since you have adequately stated in the
documentation that it is just the beginning. And it also lists several
todo's, one of which is to scour the web for other implementations/ideas
and merge them. Anyhow, as I said above, I have arrived at no conclusions
yet, just preferences.



---

archive/issue_comments_048531.json:
```json
{
    "body": "Though the interface hasn't completely settled, I think its stable enough to go in and worth starting to use. I'm opening a new ticket #6400 to review all the TODO's in this one.",
    "created_at": "2009-06-25T10:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48531",
    "user": "https://github.com/robertwb"
}
```

Though the interface hasn't completely settled, I think its stable enough to go in and worth starting to use. I'm opening a new ticket #6400 to review all the TODO's in this one.



---

archive/issue_comments_048532.json:
```json
{
    "body": "Hi Franco!\n\nReplying to [comment:17 saliola]:\n> Replying to [comment:16 nthiery]:\n> > Replying to [comment:15 saliola]:\n> > > Here is a second opinion.\n> > > I really, really like the idea of adding such a decorator! And for the\n> > > record, under normal circumstances, I would have asked for a full design\n> > > discussion to take place on sage-devel since I share many of the above\n> > > concerns and because I think that there are many subtle design issues\n> > > that need to be addressed. (We'll have to have that discussion later,\n> > > it seems.) \n\n> > \n> > I tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.\n\n> \n> I definitely missed this. I'm behind in reading the sage-devel emails.\n\n\nOops, that was in my dreams. I only advertised it oraly at SD15. You should have been there :-)\n \n> You mentioned that in the doc and in the above comments, and I must admit\n> that this is one of the things that makes me more comfortable with\n> including this into Sage. I know that you'll be around to improve it in the\n> future, and that the design isn't complete yet.\n\n\n:-)\n\n> You can't really tell from what I wrote in my last comment, but I spent\n> almost 3 hours looking at this last night. \n\n\nGreat.\n\n> I thought about what I like and dislike about the existence of such a\n> decorator. I really like the idea, but found myself wondering how much\n> better is this, really, than good documentation? Will this encourage a\n> developer to be lazy in documenting what needs to be implemented by\n> subclasses? I strongly suspect this will be the case, which is fine as long\n> as there is support for easily determining which methods of a class need to\n> be implemented (I don't want to have to grep for `abstract_method` in\n> the source). I wondered how I would use this as a developer of a subclass?\n> I mean, given an object `x`, is there a way to tell which abstract\n> methods of `x` need to be implemented without grepping the source? This\n> is where introspection would normally come in (see below). And, as the\n> developer of the subclass, it would be best to have `x.my_method?`\n> return a docstring that says what the implementation should do (this is\n> already mentioned in the docstring as a future improvement).\n\n\nBesides the nice visual effect, allowing for automatic checks is precisely the purpose of `@`abstract_method.\nThis is already in #6343 (please update to the latest Sage-Combinat in an hour or so to get the exact syntax below):\n\n        sage: TestSuite(ZZ).run(verbose = True)\n        running ._test_not_implemented_methods() ... done\n        running ._test_pickling() ... done\n\n> I wondered about, as ncalexan suggested, checking whether abstract methods\n> are implemented at instance creation. This is exactly what happens now with\n> `CombinatorialAlgebra(QQ)`, but I find that this puts too much power in\n> the hands of the developer since a user might want to use a class for\n> something that doesn't require a particular abstract method at all.\n\n\nThat's sensible for Parents, but would not be reasonable for elements that could be created by the millions.\n\n> I wondered about different mantras. If no error is returned on accessing\n> elements, then one can use introspection to find all the abstract methods\n> of an object.\n> \n> ```\n> sage: [meth for meth in dir(x) if type(x.meth, AbstractMethod)]\n> ```\n> (The above currently doesn't work because `x.my_method` raises an error.) \n\n\nNote: you can do the same on x.__class__, which is what .test_not_implemented_methods does\n\n> I also wondered whether some methods might be decorated with\n> `abstract_method`, but have a default implementation. I'm thinking of a\n> decorator that signals to the user/developer that even though that\n> particular method is implemented, it would be vastly better (for\n> speed/memory/...) to provide a better implementation if one exists. I'm\n> think about some of the methods of\n> `CombinatorialClass`/`EnumeratedSet`, in particular. Perhaps this\n> is beyond the scope of this decorator though, since an abstract method\n> seems to be just dummy code usually.\n\n\nI definitely would like this as well! Probably under a different name though, like\n`@`dummy_method / `@`default_method, since the purpose is a bit different.\n\n> Personally, I am leaning towards the idea of raising a\n> `NotImplementedError` upon calling the method instead of upon accessing\n> it, together with a good error message that tells the user that this method\n> needs to be defined in order for what they just asked for to work. I\n> haven't thought through this enough to be convinced that this is my\n> preferred approach, and there might be some fine points I haven't thought\n> of that makes this unappealing.\n\n\nOk. Let's see how this works in practice.\n\n> So, lots of thoughts, not many conclusions. \n> I decided to keep my last post short and to the point because I knew this\n> type of post would be lengthy, but you asked!\n\n\nI did! Thanks very much for taking the time typing it up.\n\nCheers,",
    "created_at": "2009-06-26T07:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48532",
    "user": "https://github.com/nthiery"
}
```

Hi Franco!

Replying to [comment:17 saliola]:
> Replying to [comment:16 nthiery]:
> > Replying to [comment:15 saliola]:
> > > Here is a second opinion.
> > > I really, really like the idea of adding such a decorator! And for the
> > > record, under normal circumstances, I would have asked for a full design
> > > discussion to take place on sage-devel since I share many of the above
> > > concerns and because I think that there are many subtle design issues
> > > that need to be addressed. (We'll have to have that discussion later,
> > > it seems.) 

> > 
> > I tried to advertise the feature to start such a discussion, but there was not much reaction. I think we first need to accumulate experience by using the current thing, and then discuss again. Release early, release often.

> 
> I definitely missed this. I'm behind in reading the sage-devel emails.


Oops, that was in my dreams. I only advertised it oraly at SD15. You should have been there :-)
 
> You mentioned that in the doc and in the above comments, and I must admit
> that this is one of the things that makes me more comfortable with
> including this into Sage. I know that you'll be around to improve it in the
> future, and that the design isn't complete yet.


:-)

> You can't really tell from what I wrote in my last comment, but I spent
> almost 3 hours looking at this last night. 


Great.

> I thought about what I like and dislike about the existence of such a
> decorator. I really like the idea, but found myself wondering how much
> better is this, really, than good documentation? Will this encourage a
> developer to be lazy in documenting what needs to be implemented by
> subclasses? I strongly suspect this will be the case, which is fine as long
> as there is support for easily determining which methods of a class need to
> be implemented (I don't want to have to grep for `abstract_method` in
> the source). I wondered how I would use this as a developer of a subclass?
> I mean, given an object `x`, is there a way to tell which abstract
> methods of `x` need to be implemented without grepping the source? This
> is where introspection would normally come in (see below). And, as the
> developer of the subclass, it would be best to have `x.my_method?`
> return a docstring that says what the implementation should do (this is
> already mentioned in the docstring as a future improvement).


Besides the nice visual effect, allowing for automatic checks is precisely the purpose of `@`abstract_method.
This is already in #6343 (please update to the latest Sage-Combinat in an hour or so to get the exact syntax below):

        sage: TestSuite(ZZ).run(verbose = True)
        running ._test_not_implemented_methods() ... done
        running ._test_pickling() ... done

> I wondered about, as ncalexan suggested, checking whether abstract methods
> are implemented at instance creation. This is exactly what happens now with
> `CombinatorialAlgebra(QQ)`, but I find that this puts too much power in
> the hands of the developer since a user might want to use a class for
> something that doesn't require a particular abstract method at all.


That's sensible for Parents, but would not be reasonable for elements that could be created by the millions.

> I wondered about different mantras. If no error is returned on accessing
> elements, then one can use introspection to find all the abstract methods
> of an object.
> 
> ```
> sage: [meth for meth in dir(x) if type(x.meth, AbstractMethod)]
> ```
> (The above currently doesn't work because `x.my_method` raises an error.) 


Note: you can do the same on x.__class__, which is what .test_not_implemented_methods does

> I also wondered whether some methods might be decorated with
> `abstract_method`, but have a default implementation. I'm thinking of a
> decorator that signals to the user/developer that even though that
> particular method is implemented, it would be vastly better (for
> speed/memory/...) to provide a better implementation if one exists. I'm
> think about some of the methods of
> `CombinatorialClass`/`EnumeratedSet`, in particular. Perhaps this
> is beyond the scope of this decorator though, since an abstract method
> seems to be just dummy code usually.


I definitely would like this as well! Probably under a different name though, like
`@`dummy_method / `@`default_method, since the purpose is a bit different.

> Personally, I am leaning towards the idea of raising a
> `NotImplementedError` upon calling the method instead of upon accessing
> it, together with a good error message that tells the user that this method
> needs to be defined in order for what they just asked for to work. I
> haven't thought through this enough to be convinced that this is my
> preferred approach, and there might be some fine points I haven't thought
> of that makes this unappealing.


Ok. Let's see how this works in practice.

> So, lots of thoughts, not many conclusions. 
> I decided to keep my last post short and to the point because I knew this
> type of post would be lengthy, but you asked!


I did! Thanks very much for taking the time typing it up.

Cheers,



---

archive/issue_events_014329.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-06-26T17:44:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6097#event-14329"
}
```



---

archive/issue_comments_048533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6097#issuecomment-48533",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: fixed
