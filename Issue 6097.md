# Issue 6097: Implements a mantra for declaring abstract methods

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-21 01:19:28

Assignee: nthiery

CC:  sage-combinat

Keywords: abstract methods

This patch implements a decorator tha can be used to declare a method
that should be implemented by derived classes. This declaration should
typically include documentation for the specification for this method.

The purpose is to enforce a consistent and visual mantra for such
declarations. In the long run, this will be used for automated
systematic signature checks.


---

Comment by was created at 2009-05-21 02:47:30

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

Attachment


---

Comment by nthiery created at 2009-05-21 23:43:41

Changing status from new to assigned.


---

Comment by nthiery created at 2009-05-21 23:43:41

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

Comment by nthiery created at 2009-05-21 23:44:53

Changing priority from minor to major.


---

Comment by ncalexan created at 2009-06-06 05:30:06

Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.


---

Comment by nthiery created at 2009-06-10 05:34:21

Replying to [comment:5 ncalexan]:
> Making this fail on access is so introspection and command line unfriendly that I vote a *very strong* -1 to it.

Thanks for the feedback!

Note that this is an exceptional situation: in principle, users are not supposed to encounter this situation
(in a compiled language, the code would not even compile). In any cases, this will be trivial to change later.

Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?
(there are 20 patches piling upon this one).


---

Comment by ncalexan created at 2009-06-10 05:49:01

> Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?

Yes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.


---

Comment by nthiery created at 2009-06-10 06:09:51

Replying to [comment:7 ncalexan]:
> > Do you see any strong reason not to merge this patch as is, until we accumulate enough experience?
> 
> Yes.  One cannot even loop over attributes of an object generically with such behaviour!  I really can't stress how bad an idea I think this is.

So what? The class of this object is broken in the first place.

On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).

My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.


---

Comment by ncalexan created at 2009-06-10 06:15:23

> My point is: the issue is non trivial enough that it requires more experience and further debate (not just the two of us). And we do not have the time for this right now.

Wait, what is the rush?

> So what? The class of this object is broken in the first place.

I think there is a significant difference between broken *functionality* and an object in the system that cannot be *interrogated* by the system.

> On the other hand, experience with MuPAD, tells that having early errors for such situations is much safer (note that a bound method need not be called immediately; instead it can be passed down to other functions and wreak havoc at a distant place later).

This is often true.  Can you guarantee that such a poisoned object can only be created by a user who "works hard" to do so?  If that's the case then I remove whatever objections I have.


---

Comment by nthiery created at 2009-06-10 07:01:33

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

Comment by ncalexan created at 2009-06-10 07:25:32

>  - Instantiating an instance of an abstract class (which should not be permitted in the first place)

Why not make __init__ (or __new__) raise NotImplementedError?

>  - Instantiating an instance of a concrete class which does not implement all the mandatory abstract methods of it super class
>  - Or shooting in your own foot, and creating the abstract_method yourself, as in the doctest.

These two can never be prevented against.  So I'm more okay with this than I was.


---

Comment by nthiery created at 2009-06-10 08:04:14

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

Comment by ncalexan created at 2009-06-10 08:08:15

Replying to [comment:12 nthiery]:
> Replying to [comment:11 ncalexan]:
> > >  - Instantiating an instance of an abstract class (which should not be permitted in the first place)
> > 
> > Why not make __init__ (or __new__) raise NotImplementedError?
> 
> Because abstract methods are perfectly valid in an abstract class. Actually, the user will want to use introspection to query for their doc, ...

This seems wrong to me.  __init__ is only called on instance creation.  Raising NotImplementedError in instance creation just means you can't create an instance.  How does this have anything to do with abstract methods or introspection?


---

Comment by nthiery created at 2009-06-10 15:53:57

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

Comment by saliola created at 2009-06-22 22:36:03

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

Comment by nthiery created at 2009-06-23 04:21:19

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
>  - raising `NotImplementedError` when an abstract method is accessed
>  - the error message is not useful
>  - returning `NotImplemented` for an optional abstract class
>  - can't access the documentation for an abstract method
>  - that `hasattr(x, 'my_method')` returns False for abstract methods
>    and True for optional abstract methods
>  - can't determine what the undefined abstract methods of an object are

Thanks for the feedback! I am also not yet happy about the current state.
So do you have suggestions for what to return in both cases?
What mantra would you like to see to test whether an optional abstract method has, or not,
been implemented?

Feel free to include those suggestions in the doc via a reviewers patch, so that users run into them in the future.


---

Comment by saliola created at 2009-06-23 08:06:37

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
> >  - raising `NotImplementedError` when an abstract method is accessed
> >  - the error message is not useful
> >  - returning `NotImplemented` for an optional abstract class
> >  - can't access the documentation for an abstract method
> >  - that `hasattr(x, 'my_method')` returns False for abstract methods
> >    and True for optional abstract methods
> >  - can't determine what the undefined abstract methods of an object are
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

Comment by robertwb created at 2009-06-25 10:28:08

Though the interface hasn't completely settled, I think its stable enough to go in and worth starting to use. I'm opening a new ticket #6400 to review all the TODO's in this one.


---

Comment by nthiery created at 2009-06-26 07:52:08

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
> {{{
> sage: [meth for meth in dir(x) if type(x.meth, AbstractMethod)]
> }}}
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

Comment by boothby created at 2009-06-26 17:44:25

Resolution: fixed
