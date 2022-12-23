# Issue 1657: make a build-from-source version of jmol spkg

Issue created by migration from https://trac.sagemath.org/ticket/1657

Original creator: was

Original creation time: 2008-01-02 19:08:00

Assignee: mabshoff

This is very important.


```
On Jan 2, 2008 11:23 AM, Robert Bradshaw <robertwb@math.washington.edu> wrote:
> In principle, all one would need is javac (and the java runtime
> binaries). If they're going to be using java at all, they'll have that.
>
> It looks like they use the ant build tool which is a nice make system
> for java. http://ant.apache.org/ For those interested in building the
> java components from source, we could make an .spkg for this too (if
> they don't have it already). I used ant for the java3d stuff too.
```



---

Comment by tkosan created at 2008-01-02 21:46:56

Changing assignee from mabshoff to tkosan.


---

Comment by tkosan created at 2008-01-02 23:10:29

Changing assignee from tkosan to mabshoff.


---

Comment by tkosan created at 2008-01-02 23:10:29

I have jmol building/installing from source, but in the interest of
saving time I am not going to go through the last step of making an
actual spkg out of it because I have not done this before and it will
probably take me some time to get it right.

Here is a .zip file that contains the files needed to create a spkg:

http://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2.spkg-src.zip


---

Comment by robertwb created at 2008-01-03 10:08:36

Fortunately, we don't need signing because we're using the unsigned version of the applets. 

Also, there are several dependancies that are simply provided as jars. These need to be built from source as well prior to building jmol. See COPYRIGHT.txt


---

Comment by tkosan created at 2008-01-11 18:53:25

jmol-11.5.2-src.spkg is ready for testing:

http://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2-src-v2.spkg

The following packages needed to be included in the source version in order to remove any dependencies on binaries:

bcmail
bcprov
commons-cli   
commons-logging 
commons-lang  
jmol-acme  
servletapi
itext            
netscape   
vecmath-objectclub


---

Comment by robertwb created at 2008-01-11 20:54:02

I looked at it an tried it out and it works great for me (after deleting the "-v2" from the filename). 

Someone on a system with a minimal java install (Java + ant) should try it out too. 

- Robert


---

Comment by robertwb created at 2008-01-12 02:01:33

Builds fine on sage.math after installing the Java SE 6 JDK (the standard one, for 64-bit Linux) and `ant`. Upgrading my copy of Sage to try it out...


---

Comment by robertwb created at 2008-01-13 06:39:45

Works great on sage.math as well. Looks ready to include (as an optional spkg).


---

Comment by mabshoff created at 2008-01-15 02:58:09

I put the spkg in the optional spkg repo and mirrored it out.


---

Comment by mabshoff created at 2008-01-15 02:58:09

Resolution: fixed
