# Issue 9196: Update ATLAS to the latest upstream souce

Issue created by migration from https://trac.sagemath.org/ticket/9196

Original creator: drkirkby

Original creation time: 2010-06-09 14:02:49

Assignee: AlexGhitza

As discussed here

http://groups.google.co.uk/group/sage-devel/browse_thread/thread/f3fa4f8737437d7f/5528028cc0c16975?lnk=gst&q=atlas#5528028cc0c16975

ATLAS needs to be updated. I'll take on that task. 




---

Comment by AlexGhitza created at 2010-09-02 11:01:27

Changing assignee from AlexGhitza to tbd.


---

Comment by AlexGhitza created at 2010-09-02 11:01:27

Changing component from algebra to packages.


---

Comment by drkirkby created at 2010-09-02 11:08:47

Sorry Alex for this. 

It is annoying that the default is "algebra". It would be better if there was no default, and someone had to chose something. 

Dave


---

Comment by AlexGhitza created at 2010-09-02 11:20:22

Not a problem, I was just doing some cleaning.  The simplest solution might be to add a new component called "aaa-misc" that would catch the tickets where the component has not been set.  Then once in a while we can sift through that and classify tickets, without "algebra" getting polluted.


---

Comment by drkirkby created at 2010-09-02 11:49:26

Replying to [comment:3 AlexGhitza]:
> Not a problem, I was just doing some cleaning.  The simplest solution might be to add a new component called "aaa-misc" that would catch the tickets where the component has not been set.  Then once in a while we can sift through that and classify tickets, without "algebra" getting polluted.

I imagine you must get this quite a lot, which is a bit of a waste of your time. To be honest, I might have left this at "algebra" deliberately, as ATLAS is an acronym for "Automatically Tuned Linear Algebra System". But I know I do occasionally leave things at "algebra" by mistake. 

As a non-mathematician, I often have difficulty in knowing what best to classify something under. 

It's arguable if this should go under "linear algebra" rather than "packages". I really don't know half the time. To me, "packages" seems a bit too wide. 

I think it would be useful if there were tick boxes, and one could tick a few. The other one to get ATLAS working on HP-UX (#9815) could reasonably be in "linear algebra", "packages" and "porting". 

Dave


---

Comment by jdemeyer created at 2013-05-24 12:19:26

Duplicate of #10508.


---

Comment by jdemeyer created at 2013-05-24 12:19:26

Resolution: duplicate
