# Issue 4549: New method horizontal_border_strip using new IntegerListsLex combinatorial class

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2008-11-19 16:24:29

Assignee: mhansen

CC:  sage-combinat

See the title. Patch integer_lists_lex-nt in development in sage-combinat.


---

Attachment

Reworked the integer lists lexicographic generator into a full featured combinatorial class IntegerListsLex
Use it systematically in Partitions to get constant amortized time iterators.
Also implements horizontal_border_strip.

Note: the attached patch does not contain the commit messages!


---

Comment by saliola created at 2009-02-13 16:45:52

Replying to [ticket:4549 nthiery]:
> See the title. Patch integer_lists_lex-nt in development in sage-combinat.

Note: this patch depends on #4371 and #5255.


---

Comment by nthiery created at 2009-02-14 18:27:43

Changing assignee from mhansen to nthiery.


---

Attachment


---

Comment by mhansen created at 2009-02-14 23:28:44

I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, and changed the default implementation of count to use Integers so that we don't have to reimplemented in IntegerListsLex

Assuming someone okay's my changes, I think both patches are good to go in.


---

Comment by hivert created at 2009-02-15 01:24:20

Replying to [comment:5 mhansen]:
It's ok for me ! The warning is a good idea. Go ahead.


---

Comment by mabshoff created at 2009-02-15 08:37:48

This patch breaks the pickle jar which according to Mike is no surprise:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    ** failed:  _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj
    ** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj
    ** failed:  _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj
    Failed:
    _class__sage_combinat_partition_PartitionsGreatestEQ_nk__.sobj
    _class__sage_combinat_partition_Partitions_constraints__.sobj
    _class__sage_combinat_partition_PartitionsGreatestLE_nk__.sobj
    Successfully unpickled 445 objects.
    Failed to unpickle 3 objects.
**********************************************************************
```


We need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.

Cheers,

Michael


---

Comment by nthiery created at 2009-02-15 22:32:17

Replying to [comment:5 mhansen]:
> I've added a patch which adds some doctests, adds a warning when min_part=0 is passed to partitions, 
Thanks!

> and changed the default implementation of count to use Integers 

Good.

> so that we don't have to reimplemented in IntegerListsLex

We still do! Sorry, I did not comment on this in the code, but the implementation of count differs from
the default one from CombinatorialClass, as it bypasses the call to _element_constructor_!


---

Comment by nthiery created at 2009-02-15 22:35:02

Replying to [comment:8 mabshoff]:
> This patch breaks the pickle jar which according to Mike is no surprise:

Indeed no surprise. 

> We need to make a call if we are going to break this pickles or not. Other than that there were no doctesting issues.

I would tend to break the pickles indeed, unless someone cries very loud for this.

Cheers,
				Nicolas


---

Comment by mabshoff created at 2009-02-16 04:59:59

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael


---

Attachment


---

Comment by nthiery created at 2009-04-02 05:28:00

Updated patch:
 - Now handles pickles of PartitionsGreatestEQ and PartitionsGreatestLE from sage <= 3.4.1.
 - Rebased against 3.4 (and sphinx)


---

Comment by nthiery created at 2009-04-02 05:44:35

I should mention: only the last patch is needed; it integrates the previous ones


---

Comment by hivert created at 2009-04-02 09:49:19

Dear Nicolas,

> I should mention: only the last patch is needed; it integrates the previous ones

The patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:

```
sage: std = os.environ['SAGE_DATA'] + '/extcode/pickle_jar/pickle_jar.tar.bz2'
sage: sage.structure.sage_object.unpickle_all(std)
** failed:  _class__sage_combinat_partition_Partitions_constraints__.sobj
/usr/local/sage/sage/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
  exec code_obj in self.user_global_ns, self.user_ns
Failed:
_class__sage_combinat_partition_Partitions_constraints__.sobj
Successfully unpickled 486 objects.
Failed to unpickle 1 objects.
```

Am I doing something wrong ?

Cheers,

Florent


---

Comment by hivert created at 2009-04-03 16:29:39

Fix for the remaining broken pickle + tests for the other one.


---

Attachment

Dear All,

> The patch looks good to me. However, though I'm not 100% sure I launched the correct check, it seems that one of the old pickle is still broken:

I added a review patch which should fix this remaining pickle problem. If someone reread it I'm ready to give a positive review. 

Florent


---

Comment by nthiery created at 2009-04-04 00:49:33

Thanks Florent for the fix. I had overlooked this pickle. 
Oh, and thanks for pointing out how one can test backward compatibility unpickles :-)

I tried the patch on my machine and it looks and works fine.

So, I allow myself to set the positive review  flag on behalf of Florent!

I also lifted the priority to major, since this gives a large (memory) efficiency gain.


---

Comment by nthiery created at 2009-04-04 00:49:33

Changing priority from minor to major.


---

Comment by hivert created at 2009-04-04 08:29:26

If its still possible, I'd rather see this integrated in 3.4.1, this allows for #5308 being integrated as soon as possible.

Florent


---

Comment by mabshoff created at 2009-04-04 23:56:30

Merged

 * integer_lists_lex-4549-submitted.patch
 * integer_lists_lex-4549-review.patch

in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 23:56:30

Resolution: fixed
