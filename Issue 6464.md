# Issue 6464: notebook: Unicode in notebook worksheets

Issue created by migration from https://trac.sagemath.org/ticket/6464

Original creator: mvngu

Original creation time: 2009-07-05 02:06:05

Assignee: boothby

Keywords: Unicode, notebook

At this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e3b8dce14b6375bf) thread, there is a patch to fix a Unicode problem related to typesetting Korean in notebook worksheets. Here's an essential snippet:

```
So I find the python code and modify it.

sageroot/devel/sage/sage/server/notebook/cell.py:211

211 : </script>"""%(self.__id,self.__id,self.__text)

=>

211 : </script>"""%(self.__id,self.__id,((self.__text).decode
('utf-8')).encode('ascii', 'xmlcharrefreplace'))
```

This might be related to #6417.


---

Comment by mora created at 2009-07-25 01:22:45

The ticket 6562 is nearly the same. I wrote that, because I didn't know about this ticket. I suggest that we should use this solution.


---

Comment by mora created at 2009-08-05 22:55:56

I suggest that we should apply this patch.


---

Comment by mvngu created at 2009-08-07 00:07:10

Replying to [comment:3 mora]:
> I suggest that we should apply this patch.
I don't see any patch file attached to this ticket.


---

Comment by mora created at 2009-08-07 12:15:08

Replying to [comment:4 mvngu]:
> Replying to [comment:3 mora]:
> > I suggest that we should apply this patch.
> I don't see any patch file attached to this ticket.
In the description mvngu suggested a little modofication of the file cell.py. I will make a patch as soon as I arrive home.


---

Comment by mora created at 2009-08-08 12:47:09

Unicode in notebook worksheets, the modification was made by mvngu.


---

Attachment


---

Comment by mvngu created at 2009-08-11 22:20:27

apply only this patch


---

Attachment

The patch `trac_6464-unicode.patch` gives proper credit to NoSyu, the person who proposed the fix. Only this patch should be applied.


---

Comment by mvngu created at 2009-08-11 22:40:46

Either of the patches `12659.patch` or `trac_6464-unicode.patch` results in a doctest failure:

```
sage -t -long devel/sage-main/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/server/simpl\
e/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s'\
 % (port, session, urllib.quote(code)))
Expected:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
Got:
    {
    "status": "done",
    "files": ["a.txt"],
    "cell_id": 3
    }
    ___S_A_G_E___
    <BLANKLINE>
    ^Ae2
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp\
/.doctest_twist.py
         [9.5 s]
```



---

Comment by mora created at 2009-08-12 11:18:38

I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:

```
sage -t -long "devel/sage/sage/server/simple/twist.py"      
         [8.9 s]
 
----------------------------------------------------------------------
All tests passed!
```

I don't know how to help, it works for me.


"The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix." Then it's my mistake, I'm sorry.


---

Comment by mvngu created at 2009-08-12 11:24:14

Replying to [comment:10 mora]:
> I used the patches on Sage 4.1 and Sage 4.1.1.rc2, but I didn't get any doctest failure. I got:

```
sage -t -long "devel/sage/sage/server/simple/twist.py"      
         [8.9 s]
 
----------------------------------------------------------------------
All tests passed!
```

> I don't know how to help, it works for me.
Hmmm... that's rather strange. I may have done something wrong.



> "The patch trac_6464-unicode.patch gives proper credit to NoSyu, the person who proposed the fix." Then it's my mistake, I'm sorry.
No worries :-)


---

Comment by kcrisman created at 2009-08-25 20:22:28

Tried this in FF3.5 and Safari 4 on Mac OSX.5 Intel.  Tried, saved, quit, resaved, went from browser to browser several times, and nothing made it break.  Character sets I used include 한글, Cyrillic, üöä, some Chinese characters, Arabic, ... I didn't try all the ones available on my system, but it seems like this solution will work fine.  It's really sort of embarrassing this isn't in yet, to be honest.  

Test for the above file passes when added to 4.1.1, so positive review - maybe mvgnu didn't use a clean tree? Don't forget to close #6562 as well.


---

Comment by mvngu created at 2009-08-26 21:15:40

Merged `trac_6464-unicode.patch`.


---

Comment by mvngu created at 2009-08-26 21:15:40

Resolution: fixed
