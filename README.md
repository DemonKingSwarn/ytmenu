<p align="center">
<b>YTMENU</b>
</br>
<a href="https://github.com/demonkingswarn/ytmenu/stargazers"><img src="https://img.shields.io/github/stars/demonkingswarn/ytmenu?color=orange&logo=github&style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/graphs/contributors"><img src="https://img.shields.io/github/contributors/demonkingswarn/ytmenu?style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/commits/master"><img src="https://img.shields.io/github/commit-activity/m/demonkingswarn/ytmenu?color=green&style=flat-square"></a>
<a href="https://discord.gg/Kzgv8XRt4a"><img src="https://img.shields.io/discord/947394369198116864?color=yellow&logo=discord&style=flat-square" alt="Discord"></a>
<br>
 <i>A POSIX script that helps you find Youtube videos and opens/downloads them using mpv/youtube-dl</i>
 <hr>
 </p>
<p align="center">
This script is a simpler version of <a href="https://github.com/pystardust/ytfzf">ytfzf</a>.

<h1 align="center">
	This is a little showcase
</h1>
<p align="center">
<img src=./assets/output.gif width="100%">
</p>

---

# Table Of Contents

* [`Dependencies`](#Dependencies)
* [`Install`](#Install)

---

# Dependencies

There are only 1 required dependency.

## Required dependency

* [`curl`](https://github.com/curl/curl)

## Recommended dependencies

* [`mpv`](https://github.com/mpv-player/mpv) (the default video and audio player)
* [`dmenu`](https://tools.suckless.org/dmenu) (the default menu selection screen)

## Optional dependency

* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) (for downloading)

## MacOs Dependencies

* [`fzf`](https://formulae.brew.sh/formula/fzf#default) (the default menu selection for mac)
* [`youtube-dl`](https://formulae.brew.sh/formula/youtube-dl#default) (for downloading)

# Install

1. Install the dependencies listed [above](#Dependencies)
2. Run the following commands

## Arch or Arch based distros

```sh
yay -S ytmenu-git
```

## Other linux distros

```sh
git clone https://github.com/demonkingswarn/ytmenu
cd ytmenu
sudo cp ytmenu /usr/local/bin/ytmenu
```

## MacOs

```sh
git clone https://github.com/demonkingswarn/ytmenu
cd ytmenu
sudo cp ytmenu-mac /usr/local/bin/ytmenu-mac
```
