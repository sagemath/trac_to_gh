# Issue 5380: devmap: allow to search for contributions by trac username

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-02-26 03:15:52

Assignee: schilly

CC:  schilly

Keywords: devmap

The development map (devmap) at



http://www.sagemath.org/development-map.html



currently supports search of a developer's contributions by her/his real name. For most developers, their real names diff from their trac usernames. The devmap should support search of contributions by trac usernames as well.


---

Attachment

diff against previous version of contributors.xml


---

Comment by mvngu created at 2009-02-26 03:28:13

The attached XML file `contributors.xml` is an updated version of the file



http://www.sagemath.org/res/contributors.xml



The new version adds trac usernames of most people listed on the Sage development map. However, there are still a number of developers for whom that I've not been able to determine their trac usernames. These people are:
 1. Antti Ajanki
 1. Bill Allombert
 1. Benjamin Antieau
 1. Jennifer Balakrishnan
 1. Gregory Bard
 1. Karim Belabas
 1. Jonathan Bober
 1. Michael Brickenstein
 1. Nils Bruin
 1. Wilson Cheung
 1. Alex Clemesha
 1. Doug Cutrell
 1. Alyson Deines
 1. Tom Denton
 1. Jan Groenewald
 1. Rob Gross
 1. Bill Hart
 1. Leif Hille
 1. Neal Holtz
 1. Sean Howe
 1. Naqi Jaffery
 1. Peter Jipsen
 1. Michael Kallweit
 1. Jason Martin
 1. Kate Minola
 1. Rich Morin
 1. Gregg Musiker
 1. David Perkinson
 1. Pearu Peterson
 1. Bill Purvis
 1. Dorian Raymer
 1. R. Rishikesh
 1. Gordon Royle
 1. Kyle Schalm
 1. Jack Schmidt
 1. Denis Simone
 1. Steven Sivek
 1. Griffen Thoma
 1. Michel Vandenbergh
 1. Steve Vonn
 1. Mark Watkins
 1. Joe Wetherell
 1. Dal S. Yu
 1. Gary Zablackis
 1. Mike Zabrocki
 1. Bin Zhang
However, Alexander Dreyer's trac username looks suspicious/ambiguous to me. I think his trac username is "PolyBoRi". I've also attached the patch file `trac_5380_search-by-username.patch  ` which should be useful for reviewers who want to view differences between the updated version of `contributors.xml` and the previous version at http://www.sagemath.org/res/contributors.xml.


---

Comment by mabshoff created at 2009-02-26 03:56:45

Hi Minh,

 * not all people listed with credit have trac accounts, but I can go over the list
 * PolyBoRi is a single account for Alexander Dreyer and Michael Brickenstein - we might want to fix that.

Cheers,

Michael


---

Comment by schilly created at 2009-02-26 10:18:57

ok, thanks, that was fast!

file uploaded and everything working. just too bad that trac doesn't support searching by username, just this full text stuff, but indeed nice to be able to see where he/she had the fingers in :)


---

Comment by mvngu created at 2009-02-28 01:04:20

Replying to [comment:4 schilly]:
> file uploaded and everything working. just too bad that trac doesn't support
> searching by username, just this full text stuff, but indeed nice to be able
> to see where he/she had the fingers in :)
OK, with `contributors.xml` uploaded, I see that visitors to the devmap are able to search for a developer's contribution. If the said XML file contains a developer's trac username, then the visitor would be presented with a list of (possible) contributions made by the developer in question. However, if the XML file doesn't contain the developer's trac username, then the search query would be made using the developer's full name as provided on the devmap.



However, I still see a number of weird things in the trac search functionalities. Disclaimer: I'm not an expert on how the trac server searches for a developer's contributions.
 1. In cases where a developer's trac username has not appeared on any trac tickets, the search is still performed using the developer's username. I think this would likely result in a misleading list of search results, and the said developer's contribution on trac tickets would be missed by the search. A case in point is Maite Aranes, who has the username "mtaranes". After clicking on the link "search contributions", the search result is just Maite's name highlighted on the page
 
 

 http://trac.sagemath.org/sage_trac/wiki/WikiStart
  
 

  From the release note of Sage 3.3 and release tour, I'm 99.9% certain that Maite has contributed code in that release, in particular the ticket #4831.
 1. If a developer's trac username is two characters in length, then the search query returns a "Search Error" message, with the explanation
   {{{
   Search query too short. Query must be at least 3 characters long.
   }}}
   For example, Yi Qiang's username is "yi" and a search of his contribution returns a search error. This is weird, because Yi has made substantial contributions to the dsage package, and I think he's the original developer of dsage. I'm not sure how to fix this. However, an ad hoc fix might be to have the following policy for trac usernames: i.e. a trac username must be at least 3 characters in length. Perhaps someone can suggest a better workaround.

Apart from the above comments, someone else should verify/review this ticket and the updated devmap.


---

Comment by mabshoff created at 2009-03-01 02:27:49

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by schilly created at 2009-03-01 17:43:46

Replying to [comment:5 mvngu]:
> However, if the XML file doesn't contain the developer's trac username, then the search query would be made using the developer's full name as provided on the devmap.

i wanted to find a way to search for contributions where no trac account is known. That's why i take the real name. Plan B would have been to only include the link for those, where a trac account name is given and not for all the others. Testing some names seemed to be good enough to include the real name for those where no trac account is given...

Mixing trac account name and real name turned out to be a bad idea. In that case, sometimes nothing at all was found.

> "yi" and a search of his contribution returns a search error. 

yeahr well, trac search isn't good. probably searching with google (restricted site search on trac.sagemath.org) would be better - at least for two letter words like this one ;)

harald


---

Attachment

Remove Yi Qiang's trac username


---

Attachment

Remove trac usernames of some people


---

Attachment

Updated contributors list


---

Comment by mvngu created at 2009-03-16 06:07:18

The updated contributors list *contributors.xml* is similar to the previous version, except that Yi Qiang's trac username has been removed so that we can search for his contribution using this full name. This search option would result in more matches than getting an error message when searching with two letters. I encountered another problem while searching contributions of the following people:
 1. Timothy Clemans
 1. Alexander Dreyer
 1. Alex Ghitza
 1. Simon King
 1. Nils-Peter Skoruppa

using the "Search contributions" links at



http://www.sagemath.org/development-map.html



Searching contributions of each of the above people result in a wiki page that says something like this:



http://trac.sagemath.org/sage_trac/wiki/TimothyClemans



That's because the trac search function mistakens the trac usernames of these people as empty wiki pages. So for now, the updated contributors list no longer has the trac usernames of the above people. Once the updated list *contributors.xml* is uploaded, a reviewer should check on the (new) devmap that clicking on the "Search contributions" links next to the above people, including Yi Qiang, should return some search results, which should not be error messages, or empty wiki pages. Other than the above comments, I think this messy ticket can be closed, unless someome has suggestions.


---

Comment by schilly created at 2009-03-16 11:33:49

Replying to [comment:8 mvngu]:
> The updated contributors list *contributors.xml*...

I've updated the website with that file. Changes looked good to me.


---

Comment by mabshoff created at 2009-03-16 15:58:00

Replying to [comment:9 schilly]:
> Replying to [comment:8 mvngu]:
> > The updated contributors list *contributors.xml*...
> 
> I've updated the website with that file. Changes looked good to me.

Changing it to a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-16 15:59:22

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-16 15:59:22

Resolution: fixed
