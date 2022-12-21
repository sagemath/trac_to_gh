# Issue 6287: sage -lisp should run ECL

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-14 20:56:44

Assignee: mabshoff

CC:  awebb

When we upgraded Sage from Clisp to ECL we forgot to make it so

```
sage -lisp
}}} 
works and runs ecl.  Right now it still runs clisp if that happens to be on your system, which is silly.



---

Comment by awebb created at 2009-06-21 13:35:27

Replaced sage -clisp with sage -ecl and pointed sage -lisp at ecl.


---

Attachment

oops, forgot to change clisp to ecl in one line.  ~ Adam


---

Comment by drkirkby created at 2009-08-19 13:48:47

Can you post a link to an .spkg I can test. I'll then review this.


---

Comment by awebb created at 2009-08-19 15:51:50

There is only the patch for the sage-sage script. When I made it I did not know which spkg it was in but I believe it is in sage-scripts. I just applied the patch directly to the mercurial repository in sage/local/bin. ~ Adam


---

Comment by drkirkby created at 2009-08-20 10:18:13

I'm not really sure how to check this. I tried to build clisp on my SPARC, but I was unable to get it to build with either gcc or the Sun compiler. I then thought I'd create a dummy executable 'clisp', put that early in my path, and see if sage would run that, rather than ecl. But all I get is an error about a command not being found. 


```
[~/sage/sage-4.1.1] $ ./sage -lisp
/export/home/drkirkby/sage/sage-4.1.1/local/bin/sage-sage: line 297: lisp: command not found
```


Despite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. 

Sorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. 

Dave


---

Comment by awebb created at 2009-08-20 11:12:07

Replying to [comment:7 drkirkby]:

> Despite having the directory with 'clisp' early in the path, maxima in Sage still pick up 'ecl'. 
> 
> Sorry, but I don't feel able to test this, as I can't build clisp and are not really sure what should happen. 
> 
> Dave 

Hi,
The whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead. The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing. In other words, if either command is used from the shell you get the ecl console. I took out 'sage -clisp' but should it stay for if someone wants it?

Adam


---

Comment by saliola created at 2009-08-28 14:38:42

Replying to [comment:8 awebb]:
> The whole point of the ticket is that clisp is no longer used and that sage should look for ecl instead.

Correct.

> The patch tells 'sage -lisp' to use ecl instead of clisp. I also added a 'sage -ecl' which does the same thing.

Great.

> I took out 'sage -clisp' but should it stay for if someone wants it?

I agree that it should be removed. All commands of the form `sage -program` run the version of `program` distributed with sage. Since we are no longer distributing clisp, keeping the clisp alias has the potential of causing confusion for a user.

*Positive review*: the patch applies cleanly on top of sage-4.1.1; and `sage -ecl` and `sage -lisp` now work as they should.


---

Comment by mvngu created at 2009-08-30 11:46:44

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 11:46:44

Doing any of these "./sage -ecl" or "./sage -lisp" would run ECL as expected. Also:

```
sage: !ecl
ECL (Embeddable Common-Lisp) 9.4.1
Copyright (C) 1984 Taiichi Yuasa and Masami Hagiya
Copyright (C) 1993 Giuseppe Attardi
Copyright (C) 2000 Juan J. Garcia-Ripoll
ECL is free software, and you are welcome to redistribute it
under certain conditions; see file 'Copyright' for details.
Type :h for Help.  Top level.
>
```

And if Clisp is installed on your system:

```
sage: !clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.42 (2007-10-16) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2007

Type :h and hit Enter for context help.

[1]> :h
You are in the top-level Read-Eval-Print loop.
Help (abbreviated :h) = this list
Use the usual editing capabilities.
(quit) or (exit) leaves CLISP.
[2]> 
Bye.
```

So one still has the option of running Clisp from within the Sage command line interface.
