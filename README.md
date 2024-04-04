# cintel-06-custom
Project 6 CI


# Environment Setup 

### Start a new project repository in GitHub and then clone down to local machine. I leveraged VS Code clone functionality

### Create Virtual Environment

```shell

py -m venv .venv
.venv\Scripts\Activate
```

### Create .gitignore file
```shell
ni .gitignore
```
add .venv/ to .gitignore file to not be tracked in github

### Add requirements folder

```shell

ni requirements.txt
py -m pip install -r requirements.txt
```

# Install and Setup the Project

### Freeze dependencies

```shell

py -m pip freeze > requirements.txt
```

# Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser dashboard/app.py
```

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a browser to <http://[::1]:8008/> and test the Pages app.

Export to docs folder and test GitHub Pages locally.

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```

### Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```

## Enable GitHub Pages

Go to your GitHub repo settings and enable GitHub Pages for the docs folder.

## Import dependencies

## Develop reactive calc

## Create template

## Develop inputs

## Develop sidebar

## Develop main page content



