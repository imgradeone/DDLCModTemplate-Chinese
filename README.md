# 嘿，你想用中文写 DDLC Mod？那你来对地方了！

这里是 DDLC 中文 Mod 模板！本模板基于 Monika After Story 团队的 [DDLCModTemplate](https://github.com/Monika-After-Story/DDLCModTemplate)，并进行了一系列汉化，以及功能追加。使用本模板制作 Mod 时，请遵循 [Team Salvato 的 IP Guidelines](http://teamsalvato.com/ip-guidelines/)。

本模板实际上是从 [Inside The Dark Mod](https://github.com/imgradeone/InsideTheDark) 的中文版中衍生出来的。

> 请注意：当前版本的中文模板可能尚不完善，且**尚对繁体中文缺乏支持**。部分 GUI 元素暂未被汉化。

## 中文字体

中文版 DDLC Mod 模板使用了一些免费商用的中文字体，在此致谢。**开始 Mod 开发之路前，请务必下载这些字体，否则将无法启动工程。安装方式见 #中文字体包安装 小节。**

如有需要，您也可以自行修改配置文件，以自定义字体，**但请自主承担版权风险**。

### 阿里巴巴 / 阿里巴巴普惠体
单独下载：https://ics.alibaba.com/project/Hn8mXx 或者 https://alibabafont.taobao.com/ （均需要登录淘宝帐号）

使用字重：Regular

文件存放于 `game\mod_assets\font\alipuhuireg.ttf`

用途：游戏文字主要字体，替代原有的 Aller 字体

### 站酷字体 / 站酷快乐体
单独下载：https://www.zcool.com.cn/special/zcoolfonts/ （记得转到免费字体区）

文件存放于 `game\mod_assets\font\zcoolkuaile.ttf`

用途：按钮、角色名使用字体

### 杨任东字体 / 杨任东竹石体
单独下载：关注“杨任东字体”微信公众号，回复 `字体`

使用字重：Regular

文件存放于 `game\mod_assets\font\zhushi.ttf`

用途：Yuri 写信字体，设置项字体，用于替代字体 `y1`（Yuri 的默认写信字体）

### Adobe、Google 等 / 思源宋体
单独下载：https://source.typekit.com/source-han-serif/cn/

中国大陆用户推荐从 [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/adobe-fonts/source-han-serif/) 按需要的语言（简体中文 / 繁体中文）获取。

使用字重：Regular

语言：简体中文

文件存放于 `game\mod_assets\font\sourcehanserif.ttf`

用途：`edited` 文本框风格使用字体（即类似 Natsuki 说 `fxxking monikammmmmmm` 时的样式）

## 中文字体包安装

> 请注意：我们仍然建议您从各个字体的官网下载这些字体，即便它们都是免费商用字体。

您可以下载懒人专用字体包，下载完后将字体解压到 `game/mod_assets/font` 目录下即可。

您可以从以下地方获取 Mod 模板的中文字体包（v1.0）：

### 中国大陆地区用户

[奶牛快传（链接会于 2020-08-31 过期）](https://imgradeone.cowtransfer.com/s/5bebe9222be64e) | [蓝奏云](https://imgradeone.lanzous.com/icxhqqj) | [百度网盘 提取码 6b8z](https://pan.baidu.com/s/1LTv9N1Yfmd3cQsFTAoOSQA) | [城通网盘（仅供赞助用途，实际体验差）](https://ct.imgradeone.xyz/file/24390393-446444253)

<details>
  <summary>百度网盘用户亦可点击展开扫描小程序码下载</summary>
  
  ![](./bdwp-dl-code.png)

</details>

### 其他地区用户

[MEGA（可能我的 MEGA 流量额不足以支撑下载，佛系吧）](https://mega.nz/file/1QwHkTga#N9yvUtQHAvqQ2szeJvhFT3CJdzL7elxfbR4AeFuAcb0) | [MediaFire](https://www.mediafire.com/file/4aciv23rhf5x8kg/font.zip/file) | [Google 云端硬盘](https://drive.google.com/open?id=1b96aSF7A6VtIh4-XuJfaEFHhVpsQZQzw)

## 下载 Demo

您可以在 [Releases 页面](https://github.com/imgradeone/DDLCModTemplete-Chinese/releases) 获取 Demo。

## 开始使用模板

1. 去 Ren'Py 官网下载 [Ren'Py SDK 6.99.12](https://www.renpy.org/release/6.99.12)。**注意：由于模板历史原因和兼容性考虑，请务必使用 Ren'Py SDK 6.99.12 进行 Mod 制作，不要使用 Ren'Py SDK 7，这会导致 Mod 出现兼容性问题。**
1. 前往 Releases 页面下载稳定版模板。如需开发版，可以点击页面上的 Clone & Download。当然，我们已经将此 Repo 设置为模板 Repo，所以你也可以点击绿色的 `Use this template`，然后使用开发版模板创建新 Repo，再 Clone 到本地。
1. 将模板文件解压到刚刚你解压 Ren'Py SDK 的文件夹里，或者在你指定的工程目录里。（默认情况下，`renpy-6.99.12.4-sdk`）
1. 前往 [DDLC.moe](https://ddlc.moe) 或者 Steam 下载 DDLC 游戏本体，并将游戏目录下 `game` 文件夹内的 `audio.rpa`、`images.rpa` 和 `fonts.rpa` 复制到工程文件夹（即你解压模板文件的地方）。（千万不要把 `scripts.rpa` 一并复制过去，会出现冲突）
1. 下载中文字体包，请查看 [中文字体](#中文字体) 小节。
1. 现在，打开 Ren'Py SDK，启动工程。正常情况下，工程将会完美启动。如果出错，请检查有没有忘记导入什么东西。
1. 接下来，开始你的写 Mod 之旅吧！

> 注意：写 Mod 的时候，如果有额外资源，请务必存放在 `mod_assets` 文件夹，否则打包时资源将不会被包含在内。

## 打包 Mod

1. 打开 Ren'Py SDK，点击 “Build Distributions” / “生成分发版”。
1. 在 “Build Packages:” / “生成分发包：” 选项中勾选 “DDLC Compatible Mod”，然后开始构建。
1. 构建完成后，系统将自动打开文件管理器，展示打包后的 Mod。建议先自行安装 Mod 并测试后，再分发到各个平台。

## 模板功能

原版有啥就有啥 XD

## 特色功能

1. 绝赞中文化（目前是简体中文）
1. 绝赞字体优化
1. ~~绝赞咕咕咕~~
1. 默认在 `/characters` 文件夹下保留所有 `.chr` 文件，全角色厨的福利
1. 首次启动 Mod 时加入“不同意”选项

## 注意事项

由于这是 Mod 模板，因此如果你是 Mod 作者，请不要将 DDLC 游戏本体包含在你分发的 ZIP 里，这是违反 IP Guidelines 的行为。

## TODO

- [ ] 教程翻译
- [ ] 补充原模板没有的功能，如 `ghostmenu`

## 特别感谢

- Team Salvato http://teamsalvato.com / https://ddlc.moe
- Monika After Story Team http://www.monikaafterstory.com
- 所有中文字体作者
