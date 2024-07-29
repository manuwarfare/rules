# Rules for Debian-derived
update = sudo apt update -y
fupdate = sudo apt update -y && sudo apt upgrade -y
fail2log = sudo cat /var/log/fail2ban.log >> $HOME/fail2ban.log
build = sudo chmod 644 debian/install && sudo chmod -x debian/changelog && sudo chmod -x debian/control && sudo chmod -x debian/copyright && debuild -S -sa
compile = go clean -cache && go clean -modcache && sudo go clean -i -r -x && dpkg-buildpackage --sanitize-env -us -uc -m
