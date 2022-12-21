# Issue 5490: Easter!

Issue created by migration from Trac.

Original creator: psinis

Original creation time: 2009-03-11 22:19:28

Assignee: psinis

CC:  cswiercz

Keywords: finance, dates

Calculates the date for Easter according to any of three methods: Western, Eastern Orthodox, and Julian.

(Critical for future libraries which will introduce business date calculations)


---

Attachment


---

Comment by jsp created at 2009-03-12 02:00:41

What is the use of the date of Easter in the Julian calender? I mean business wise?


---

Comment by psinis created at 2009-03-12 05:43:29

Replying to [comment:2 jsp]:
> What is the use of the date of Easter in the Julian calender? I mean business wise?

I cannot think of a bank holiday that uses the Julian calendar in any major currency.
Checked Russia but even there they are on the new Orthodox calendar.
What is the preference here-- should I remove Julian?


---

Comment by jsp created at 2009-03-12 21:20:12

Replying to [comment:3 psinis]:
> Replying to [comment:2 jsp]:
> > What is the use of the date of Easter in the Julian calender? I mean business wise?
> 
> I cannot think of a bank holiday that uses the Julian calendar in any major currency.
> Checked Russia but even there they are on the new Orthodox calendar.
> What is the preference here-- should I remove Julian?
>  

You should start a discussion on the sage devel list, I think.
There you will find more people who might be interested.

Cheers,

Jaap


---

Comment by cswiercz created at 2009-03-16 00:28:49

Tests pass:


```
sage -t  "devel/sage-5490/sage/finance/easter.py"           
	 [2.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.0 seconds
```


I also manually checked the dates (just in case) for the next several years and all three cases seem to hold.

If this module is going to be critical for future libraries, as the ticket description says, then should it perhaps be automatically imported? Just curious.


```
# finance/all.py
...
from easter import easter
```



---

Comment by psinis created at 2009-03-17 08:21:38

thank you Chris for checking! 
I think we can safely leave Julian in there -- it doesn't bloat the code, nor does it make the method signature unwieldy.

What's the next step...?


---

Comment by cswiercz created at 2009-03-17 12:16:25

Replying to [comment:6 psinis]:
> What's the next step...?

Er...whatever you like, I suppose!


---

Comment by AlexGhitza created at 2009-03-17 21:12:38

Replying to [comment:6 psinis]:
> What's the next step...?

If you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).


---

Comment by cswiercz created at 2009-03-17 21:16:29

Replying to [comment:8 AlexGhitza]:
> Replying to [comment:6 psinis]:
> > What's the next step...?
> 
> If you mean the next step in this patch getting into Sage: now that it has a positive review, Michael Abshoff will eventually make sure that it merges properly and doesn't cause trouble in unforeseen places, and then it will be in the next release of Sage (either 3.4.1 or 3.4.2).

Ah, yes. I misunderstood! Once someone has given your ticket a positive review then the rest is out of your hands. You're done and can go on to do more exciting things!


---

Comment by mabshoff created at 2009-03-23 22:43:04


```
# finance/all.py
...
from easter import easter
```


I don't think easter should be in the global namespace, but in finance.easter.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 09:41:24

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 09:41:24

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
