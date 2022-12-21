# Issue 4640: Do not dot out the number of pickles in the pickle jar doctest in sage/structure/sage_object.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-28 03:21:17

Assignee: mabshoff


```
[7:17pm] mabshoff: ws-4083: In the pickle jar doctest the number of pickles is dotted out. Shouldn't we hard code that number and update it every time we do the latest pickle jar?
[7:17pm] ws-4083 is now known as ws-3621.
[7:17pm] ws-3621: mabshoff -- sure, we could.
[7:18pm] ws-3621: I don't see why not.
[7:18pm] ws-3621: good idea.
[7:18pm] mabshoff: mk, ticket coming up.
```



---

Comment by mabshoff created at 2008-12-15 19:13:36

If we are going to update the pickle jar for 3.2.2 we might as well fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 19:18:55

I am seeing two doctest failures, one which could have been caused by my dumb rebase attempt:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests 
sage -t -long devel/sage/sage/combinat/words/word_generators.py # 1 doctests failed
```

In detail: This might be caused by missing pickles in the pickle jar:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/structure/sage_object.pyx", line 371, in __main__.example_16
Failed example:
    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    ** failed:  _class__sage_combinat_word_Words_alphabet__.sobj
    ** failed:  _class__sage_combinat_word_Words_n__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Failed:
    _class__sage_combinat_word_Words_alphabet__.sobj
    _class__sage_combinat_word_Words_n__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Successfully unpickled 448 objects.
    Failed to unpickle 6 objects.
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/combinat/words/word_generators.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/combinat/words/word_generators.py", line 282, in __main__.example_6
Failed example:
    f[:Integer(10000)] == u[:Integer(10000)] #long time###line 286:_sage_    >>> f[:10000] == u[:10000] #long time
Expected:
    True
Got:
    False
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 19:19:34

oops, wrong ticket.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-03-10 20:17:48

Changing status from new to assigned.


---

Comment by was created at 2009-03-10 20:35:45

yes!


---

Comment by mabshoff created at 2009-03-10 20:43:07

Resolution: fixed


---

Comment by mabshoff created at 2009-03-10 20:43:07

Merged in Sage 3.4.final.

Cheers,

Michael
