# Issue 7694: change pickle jar doctest to make it a bit more robust and flexible...

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-15 23:47:06

Assignee: tbd

Change the pickle jar doctest in devel/sage/sage/structure/sage_object.pyx to:


```
sage: print "x"; sage.structure.sage_object.unpickle_all(std)
x...
Failed to unpickle 0 objects.
```



---

Comment by was created at 2009-12-24 07:07:24

I'm declaring a total feature freeze on sage-4.3.


---

Comment by jhpalmieri created at 2010-04-23 04:57:38

Moved to Sage 5.0.   This still needs a patch...


---

Comment by was created at 2010-06-03 04:09:49

Resolution: fixed


---

Comment by was created at 2010-06-03 04:09:49

Interestingly, I just looked in sage-4.4.3.alpha2, and this is already fixed:

```


    ::

        sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
        sage: print "x"; sage.structure.sage_object.unpickle_all(std)
        x...
        Successfully unpickled ... objects.
        Failed to unpickle 0 objects.
```

Cool.
