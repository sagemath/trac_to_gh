# Issue 4813: [with patch, needs review] contribution to the tests/ directory

Issue created by migration from https://trac.sagemath.org/ticket/4813

Original creator: ddrake

Original creation time: 2008-12-16 13:48:57

Assignee: mabshoff

From http://groups.google.com/group/sage-support/msg/3ea7ed2eeab0824a :

> Note that you could also submit a patch to Sage with the code you're doctesting.
> I did that with all the tests from both of the books I published, and
> I encourage you and many others to do the same with the code from your
> article.  The code would go in a file
>
>    devel/sage/sage/tests/
>
> like the file devel/sage/sage/tests/book_stein_modform.py
>
> In fact, I could imagine having dozens of files in that directory, and
> when doctests break there, we could notify the authors before
> releasing the version of Sage that breaks their doctests for feedback
> -- then they could update their papers or Sage.

Here's the code from a preprint I just posted. I tried to follow "official" style in writing the code -- comments about the style and so on are welcome.


---

Attachment


---

Comment by mabshoff created at 2008-12-16 13:59:20

Is this code too specialized to go into the Sage library?

Cheers,

Michael


---

Comment by ddrake created at 2008-12-18 03:31:26

Replying to [comment:1 mabshoff]:
> Is this code too specialized to go into the Sage library?

Some of it definitely is; there's a function that computes columns of the tables in the paper. OTOH, I've been meaning to add support for complete matchings to Sage, and this code includes a function to generate complete matchings.

Either way, I would like this code to get put into the tests/ directory; William above mentioned "when doctests break there, we could notify the authors before releasing the version of Sage that breaks their doctests for feedback -- then they could update their papers or Sage." The paper is on the arXiv and will remain there forever (for some value of "forever"...) and I'd like to have this mechanism in place to make sure the code accompanying the paper always works.


---

Attachment

I think this is good to go in.  I've added a patch which does some minor formatting issues.  

Dan: Could you just give my little patch a positive review?


---

Comment by ddrake created at 2009-01-25 13:22:49

Replying to [comment:3 mhansen]:
> Dan: Could you just give my little patch a positive review?

Certainly. Thanks for recommending this go in!


---

Comment by mabshoff created at 2009-01-28 16:01:23

Dan,

please chose a much more descriptive summary for a patch like this next time.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 16:14:54

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 16:14:54

Merged in Sage 3.3.alpha3.

Cheers,

Michael
