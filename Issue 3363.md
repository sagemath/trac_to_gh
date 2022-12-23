# Issue 3363: Use Applescript to start Sage on OSX (step 4-6 from README)

Issue created by migration from https://trac.sagemath.org/ticket/3363

Original creator: mabshoff

Original creation time: 2008-06-04 16:23:07

Assignee: mabshoff


```
Hi
I just read the installation readme and built my own application to
start the sageserver:

Just start the Apple-ScriptEditor and enter the following code:

tell application "Terminal"
        do script "/Applications/sage/sage -notebook"
end tell

Well, that's all. Now only save the script as a program-bundle. After
that, you can assign the .app file a nice icon and put it in your
dock, click it, see firefox coming up and have fun.

I'd propose that this app could be part of the sage-install
bundle... ;-)

Hope, you like this tip

greeting,
Kai-Philipp 
```



---

Comment by iandrus created at 2009-11-27 21:02:01

I believe this issue is invalid now that we have a Sage.app.


---

Comment by kcrisman created at 2010-05-26 20:26:00

To release manager: Yes, this should be closed.  Although the app is still not default (sigh).


---

Comment by mvngu created at 2010-06-12 18:47:30

On OS X, we can create an app bundle from a newly compiled source tarball:


```
export SAGE_APP_BUNDLE=yes
./sage -bdist version
```


So close as invalid.


---

Comment by mvngu created at 2010-06-12 18:47:30

Resolution: invalid
