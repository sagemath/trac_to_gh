# Issue 3763: [with patch, needs review] add conversions from AA/QQbar to standard types

Issue created by migration from https://trac.sagemath.org/ticket/3763

Original creator: cwitty

Original creation time: 2008-08-03 00:28:15

Assignee: somebody

This was triggered by a comment from Jason Grout on IRC a couple of weeks ago.

Currently several of the conversions that "ought to be there", like CDF(QQbar(3)), are missing.

This patch adds conversions and tests, so that all of the conversions from AA/QQbar to float,complex,RDF,CDF,RR,CC,RIF,CIF,ZZ,QQ do the right thing.


---

Attachment

I applied the patch to 3.1.alpha0.  It worked though this message appeared:

```
patching file sage/rings/qqbar.py
Hunk #1 succeeded at 122 with fuzz 2 (offset 0 lines).
```


I tested the file sage/rings/qqbar.py and found the following failure:

```
sage -t  devel/sage-qqbar/sage/rings/qqbar.py               **********************************************************************
File "/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py", line 368:
    sage: convert_test_all(RIF)
Expected:
    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, None]
Got:
    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], None]
**********************************************************************
File "/home/john/tmp/sage-3.1.alpha0/tmp/qqbar.py", line 370:
    sage: convert_test_all(CIF)
Expected:
    [42.000000000000000?, 3.142857142857143?, 1.618033988749895?, -13.000000000000000?, 1.6181818181818183?, -2.645751311064591?, 0.3090169943749475? + 0.9510565162951536?*I]
Got:
    [[42.000000000000000 .. 42.000000000000000], [3.1428571428571427 .. 3.1428571428571433], [1.6180339887498946 .. 1.6180339887498950], [-13.000000000000000 .. -13.000000000000000], [1.6181818181818181 .. 1.6181818181818184], [-2.6457513110645908 .. -2.6457513110645902], [0.30901699437494739 .. 0.30901699437494746] + [0.95105651629515353 .. 0.95105651629515365]*I]
```


The code looks reasonable to me, but some work is needed.  On second thoughts, looking at the "expected" output it seems that this patch relies on another -- the one where the output format ending in ? is introduced.  I'll go looking for that...


---

Comment by mabshoff created at 2008-08-08 20:57:37

John,

that "question mark" patch is #3757, which has been merged in Sage 3.1.alpha1 - out hopefully tonight.

Cheers,

Michael


---

Comment by cremona created at 2008-08-08 21:16:25

OK, I applied also the two patches from #3757 and now the tests pass, so I am happy to endorse this patch too.


---

Comment by mabshoff created at 2008-08-08 22:40:48

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-08 22:40:48

Resolution: fixed
