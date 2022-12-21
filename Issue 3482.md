# Issue 3482: create a pickle jar

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-20 06:17:40

Assignee: robertwb

This is easy to use -- so the docstrings at the bottom of sage/structure/sage_object.pyx.

```
sage.structure.sage_object.picklejar?
```

and 

```
sage.structure.sage_object.unpickle_all?
```



---

Attachment


---

Comment by was created at 2008-06-20 17:17:04

:-)

Hi, it turns out that *all* 465 pickles in sage-3.0.3 made on opteron 64-bit linux unpickle fine on 32-bit osx intel.


---

Comment by ncalexan created at 2008-06-20 21:54:59

Please change the environment variable to start with SAGE; these should all be consistent.  Also, why is it not SAGE_PICKLE_JAR_ROOT in keeping with the convention?

The doctests do not show what filename a particular object is given, nor does it demonstrate a failing load.  If the idea is figure out what class cannot be reconstituted, that's not enough.  Also, it would be nice to test unpickling a class that no longer exists in the library.

In addition, the code doesn't return the unpickled objects -- say a dict or similar.  Why not?

I say this is not done yet.


---

Comment by was created at 2008-06-22 00:53:50

> Please change the environment variable to start with SAGE; 
> these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT 
> in keeping with the convention?

How about SAGE_PICKLE_JAR?  That's simple and easy to remember. 

> The doctests do not show what filename a particular object is given, nor 
> does it demonstrate a failing load. If the idea is figure out what class 
> cannot be reconstituted, that's not enough. 

The idea is that one would unpickle the object in the current released
version of sage, which would allow one to find out anything you want
about it.   I could change the filename to be some nice-ified version of
type(obj), with a number appended in case of duplicates.  Would you prefer that?

> Also, it would be nice to 
> test unpickling a class that no longer exists in the library.

How?  

> In addition, the code doesn't return the unpickled objects -- say a 
> dict or similar. Why not?

Simplicity.   What would be the point of returning the unpickled objects?
Which code are you talking about?     The point
is to get a list of the objects that don't unpickle, so one can investigate
further and see what major/minor change to the library caused the objects
to no longer unpickle.


---

Comment by cwitty created at 2008-06-22 20:27:17

A suggestion: maybe the file should actually store a triple, `(dumps(x), repr(x), repr(parent(x)))` (maybe also repr(type(x)) and repr(type(parent(x)))).  The repr's would serve two purposes: in case a pickle fails to unpickle in a new version, this is useful for figuring out where to look; and repr(x) and repr(parent(x)) can be recomputed in the new version of Sage and compared to the pickled version, as a minimal check that unpickling actually gave the correct object.

The downside is that changing the printing of an object would start to make the pickle jar tests fail; there would have to be a way of updating the printing in previous-version pickle jars (without changing the previous dumps(x)).


---

Comment by was created at 2008-06-23 13:56:57

> A suggestion: maybe the file should actually store a triple, 
> (dumps(x), repr(x), repr(parent(x))) (maybe also repr(type(x))
> and repr(type(parent(x)))). The repr's would serve two purposes: 
>in case a pickle fails to unpickle in a new version, this is useful 
> for figuring out where to look; and repr(x) and repr(parent(x)) 
> can be recomputed in the new version of Sage and compared to the 
> pickled version, as a minimal check that unpickling actually gave the correct object.

> The downside is that changing the printing of an object would 
> start to make the pickle jar tests fail; there would have to 
> be a way of updating the printing in previous-version pickle jars 
> (without changing the previous dumps(x)).


I think it would be better would be to have two files:

```
   a.sobj  -- pickled version of x
   a.txt  -- a line with type(x); rest of file has repr(x)
```

Many objects don't have parents, and the above addresses the
"updating the pickle jar" problem you cite above.  Also,
one can always get at a.txt without having to deal with
pickle at all.


---

Comment by ncalexan created at 2008-06-24 04:09:19

Replying to [comment:5 was]:
> > Please change the environment variable to start with SAGE; 
> > these should all be consistent. Also, why is it not SAGE_PICKLE_JAR_ROOT 
> > in keeping with the convention?
> 
> How about SAGE_PICKLE_JAR?  That's simple and easy to remember.

I agree, sounds good.

 > > The doctests do not show what filename a particular object is given, nor 
> > does it demonstrate a failing load. If the idea is figure out what class 
> > cannot be reconstituted, that's not enough. 
> 
> The idea is that one would unpickle the object in the current released
> version of sage, which would allow one to find out anything you want
> about it.   I could change the filename to be some nice-ified version of
> type(obj), with a number appended in case of duplicates.  Would you prefer that?

Maybe?  I don't understand how this is supposed to work.  This dumps a directory of random looking pickles.  (I can't see how to identify any of the outputs.)  I update sage.  Some things don't load -- but I don't have any way to identify what they were supposed to be!  How on earth could you debug it?

> > Also, it would be nice to 
> > test unpickling a class that no longer exists in the library.
> 
> How?

Create a class A, pickle it, then del A.  Something like:


```
sage: class TestClass: pass
....: 
sage: test = TestClass()
sage: loads(dumps(test))
<__main__.TestClass instance at 0xca06940>
sage: s = dumps(test)
sage: del test
sage: del TestClass
sage: loads(s)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/sage_object.pyx in sage.structure.sage_object.loads (sage/structure/sage_object.c:5491)()

<type 'exceptions.RuntimeError'>: FakeModule object has no attribute 'TestClass'
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```


> 
> > In addition, the code doesn't return the unpickled objects -- say a 
> > dict or similar. Why not?
> 
> Simplicity.   What would be the point of returning the unpickled objects?
> Which code are you talking about?     The point
> is to get a list of the objects that don't unpickle, so one can investigate
> further and see what major/minor change to the library caused the objects
> to no longer unpickle.

How does one get that list?  No matter what else happens, the doctests don't show what happens on failure and how one uses this to debug.  That's what they are there for.

Nick


---

Attachment

this addresses the referee's remarks.


---

Attachment

an official pickle jar from sage-3.0.3 made on ubuntu 64-bit (sagemath.org)


---

Attachment


---

Comment by ncalexan created at 2008-07-06 20:01:30

I still want to see doctests that show a failing unpickle, but this is still good and should be applied.  Positive review from me.


---

Comment by mabshoff created at 2008-07-07 03:34:15

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 03:34:15

Resolution: fixed


---

Attachment
