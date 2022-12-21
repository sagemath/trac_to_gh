# Issue 5174: _repr_ for large matrices should indicate how to see the entries

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-04 15:38:28

Assignee: was


```
[09:30] <jason-> on the other hand, I always get frustrated trying to see a 30x30 matrix in Sage
[09:30] <wstein> print a.str()
[09:30] <jason-> yeah, I never remember it.
[09:30] <wstein> That will show you any matrix in sage of any size.
[09:31] <wstein> Well then the output of a._repr_() should mention it so you can remember it.  make a ticket.
[09:31] <jason-> good point.
[09:31] <jason-> I think I usually end up doing a.rows()
[09:32] <jason-> or list(a)
[09:32] <jason-> so you're saying print a should do:
[09:32] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, do print a.str())
[09:33] <wstein> Yep.
[09:33] <jason-> 30 x 30 dense matrix over Integer Ring (to see the entries, type "print a.str()")
[09:33] <wstein> Of course it's possibly confusing since "a.str()" is really "yourvar.str()"
[09:33] <wstein> but hopefully people can understand that.
```



---

Comment by was created at 2009-12-11 23:29:06

Idea:


```
sage: obj = random_matrix(ZZ,100)
sage: str(obj) + " ('print obj.str()' to see all entries)"
```



---

Comment by was created at 2009-12-11 23:30:54

Change this function in matrix/matrix0.pyx:

```
    def __repr__(self):
        if self._nrows < max_rows and self._ncols < max_cols:
            return self.str()
        if self.is_sparse():
            s = 'sparse'
        else:
            s = 'dense'
        return "%s x %s %s matrix over %s"%(self._nrows, self._ncols, s, self.base_ring())
```



---

Comment by jhpalmieri created at 2009-12-12 20:18:39

Changing status from new to needs_review.


---

Attachment

Here's a patch.  The docstring to the `__repr__` method for matrices illustrates what the patch does:

```
        EXAMPLES::

            sage: A = matrix([[1,2], [3,4], [5,6]])
            sage: A.__repr__()
            '[1 2]\n[3 4]\n[5 6]'
            sage: print A
            [1 2]
            [3 4]
            [5 6]

        If the matrix is too big, don't print all of the elements::

            sage: A = random_matrix(ZZ, 100)
            sage: A.__repr__()
            "100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)"
            sage: print A
            100 x 100 dense matrix over Integer Ring (type 'print A.str()' to see all of the entries)

        If there are several names for the same matrix, write it as "obj"::

            sage: B = A; print B
            100 x 100 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries)
```


I actually think that this looks a little funny in some situations; for example, in chain_complex.py, the old version did this:

```
            sage: C.differential()
            {0: 40 x 40 dense matrix over Integer Ring, 1: []}
```

while the new version does this:

```
            sage: C.differential()
            {0: 40 x 40 dense matrix over Integer Ring (type 'print obj.str()' to see all of the entries), 1: []}
```

It would be pretty easy to change the print representation so if there were no name attached to the object (e.g., if it were produced by another method, as in this example), then the extra message about "print ..." would be omitted.  Opinions?


---

Comment by was created at 2009-12-13 21:20:03

> It would be pretty easy to change the print representation so
>  if there were no name attached to the object (e.g., if it were 
> produced by another method, as in this example), then the extra 
> message about "print ..." would be omitted. Opinions? 

How do you do that?  I would have no clue.


---

Comment by jhpalmieri created at 2009-12-14 00:01:25

Replying to [comment:4 was]:
> > It would be pretty easy to change the print representation so
> >  if there were no name attached to the object (e.g., if it were 
> > produced by another method, as in this example), then the extra 
> > message about "print ..." would be omitted. Opinions? 
> 
> How do you do that?  I would have no clue.

A web search led me to a code snippet (by Georg Brandl, the author of Sphinx) which more or less searches through the `locals()` dictionary for the object, making a list of the variable names bound to it.   (See the part of the patch for the file sageinspect.py.)  If you exclude the variable names starting with "_", then if the resulting list is empty, you don't print the message.


---

Comment by jhpalmieri created at 2009-12-20 06:32:32

Here's a new version of the patch.  This is similar to the old one, but it behaves like this:

```
     sage: C.differential()
     {0: 40 x 40 dense matrix over Integer Ring, 1: []}
```



---

Attachment

The second patch looks good to me.


---

Comment by mhansen created at 2009-12-27 15:38:23

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:51:32

Resolution: fixed
