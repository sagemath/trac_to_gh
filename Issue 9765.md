# Issue 9765: Cliquer - Update Upstream contact

archive/issues_009765.json:
```json
{
    "body": "Assignee: tbd\n\nThe URL was missing from the SPKG.txt file, and CJ Fearnley requested it to be changed to work on a debian package of Sage.\n\nThe package is located on ~ncohen/cliquer-1.2.p6.spkg \n\nor at \n\nhttp://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.p6.spkg\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9766\n\n",
    "created_at": "2010-08-19T07:46:25Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Cliquer - Update Upstream contact",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9765",
    "user": "ncohen"
}
```
Assignee: tbd

The URL was missing from the SPKG.txt file, and CJ Fearnley requested it to be changed to work on a debian package of Sage.

The package is located on ~ncohen/cliquer-1.2.p6.spkg 

or at 

http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.p6.spkg

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9766





---

archive/issue_comments_095668.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T07:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95668",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095669.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-19T12:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95669",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095670.json:
```json
{
    "body": "SPKG.txt does not list the change you made - instead it lists\n\n\n```\n## Changelog\n\n### cliquer-1.2.p6 (19 August 2010)\n * Fixed Trac #8279 to make the cliquer spkg work on Cygwin with the Sage library.\n\n### cliquer-1.2.p5 Mike Hansen (15 February 2010)\n * Fixed Trac #8279 to make the cliquer spkg work on Cygwin with the Sage library.\n```\n\n\nIt seems you have just copied the previous entry and incremented the patch level. \n\nYou need to put your own name and date, along with the change you made - but I think you know that. \n\nAlso the commit message does not have the trac number in it. \n\nYou should take the opportunity to add the sections from SPKG.txt which are missing - namely:\n\n\n```\n## Dependencies\n\nList the dependencies here\n\n## Special Update/Build Instructions\n\nList patches that need to be applied and what they do\n\n```\n\n\nSee \nhttp://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg\n\nIt wont take you long to find out the dependcies, and if there are no special build instructions, just put \n\n\n```\n## Special Update/Build Instructions\n * None\n```\n\n\nDave",
    "created_at": "2010-08-19T12:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95670",
    "user": "drkirkby"
}
```

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

archive/issue_comments_095671.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-19T14:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95671",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095672.json:
```json
{
    "body": "Stupid copy/paste mistake... I was even doubting adding a line to the changelog in this case was necessary `^^;`\n\nSorryyyyy ! (SPKG updated)\n\nNathann",
    "created_at": "2010-08-19T14:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95672",
    "user": "ncohen"
}
```

Stupid copy/paste mistake... I was even doubting adding a line to the changelog in this case was necessary `^^;`

Sorryyyyy ! (SPKG updated)

Nathann



---

archive/issue_comments_095673.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-19T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95673",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095674.json:
```json
{
    "body": "That looks a bit better, but I would suggest a few changes. \n\n* Add the trac number (#9766) on the cliquer-1.2.p6 entry. \n* State the URL was added to SPKG.txt - at the moment we have no idea where it was added. \n* State you added the `Special Update/Build Instructions` and `Dependencies` to SPKG.txt which were previously missing. \n* I think it should be URL, not url, though that's a minor point. \n\nI noticed there was no spkg-check file to run the self-tests, which the package does have. That needs addressing, but on another ticket, as it's quite separate.  I created a ticket for that (#9767) and will address that at some point myself, if nobody beats me to it. \n\nAs such, it might be wise to put a note of this fact - one suggestion is below. \n\n\n```\n## Special Update/Build Instructions\n * TODO - Add an spkg-check file - see #9767\n```\n\n\nOnce that is done, I expect to be able to give it a positive review. \n\nDave",
    "created_at": "2010-08-19T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95674",
    "user": "drkirkby"
}
```

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

archive/issue_comments_095675.json:
```json
{
    "body": "Nathann, \ndid you manage to finish this? The amount you need to do to get a positive review is trivial. \n\nDave",
    "created_at": "2010-08-27T03:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95675",
    "user": "drkirkby"
}
```

Nathann, 
did you manage to finish this? The amount you need to do to get a positive review is trivial. 

Dave



---

archive/issue_comments_095676.json:
```json
{
    "body": "> Nathann, \n> did you manage to finish this? The amount you need to do to get a positive review is trivial. \n\nI have not had a \"stable\" internet connection for several weeks now (travelling -- I access internet through coffes, and when I am lucky in the hotels I stay in if they have a connection), and I will not be able to update this spkg until at least one week and a half. Sorry for that.\n\nOn the technical side David, we have known for a long time that we view development very differently. I try not to forget that you want Sage to be a \"professionnal\" software, with all the necessary -- what I call -- administration (standard procedures for modification of the code, correct documentation, supporting many platforms, changelogs, etc...). Even though it very often seems \"too much\" for my way of doing, I have two things to admit :\n\n* You think Sage will be improved through all this, and your intent is good\n* It requires a lot of work, which you often do yourself\n\nIn the end, even though I have a different way to work, it sounds like we are both trying to work on the same piece of (great) software, as efficiently as we can. This is why I am asking this question to a fellow developper : \n\nThere are necessary things in all this administration, to ensure that everything stays correct (doctests, spkg-checks, ...), or documented, or logged. But don't you think somethings goes really wrong when it takes 2 weeks, 2 persons, and 30 minutes or 1 hour of cumulated worktime to add an url to a file ?\n\nHow do you think we could simplify these things ? I am confident any mean you could name would never harm Sage's reliability.\n\nI promise you will have this spkg updated with the modifications you requested as soon as I have a -- real -- internet connection. I may even be able to find a way to send it tomorrow ! :-)\n\nNathann",
    "created_at": "2010-08-27T06:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95676",
    "user": "ncohen"
}
```

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

archive/issue_comments_095677.json:
```json
{
    "body": "Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`\n\nNathann",
    "created_at": "2010-08-28T07:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95677",
    "user": "ncohen"
}
```

Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`

Nathann



---

archive/issue_comments_095678.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-28T07:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95678",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095679.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n> > Nathann, \n> > did you manage to finish this? The amount you need to do to get a positive review is trivial. \n> \n> I have not had a \"stable\" internet connection for several weeks now\n\nSorry to hear that. I often lose mine from home, and it really annoying. Particularly if I have a chess game scheduled as part of a team. Failure to play lets the whole team down, so I have on several occasions made a 90 mile round-trip to go to my fathers, use his internet, then come home. There's not even a local internet cafe here. \n\n> On the technical side David, we have known for a long time that we view development very differently. \n\nYes. \n\n> I try not to forget that you want Sage to be a \"professionnal\" software, with all the necessary -- what I call -- administration (standard procedures for modification of the code, correct documentation, supporting many platforms, changelogs, etc...). Even though it very often seems \"too much\" for my way of doing, I have two things to admit :\n\nI think if Sage is ever going to be a viable alternative to the commercial products, it needs to get more professional in its approach. As Tim Daily points out in that recent thread on sage-devel, if things are not documented properly, then whole sections of code may need to be swapped out as they are unmaintainable. This is very close to the case with SYMPOW. \n\n>     * You think Sage will be improved through all this, and your intent is good\n>     * It requires a lot of work, which you often do yourself\n> \n> In the end, even though I have a different way to work, it sounds like we are both trying to work on the same piece of (great) software, as efficiently as we can. This is why I am asking this question to a fellow developper : \n> \n> There are necessary things in all this administration, to ensure that everything stays correct (doctests, spkg-checks, ...), or documented, or logged. But don't you think somethings goes really wrong when it takes 2 weeks, 2 persons, and 30 minutes or 1 hour of cumulated worktime to add an url to a file ?\n\nYes, I do. It is a waste of peoples time. \n \n> How do you think we could simplify these things ? I am confident any mean you could name would never harm Sage's reliability.\n\n* Sage has a Developers Guide. It's not that large, and I feel that anyone developing for Sage should look at the sections which are relevant to their work. Minh in particular has put a lot of effort into improving Sage's documentation. Let's hope hope his, and others efforts to improve documentation are not wasted, because people can't be bothered to read them. I think you would have to agree it's a waste of time creating documentation if it's not read. \n* Had the original author set up SPKG.txt properly, as documented in the section on [creating a new spkg](http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg), CJ Fearnley would not have needed to request the information for Debian. So first and foremost, whoever wrote the SPKG.txt file in the first place, failed to follow the documentation, and so has caused \n  * CJ Fearnley to write you an email\n  * You to create a ticket\n  * Me to review it. \n  * The release manager to merge the package \n  * You to write to CJ Fearnley to advise him the package is now corrected. \n* Next, had the reviewer for the cliquer package done their job properly, they would have spotted the authors omissions, \n* Finally, had you have taken a bit more care, and updated your SPKG.txt to actually reference the ticket, and not copy/past the previous entry, I would probably have given it a positive review immediately, though probably put a note like \"it could be useful if you added the missing sections\", and leave it up to your judgment whether you did that. Most developers will make minor changes like that. But your entry was confusing, so it needed to be changed. \n* Once your entry needed to be changed, it did not seem unreasonable that you add the missing sections at the same time. \n\n> I promise you will have this spkg updated with the modifications you requested as soon as I have a -- real -- internet connection. I may even be able to find a way to send it tomorrow ! :-)\n> \n> Nathann\n\nI believe I have spoke to you about the *cost of fixing bugs*. Basically, the earlier a bug is caught, the less expensive it it to fix. In the case of Sage, we are primarily talking about peoples time. Had the documentation error been picked up early, a lot less of peoples time would have been wasted. \n\nThat's why I've tried to get over to you the point that you should spend you time stopping the bugs in the first place, as it's less time consuming to do that, than it is to fix bugs when they are reported. \n\nDave",
    "created_at": "2010-08-28T10:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95679",
    "user": "drkirkby"
}
```

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

I believe I have spoke to you about the *cost of fixing bugs*. Basically, the earlier a bug is caught, the less expensive it it to fix. In the case of Sage, we are primarily talking about peoples time. Had the documentation error been picked up early, a lot less of peoples time would have been wasted. 

That's why I've tried to get over to you the point that you should spend you time stopping the bugs in the first place, as it's less time consuming to do that, than it is to fix bugs when they are reported. 

Dave



---

archive/issue_comments_095680.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`\n> \n> Nathann\n\nYes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review. \n\nAs a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.\n\nDave",
    "created_at": "2010-08-28T10:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95680",
    "user": "drkirkby"
}
```

Replying to [comment:7 ncohen]:
> Wonderful airport with a free wifi, and no filter on port 80... Packages updated ! I hope you will like this version `:-)`
> 
> Nathann

Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review. 

As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.

Dave



---

archive/issue_comments_095681.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-28T10:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95681",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095682.json:
```json
{
    "body": "> Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review.\n\nThanks ! But why do you want a patch to be independently uploaded when it is contained in the spkg file ? \n\n> As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.\n\nYes. The reason is that I ignored a new version had been released, and that no one beside me was expected to pay attention to this. It's past time I sent an email to the original developpers though, they may not even know their software is used in Sage. I will also ask them to drop me a line when they update their code if they happen to think of it :-)\n\nNathann",
    "created_at": "2010-08-28T13:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95682",
    "user": "ncohen"
}
```

> Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review.

Thanks ! But why do you want a patch to be independently uploaded when it is contained in the spkg file ? 

> As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.

Yes. The reason is that I ignored a new version had been released, and that no one beside me was expected to pay attention to this. It's past time I sent an email to the original developpers though, they may not even know their software is used in Sage. I will also ask them to drop me a line when they update their code if they happen to think of it :-)

Nathann



---

archive/issue_comments_095683.json:
```json
{
    "body": "Replying to [comment:10 ncohen]:\n> > Yes, that looks fine. You should have put the patch on the trac server, but I will do that for you. I'm giving it positive review.\n> \n> Thanks ! But why do you want a patch to be independently uploaded when it is contained in the spkg file ? \n\nIt is how ever other .spkg gets updated. The patch is kept on the trac server. It makes it much easier for a review to see what he is reviewing, and for anyone else to look back and see the changes which were made on the ticket. \n\n> > As a matter of interest, are you aware of any reason the package should not be updated to the latest, which is 1.2.1? If not, I'll update the package version at the same time as adding the test code to #9767.\n> \n> Yes. The reason is that I ignored a new version had been released, and that no one beside me was expected to pay attention to this. It's past time I sent an email to the original developpers though, they may not even know their software is used in Sage. I will also ask them to drop me a line when they update their code if they happen to think of it :-)\n> \n> Nathann\n\nI'll update the package then. There needs to be a Solaris specific change too, as the libraries are not being created optimally on Solaris. \n\nDave",
    "created_at": "2010-08-28T17:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95683",
    "user": "drkirkby"
}
```

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

archive/issue_comments_095684.json:
```json
{
    "body": "Attachment\n\nMercurial patch to add contact information and generally clean up SPKG.txt",
    "created_at": "2010-08-28T17:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95684",
    "user": "drkirkby"
}
```

Attachment

Mercurial patch to add contact information and generally clean up SPKG.txt



---

archive/issue_comments_095685.json:
```json
{
    "body": "Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?",
    "created_at": "2010-08-30T21:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95685",
    "user": "mpatel"
}
```

Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?



---

archive/issue_comments_095686.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  \n\nNo, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. \n\n> If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?\n\nI don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note?",
    "created_at": "2010-08-30T23:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95686",
    "user": "drkirkby"
}
```

Replying to [comment:13 mpatel]:
> Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  

No, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. 

> If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?

I don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note?



---

archive/issue_comments_095687.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-30T23:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95687",
    "user": "drkirkby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095688.json:
```json
{
    "body": "Perhaps under \"Special Update/Build Instructions\" or in the relevant \"Changelog\" note?",
    "created_at": "2010-08-30T23:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95688",
    "user": "mpatel"
}
```

Perhaps under "Special Update/Build Instructions" or in the relevant "Changelog" note?



---

archive/issue_comments_095689.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-08-30T23:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95689",
    "user": "drkirkby"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_095690.json:
```json
{
    "body": "I've put a package which removes the SCons from SPKG.txt. I also thought it wise to set the dependency to \"None\", since that's what used on every other package I've seen, though strictly \"Base\" is more accurate, I think it's also more confusing. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg\n\nI'm considering this a reviewer patch, so are just going to mark it positive again. \n\nDave",
    "created_at": "2010-08-30T23:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95690",
    "user": "drkirkby"
}
```

I've put a package which removes the SCons from SPKG.txt. I also thought it wise to set the dependency to "None", since that's what used on every other package I've seen, though strictly "Base" is more accurate, I think it's also more confusing. 

http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg

I'm considering this a reviewer patch, so are just going to mark it positive again. 

Dave



---

archive/issue_comments_095691.json:
```json
{
    "body": "Replying to [comment:16 mpatel]:\n> Perhaps under \"Special Update/Build Instructions\" or in the relevant \"Changelog\" note?\n\nI'm not sure how best to do this. It would seem sensible that it was documented under the particular version where the dependency was removed, but I don't know how to find that out. \n\nI wonder if this package ever had such a dependancy? The upstream source code does not. Nathann created the package, and I don't think he knows anything about SCons, so I doubt he would have used it. You know mercurial better than me - perhaps you can see if there's a record of SCons being removed. \n\nDave",
    "created_at": "2010-08-30T23:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95691",
    "user": "drkirkby"
}
```

Replying to [comment:16 mpatel]:
> Perhaps under "Special Update/Build Instructions" or in the relevant "Changelog" note?

I'm not sure how best to do this. It would seem sensible that it was documented under the particular version where the dependency was removed, but I don't know how to find that out. 

I wonder if this package ever had such a dependancy? The upstream source code does not. Nathann created the package, and I don't think he knows anything about SCons, so I doubt he would have used it. You know mercurial better than me - perhaps you can see if there's a record of SCons being removed. 

Dave



---

archive/issue_comments_095692.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-08-30T23:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95692",
    "user": "drkirkby"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_095693.json:
```json
{
    "body": "It looks like there was a SConstript file at one point in time:\n\n\n```\ndrkirkby@hawk:/tmp/cliquer-1.2.p6/.hg$ ggrep -r SCons *\nstore/fncache:data/SConstruct.i\n```\n\n\nNow how do I find it when it was removed? \n\nDave",
    "created_at": "2010-08-30T23:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95693",
    "user": "drkirkby"
}
```

It looks like there was a SConstript file at one point in time:


```
drkirkby@hawk:/tmp/cliquer-1.2.p6/.hg$ ggrep -r SCons *
store/fncache:data/SConstruct.i
```


Now how do I find it when it was removed? 

Dave



---

archive/issue_comments_095694.json:
```json
{
    "body": "Attachment\n\nImprove the historical accuracy of SPKG.txt",
    "created_at": "2010-08-31T00:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95694",
    "user": "drkirkby"
}
```

Attachment

Improve the historical accuracy of SPKG.txt



---

archive/issue_comments_095695.json:
```json
{
    "body": "I found out that the call to 'scons' was removed in change set 4 by Minh. I've added that information to that entry. \n\nI've marked it as needing review again - perhaps you can look over it Mitesh. \n\nDave",
    "created_at": "2010-08-31T00:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95695",
    "user": "drkirkby"
}
```

I found out that the call to 'scons' was removed in change set 4 by Minh. I've added that information to that entry. 

I've marked it as needing review again - perhaps you can look over it Mitesh. 

Dave



---

archive/issue_comments_095696.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-31T00:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95696",
    "user": "drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_095697.json:
```json
{
    "body": "The package with the changes can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg\n\nDave",
    "created_at": "2010-08-31T00:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95697",
    "user": "drkirkby"
}
```

The package with the changes can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p6.spkg

Dave



---

archive/issue_comments_095698.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2010-08-31T00:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95698",
    "user": "drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_095699.json:
```json
{
    "body": "Positive review, except for a stray file with the name \"`,`\" (a comma):\n\n```sh\ncliquer-1.2.p6$ hg stat\n? ,\n```\n\nCould you remove the file?",
    "created_at": "2010-08-31T00:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95699",
    "user": "mpatel"
}
```

Positive review, except for a stray file with the name "`,`" (a comma):

```sh
cliquer-1.2.p6$ hg stat
? ,
```

Could you remove the file?



---

archive/issue_comments_095700.json:
```json
{
    "body": "Replying to [comment:23 mpatel]:\n> Positive review, except for a stray file with the name \"`,`\" (a comma):\n> {{{\n> #!sh\n> cliquer-1.2.p6$ hg stat\n> ? ,\n> }}}\n> Could you remove the file?\nSure. I don't know how that got there. It has a date in 2032 too - only 22 years ahead in time. \n\n\n```\ndrkirkby@hawk:/tmp/cliquer-1.2.p6$ ls -l ,\n-rw-r--r--   1 drkirkby staff       2032 Aug 31 01:15 ,\n```\n\n\nI've uploaded the new .spkg, without the file with a comma in its name. \n\nDave",
    "created_at": "2010-08-31T00:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95700",
    "user": "drkirkby"
}
```

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

archive/issue_comments_095701.json:
```json
{
    "body": "I see the 2032 was the size of the file, not the date! \n\nI must have created it myself somehow. \n\nAnyway, it has gone now.",
    "created_at": "2010-08-31T00:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95701",
    "user": "drkirkby"
}
```

I see the 2032 was the size of the file, not the date! 

I must have created it myself somehow. 

Anyway, it has gone now.



---

archive/issue_comments_095702.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-31T00:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95702",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095703.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-08-31T00:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95703",
    "user": "mpatel"
}
```

Thanks!



---

archive/issue_comments_095704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-31T03:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95704",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_095705.json:
```json
{
    "body": "Replying to [comment:14 drkirkby]:\n> Replying to [comment:13 mpatel]:\n> > Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  \n> \n> No, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. \n> \n> > If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?\n> \n> I don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note? \n\nI think it's worth adding a note (in parentheses) to the *Dependencies* section that some package['s ordinary build] does *not* depend on `xy` especially if (e.g) the upstream contains source files for / files (usually) to be processed by `xy`, or in cases where the package *previously* depended on some package(s), but no longer does. (And even if there erroneously was some dependency listed in `spkg/standard/deps`.)\n\nTypical candidates for `xy` are Python, Perl, lex/flex, yacc/bison etc. (Autotools should not be listed.)\n\nAlso, some packages only do *not* depend on some others (e.g. libraries) *in Sage* just because of the way we configure, patch or build / install them. IMHO as well worth a note.",
    "created_at": "2010-09-04T04:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9765#issuecomment-95705",
    "user": "leif"
}
```

Replying to [comment:14 drkirkby]:
> Replying to [comment:13 mpatel]:
> > Since we build Cliquer in Sage with make instead of with SCons (see #9804), should we include SCons in the dependency list in `SPKG.txt`?  
> 
> No, we should not. I'll create a new patch and provide a new package in a minute. It wont take me long to delete one line. 
> 
> > If we do, should we add a note that SCons is not a Cliquer dependency *in Sage*?
> 
> I don't know where you would add a note that SCons is not a Cliquer dependency. Where would you propose to add such a note? 

I think it's worth adding a note (in parentheses) to the *Dependencies* section that some package['s ordinary build] does *not* depend on `xy` especially if (e.g) the upstream contains source files for / files (usually) to be processed by `xy`, or in cases where the package *previously* depended on some package(s), but no longer does. (And even if there erroneously was some dependency listed in `spkg/standard/deps`.)

Typical candidates for `xy` are Python, Perl, lex/flex, yacc/bison etc. (Autotools should not be listed.)

Also, some packages only do *not* depend on some others (e.g. libraries) *in Sage* just because of the way we configure, patch or build / install them. IMHO as well worth a note.
