# Issue 6251: LogoutResource in sage/server/simple/twist.py doesn't really log you out

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-06-09 01:20:04

Assignee: boothby

CC:  robertwb

Keywords: simple server logout

I'm using the simple server, and it seems like the logout command doesn't really log you out. From a regular Python (2.6) session:

```
>>> import urllib
>>> def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data 
... 
>>> print(get_url('http://localhost:8000/simple/login?username=admin&password=xxx'))
{
"session": "515f64ef06471627e1d4a903ee921899"
}
___S_A_G_E___

>>> sess = "515f64ef06471627e1d4a903ee921899"
>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=2*2'.format(sess)))
{
"status": "done",
"files": [],
"cell_id": 1
}
___S_A_G_E___

4

>>> print(get_url('http://localhost:8000/simple/logout?session={0}'.format(sess)))
{
"session": "515f64ef06471627e1d4a903ee921899"
}
___S_A_G_E___

```


But you can still issue compute commands and have them evaluated. In the same Python session:

```
>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=3*3'.format(sess)))
{
"status": "done",
"files": [],
"cell_id": 3
}
___S_A_G_E___

9

```

In the LogoutResource class of twist.py, I see that we quit the worksheet and remove all the cells, but it's retaining some state -- note above that after we logout, the next compute command uses  cell 3. You never explicitly remove "session" from the sessions dictionary; is that something that should be done?



---

Comment by ddrake created at 2009-06-09 01:24:33

I should add a bit about why I'm concerned about this: I'm working on some SageTeX stuff that uses the simple server, and I had run maybe 20 tests and the server now had 20 running worksheets and was consuming tons of memory. I want to make sure that when you issue a logout command, the worksheet and session really are disposed of, so that we don't unncessarily use memory and resources.


---

Comment by robertwb created at 2009-06-09 04:20:11

Yes, this should be fixed. It's a security issue as well. I'm surprised the session is still good!


---

Attachment


---

Comment by ddrake created at 2009-06-09 07:32:12

I've attached one attempt at some kind of solution. I noticed that the SessionObject never gets deleted, so I thought I would just remove it from the "sessions" dictionary. This does make the session unavailable from the simple server, but I thought it might not properly get rid of the worksheet...but it seems like it does. Perhaps when the SessionObject gets deleted from the sessions dictionary, the worksheet and so on all get garbage collected?

The GC theory seems a bit plausible, especially since I noticed the line `sessions['test'] = session` in the file, which seems like some leftover debugging cruft...I deleted that line and things seem to work better, since now there isn't a spurious second reference to the session object.

Here's a question: in the simple server, we create a worksheet, and to get rid of it, we simply delete its directory. Is that sufficient? My thinking is that it is, since we aren't creating the worksheet within the notebook, so there's no other record of the worksheet's existence; hence deleting the files removes all traces of the worksheet on disk. Is this correct?

I've tested this some, and it seems to solve my problems. Please check this over!


---

Comment by robertwb created at 2009-06-09 08:52:40

Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though.


---

Comment by ddrake created at 2009-06-09 09:30:27

Replying to [comment:4 robertwb]:
> Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though. 

I don't see the transient worksheets in the usual web notebook, and if load `nb.sobj` after running some sessions, I don't see any worksheets there (but I might have missed something). I've tested this on my own machine, sage.math, and bsd.math.

The "further-stuff" patch removes the nodoctest, since the file does pass doctests. It also adds the server to the reference manual and improves the documentation a bit. It doesn't have anything to do with fixing the issue in this ticket, but while we're there, we might as well fix some things up.


---

Comment by ddrake created at 2009-06-09 09:30:27

Changing assignee from boothby to ddrake.


---

Comment by ddrake created at 2009-06-09 09:30:27

Changing status from new to assigned.


---

Comment by ddrake created at 2009-06-15 07:17:06

robertwb, can you review this? If this patch is good, I'd like to see it get into Sage very soon, so I can more publicly release my remote-sagetex script.


---

Comment by jhpalmieri created at 2009-07-20 02:42:15

One quick comment: in "trac_6251-further-stuff.patch", you don't need to add the file "twist.rst": it is autogenerated (as it says) -- it is created automatically because of the line you added to "doc/en/reference/notebook.rst".


---

Comment by ddrake created at 2009-07-20 05:17:39

Replying to [comment:7 jhpalmieri]:
> One quick comment: in "trac_6251-further-stuff.patch", you don't need to add the file "twist.rst": it is autogenerated (as it says) -- it is created automatically because of the line you added to "doc/en/reference/notebook.rst".

Okay, thanks. I still don't really know what I'm doing with the documentation system. I'll get an updated version of this patch up.


---

Comment by was created at 2009-07-26 02:19:52

Positive review subject to removing twist.rst from the patch.


---

Attachment


---

Comment by mvngu created at 2009-07-29 12:11:56

Resolution: fixed


---

Comment by mvngu created at 2009-07-29 12:11:56

Merged both patches.
