These notes are part of the Operating Manual of the OGD Handbook project.

# 1 System overview

The OGD Handbook is a static site running on a standard web hosting provider (METANET). Content changes are made to a set of formatted text files (Markdown) and hosted in an open source wiki-style repository in a cloud service (GitHub). A static site generator (Pelican) updates the site when changes are made to any of the content. This is an optimal, modern solution to hosting sites of this type in a secure and performant way. The project is currently in Beta and being actively further developed by the opendata.swiss team in consultation with Oleg Lavrovsky, Datalets.

- The OGD Handbook is hosted at https://handbook.opendata.swiss
- All primary content sources are maintained at https://github.com/opendata-swiss/ogd-handbook-wiki
- The website generator and frontend assets are at https://github.com/opendata-swiss/ogd-handbook-site
- User-facing instructions on editing the content are at https://handbook.opendata.swiss/en/pages/contribute
- Web site administration and maintenance is done at https://quintus.metanet.ch:8443
- Usage statistics can be found at https://handbook.opendata.swiss/plesk-stat/webstat/
- Site generation is done on a server maintained by https://datalets.ch

# 2 Operating process

Making content changes requires knowledge of the Markdown syntax for plain text formatting, an understanding of the metadata used to classify the content at the top of each Markdown-formatted page, and some appreciation of the overall structure of the OGD Handbook.

There are four main sections (Identify, Prepare, Publish, Support) as well as a Library and search function. Each section contains pages (articles or Library documents), which are translated into each of the four supported languages (German, French, Italian, English) by using four distinct files for each piece of content.

Any changes to the site content through updates to the master branch of the „wiki“ repository lead to the HTML site being refreshed automatically using the site generator application (Pelican) running on an application server (Linux, Nginx), the refresh processing being triggered by a web hook configured in GitHub. Note that besides the web version (HTML), articles are also exported to downloadable formats (ODT, DOCX) as described in the next section.

The web site is developed with a frontend based on the opendata.swiss theme, and uses the same Bootstrap 3 framework. CSS3 and HTML5 skills are needed to make improvements to the frontend, and some Python and JavaScript experience to change global configuration, or work on some of the interactive functionality like navigation and search.

Maintenance requirements include ability to run and configure standard HTML web hosting provider, as well as to host the Python based refresh application on a Linux application server.

Quality assurance can be done by seeing if there are any visible issues on the public web site, checking the history of changes to the content repository to see if there were any errors added by editors, and looking in the logs of the site generator to make sure the job completed successfully.

# 3 Monitoring

Since the main user facing application is a simple static web site with currently relatively low amounts traffic, the monitoring requirements are minimal. Notifications are obtained from the web hosting provider in case of any downtime or security issues, and additional users can be added to this list. Basic uptime monitoring could be added, but in our experience the amount of downtime is negligible for the user-facing part. There is a plethora of statistics and various monitoring options available in the Plesk web console provided by METANET.

The main monitoring concern is moderation of content changes. Since the content is open access, we need to limit editing to authorized persons only. This is done using repository permissions on GitHub. Only specific users are allowed to make changes to the master branch. And they are only allowed to do this by approving a Pull Request, adding transparency to every change made to the content. This process of making contributions is known as Git Flow, and is widespread in the open source community.

Monitoring of content changes can be done using the tools provided by GitHub, i.e. watching the repositories to be notified on the GitHub dashboard and by email of changes, checking the commit log on the website, or even by looking directly at the git log using other tools. Pull Requests are an important mechanism to ensure that checks are being done of any major edits of the content.

A feature of the OGD Handbook is that all articles are also exported to LibreOffice (ODT) and Microsoft Office (DOCX) formats during site generation, using a custom script and document template which is processed in a headless (no GUI) version of LibreOffice running on the server. This is the most intensive part of the content generation, using considerable amounts of CPU and RAM to refresh the site if changes occur.

There is a reasonable likelihood that the refresh job will fail. The person making changes – or more likely, approving them using GitHub Pull Requests – will notice that the site does not update. In the worst case, the update job aborts mid-way resulting in a partial upload. Currently there is no notification of success or failure, but options to do this are available. There are also now several providers of hosted Site Generators which could make a fully managed solution possible.

Statistics about hits and visits is currently handled by the Webalizer software provided by METANET. Metrics about the content and contributors is available from in the GitHub repositories. Integration with the Piwik web analytics service used at opendata.swiss has been foreseen, but not yet implemented.

In case of errors, the primary contact for the project is the opendata.swiss team, via https://opendata.swiss/en/contact/

Currently the project is actively being developed by Oleg Lavrovsky, Datalets and the opendata.swiss team into a next phase. We are using Trello boards to coordinate tasks and set the roadmap.

# 4 Interruption or end of service

Temporarily downtime can be instated through the METANET control panel (Plesk), to show a "temporarily offline" message to website visitors.

Permanent disconnection can be achieved by:

1. Disabling web hooks in the GitHub repositories
2. Removing the websites from METANET's control panel
3. Deleting web hosting accounts at METNAET
4. Stopping the site generation service provided by Datalets
5. Archiving and deleting the content and site code repositories in GitHub
6. Archiving the handbook subdomain

The service can be reinstated through:

1. Setting up content and site code repositories
2. Setting up a web hosting service and connecting the subdomain
3. Setting up a site generator service and authenticating it to the web hosting
4. Connecting the site generator job to a refresh web hook notification
5. Publishing the site and activating the web hosting

To ensure the system is working as expected, the following checks should be made:

- [ ] Ensure that the generated web site looks and works as expected
- [ ] Make a modification to the content, and check that it is published
- [ ] Check that there are no errors in the site generator logs
- [ ] Check that there are no errors in the browser error console
- [ ] Check that there are no errors in the web administration console (Plesk)

The complete and current source code and content can be downloaded at anytime from the GitHub repositories.

During the initial development phase, complete project documentation (including preliminary research, analysis and writing), was provided on DVD to the team at the Swiss Federal Archives. This historical information can also be obtained from Oleg Lavrovsky, Datalets.

# 5 Support Process

Currently there are no strictly defined support processes or roles. End-user support responsibilities are with the opendata.swiss team, who get technical support from Oleg Lavrovsky, Datalets. Several members of the technical team at Liip AG responsible for the opendata.swiss portal are also experienced in working with the OGD Handbook, however they are not currently supporting it.

# 6 Change Management

No Change Management Process or Roles have  been defined yet in this project. A series of workshops have been organized to share knowledge and introduce more people from Swiss Open Government Data projects and the wider open data community to the OGD Handbook and the way it operates, and could be a starting point.

# 7 Security Notes

Data loss concerns are minimal for a site whose contents are completely stored in a Git repository. Complete copies of the entire site exist on the web and application server, and data loss on a top-notch platform like GitHub is highly unlikely. Nevertheless, Git technology makes it easier to add additional automatic backups of the site to increase redundancy.

No particular data protection mechanisms are necessary in this project, as none of the content has personal information. Protection of user account data for content editing is handled by GitHub, with more information on the mechanisms in place available at https://help.github.com/articles/about-github-s-use-of-your-data/

No security reviews have been done of the code base, however the site generator project dependencies are being validated for security issues using automatic vulnerability alerts. There is no mechanism in place for ensuring the safety of contributed content, this is done through a manual review of every change to the content. It would be reasonable to augment this with automatic checks of the resulting frontend site in the future.

The public website is secured using SSL and a Let's Encrypt certificate automatically renewed by the Plesk console.
