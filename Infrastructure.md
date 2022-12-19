This page aims to keep information public about Sage's infrastructure.
Question mark means that the information is not confirmed, please edit if you know more... and *note the date of your update* so that current and stale information can be distinguished.

Please mark which services still need to find a new home, with the system requirements and the deadline.

[This is the Trac macro *PageOutline* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PageOutline-macro)

# Current services

## DNS
  * registrant: was
  * admin: was, schilly
  * tech contact: was, schilly

## ask.sagemath.org
  * purpose: webserver where users can get support
  * hosted at: [LIPN (CS lab)](https://lipn.univ-paris13.fr/), University Paris North (Villetaneuse)
  * contact: sage-askbot-admin`@`googlegroups.com
  * url: https://ask.sagemath.org
  * admin: tmonteil
  * local sage dev: tmonteil
  * technology used: unprivileged LXC, debian, nginx, uwsgi, postgesql, askbot
  * issues : upgrade askbot to further versions is pretty painful (broken database migration scripts)
  * formerly hosted at: [Ohio State University](https://www.osu.edu/) (thanks !)
    * resources needed: database on a separate VM, 2GB RAM, 10GB disk
    * admin: niles, tmonteil
    * local tech contact: David Alden, Josh Carroll
    * technology used: ubuntu, nginx, uwsgi, postgesql, askbot
    * there are two machines : ask-sagemath and ask-sagemath-db


## backup
  * purpose: keep the data of various services in a separate place
  * hosted at: [Mathematics lab](https://www.math.u-psud.fr/?lang=fr), Université Paris Sud (Orsay)
  * technology used: debian, rsync, cron
  * resources needed: 1TB disk
  * admin: tmonteil, slelievre
  * local sage dev: slelievre
  * local tech contact: Mathilde Rousseau
  * currently keeping a daily backup of :
    * https://ask.sagemath.org
    * https://wiki.sagemath.org


## doc.sagemath.org, planet.sagemath.org, www.sagemath.org
  * purpose: on-line browsable documentation + web homepage
  * hosted at: github.io
  * technology used: proprietary
  * resources needed: 0 CPU, 0 RAM, 0 DISK
  * admin: everyone who is on the github group for sagemath
  * contact: schilly for the website
  * url: https://doc.sagemath.org https://planet.sagemath.org https://www.sagemath.org

## files.sagemath.org, fileserver.sagemath.org, old.files.sagemath.org
  * purpose: main files, spkgs, and backup of "other" files
  * what's at files.sagemath.org is _exactly_ rsync.sagemath.org::sage
  * old.files.sagemath.org has the old stable releases
  * are the old development tarballs are still archived somewhere?
  * hosted at: UW. Other places are the mirrors of it.
  * contact: schilly, vbraun
  * admin: ohanar?
  * url: http://files.sagemath.org http://fileserver.sagemath.org http://old.files.sagemath.org

## git.sagemath.org, trac.sagemath.org
  * purpose: development tools, they share the same host
  * hosted at: google ?
  * technology used: ubuntu, apache, git, trac
  * resources needed: ?CPU ?RAM ?DISK
  * admin: people with root access: kclawson, ohanar, vbraun, mderickx, robertwb, wstein, dimpase
  * contact: no real organisation yet, go to sage-devel
  * url: https://git.sagemath.org https://trac.sagemath.org

## [GitHub](GitHub) organization for [SageMath](SageMath)
  * url: https://github.com/sagemath
  * admin: schilly, vbraun

## [GitLab](GitLab) organization for [SageMath](SageMath)

  * url: https://gitlab.com/sagemath
  * admin: embray, jrueth

## build.sagemath.org
  * purpose: distribute and gathers automatic binary building on volunteer's machines
  * hosted at: University of Washington
  * technology used: ubuntu, nginx; using using the continuous integration framework of http://buildbot.net/
  * resources needed: ?CPU ?RAM ?DISK
  * admin: ??
  * contact: ??
  * url: http://build.sagemath.org

## patchbot.sagemath.org
  * purpose: distribute and gathers automatic ticket testing on volunteer's machines
  * hosted at: [IRMA](https://irma.math.unistra.fr/), [Université de Strasbourg](http://www.unistra.fr)
  * technology used: ubuntu, nginx, uwsgi, flask, mongodb, see [patchbot](patchbot) for more details
  * application source code: https://github.com/sagemath/sage-patchbot
  * resources needed: Minimal CPU, RAM. ~50GB disk.
  * admin: chapoton, tmonteil
  * root access: chapoton, tmonteil
  * contact: chapoton, tmonteil
  * local sage dev: chapoton
  * local tech contact: Alain Sartout
  * url: https://patchbot.sagemath.org

## rsync.sagemath.org
  * purpose: the seed for mirrors, see MirrorNetwork for more details
  * hosted at: University of Washington
  * technology used: rsync
  * resources needed:
     * CPU 1 core
     * RAM 2-3 GB (mostly for caching when calculating hashes)
     * DISK enough for all sage files (50+ GB)
  * admin: schilly
  * contact: schilly
  * url: http://rsync.sagemath.org

## sagecell.sagemath.org
  * purpose: allow embedding sage computations within a webpage
  * hosted at:
    * [Goethe-Universität](https://www.uni-frankfurt.de) (Frankfurt, Germany)
    * [Universidad Autónoma de Madrid](https://www.uam.es) (Madrid, Spain)
    * Google Compute Engine (Council Bluffs, Iowa, USA)
  * technology used: production installation requires a dedicated server (either physical or virtual)
  * resources needed:
    * RAM: 32GB recommended for smooth operation, 16GB may become enough in the future
    * CPU: the more the better for handling spikes in load and allowing parallel interacts, but any will do if necessary
    * DISK: must have BTRFS at least for /var/lib/lxc, SSD is preferable, 100GB should be sufficient for the foreseeable future
  * admin: novoselt
  * contact: novoselt
  * available urls: http://aleph.sagemath.org, https://sagecell.sagemath.org

## wiki.sagemath.org
  * purpose: the wiki you are reading!
  * [#33725](https://trac.sagemath.org/ticket/33725): Migrate wiki.sagemath.org to trac.sagemath.org/wiki
  * hosted at: [LIPN (CS lab)](https://lipn.univ-paris13.fr/), University Paris North (Villetaneuse)
  * contact: sagemath-admins`@`googlegroups.com
  * url: https://wiki.sagemath.org
  * admin: tmonteil
  * local sage dev: tmonteil
  * technology used: unprivileged LXC, debian, nginx, certbot, uwsgi, moinmoin, jsmath, docutils
  * formerly hosted at: cloud.google.com
  * possible issue in migration: the database of user accounts is synced from trac when this latter is modified (incron)

## DockerHub organization
  * purpose: distribute SageMath Docker images
  * hosted at: https://hub.docker.com/u/sagemath/
  * admin: embray, jrueth
  * other: slelievre also has push access

# Defunct services

## sagenb.org
  * purpose: public notebook,
  * state: end of life; redirects to [CoCalc](https://cocalc.com/)
  * volunteers to provide worksheets back to the users: dimpase, tmonteil, vdelecroix

## sageb0t
  * purpose: turn pull requests on GitHub into trac tickets
  * contact: robertwb

## zulip.sagemath.org
  * purpose: chat system
  * state: has been replaced by https://sagemath.zulipchat.com/
