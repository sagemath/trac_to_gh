# Issue 9765: Cliquer - Update Upstream contact

Issue created by migration from https://trac.sagemath.org/ticket/9766

Original creator: ncohen

Original creation time: 2010-08-19 07:46:25

Assignee: tbd

The URL was missing from the SPKG.txt file, and CJ Fearnley requested it to be changed to work on a debian package of Sage.

The package is located on ~ncohen/cliquer-1.2.p6.spkg 

or at 

http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.p6.spkg

Nathann


---

Comment by ncohen created at 2010-08-19 07:46:37

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-08-19 12:10:18

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-08-19 12:10:18

SPKG.txt does not list the change you made - instead it lists


```
## Changelog

### cliquer-1.2.p6 (19 August 2010)
 * Fixed Trac #8279 to make the cliquer spkg work on Cygwin with the Sage library.

### cliquer-1.2.p5 Mike Hansen (15 February 2010)
 * Fixed Trac #8279 to make the cliquer spkg work on Cygwin with the Sage library.
```


It seems you have just copied the previous entry and incremented the patch level. 

You need to put your own name and date, along with the change you made - but I think you know that. 

Also the commit message does not have the trac number in it. 

You should take the opportunity to add the sections from SPKG.txt which are missing - namely:


```
## Dependencies

List the dependencies here

## Special Update/Build Instructions

List patches that need to be applied and what they do

```


See 
http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg

It wont take you long to find out the dependcies, and if there are no special build instructions, just put 


```
## Special Update/Build Instructions
 * None
```


Dave


---

Comment by ncohen created at 2010-08-19 14:41:10

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-08-19 14:41:10

Stupid copy/paste mistake... I was even doubting adding a line to the changelog in this case was necessary `^^;`

Sorryyyyy ! (SPKG updated)

Nathann


---

Comment by drkirkby created at 2010-08-19 15:16:57

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-08-19 15:16:57

That looks a bit better, but I would suggest a few changes. 

 * Add the trac number (#9766) on the cliquer-1.2.p6 entry. 
 * State the URL was added to SPKG.txt - at the moment we have no idea where it was added. 
 * State you added the `Special Update/Build Instructions` and `Dependencies` to SPKG.txt which were previously missing. 
 * I think it should be URL, not url, though that's a minor point. 

I noticed there was no spkg-check file to run the self-tests, which the package does have. That needs addressing, but on another ticket, as it's quite separate.  I created a ticket for that (#9767) and will address that at some point myself, if nobody beats me to it. 

As such, it might be wise to put a note of this fact - one suggestion is below. 


```
## Special Update/Build Instructions
 * TODO - Add an spkg-check file - see #9767
```


Once that is done, I expect to be able to give it a positive review. 

Dave


---

Comment by drkirkby created at 2010-08-27 03:32:38

Nathann, 
did you manage to finish this? The amount you need to do to get a positive review is trivial. 

Dave


---

Comment by ncohen created at 2010-08-27 06:22:26

> Nathann, 
> did you manage to finish this? The amount you need to do to get a positive review is trivial. 

I have not had a "stable" internet connection for several weeks now (travelling -- I access internet through coffes, and when I am lucky in the hotels I stay in if they have a connection), and I will not be able to update this spkg until at least one week and a half. Sorry for that.

On the technical side David, we have known for a long time that we view development very differently. I try not to forget that you want Sage to be a "professionnal" software, with all the necessary -- what I call -- administration (standard procedures for modification of the code, correct documentation, supporting many platforms, changelogs, etc...). Even though it very often seems "too much" for my way of doing, I have two things to admit :

    * You think Sage will be improved through all this, and your intent is good
    * It requires a lot of work, which you often do yourself

In the end, even though I have a different way to work, it sounds like we are both trying to work on the same piece of (great) software, as efficiently as we can. This is why I am asking this question to a fellow developper : 

There are necessary things in all this administration, to ensure that everything stays correct (doctests, spkg-checks, ...), or documented, or logged. But don't you think somethings goes really wrong when it takes 2 weeks, 2 persons, and 30 minutes or 1 hour of cumulated worktime to add an url to a file ?

How do you think we could simplify these things ? I am confident any mean you could name would never harm Sage's reliability.

I promise you will have this spkg updated with the modifications you requested as soon as I have a -- real -- internet connection. I may even be able to find a way to send it tomorrow ! :-)

Nathann


---

Comment by ncohen created at 2010-08-28 07:42:55

Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`

Nathann


---

Comment by ncohen created at 2010-08-28 07:42:55

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-08-28 10:10:26

Replying to [comment:6 ncohen]:
> > Nathann, 
> > did you manage to finish this? The amount you need to do to get a positive review is trivial. 
> 
> I have not had a "stable" internet connection for several weeks now

Sorry to hear that. I often lose mine from home, and it really annoying. Particularly if I have a chess game scheduled as part of a team. Failure to play lets the whole team down, so I have on several occasions made a 90 mile round-trip to go to my fathers, use his internet, then come home. There's not even a local internet cafe here. 

> On the technical side David, we have known for a long time that we view development very differently. 

Yes. 

> I try not to forget that you want Sage to be a "professionnal" software, with all the necessary -- what I call -- administration (standard procedures for modification of the code, correct documentation, supporting many platforms, changelogs, etc...). Even though it very often seems "too much" for my way of doing, I have two things to admit :

I think if Sage is ever going to be a viable alternative to the commercial products, it needs to get more professional in its approach. As Tim Daily points out in that recent thread on sage-devel, if things are not documented properly, then whole sections of code may need to be swapped out as they are unmaintainable. This is very close to the case with SYMPOW. 

>     * You think Sage will be improved through all this, and your intent is good
>     * It requires a lot of work, which you often do yourself
> 
> In the end, even though I have a different way to work, it sounds like we are both trying to work on the same piece of (great) software, as efficiently as we can. This is why I am asking this question to a fellow developper : 
> 
> There are necessary things in all this administration, to ensure that everything stays correct (doctests, spkg-checks, ...), or documented, or logged. But don't you think somethings goes really wrong when it takes 2 weeks, 2 persons, and 30 minutes or 1 hour of cumulated worktime to add an url to a file ?

Yes, I do. It is a waste of peoples time. 
 
> How do you think we could simplify these things ? I am confident any mean you could name would never harm Sage's reliability.

 * Sage has a Developers Guide. It's not that large, and I feel that anyone developing for Sage should look at the sections which are relevant to their work. Minh in particular has put a lot of effort into improving Sage's documentation. Let's hope hope his, and others efforts to improve documentation are not wasted, because people can't be bothered to read them. I think you would have to agree it's a waste of time creating documentation if it's not read. 
 * Had the original author set up SPKG.txt properly, as documented in the section on [creating a new spkg](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg), CJ Fearnley would not have needed to request the information for Debian. So first and foremost, whoever wrote the SPKG.txt file in the first place, failed to follow the documentation, and so has caused 
  * CJ Fearnley to write you an email
  * You to create a ticket
  * Me to review it. 
  * The release manager to merge the package 
  * You to write to CJ Fearnley to advise him the package is now corrected. 
 * Next, had the reviewer for the cliquer package done their job properly, they would have spotted the authors omissions, 
 * Finally, had you have taken a bit more care, and updated your SPKG.txt to actually reference the ticket, and not copy/past the previous entry, I would probably have given it a positive review immediately, though probably put a note like "it could be useful if you added the missing sections", and leave it up to your judgment whether you did that. Most developers will make minor changes like that. But your entry was confusing, so it needed to be changed. 
 * Once your entry needed to be changed, it did not seem unreasonable that you add the missing sections at the same time. 

> I promise you will have this spkg updated with the modifications you requested as soon as I have a -- real -- internet connection. I may even be able to find a way to send it tomorrow ! :-)
> 
> Nathann

I believe I have spoke to you about the _cost of fixing bugs_. Basically, the earlier a bug is caught, the less expensive it it to fix. In the case of Sage, we are primarily talking about peoples time. Had the documentation error been picked up early, a lot less of peoples time would have been wasted. 

That's why I've tried to get over to you the point that you should spend you time stopping the bugs in the first place, as it's less time consuming to do that, than it is to fix bugs when they are reported. 

Dave


---

Comment by drkirkby created at 2010-08-28 10:24:38

Replying to [comment:7 ncohen]:
> Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`
> 
> Nathann

Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review. 

As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.

Dave


---

Comment by drkirkby created at 2010-08-28 10:24:38

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-08-28 13:04:49

> Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review.

Thanks ! But why do you want a patch to be independently uploaded when it is contained in the spkg file ? 

> As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.

Yes. The reason is that I ignored a new version had been released, and that no one beside me was expected to pay attention to this. It's past time I sent an email to the original developpers though, they may not even know their software is used in Sage. I will also ask them to drop me a line when they update their code if they happen to think of it :-)

Nathann


---

Comment by drkirkby created at 2010-08-28 17:00:16

Replying to [comment:10 ncohen]:
> > Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review.
> 
> Thanks ! But why do you want a patch to be independently uploaded when it is contained in the spkg file ? 

It is how ever other .spkg gets updated. The patch is kept on the trac server. It makes it much easier for a review to see what he is reviewing, and for anyone else to look back and see the changes which were made on the ticket. 

> > As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.
> 
> Yes. The reason is that I ignored a new version had been released, and that no one beside me was expected to pay attention to this. It's past time I sent an email to the original developpers though, they may not even know their software is used in Sage. I will also ask them to drop me a line when they update their code if they happen to think of it :-)
> 
> Nathann

I'll update the package then. There needs to be a Solaris specific change too, as the libraries are not being created optimally on Solaris. 

Dave


---

Attachment

Mercurial patch to add contact information and generally clean up SPKG.txt


---

Comment by mpatel created at 2010-08-30 21:47:13

Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  If we do, should we add a note that SCons is not a Cliquer dependency _in Sage_?


---

Comment by drkirkby created at 2010-08-30 23:21:01

Replying to [comment:13 mpatel]:
> Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  

No, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. 

> If we do, should we add a note that SCons is not a Cliquer dependency _in Sage_?

I don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note?


---

Comment by drkirkby created at 2010-08-30 23:21:11

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-30 23:29:14

Perhaps under "Special Update/Build Instructions" or in the relevant "Changelog" note?


---

Comment by drkirkby created at 2010-08-30 23:31:12

Changing status from needs_work to positive_review.


---

Comment by drkirkby created at 2010-08-30 23:31:12

I've put a package which removes the SCons from SPKG.txt. I also thought it wise to set the dependency to "None", since that's what used on every other package I've seen, though strictly "Base" is more accurate, I think it's also more confusing. 

http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg

I'm considering this a reviewer patch, so are just going to mark it positive again. 

Dave


---

Comment by drkirkby created at 2010-08-30 23:38:54

Replying to [comment:16 mpatel]:
> Perhaps under "Special Update/Build Instructions" or in the relevant "Changelog" note?

I'm not sure how best to do this. It would seem sensible that it was documented under the particular version where the dependency was removed, but I don't know how to find that out. 

I wonder if this package ever had such a dependancy? The upstream source code does not. Nathann created the package, and I don't think he knows anything about SCons, so I doubt he would have used it. You know mercurial better than me - perhaps you can see if there's a record of SCons being removed. 

Dave


---

Comment by drkirkby created at 2010-08-30 23:39:45

Changing status from positive_review to needs_info.


---

Comment by drkirkby created at 2010-08-30 23:42:50

It looks like there was a SConstript file at one point in time:


```
drkirkby@hawk:/tmp/cliquer-1.2.p6/.hg$ ggrep -r SCons *
store/fncache:data/SConstruct.i
```


Now how do I find it when it was removed? 

Dave


---

Attachment

Improve the historical accuracy of SPKG.txt


---

Comment by drkirkby created at 2010-08-31 00:23:13

I found out that the call to 'scons' was removed in change set 4 by Minh. I've added that information to that entry. 

I've marked it as needing review again - perhaps you can look over it Mitesh. 

Dave


---

Comment by drkirkby created at 2010-08-31 00:23:13

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-08-31 00:26:32

The package with the changes can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg

Dave


---

Comment by drkirkby created at 2010-08-31 00:26:32

Changing assignee from tbd to drkirkby.


---

Comment by mpatel created at 2010-08-31 00:29:56

Positive review, except for a stray file with the name "`,`" (a comma):

```sh
cliquer-1.2.p6$ hg stat
? ,
```

Could you remove the file?


---

Comment by drkirkby created at 2010-08-31 00:36:32

Replying to [comment:23 mpatel]:
> Positive review, except for a stray file with the name "`,`" (a comma):
> {{{
> #!sh
> cliquer-1.2.p6$ hg stat
> ? ,
> }}}
> Could you remove the file?
Sure. I don't know how that got there. It has a date in 2032 too - only 22 years ahead in time. 


```
drkirkby@hawk:/tmp/cliquer-1.2.p6$ ls -l ,
-rw-r--r--   1 drkirkby staff       2032 Aug 31 01:15 ,
```


I've uploaded the new .spkg, without the file with a comma in its name. 

Dave


---

Comment by drkirkby created at 2010-08-31 00:38:36

I see the 2032 was the size of the file, not the date! 

I must have created it myself somehow. 

Anyway, it has gone now.


---

Comment by mpatel created at 2010-08-31 00:42:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-31 00:42:31

Thanks!


---

Comment by mpatel created at 2010-08-31 03:20:40

Resolution: fixed


---

Comment by leif created at 2010-09-04 04:11:12

Replying to [comment:14 drkirkby]:
> Replying to [comment:13 mpatel]:
> > Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  
> 
> No, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. 
> 
> > If we do, should we add a note that SCons is not a Cliquer dependency _in Sage_?
> 
> I don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note? 

I think it's worth adding a note (in parentheses) to the _Dependencies_ section that some package['s ordinary build] does _not_ depend on `xy` especially if (e.g) the upstream contains source files for / files (usually) to be processed by `xy`, or in cases where the package _previously_ depended on some package(s), but no longer does. (And even if there erroneously was some dependency listed in `spkg/standard/deps`.)

Typical candidates for `xy` are Python, Perl, lex/flex, yacc/bison etc. (Autotools should not be listed.)

Also, some packages only do _not_ depend on some others (e.g. libraries) _in Sage_ just because of the way we configure, patch or build / install them. IMHO as well worth a note.
