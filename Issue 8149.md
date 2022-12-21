# Issue 8149: files with space in their names do not load properly

Issue created by migration from Trac.

Original creator: rkirov

Original creation time: 2010-02-02 07:30:10

Assignee: tbd

Thanks to the load/attach rewrite most of the weirdness is gone. My only issue left is that files with space in their names somehow only work with the depreciated style of calling load. This behavior is the same in prompt and notebook.


```
sage: t=tmp_filename()+' space.py'; open(t,'w').write("print 'hello world'")
sage: load t
hello world
sage: load(t)
---------------------------------------------------------------------------
ValueError  
```


I should be able to fix this soon, as probably it is a minor tweak, but if anyone wants to go ahead...


---

Comment by rkirov created at 2010-02-26 07:16:30

ok, the culprit is in sage.misc.preparser.load 


```
    try:
        filename = eval(filename, globals)
    except Exception:
        # handle multiple input files separated by spaces, which was
        # maybe a bad idea, but which we have to handle for backwards
        # compatibility.
        v = filename.split()
        if len(v) > 1:
            for file in v:
                load(file, globals, attach=attach)
            return
```


so I guess any fix for files with spacebars will break the backwards compatibility :/ Maybe for Sage 4 we can go away with backwards compatibility on this issue (also maybe remove 'eval'). The new load() already has capabilities of loading multiple files. Consider 

1) load('file1.py file2.py')
2) load('file1.py','file2.py')

2) looks more pythonic to me.


---

Comment by jdemeyer created at 2015-03-25 16:28:19

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-03-25 16:28:19

This works correctly now (with a doctest in `src/sage/repl/load.py`)


---

Comment by jdemeyer created at 2015-03-25 16:28:23

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-03-25 19:21:10

Resolution: fixed
