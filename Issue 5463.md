# Issue 5463: [with patch, needs review] new section for tutorial about functions vs. expressions, etc.

Issue created by migration from https://trac.sagemath.org/ticket/5463

Original creator: jhpalmieri

Original creation time: 2009-03-09 23:27:00

Assignee: jhpalmieri

There are lots of questions sage-support in which people trying to do basic calculus or plotting have gotten confused about how to specify a "function" to be plotted, differentiated, etc. The attached patch adds a section to the tutorial with some remarks about this issue.

See [http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html](http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html) for a typeset version (although you can just type 'sage -docbuild tutorial html' to get your own version).



---

Comment by was created at 2009-03-10 07:06:29

Looks good to me.  Well I sort of don't like the **'s instead of ^'s, but that's just a very minor style issue. All of the actual text looks good, and I like the description. 

The ReST here looks funny: http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html

I.e., in each of the code blocks there is some text afterwards explaining the example, and it is typeset as code instead of text.  I don't know why.   Again, just a minor ReST issue.  Mhansen?


---

Comment by mabshoff created at 2009-03-10 16:33:50

Yep, the ReST output does look funny, i.e. it seems that there is a lot of text that shouldn't be verbatim is rendered verbatim.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-03-10 18:07:17

Sorry about the ReST output.  I was trying to balance two things, and failed.  Given my limited knowledge of ReST, I can either make all of the sage output accessible to doctesting, or I can have the text indented the way I want for an enumerated list, but not both.  In the new version of the patch (along with updated html on the cited web page), I've gone for the first option: doctesting sees and tests all of the examples.

(I also changed "**" to carets, since I don't care much one way or the other, and was expressed a preference.)


---

Attachment

Merged in Sage 3.4.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 20:58:25

Resolution: fixed
