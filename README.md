<h1 align="center">YTMENU</h1>
<br>
<p align="center">
<a href="https://github.com/demonkingswarn/ytmenu/stargazers"><img src="https://img.shields.io/github/stars/demonkingswarn/ytmenu?color=orange&logo=github&style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/graphs/contributors"><img src="https://img.shields.io/github/contributors/demonkingswarn/ytmenu?style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/releases/tag/v1.1.1"><img src="https://img.shields.io/github/v/tag/demonkingswarn/ytmenu?style=flat-square"> </a>
<a href="https://github.com/demonkingswarn/ytmenu/commits/master"><img src="https://img.shields.io/github/commit-activity/m/demonkingswarn/ytmenu?color=green&style=flat-square"></a>
<a href="https://matrix.to/#/#demonkingswarn:matrix.org"><img src="https://img.shields.io/static/v1?color=%230eb687&message=chat&logo=matrix&label=matrix&style=flat-square" alt="Discord"></a>
<br />
<a href="https://discord.gg/JF85vTkDyC"><img src="https://invidget.switchblade.xyz/JF85vTkDyC"></a>
<br />
 <i>A POSIX script that helps you find Youtube videos and opens/downloads them using mpv/youtube-dl</i>
 <br />
 <i>This project was inspired from <a href="https://github.com/pystardust/ytfzf">ytfzf</a>.</i> 
 <hr>
 </p>

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
* [`Credits`](#Credits)

---

# Dependencies

There is only 1 required dependency.

## Required dependency

* [`curl`](https://github.com/curl/curl)

## Recommended dependency

* [`mpv`](https://github.com/mpv-player/mpv) (the default video and audio player)

## Linux dependencies

* [`dmenu`](https://tools.suckless.org/dmenu) (the default menu selection screen)
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) (for downloading)

## MacOs Dependencies

* [`fzf`](https://formulae.brew.sh/formula/fzf#default) (the default menu selection screen)
* [`youtube-dl`](https://formulae.brew.sh/formula/youtube-dl#default) (for downloading)

# Install

1. Install the dependencies listed [above](#Dependencies)
2. Run the following commands

## Arch

```sh
yay -S ytmenu-git
```

## Other linux distros

```sh
sudo curl -sL "https://github.com/DemonKingSwarn/ytmenu/raw/main/ytmenu" -o /usr/local/bin/ytmenu
sudo chmod +x /usr/local/bin/ytmenu
```

## MacOs

```sh
sudo curl -sL "https://github.com/DemonKingSwarn/ytmenu/raw/main/ytmenu-mac" -o /usr/local/bin/ytmenu-mac
sudo chmod +x /usr/local/bin/ytmenu-mac
```

# Credits

| User           | Contributions                             | Donate|
| :---           | :---                                      | :--- |
| Pystardust 	| [contributions](./credits/pystardust.md) 	| |
| DemonKingSwarn    | [contributions](./credits/demonkingswarn.md)    ||
| Bugswriter 	| [contributions](./credits/bugswriter.md) | |
