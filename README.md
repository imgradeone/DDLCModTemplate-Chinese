# DDLC 中文 Mod 模板
嘿，你想用中文写 DDLC Mod？**那你来对地方了！**

这里是 DDLC 中文 Mod 模板！本模板基于 Monika After Story 团队的 [DDLCModTemplate](https://github.com/Monika-After-Story/DDLCModTemplate)，并进行了一系列汉化，以及功能追加。使用本模板制作 Mod 时，请遵循 [Team Salvato 的 IP Guidelines](http://teamsalvato.com/ip-guidelines/)。

本模板实际上是从 [Inside The Dark Mod](https://github.com/imgradeone/InsideTheDark) 的中文版中衍生出来的。

> 请注意：当前版本的中文模板可能尚不完善，且**尚缺乏繁体中文支持**。部分 GUI 元素暂未被汉化。

## 中文字体

中文版 DDLC Mod 模板使用了一些免费商用的中文字体，在此致谢。**开始 Mod 开发前，请务必下载这些字体，否则将无法启动工程。安装方式见 [中文字体包安装](#中文字体包安装) 小节。**

如有需要，您也可以自行修改配置文件，以自定义字体，**但请自主承担版权风险**。

中文字体详情请查看 [这里](./game/mod_assets/font/README.md)

## 中文字体包安装

> 请注意：我们仍然建议您从各个字体的官网下载这些字体，即便它们都是免费商用字体。

您可以下载懒人专用字体包，下载完后将字体解压到 `game/mod_assets/font` 目录下即可。

当前版本字体包：v1.2

对应支持模板 v1.2 版本，不支持模板 v1.0 ~ v1.1

您可以从以下地方获取 Mod 模板的中文字体包（v1.2）：

### 中国大陆地区用户

[奶牛快传（链接会于 2020-10-01 过期）](https://imgradeone.cowtransfer.com/s/3852906fbdf246) | [蓝奏云](https://imgradeone.lanzous.com/iwq7wec3j7a) | [百度网盘 提取码 hi2j](https://pan.baidu.com/s/1WiO1qD8cI8U1YTEVeVrkuQ) | [城通网盘（仅供赞助用途，实际体验差）](http://ct.imgradeone.xyz/file/24390393-452015477)

### 其他地区用户

[MediaFire](http://www.mediafire.com/file/6juwd7h0venrg7f/font%25282%2529.zip/file) | [Google 云端硬盘](https://drive.google.com/file/d/1LClyzgxq-les-N5egLXm1aK7ULATDpex/view?usp=sharing) | GitHub (later)

## 下载 Demo

您可以在 [Releases 页面](https://github.com/imgradeone/DDLCModTemplete-Chinese/releases) 获取 Demo。

## 开始使用模板

1. 去 Ren'Py 官网下载 [Ren'Py SDK 6.99.12](https://www.renpy.org/release/6.99.12)。**注意：由于模板历史原因和兼容性考虑，请务必使用 Ren'Py SDK 6.99.12 进行 Mod 制作，不要使用 Ren'Py SDK 7，这可能会导致 Mod 出现兼容性问题。** <!-- 因 Mod 而异 -->
2. 前往 Releases 页面下载稳定版模板。如需开发版，可以点击页面上的 "Clone" -> "Download ZIP"。当然，我们已经将此 Repo 设置为模板，所以你也可以点击绿色的 `Use this template`，然后使用开发版模板创建新 Repo，再 Clone 到本地。
3. 将模板文件解压到刚刚你解压 Ren'Py SDK 的文件夹里，或者在你指定的工程目录里。（默认情况下，是 `renpy-6.99.12.4-sdk`）
4. 前往 [DDLC.moe](https://ddlc.moe) 或者 Steam 下载 DDLC 游戏本体，并将游戏目录下 `game` 文件夹内的 `audio.rpa`、`images.rpa` 和 `fonts.rpa` 复制到工程文件夹（即你解压模板文件的地方）。（千万不要把 `scripts.rpa` 一并复制过去，会出现冲突）
5. 下载中文字体包，请查看 [中文字体](#中文字体) 小节。
6. 现在，打开 Ren'Py SDK，启动工程。正常情况下，工程将会完美启动。如果出错，请检查有没有忘记导入什么东西。
7. 接下来，开始你的写 Mod 之旅吧！

> 注意：写 Mod 的时候，如果有额外资源，请务必存放在 `mod_assets` 文件夹，否则打包时资源将不会被包含在内，除非你自定义 `options.rpy`。

## 打包 Mod

1. 打开 Ren'Py SDK，点击 “Build Distributions” / “生成分发版”。
1. 在 “Build Packages:” / “生成分发包：” 选项中勾选 “DDLC Compatible Mod”，然后开始构建。
1. 构建完成后，系统将自动打开文件管理器，展示打包后的 Mod。建议先自行安装 Mod 并测试后，再分发到各个平台。

## 模板特色功能

1. 绝赞中文化（目前是简体中文）
1. 绝赞字体优化
1. ~~绝赞咕咕咕~~
1. 默认在 `/characters` 文件夹下保留所有 `.chr` 文件，全角色厨的福利
1. 首次启动 Mod 时加入“不同意”选项
1. Doki Doki Mod Manager 联动

## 注意事项

由于这是 Mod 模板，因此如果你是 Mod 作者，请不要将 DDLC 游戏本体包含在你分发的 ZIP 里，这是违反 IP Guidelines 的行为。

## TODO

- [ ] 教程翻译
- [ ] 恢复原模板移除的功能，如 `ghostmenu`
- [ ] Ren'Py 7 支持（有生之年？）
- [ ] 无尽存档位按钮展示
- [ ] 成就支持（原生 + DDMM）

## 特别感谢

- Team Salvato http://teamsalvato.com / https://ddlc.moe
- Monika After Story Team http://www.monikaafterstory.com
- 所有中文字体作者
- Sayo-nika Team
- Doki Doki Mod Manager Team

## 开源许可

本模板采用 [Sayo-nika 的 GitHub Action](https://github.com/Sayo-nika/quickstart-actions) 进行远程 Mod 构建，在此致谢。

本 Mod 模板需要使用 Ren'Py。Ren'Py 包含自由软件许可中的一些许可证，包括 GNU 宽通用公共许可证。  
Ren'Py 由一系列开源组件构成，它们的开源协议可以在 https://www.renpy.cn/doc/license.html （简体中文）或 https://www.renpy.org/doc/html/license.html （英文）查看。

本模板基于 Monika After Story 团队的 [DDLCModTemplate](https://github.com/Monika-After-Story/DDLCModTemplate)。

本模板属于粉丝作品，遵循 Team Salvato IP Guidelines。

## 加入社区

[Telegram 频道](https://t.me/DDLCModCN)