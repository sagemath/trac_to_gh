# Issue 4176: matplotlib build failure due to broken tcl/tk detection

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-23 18:12:53

Assignee: mabshoff

CC:  jsp


```
BUILDING MATPLOTLIB 
            matplotlib: 0.98.3 
                python: 2.5.2 (r252:60911, Sep 23 2008, 17:09:57) 
[GCC 
                        4.3.0 20080428 (Red Hat 4.3.0-8)] 
              platform: linux2 
REQUIRED DEPENDENCIES 
                 numpy: 1.1.0 
             freetype2: 9.16.3 
OPTIONAL BACKEND DEPENDENCIES 
                libpng: 1.2.29 
Traceback (most recent call last): 
  File "setup.py", line 125, in <module> 
    if check_for_tk() or (options['build_tkagg'] is True): 
  File "/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ 
setupext.py", line 846, in check_for_tk 
    explanation = add_tk_flags(module) 
  File "/home/abhishek/sage-3.1.2/spkg/build/matplotlib-0.98.3.p1/src/ 
setupext.py", line 1106, in add_tk_flags 
    module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) 
UnboundLocalError: local variable 'tk_ver' referenced before 
assignment 
Error building matplotlib package. 
```



---

Comment by mabshoff created at 2008-09-23 18:13:27

The issue came up in http://groups.google.com/group/sage-support/t/1ee74c5c3b1a391


---

Comment by mabshoff created at 2008-09-23 18:13:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-21 20:02:37

The issue has also been reported in http://groups.google.com/group/sage-support/t/a44e084a94b72724

Some more info: This also happens with

```
it's scientific linux 4.2, but have seen it on newer systems (will 
have alook again) 
Machine: Linux fwnc7122.wks.gorlaeus.net 2.6.9-67.0.15.ELsmp #1 SMP 
Wed May 7 04:33:01 CDT 2008 i686 i686 i386 GNU/Linux 
if you want I can send the install.log 
-eiso
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 20:20:21

And it is also broken on the freshly release Fedora Core 10:

```
BUILDING MATPLOTLIB 
             matplotlib: 0.98.3 
                 python: 2.5.2 (r252:60911, Nov 25 2008, 20:08:09)  [GCC 
                         4.3.2 20081105 (Red Hat 4.3.2-7)] 
               platform: linux2 
REQUIRED DEPENDENCIES 
                  numpy: 1.2.0 
              freetype2: 9.18.3 
OPTIONAL BACKEND DEPENDENCIES 
                 libpng: 1.2.33 
Traceback (most recent call last): 
   File "setup.py", line 125, in <module> 
     if check_for_tk() or (options['build_tkagg'] is True): 
   File "/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py", 
line 846, in check_for_tk 
     explanation = add_tk_flags(module) 
   File "/home/jaap/Download/sage-3.2.1.alpha0/spkg/build/matplotlib-0.98.3.p2/src/ setupext.py", 
line 1106, in add_tk_flags 
     module.libraries.extend(['tk' + tk_ver, 'tcl' + tk_ver]) 
UnboundLocalError: local variable 'tk_ver' referenced before assignment 
Error building matplotlib package. 
```

So let's make this a blocker.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 20:20:21

Changing priority from major to blocker.


---

Comment by was created at 2008-11-26 05:27:08

New spkg at http://sage.math.washington.edu/home/was/patches/matplotlib-0.98.3.p3.spkg

I don't have access to a system to test for the problem or if this fixes it.  I just read the relevant source code, and there is *clearly* a bug in upstream, which this new spkg fixes.


---

Comment by mabshoff created at 2008-11-26 06:17:17

That ain't no patch :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-26 09:04:42

Jaap,

since you are the man with the box that fails please try the spkg William posted.

Cheers,

Michael


---

Comment by jsp created at 2008-11-26 16:56:36

The spkg worked for me!



```
real	2m8.649s
user	1m32.105s
sys	0m5.449s
Successfully installed matplotlib-0.98.3.p3
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing matplotlib-0.98.3.p3.spkg



```


Jaap

So positive review!


---

Comment by jsp created at 2008-11-26 18:40:29

changed Cc: to jsp


---

Comment by was created at 2008-11-26 19:25:18

fix typo


---

Comment by mabshoff created at 2008-11-27 02:19:49

Spkg looks good to me, i.e. changes to SPKG.txt and so on. The only change I did was to update 

 * patches/setupext.py.diff

to reflect the fixes done by William to setupext.py. I always check the diff in between src and patches since that makes applying fixes from our end to upstream somewhat easier once we upgrade an spkg. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 02:21:59

Merged in Sage 3.2.1.alpha2


---

Comment by mabshoff created at 2008-11-27 02:21:59

Resolution: fixed


---

Comment by mabshoff created at 2008-11-27 02:26:43

The fix should obviously go upstream. I have a FreeBSD 7 build fix that I will submit in the not too distant future. I will also send this patch upstream then.

Cheers,

Michael
