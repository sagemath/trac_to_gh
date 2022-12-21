# Issue 6562: [with patch, needs review] Unicode support in TextCells

Issue created by migration from Trac.

Original creator: mora

Original creation time: 2009-07-19 18:54:53

Assignee: boothby

Keywords: textcell unicode

In a TextCell (shift+click on the blue line) I write some letters:

 http://www.math.bme.hu/~morap/sage_textcell1.png

after I save it. It looks fine:

 http://www.math.bme.hu/~morap/sage_textcell2.png

but when I double click on it to edit, then I get:

 http://www.math.bme.hu/~morap/sage_textcell3.png

That's the problem. I could not find out what (Python or TinyMCE) converts the special characters to html entities (for example é to &eacute;), but it does not convert all of them.

The patch solves the problem. Without it the html code looks like:

 http://www.math.bme.hu/~morap/sage_textcell4.png

using the patch everything's fine. The html code after applying the patch:

 http://www.math.bme.hu/~morap/sage_textcell5.png


---

Attachment


---

Comment by mora created at 2009-07-25 01:20:35

The Ticket 6464 is nearly the same. I suggest the solution of 6464 to use.


---

Comment by kcrisman created at 2009-08-26 13:10:09

To release manager: this should be closed as a duplicate of #6464, as mentioned above.


---

Comment by mvngu created at 2009-08-26 20:02:49

Closing this as a duplicate of #6464.


---

Comment by mvngu created at 2009-08-26 20:02:49

Resolution: duplicate
