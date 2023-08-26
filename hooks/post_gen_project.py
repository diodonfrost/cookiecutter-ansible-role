import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def strtobool(value: str) -> bool:
    """Convert string to boolean."""
    return value.lower() in ("yes", "y", "true", "t", "1")


openbsd_support = strtobool('{{cookiecutter.openbsd_support}}')
freebsd_support = strtobool('{{cookiecutter.freebsd_support}}')
solaris_support = strtobool('{{cookiecutter.solaris_support}}')
windows_support = strtobool('{{cookiecutter.windows_support}}')
macos_support = strtobool('{{cookiecutter.macos_support}}')
dev_container = strtobool('{{cookiecutter.dev_container}}')
project_licenses = '{{cookiecutter.license}}'

if not openbsd_support:
    remove(os.path.join('molecule', 'openbsd'))
    remove(os.path.join('vars', 'OpenBSD.yml'))

if not freebsd_support:
    remove(os.path.join('molecule', 'freebsd'))
    remove(os.path.join('vars', 'FreeBSD.yml'))

if not solaris_support:
    remove(os.path.join('molecule', 'solaris'))
    remove(os.path.join('vars', 'SunOS.yml'))

if not windows_support:
    remove(os.path.join('molecule', 'windows'))
    remove(os.path.join('vars', 'Win32NT.yml'))

if not macos_support:
    remove(os.path.join('vars', 'Darwin.yml'))

if not dev_container:
    remove('.devcontainer')

if project_licenses == "Apache Software License 2.0":
    shutil.move(os.path.join('_licenses', 'Apache-2'), 'LICENSE')
    remove('_licenses')

if project_licenses == "BSD-3":
    shutil.move(os.path.join('_licenses', 'BSD-3'), 'LICENSE')
    remove('_licenses')

if project_licenses == "GNU GPL v3.0":
    shutil.move(os.path.join('_licenses', 'GPL-3'), 'LICENSE')
    remove('_licenses')

if project_licenses == "MIT":
    shutil.move(os.path.join('_licenses', 'MIT'), 'LICENSE')
    remove('_licenses')

if project_licenses == "Mozilla Public License 2.0":
    shutil.move(os.path.join('_licenses', 'Mozilla-2.0'), 'LICENSE')
    remove('_licenses')
