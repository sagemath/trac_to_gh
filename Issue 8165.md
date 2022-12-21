# Issue 8165: title cuts off on worksheet upload

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-02-03 05:39:24

Assignee: was

I just tried uploading the following worksheet:

http://sagenb.org/home/pub/1139/

by pasting the URL into the middle box of the upload page on a (fairly fresh) 4.3.1 install.  When I opened up the worksheet on the local server, the title was cut off to be about 14 characters long.  This is a bug.



---

Attachment

Don't use `rstrip` to chop `'.sws'`.  sagenb repo.


---

Comment by mpatel created at 2010-02-03 06:20:44

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-03 06:20:44

The problem is the use of [str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `twist.Worksheet_download`:

```python
sage: '112 - 01 - Review.sws'.rstrip('.sws')
'112 - 01 - Revie'
```

The patch uses `str.endswith` and a slice, instead.


---

Comment by mpatel created at 2010-02-03 06:23:07

Related: #7663, #7924.

To review this, if you have the time, I suggest using the latest spkg at #8051.


---

Comment by rbeezer created at 2010-02-07 06:49:48

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-02-07 06:49:48

I've reproduced the problem on 4.3.1, then applied the patch on top of sagenb-0.7.4.spkg and the title survives properly when saved to an sws file and subsequently loaded into a notebook.

Positive review.


---

Comment by mpatel created at 2010-02-10 18:32:38

Resolution: fixed
