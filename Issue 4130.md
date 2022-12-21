# Issue 4130: #4125 does not work on OS X 10.4

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-15 20:11:56

Assignee: mabshoff

It looks like OS X 10.4.11's version of `which` doesn't behave very well...


```
hamptonio: nomad66-214:~ mh$ echo $PORTS_PATH
[1:03pm] hamptonio: no port in /Volumes/D/sage-3.0.2 /Library/Frameworks/Python.framework/Versions/Current/bin /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/teTeX/bin/i386-apple-darwin-current
[1:03pm] hamptonio: nomad66-214:~ mh$ echo $FINK_PATH
[1:03pm] hamptonio: no fink in /Volumes/D/sage-3.0.2 /Library/Frameworks/Python.framework/Versions/Current/bin /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/teTeX/bin/i386-apple-darwin-current
[1:03pm] hamptonio: nomad66-214:~ mh$ if [ "$PORTS_PATH" -o "$FINK_PATH" ]; then echo "*"; fi
[1:03pm] hamptonio: *
```



---

Attachment


---

Comment by mabshoff created at 2008-09-16 03:32:46

The attached patch has been tested on OSX 10.4 and 10.5, with and without Fink and/or MacPorts. The patch also contains a fix to sage-env that was not yet in the spkg/base repo (since -sdist copies sage-env over without committing it to the repo).

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-16 03:32:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-16 03:47:09

Merged in Sage 3.1.2.rc5


---

Comment by mabshoff created at 2008-09-16 03:47:09

Resolution: fixed


---

Comment by dphilp created at 2008-09-17 05:09:57

hmmm... this is still not foolproof.  If you type 'make', the first time, it dies with the proper message.  But despite not                 setting any environment vairable, the second time you run 'make', there is no error, no warning, nothing.


I assume that the prereq script doesn't get called every time make is run?  Maybe the fink/ports detection should go at the start.


---

Comment by mabshoff created at 2008-09-17 11:27:08

Replying to [comment:4 dphilp]:
> hmmm... this is still not foolproof.  If you type 'make', the first time, it dies with the proper message.  But despite not                 setting any environment vairable, the second time you run 'make', there is no error, no warning, nothing.
> 
> 
> I assume that the prereq script doesn't get called every time make is run?  Maybe the fink/ports detection should go at the start.

That issue is pretty much covered by #3140. This ticket was about fixing the OSX 10.4 issues, so closing it is valid. But thanks for being persistent :)

Cheers,

Michael
