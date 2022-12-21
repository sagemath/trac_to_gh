# Issue 7279: issue with %sh in sagenb (notebook)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-24 00:46:02

Assignee: boothby


```
When I do this in a cell on demo.sagenb.org:

%sh
ls


I get an error:

cd: 1: can't cd to
/home/sage/sagenb/sage_notebook-demo.sagenb/home/jason3/7/cells/4
data
_sage_input_5.py
/tmp/tmp4oPNHC

Thanks,

Jason
```


Jason doesn't want to see that error.  It is there because of enhanced security on the public notebook.




---

Comment by was created at 2009-10-24 00:46:44

Changing status from new to needs_review.


---

Comment by jason created at 2009-12-08 20:42:43

Do you mind elaborating on what the "enhanced security" is and why we are not making that more common for other public or campus Sage servers?  Now I'm concerned that my campus server has a security problem.


---

Comment by was created at 2009-12-09 14:22:53

> Do you mind elaborating on what the "enhanced security" is

If you use server_pool, the worksheet process now run in a way that is much, much safer than it was before.  In particular, they don't have read or write access to anything outside /tmp (except to the DATA dir temporarily in their worksheet), whereas the old worksheet processes could pretty much delete or change all the worksheet data for any worksheet.   

> more common for other public or campus Sage servers? Now 
> I'm concerned that my campus server has a security problem. 

This enhanced security is totally automatic for anybody that uses the server_pool option.


---

Comment by jason created at 2009-12-09 16:14:42

So:

1. Usually a shell script changes directory to the worksheet directory and executes its commands there.

2. It can't do that if server_pool option is used.

It seems that instead of masking the error, we should use sh.chdir so that the script does not try to change directory to the worksheet directory.  It makes me uncomfortable to just mask the error, when the real problem is that sh tries to change directory when it should just stay inside of the temporary directory.


---

Comment by was created at 2009-12-09 19:43:08

Jason, I simply do not understand what you're proposing.  Can you clarify?
What do you mean by "should use sh.chdir"?  

Do you want me to change the %sh mode so it specifically changes to the /tmp/foo-* directory instead of the worksheet directory?   That seems like a good idea, though it
will mean that %sh behaves differently than it used to when server_pool isn't set.


---

Comment by was created at 2009-12-09 19:43:08

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-12-09 21:40:33

Is a temporary directory created when server_pool is not used?

If yes, then right now there is a terrible inconsistency, in that we are in that temporary directory when server_pool is used (because chdir errors out), but we are not in that directory when server_pool is not used (because chdir succeeds).  What I'm saying is that this inconsistency between server_pool=True and server_pool=False is really bad.

Note that the default for sh._curdir is '.'.  Would it be best to just change the current working directory to the temporary directory before executing anything?  I'm surprised that '.' refers to the worksheet directory, rather than the temporary directory.  If we can change the current directory to the temporary directory before calling any scripts (including shell scripts), then I think the problem would be solved, as sh would just chdir to the temporary directory then.


---

Comment by was created at 2009-12-10 07:03:30

Jason -- The answer to your question is "yes".  Also, now that you explain it, I think your suggested solution makes perfect sense, and I'll implement it.  

Thanks!


---

Comment by was created at 2009-12-11 00:04:03

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-11 00:04:03

Jason, I replaced everything by 3 very simple lines that get the job done better. E.g., now you can do 


```
sleep 1
echo "hi"
sleep 1
echo "there"
...
```


and you see the output as it appears, etc.   And the code is vastly simpler too.


---

Comment by jason created at 2009-12-11 00:09:11

Great.

However, one last thing: the docs mention the temporary directory for worksheet processes.  However, it is perfectly okay to execute this from the command line, in which case the docs are then false.

I'd just delete the mention of the temporary directory.  Besides, what if we switch the way we do things again in the notebook?  We'll then have to hunt this statement down and change it.


---

Comment by jason created at 2009-12-11 00:10:27

Or maybe just combine the last two paragraphs so that it is obvious that the directory is only the temporary directory when executing from the worksheet.


---

Comment by jason created at 2009-12-11 00:14:56

Hmm...now you're also changing the behavior quite a bit.  No longer does the eval command return the results as a string.  Instead, it is out of our control.

I suppose one could just use os.system or subprocess by themselves to get the string.  So it doesn't bother me that there is a change.


---

Comment by was created at 2009-12-11 13:26:08

Replying to [comment:11 jason]:
> Hmm...now you're also changing the behavior quite a bit.  No longer does the eval command return the results as a string.  Instead, it is out of our control.
> 
> I suppose one could just use os.system or subprocess by themselves to get the string.  So it doesn't bother me that there is a change.

Yep.  Plus the advantage of being able to watch the output as it appears is *huge*, IMHO.


---

Attachment


---

Comment by was created at 2009-12-11 13:29:21

apply both to the core sage library


---

Attachment

Replying to [comment:10 jason]:
> Or maybe just combine the last two paragraphs so that it is obvious that the directory is only the temporary directory when executing from the worksheet.

I've done this.


---

Comment by mhansen created at 2009-12-27 16:00:37

Looks good.


---

Comment by mhansen created at 2009-12-27 16:00:37

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 02:00:26

Resolution: fixed
