# Issue 8195: Problems with the 'download' page on the Sage web site.

Issue created by migration from https://trac.sagemath.org/ticket/8195

Original creator: drkirkby

Original creation time: 2010-02-05 18:24:51

Assignee: schilly

CC:  mvngu

I believe there are several problems on the downloads page: http://www.sagemath.org/download.html

This is particularity important now, as I want to put an announcement on compu.unix.solaris about Sage on Solaris, but there is no point until the web pages are more accurate. 

## Download and Media
 * It says the current release is 4.3.1, yet there is no mention of the fact that for Solaris, the latest is 4.3.0.1. I think this is pretty important to have prominently, so a Solaris user does not download 4.3.1, which will not work for them. I would suggest adding "Unfortunately, 4.3.1 will not build on any version of Solaris. We are working on fixing these issues. However, version 4.3.0.1 successfully builds on Solaris 10 (SPARC)"
 * Further down (too far down IMHO), it says "Sage 4.3.0.1 is the latest version that successfully builds on the Sun T5240. See the Sage wiki for build instructions" This has three issues
  * Solaris builds on many systems, not just the T5240. In fact, I rarely build it on that, as it is so slow. 
  * A lot of Solaris users wont even know what a T5240 is. It is probably the worst possible sort of machine for scientific users. 
  * The Wiki page it points to is *very* specific for 't2'. Those instructions will be of no use to anyone with any other Solaris machine, not even a T5240 unless it is 't2'.  I believe there should be a link to the build instructions for Solaris, which are at http://wiki.sagemath.org/solaris *plus* a note for users with access to t2.math.washington.edu, that there are very simpled instructions at http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2 specifically for 't2'. The point is, the instructions at http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2 are very specific to how 't2' has been configured. They would not apply to anyone elses T5240, nor any other Solaris machine. For other Solaris users, the only Solaris page of interest is http://wiki.sagemath.org/solaris

## DVD
The link to Lulu to get a live CD reports a message that the CD is not available. As such, it should be removed until such time as the DVD becomes available, which does not look to be any time soon. It has been broken for months.


---

Comment by schilly created at 2010-02-05 18:39:04

the version numbers are inserted dynamically. i'm adding a new variable for solaris, currently set to 4.3.0.1. I'm against adding the sentence "unfortunately ... " .. because that will change in the future ;)

> Further down (too far down IMHO)

it's the first entry after the download information, where should it be then? when such a text was above the links i got complaints that one has to scroll down to download.

i suggest that someone writes a nice and *short* text for the download.html page and the download-solaris.html page. just quote it here on the ticket. it should not go into any specifics because they might change. that's better off in the wiki pages.

dvd: it was already removed on all individual download pages (download-*.html) but i have overlooked that the main download page doesn't have this part as a template. it's gone there too.

the part below the usage information is a template for all pages. i can remove it.

the last point where solaris specific text is, is above the download links on the mirror pages. it's just pointing to the two wiki pages, better ideas welcome ;)


---

Comment by drkirkby created at 2010-02-05 23:30:43

Hi Harald. 

Thanks for the quick reply. I'd really like to get some Solaris users trying Sage - hence my desire that the information is as up to date as possible. Here are some specific issues, and some suggestions. 

In the light of what you said, about not being too specific about things that might change, I created a page giving information about installing the Solaris binaries. 

http://wiki.sagemath.org/solaris-binaries

So now there are 3 wiki pages about Solaris. I need to expand the first one, but it is there for a start, so you can link to it. 

 * http://wiki.sagemath.org/solaris-binaries - how to install the binaries downloaded from the Sage web site. 
 * http://wiki.sagemath.org/solaris - detailed information about building Sage from source on Solaris
 * http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2 - Building Sage on 't2'. This is only for those with accounts on 't2', and it totally irrelevant to 99% of users. 

I've broken the issues down into those on specific pages. 

## http://www.sagemath.org/download-source.html
http://www.sagemath.org/download-source.html 
says "The newest source-code release is 4.3.1.
Please select a mirror closest to you to reduce server traffic. The current release is 4.3.1. "

Could you change that to: 

*The newest source-code release is 4.3.1, but unfortunately that does not build on Solaris. The latest version of Sage to build on Solaris is 4.3.0.1. Please select the nearest mirror ...*

The second sentence in the _Information section_ says

"You can get the complete source for Sage to compile it on your own Linux or Mac OS X system."
There is no mention of Solaris. Could you please add Solaris along with the Linux and OS X. 

## http://www.sagemath.org/download.html
Despite the name, this page is almost exclusively be about *binary* distributions. Perhaps it would be better to rename it to _Download Sage Binaries and Media_. 

For the Solaris entry, I would suggest you write the following, which should not change too often. 

-------------------------------------
*Solaris*
Download 4.3.0.1 for Solaris 10 (SPARC)

Sage 4.3.0.1 is the latest version that successfully builds on Solaris 10. The binary distribution was built a Sun running Solaris 10 03/05, so should run on any Solaris 10 release. See the Sage Wiki 

http://wiki.sagemath.org/solaris-binaries

for information about how to install the Sage binary distribution for SPARC based systems running Solaris 10. 

## http://www.sagemath.org/download-solaris.html
The main issues with this page currently are

 * The first sentence says "Sage 4.3.0.1 is the latest version that builds on SPARC Solaris 10, specifically on the Sun T5240". However, there is nothing specific about that binary for a T5240. It was not even built on a T5240. It was built on an old Sun Netra T1 running the first release of Solaris 10. Building it on 't2' would have been unwise, as it could not be guaranteed to run on earlier releases of Solaris 10. (There are in fact 9 releases of Solaris 10. The first was in 03/2005, and since then there have been 8 updates). 
 * The Wiki page it points to, http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2 is just about building Sage on 't2. Those instructions are very specific to 't2', and will not work elsewhere. 
 * The page contains information on a "Sage Live CD", yet that is nothing to do with Solaris. Since there are Solaris live CD's, this could be confusing. 
 * The _Usage_ section is incorrect, as it uses the 'tar' command with some GNU specific options, which will not work on Solaris. 

At your suggestion, I think the following would be suitable. 
---
Sage 4.3.0.1 is the latest version that builds on Solaris 10 (SPARC). See the Sage wiki 

http://wiki.sagemath.org/solaris-binaries

for detailed and up to date instructions on installing the Solaris binaries. 


### Usage
The Solaris binaries are compressed and are available in two forms. If your SPARC system has the 'p7zip' command, which is standard on recent Solaris 10 releases, then it is recommended you download sage-...tar.7z as it is considerably smaller than the gzip compressed file. Otherwise you can download the .gz file, build pk7zip yourself, or install Sun patch 137477.

$ p7zip -d sage-....tar.7z (if you used the recommended .7z file)
$ gzip -d sage-....tar.gz (if you downloaded the larger .gz file)
Sun's version of tar will not extract the binaries, so use the GNU tar. 
$ /usr/sfw/bin/gtar xf sage-..tar
$ LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/sfw/lib
$ export LD_LIBRARY_PATH

Change to the directory where the files were extract, then run 

$ ./sage 

More detailed instructions can be found on the Sage Wiki at 
http://wiki.sagemath.org/solaris-binaries

*Sage Live CD *
Delete it, as it is nothing to do with Solaris. 

*Source*
Make sure that points to somewhere where one can get the Solaris 4.3.0.1 source code. Currently it only points to a page saying the latest release is 4.3.1


---

Comment by drkirkby created at 2010-02-05 23:34:30

Oops, I forgot to put braces around the commands. 


```
$ p7zip -d sage-....tar.7z (if you used the recommended .7z file) 
$ gzip -d sage-....tar.gz (if you downloaded the larger .gz file) 
```

Sun's version of tar will not extract the binaries, so use the GNU tar. 

```
$ /usr/sfw/bin/gtar xf sage-..tar 
$ LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/sfw/lib 
$ export LD_LIBRARY_PATH

Change to the directory where the files were extract, then run

$ ./sage


---

Comment by schilly created at 2010-02-06 00:22:30

Ok, I did most of the changes, also found some other tiny issues. One page you didn't say anything about is the mirror page. I copied the "usage" info. see: [http://sage.math.washington.edu/sage/solaris/](http://sage.math.washington.edu/sage/solaris/)

And I understand the confusion, the download is only for binaries, as is the solaris page. So, my suggestion is to move the solaris source (renamed to sage-x.y.z-solaris.tar) to the actual source download page and directory and put a pointer from the solaris binary download page to that general source page. 

This has two reasons: 1. that's how it "works" ;) and 2. we keep a backup of all sources that were ever released and that solaris source belongs into that attic, too. [the motivation behind is, that if someone cites a certain version, at least the source code of his/her algorithms should be available]

The single wiki page is good good .. then you have full control what to put there. (instead of solaris-build, you could also name it solaris-release) ... 

However, check the pages and tell me what is left to do.


---

Comment by drkirkby created at 2010-02-06 11:48:09

Changing assignee from schilly to drkirkby.


---

Comment by drkirkby created at 2010-02-06 11:48:09

Replying to [comment:4 schilly]:
> Ok, I did most of the changes, also found some other tiny issues. 


Thank you Harald, that looks a lot better and is far less confusing.


> One page you didn't say anything about is the mirror page. I copied the "usage" info. see: [http://sage.math.washington.edu/sage/solaris/](http://sage.math.washington.edu/sage/solaris/)
> 
> And I understand the confusion, the download is only for binaries, as is the solaris page. So, my suggestion is to move the solaris source (renamed to sage-x.y.z-solaris.tar) to the actual source download page and directory and put a pointer from the solaris binary download page to that general source page. 


I have some concerns this implies the source for Solaris is somehow different from the other source code. 4.3.0.1 will build on any system - the one fix applied (#6595) to 4.3 to get Sage to build on Solaris will have no impact on any other system. In any case, #6595 was merged in 4.3.1. 

Perhaps a better name might be 

`4.3.0.1-for-Solaris-OSX-and-Linux.tar`

Or perhaps, just copying the 4.3.0.1.tar.gz file there, and creating another empty file called 

`Version_4.3.0.1_will_additionally_build_on_Solaris-10`

Neither solution seems perfect I must admit. Of course, the best solution it to sort out the Solaris issue! I just want to avoid the impression that Solaris is not being taken seriously. 


> This has two reasons: 1. that's how it "works" ;) and 2. we keep a backup of all sources that were ever released and that solaris source belongs into that attic, too. [the motivation behind is, that if someone cites a certain version, at least the source code of his/her algorithms should be available]
 
I can see the logic of this. 


> The single wiki page is good good .. then you have full control what to put there. (instead of solaris-build, you could also name it solaris-release) ... 
> 
> However, check the pages and tell me what is left to do.

OK, here are a few points I noted. 

 * First a general point. The link on the mirrors page "JMU (VA, USA)" gives a 404 error, as it points to a non-existent page http://modular.math.jmu.edu/src/index.html. If the link was changed to http://modular.math.jmu.edu/src/ then it would work. 

 * http://www.sagemath.org/download-source.html says "The newest source-code release is 4.3.1, but unfortunately that does not build on Solaris. The latest version of Sage to build on Solaris is 4.3.0.1."

I know that was my idea, but it would be good if we changed it, so it does not imply Solaris support was dropped, but in contrast we are trying to fix it. I would suggest changing it, by adding the bit I marked in bold below. 

"The newest source-code release is 4.3.1, but unfortunately that does not build on Solaris, *but we are working on resolving this issue*. The latest version of Sage to build on Solaris is 4.3.0.1."

 * http://www.sagemath.org/download.html still says at the top that the latest release is 4.3.1, with no mention of the different release for Solaris. 

 * http://www.sagemath.org/download-solaris.html has a typo, which is my fault. It needs to say "Change to the directory where the files were extract*ed*, then run" (The 'ed' is missing). Also, the font of that sentence is currently fixed-spaced - again my fault. 

 * Could the first sentence of http://www.sagemath.org/download-solaris.html be changed from "Sage 4.3.0.1 is the latest version that builds on SPARC Solaris 10 (SPARC)." 

to 

"Sage 4.3.0.1 is the latest version that builds on SPARC Solaris 10 (SPARC), *although we are working on ensuring the latest version of Sage will always run on Solaris 10. We are also working on a 64-bit port to OpenSolaris on x64*" 

That will reinforce the fact that Solaris development is taking place and not abandoned. 

 * http://www.sagemath.org/download-source.html has some duplication, as it says twice in the top paragraph that the latest release is 4.3.1. I think the sentence "The current release is 4.3.1." is a bit redundant, as this was stated only 3 sentences earlier in the same paragraph. 

 * Could http://www.sagemath.org/download-solaris.html have a section "Try online" where it says 

You can try Sage on a Sun T5240 running Solaris 10 at http://t2nb.math.washington.edu:8000/ This was kindly donated by Sun to the Sage project. 

I realise it is not really about downloading, so you might prefer not to have that, but given it is a Solaris specific page, it might be useful. I know Sun are keen to have a page where they can point their customers at. Clearly this would be a good page, so having a link to the server and an acknowledgement would be good 

PS - in case you were unaware, Sun were bought by Oracle for $7 billion on the 27th January this year. 

Dave


---

Comment by schilly created at 2010-02-06 19:06:15

Replying to [comment:5 drkirkby]:
> I have some concerns this implies the source for Solaris is somehow different from the other source code. 

Well, I think you think a bit too complicated ;) If someone is looking for the solaris source, it would be helpful that there is solaris in the list. Nothing more. Nobody draws so many conclusions from the download page, just wants to get it, nothing more... For now we keep this source file here in solaris, i'll move it into the older sources once a newser solaris cut is available. and that's it in my eyes.


> `4.3.0.1-for-Solaris-OSX-and-Linux.tar`

that's true for all of them.


>  * First a general point. The link on the mirrors page "JMU (VA, USA)" gives a 404 error, as it points to a non-existent page http://modular.math.jmu.edu/src/index.html. If the link was changed to http://modular.math.jmu.edu/src/ then it would work. 

Well, the index.html is indeed missing. The problem is that their syncing seems to delete files that make a problem. Currently, the nfs file system on boxen tells rsync this list of errors:


```
2010/02/06 18:45:54 [22873] rsync: readlink_stat("/src/index.html" (in sage)) failed: Stale NFS file handle (116)
2010/02/06 18:45:54 [22873] rsync: readlink_stat("/src/changelogs/index.html" (in sage)) failed: Stale NFS file handle (116)
2010/02/06 18:45:54 [22873] rsync: readlink_stat("/src/announce/index.html" (in sage)) failed: Stale NFS file handle (116)
...
...
```


So, well, it would work if our servers would work (should be fixed soon). And in case you think it would be ok to omit the index.html -> it's  necessary to include it because not all webservers (especially not the ftp ones) open the pretty download page. and without that we do not have any info on the download statistics :(

Call it "optimistic mirroring", because I just assume that if a mirror has the correct timestamp file it is also complete and online.

> I know that was my idea, but it would be good if we changed it ... 

i know how hard it is to write text on websites, i learned to be patient. Just tell me where to put which strings...

> That will reinforce the fact that Solaris development is taking place and not abandoned. 

+1

>   a section "Try online" where it says 

yes

> PS - in case you were unaware, Sun were bought by Oracle for $7 billion on the 27th January this year. 
> 

I know, and this can end good or bad  for solaris. (Oracle has their focus on linux on smaller systems and i think they will drop open solaris).


---

Comment by drkirkby created at 2010-02-12 01:17:14

Hi Harald.

There is still an issue. Going to 

http://www.sagemath.org/download-solaris.html

Under the section "Source; Download complete source code." the link has a directory with only sage-4.3.2.tar, and no sage-4.3.0.1-solaris.tar, or whatever you want to call it. It would be useful to keep it in the same directory as the latest Sage release. 

The only way to find the source code is to go to http://www.sagemath.org/download.html, click on binaries, then one finds the source and binaries in the one directory. 

All a bit confusing. 

BTW, you might well be right about OpenSolaris and Oracle. From what I gather from someone at Sun, Oracle only really want the SPARC architecture and Solaris operating system. Whether they will keep Open Solaris going is another matter. They might well switch from Linux to Solaris even on smaller systems. It seems pretty clear they will go the Solaris route on larger systems, otherwise there was no point buying Sun. Who knows? 

Dave


---

Comment by jdemeyer created at 2012-05-17 22:13:30

Sage 5.0 "almost works" on Solaris SPARC (it builds but there are a few doctest errors) and it works fully on OpenSolaris i386.  See [SupportedPlatforms](http://wiki.sagemath.org/SupportedPlatforms).  Currently, we don't build (Open)Solaris binaries on the buildbot.  Should this be changed?


---

Comment by mkoeppe created at 2020-07-08 16:38:40

outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:38:40

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2020-07-08 18:00:31

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-14 13:02:28

Resolution: invalid
