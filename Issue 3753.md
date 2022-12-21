# Issue 3753: notebook -- change the default for nb.save('...')

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-01 01:34:06

Assignee: boothby

CC:  was mhansen


```


Hi,

I also noticed there is a problem with "nb.save()". It assumes that
the current directory is ".sage". So it saves the notebook object in a
wrong place if you are not in ".sage". I think this is a bug.


Kwankyu

	
```



---

Comment by TimothyClemans created at 2008-08-03 17:56:08

I can't seem to confirm that this is the case. I added the method filename to the Notebook class and here's what I get:


```
nb = load('test/nb.sobj')
sage: nb.filename()
'test/nb.sobj'
```


Looking at the source code for Notebook.save() it appears to me that save() relies on self.__filename.


---

Comment by AlexGhitza created at 2009-01-23 02:50:48

Changing type from defect to enhancement.


---

Comment by timdumol created at 2009-11-19 20:14:57

This does not seem to be a problem anymore, especially noting the change to the Datastore backend. Can someone check this and close it if it is so?


---

Comment by was created at 2009-11-19 23:30:27

I agree timdumol -- there's no reason to save nb anymore so who cares what it does.


---

Comment by was created at 2009-11-19 23:30:27

Resolution: wontfix
