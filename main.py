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
    os.system(f"ionic start {name} --type=angular --cordova --appname='{name}' ")
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
                    '  "homepage": "https://ionicframework.com/",\n'
                    '  "scripts": {\n'
                    '    "ng": "ng",\n'
                    '    "start": "ng serve",\n'
                    '    "build": "ng build",\n'
                    '    "test": "ng test",\n'
                    '    "lint": "ng lint",\n'
                    '    "e2e": "ng e2e",\n'
                    '    "lab": "ionic serve -o --lab",\n'
                    '	 "platform": "ionic cordova platform add android@11.0.0",\n'
                    '	 "apk": "ionic cordova build android"'
                    '  },\n'
                    '  "private": true,\n'
                    '  "dependencies": {\n'
                    '    "@angular/common": "^14.0.0",\n'
                    '    "@angular/core": "^14.0.0",\n'
                    '    "@angular/forms": "^14.0.0",\n'
                    '    "@angular/platform-browser": "^14.0.0",\n'
                    '    "@angular/platform-browser-dynamic": "^14.0.0",\n'
                    '    "@angular/router": "^14.0.0",\n'
                    '    "@ionic/angular": "^6.1.9",\n'
                    '    "rxjs": "~6.6.0",\n'
                    '    "tslib": "^2.2.0",\n'
                    '    "zone.js": "~0.11.4"\n'
                    '  },\n'
                    '  "devDependencies": {\n'
                    '    "@angular-devkit/build-angular": "^14.0.0",\n'
                    '    "@angular-eslint/builder": "~13.0.1",\n'
                    '    "@angular-eslint/eslint-plugin": "~13.0.1",\n'
                    '    "@angular-eslint/eslint-plugin-template": "~13.0.1",\n'
                    '    "@angular-eslint/template-parser": "~13.0.1",\n'
                    '    "@angular/cli": "^14.0.0",\n'
                    '    "@angular/compiler": "^14.0.0",\n'
                    '    "@angular/compiler-cli": "^14.0.0",\n'
                    '    "@angular/language-service": "^14.0.0",\n'
                    '    "@ionic/angular-toolkit": "^6.0.0",\n'
                    '    "@types/jasmine": "~3.6.0",\n'
                    '    "@types/jasminewd2": "~2.0.3",\n'
                    '    "@types/node": "^12.11.1",\n'
                    '    "@typescript-eslint/eslint-plugin": "5.3.0",\n'
                    '    "@typescript-eslint/parser": "5.3.0",\n'
                    '    "eslint": "^7.6.0",\n'
                    '    "eslint-plugin-import": "2.22.1",\n'
                    '    "eslint-plugin-jsdoc": "30.7.6",\n'
                    '    "eslint-plugin-prefer-arrow": "1.2.2",\n'
                    '    "jasmine-core": "~3.8.0",\n'
                    '    "jasmine-spec-reporter": "~5.0.0",\n'
                    '    "karma": "~6.3.2",\n'
                    '    "karma-chrome-launcher": "~3.1.0",\n'
                    '    "karma-coverage": "~2.0.3",\n'
                    '    "karma-coverage-istanbul-reporter": "~3.0.2",\n'
                    '    "karma-jasmine": "~4.0.0",\n'
                    '    "karma-jasmine-html-reporter": "^1.5.0",\n'
                    '    "protractor": "~7.0.0",\n'
                    '    "ts-node": "~8.3.0",\n'
                    '    "typescript": "~4.7.3"\n'
                    '  },\n'
                    '  "description": "An Ionic project"\n'
                    '}')
            f.close()
            continue

    # Generation completed
    os.chdir(project_dir)
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
