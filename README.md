# RPM spec for envconsul

The resulting RPM will contain one (1) file: the `envconsul` binary.
Nonetheless, it is worth mentioning that this spec attempts to respect the
Fedora [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines).

* Binary: `/usr/bin/envconsul`

# How to build

* Check out this repo. Seriously, check it out. Nice.
* Ensure that `rpmdevtools` and `mock` are available:
```
$ sudo yum install rpmdevtools mock
```
* Get with the build tree.
```
$ rpmdev-setuptree
```
* Symlinks for great justice.
```
$ ln -s envconsul-rpm/SPECS/envconsul.spec rpmbuild/SPECS/
```
* Download the release tarball.
```
$ spectool -g -R rpmbuild/SPECS/envconsul.spec
```
* And at long last, we build.
```
$ rpmbuild -ba rpbuild/SPECS/envconsul.spec
```

# More info

Largely based on @tomhillable's [consul-rpm](https://github.com/tomhillable/consul-rpm)
repo. Thanks!
