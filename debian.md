# Rules for Debian-derived
b:update = sudo apt update -y:b
b:fupdate = sudo apt update -y && sudo apt upgrade -y:b
b:fail2log = sudo cat /var/log/fail2ban.log >> $HOME/fail2ban.log:b
b:build = sudo chmod 644 debian/install && sudo chmod -x debian/changelog && sudo chmod -x debian/control && sudo chmod -x debian/copyright && debuild -S -sa:b
b:compile = go clean -cache && go clean -modcache && sudo go clean -i -r -x && dpkg-buildpackage --sanitize-env -us -uc -m:b
