# Issue 8474: Detect whether a program is in the path

archive/issues_008474.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirby @mwhansen\n\nIn various places in the Sage library, we test for the existence of programs using code like this:\n\n```\nimport os\nif os.system('which program') == 0:\n    # program exists\nelse:\n    # it doesn't\n```\n\nOn Solaris, executing \"which program\" seems to return 0 regardless of whether the program actually exists, and so any code like this is broken.  For example, try this on t2.math:\n\n```\nsage: from sage.misc.latex import have_latex\nsage: have_latex()\nTrue\nsage: import os\nsage: os.system('which latex')                                                                    \nno latex in /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/lib /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v /usr/local/sage-4.3.0.1-Solaris-10-SPARC-sun4u-or-sun4v/local/bin /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin\n0\n```\n\n\nSo we should have a function which replaces this, and we should use it in the Sage library.  On IRC, mhansen says\n\n```\n<mhansen> I think you can use \"type\" on Solaris\n```\n\nThe \"type\" command actually works for me on several different platforms, and so it's what the patch uses.\n\nThis needs testing on lots more different platforms to make sure it's portable.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8474\n\n",
    "created_at": "2010-03-07T05:15:31Z",
    "labels": [
        "component: porting",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Detect whether a program is in the path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8474",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: drkirkby

CC:  drkirby @mwhansen

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


Issue created by migration from https://trac.sagemath.org/ticket/8474





---

archive/issue_comments_076238.json:
```json
{
    "body": "This should also fix the problem at #8463.",
    "created_at": "2010-03-07T05:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76238",
    "user": "https://github.com/jhpalmieri"
}
```

This should also fix the problem at #8463.



---

archive/issue_comments_076239.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-07T05:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76239",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076240.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-07T10:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76240",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076241.json:
```json
{
    "body": "Hi, I believe this needs changing a little, as *type* is nothing really like *which*. Here are a few specific points though. \n\n* 'which' is not part of POSIX, so as such I think it is best avoided. It is not portable.\n* 'which' does exist on Solaris, so it should be ok(ish), though it would not be my first choice. However, the documented behavior (in the Solaris man page) of *which* is to exit with an exit status of 0 if the command is found, and an exit status of >0 if the command is not found. So it should be ok for Solaris, even though I have reservations it is not a good command to use due to its non-portability. \n  {{{\ndrkirkby`@`hawk:~$ man which\n\nUser Commands                                            which(1)\n\nNAME\n     which - locate a command and display its pathname or alias\n\nSYNOPSIS\n     which [name]...\n<snip>\nEXIT STATUS\n     The following exit values are returned:\n\n     0      Successful completion.\n\n     >0     One or more name operands  were  not  located  or  an\n            error occurred.\n  }}}\n\n Although I thought it highly unlikely to be a bug in Sun's implementation 'which', I decided to check. But that is not the problem, as the following code shows:\n   {{{\ndrkirkby`@`hawk:~$ cat testit2\n#!/bin/sh\nwhich $1\nif [ $? -ne 0 ]; then\n    echo \" can't find $1\"\nelse\n  echo \"found $1\"\nfi\n   }}}\n Running that script twice, first with a command one expects to find (ls), then one does not (tokoklklstgjglkjhs), we find it behaves as you expect, and how it is documented to behave.\n\n   {{{\ndrkirkby`@`hawk:~$ ./testit2 ls\n/usr/bin/ls\nfound ls\ndrkirkby`@`hawk:~$ ./testit2 tokoklklstgjglkjhs\nno tokoklklstgjglkjhs in /export/home/drkirkby/bins-for-sage /usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/bin /usr/csw/bin/ /usr/local/bin /usr/bin /usr/X11/bin /usr/openwin/bin\n can't find tokoklklstgjglkjhs\ndrkirkby`@`hawk:~$ \n   }}}\n\n So 'which' is behaving on Solaris in the way documented in the Solaris man page! It's also as documented in the Linux man page, so I suspect the problem might lie elsewhere. \n\n* I have reservations about the use of *type* too, as the output is nothing like that of *which*, as it does not show the path and only the path. It shows more information, in a more confusing way. \n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/type.html\n\n  It will tell you if the command exits or not, but does not give the output in the same way as *which* \n  {{{\ndrkirkby`@`hawk:~$ which ls\n/usr/bin/ls\ndrkirkby`@`hawk:~$ type ls\nls is /usr/bin/ls\n   }}}\n* After spending 10-15 minutes reading the POSIX specification, I've come to the conclusion what we should really be using is *command -v* to find if a command exists, and if so its path. \n\n  http://www.opengroup.org/onlinepubs/9699919799/utilities/command.html\n\n  {{{\nNAME\n\n    command - execute a simple command\n\nSYNOPSIS\n\n    command [-p] command_name [argument...]\n\n    command [-p][-v|-V] command_name\n\nDESCRIPTION\n\n    The command utility shall cause the shell to treat the arguments as a simple command, suppressing the shell function lookup that is described in Command Search and Execution , item 1b.\n\n    If the command_name is the same as the name of one of the special built-in utilities, the special properties in the enumerated list at the beginning of Special Built-In Utilities shall not occur. In every other respect, if command_name is not the name of a function, the effect of command (with no options) shall be the same as omitting command.\n\n    When the -v or -V option is used, the command utility shall provide information concerning how a command name is interpreted by the shell.\n\nOPTIONS\n\n    The command utility shall conform to XBD Utility Syntax Guidelines .\n\n    The following options shall be supported:\n\n    -p\n        Perform the command search using a default value for PATH that is guaranteed to find all of the standard utilities.\n    -v\n        Write a string to standard output that indicates the pathname or command that will be used by the shell, in the current shell execution environment (see Shell Execution Environment ), to invoke command_name, but do not invoke command_name. \n<snip>\nEXIT STATUS\n\n    When the -v or -V options are specified, the following exit values shall be returned:\n\n     0\n        Successful completion.\n    >0\n        The command_name could not be found or an error occurred. \n  }}}\n\nSo using *command -v* has many advantages. \n* It is part of POSIX\n* It's output is the same format as the 'which' command. \n* It works on every system I have tried it on - these include\n  * Linux\n  * OS X\n  * Solaris\n  * HP-UX\n  * FreeBSD\n   \nSo, in summary, I believe *command -v* is the most appropriate, but I can't understand why which is not working, as it is documented to work and I've tested it and found it does work. \n\nComments? \n\nDave",
    "created_at": "2010-03-07T10:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76241",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi, I believe this needs changing a little, as *type* is nothing really like *which*. Here are a few specific points though. 

* 'which' is not part of POSIX, so as such I think it is best avoided. It is not portable.
* 'which' does exist on Solaris, so it should be ok(ish), though it would not be my first choice. However, the documented behavior (in the Solaris man page) of *which* is to exit with an exit status of 0 if the command is found, and an exit status of >0 if the command is not found. So it should be ok for Solaris, even though I have reservations it is not a good command to use due to its non-portability. 
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

* I have reservations about the use of *type* too, as the output is nothing like that of *which*, as it does not show the path and only the path. It shows more information, in a more confusing way. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/type.html

  It will tell you if the command exits or not, but does not give the output in the same way as *which* 
  {{{
drkirkby`@`hawk:~$ which ls
/usr/bin/ls
drkirkby`@`hawk:~$ type ls
ls is /usr/bin/ls
   }}}
* After spending 10-15 minutes reading the POSIX specification, I've come to the conclusion what we should really be using is *command -v* to find if a command exists, and if so its path. 

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

So using *command -v* has many advantages. 
* It is part of POSIX
* It's output is the same format as the 'which' command. 
* It works on every system I have tried it on - these include
  * Linux
  * OS X
  * Solaris
  * HP-UX
  * FreeBSD
   
So, in summary, I believe *command -v* is the most appropriate, but I can't understand why which is not working, as it is documented to work and I've tested it and found it does work. 

Comments? 

Dave



---

archive/issue_comments_076242.json:
```json
{
    "body": "Just to show you what I mean, here is the output when testing for an existing file, and a non-existing file. Note there is a different response from Solaris 10 (on SPARC) to all the others if the command is not found, but the exit code remains non-zero on Solaris 10 (SPARC).\n\nIf the command is found on Solaris 10, then the output is exactly the same as on every other platform, and exactly the same as 'which'. But I think 'command -v' is preferable, as it is more portable. \n\nOn Solaris 10 (SPARC processor):\n\n```\ndrkirkby@redstart:~$ command -v ls\n/usr/bin/ls\ndrkirkby@redstart:~$ command -v fdsfdgddgt\n-bash: command: fdsfdgddgt: not found\n```\n\n\nOn HP-UX (PA-RISC processor):\n\n```\n-bash-4.0$ command -v ls                                                \n/usr/bin/ls\n-bash-4.0$ command -v lssdsssdfdf\n-bash-4.0$ \n```\n\n\nOn OpenSolaris (Intel Xeon processor):\n\n\n```\ndrkirkby@hawk:~$ command -v ls\n/usr/bin/ls\ndrkirkby@hawk:~$ command -v klsddshfsd\ndrkirkby@hawk:~$ \n```\n\n\nOn OS X (Intel processor of some sort):\n\n```\n[kirkby@bsd ~]$ command -v ls\n/bin/ls\n[kirkby@bsd ~]$ command -v reererer\n[kirkby@bsd ~]$ \n```\n\n\nOn Linux (Intel processor of some sort)\n\n```\nkirkby@sage:~$ command -v ls\n/bin/ls\nkirkby@sage:~$ command -v fdlkskld\nkirkby@sage:~$ \n```\n\n\nOn FreeBSD (VirtualBox virtual machine, running on OpenSolaris host):\n\n```\neagle# command -v ls\n/bin/ls\neagle# command -v sdfdsf\neagle#\n```\n",
    "created_at": "2010-03-07T15:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76242",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_076243.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-07T16:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76243",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076244.json:
```json
{
    "body": "Here's a new patch which uses \"command -v\".  On my mac, on sage.math, and on t2.math, \"type\" and \"command -v\" behave essentially the same, more or less like this:\n\n```\nsage: from subprocess import call, PIPE\nsage: call('type ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)  # note the space in 'type '\n0\nsage: call('type ' + 'lljsdfs', shell=True, stdout=PIPE, stderr=PIPE)       \n1\nsage: call('command -v ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)      \n0\nsage: call('command -v ' + 'llkjsdfs', shell=True, stdout=PIPE, stderr=PIPE)\n127\n```\n\nThe only difference on the platforms is the value of the nonzero return code: sometimes it's 1, sometimes is 127, depending on the platform and the command.  It's always nonzero, though, when the program doesn't exist.\n\n(With these arguments, the command \"call\" calls a program by passing to the shell without printing standard output or standard error, and it returns a code which is zero if the program exits correctly, nonzero otherwise, and I think the return codes have something to do with the system return codes, but they're not necessarily the same. See [http://docs.python.org/library/subprocess.html#convenience-functions](http://docs.python.org/library/subprocess.html#convenience-functions).)\n\nNote that I don't care about the output of the functions, so your concern about \"type\" in that regard is not a big deal.  However, if \"command -v\" is Posix standard, we can switch to that, since it seems to behave the same way.\n\nRegardless, I think you'll agree that it would be good to have one portable way to do this, in one place in the Sage library, so functions like \"have_latex\" and \"have_chomp\" will work right on Solaris, linux, Mac, etc.",
    "created_at": "2010-03-07T16:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76244",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_076245.json:
```json
{
    "body": "Just to emphasize: on t2.math, I get this behavior (in contrast to using \"command -v\" or \"type\"):\n\n```\nsage: from subprocess import call, PIPE\nsage: call('which ' + 'ls', shell=True, stdout=PIPE, stderr=PIPE)\n0\nsage: call('which ' + 'lljsdfs', shell=True, stdout=PIPE, stderr=PIPE)\n0\n```\n\nI don't know why.  The same happens with `os.system('which lljsdfs')`, and this is what is used in the Sage library.  (\"call\" is similar in behavior to \"os.system\", but I think \"call\" is slightly preferred.  It also gives better control of stdin, stdout, and stderr.)  So I do think this is what's wrong with #8463.  As I said in the description of this ticket, the function \"have_latex\" returns True on t2.math, and I would guess that if I could install Sage 4.3.4.alpha0 on t2.math, then the comparable \"have_chomp\" functions would return True as well.  Therefore Sage would try to call chomp when doing homology calculations, and since the program isn't there, it would crash.",
    "created_at": "2010-03-07T16:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76245",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_076246.json:
```json
{
    "body": "Note that on t2 from the command-line\n\n\n```\nmhansen@t2:~$ which asdfasdfasfdsfsadf\nno asdfasdfasfdsfsadf in /scratch/mhansen/bin /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin\nmhansen@t2:~$ echo $?\n0\n```\n",
    "created_at": "2010-03-07T18:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76246",
    "user": "https://github.com/mwhansen"
}
```

Note that on t2 from the command-line


```
mhansen@t2:~$ which asdfasdfasfdsfsadf
no asdfasdfasfdsfsadf in /scratch/mhansen/bin /usr/local/gcc-4.4.1-sun-linker/bin /usr/local/bin2 /usr/bin /usr/ccs/bin /usr/local/bin /usr/sfw/bin /bin /usr/sbin
mhansen@t2:~$ echo $?
0
```




---

archive/issue_comments_076247.json:
```json
{
    "body": "I installed Solaris on a virtual machine on my Mac:\n\n```\n$ uname -a\nSunOS unknown 5.10 Generic_141445-09 i86pc i386 i386pc\n```\n\nand I get the same results that mhansen reported on t2.  Also, the man page for \"which\" doesn't discuss error codes.  It says, among other things\n\n```\nNOTES\n     which is not a shell built-in command; it is the  UNIX  com-\n     mand, /usr/bin/which\n```\n\nI haven't tried to install Sage on this (for one thing, I don't have gcc installed and I don't know how to get it), but I get similar results in python: running \"call('which lsjdflsjdflkjs', ...)\" returns 0, same as \"call('which ls', ...)\".",
    "created_at": "2010-03-07T18:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76247",
    "user": "https://github.com/jhpalmieri"
}
```

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

archive/issue_comments_076248.json:
```json
{
    "body": "OK, I think I understand this better now. \n\nI just noticed the example above where I showed 'which' behaving as expected was actually on OpenSolaris x64 (hostname hawk). However, I just tried it on Solaris 10 (SPARC), and get the same behavior. i.e. my script works as expected. \n\nI just tried what Mike did, using 'which ffddfdfd' on Solaris 10 (SPARC), Solaris 10 x64 (virtual machine) and OpenSolaris (x64). What I found was\n\n* 'which' has an exit code of 0 on Solaris 10 (SPARC).\n* 'which' has an exit code of 0 on Solaris 10 x86 (virtual machine).\n* 'which' an exit code of 1 on OpenSolaris. \n\nHowever, the man pages on OpenSolaris and Solaris 10 are different. The Solaris 10 man page does not discuss exit codes, but the OpenSolaris man page does. (This is one of the problems of using non-POSIX functions - their behavior is not well defined). \n \nI installed the patch and run the tests. All thse doctests then pass - there are still some other failures. \n\nI'm not a Python guru, but the patch all looks logical to me. So I'm going to give it positive review. \n\nOne very minor niggle - you might want to change the example in the docstring. I think \n\n\n```\n   sage: have_program('ls') \n   True \n   sage: have_program('there_is_not_a_program_with_this_name') \n   False \n```\n\n\nwould be a bit preferable to \n\n\n```\n   sage: have_program('command') \n   True \n   sage: have_program('there_is_not_a_program_with_this_name') \n   False \n```\n\n\nas far more people will know what 'ls' is. I doubt many will realise there is such a command called 'command'. I thought I knew Unix pretty well, but I was unaware of it until today. But it is a very minor point. \n\nSo positive review from me. Change that docstring if you want, but otherwise leave it unchanged. \n\nI've also noticed a rather annoying message about a lack of *xdg-open* before. It looks like it might have been related - I see you have fixed that too, so hopefully I won't see that any more. \n\nI agree it is more logical to have one library function that works on any system, rather than loads of different implementations which are not portable. \n\nThank you very much John. \n\n**Note to the release manager**\nWhen this is merged, #8463 may be closed. \n\nDave",
    "created_at": "2010-03-07T19:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76248",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

I've also noticed a rather annoying message about a lack of *xdg-open* before. It looks like it might have been related - I see you have fixed that too, so hopefully I won't see that any more. 

I agree it is more logical to have one library function that works on any system, rather than loads of different implementations which are not portable. 

Thank you very much John. 

**Note to the release manager**
When this is merged, #8463 may be closed. 

Dave



---

archive/issue_comments_076249.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-07T19:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76249",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076250.json:
```json
{
    "body": "Attachment [trac_8474-have-program.patch](tarball://root/attachments/some-uuid/ticket8474/trac_8474-have-program.patch) by @mwhansen created at 2010-03-08 20:56:14",
    "created_at": "2010-03-08T20:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76250",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8474-have-program.patch](tarball://root/attachments/some-uuid/ticket8474/trac_8474-have-program.patch) by @mwhansen created at 2010-03-08 20:56:14



---

archive/issue_comments_076251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-08T20:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8474#issuecomment-76251",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
