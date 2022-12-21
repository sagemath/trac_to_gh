# Issue 5897: add some javascript to make jsmath happier (very easy ticket to close, probably)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-26 02:05:09

Assignee: boothby

This was on sage-support on April 25.  

```
Thanks for posting the new example.  I have found that the problem is
due to the fact that Sage puts the output inside a <PRE> block, and
IE7 gets confused about some of its measurements in that case.  It can
be fixed by including

 span.typeset {
    white-space: normal;
 }

in the css/main.css file for sage.  I will add this to jsMath in the
next release.

Davide
```


We should add this to sage, since who knows when it'll go into jsmath and get into sage.


---

Comment by mpatel created at 2009-11-14 05:51:30

This is in the version of jsMath included with SageNB.  Should we close this ticket?


---

Comment by mhansen created at 2009-11-15 14:17:11

Resolution: invalid
