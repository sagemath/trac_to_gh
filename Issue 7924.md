# Issue 7924: Notebook trims trailing underscores from output.

Issue created by migration from https://trac.sagemath.org/ticket/7924

Original creator: robertwb

Original creation time: 2010-01-14 04:16:48

Assignee: was

Try


```
print "___x___"
```


In a notebook cell. 


---

Comment by mpatel created at 2010-01-15 22:19:08

More data:

```python
sage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation 
sage: wp = WorksheetProcess_ExpectImplementation() 
sage: wp.execute('print "___x___"')
sage: wp.output_status()
Output Status:
        output: '___x'
        filenames: []
        done: True
```



---

Comment by mpatel created at 2010-01-15 22:37:57

[str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip)


---

Comment by mpatel created at 2010-01-15 22:40:54

This may be a duplicate of #7663.


---

Comment by mpatel created at 2010-01-15 23:08:19

The patch at #7663 should fix this.  If it does and that ticket merges, please close this one.


---

Comment by timdumol created at 2010-01-19 03:15:53

Works with sagenb-0.6.


---

Comment by timdumol created at 2010-01-19 03:15:53

Resolution: duplicate
