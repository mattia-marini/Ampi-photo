# Apple photo importer:
In this repository there is a small utility to upload a photo backup (requested from the [privacy site](https://privacy.apple.com/)) to Apple's photo app, while preserving metadata, albums, and folders. 

The app bundle is composed of 2 scripts (both in the _app/Contents/Resource/Scripts_ directory)

* `gather_infos.py`: Python utility to gather and organize information about the photo database.
* `driver_script`: AppleScript script leverages direct Photo integration and provides handy UI.

## Usage:
* Install python 3
* Download the release version from [the release page](https://github.com/mattia-marini/Apple-Photo-Importer/releases)
* Unzip and run the app

## Create from source
To edit the source code clone the repo or download the [latest release](https://github.com/mattia-marini/Apple-Photo-Importer/releases) and open the app bundle with the default script app in macos. As stated in the first section, the functionality resides only in `gather_infos.py` and `driver_script`, int the `Scripts` folder

Enjoy!
