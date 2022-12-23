# Issue 6342: notebook -- fix that the slideshow mode in the notebook utterly completely broken

Issue created by migration from https://trac.sagemath.org/ticket/6342

Original creator: was

Original creation time: 2009-06-16 22:15:54

Assignee: boothby

This patch turns slideshow mode into something actually pretty useful.  It is maybe uglier than it was 2 years ago.  It is maybe "lame"-ish, perhaps.  But it is usable!  Which is a million times better than the literally buggy situation now.  

The actual patch attached here tracks both the cell_list (the compute cells), and adds a new list allcell_list, which contains all the cells (not just the compute cells).


---

Attachment

Under Ubuntu j & firefox, I can repeatably hit an infinite memory consumption:

 1. Switch into slideshow mode
 1. Shift-click to create an html cell above the first cell
 1. Enter the text, `This is some $foo$`
 1. Shift-enter to save the html cell
 1. Shift-click to edit the html cell just created
 1. Quickly kill firefox before it takes down your system.


---

Comment by boothby created at 2009-06-16 22:44:22

notes on the above comment:

Step 1 may be omitted, this bug is active in normal mode.  Step 5 should read, "double-click".


---

Attachment

a tiny little bugfix


---

Attachment


---

Comment by was created at 2009-06-17 19:36:19

make it so slides delimited by text cells with <hr>'s; lighten up control css


---

Attachment

Problems:

 1. Shift-enter is broken in html cells
 1. Up & down buttons are completely broken (as are the pgup/pgdn keys):
   a. Without any <hr> tags, nothing happens at all
   a. With one <hr> tag, one can view either the first cell or just the text cell with the <hr> all by itself.
 
Comments:

 1. I liked the previous version which showed cells after the current one.
 1. It would be nice if you didn't have to have your mouse in a cell for the pgdn/pgup keys to work. (this would take some effort, as we have no global key handling right now -- so this should be handled in another ticket)


---

Comment by boothby created at 2009-06-17 21:08:54

I just read the new entry in the tutorial.  According to the specified behavior (which I don't like), the up&down buttons are almost working -- however,

 1. Deleting a cell in a 'frame' jumps back to the previous frame, even if it wasn't the first cell in the frame.
 1. The first frame shows up fine, but the second and subsequent frames don't show any code cells -- it's just the HTML cells, and there's no way to view the code cells.  Interestingly, if you add a few cells to the frame, they don't show up -- but after 10 or 20, they start appearing.  However, if you switch out of and back into the frame, it's back to not showing any code cells.
 1. The counter / progress meter shows the number of cells, not the number of frames.  This is counterintuitive.

Reasons I don't like the specified behavior:

 1. The resulting code is more complex.
 1. Using <hr>'s, while documented, is not intuitive.  I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap.

By contrast, the version before part-2.patch was clean, simple and intuitive.


---

Comment by was created at 2009-06-17 22:50:11

> The first frame shows up fine, but the second and subsequent frames don't show any code cells 

This is an unintended bug which I'm fixing. 

> Reasons I don't like the specified behavior:
>   1. The resulting code is more complex.
>   2. Using <hr>'s, while documented, is not intuitive. I'd never have thought of that, and I'd probably assume that the slideshow mode was just broken crap. 
> By contrast, the version before part-2.patch was clean, simple and intuitive. 

I'm trying to give an *actual* talk, and in preparing it, I learned that the version before part-2.patch was actually totally broken crap for actual use.  In contrast, what I've just written is really awesome for actual use.   There is a huge difference between imagining maybe giving a talk and actually writing a talk you're going to give in front of a 130 people.  It is absolutely essential to have slides that are given by a marker.  <hr> is a very reasonable choice for a marker.

> 3. The counter / progress meter shows the number of cells, not the number of frames. This is counterintuitive. 

It's going to be a lot more work to implement the counter to show the frames, and I decided not to implement that in the interest of iterative development.


---

Attachment

Slideshow mode now works, shift-enter on HTML cells is still broken.


---

Comment by boothby created at 2009-06-17 23:47:40

Oops, the "bottom" button now jumps to the last cell instead of the last frame.


---

Comment by rlm created at 2009-06-23 09:07:47

It would be nice if there were some way to

 1. indicate which hr's delimit slide breaks, and which don't, i.e. if you want to use an hr in the middle of a slide, and

 2. allow for slides which don't contain any cells.

Regarding 1, we could even use something like <sage_slide_break> instead


---

Comment by rlm created at 2009-06-23 10:34:16

I think also if there is a newline at the end of an html block, it cuts the slide after the next cell.


---

Comment by rlm created at 2009-06-23 10:56:31

Adding a cell to the end of a slide is also problematic.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid
