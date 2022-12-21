# Issue 3099: Singular crashes

Issue created by migration from Trac.

Original creator: jxxcarlson

Original creation time: 2008-05-03 21:00:46

Assignee: malb

CC:  polybori dimpase

Singular crashes at degree 13 on intel core duo machine (mac os 10.5.2) when running "fano7.sage" with user command "run2(1,20)".  See attached files (fano7.sage, crash.txt}.  You may want to try "run(12,20)" to get to the crash more quickly.  Also, "run2(19,40)" crashed a quad core ppc machine with 8 gigs of memory.  The crash occurred before there was any significant output.


---

Comment by jxxcarlson created at 2008-05-03 21:01:40

Sage source file


---

Attachment

Crash log


---

Comment by mabshoff created at 2008-05-04 03:32:54

Hi Jim,

this looks related to #3098. Since we have a fix for that issue which will be part of 3.0.1 can you try with it and check if the issue has been fixed? William is trying on a similar setup that also shows #3098, so hopefully he can give us some info here, too.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-04 04:17:23

FYI:

```
me: ok. I just commented on the ticket that it likely would.
So you might want to clue us in that it is not that issue, but a similar problem
 William: Good.
 me: I also think that the "huge" problem he posted might just be that he ran out of RAM.
 William: Line 803 in singular.py would be fixed in a similar way to the fix in my other patch.
We'll find out in a while.
 me: After all: we are running Singular in 32 bit mode on OSX for now.
Now if that mabshoff guy got moving on that issue .... [wink]
 William: Yes, what's holding up the 64-bit port?
 me: Nothing. Just spending my "free" time with lisp, Itanium and other fun stuff.
```


The 64 bit OSX port is a high priority item for us and most problems have been already solved. William and I will likely spend some good time this Sunday and try to get everything merged back into 3.0.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 01:58:21

I had some off list communication with Michael Brickenstein and he recommended using 

```
Hi Michael!

I also use
-with-valloc=system
additionally to
--with-malloc=system

on Mac OS X  (32bit). I had issues with Singular not being able to
allocate much memory (under certain circumstances) a few years ago
and this configuration has proven to be useful.

Best regards,
Michael 
```

I am not sure how Singular normally reacts when running out of memory, but it should obviously never crash.

I am CCing PolyBoRi since Michael B. might enlighten us about this specific problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 01:58:21

Changing assignee from malb to mabshoff.


---

Comment by mabshoff created at 2008-05-29 01:58:21

Changing status from new to assigned.


---

Comment by PolyBoRi created at 2008-05-29 06:04:38

usually I got a clear error message about not being able to allocate more virtual memory (sometimes having only 100MB of memory consumed).
I would recommend to export the actual commands sent to Singular somehow and to reproduce them with the Singular version in fink (and on other platforms).


---

Comment by PolyBoRi created at 2008-05-29 07:06:45

By the way: In Singular it is never checked, if an allocation is successful.
In this case, it usually crashes...
In fact, I was explicitely asked not to check the results of malloc calls...


---

Comment by kcrisman created at 2016-08-08 19:21:46

On a new Mac,

```
degree = 13
Time: CPU 171.29 s, Wall: 171.90 s
5107 [3, 4, 5, 7, 17, 22, 71, 104, 162, 189]
Time: CPU 216.02 s, Wall: 218.62 s
54323 [1, 3, 3, 7, 8, 11, 90, 109, 352]
----------------------------------------------
```

but this is presumably 64-bit.   It would be useful to know if this is still an issue with much larger input on a generic machine. Or is it so old it's wontfix?


---

Comment by mkoeppe created at 2020-04-18 06:49:14

Outdated, should be closed


---

Comment by dimpase created at 2020-04-18 11:09:20

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-04-18 11:09:41

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-18 12:57:50

Resolution: invalid
