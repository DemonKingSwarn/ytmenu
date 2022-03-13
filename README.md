<h1 align="center">YTMENU</h1>
<br>
<p align="center">
<a href="https://github.com/demonkingswarn/ytmenu/stargazers"><img src="https://img.shields.io/github/stars/demonkingswarn/ytmenu?color=orange&logo=github&style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/graphs/contributors"><img src="https://img.shields.io/github/contributors/demonkingswarn/ytmenu?style=flat-square"></a>
<a href="https://github.com/demonkingswarn/ytmenu/commits/main"><img src="https://img.shields.io/github/commit-activity/m/demonkingswarn/ytmenu?color=green&style=flat-square"></a>
<a href="https://matrix.to/#/#demonkingswarn:matrix.org"><img src="https://img.shields.io/static/v1?color=%230eb687&message=chat&logo=matrix&label=matrix&style=flat-square" alt="Discord"></a>
<br />
<a href="https://discord.gg/JF85vTkDyC"><img src="https://invidget.switchblade.xyz/JF85vTkDyC"></a>
<br />
 <i>A POSIX script that helps you find Youtube videos and opens/downloads them using mpv/youtube-dl</i>
 <br />
 </p>

---

# Table Of Contents

* [`Dependencies`](#Dependencies)
* [`Install`](#Install)
* [`Usage`](#Usage)
* [`Options`](#Options)
* [`Credits`](#Credits)
---

# Dependencies

There is only 1 required dependency.

## Required dependency

* [`curl`](https://github.com/curl/curl)

## Recommended dependency

* [`mpv`](https://github.com/mpv-player/mpv) (the default video and audio player)
* [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) (for downloading)

# Install

1. Install the dependencies listed [above](#Dependencies)
2. Run the following commands

## Arch

```sh
yay -S ytmenu-git
```

## Other linux distros & MacOs

```sh
curl -sL "https://github.com/DemonKingSwarn/ytmenu/raw/main/ytmenu" -o ~/.local/bin/ytmenu
chmod +x ~/.local/bin/ytmenu
```

# Usage

```
  ytmenu [-c]
  ytmenu [-v]
  ytmenu -h | -U | -V
```

# Options

```
-h show helptext
-v use VLC as the media player
-U fetch update from github
-V print version number and exit
-c search youtube
-d downloads the video
```

# Credits

| User           | Contributions                             | Donate|
| :---           | :---                                      | :--- |
| DemonKingSwarn    | [contributions](./credits/demonkingswarn.md) | 43Lmjz4PxuQCKh1mua6qj1Ti5HVDJU1ta6gzock4G3uSW4bb8FGADsSJ6GHhwBK6hLHyE2ARai9ijHsFW76rpRBkBzEg7Jp |
| Bugswriter 	| [contributions](./credits/bugswriter.md) | |
| thecashewtrader | [contributions](./credits/thecashewtrader.md) ||
