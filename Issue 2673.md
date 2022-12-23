# Issue 2673: Upgrade mercurial to the 1.0 release.

Issue created by migration from https://trac.sagemath.org/ticket/2673

Original creator: mabshoff

Original creation time: 2008-03-26 08:55:42

Assignee: mabshoff

Mercurial 1.0 has been released - see http://www.selenic.com/pipermail/mercurial/2008-March/018014.html

Shamelessly copying the release announcement:

```
After nearly three years of development (and nearly that many of
production use) we're proud to announce the release of Mercurial 1.0. 
Thanks to the countless people who've contributed to development and
testing!

Available at http://selenic.com/mercurial/

General:
 * greatly improved merge tool configuration, see "hgrc.5.txt" for details
 * improved copy/rename handling in diffs, status, and merge
 * files in .hg inherit permissions from .hg/store
 * infer --repository when possible, so commands may be run from anywhere.
 * easy-installable
 * new "droplet" logo

Commands:
 * archive: disable ".hg_archival.txt" file addition with "ui.archivemeta"
 * bisect: now built-in with greatly improved performance and usability
 * bundle: new --all option to bundle the whole repository more easily.
 * cat: apply decode filters with --decode
 * clone: can clone from a full-history bundle
 * commit: warn when creating a new head
 * debugancestor: index argument is now optional
 * diff: set the number of context line to show with -U/--unified
 * grep: display matched revisions commit date with --date
 * import: new --no-commit and --user options
 * incoming/outgoing: add --limit option
 * log: use -b/--only-branch to show revisions of a single branch
 * remove: improve handling for --after
 * revert: major speedup
 * serve: prefix the served path with --prefix (also in [web] section)
 * status: unknown files are skipped by --quiet
 * tag: allow multiple tags to be added or removed
 * tags: --verbose flags local tags
 * update: switch between named branches without -C

Extensions:
 * churn: promoted to an official extension (previously in contrib)
 * color: new extension coloring "status" and "qseries" command outputs
 * convert:
   * allow synthetic history to be spliced in with --splicemap
   * support GNU Arch and Monotone sources
   * svn: allow shallow conversions of single branches with convert.svn.startrev option.
   * svn: make trunk/branches/tags layout detection more flexible by allowing either of them to be skipped.
   * svn: preliminary support as a conversion target
 * hgk: configuration file changed from .gitk to .hgk
 * highlight: new extension enabling syntax highlighting in hgweb file view (requires pygments)
 * inotify: new extension using Linux 2.6 inotify API for instant status checking
 * keyword: new extension for filewise RCS-keyword expansion in working directory
 * mq: new --currentdate, --date, --currentuser, and --user options
 * record: add "qrecord" command when used with mq
 * win32mbcs: new extension dealing with problematic MBCS behavior on Windows 

Web interface:
 * improved WSGI integration and compatibility
 * follow symlinks in hgwebdir collections
 * show branches in most of gitweb templates
 * add line anchors to annotate, changeset, diff and file views 
 * support web.baseurl in hgwebdir, overriding SCRIPT_NAME

Hooks:
 * standard hook to reject text files with CRLF in win32text extension
 * redirect stdout to stderr for ssh and http servers

Windows support:
 * "hg" script output set to binary mode for redirecting diff, export, annotate, etc.
 * also search for .hgrc if mercurial.ini cannot be found
 * major speedup of "clone --pull"

```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 08:55:51

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-31 01:04:09

This is a duplicate of #3705, so I am closing it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 01:04:09

Resolution: duplicate
