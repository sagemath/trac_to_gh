# Issue 8391: Temporary ugly fix: Change 'top' to 'prstat' on Solaris for 'getusage.py'

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-27 19:18:49

Assignee: drkirkby

The file 'getusage.py' has two main functions. 

 * top() - Display the output of the 'top' command for the current process. 
 * get_memory_usage() - Display the memory usage in MB. 

The implementation on Solaris is particularly poor for many reasons. 
 * The Sage function 'top()' calls the external command 'top' on Solaris, despite the fact that 'top' has never been part of the Solaris operating system. (The command has to be installed, but is not standard.)
 * The Sage function get_memory_usage() calls the function top(), so obviously breaks get_memory_usage() fails if the command 'top' is not installed. 
 * 'top' is not very accurate on modern Solaris versions - is was OK 10+ years ago, but not now. 
 * You need root access to install 'top'. 
 * The ticket #6028 created by Micheal Abshoff with the title "get_memory_usage() sucks performance wise on Solaris" gives a gentle hint at one more problem. 
 * Running the Sage doctests brings a system to an almost standstill if top is not installed. The non-existent 'top' is run multiple times in a loop in an attempt to overcome some race condition. 
 * I believe not having 'top' is causing doctest failures, which brings the system to an almost standstill as documented at #7153.

*Overall, the usage of 'top' in Solaris is a disaster.* The proper way to get the memory usage is to use a system call, but it is going to take some effort to sort out how to do so and is not high on the list of priorities. 

A command with similar functionality to 'top', but greater accuracy is '/usr/bin/prstat' which comes as part of all recent versions of Solaris. The output looks similar to that of 'top'


```
   PID USERNAME  SIZE   RSS STATE  PRI NICE      TIME  CPU PROCESS/NLWP       
   604 drkirkby  189M  106M cpu2    59    0 537:45:37  11% Xorg/1
 28286 drkirkby   78M   19M sleep   32    0 244:22:50 5.2% zenity/1
 15753 drkirkby  553M  517M sleep   49    0  46:10:43 0.5% VirtualBox/24
 14951 drkirkby  345M  161M sleep   48    0   0:07:45 0.3% firefox-bin/20
 22223 drkirkby  163M   80M sleep   59    0   0:06:58 0.0% gnome-terminal/2
   731 drkirkby  106M   26M sleep   59    0   0:14:12 0.0% gnome-netstatus/2
   719 drkirkby  113M   34M sleep   59    0   0:08:23 0.0% wnck-applet/1
  7703 drkirkby 6328K 3144K cpu3    49    0   0:00:00 0.0% prstat/1
   730 drkirkby  107M   26M sleep   59    0   0:09:18 0.0% mixer_applet2/1
   741 root     1636K 1080K sleep   59    0   0:12:55 0.0% gnome-netstatus/1
   663 drkirkby   94M   35M sleep   59    0   0:06:55 0.0% metacity/1
   294 root     4804K 2056K sleep   59    0   0:00:00 0.0% dbus-daemon/1
   153 root     6396K 2824K sleep   59    0   0:00:00 0.0% picld/4
   385 root     5140K 1576K sleep   59    0   0:00:00 0.0% automountd/2
   270 root     4596K 1420K sleep   59    0   0:00:02 0.0% cron/1
Total: 141 processes, 389 lwps, load averages: 1.79, 1.70, 1.66
```


Hence I propose to replace the call to 'top' with one to 'prstat'. Despite I know this is not the correct way to determine memory usage, using 'prstat' is at least better than the current implementation using 'top'


---

Comment by drkirkby created at 2010-02-28 01:26:36

Here is the output of an modified version of Sage 4.4.3, where top is not installed. The modifications were only to get Sage to build at this point. The hardware is a Sun Blade 1000 with 2 GB RAM. 

top() reports that 'top' is not found, and get_memory_usage() goes into an infinite loop. If you look at the source code, you can see why the infinite loop exists. 


```
-bash-3.00$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: top()
sh: top: not found
''
sage: get_memory_usage()
sh: top: not found
sh: top: not found
sh: top: not found
sh: top: not found
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
Here is the output of the same two commands with the changes I will soon attach.


```
drkirkby`@`redstart:~/fresh/sage-4.3.3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: top()
'25519 drkirkby  164M   91M sleep   59    0   0:00:07 9.2% python/1'
sage: get_memory_usage()
91.0
```

| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
The program 'top' is not installed - instead prstat is used to get the information. I also expanded the information someone gets when using help(top) or help(get_usage_message) - see below. 


```
sage: help(top)
Help on function top in module sage.misc.getusage:

top()
    Return the 'top' or 'prstat' line that contains this running 
    Sage process.
    
    EXAMPLES:
        sage: top()              # random output
        '72373 python       0.0%  0:01.36   1    14+  1197   39M+   34M+   55M+  130M+'
    
    NOTES:
    The external command 'top' (http://www.unixtop.org/) is called on Linux, 
    and most other operating systems. The output format of 'top' is not 
    consistent across all platforms and all versions of 'top'. If the 
    top() function does not work in Sage, you may need to install 'top'.
    
    The external command 'prstat' is called on the Solaris and OpenSolaris 
    systems. That is part of Solaris, and will not need to be installed. The 
    columns used in the 'prstat' output are: 
    PID USERNAME  SIZE   RSS STATE  PRI NICE      TIME  CPU PROCESS/NLWP

sage: help(get_memory_usage)
Help on function get_memory_usage in module sage.misc.getusage:

get_memory_usage(t=None)
    Return memory usage.
    
    INPUT:
    
    -  ``t`` - None or output of previous call; (only used
       on Linux)
    
    OUTPUT:
    
    - ``Linux`` - Returns float number (in megabytes)
    
    - ``OS X`` - Returns float number (in megabytes) that matches VSIZE column of 'top'
    
    - ``Solaris or OpenSolaris`` - Returns float number (in megabytes) that matches RSS 
        column of 'prstat'. Depending on the memory usage, 'prstat' will output the
        data in KB, MB or GB. In each case, the value returned by this function will
        always be in MB. 
        
    
    - ``other`` - not implemented for any other operating systems
    
    EXAMPLES:
    
    We test that memory usage doesn't change instantly::
    
        sage: t = get_memory_usage()
        sage: get_memory_usage(t)          # amount of memory more than when we defined t.
        0.0
    
    NOTES:
      
    Currently get_memory_usage() calls ''prstat' (Solaris and 
    OpenSolaris) to get the data it requires. In the long term, 
    a better solution would be to use Solaris system calls. 
    
    In some instances, 'top' may be used on OS X. This may break
    if the memory usage is greater than 9999 MB. However, normally
    'top' is not used on OS X.

sage: 

```



---

Comment by drkirkby created at 2010-02-28 01:38:11

Mercurial patch


---

Attachment

I'm removing the 'temporary and ugly fix' from the title, as this actually works quite well now.


---

Comment by mvngu created at 2010-03-01 01:56:31

Changing status from new to needs_review.


---

Attachment

Use `prstat` instead of `top` on (Open)Solaris.  Docstring tweaks.


---

Comment by mpatel created at 2010-03-03 09:04:47

I've attached an updated patch with minor (mostly docstring) tweaks.  Please see the [developer's guide](http://www.sagemath.org/doc/developer/index.html) for useful tips and recommendations.

Just to double check: Is the multiplier / divisor definitely not 1024?


---

Attachment

Updated with multipy/divide=1024. I could not overwrite the original


---

Comment by drkirkby created at 2010-03-03 11:38:39

Thank you for the tip. You are correct of course, the conversion from KB -> MB ->GB should use multipliers of 1024, not 1000. I don't know what I was thinking then. 

I was unable to overwrite the ticket, but instead got the message

_"ATTACHMENT_DELETE privileges are required to perform this operation on Attachments of Ticket #8391_'

So I created this with a new file name.


---

Comment by jsp created at 2010-03-03 20:42:26

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-03-03 20:42:26

Looks good to me. This effects (Open) Solaris only.

I'll give a positive review.

Jaap


---

Comment by mhansen created at 2010-03-06 08:26:50

Resolution: fixed
