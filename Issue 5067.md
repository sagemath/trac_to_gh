# Issue 5067: linear_code -- four doctest failures in specture method='leon' exposed by #4588

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-23 09:26:08

Assignee: rlm

When doing #4588 to fix some "doctests never got run" stuff, I discovered exactly one case of some wrong non-optional doctests that weren't being run. 

They are in linear_code.py:


```
sage -t  devel/sage/sage/coding/linear_code.py
**********************************************************************
File "/space/wstein/build/sage-3.3.alpha0/devel/sage-main/sage/coding/linear_code.py", line 1984:
    sage: C.spectrum(method="leon")
Expected:
    [1, 0, 0, 7, 7, 0, 0, 1]
Got:
    [0, 0, 0, 0, 0, 0, 0, 0]
**********************************************************************
File "/space/wstein/build/sage-3.3.alpha0/devel/sage-main/sage/coding/linear_code.py", line 1988:
    sage: C.spectrum() == C.spectrum(method="leon")
Expected:
    True
    #[1, 0, 0, 104, 468, 1404, 4056, 8424, 11934, 13442, 11232, 5616, 2080, 288]
Got: 
    False
**********************************************************************
File "/space/wstein/build/sage-3.3.alpha0/devel/sage-main/sage/coding/linear_code.py", line 1993:
    sage: C.spectrum() == C.spectrum(method="leon")
Expected:
    True
    #[1, 0, 0, 80, 120, 264, 160]
Got: 
    False
**********************************************************************
File "/space/wstein/build/sage-3.3.alpha0/devel/sage-main/sage/coding/linear_code.py", line 1998:
    sage: C.spectrum() == C.spectrum(method="leon")
Expected:
    True
    #[1, 0, 0, 336, 1680, 9072, 26544, 45744, 34272]
Got: 
    False
**********************************************************************
1 items had failures:
   4 of  17 in __main__.example_44
```



---

Comment by was created at 2009-01-23 09:34:15

Changing priority from blocker to major.


---

Comment by wdj created at 2009-01-24 02:25:35

Applies cleanly to 3.3.alpha1.

However, it seems to still fail doctests:


```

./sage -t -optional /home/wdj/sagefiles/sage-3.3.alpha1/devel/sage-spectrum/sage/coding/linear_code.py                                                                                          
sage -t -optional "devel/sage-spectrum/sage/coding/linear_code.py"                                                 
**********************************************************************                                             
File "/home/wdj/sagefiles/sage-3.3.alpha1/devel/sage-spectrum/sage/coding/linear_code.py", line 1975:              
    sage: C.spectrum() == C.spectrum(method="leon")                                                                
Expected:                                                                                                          
    True                                                                                                           
    #[1, 0, 0, 104, 468, 1404, 4056, 8424, 11934, 13442, 11232, 5616, 2080, 288]                                   
Got:                                                                                                               
    True                                                                                                           
**********************************************************************                                             
File "/home/wdj/sagefiles/sage-3.3.alpha1/devel/sage-spectrum/sage/coding/linear_code.py", line 1980:              
    sage: C.spectrum() == C.spectrum(method="leon")                                                                
Expected:
    True
    #[1, 0, 0, 80, 120, 264, 160]
Got:
    True
**********************************************************************
File "/home/wdj/sagefiles/sage-3.3.alpha1/devel/sage-spectrum/sage/coding/linear_code.py", line 1985:
    sage: C.spectrum() == C.spectrum(method="leon")
Expected:
    True
    #[1, 0, 0, 336, 1680, 9072, 26544, 45744, 34272]
Got:
    True
**********************************************************************
```



---

Attachment


---

Comment by rlm created at 2009-01-24 04:12:55

OK, I've updated the patch. Please try again.


---

Comment by wdj created at 2009-01-24 13:19:02

Applies cleanly to 3.3.alpha1 and all tests pass. I also looked at the code and the patch. It looks like a more concise revision of the original code and a (presumably more intelligent) revision of the process of opening and closing files which you have to read+write to for Leon's binaries.

Thanks Robert!


---

Comment by mabshoff created at 2009-01-24 15:29:36

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 15:29:36

Merged in Sage 3.3.alpha2
