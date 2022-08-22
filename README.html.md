<head>
    <style>
        .instruction {
            color: #FBB454;
        }
        .path {
            color: #F637EC;
        }
        .noun {
            color: lightgreen;
        }
        .fa-star {
            color: yellow;
        }
        .fa-triangle-exclamation {
            color: red;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css">
</head>

# Ionic-Cordova App Starter (I.C.A.S) - Simon D. Maxwell

## Features

<i class="fa-solid fa-star"></i> Create an Angular Ionic application fitted with Cordova <br/>
<i class="fa-solid fa-star"></i> Generate <span class="noun">angular.json</span> to comply with the needs of <span class="noun">@ionic/cordova-builders</span> <br/>

If you'd like to contribute to this project, simply create a fork and make a pull request following this projects pull request format.

## Pre-requisites

-   Python <span class="noun">3.10.x</span> or later <i class="fa-solid fa-triangle-exclamation"></i>
-   Windows Operating System <i class="fa-solid fa-triangle-exclamation"></i>
-   JDK 11+ <i class="fa-solid fa-triangle-exclamation"></i>
    -   Set JAVA_HOME to the JDK folder <span class="path">C:\Program Files\Java\jdk_version_folder</span> <i class="fa-solid fa-triangle-exclamation"></i>
-   Android Studio(Android SDK) <i class="fa-solid fa-triangle-exclamation"></i>
    -   Set ANDROID_HOME to <span class="path">C:\Users\\\*\*\*\AppData\Local\Android\Sdk</span> <i class="fa-solid fa-triangle-exclamation"></i>
    -   Get SDK Manager > SDK Platforms > Android API 32 <i class="fa-solid fa-triangle-exclamation"></i>
    -   Get SDK Manager > SDK Tools > Android SDK Tools (Obsolete): <span class="instruction">uncheck Hide Obsolete Packages</span> <i class="fa-solid fa-triangle-exclamation"></i>
    -   Get SDK Manager > SDK Tools > SDK Build-Tools 32: <span class=instruction>check Show Package Details</span> <i class="fa-solid fa-triangle-exclamation"></i>
-   Gradle <i class="fa-solid fa-triangle-exclamation"></i>
    -   Create new entry to **path** in System Environment Variables pointing to <span class="path">C:\Gradle\gradle_version_folder</span> <i class="fa-solid fa-triangle-exclamation"></i>
-   Microsoft Build Tools for Visual Studio 2015 <i class="fa-solid fa-triangle-exclamation"></i>
-   Cordova `npm i -g cordova` <i class="fa-solid fa-triangle-exclamation"></i>
-   Cordova Builders `npm i -g @ionic/cordova-builders` <i class="fa-solid fa-triangle-exclamation"></i>
-   Ionic `npm i -g ionic` <i class="fa-solid fa-triangle-exclamation"></i>

## Usage

> Double click <span class="noun">expressgen.bat</span> to get started
> Double click **ICAS.gen.Ink** (option 2)
> Run Set Android Platform script before Build Android APK script
> ICAS.gen.Ink is a shortcut file that can be added to your start menu `right click file, select Pin to Start Menu`


## Npm Commands

### Open Lab <i class="fa-solid fa-flask"></i>

> Runs commands to pull up the lab view of your project `npm run lab`

### Set Android Platform (Default Android@11.0.0) <i class="fa-brands fa-android"></i>

> Runs commands to build your apk `npm run platform`

### Build Android APK <i class="fa-brands fa-android"></i>

> Runs commands to build your apk `npm run apk`
