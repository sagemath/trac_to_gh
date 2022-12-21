# Issue 5028: point2d? says point.options instead of point2d.options

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-01-19 16:53:26

Assignee: slabbe

Keywords: point2d


```
sage: point2d?
...
Docstring:
    
        A point of size `pointsize' defined by point = (x,y).
        Point takes either a single tuple of coordinates or a list of tuples.
    
        Type point.options to see all options.
    
        EXAMPLES:
            ...

sage: point.options
Traceback (most recent call last):
...
AttributeError: 'function' object has no attribute 'options'
sage: point2d.options
{'alpha': 1, 'faceted': False, 'pointsize': 10, 'rgbcolor': (0, 0, 1)}
```



---

Attachment


---

Comment by mhansen created at 2009-01-20 21:38:14

Looks good to me.


---

Comment by mabshoff created at 2009-01-23 09:40:16

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 09:40:16

Resolution: fixed
