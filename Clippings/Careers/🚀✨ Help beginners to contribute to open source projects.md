---
title: "firstcontributions/first-contributions: 🚀✨ Help beginners to contribute to open source projects"
source: "https://github.com/firstcontributions/first-contributions#first-contributions"
author:
  - "[[lokashakthivel-sp]]"
published:
created: 2026-03-09
description: "🚀✨ Help beginners to contribute to open source projects - firstcontributions/first-contributions"
tags:
  - "clippings"
---
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/firstcontributions/first-contributions?resume=1)

## First Contributions

This project aims to simplify and guide the way beginners make their first contribution. If you are looking to make your first contribution, follow the steps below.

*If you're not comfortable with command line, [here are tutorials using GUI tools.](https://github.com/firstcontributions/#tutorials-using-other-tools)*

[![fork the repository](https://camo.githubusercontent.com/42b18e612219cae827d8c4ee97bf15ec971f271fe60789e73a8aaeeeb42eb73f/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f666f726b2e706e67)](https://camo.githubusercontent.com/42b18e612219cae827d8c4ee97bf15ec971f271fe60789e73a8aaeeeb42eb73f/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f666f726b2e706e67)

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

[![clone the repository](https://camo.githubusercontent.com/d4bafe4b6b8db07be80cb5d74070c2fb8ec18559711ad85ab3ae2bc576e1e9bc/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67)](https://camo.githubusercontent.com/d4bafe4b6b8db07be80cb5d74070c2fb8ec18559711ad85ab3ae2bc576e1e9bc/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67)

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button, then on SSH tab and then click the *copy url to clipboard* icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

[![copy URL to clipboard](https://camo.githubusercontent.com/fe81d0584418cc04c31a477538ec11825bceb285d865f5c34dff84180fb5adeb/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f70792d746f2d636c6970626f6172642e706e67)](https://camo.githubusercontent.com/fe81d0584418cc04c31a477538ec11825bceb285d865f5c34dff84180fb5adeb/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f70792d746f2d636c6970626f6172642e706e67)

For example:

```
git clone git@github.com:this-is-you/first-contributions.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

Change to the repository directory on your computer (if you are not already there):

```
cd first-contributions
```

Now create a branch using the `git switch` command:

```
git switch -c your-new-branch-name
```

For example:

```
git switch -c add-alonzo-church
```
**If you get any errors using git switch, click here:**

If the error message "Git: `switch` is not a git command. See `git –help` " appears, it's likely because you're using an older version of git.

In this case, try to use `git checkout` instead:

```
git checkout -b your-new-branch-name
```

Now open `Contributors.md` file in a text editor, add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file.

[![git status](https://camo.githubusercontent.com/f4e28238c2321744c1488e34da1b0a439e91d12a9ce67f5d0fc425baead200c4/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)](https://camo.githubusercontent.com/f4e28238c2321744c1488e34da1b0a439e91d12a9ce67f5d0fc425baead200c4/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add Contributors.md
```

Now commit those changes using the `git commit` command:

```
git commit -m "Add your-name to Contributors list"
```

replacing `your-name` with your name.

Push your changes using the command `git push`:

```
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

**If you get any errors while pushing, click here:**
- ### Authentication Error
	```
	remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
	remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
	fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
	```
	Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.
	Also, you might want to run 'git remote -v' to check your remote address.
	If it looks anything like this:
	```
	origin    https://github.com/your-username/your_repo.git (fetch)
	origin    https://github.com/your-username/your_repo.git (push)
	```
	change it using this command:
	```
	git remote set-url origin git@github.com:your-username/your_repo.git
	```
	Otherwise you'll still get prompted for username and password and get authentication error.

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

[![compare and create pull request](https://camo.githubusercontent.com/af350925874cc9d92469b7800b819295f2b8da906486a169b54a874a30d75ded/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67)](https://camo.githubusercontent.com/af350925874cc9d92469b7800b819295f2b8da906486a169b54a874a30d75ded/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67)

Now submit the pull request.

[![submit pull request](https://camo.githubusercontent.com/87bc1d6af5a0c15e6ed798ff80fe57efe8a145c47e98ba16245350ebdfd13007/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67)](https://camo.githubusercontent.com/87bc1d6af5a0c15e6ed798ff80fe57efe8a145c47e98ba16245350ebdfd13007/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67)

Soon I'll be merging all your changes into the main branch of this project. You will get a notification email once the changes have been merged.

Congrats! You just completed the standard *fork -> clone -> edit -> pull request* workflow that you'll often encounter as a contributor!

Celebrate your contribution and share it with your friends and followers by going to [web app](https://firstcontributions.github.io/#social-share).

If you'd like more practice, checkout [code contributions](https://github.com/roshanjossey/code-contributions).

Now let's get you started with contributing to other projects. We've compiled a list of projects with easy issues you can get started on. Check out [the list of projects in the web app](https://firstcontributions.github.io/#project-list).

### Additional material

| [![GitHub Desktop](https://camo.githubusercontent.com/ecb4871e94f4d94998f674d8cf7761bffb0f9b40a1b63f9c70eadd78efbcc852/68747470733a2f2f6465736b746f702e6769746875622e636f6d2f696d616765732f6465736b746f702d69636f6e2e737667)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-desktop-tutorial.md) | [![Visual Studio 2017](https://camo.githubusercontent.com/98064572bfd8c99eef134e5bd68cdc59c00cef9a8ccd2228f6da95f5e217011a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f632f63642f56697375616c5f53747564696f5f323031375f4c6f676f2e737667)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [![GitKraken](https://camo.githubusercontent.com/0e86acff6fc241f6a829b9ccaad48f7d0dddc77fea7edf718e81bee63682f60e/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f6775692d746f6f6c2d7475746f7269616c732f6769746b72616b656e2d7475746f7269616c2f676b2d69636f6e2e706e67)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/gitkraken-tutorial.md) | [![VS Code](https://camo.githubusercontent.com/55159da6ec9bfa5ab578098c38cb2f069f9134a47b3a4d5fe009fd31b72826bf/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f312f31632f56697375616c5f53747564696f5f436f64655f312e33355f69636f6e2e706e67)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [![Sourcetree App](https://camo.githubusercontent.com/92c979ff222ccc7ac82b7c9a447fc35b4b77c94be470e2915ef519b567e195d4/68747470733a2f2f7761632d63646e2e61746c61737369616e2e636f6d2f64616d2f6a63723a38316231356364652d626532652d346634612d386166372d3934333666346131623433312f536f75726365747265652d69636f6e2d626c75652e737667)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/sourcetree-macos-tutorial.md) | [![IntelliJ IDEA](https://camo.githubusercontent.com/266cafcd012290bec5211f89b4dfea2afbd004b1efa1ec4af1f326462cebcbe0/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f392f39632f496e74656c6c694a5f494445415f49636f6e2e7376672f35313270782d496e74656c6c694a5f494445415f49636f6e2e7376672e706e67)](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-intellij-tutorial.md) |
| --- | --- | --- | --- | --- | --- |
| [GitHub Desktop](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-desktop-tutorial.md) | [Visual Studio 2017](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-vs2017-tutorial.md) | [GitKraken](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/gitkraken-tutorial.md) | [Visual Studio Code](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-vs-code-tutorial.md) | [Atlassian Sourcetree](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/sourcetree-macos-tutorial.md) | [IntelliJ IDEA](https://github.com/firstcontributions/first-contributions/blob/main/docs/gui-tool-tutorials/github-windows-intellij-tutorial.md) |

## Sponsor this project

[**firstcontributions** First Contributions](https://github.com/firstcontributions)

[Sponsor](https://github.com/sponsors/firstcontributions)

[Learn more about GitHub Sponsors](https://github.com/sponsors)

## Deployments 42

- [github-pages](https://github.com/firstcontributions/first-contributions/deployments/github-pages)

[\+ 41 deployments](https://github.com/firstcontributions/first-contributions/deployments)