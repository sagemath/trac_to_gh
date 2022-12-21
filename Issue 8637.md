# Issue 8637: typo in sagenb/data/sage/html/worksheet_listing.html, line 117

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-03-31 23:34:09

Assignee: jason, was

From IRC on March 31 2010:

```
15:24 < uc-paul> OK to report a bug in sagenb in this room?
15:28 < uc-paul> My public facing Sage notebook server has a log file full of 
                 entries like the following:
15:28 < uc-paul> *.*.*.* - - [01/Apr/2010:11:04:58 +1300] "GET 
/pub/?typ=activereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverserevers
15:28 < uc-paul> eversereversereversereversereversereversereversereversereverser
eversereversereversereversereversereversereversereversereversereversereversereversereversereversereversereverse&sort=owner&reverse=True HTTP/1.0" 200 31347
15:28 < uc-paul> This is due to a typo in 
                 sagenb/data/sage/html/worksheet_listing.html, line 117
15:31 < uc-paul> Patch at  http://www.math.canterbury.ac.nz/~p.brouwers/sage/worksheet.patch
```


The patch, in case it gets taken down, is:

```
--- a/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:39:58.000000000 +1300
+++ b/sagenb/data/sage/html/worksheet_listing.html      2010-04-01 10:47:49.000000000 +1300
`@``@` -114,7 +114,7 `@``@`
             </td>

             <td>
-                <a class="listcontrol" href=".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else 'reverse&=True' }}">
+                <a class="listcontrol" href=".?typ={{ typ }}{{ '' if sort != 'last_edited' or reverse else '&reverse=True' }}">
                     Last Edited
                 </a>
             </td>
```



---

Attachment

I made Paul's patch into a proper Mercurial patch and credited him for it. Please review!


---

Comment by ddrake created at 2010-03-31 23:47:22

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-04-01 19:38:59

Nice catch by Paul. Positive review.


---

Comment by timdumol created at 2010-04-01 19:38:59

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-05-04 04:44:41

Resolution: fixed
