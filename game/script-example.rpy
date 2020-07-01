# 做 Mod 时，label 是个很重要的东西
label example_chapter:
    stop music fadeout 2.0

    scene bg club_day
    with dissolve_scene_full
    play music t3

    m "...[player]？"

    show monika 1 zorder 2 at t11
    m "你来了？"

    show monika 1b zorder 2 at t11
    m "欢迎来到新开张的 Mod 俱乐部！"

    show monika 3 zorder 2 at t11
    m "为了改写当时几近崩坏的故事，我才开了这个俱乐部的。"

    m 3l "讲真，以前我写的烂代码害了不少人..."
    m 3j "所以我才希望你改写这一切的。"

    m 2a "首先，恭喜你选择了正确的模板！"
    m 2b "如果你的母语是中文，那么就更棒了！你可以更尽情、更自然地发挥你的想象了！"
    $ config.developer = "auto"
    if config.developer:
        m 2b "诶？您已经选用了这个模板进行开发了？！"
        m 2j "太棒了！"
    else:
        m 2b "虽然你只是个玩家，但是学写 Mod 也不是不可以..."
        m "啊哈..."
        m "您可以在 {a=https://github.com/imgradeone/DDLCModTemplete-Chinese}这里{/a} 找到这个模板，改动世界线。"

    m 1a "接下来就是下载 DDLC，然后把 DDLC /game 文件夹下的东西丢进模板里了。你可以 {a=https://ddlc.moe/}点击这里{/a} 下载。"
    if config.developer:
        m 1b "诶，等一下，我忘记你已经看过 README 了..."
        m 1l "emm，无意冒犯（（（"
    else:
        m 1b "相信你也会做的吧。"

    m 1a "接下来需要下载 Ren'Py SDK，你可以 {a=https://www.renpy.org/release/6.99.12}点击这里{/a} 下载。"
    m 2a "而且必须是 6.99.12 版哦！"
    m "因为 DDLC 不兼容 Ren'Py 7，安装 Mod 时可能会有兼容性问题。"
    if config.developer:
        m 2j "不过我们现在准备得差不多了。"
    else:
        m 2a "调代码和打包时会用上它的。"

    m 1a "最后是最重要的，你需要下载中文字体包。"
    m 2a "毕竟这是这枚模板最关键的地方。"
    if config.developer:
        m 2j "但是，你肯定准备好了，不然你都见不到我，嘿嘿！"
    else:
        m 2a "这是让 Mod 更出彩的关键。"

    m 4a "既然准备完成了，那么就开始吧！"
    m 4b "首先，打开工程目录下的 /game 文件夹。"
    m 4c "看上去没什么东西的亚子。"
    m 4a "毕竟待会用到的东西都在 DDLC 那，所以也就没整这么多。"
    m "整多了，新人会晕的。"
    m 4k "你仅仅只需要改动世界线，写出你的故事！"
    m 4c "当然，如果你想把整个游戏都进行改动的话..."
    m 4b "当然可以！万能的 Ren'Py 会满足你的愿望的！"

    m 1j "等一下..."
    m 1k "我似乎忘记问你一个重要的问题..."
    m "...你的功底怎么样..."
    m 5 "啊哈...我居然这都能忘..."

    default knows_python = False
    default knows_renpy = False

    menu:
        m "你的写代码经验怎么样呢？"
        "开玩笑，我超强的，好不好？":
            $ experience_level = 2
            m 5 "纳尼？？？{nw}"
            scene bsod
            pause 3.0
            show monika 1m zorder 2 at t11
            m "..."
            m 1m "讲真，你也看到我写了那么多 bug 了..."
            m "那么，接下来，你就是我的师父！"
            hide bsod
            scene bg club_day
            show monika 2a zorder 2 at t11
            with dissolve_cg
        "我以前写过代码":
            $ experience_level = 1
            m 5 "可以啊。"
            show monika 1j zorder 2 at t11
            with Dissolve(0.3)
            m 1j "既然这样，写 DDLC Mod 也就非常简单了。"
        "我从来没写过啊...":
            $ experience_level = 0
            m 5 "纳尼？"
            m "你不会写代码？"
            m "其实也没事的啦~"
            show monika 1m zorder 2 at t11
            with Dissolve(0.3)
            m 1m "其实，我也是个小萌新..."
            m 1n "所以，讲真，当你的老师，我还是有那么一点点紧张的..."
            m "当然，其实问题也不大，我可以叫其他部员来帮忙。"
            m "我指的是以前文学部的那些呐~"
            m 1k "当然我也会尽全力帮助你写出自己的第一个 Mod 的！"

    if experience_level > 0:
        m 2a "既然你写过代码，那么你应该知道 DDLC 是使用 Ren'Py 这款好用的引擎制作的。"
        m "这款视觉小说引擎其实非常火，中国大陆也有专门讨论 Ren'Py 的社区。"
        m "而且，既然你玩过 DDLC 了，那么你应该也知道它有多么强大了吧。"
        m "我甚至可以知道你对角色文件干了什么..."
        m "..."
        m 3l "啊哈..."

        show monika 1a zorder 2 at t11

        menu:
            m "那么，你以前用过 Ren'Py 吗？"
            "用过。":
                $ knows_renpy = True
                m 1b "看来你已经轻车熟路了嘛。"
            "没有...":
                m 1e "emm，其实你也不用慌。"
                m 1b "因为 Ren'Py 真的超级简单！像中文模板作者这种从来没用过 Ren'Py 的人，都可以轻松驾驭。"
                m "所以，放轻松，有时事情没你想象中那么难。"

        m 3a "如果想让游戏更高端，你可能还需要了解 Python。"
        m 3c "因为，Ren'Py 其实就是使用 Python 构建的。"
        m "当然，你也不必惊慌，你现有的知识其实也足够了。"
        m 3j "但是，想要登上顶峰，还需要超强的本领，嘤。"

        show monika 1a zorder 2 at t11
        menu:
            m "你熟悉 Python 吗？"
            "很熟悉。":
                $ knows_python = True
                if not knows_renpy:
                    m 1a "那么接下来你应该可以很快地入门 Ren'Py 了。"
                    m 3a "但有时，Ren'Py 的 Python 又和常规的 Python 有点区别。"
                    m 3j "不过大可不必惊慌。"
                else:
                    m 1b "天哪，您太强了！"
                    m 1j "看来你马上就要成为站在顶峰的那个人了！"
                    m 1k "我已经迫不及待，想看到你的 Mod 了！"
            "没...":
                if not knows_renpy:
                    m 2c "其实，一丢丢的编程经验也很有帮助的。"
                    m 2a "Python 本身就是一个易于学习的语言呐。"
                else:
                    m 2d "[player]，别卖弱啦..."
                    m 2a "你既然驾驭了 Ren'Py，那么 Python 其实也不在话下了。"

    m 1c "接下来，我想知道你想做什么类型的 Mod。"
    m "一个项目到底有多复杂，取决于你的想法。"
    m 1d "你可以做出仅仅只有几个选项的互动小游戏，也可以颠覆整个游戏系统。"
    m 5 "这一切，取决于你。"

    menu:
        m "那么，你接下来计划做什么？"
        "基本的。":
            m 5 "从一个小项目开始？"
            show monika 3b zorder 2 at t11
            with Dissolve(0.3)
            m 3b "这其实是一个不错的起点！"
            m 3a "写视觉小说的脚本就和真正的出小说类似。"
            m 1m "但是，大家都在 DDLC 这片星球里呢！"
        "高级的。":
            m 5 "想来点高端的？"
            show monika 1e zorder 2 at t11
            with Dissolve(0.3)
            m 1e "那么，我会尽可能用上一些工具来帮助你的。"
            m 1k "没多久，你就可以做出成功的 Mod 了！"

    m 1a "接下来，我想知道你使用的是什么文本 / 代码编辑器。"
    m "因为中文模板作者使用的是 Visual Studio Code，这款优秀的文本编辑器。"
    m 1c "虽然你可以使用你喜欢的{b}任何一款{/b}文本编辑器来制作 Mod，但是这款内置的教程是使用 Visual Studio Code 制作的。"
    m "如果你没有使用 VS Code，也许会有那么一点点出入，但也不影响理解。"
    m "您可以 {a=https://code.visualstudio.com/}点击这里{/a} 下载 VS Code。"

    show monika 3a zorder 2 at t11

    menu:
        m "所以，你现在在使用什么文本编辑器呢？"
        "就是 Visual Studio Code！":
            m 1b "那可太棒了！"
            m "你现在已经和我在同一条路了！"
            m 1e "当然，你可能会意识到，VS Code 对于 Ren'Py 的代码高亮有那么一点点问题。"
            m 1a "不过，我们可以安装插件！"
            m "看到侧边栏上那几个方块状的图标了吧？那个就是 Marketplace。"
            m "点开它，然后在搜索框输入 \"RenPy\"。"
            m "然后找到 \"Ren'Py Language\" 插件，点击安装。"
            m "接下来，代码看上去就很舒服了！"
            m "您也可以 {a=https://marketplace.visualstudio.com/items?itemName=LuqueDaniel.languague-renpy}点击这里{/a} 进行安装。"
        "我用的是别的...":
            m 1l "其实也没事啦..."
            m "因为任何文本编辑器都可以做 Mod..."
            m "只是，代码高亮或许会有那么一点点折腾。"

    m "我顺便说一下，有时一个垃圾的编辑器会毁掉你的 Mod 工程。"
    m "有些太老的、不维护的文本编辑器，可能会没那么好用。"
    m "而且，由于这是中文模板，所以你需要一个对中日韩输入法友好的编辑器。"
    m "所以，Ren'Py 6 时代的 Editra 就不合适了。"
    m "当然，HBuilder 其实也可以编辑，但需要手动设置 Python 高亮。"
    m "对于我，我会强烈推荐 Visual Studio Code、Atom 这类现代的文本编辑器。"
    m 5 "而且 Atom 是 Ren'Py 7 官方推荐的编辑器哦！您可以 {a=https://atom.io/}点击这里{/a} 下载 Atom。"
    m 3a "如果你实在讨厌微软，却又喜欢 VS Code，你可以尝试社区的 VSCodium。您可以 {a=https://vscodium.com/}点击这里{/a} 下载 VSCodium。"
    m 1b "最后，再强调一下，你可以使用 任何 编辑器。"
    m "{s}但是，使用的编辑器不恰当，小心被谴责哦！（逃）{/s}"# 我说的是那个在自家论坛开抵制自家编辑器板块的那个 XD #donhonmsl

    m 1a "其实我刚刚问你的那些问题，不会影响到接下来的教程..."
    m 2b "但是，我知道你要做什么类型的 Mod 了。"
    m 2a "那么，我们就可以开始一起学习了！"
    m "相信你很快就能做出一个好玩的 Mod 了！"
    m "当然，在此之前，一定要看好 README 哦！"

    $ persistent.example_seen = True

    jump tutorial_selection

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
