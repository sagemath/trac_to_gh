# Issue 2288: tutorial -- fix some typos (easy)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-24 01:18:22

Assignee: wdjoyner


```
Somebody in france found some typos in the tutorial.

Note, they want to change "Magma" to "MAGMA" which is WRONG.
They also want to change "Sage" to "SAGE" which is also wrong -- Sage is no
longer an acronym.
- Hide quoted text -


---------- Forwarded message ----------
From: Mihai Cipu <cipu`@`math.u-strasbg.fr>
Date: Sat, Feb 23, 2008 at 4:03 AM
Subject: SAGE Tutorial Release 2008.01.18
To: wstein`@`gmail.com


Dear William,

 Congratulations for your excellent work!
 To read the tutorial named above I needed
 3h10m wall time (I didn't substract the time
 spent drinking a cup of tea). Let me tell
 what typos I've noticed:

 p.5, l.2 of the second paragraph
   "On some Mac's you..." instead of "One some..."

 p.12, l.2 "comparison" instead of "comparision"

 p.14, l.1  "indeterminate"  instead of "interderminate"

 p.15, l.2 of the first paragraph
         "MAGMA" instead of "Magma"

 p.18, l.1 of the second paragraph
             "Gr\"obner"  instead of "Groebner"

 p.23, l.1 of the first paragraph
        remove "+"   before " tells SAGE"

 p.26, l.1 "Maxima" instead of "maxima"
     l.-1   a blank needed between "\latex" and "format"

 p.30, l.1 of the second paragraph
          "it needs not" instead of "it need not"

 p.35, l. 2 of Subsection 2.10.2
          "one can use" instead of "obe can use"

 p.36, l.8, 13   "transform" instead of "transforms"

 p.37, l.3   "can be plotted" instead of "and be plotted"

 p.39, l.2, 16   "PARI" instead of "pari"
     l.3, 19   "Maxima" instead of "maxima"

 p.45, l.-8  "Maple" instead of "maple"

 p.55, l.4  of the Help on class VectorSpace
             "To create" instead of "Two create"

 p.59, l.-4    "SAGE"   instead of "sage"

 p.61, l.6, 7, 10, 11   "GAP"  instead of "Gap"  or "gap"

 p.69, l.3, 7  of Subsection  5.2.1
        double opening quotes needed

 p.85, l.2, 4  from the second paragraph of Section 6.2
      "GAP" instead of "Gap"

 p.86, l.3 of the first paragraph of Section 6.3
       remove the  point after "you used"
     l.5  "GAP"  instead of "Gap"


 Now it's time time to have fun with SAGE!

 Best regards,
 Mihai
```



---

Attachment


---

Comment by wdj created at 2008-02-24 22:15:32

The patch fixes the valid typos reported above.


---

Comment by mabshoff created at 2008-02-24 22:17:48

Does this patch depend or conflict in any way with #2289?

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-26 02:02:33

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-26 02:03:33

Resolution: fixed


---

Comment by mabshoff created at 2008-02-26 02:03:33

Merged in Sage 2.10.3.alpha0
