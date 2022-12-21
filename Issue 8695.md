# Issue 8695: UniqueRepresentations implements __eq__ but not __ne__

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-04-16 15:13:49

Assignee: hivert

CC:  sage-combinat

Keywords: UniqueRepresentation, equality

Python manuals says:

    There are no implied relationships among the comparison operators. The truth of x==y does not imply that x!=y is false. Accordingly, when defining __eq__(), one should also define __ne__() so that the operators will behave as expected.

UniqueRepresentation fails to comply with this. As a consequence:

```
sage: G6 = GL(6, QQ)
sage: G6 == G6
True
sage: G6 != G6
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Matrix group over Rational Field not implemented.
```



---

Comment by hivert created at 2010-04-16 15:19:45

This should be ready for review.


---

Comment by hivert created at 2010-04-16 15:19:45

Changing status from new to needs_review.


---

Comment by nborie created at 2010-04-16 16:09:12

Changing status from needs_review to positive_review.


---

Comment by nborie created at 2010-04-16 16:09:12

apply, tests, doc...

Positive review for this patch.


---

Comment by nthiery created at 2010-04-16 21:33:10

I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.


---

Comment by nthiery created at 2010-04-16 21:33:10

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2010-04-16 21:38:36

Also, this would have been caught by a _test_eq, which we should implement! See #8697!


---

Comment by hivert created at 2010-04-16 23:37:56

Replying to [comment:5 nthiery]:
> Also, this would have been caught by a _test_eq, which we should implement! See #8697!

Actually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.


---

Comment by mhansen created at 2010-04-17 01:48:45

Replying to [comment:4 nthiery]:
> I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.

The only thing that inheriting from object does is make it a "new-style" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html


---

Comment by nthiery created at 2010-04-17 20:19:40

Replying to [comment:6 hivert]:
> Replying to [comment:5 nthiery]:
> > Also, this would have been caught by a _test_eq, which we should implement! See #8697!
> 
> Actually that exactly how I caught it except that it was with _test_self_equal which is implemented in #8402. I think #8697 should be closed as a duplicate of #8402.

Oops, right. I looked for that one and somehow missed it.


---

Comment by nthiery created at 2010-04-17 20:21:52

Replying to [comment:7 mhansen]:
> Replying to [comment:4 nthiery]:
> > I am just not sure about forcing UniqueRepresentation to inherit from object. Let's discuss this over the phone.
> 
> The only thing that inheriting from object does is make it a "new-style" class in Python, which is what everything should be now.  In the 3.x series, old-style classes are removed.  http://docs.python.org/reference/datamodel.html

Yup! So there is particularly no point about forcing it explicitly, since it will be automatically the case later, and in the mean time there is no reason to fix something that ain't broken.

We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.


---

Comment by hivert created at 2010-04-17 20:45:09

Changing status from needs_work to needs_review.


---

Attachment

> We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.

Done !


---

Comment by hivert created at 2010-04-17 20:45:56

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-04-17 20:45:56

Replying to [comment:10 hivert]:
> > We discussed with Florent over the phone. He will remove the inheritance from object, reupload the patch, and set a positive review on my behalf.
> 
> Done !

At put back to positive review.


---

Comment by jhpalmieri created at 2010-04-19 05:16:59

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:16:59

Merged "trac_8695-uniquerep_missing__ne__-fh.patch" into 4.4.alpha1.
