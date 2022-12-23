# Issue 6090: plot(x^2, (x, -2, 2), fill=2) does not match documentation

Issue created by migration from https://trac.sagemath.org/ticket/6090

Original creator: jason

Original creation time: 2009-05-20 05:27:43

Assignee: was

According to the docs, if fill is a number c, then: "a number c: Fill the area between the function and the horizontal line y = c."

However, the above plot just fills to the x-axis.  My guess is that it is because bool(2)==True, so plot thinks we have fill=True?







---

Comment by whuss created at 2009-05-20 08:26:10

This is a duplicate of #5438.


---

Comment by mabshoff created at 2009-05-20 11:06:25

Replying to [comment:1 whuss]:
> This is a duplicate of #5438.

Hmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 11:07:22

Jason, 

I am marking this a potential dupe in the summary so we won't forget to close it assuming you can confirm it as one.

Cheers,

Michael


---

Comment by whuss created at 2009-05-20 11:21:55

Replying to [comment:2 mabshoff]:
> Replying to [comment:1 whuss]:
> > This is a duplicate of #5438.
> 
> Hmm, given that this went into 3.4.2 I wonder why Jason did hit this problem?

#5438 says it went into 4.0.alpha0 not 3.4.2.

Cheers,

Wilfried


---

Comment by mabshoff created at 2009-05-20 11:27:11

Resolution: duplicate


---

Comment by mabshoff created at 2009-05-20 11:27:11

Replying to [comment:4 whuss]:

> #5438 says it went into 4.0.alpha0 not 3.4.2.

Oops, I must have looked at some permutation of "5438" then. Sorry for the screwup.
 
> Cheers,

> Wilfried

Closed as dupe. Jason: If you disagree let us know.

Cheers,

Michael


---

Comment by jason created at 2009-05-20 12:01:47

Okay, I just tested it in 4.0, and it works great.  Sorry; it seems that I should have caught the other ticket in a search.  I'm not sure why I didn't.  Thanks for the prompt response!
