# Issue 1379: "What is Sage" interactive javascript webpage app

Issue created by migration from https://trac.sagemath.org/ticket/1379

Original creator: TimothyClemans

Original creation time: 2007-12-03 07:10:23

Assignee: was

App is live at http://sagemath.timothyclemans.com/whatis/

The app is a pretty interactive box where users click the three definitions of Sage and see the definitions one at a time.

To implement on sagemath.org homepage download http://sagemath.timothyclemans.com/whatis/whatis.zip and place in root of sagemath.org 

Index.html is replaced, javascript, css file, images folder added.




---

Comment by frankie.robertson created at 2008-01-04 21:01:40

I'm -1 on this
Problems:
 * Hover images are only fetched when button is hovered over. Use a single image and use css to have it as a background-image to a div and change it's offset on hover. 
 * Doesn't currently degrade gracefully.
 * Is more confusing than the current site, which isn't aesthetically perfect but is pretty functional and does a good job of giving an overview of sage.

That said, the prose is pretty good and I can see the benefit of explaining sage in these terms.


---

Comment by malb created at 2008-01-06 13:15:14

-1, I don't see the benefit. This makes reading the website much harder (because it adds the need to click on stuff first) and doesn't add any benefit (at least for me).


---

Comment by mabshoff created at 2008-02-10 01:06:47

Ok, unless somebody speaks up for this I will close this before 2.10.2 is released.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:10:49

Resolution: invalid


---

Comment by mabshoff created at 2008-02-15 23:10:49

Nobody cared -> invalid.
