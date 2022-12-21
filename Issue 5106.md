# Issue 5106: preparse bug with time and generator assignment naming

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-26 19:10:38

Assignee: cwitty

CC:  boothby mhansen

The Sage `.<a>` notation doesn't properly deal with `time foo`.


```
sage: time K.<a> = GF(9)
------------------------------------------------------------
   File "<timed exec>", line 1
     K = GF(Integer(Integer(9)),names=(u'a',)); (a,) = time K._first_ngens(Integer(1))
                                                            ^
SyntaxError: invalid syntax
```


Note that the Ipython magic %time works fine:

```
sage: %time K.<a> = GF(9)
CPU times: user 0.11 s, sys: 0.09 s, total: 0.19 s
Wall time: 2.17 s
```





---

Comment by robertwb created at 2009-01-27 23:52:50

Simplifies the generator and calculus preparsing, fixing the above bug. Depends on #5079.


---

Comment by mabshoff created at 2009-02-11 08:08:38

This would be nice to have in 3.3. Can someone review this?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 08:18:11

One ought to check if this patch fixes #4454.

Cheers,

Michael


---

Comment by boothby created at 2009-02-13 20:50:23

works for me


---

Comment by mabshoff created at 2009-02-14 01:52:25

Hmm, I have the dependency applies, but the patch does not apply:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5106-preparse-gens.patch 
patching file sage/misc/preparser.py
Hunk #7 FAILED at 739.
Hunk #8 FAILED at 825.
2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
```

Can someone rebase for 3.3.rc0?

Cheers,

Michael


---

Comment by mhansen created at 2009-02-15 04:20:42

Robert, what is the patch based on?  I can't get it to apply to 3.2.3 or 3.3.alpha1/2 ?


---

Comment by robertwb created at 2009-02-15 05:22:38

It's based on 3.2.3, with #5079, and perhaps another patch or two. I haven't upgraded to the latest alpha yet, which is why I haven't rebased this. I'll look into that later tonight if someone else doesn't beat me to it.


---

Comment by robertwb created at 2009-02-15 09:01:19

Changing assignee from cwitty to was.


---

Comment by robertwb created at 2009-02-15 09:01:19

Changing component from misc to user interface.


---

Comment by robertwb created at 2009-02-15 09:08:20

The rebase issue was #4405, which was independently resolved by this patch.


---

Attachment


---

Comment by mabshoff created at 2009-02-15 13:50:50

Hi Robert,

this patch is either not the right one or something else went wrong since it does not apply:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < 5106-preparse-gens.patch 
patching file sage/misc/preparser.py
Hunk #7 FAILED at 739.
Hunk #8 FAILED at 825.
2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
```


At SD 12 there were some issues merging the preparser patches including #4405, so it sounds like a very good idea to rebase this against 3.3.rc1 which will be out by the time you get this email on Monday :).

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-02-17 06:37:55

OK, new patch rebased against 3.3rc1


---

Comment by mhampton created at 2009-02-17 11:45:45

New patch applied cleanly, and works on the commandline, but I get this error in the notebook when trying to time anything:


```
time a = number_of_partitions(10^6)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mh/.sage/sage_notebook/worksheets/admin/182/code/1.py", line 9, in <module>
    _time__=misc.cputime(); __wall__=misc.walltime(); a = number_of_partitions(_sage_const_10 **_sage_const_6 ); print "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
  File "/Users/mh/sagestuff/sage-3.3.rc0/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
NameError: name '__time__' is not defined
```



---

Comment by robertwb created at 2009-02-17 11:51:13

Hmm... I'll look at this in a moment.


---

Attachment

OK, I've resolved the issue above.


---

Comment by mabshoff created at 2009-02-17 19:50:24

Resolution: fixed


---

Comment by mabshoff created at 2009-02-17 19:50:24

Merged

 * 5106-preparse-gens-rebase.patch
 * 5106-fix.patch

in Sage 3.3.rc2.

Cheers,

Michael
