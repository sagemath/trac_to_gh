# Issue 7156: prereq-0.4 has a minor portability issue.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-08 14:28:05

Assignee: tbd

My recently updated prereq-0.4 #7021 has a minor portability issue, which existed in version 0.3 too. If run on HP-UX, which the 'uname' command does not support the -p option needed to get the processor, so generates the following message:

```
Starting prerequisite check.
Machine: HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]
```


The reason is quite simple. The code which checks for an operating system which is not Solaris SPARC uses this: 

```

    elif [ `uname` = "SunOS" -a "`uname -p`" != "sparc" ]; then
        echo "Building or using Sage on non-Sparc Solaris is tricky and not supported"
        echo "at the moment. It is possible, but you should be well aware that"
        echo "some things do not work. Support for Solaris"
        echo "on non-SPARC hardware is actively being worked on."
        echo "To get past this message, export the variable SAGE_PORT to"
        echo "something non-empty."
        exit 1
    elif [ `uname` = "HP-UX" ]; then

```


It would better be changed to 


```
    elif [ `uname` = "SunOS" ]; then
       # The -p option to 'uname' is not portable (HP-UX does not support it for example)
       # So it is safer to test for Solaris first, then test for the processor with the
       # -p option if necessary.
       if [ "`uname -p`" != "sparc" ]; then
          echo "Building or using Sage on non-Sparc Solaris is tricky and not supported"
          echo "at the moment. It is possible, but you should be well aware that"
          echo "some things do not work. Support for Solaris"
          echo "on non-SPARC hardware is actively being worked on."
          echo "To get past this message, export the variable SAGE_PORT to"
          echo "something non-empty."
          exit 1
       fi
    elif [ `uname` = "HP-UX" ]; then

```


which would then only use the -p option on Solaris. 

I'll update this at one point in the future. I expect I'll get some feedback from the prereq-0.4, so I'll created a 0.5 at some time in the future. 

This does not actually terminate the build process on HP-UX, so even for a port, it is not a big issue. 




---

Comment by mhansen created at 2009-11-20 06:20:56

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 06:20:56

Fixed by #7352
