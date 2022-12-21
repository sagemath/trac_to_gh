# Issue 4523: browser cache not cleared when restarting the worksheet

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-14 16:28:31

Assignee: boothby

From an email on sage-devel:

The problem is not in your code.  I think the problem is in your browser caching the image.  When Sage creates the image, it gives it the same name.  Your browser thinks that it is the same image as before, so it doesn't bother to update the image.  If you refresh the page after you first see the wrong image, you'll see the right image appear.

You'll see the same problem if you have two cells:

`f(x) = x^2`

and 

`plot(f, (x, 1, 2))`


1. Evaluate the two cells, so you get a plot
2. Restart the worksheet
3. Change the function
4. Evaluate the two cells again.  Notice you get the same plot.
5. Hit Refresh in the browser.  Now the plot updates.



---

Comment by mhansen created at 2009-01-19 08:26:02

This is fixed by adding a Last-Modified header to the response.


---

Attachment

For anyone who doesn't want to read the patch, the new code adds the time (in seconds since the epoch) to the URL for each image, so the browser fetches image.png?1232408438 (or whatever the time is), and since that URL will change if one evaluates the cell at least one second later, the browser should pick up the new image.

I tested this with Firefox (Ubuntu, XP), IE7, IE8 beta, and Opera (Ubuntu and XP) and can no longer reproduce the bug. Positive review.

(BTW, at 23:31:30 UTC on February 13, 2009, the Unix time will be 1234567890.)


---

Comment by mabshoff created at 2009-01-23 02:34:25

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 02:34:25

Merged in Sage 3.3.alpha1
