# Issue 568: sage -t --long coding/code_constructions.py times out after several *hours*

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-02 17:34:58

Assignee: wdjoyner

There is a doctest (or doctests) in 

```
    sage -t --long coding/code_constructions.py 
```

that take many *hours*.  Run the above with --verbose and fix the doctests so they run in a reasonable
amount of time.  An example that never finishes is broken.


---

Comment by wdj created at 2007-09-06 00:01:30

The following example is in the docstring for ToricCode:

```
sage: C = ToricCode([[0,0],[1,1],[1,2],[1,3],[1,4],[2,1],[2,2],[2,3],[3,1],[3,2],[4,1]],GF(8,"a"))
sage: C
Linear code of length 49, dimension 11 over Finite Field in a of size 2^3
sage: C.minimum_distance()  ## long time -- very time consuming
28
```

I assumed that the tester would ignore commands with a "## long time -- very time consuming" comment. If not, this could definitely bog this test down. 
I'll keep investigating this though.


---

Comment by wdj created at 2007-09-06 00:06:12

That was it. It replaced 

```
sage: C.minimum_distance()  ## long time -- very time consuming
```

by

```
sage.:. C.minimum_distance()  ## long time -- very time consuming
```

and then the following was the result of sage -t:

```
wdj`@`wooster:~/sagefiles/sage-2.8.3.rc3> ./sage -t --long "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage/sage/coding/code_constructions.py"
sage -t --long devel/sage-main/sage/coding/code_constructions.py
         [11.6 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.6 seconds
```

It appears that the sage -t test is behaving differently since at one time this
"long time" comment would be passed over by sage -t. Is this new 
behavior intentional? If yes, I'll submit a patch. If not, then the file can 
stay as is.


---

Comment by wdj created at 2007-09-06 01:23:57

I fixed the docstring to that sage -t --long doesn't time out.

```

 wdj`@`wooster:~/sagefiles/sage-2.8.3.rc3> ./sage -t --long "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-coding/sage/coding/code_constructions.py"
sage -t --long devel/sage-coding/sage/coding/code_constructions.py
         [12.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 12.4 seconds
```



---

Comment by was created at 2007-09-06 17:21:03

Resolution: fixed


---

Attachment

This works.
