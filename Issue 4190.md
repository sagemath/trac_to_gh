# Issue 4190: division of number field order elements doesn't check for membership

Issue created by migration from https://trac.sagemath.org/ticket/4190

Original creator: davidloeffler

Original creation time: 2008-09-24 11:21:35

Assignee: was

CC:  robertwb

I think this just about says it all:

```
sage: OK = NumberField(x^2 - x + 2, 'w').ring_of_integers()
sage: w = OK.ring_generators()[0]
sage: 1/w in OK
True
```

I tested this for cubic fields as well, and the same problem comes up. I can't work out why this happens -- it must be something weird in the coercion framework, as there isn't a specific method for division or inversion of elements of orders: it falls back to NumberFieldElement.__invert__ and then somehow coerces the result back to an OrderElement without doing any checks along the way.

I discovered this when trying to find out whether one element of OK was divisible by another -- "x.divides(y)" raises an error, and "y/x in OK" always returns True, which isn't very helpful; the best I could find was "y in x*OK" which seems to give the right results.


---

Comment by mabshoff created at 2008-09-24 11:25:57

Hi David,

I would assume Robert knows what this is all about, so I am adding him to the CC. 

In general it would be good to mention the issue on [sage-devel] so that the right people get a change to become aware of the problem since not too many people read [sage-trac].

Cheers,

Michael


---

Comment by robertwb created at 2008-09-24 16:43:54

`_div_` on order elements needs to be written so as to return something that is always in the fraction field, not self. This is an oversight, not by design.


---

Comment by davidloeffler created at 2008-09-24 19:42:33

I'll have a go at writing that then.


---

Comment by davidloeffler created at 2008-09-24 19:42:33

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2008-09-25 11:21:24

OK, here's a very small patch. Turns out order elements are a cdef class, so I wrote a _div_c_impl.

I wondered whether the return value should be in the order if that makes sense, and in the fraction field otherwise, but this slowed everything down by a factor of 2 according to timeit() so I made it always return fraction field elements.


---

Comment by davidloeffler created at 2008-09-25 11:21:24

Changing status from new to assigned.


---

Comment by robertwb created at 2008-09-25 11:35:34

Good work. Note that as of the latest alpha, both cdef and normal classes use _div_. Also, given the way these two are implemented, you could just reset the _parent slot instead of using the `__call__` method which is probably eating up a large chunk of the time. 

As for your question about whether or not it belongs in the fraction field, the convention is to have division return elements of the fraction field, so go ahead and remove that commented code. 


```
sage: parent(4/2)
Rational Field
```



---

Comment by davidloeffler created at 2008-09-25 15:38:44

OK. I'm not keen on downloading and recompiling each new alpha from scratch -- I don't have a fast enough machine for that sort of game -- so perhaps this one will have to wait for 3.1.4; I've changed the status to "needs work" to reflect this.

(PS. If there's something analogous to sage -upgrade or hg_sage.pull() that I can use to upgrade my sage to the latest alpha without having to recompile all the libraries that haven't changed since 3.1.2 anyway, then I'd be very interested to hear about it.)


---

Comment by mabshoff created at 2008-09-25 16:14:51

Replying to [comment:6 davidloeffler]:

Hi David,

> OK. I'm not keen on downloading and recompiling each new alpha from scratch -- I don't have a fast enough machine for that sort of game -- so perhaps this one will have to wait for 3.1.4; I've changed the status to "needs work" to reflect this.

There are usually development binaries for sage.math which you just need to unpack on that machine and you are ready to go to do development work in an instant. Ironically there is no 3.1.3.alpha1 binary at the moment since I am valgrinding the release for the next day or so and I cannot bdist since that will impact the running jobs. But there will be an alpha2 binary. If you need a sage.math account just ping me by email.

> (PS. If there's something analogous to sage -upgrade or hg_sage.pull() that I can use to upgrade my sage to the latest alpha without having to recompile all the libraries that haven't changed since 3.1.2 anyway, then I'd be very interested to hear about it.)

There is no such thing, even as it has been requested a lot. One thing to do is to unpack the new source tarball and to move the new spkgs into $SAGE_ROOT/spkg/standard and then invoke make. That will pretty much do an in place upgrade.

Cheers,

Michael


---

Comment by davidloeffler created at 2008-10-31 15:14:42

New patch


---

Attachment

I've uploaded a new patch, taking into account the changes to the coercion model, which works under 3.1.4 and 3.2.alpha1.


---

Comment by cremona created at 2008-11-13 13:58:06

Question: is it necessary to have three versions of this?   Would it not be enough to have one and the others would work just by inheritance?

Apart from that, I noticed that the doctest has a duplicate line (repeated 3 times!).

I tried to find out what code is run when you say "a in OK" but I have absolutely no idea.  I could not find any `__contains__` function which seemed to be relevant.  Does this work via some coercion magic, or by chance, or what have I missed?

The patch applies fine to 3.2.alpha3.  All tests in number_field/ pass.  You should add this doctest (from the original post):

```
sage: OK = NumberField(x^2 - x + 2, 'w').ring_of_integers()
sage: w = OK.ring_generators()[0]
sage: 1/w in OK
False
```



---

Comment by davidloeffler created at 2008-11-13 15:56:25

As for the inheritance thing: unfortunately, OrderElement_relative, OrderElement_absolute and OrderElement_quadratic all inherit from the corresponding number field classes, which all have different _ div _ implementations, and multiple inheritance is banned. So there is no one place we can put the method where it will be inherited by everything. Personally I'm not sure I agree on that design decision, but I don't have the skills or the time to reimplement it otherwise. 

As far as I can tell, the "a in OK" is calling some very generic code (probably in sage.structure.Parent at a guess) which checks whether or not a.parent() is OK, and if it isn't, attempts to coerce a into OK via OK's __ call __ method, returning False if this fails.

I am in India at the moment and it is late evening local time; I will get to work on improving the doctests tomorrow.


---

Comment by cremona created at 2008-11-13 16:18:46

Replying to [comment:10 davidloeffler]:
> As for the inheritance thing: unfortunately, OrderElement_relative, OrderElement_absolute and OrderElement_quadratic all inherit from the corresponding number field classes, which all have different _ div _ implementations, and multiple inheritance is banned. So there is no one place we can put the method where it will be inherited by everything. Personally I'm not sure I agree on that design decision, but I don't have the skills or the time to reimplement it otherwise. 

OK, too bad.

> 
> As far as I can tell, the "a in OK" is calling some very generic code (probably in sage.structure.Parent at a guess) which checks whether or not a.parent() is OK, and if it isn't, attempts to coerce a into OK via OK's __ call __ method, returning False if this fails.

You are right.  In fact one way to see where this is happening is to try OK(1/a) (where 1/a is not in OK) and see where the TypeError comes from, in this case order.py, in OK's `__call__` function.

> 
> I am in India at the moment and it is late evening local time; I will get to work on improving the doctests tomorrow.

No hurry.  If you had time to look at #4392, even better!


---

Comment by davidloeffler created at 2008-11-14 05:57:32

apply after previous patch


---

Attachment

I could only find the duplicate line in one of the doctests, but I've killed it there. I also realised that while my patch fixed the div methods it didn't fix the separate invert methods, so I've added a similar fix to those.


---

Comment by cremona created at 2008-11-14 10:15:11

OK (!) so there was only one duplicate.  Good to have the `__invert__` functions too.  I successfully applied the second patch on top of the first one, and all tests in number_field pass.

As far as I can see this is ready to go in.


---

Comment by mabshoff created at 2008-11-14 18:48:39

Resolution: fixed


---

Comment by mabshoff created at 2008-11-14 18:48:39

Megred both patches in Sage 3.2.rc1
