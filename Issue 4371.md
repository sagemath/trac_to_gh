# Issue 4371: Add support for lazy attributes via a decorator

Issue created by migration from https://trac.sagemath.org/ticket/4371

Original creator: nthiery

Original creation time: 2008-10-26 13:30:55

Assignee: cwitty

The lazy-attribute-...-nt patch on the sage-combinat patch servers is a first implementation of lazy attributes (see the doc in the patch).
Comments and alternative implementations welcome! See the current caveats in the doc

Cheers,
								Nicolas


---

Comment by nthiery created at 2008-10-26 13:33:17

Patch


---

Attachment

In case I did not make myself clear: this patch is *not* ready for insertion in sage.
It's more of a request for comments!


---

Comment by mvngu created at 2008-10-26 23:44:59

Replying to [comment:1 nthiery]:
> In case I did not make myself clear: this patch is *not* ready for insertion in sage.
> It's more of a request for comments!


Here are some possible fixes for improving the documentation of the patch *lazy_attributes-4371-nt.patch*:



1.

```
-easilly override a given attribute; you don't need to call the
+easily override a given attribute; you don't need to call the
```




2.

```
-the internal dictionnary of the object:
+the internal dictionary of the object:
```



Otherwise, the doc looks OK to me.


---

Comment by nthiery created at 2008-10-27 10:55:41

Fixes applied. Thanks. Lazy attributes now work well with new style classes:

http://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch


---

Comment by mvngu created at 2008-10-27 11:30:23

Replying to [comment:3 nthiery]:
> Fixes applied. Thanks. Lazy attributes now work well with new style classes:
> 
> http://sage.math.washington.edu:2144/file/03b4130fb25d/lazy_attributes-4371-nt.patch


For your new patch at the above URL, here's a fix to improve your documentation:

```
-Invoking Descriptors in the python reference manual).
+Invoking Descriptors in the Python reference manual).
```



---

Comment by mabshoff created at 2008-10-30 17:37:20

Nicolas,

should this patch be reviewed?

Cheers,

Michael


---

Comment by nthiery created at 2008-11-09 21:10:15

Changing status from new to assigned.


---

Comment by nthiery created at 2008-11-09 21:10:15

Changing assignee from cwitty to nthiery.


---

Comment by nthiery created at 2008-11-09 21:10:15

Comments on it are more than welcome (in particular for the hasattr feature).
No need to waste time on a complete final review though.

Thanks,
			Nicolas


---

Comment by nthiery created at 2009-02-13 16:12:06

Ready for review.
Not all desired features are implemented, but we need the bulk for upcoming patches.


---

Attachment


---

Comment by rlm created at 2009-02-14 00:26:20

Apply `lazy_attributes-4371-nt.2.patch` only.


---

Comment by mabshoff created at 2009-02-14 02:16:29

For the record note that 

 * `__init___`
 * `__get__`

do not have doctests, but this will not stop the merge in this case :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 02:29:51

Merged lazy_attributes-4371-nt.2.patch in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 02:29:51

Resolution: fixed


---

Comment by nthiery created at 2009-02-14 18:33:57

Thanks Michael and Robert.

Michael: could you please fold the patch into sage-3.3 on the sage-combinat patch server?

Thanks!
