# Issue 4704: Use jquery to make the javascript code nicer

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-05 01:11:07

Assignee: boothby

CC:  boothby tclemans robertwb

This ticket splits off part of #4267.




---

Attachment

This depends on the patch at #4700.


---

Comment by jason created at 2008-12-05 01:12:10

Changing assignee from boothby to jason.


---

Comment by jason created at 2008-12-05 01:12:10

Changing status from new to assigned.


---

Comment by jason created at 2008-12-05 10:20:53

Ignore the dependency on #4700.  Instead, this depends on #3767.


---

Comment by was created at 2008-12-06 23:36:02

This definitely needs to be commented on by Tom Boothby, since this patch simply deletes the entire optimized-for-us javascript AJAX "framework" he wrote, and replaces it by jQuery's.  Is jQuery's actually better?


---

Comment by jason created at 2008-12-06 23:50:00

Yep, I agree.  CCing boothby.


---

Comment by boothby created at 2008-12-07 06:14:11

I'm not sure I see the point of this.  I'm inclined to say, "If it ain't broke, don't fix it."  One might accuse me of being biased... but I really don't think I am here -- I'd be happy to see my code go if it made the rest of the notebook code significantly better.

There's one benefit that I see: 

```
'newcell=0' + '&id=' + id + '&input='+escape0('%__sage_interact__\n' + input))
```


becomes


```
{newcell: 0, id: id, input: '%__sage_interact__\n' + input}
```


and this is more readable (I'm hoping that the escape0 functionality is preserved).  I'd like to see what was, bradshaw, and tclemans say about this.  I'll test after finals are over.


---

Comment by jason created at 2008-12-09 09:49:46

I like the cleaner syntax.  The other thing that may be nice about jquery is that it offloads maintaining to a third party that presumably has more time to focus on it.  That may be a non-issue for our code right now, though.


---

Comment by robertwb created at 2008-12-10 02:23:18

If there isn't any behavior or performance degradation, I think cleaner syntax is worth having, especially if it makes it easier for more people to work on the notebook code. Also, assuming that jquery can do all we need it to, the more we can offload javascript ajax and browser compatibility code to a larger community the more time we can focus on writing interesting stuff.


---

Comment by jason created at 2008-12-20 21:36:11

boothby: could you test this patch now that finals are over?


---

Comment by jason created at 2008-12-20 21:40:27

boothby: I should mention that everything is automatically escaped, so the escape0 functionality is preserved, but is way more transparent to the user.


---

Comment by TimothyClemans created at 2008-12-20 21:41:56

Changing type from defect to enhancement.


---

Comment by TimothyClemans created at 2008-12-20 21:41:56

Jason asked me to comment. I don't know Javascript, but I like the idea of outsourcing to an actively developed library.


---

Comment by mabshoff created at 2009-01-19 06:32:48

Positive review due to #4705. Jason commented that Tom gave his thumbs up to this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 08:09:40

Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 08:09:56

Merged jquery-javascript-cleanup.patch in Sage 3.3.alpha0. Oops :)


---

Comment by mabshoff created at 2009-01-19 08:09:56

Resolution: fixed


---

Comment by jason created at 2009-01-19 13:53:48

When did I comment that Tom gave his thumbs up?  I don't remember that.


---

Comment by mabshoff created at 2009-01-19 14:01:57

Replying to [comment:17 jason]:
> When did I comment that Tom gave his thumbs up?  I don't remember that.

It come up in IRC, but I am no longer 100% sure it was you who told me or of it was Tom directly. Either way, the code is in and while it might have slipped in somewhat below standards SD 12 will see some pounding of the new code, so things should turn out ok :)

Cheers,

Michael
