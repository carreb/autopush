# autopush
a simple python program that checks a directory for updates and automatically commits any updated files (and optionally pushes them)
## installation 📲
1. download the latest release
2. choose the options you want in config.ini
3. clone the repository you want to commit to in the same directory as this program. ensure the directory name is the same as the repository's name
4. `python main.py`: it will start checking the directory for changes and commit them if changes are detected.
## config ⚙️
there are 3 options in the config.ini file. required changes are marked with an *
### repo_name* 📂
put the repository name here, it will use it to know which directory to track.
### token* 🪙
generate an api token by going to Settings > Developer settings > Personal access tokens and then clicking on Generate new token configure it however you'd like and then paste it into the config file. make sure it has access to all repo features!!
### push_automatically 🔄
if `true`, the program will automatically push any changes made, if `false` you will have to run `$git push` to push your changes
## upcoming features ⏰
* add an option in config.ini that will allow you to change commit message
## problem? 🤖
open an issue and i'll get back to you!  
feel free to leave feature requests, bug reports, or any other thing you need to let me know about.
