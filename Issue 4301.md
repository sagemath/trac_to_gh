# Issue 4301: [with patch, needs review] lookup generic methods on category

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-10-15 16:24:55

Assignee: robertwb

CC:  mhansen

No caching is done yet, but it shouldn't be too hard to add at some point. 


---

Attachment

So this patch looks good -- I believe that the code does what it claims to. 

However, there are no doctests. 

So if you say "there are no categories that implement anything like this yet," I believe you -- but let's add one, and put it in the docstring, so that we can use this as an example.


---

Comment by robertwb created at 2009-05-18 21:47:25

See http://sagetrac.org/sage_trac/wiki/CategoriesRoadMap


---

Comment by mhansen created at 2009-10-19 17:32:24

Resolution: invalid


---

Comment by mhansen created at 2009-10-19 17:32:24

I'm going to go ahead and close this as invalid since we decided on another approach for handling these generic method lookups.


---

Comment by robertwb created at 2009-10-19 17:53:50

The other method doesn't work for Cython elements or parents.


---

Comment by mhansen created at 2009-10-19 18:12:18

Hmm... I must have been confused.  I thought we had worked that out in the categories code.

Is this patch still current / relevant?


---

Comment by robertwb created at 2009-10-20 05:48:26

The combinat way of doing things was to make all elements and parents into dynamically generated classes with one half coming from their category and the other half from their implementation. Of course, this makes them Python types, which would be an unacceptable speed regression for, e.g. Integer, so we need some manual lookup in that case. 

What we haven't done is figured out how the these two different approaches would interact, and this should be worked out before applying (some variation of) the above patch.
