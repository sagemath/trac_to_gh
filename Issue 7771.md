# Issue 7771: fix R restart in interface

Issue created by migration from https://trac.sagemath.org/ticket/7771

Original creator: kcrisman

Original creation time: 2009-12-27 03:58:13

Assignee: was

This nearly always happens after installing an R package and then following the directions Sage gives:

```
sage: r.restart()
Error: object 'sage0' not found
```

This seems to be unrelated to whether R has recommended packages installed or not, so I am making a new ticket for this.  Making it minor since just restarting Sage takes care of things as well.


---

Comment by mvngu created at 2010-02-03 06:29:27

As of Sage 4.3.2.alpha1, ticket #6532 upgrades R to version 2.10.1. From what I gather, after installing an R package, one needs to restart Sage:

```
[mvngu@mod sage-4.3.2.alpha1]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: r.install_packages("cluster")
<downloading-compiling-messages>
* DONE (cluster)
| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |
| Type notebook() for the GUI, and license() for information.        |
The downloaded packages are in
	‘/tmp/RtmpqofuAu/downloaded_packages’
Updating HTML index of packages in '.Library'
> 
Please restart Sage in order to use 'cluster'.
sage: exit
Exiting SAGE (CPU time 0m0.05s, Wall time 0m38.43s).
```

It didn't say to use the command `r.restart()`. What about issuing `reset()` after installing an R package? It works for me:

```
sage: r.install_packages("igraph")
<downloading-compiling-messages>
* DONE (igraph)

The downloaded packages are in
	‘/tmp/RtmpllHMEs/downloaded_packages’
Updating HTML index of packages in '.Library'
> 
Please restart Sage in order to use 'igraph'.
sage: reset()
sage: r.library("igraph")
```

Perhaps you want the command `r.restart()` to achieve the same effect as `exit` and `reset()`? That is, one could install an R package with `r.install_packages("pkg-name")`, run `r.reset()`, and then load the newly installed package with `r.library("pkg-name")`? As a side note, one could not install R packages with a binary Sage distribution.


---

Comment by kcrisman created at 2010-02-03 15:39:49

Replying to [comment:1 mvngu]:
> As of Sage 4.3.2.alpha1, ticket #6532 upgrades R to version 2.10.1. From what I gather, after installing an R package, one needs to restart Sage:
> It didn't say to use the command `r.restart()`. 

Yes, that is a change I made since r.restart() didn't work, but in the source it is commented that this _should_ work.

> What about issuing `reset()` after installing an R package? It works for me:
> Perhaps you want the command `r.restart()` to achieve the same effect as `exit` and `reset()`? That is, one could install an R package with `r.install_packages("pkg-name")`, run `r.reset()`, and then load the newly installed package with `r.library("pkg-name")`?

Maybe; I am not familiar with the reset command.  Maybe that is what restart was supposed to do all along?  We should ask an R expert.

> As a side note, one could not install R packages with a binary Sage distribution.

Oh, that is bad.  I wonder why?  One can install optional spkgs in a binary install, correct?


---

Comment by kcrisman created at 2010-04-27 20:06:06

Replying to [comment:2 kcrisman]:
> Replying to [comment:1 mvngu]:
> > As of Sage 4.3.2.alpha1, ticket #6532 upgrades R to version 2.10.1. From what I gather, after installing an R package, one needs to restart Sage:
> > It didn't say to use the command `r.restart()`. 
> 
> Yes, that is a change I made since r.restart() didn't work, but in the source it is commented that this _should_ work.

Yikes!  Turns out that...

```
## <entry>
## Deprecated in 1.6.0
## Defunct in 1.7.0
machine <- function() .Defunct()
Machine <- function() .Defunct(".Machine")
Platform <- function() .Defunct(".Platform")
restart <- function() .Defunct("try")
## </entry>
```

Note that R is now at version 2.10.1!   So this is the problem here.  The restart() thing must be very old - and odd, since the function that replaced it was try (for exception handling.  Anyway, if reset() is good enough, that is fine - no need to do r.foo() if a normal Sage command does it well enough.  I'll work on a patch for this.


---

Comment by kcrisman created at 2010-04-27 20:16:20

In fact, it's not even clear whether one needs to reset().  

```
Please restart Sage in order to use 'igraph'.
sage: r.library("igraph")
sage: a = r.graph_ring(10)
sage: a
Vertices: 10 
Edges: 10 
Directed: FALSE 
Edges:
          
[0] 0 -- 1
[1] 1 -- 2
[2] 2 -- 3
[3] 3 -- 4
[4] 4 -- 5
[5] 5 -- 6
[6] 6 -- 7
[7] 7 -- 8
[8] 8 -- 9
[9] 0 -- 9
sage: r.add_edges(a, (1,5,2,6) )
Vertices: 10 
Edges: 12 
Directed: FALSE 
Edges:
           
[0]  0 -- 1
[1]  1 -- 2
[2]  2 -- 3
[3]  3 -- 4
[4]  4 -- 5
[5]  5 -- 6
[6]  6 -- 7
[7]  7 -- 8
[8]  8 -- 9
[9]  0 -- 9
[10] 1 -- 5
[11] 2 -- 6
```

And this on an install which definitely hadn't had this package installed before.  The same happened with package 'aaMI'.  Which leads me to believe one doesn't even have to reset() - the package is just automatically available.  I'm going to put up a patch to that effect, with the covering statement to use reset() or restart Sage if you encounter problems.


---

Attachment

Based on Sage 4.3.5


---

Comment by kcrisman created at 2010-04-27 20:29:48

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-04-27 20:29:48

This may need slight rebasing after #7665.


---

Comment by kcrisman created at 2010-05-09 00:30:09

Replying to [comment:5 kcrisman]:
> This may need slight rebasing after #7665.   
No rebase needed to apply to 4.4.1, as it turns out.  Someone please review, it's an easy one!


---

Attachment

With the patch [trac_7771-r-restart.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7771/trac_7771-r-restart.patch), I got the following failure when doctesting with "-t -long -optional":


```
Expected:
    R is free software and comes with ABSOLUTELY NO WARRANTY.
    You are welcome to redistribute it under certain conditions.
    Type 'license()' or 'licence()' for distribution details.
    ...
    The R package 'aaMI' may now be loaded via r.library('aaMI').
    If this should not work, type reset(), or restart Sage.
Got:
    The R package 'aaMI' may now be loaded via r.library('aaMI').
    If this should not work, type reset(), or restart Sage.
```


It might be simpler to just test for the output:


```
The R package 'aaMI' may now be loaded via r.library('aaMI').
If this should not work, type reset(), or restart Sage.
```


I have attached a reviewer patch that does only that. With both patches, I now get the following failure:


```sh
[mvngu@sage sage-4.4.1]$ ./sage -t -long -optional devel/sage-main/sage/interfaces/r.py 
sage -t -long -optional "devel/sage-main/sage/interfaces/r.py"

<output-trancated>

File "/dev/shm/mvngu/sandbox/sage-4.4.1/devel/sage-main/sage/interfaces/r.py", line 1755:
    sage: latex(r(2))  #optional requires the Hmisc R package
Expected:
    2
Got:
    % latex.default(sage12, file = "") 
    %
    \begin{table}[!tbp]
     \begin{center}
     \begin{tabular}{r}\hline\hline
    \multicolumn{1}{c}{}\tabularnewline
    \hline
    $2$\tabularnewline
    \hline
    \end{tabular}
    <BLANKLINE>
    \end{center}
    <BLANKLINE>
    \end{table}
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_67
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_r.py
	 [11.5 s]
```


But that is for another ticket. So only my patch needs reviewing by anyone but me.


---

Comment by kcrisman created at 2010-05-10 15:48:36

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-05-10 15:48:36

The above isn't really a problem; it says explicitly that it requires the Hmisc R package, and should be expected to fail unless you have it, which is why it's optional.

The change in the reviewer patch is not okay, though.  If R does not start or causes an error, it is silent, but the two print statements will still happen (I just checked this by introducing a typo in the R command).  Can you try that again - I assume you were connected to the internet when you tested it, as the optional flag says?


---

Comment by kcrisman created at 2010-05-25 14:37:43

I see now - you already had loaded Hmisc, and apparently it changed its default Latexing.  I can change the patch to fix this.

However, as I said, I still disagree with the reviewer patch.  I don't know what to do, though, because apparently doctesting changed and now all things like that loading and downloading happen "before" the actual doctest, at least in how it turns out.  I'm not sure what to do about that, because I get the same thing whether I'm connected to the internet or not, which clearly should not be the case for an optional internet doctest!  Suggestions?


---

Comment by kcrisman created at 2012-05-21 13:18:52

Changing keywords from "" to "r-project, R".
