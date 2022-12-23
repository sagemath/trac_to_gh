# Issue 8438: Construction of a skew partition from its row and column lengths

Issue created by migration from https://trac.sagemath.org/ticket/8438

Original creator: hivert

Original creation time: 2010-03-04 20:42:23

Assignee: hivert

CC:  nborie

Keywords: skew partitions


```
sage: print from_row_and_column_length([3,1,2,2],[2,3,1,1,1]).diagram()
         ###
        #
       ##
       ##
```



---

Comment by hivert created at 2010-03-04 20:44:37

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-05 18:02:23

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-03-05 18:02:23

Can you improve that : 


```
sage: S = SkewPartition(([6],[6])) 
sage: S.column_lengths()
[0, 0, 0, 0, 0, 0]
sage: S.row_lengths()
[0]
sage: from_row_and_column_length([0],[0,0,0,0,0,0]) 
[[6], [6]] #perfect

sage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))
sage: S.column_lengths()
[0]
sage: S.row_lengths()
[0, 0, 0, 0, 0, 0]
sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
...
ValueError: invalid skew partition
```



---

Comment by nborie created at 2010-03-05 18:30:27

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-03-05 18:30:27

Sorry,

I don't know which behaviour you want for the last example I gave...

I ran : 

```
sage: for i in range(10):
....:     for S in SkewPartitions(i):
....:         if S != from_row_and_column_length(S.row_lengths(),S.column_lengths()):
....:             print S
....:             
sage:
```

That works! For the example comming from my last comment... I don't know.

Otherwise, the patch is correct (apply, test and doc.). I am not an expert with Skew Partitions...


---

Attachment


---

Comment by hivert created at 2010-03-10 08:37:50

Replying to [comment:2 nborie]:
> Can you improve that : 
> 

```
sage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))
sage: S.column_lengths()
[0]
sage: S.row_lengths()
[0, 0, 0, 0, 0, 0]
sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
...
ValueError: invalid skew partition
```

The cases with 0 row and columns length are ambiguous (see the example in the doc). I now raise a proper error:

```
sage: sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: row and column length must be positive
```

I re-uploaded the new patch ! Please review.


---

Comment by nborie created at 2010-03-10 10:41:25

Ok, no more corner case from my point of view....

The patch apply, the doc is perfect, all test passed. The rst construction with ..warning:: produces a very very nice html output.

Positive review from me.


---

Comment by nborie created at 2010-03-10 10:41:25

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:52:13

Merged "trac_8438-skew_partitions_from_rc_lenghts-fh.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:52:13

Resolution: fixed
