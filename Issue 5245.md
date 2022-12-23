# Issue 5245: treat truncated HTML intelligently

Issue created by migration from https://trac.sagemath.org/ticket/5245

Original creator: schilly

Original creation time: 2009-02-12 15:49:47

Assignee: boothby

from the [notebook "report problem" bugtracker](http://spreadsheets.google.com/ver?key=pCwvGVwSMxTzT6E2xNdo5fA&t=1234452850833000&pt=1234452830833000&diffWidget=true&s=AJVazbVHq6MFP1rt4M9kABykB37gF_Uy_g)

Too long HTML outputs are truncated in the notebook. A silly example:


```
html('<table>'+'<tr>'+
'\n'.join(('<td>'+'</td><td>'.join(
'<font color="#0000ff" style="background-color: #dddddd;">%s</font>'
% (row*column)
for column in range(1, 25))+'</td>')+'</tr>'
for row in range(1, 20))+'</table>')
```


This produces "WARNING: Output truncated! full_output.txt" and the displayed HTML is somewhat garbled (truncation doesn't work so well for HTML, obviously). Wrapping the expression around show() changes nothing.

Expected:

Program-generated HTML is a quite nice way to visualize some things quickly: The output may be long though (especially for quick & dirty scripts), even when the actually displayed content does not take much space on screen. Sage shouldn't be so quick to truncate HTML, and even if it does truncate sometimes (I'm not sure if it should), *the output should be a .html file, not .txt, so that the browser displays it correctly by default*.

---

Note by me: changing the ending isn't everything, also the mime-content type has to change. maybe it should not be a txt output in the first place and everything html as a default...


---

Comment by timdumol created at 2010-01-17 10:26:10

Changing type from defect to enhancement.


---

Comment by nthiery created at 2014-09-24 09:05:23

Just to add one datapoint: a student of mine got the following in the Sage 6.3 notebook:

```
    sage: solve?
    ... output truncated ...
```


and due to the above the full output was displayed as text and thus rather unreadable.

I was not able to reproduce this truncation happening, even in his own session a bit later.


---

Comment by boothby created at 2020-03-29 02:08:51

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:08:51

Resolution: invalid
