# Apple photo importer:
In this repository there is a small utility to upload a photo backup (requested from the [privacy site](https://privacy.apple.com/)) to Apple's photo app, while preserving metadata, albums, and folders.

* `gather_infos.py`: Python utility to gather and organize information about the photo database.
* `driver_script`: AppleScript script leverages direct Photo integration and provides handy UI.

## Usage:
* Install python 3
* Download the release version from [the release page](https://github.com/mattia-marini/Apple-Photo-Importer/releases)
* Unzip and run the app

## Create from source
If you want to create the bundle from the source code, you need to:
* Open `driver_script` with the defaul Script app
* _File -> Export_ and export thee script  *as an application*
* In the app generated: _Right click -> Show package content_ and navigate to _Contents/Resources/Scripts_
* Copy the `gather_infos.py` in this folder
