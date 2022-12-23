# Issue 5693: sloane_sequence -- very confusing error message

Issue created by migration from https://trac.sagemath.org/ticket/5693

Original creator: was

Original creation time: 2009-04-06 17:00:21

Assignee: cwitty

The "sloan_sequence" command fails on every input I give it, whereas sloan_find works fine!

```
sage: sloane_sequence(prime_range(100))
Searching Sloane's online database...
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/4529/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/databases/sloane.pyc in sloane_sequence(number)
    302     results = sloane_find('id:A%s'%number)
    303     if len(results) == 0:
--> 304         raise ValueError, "sequence '%s' not found"%number
    305     return results[0]
    306 

ValueError: sequence '[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]' not found
sage: print sloane_find(prime_range(100))
Searching Sloane's online database...
[[40, 'The prime numbers.', [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
```


Doh -- on checking the docs it appears that sloane_sequence takes a sequence number... and it just happens to be perfectly fine letting that "number" be a list.  Much better type checking would save a lot of confusion.


---

Comment by was created at 2009-04-06 17:07:45

To test the attached patch, apply it, then do


```
 ./sage -t --only_optional=internet devel/sage/sage/databases/sloane.py 
```


and



```
 ./sage -t devel/sage/sage/databases/sloane.py 
```



---

Attachment


---

Comment by jsp created at 2009-04-06 17:49:17

Patch is ok for me.

So a positive review.

Jaap


---

Comment by mabshoff created at 2009-04-09 09:52:45

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 09:52:45

Resolution: fixed
