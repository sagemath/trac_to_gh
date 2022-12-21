# Issue 6340: var('x',ns=False)  -- should go boom but silently gives a new symbolic variable

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 19:22:25

Assignee: burcin


```
sage: type(var('x',ns=False))
<type 'sage.symbolic.expression.Expression'>
```



---

Comment by was created at 2009-06-16 19:25:48

The fix should be to raise a DeprecationError... or possibly just a NotImplementedError...


---

Comment by kcrisman created at 2009-08-26 16:51:32

This raises a NotImplementedError for ns=False, but still creates the variable for ns=1 or ns=True, with a verbose level 0 message.


---

Comment by gmhossain created at 2009-09-05 21:55:19

Patch at #6559 enhances symbolic variables definition. Unfortunately, the patch there
will conflict with the patch here.


---

Comment by kcrisman created at 2009-09-06 02:26:19

It looks like #6559 functionality is better to incorporate first.  What happens after its inclusion with the following?

```
sage: var('z',ns=False)
```


```
sage: var('z',ns=True)
```

The results of these will help create a new patch, though that may not happen for a bit.  

Alternately, since this one is small, one could review it positively (if it deserves to be) :) and then base the bigger patch at #6559 on it.


---

Comment by kcrisman created at 2009-09-21 15:15:36

Based on 4.1.1 and #6559


---

Attachment

Depending on which one is reviewed first, here's a patch on top of #6559.  Should work identically.


---

Comment by jason created at 2009-09-22 15:56:49

This should use the deprecation function instead of the verbose function.

For example (from matrix_rational_dense.pyx)


```
        from sage.misc.misc import deprecation
        deprecation("'invert' is deprecated; use 'inverse' instead.")
```



---

Comment by burcin created at 2009-09-22 17:48:33

I think `NotImplementedError` is OK for `ns=False`, but we should use a deprecation warning for `ns=1`.


---

Comment by kcrisman created at 2009-09-22 18:31:59

This makes sense.  I've updated the first patch as per Burcin's idea, which seems most appropriate.


---

Comment by burcin created at 2009-09-22 18:57:50

Sorry for not pointing this out earlier, but I suggest changing the block:


```
    if ('ns', False) in kwds.items(): 
        raise NotImplementedError, "The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer." 
    if ('ns', True) in kwds.items(): 
        from sage.misc.misc import deprecation 
        deprecation("The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.") 
```


with


```
    if kwds.has_key('ns'):
        if kwds['ns']:
            from sage.misc.misc import deprecation 
            deprecation("The new (Pynac) symbolics are now the only symbolics; please do not use keyword 'ns' any longer.") 
        else:
            raise NotImplementedError, "The new (Pynac) symbolics are now the only symbolics; please do not use keyword `ns` any longer." 
```


Even if `kwds` is expected to be empty, it is a waste to call `.items()`.

Putting a check that `*args` is empty would also help. Dropping arguments silently is not very user friendly.


---

Comment by kcrisman created at 2009-09-22 19:02:46

Yes, I knew there was a more elegant way to do it, but didn't have time to look it up.  As for *args, I think I can safely get rid of that completely, since there are no args, only keywords.  Patch coming up.


---

Comment by kcrisman created at 2009-09-22 19:43:34

Based on 4.1.2.alpha2


---

Attachment

This should take care of it, I hope.


---

Attachment

more doctest fixes


---

Comment by burcin created at 2009-09-22 22:45:29

Looks good to me. AFAICT, there were two more places using the `ns=1` option. attachment:trac_6340-missing_bits.patch should take care of them.

Apply only

 * attachment:trac_6340-var-ns.patch
 * attachment:trac_6340-missing_bits.patch


---

Comment by kcrisman created at 2009-09-23 00:56:10

To release manager:  the "missing bits" may be covered in other patches reviewed related to symbolics, so do not merge if that one won't merge (simple enough!).


---

Comment by mvngu created at 2009-09-24 08:29:46

Resolution: fixed


---

Comment by mvngu created at 2009-09-24 08:29:46

Merged `trac_6340-var-ns.patch`.


---

Comment by mvngu created at 2009-09-27 10:17:03

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
