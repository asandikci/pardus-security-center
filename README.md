# Pardus Security Center
**Secure your Pardus/Linux Installation with Firewall, Malware Scan and Link Checker**

### Features
- [ ] Firewall management
  - [ ] ufw
  - [ ] firewalld
<!-- ANCHOR - FOR FUTURE
  - [ ] iptables / nftables
-->
- [ ] Malware checker
  - [ ] ClamAV 
    - [ ] Complete scan
    - [ ] Realtime scan
    - [ ] Custom scan (file/folder)
<!-- ANCHOR - FOR FUTURE
    - [ ] Custom scan (disk)
--> 
  - [ ] VirusTotal (over API - for other suspicious files)
- [ ] Link checker <!-- (like URLChecker in Android) -->
- [ ] System certificate manager
- [ ] Suspicious command checker <!-- like `rm ~/` etc. Is it even possible to check this? -->
- [ ] Application validation <!-- via Hashes (/usr/share/pardus apps for example) -->
- [ ] Alert for critical security updates
- [ ] Hardware security
  - [ ] fwupd <!-- for hardware updates-->
  - [ ] USB/Disk mount settings <!-- no automount, allow only some disks/usbs (like in LiderAhenk) -->
  - [ ] Camera/Microfon access alert/history
- [ ] Network management <!-- like a mini/lightweight portmaster clone -->
  - [ ] Application network usage history
  - [ ] Basic DNS manager
<!-- ANCHOR - FOR FUTURE
  - [ ] DNS filtering
-->

<!-- ANCHOR - FOR FUTURE
- [ ] System Suspicious Usage Checker (Based Application CPU/GPU/RAM/Disk usage and opening frequency)
- [ ] Sandboxing & Application Permission Management
  - [ ] Flatpak Permissions (like Flatseal) 
  - [ ] AppArmor
  - [ ] SELinux
  - [ ] Firejail 
  - [ ] Docker/Subuser 
  - [ ] Bubblewrap Implementation ?
  - [ ] chroot Implementation ?
  - [ ] Mandatory Access Control Implementation ?
  - [ ] pure Namespace Implementation ?
  NOTE about flatpak security: https://hanako.codeberg.page/

- [ ] Hardened Kernel Setup
- [ ] Kernel CVE History (actually this could be another web based project)
- [ ] Keyring/Wallet Management
  - [ ] GNOME Keyring
  - [ ] KDE Wallet
  - [ ] other keyring/wallets?
- [ ] Password Checker (common security checks + HaveIBeenPwned request)
- [ ] GPG/SSH Key Management
-->

### Tech Stack
- Programming Language: **Python**
- Widget Toolkit: **PTK 4** (GTK4 Wrapper) and **Adwaita**
<!-- - Other Development Tools: VSCodium, GTranslator -->


### Dependencies
`sudo apt install libpardus libgtk-4-dev libadwaita-1-dev python3-gi python3`
<!-- TODO Dependencies should be updated?! -->

<!-- ### Screenshots -->

### Other
<details><summary>setting up NixOS development environment</summary>
install [gtk4.nix](https://git.aliberksandikci.com.tr/asandikci/common-dev/src/branch/main/gtk4.nix) and run `nix develop -f gtk4.nix` for installing dependencies
</details>

<details open><summary>Resource Projects</summary>

- This project is based on [Pardus Gnome Greeter](https://github.com/pardus/pardus-gnome-greeter) because uses libpardus/Ptk and latest GTK version (4)
- Also [Python GTK4 Dersi](https://github.com/pardus-topluluk/python-gtk4-dersi) used for general knowledge
- Main Resource: https://lazka.github.io/pgi-docs/
</details>