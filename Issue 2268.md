# Issue 2268: has_coerce_map_from_c performance improvements (patch included)

Issue created by migration from https://trac.sagemath.org/ticket/2268

Original creator: gfurnish

Original creation time: 2008-02-22 22:17:23

Assignee: gfurnish

The following patch "makes the common case fast."  If there is a trivial coercion map this can improve performance by 30x or more.  Furthermore the previous has_key() was not compiling into fast code, this improves it.  It also cleans up the try statement by replacing it with the if statement that maintains backwards compatibility.  This if statement should be eventually removed, but there is a significant body of doctests that fail because code calls has_coerce_map with nonsensical arguments (sometimes self is not a Parent, for instance).  Non-trivial speedups are not as dramatic but still easily measurable in tight loops.  This code has been verified at the .c file level for reference issues and make checked.  


---

Attachment


---

Comment by gfurnish created at 2008-02-22 23:24:02

Changing status from new to assigned.


---

Comment by robertwb created at 2008-02-23 01:53:28

Thanks for your contribution. Actually, the entire coercion model is being re-worked, I think you might find http://wiki.sagemath.org/days7/coercion/ interesting. In particular, this function has been rewritten. 

As far as your code goes, I think you are making things too hard on yourself trying to use the Python C API. Cython will do most of that for you to make your life easier: 


```
if PyObject_RichCompareBool(self, S, Py_EQ)==True: 
```


is faster (and easier to read) as 

```
if self == S:
```

and 

```
PyObject_TypeCheck(self._has_coerce_map_from,NoneType)==1)
```

would be faster if written

```
self._has_coerce_map_from is None
```


Also

```
try:
    return self._has_coerce_map_from[S]
except AttributeError:
    pass
```

Is faster than testing the key first, and then retrieving the object (as that requires two lookups rather than one on success). 

The point that the trivial case should be handled first is a very good one and the new coercion code will do that.


---

Comment by gfurnish created at 2008-02-23 02:51:58

I agree with your points about the None, but I disagree with your comments about try.  The try should not even need to be there, and is there only because code is broken.  Using try as control flow is an expensive idea when the exception gets hit, and in this case it will get hit often from cache misses.  Furthermore, to maintain compatibility with existing code, it is necessary to reset the _has_coerce_map_from attribute in the exception.  This necessitates that the case where there is not a coercion map for the specific key be caught separately, so some type of if statement is needed.  Perhaps the best way to approach it would be to replace the if statement with a if statement based on the result of the Py_GetObject (to eliminate the double lookup).  This was written specifically because the python maps are a major speed bottleneck. Using Py_* manually does give a speed advantage, or at most it doesn't hurt performance. Furthermore when speed is needed, it makes exactly clear what cython is doing, as I've seen too many cases over the last few days where cython inserted a dictionary lookup when it was not necessary (in fact, the has_key in the current version of this is exactly such a case).  I guess this is mostly irrelevant though if the function has already been rewritten, is there a public repository for the new coercion code so that I can use it instead?


---

Comment by gfurnish created at 2008-02-23 06:17:56

patch based off 2.10.2


---

Attachment

While there is a new coercion system coming soon, it seems like a good idea to have a high performance solution until it is released.  This new solution uses a single lookup statement but uses Py* to bypass the try except mechanism to keep speed up.  Unfortunately it has the if statement for backwards compatibility, but with some luck that might be removable before the next release.


---

Attachment


---

Comment by robertwb created at 2008-02-29 01:39:27

Using the Python/C API directly significantly impacts readability, and often doesn't offer any speed improvements. Using a try/except in Cython is free if no error is thrown, which will usually be the case (only once for a given ring will it fail). What you are doing with `PyObject_GetItem` is manually catching and clearing the error (rather than letting Cython do it for you), which is not a huge speed gain. The same can be said of using the `PyObject_RichCompareBool` manually. 

I've attached an alternative patch that is instantly understandable to anyone who knows Python, and should be just as fast (look at the generated C). 

As to the new coercion code, see the bundles/patches on the wiki. The new function is not a plug-in replacement for this one though. 

BTW, the has_key was there to cover up a segfault in a previous version of Pyrex error handling.


---

Comment by gfurnish created at 2008-02-29 06:44:14

This passes tests and I'm happy with the cython output.


---

Comment by mabshoff created at 2008-02-29 19:59:35

Merged 2268-alt.patch in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-02-29 19:59:35

Resolution: fixed
