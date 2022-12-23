# Issue 1496: notebook -- make it easy to link different worksheets

Issue created by migration from https://trac.sagemath.org/ticket/1496

Original creator: was

Original creation time: 2007-12-13 23:20:45

Assignee: boothby

CC:  embray


```


On Dec 13, 2007 12:31 PM, greg2k4 <greg2k4@mail.ru> wrote:
> 
> Hi,
> 
> I'd like to create an interactive book like SAGE tutorial from my
> notebook worksheets.
> But how can I link them together?
> 
> In tutorial, links look like "http://192.168.1.1/doc/live/tut/
> nodeNN.html" .
> But actual worksheets have .sws extension.
> 
> BTW, was this tutorial built using some tool? I've heard of JavaDoc
> and others, but never used them...

It was built using latex2html plus an html --> worksheet parser
that Dorian Raymer wrote. 

I did start writing something to turn *tex* documents into sage notebooks, but
it's really not ready for prime time, and that's not what you want anyways. 

You can link worksheets together though, e.g., this will make a link to worksheet 15:

<a href="/home/admin/15">worksheet 15</a>

This is obviously sucky, since the worksheet numbers change if you download/upload
the worksheets.  Doing something better, i.e., somehow linking by the title of the worksheet,
etc., is not yet implemented.  

 -- William
```



---

Comment by chapoton created at 2018-08-11 19:40:35

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-08-11 19:40:35

obsolete, should be closed now


---

Comment by embray created at 2018-08-14 17:18:42

Resolution: wontfix
