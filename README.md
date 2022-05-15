## SidharthPadhee.com

 1. Install [Hugo](https://gohugo.io/getting-started/quick-start/)
 2. Create new website -> `hugo new site sidharthpadhee.com`
 3. Add a theme
 ```
 cd sidharthpadhee.com
 git init
 git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal
 ```
 4. Start the hugo server `hugo server -t terminal`
 5. Generate public folder -> `hugo -t terminal`. This will generate the static website in the public folder.
 6. Link the github page repo to public folder -> `git submodule add -b main git@github.com:dragod812/myself.git public`
