import os
import subprocess
import tkinter
from datetime import date
from tkinter import filedialog


# Main function
def main():
    app_name = "Ionic-Cordova App Starter (ICAS) - Simon Maxwell"
    app_version = "v1.2.0"

    authorsCount = int(input('How many authors does this project have?\n'))
    print('If at any time you realize you have requested too many authors, enter "*end"\n'
          'If at any time you realize you have requested too little authors, enter "*more"\n')
    def authors(count):
        List = ""
        for i in range(count):
            temp = input(f"\nAuthor {i + 1}:")
            if temp == "*end":
                break
                print("\nYou have stopped the collection of any more authors!")
            elif temp == "*more":
                print("\nAn additional author will be accepted!")
                count+=1
                return authors(count)
            else:
                List += temp + "\n"
        return List

    authorList = authors(authorsCount)
    print(authorList)
    name = input("What will this project be named?")
    print("[!] Where should this project be stored? [Hit enter to select location]")
    tkinter.Tk().withdraw()
    gen_directory = filedialog.askdirectory()
    os.chdir(gen_directory)
    os.system(f"ionic start {name} --type=ionic-angular --cordova")
    project_dir: str = os.path.normpath(os.path.join(gen_directory, name))
    # folders: list[str] = [  ]
    files: list[str] = [ "authors", "package.json" ]

    # Create folders
    # for folder in folders:
    #     depth_1_folder: str = os.path.normpath(os.path.join(project_dir, folder))
    #     os.mkdir(depth_1_folder)

    # Create files
    for file in files:
        if file == "authors":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "w")
            f.write(authorList)
            f.close()
            continue
        if file == "package.json":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "w")
            f.write('{\n'
                    f'  "name": "{name}",\n'
                    '  "version": "0.0.1",\n'
                    '  "author": "Ionic Framework",\n'
                    '  "homepage": "http://ionicframework.com/",\n'
                    '  "private": true,\n'
                    '  "scripts": {\n'
                    '    "start": "ionic-app-scripts serve",\n'
                    '    "clean": "ionic-app-scripts clean",\n'
                    '    "build": "ionic-app-scripts build",\n'
                    '    "lint": "ionic-app-scripts lint",\n'
                    '    "lab": "ionic serve -o --lab",\n'
                    '    "platform": "ionic cordova platform add android@11.0.0",\n'
                    '    "apk": "ionic cordova build android"\n'
                    '  },\n'
                    '  "dependencies": {\n'
                    '    "@angular/animations": "5.2.11",\n'
                    '    "@angular/common": "5.2.11",\n'
                    '    "@angular/compiler": "5.2.11",\n'
                    '    "@angular/compiler-cli": "5.2.11",\n'
                    '    "@angular/core": "5.2.11",\n'
                    '    "@angular/forms": "5.2.11",\n'
                    '    "@angular/platform-browser": "5.2.11",\n'
                    '    "@angular/platform-browser-dynamic": "5.2.11",\n'
                    '    "@ionic-native/core": "4.20.0",\n'
                    '    "@ionic-native/splash-screen": "4.20.0",\n'
                    '    "@ionic-native/status-bar": "4.20.0",\n'
                    '    "@ionic/storage": "2.2.0",\n'
                    '    "ionic-angular": "3.9.9",\n'
                    '    "ionicons": "3.0.0",\n'
                    '    "rxjs": "5.5.11",\n'
                    '    "sw-toolbox": "3.6.0",\n'
                    '    "zone.js": "0.8.29"\n'
                    '  },\n'
                    '  "devDependencies": {\n'
                    '    "@ionic/app-scripts": "3.2.4",\n'
                    '    "@ionic/lab": "3.2.13",\n'
                    '    "cordova-android": "^11.0.0",\n'
                    '    "cordova-plugin-device": "^2.0.2",\n'
                    '    "cordova-plugin-ionic-keyboard": "^2.2.0",\n'
                    '    "cordova-plugin-ionic-webview": "^5.0.0",\n'
                    '    "cordova-plugin-splashscreen": "^5.0.2",\n'
                    '    "cordova-plugin-statusbar": "^2.4.2",\n'
                    '    "typescript": "2.6.2"\n'
                    '  },\n'
                    '  "description": "An Ionic project",\n'
                    '  "cordova": {\n'
                    '    "plugins": {\n'
                    '      "cordova-plugin-statusbar": {},\n'
                    '      "cordova-plugin-device": {},\n'
                    '      "cordova-plugin-splashscreen": {},\n'
                    '      "cordova-plugin-ionic-webview": {},\n'
                    '      "cordova-plugin-ionic-keyboard": {}\n'
                    '    },\n'
                    '    "platforms": [\n'
                    '      "android"\n'
                    '    ]\n'
                    '  }\n'
                    '}')
            f.close()
            continue

    # Generation completed
    os.system("ng add @ionic/cordova-builders")
    completed(os.path.normpath(project_dir))


def banner():
    print('\n'
          '████████     ██████     ███    ██   ████████    ██████   ██ █         ██████  ███████ ███    ██ \n'
          '   ██      ██      ██   ████   ██      ██      ██          ██ █      ██       ██      ████   ██ \n'
          '   ██      ██      ██   ██ ██  ██      ██      ██            ██ █    ██   ███ █████   ██ ██  ██ \n'
          '   ██      ██      ██   ██  ██ ██      ██      ██          ██ █      ██    ██ ██      ██  ██ ██ \n'
          '████████     ██████     ██   ████   ████████    ██████   ██ █         ██████  ███████ ██   ████ \n'
          '\n')


def completed(generated_app_dir: str):
    # Change generated directory to absolute path if it is in the script's directory
    if "\\" not in generated_app_dir:
        generated_app_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), generated_app_dir))

    print()
    print("*******************************************")
    print("[!] Ionic-Cordova App Generated")
    print(f"[!] Directory - {generated_app_dir}")
    print("*******************************************")
    print()

    # Open project directory after app is generated. Windows Only
    # explorer_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    # subprocess.run([explorer_path, generated_app_dir])

    # Open project directory in VSCode if installed
    cmd_path = os.path.join(os.getenv("WINDIR"), os.path.normpath("/Windows/System32"), "cmd.exe")
    subprocess.run([cmd_path, f"cmd.exe /C cd {generated_app_dir} && code ."])


# Script entry point
if __name__ == "__main__":

    # print(cmd_path)
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\033[93m\n\nUnexpected Exit\n\033[0m")
        exit(0)
