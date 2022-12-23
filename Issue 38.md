# Issue 38: bug in notebook (too much text clipped)

Issue created by migration from https://trac.sagemath.org/ticket/38

Original creator: was

Original creation time: 2006-09-12 23:30:56

Assignee: somebody

*bug in notebook: 

```
  sage: sys.stdout.write('hi there')
  sage: sys.stdout.flush()
  hi ther
      ^^^^ ----- where's the e!!
```



---

Comment by boothby created at 2006-09-14 18:40:16

Try the following:

```
sys.stdout.write('hi there')
sleep(2)
```

While sage is sleep()ing, you'll see the full text.  When it finishes, the e disappears.  ?????


Messing with stdout from the notebook seems like a categorically bad idea.  I've found that any of the following commands cause the notebook to hang.


```
sys.stdout.close()
sys.stdout.next()
sys.stdout.read()
```


I have found a trivial workaround.  If we tack an extra print statement onto the end, it works fine.  But why do we have to do this?  Mysterious. 

```
  sage: sys.stdout.write('hi there')
  sage: print
  hi there
         ^ ----- w00t
```



---

Comment by was created at 2006-10-15 17:57:14

Fixed.

There was some interaction between the code that asks for an updated list of variables that have been defined and this problem.  

I changed a few lines in sage/server/notebook/worksheet.py to the following:


```
        if not C.introspect():
            input += 'print "\\n\\n%s'%SAGE_VARS + '=%s"%_support_.variables(True)'
```



---

Comment by was created at 2006-10-15 17:57:14

Resolution: fixed
