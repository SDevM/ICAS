# Ionic-Cordova App Starter (I.C.A.S) - Simon D. Maxwell
#### Please leave a ⭐ star if you use my script! :)
## Features

-   [x] Generate app name, authors and description
-   [x] Create an Angular Ionic application fitted with Cordova
-   [x] Prepare **@ionic/cordova-builders**
-   [x] Optional Bootstrap and Tailwind options

If you'd like to contribute to this project, simply create a fork and make a pull request following this projects pull request format.

## Pre-requisites

-   Windows Operating System
-   Python **3.10.x** or later
-   Ionic

## Requisites

-   JDK 11+
    -   Set JAVA_HOME to the JDK folder [C:\Program Files\Java\jdk_version_folder]()
-   Android Studio(Android SDK)
    -   Set ANDROID_HOME to [C:/users/\*\*\*/AppData/Local/Android/Sdk]()
    -   Get SDK Manager > SDK Platforms > Android API 32
    -   Get SDK Manager > SDK Tools > Android SDK Tools (Obsolete) `uncheck Hide Obsolete Packages`
    -   Get SDK Manager > SDK Tools > SDK Build-Tools 32 `check Show Package Details`
-   Gradle
    -   Create new entry to `path` in System Environment Variables pointing to [C:Gradle/gradle_version_folder]()
-   Microsoft Build Tools for Visual Studio 2015
-   Cordova

## Usage

-   Double click **gen.bat** to get started
-   Double click **ICAS.gen.Ink** (option 2)
-   Run the platform script `npm run platform`, then you can run the apk script `npm run apk`
-   ICAS.gen.Ink is a shortcut file that can be added to your start menu `right click file, select Pin to Start Menu`

## NPM COMMANDS

### Open Lab

> Runs commands to pull up the lab view of your project `npm run lab`

### Set Android Platform (Default Android@11.0.0)

> Runs commands to set your android platform `npm run build:platform`

### Build Android APK

> Runs commands to build your apk `npm run build:apk`

### Combo: `npm run build:deploy`

### Open Android Project In Android Studio

> Runs command to open android studio `npm run studio`

### Prepare Android Resources For Android Studio

> Runs command to prepare android resources`npm run studio:prepare`

### Combo: `npm run studio:launch`
