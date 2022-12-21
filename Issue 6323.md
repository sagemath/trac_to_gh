# Issue 6323: optional doctest failure -- problem in species code (easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:53:29

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/combinat/species/library.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 55:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 62:
    sage: number, name, sseq = sloane_find(seq)[0]    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 101:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/combinat/species/library.py", line 135:
    sage: number, name, sseq = sloane_find(seq)[0]                    #optional
Expected nothing
Got:
    Searching Sloane's online database...
**********************************************************************
3 items had failures:
   2 of  12 in __main__.example_1
   1 of  12 in __main__.example_2
   1 of   9 in __main__.example_3
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_library.py
	 [6.9 s]
```



---

Comment by mhansen created at 2013-06-21 15:28:39

Changing status from new to needs_review.


---

Comment by mhansen created at 2013-06-21 15:28:39

Changing priority from major to trivial.


---

Comment by mhansen created at 2013-06-21 15:28:39

Changing component from packages: optional to combinatorics.


---

Attachment


---

Comment by ncohen created at 2013-06-25 12:37:21

Helloooooooooo !!!

Could you please change the "#optional" tag to "# optional - internet" ? It will never be run otherwise `:-)`

Nathann


---

Comment by ncohen created at 2013-06-27 17:08:20

Changing status from needs_review to positive_review.


---

Attachment

Hmmmmmm... The doctests do not pass because of a bug in Sage's interface with sloane, and #10358 fixes the file anyway !

Nathann


---

Comment by jdemeyer created at 2013-08-13 08:46:11

Resolution: duplicate
