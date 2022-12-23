# Issue 9951: make SAGE_CHECK work with SAGE_ATLAS_LIB

Issue created by migration from https://trac.sagemath.org/ticket/9952

Original creator: jhpalmieri

Original creation time: 2010-09-20 01:43:46

Assignee: tbd

CC:  drkirkby

If SAGE_CHECK is set, then the spkg-check file in the ATLAS spkg tries to run the test suite.  But if SAGE_ATLAS_LIB is also set, then there is nothing to test, so SAGE_CHECK fails.  The new spkg (based on the one from #9780) fixes this by skipping the test suite if SAGE_CHECK is set.

Note that if SAGE_ATLAS_LIB is set badly, then spkg-install fails before spkg-check is ever run, so in spkg-check we just need to see whether SAGE_ATLAS_LIB is not empty.

Get the new spkg here:

[http://sage.math.washington.edu/home/palmieri/SPKG/atlas-3.8.3.p16.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/atlas-3.8.3.p16.spkg)



---

Comment by leif created at 2010-09-20 02:56:06

I think the `$` in the message should be escaped... ;-)


---

Comment by leif created at 2010-09-20 02:56:06

Changing status from new to needs_work.


---

Comment by jhpalmieri created at 2010-09-20 03:54:41

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-09-20 03:54:41

Oops, you're right.  I've fixed it now.  

By the way, I didn't know whether to use

```sh
if [ "x$SAGE_ATLAS_LIB" != "x" ]; then
```

or

```sh
if [ -n "$SAGE_ATLAS_LIB" ]; then
```

or whether it mattered.  Right now I'm using the first of these.


---

Comment by leif created at 2010-09-20 04:07:34

Hmmm, the latter is much nicer (and works with all shells / `test` programs).

Some dead old are only broken in comparing empty strings with `=` or `!=`; `-z` and `-n` always work (otherwise wouldn't make sense at all).


---

Comment by leif created at 2010-09-20 04:12:25

(... as long as you put the variable to test into quotes.)


---

Comment by jhpalmieri created at 2010-09-20 04:54:08

Okay, I switched it to the second one.


---

Comment by drkirkby created at 2010-09-20 06:00:02

I agree with Leif, the $ in the message should be skipped. We have refereed to SAGE_ATLAS_LIB before, so I think it's best to refer to it as that and not $SAGE_ATLAS_LIB. But it works fine. 


```
real	0m0.147s
user	0m0.060s
sys	0m0.085s
Successfully installed atlas-3.8.3.p16
Running the test suite.
$SAGE_ATLAS_LIB is set; skipping test suite.
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p16.spkg
drkirkby@hawk:~/sage-4.6.alpha1$ 
```


Arguably a nice touch would be to add 


```
echo "SAGE_ATLAS_LIB is set to $SAGE_ATLAS_LIB; skipping test suite."
```


BTW, one more stupid thing, which is nothing to do with you, but a result of a bad bit of code being copied around everywhere, is there's no need for the semi-colon on the line


```
echo "SAGE_LOCAL undefined ... exiting";
```


You might as well remove that at the same time. 

Dave


---

Comment by drkirkby created at 2010-09-20 06:26:02

Replying to [comment:3 leif]:
> Hmmm, the latter is much nicer (and works with all shells / `test` programs).
> 
> Some dead old are only broken in comparing empty strings with `=` or `!=`; `-z` and `-n` always work (otherwise wouldn't make sense at all).

Actually, I'd have to disagree with that. I've been using -z and -n, as I agree it looks cleaner, but this is a quote from the autoconf mailing list: 

http://lists.gnu.org/archive/html/autoconf/2010-09/msg00030.html

says 


_this is yet another case of `@`var{string} that looks like an operator, and yet another reason that you should ALWAYS use test x"$val" = x rather than test -z "$val" if you don't know what $val contains._

The autoconf developers have a *huge* experience in writing code as portable as possible, so I'm going to switch to the the more portable `"x$var" = x`. IMHO, for questions of portability, the autoconf mailing list is the best place to ask. 

You can argue rightly argue it does not matter with bash, which this shell is, but it does matter with some shells. So I would *personally* choose to use the most portable way, so things I write do not rely on bash, but would work with just about any shell. But it's a matter of style. Let John choose what he wants. I believe in order of decreasing portability, they are:

 * ` if [ "x$var" = x ] ; then` 
 * ` if [ -z "$var" ] ; then` 
 * ` if [ "$var" = "" ] ; then` 

But all work with modern bash shells. But my *personal* preference is for the first of these, since it would appear to be the most portable. 

Dave


---

Comment by drkirkby created at 2010-09-20 06:39:42

Replying to [comment:1 leif]:
> I think the `$` in the message should be escaped... ;-)
> 
> 

I realise I was *not* agreeing with Leif - how unusual! 

IMHO, the $ should not be there. Leif was saying it should be escaped, I think it should not be there at all, since throughout we have called the variable `SAGE_ATLAS_LIB`, now to switch it to `$SAGE_ATLAS_LIB` seems wrong to me. 

Dave


---

Comment by leif created at 2010-09-20 12:20:00

I'd say there's a slight difference between `test -z ...` and `[ -z ... ]`, but I can't confirm that for the example given because my `ksh` isn't broken like the mentioned Solaris one.

I won't consider this a real _portability_ issue (at least in our case), but a matter of _robustness_. Furthermore, at that point we can rely on `SAGE_ATLAS_LIB` being unset or empty, or containing a valid filename IIRC.

W.r.t `$`, of course `$SAGE_ATLAS_LIB` refers to _the value_ of the environment variable `SAGE_ATLAS_LIB`, but the former might be clearer to some users in case one omits _"The environment variable ..."_.

I think Dave's

```sh
    echo "SAGE_ATLAS_LIB is set to $SAGE_ATLAS_LIB; skipping test suite."
```

is also more explicit, though I'd add (escaped) double quotes around the variable's value.


---

Attachment

for reference only: the diff between the old spkg and the new one


---

Comment by jhpalmieri created at 2010-09-20 15:11:56

This is an amusingly large amount of discussion for a ticket which will deals with an extremely unusual case.  Anyway, I've changed it now.  It seems to work for me on sage.math and on t2.  Note that setting SAGE_ATLAS_LIB to an empty string causes the build to fail earlier, so we really only need to check whether SAGE_ATLAS_LIB is set.  Nonetheless, I'm using 

```sh
if [ "x$SAGE_ATLAS_LIB" != "x" ]; then
```



---

Comment by leif created at 2010-09-20 15:42:19

Replying to [comment:10 jhpalmieri]:
> This is an amusingly large amount of discussion [...]

Yes.

> Nonetheless, I'm using 

```sh
if [ "x$SAGE_ATLAS_LIB" != "x" ]; then
```


Though quite weird in the presence of

```sh
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting"
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```


The "style" of autotools is IMHO targeted at (or demanded by) other purposes. We wouldn't discuss the C "coding style" of e.g. Cython either... ;-)

Readability and maintainability also count.


---

Comment by leif created at 2010-09-20 15:42:19

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-20 15:51:39

P.S.: If the (unescaped) `$` hadn't been there in the first place, the first "comment" (by me) would have been "positive review". :)


---

Comment by jhpalmieri created at 2010-09-20 16:04:37

Oh, so it's my fault, is it?  ;)


---

Comment by leif created at 2010-09-20 16:08:37

Yeah, never raise such issues when *both* Dave and me are involved! (We have our separate tickets for endless discussions.)


---

Comment by drkirkby created at 2010-09-20 16:44:23

Replying to [comment:10 jhpalmieri]:
> This is an amusingly large amount of discussion for a ticket which will deals with an extremely unusual case. 

Yes, it is rather a case of the bike shed problem. 

http://en.wikipedia.org/wiki/Parkinson%27s_Law_of_Triviality

This is the reason I was not willing to write anything for the Sage Developer's Guide about writing shell scripts - note there was a discussion about this matter on sage-devel. Lot's of people have their own ideas, and coming to any sort of agreement is difficult. 

Dave


---

Comment by mpatel created at 2010-09-29 08:40:29

Resolution: fixed
