# Issue 8474: Detect whether a program is in the path

Issue created by migration from https://trac.sagemath.org/ticket/8474

Original creator: jhpalmieri

Original creation time: 2010-03-07 05:15:31

Assignee: drkirkby

CC:  drkirby mhansen

In various places in the Sage library, we test for the existence of programs using code like this:

```
import os
if os.system('which program') == 0:
    # program exists
else:
    # it doesn't
```

On Solaris, executing "which program" seems to return 0 regardless of whether the program actually exists, and so any code like this is broken.  For example, try this on t2.math:

```
sage: from sage.misc.latex import have_latex
sage: have_latex()
True
sage: import os
sage: os.system('which latex')                                                                    
no latex in /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/lib /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/bin /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin
0
```


So we should have a function which replaces this, and we should use it in the Sage library.  On IRC, mhansen says

```
<mhansen> I think you can use "type" on Solaris
```

The "type" command actually works for me on several different platforms, and so it's what the patch uses.

This needs testing on lots more different platforms to make sure it's portable.



---

Comment by jhpalmieri created at 2010-03-07 05:18:54

This should also fix the problem at #8463.


---

Comment by jhpalmieri created at 2010-03-07 05:18:54

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-03-07 10:19:15

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-03-07 10:19:15

Hi, I believe this needs changing a little, as _type_ is nothing really like _which_. Here are a few specific points though. 

 * 'which' is not part of POSIX, so as such I think it is best avoided. It is not portable.
 * 'which' does exist on Solaris, so it should be ok(ish), though it would not be my first choice. However, the documented behavior (in the Solaris man page) of _which_ is to exit with an exit status of 0 if the command is found, and an exit status of >0 if the command is not found. So it should be ok for Solaris, even though I have reservations it is not a good command to use due to its non-portability. 
  {{{
drkirkby`@`hawk:~$ man which

User Commands                                            which(1)

NAME
     which - locate a command and display its pathname or alias

SYNOPSIS
     which [name]...
<snip>
EXIT STATUS
     The following exit values are returned:

     0      Successful completion.

     >0     One or more name operands  were  not  located  or  an
            error occurred.
  }}}

 Although I thought it highly unlikely to be a bug in Sun's implementation 'which', I decided to check. But that is not the problem, as the following code shows:
   {{{
drkirkby`@`hawk:~$ cat testit2
#!/bin/sh
which $1
if [ $? -ne 0 ]; then
    echo " can't find $1"
else
  echo "found $1"
fi
   }}}
 Running that script twice, first with a command one expects to find (ls), then one does not (tokoklklstgjglkjhs), we find it behaves as you expect, and how it is documented to behave.

   {{{
drkirkby`@`hawk:~$ ./testit2 ls
/usr/bin/ls
found ls
drkirkby`@`hawk:~$ ./testit2 tokoklklstgjglkjhs
no tokoklklstgjglkjhs in /export/home/drkirkby/bins-for-sage /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/bin /usr/csw/bin/ /usr/local/bin /usr/bin /usr/X11/bin /usr/openwin/bin
 can't find tokoklklstgjglkjhs
drkirkby`@`hawk:~$ 
   }}}

 So 'which' is behaving on Solaris in the way documented in the Solaris man page! It's also as documented in the Linux man page, so I suspect the problem might lie elsewhere. 

 * I have reservations about the use of _type_ too, as the output is nothing like that of _which_, as it does not show the path and only the path. It shows more information, in a more confusing way. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/type.html

  It will tell you if the command exits or not, but does not give the output in the same way as _which_ 
  {{{
drkirkby`@`hawk:~$ which ls
/usr/bin/ls
drkirkby`@`hawk:~$ type ls
ls is /usr/bin/ls
   }}}
 * After spending 10-15 minutes reading the POSIX specification, I've come to the conclusion what we should really be using is _command -v_ to find if a command exists, and if so its path. 

  http://www.opengroup.org/onlinepubs/9699919799/utilities/command.html

  {{{
NAME

    command - execute a simple command

SYNOPSIS

    command [-p] command_name [argument...]

    command [-p][-v|-V] command_name

DESCRIPTION

    The command utility shall cause the shell to treat the arguments as a simple command, suppressing the shell function lookup that is described in Command Search and Execution , item 1b.

    If the command_name is the same as the name of one of the special built-in utilities, the special properties in the enumerated list at the beginning of Special Built-In Utilities shall not occur. In every other respect, if command_name is not the name of a function, the effect of command (with no options) shall be the same as omitting command.

    When the -v or -V option is used, the command utility shall provide information concerning how a command name is interpreted by the shell.

OPTIONS

    The command utility shall conform to XBD Utility Syntax Guidelines .

    The following options shall be supported:

    -p
        Perform the command search using a default value for PATH that is guaranteed to find all of the standard utilities.
    -v
        Write a string to standard output that indicates the pathname or command that will be used by the shell, in the current shell execution environment (see Shell Execution Environment ), to invoke command_name, but do not invoke command_name. 
<snip>
EXIT STATUS

    When the -v or -V options are specified, the following exit values shall be returned:

     0
        Successful completion.
    >0
        The command_name could not be found or an error occurred. 
  }}}

So using _command -v_ has many advantages. 
 * It is part of POSIX
 * It's output is the same format as the 'which' command. 
 * It works on every system I have tried it on - these include
  * Linux
  * OS X
  * Solaris
  * HP-UX
  * FreeBSD
   
So, in summary, I believe _command -v_ is the most appropriate, but I can't understand why which is not working, as it is documented to work and I've tested it and found it does work. 

Comments? 

Dave


---

Comment by drkirkby created at 2010-03-07 15:22:54

Just to show you what I mean, here is the output when testing for an existing file, and a non-existing file. Note there is a different response from Solaris 10 (on SPARC) to all the others if the command is not found, but the exit code remains non-zero on Solaris 10 (SPARC).

If the command is found on Solaris 10, then the output is exactly the same as on every other platform, and exactly the same as 'which'. But I think 'command -v' is preferable, as it is more portable. 

On Solaris 10 (SPARC processor):

```
drkirkby@redstart:~$ command -v ls
/usr/bin/ls
drkirkby@redstart:~$ command -v fdsfdgddgt
-bash: command: fdsfdgddgt: not found
```


On HP-UX (PA-RISC processor):

```
-bash-4.0$ command -v ls                                                
/usr/bin/ls
-bash-4.0$ command -v lssdsssdfdf
-bash-4.0$ 
```


On OpenSolaris (Intel Xeon processor):


```
drkirkby@hawk:~$ command -v ls
/usr/bin/ls
drkirkby@hawk:~$ command -v klsddshfsd
drkirkby@hawk:~$ 
```


On OS X (Intel processor of some sort):

```
[kirkby@bsd ~]$ command -v ls
/bin/ls
[kirkby@bsd ~]$ command -v reererer
[kirkby@bsd ~]$ 
```


On Linux (Intel processor of some sort)

```
kirkby@sage:~$ command -v ls
/bin/ls
kirkby@sage:~$ command -v fdlkskld
kirkby@sage:~$ 
```


On FreeBSD (VirtualBox virtual machine, running on OpenSolaris host):

```
eagle# command -v ls
/bin/ls
eagle# command -v sdfdsf
eagle#
```



---

Comment by jhpalmieri created at 2010-03-07 16:44:49

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-07 16:44:49

Here's a new patch which uses "command -v".  On my mac, on sage.math, and on t2.math, "type" and "command -v" behave essentially the same, more or less like this:

```
sage: from subprocess import call, PIPE
sage: call('type ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)  # note the space in 'type '
0
sage: call('type ' + 'lljsdfs', shell=True, stdout=PIPE, stderr=PIPE)       
1
sage: call('command -v ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)      
0
sage: call('command -v ' + 'llkjsdfs', shell=True, stdout=PIPE, stderr=PIPE)
127
```

The only difference on the platforms is the value of the nonzero return code: sometimes it's 1, sometimes is 127, depending on the platform and the command.  It's always nonzero, though, when the program doesn't exist.

(With these arguments, the command "call" calls a program by passing to the shell without printing standard output or standard error, and it returns a code which is zero if the program exits correctly, nonzero otherwise, and I think the return codes have something to do with the system return codes, but they're not necessarily the same. See [http://docs.python.org/library/subprocess.html#convenience-functions](http://docs.python.org/library/subprocess.html#convenience-functions).)

Note that I don't care about the output of the functions, so your concern about "type" in that regard is not a big deal.  However, if "command -v" is Posix standard, we can switch to that, since it seems to behave the same way.

Regardless, I think you'll agree that it would be good to have one portable way to do this, in one place in the Sage library, so functions like "have_latex" and "have_chomp" will work right on Solaris, linux, Mac, etc.


---

Comment by jhpalmieri created at 2010-03-07 16:53:23

Just to emphasize: on t2.math, I get this behavior (in contrast to using "command -v" or "type"):

```
sage: from subprocess import call, PIPE
sage: call('which ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)
0
sage: call('which ' + 'lljsdfs', shell=True, stdout=PIPE, stderr=PIPE)
0
```

I don't know why.  The same happens with `os.system('which lljsdfs')`, and this is what is used in the Sage library.  ("call" is similar in behavior to "os.system", but I think "call" is slightly preferred.  It also gives better control of stdin, stdout, and stderr.)  So I do think this is what's wrong with #8463.  As I said in the description of this ticket, the function "have_latex" returns True on t2.math, and I would guess that if I could install Sage 4.3.4.alpha0 on t2.math, then the comparable "have_chomp" functions would return True as well.  Therefore Sage would try to call chomp when doing homology calculations, and since the program isn't there, it would crash.


---

Comment by mhansen created at 2010-03-07 18:01:53

Note that on t2 from the command-line


```
mhansen@t2:~$ which asdfasdfasfdsfsadf
no asdfasdfasfdsfsadf in /scratch/mhansen/bin /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin
mhansen@t2:~$ echo $?
0
```



---

Comment by jhpalmieri created at 2010-03-07 18:37:43

I installed Solaris on a virtual machine on my Mac:

```
$ uname -a
SunOS unknown 5.10 Generic_141445-09 i86pc i386 i386pc
```

and I get the same results that mhansen reported on t2.  Also, the man page for "which" doesn't discuss error codes.  It says, among other things

```
NOTES
     which is not a shell built-in command; it is the  UNIX  com-
     mand, /usr/bin/which
```

I haven't tried to install Sage on this (for one thing, I don't have gcc installed and I don't know how to get it), but I get similar results in python: running "call('which lsjdflsjdflkjs', ...)" returns 0, same as "call('which ls', ...)".


---

Comment by drkirkby created at 2010-03-07 19:02:28

OK, I think I understand this better now. 

I just noticed the example above where I showed 'which' behaving as expected was actually on OpenSolaris x64 (hostname hawk). However, I just tried it on Solaris 10 (SPARC), and get the same behavior. i.e. my script works as expected. 

I just tried what Mike did, using 'which ffddfdfd' on Solaris 10 (SPARC), Solaris 10 x64 (virtual machine) and OpenSolaris (x64). What I found was

 * 'which' has an exit code of 0 on Solaris 10 (SPARC).
 * 'which' has an exit code of 0 on Solaris 10 x86 (virtual machine).
 * 'which' an exit code of 1 on OpenSolaris. 

However, the man pages on OpenSolaris and Solaris 10 are different. The Solaris 10 man page does not discuss exit codes, but the OpenSolaris man page does. (This is one of the problems of using non-POSIX functions - their behavior is not well defined). 
 
I installed the patch and run the tests. All thse doctests then pass - there are still some other failures. 

I'm not a Python guru, but the patch all looks logical to me. So I'm going to give it positive review. 

One very minor niggle - you might want to change the example in the docstring. I think 


```
   sage: have_program('ls') 
   True 
   sage: have_program('there_is_not_a_program_with_this_name') 
   False 
```


would be a bit preferable to 


```
   sage: have_program('command') 
   True 
   sage: have_program('there_is_not_a_program_with_this_name') 
   False 
```


as far more people will know what 'ls' is. I doubt many will realise there is such a command called 'command'. I thought I knew Unix pretty well, but I was unaware of it until today. But it is a very minor point. 

So positive review from me. Change that docstring if you want, but otherwise leave it unchanged. 

I've also noticed a rather annoying message about a lack of _xdg-open_ before. It looks like it might have been related - I see you have fixed that too, so hopefully I won't see that any more. 

I agree it is more logical to have one library function that works on any system, rather than loads of different implementations which are not portable. 

Thank you very much John. 

*Note to the release manager*
When this is merged, #8463 may be closed. 

Dave


---

Comment by drkirkby created at 2010-03-07 19:02:28

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2010-03-08 20:56:14

Resolution: fixed
