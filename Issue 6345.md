# Issue 6345: load/attach do not recursively preparse files when run in interpreter

Issue created by migration from https://trac.sagemath.org/ticket/6345

Original creator: ddrake

Original creation time: 2009-06-17 00:51:06

Assignee: was

CC:  mvngu

Keywords: preparse ipython attach load

From http://groups.google.com/group/sage-support/browse_thread/thread/9aa4fa8cdb5d8b90:


```
After a lot of headaches over some mysterious behaviour in some
scripts, I found the following:
I have two files:
test1.sage contains:
attach test2.sage
print "test1", 1/2

test2.sage contains:
print "test2", 1/2

When I say on the command line of sage 3.3: attach test1.sage, the
output is (correctly):
sage: attach test1.sage
test2 1/2
test1 1/2

But on sage 4.01, the output is:
sage: attach test1.sage
test2 0
test1 1/2

It looks as if on a file that is attached from another attached file,
no preparsing takes place. If within this same session I touch
test2.sage, it works fine. 
```


This is only a problem in the IPython interpeter; when running from the command line, the files are recursively preparsed correctly.


---

Comment by ddrake created at 2009-06-17 01:05:55

Just briefly looking around, perhaps there's a problem in `preparse_file()` in `sage.misc.preparser`: when attaching a .sage file, it does:

```
elif name_load[-5:] == '.sage':
                try:
                    G = open(name_load)
                except IOError:
                    print "File '%s' not found, so skipping load of %s"%(name_load, name_load)
                    i += 1
                    continue
                else:
                    A = A[:i] + G.readlines() + A[i+1:]
                    continue
```

In the example given in this ticket, it seems to just insert the lines of test2.sage without preparsing them.


---

Comment by mpatel created at 2010-01-20 11:13:10

This appears to be fixed, post-#7514.  For example, with

```sh
> cat test1.sage 
attach test2.sage
print "test1", [1..10]
> cat test2.sage 
print "test2", [11..20]
```

I see

```python
sage: attach test1.sage
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: attached_files()
['test1.sage', 'test2.sage']
sage: # After 'touch test2.sage'
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sage: # After 'touch test1.sage'
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

If I'm correct, should we close this ticket?


---

Comment by mpatel created at 2010-01-20 11:13:10

Changing status from new to needs_info.


---

Comment by mvngu created at 2010-02-05 19:57:00

Close as fixed by #7514:

```
[mvngu@sage sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: attach test1.sage
test2 1/2
test1 1/2
sage: attach test3.sage
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: !touch test2.sage
sage: attach test1.sage
test2 1/2
test2 1/2
test1 1/2
sage: !touch test4.sage
sage: attach test3.sage
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: !more test1.sage
attach test2.sage
print "test1", 1/2
sage: !more test2.sage
print "test2", 1/2
sage: !more test3.sage
attach test4.sage
print "test3", [1..10]
sage: !more test4.sage
print "test4", [1..10]
```



---

Comment by mvngu created at 2010-02-05 19:57:00

Resolution: fixed
