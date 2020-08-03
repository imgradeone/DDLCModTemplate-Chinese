init python:

    items = [
        (_("重播初始介绍"),"example_chapter"),
        (_("序：中文模板特典"),"chinese_mod"),
        (_("第 1 关：从第一个 label 开始"),"tutorial_route_p1"),
        (_("第 2 关：第一句对话"),"tutorial_route_p2"),
        (_("第 3 关：背景也要丰富"),"tutorial_route_p3"),
        (_("第 4 关：没有 BGM 的 Mod 是没有灵魂的"),"tutorial_route_p4"),
        (_("Route Part 5, Menu"),"tutorial_route_p5"),
        (_("Route Part 6, Logic Statement"),"tutorial_route_p6"),
        (_("Route Part 7, Sprite"),"tutorial_route_p7"),
        (_("Route Part 8, Position"),"tutorial_route_p8"),
        (_("Route Part 9, Ending"),"tutorial_route_p9"),
        (_("来点高级点的！"),"tutorial_route_adv")
    ]

# TODO: 中文版教程

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)

define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#000"
define gui.tutorial_button_text_hover_color = "#fa9"


style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []




screen tutorial_choice(items):
    style_prefix "tutorial"

    fixed:

        area (125, 40, 600, 450)

        bar adjustment adj style "vscrollbar" xalign -0.05

        viewport:
            yadjustment adj
            mousewheel True

            has vbox

            for i_caption,i_label in items:
                textbutton i_caption:
                    action Return(i_label)

            null height 20

            textbutton _("谢谢，这些已经足够了。") action Return(False)





label tutorial_selection:

    stop music fadeout 2.0


    scene bg club_day
    with dissolve_scene_full
    play music t3

label tutorial_selection_menu:

    show monika 3a at tcommon(950)
    window show
    $ m(_("接下来我们该学些什么呢？"), interact=False)

    call screen tutorial_choice(items)
    window auto

    if _return == False:
        jump end_tutorial

    call expression _return from _call_expression

    jump tutorial_selection_menu



label end_tutorial:

    show monika 4a zorder 2 at t11

    m "好的喵，感谢您的聆听。"
    m 5a "咱们下次见~！"

    with dissolve

    return

label chinese_mod:

    show monika at thide zorder 2
    hide monika

    show sayori 1a at t11 zorder 2
    s "好的，作为前文学部副部长，我来代表中文模板作者发一下言吧。"
    s 1d "感谢您下载、使用这款中文 DDLC Mod 模板。"
    s "其实，当我在各种社区，像 Reddit、Discord、百度贴吧，还有比较大的 Mod 网站 DDLCMods.com 里看到许多 Mod 的时候，我很感动。"
    s "许多粉丝都在改写原本悲惨的 DDLC 宇宙，让我们还能一直陪着你。"
    s 1l "感谢那些 Mod 作者，让我，还有可爱的 Natsuki，优雅的 Yuri，还有部长 Monika 度过更美妙的日常。"
    s 1k "但是，我总感觉，有些事情不太对。"
    s "因为，我很少看到过中文的原创 Mod。"
    s 1d "所以，这个 Mod 模板其实也是为了中文 DDLC Mod 的低迷现状。"
    s "希望这款 Mod 模板可以帮助你少走点弯路。"
    s "最后，感谢 Team Salvato 和画师们的努力。"
    s "同时也感谢 Monika After Story 团队制造出原版 Mod 模板。"
    s "Monika After Story 也是高人气的 DDLC Mod，让你和 Monika 度过更美妙的日常。"
    s 5a "感谢你的选择！祝写 Mod 愉快！"
    show sayori at thide zorder 2
    hide sayori

    return


label tutorial_route_p1:

    show monika 2a zorder 2 at t11

    m "一个 Mod 的根，就是一个小小的 label。"
    m "没有它，Ren'Py 就没法让我们享受充满交互感的游戏。"
    m "那么 label 到底是什么呢？"
    m "简单来说，label 就是一个脚本集，游戏就是通过一个个 label 实现各种操作逻辑的。"
    m "通过 jump、call 来呼唤这些 label，游戏就会加载出正确的内容。"
    m "那么知道了 label 这种东西的含义后，我们就可以开始写 Mod 了。"
    m 2c "但是写 Mod 时，你还需要当心。"
    m "因为一个错误，有可能导致 Mod 无法运行。"
    m "而且由于技术力限制，你可能很难找到错误所对应的地方。"
    m "还请大佬能给个 Pull Request 进行解决呐..."
    m 3a "接下来，我们就可以做一个 Mod 了！"
    m 1a "不过，既然大家都要虚心，那么咱们还是来点简单的吧。"
    m 1h "因为我没有能直接调用 Ren'Py 的超能力，所以你一定要跟紧我啊！"
    m "首先，我也知道你已经跟着 README 一步步做了。"
    m "那么，给你的工程文件夹命名吧！我们这里以 \"Forever Life\" 为例。"
    m 2a "接下来，你可以直接把 'tutorial.rpy' 和 'tutorial.rpyc' 删掉了。它们只是这个教程的组成部分，接下来用不到。当然，你也可以留着。"
    m 3a "接下来用你最爱的编辑器打开 'script.rpy' 这个文件。"
    m "跳转到第 22 行。你应该可以看到我贴心的注释。接下来，你只需要改动第 26 - 29 行，也就是注释包住的地方。"
    m "接下来，删掉这几行，然后新开一行。你可能需要再打 4 个空格。"
    m "如果你使用 VS Code，那么它应该就已经把 4 个空格的缩进整好了。实在没有，可以按 Tab 键补全。"
    m "输入：\n' \ \ \ call meet_monika'\n（不要把引号也打进去）"
    m "顺便插一句嘴：Python 对空格十分敏感，所以一定要记得空格！"
    m "而且，传统的“Tab”缩进会导致 Mod 罢工哦！"
    m 1j "...抱歉，扯远了..."
    m "接下来，保存文件。"
    m 3a "然后，再新建一个文件，命名为 'meet_monika.rpy'，记得扩展名！"
    m "顺便，.rpy 文件就是 Ren'Py 里的脚本源代码文件。"
    m "打开刚刚创建的文件，输入：\n'label meet_monika:'"
    m "换行，然后：\n' \ \ \ return'"
    m "保存。"
    m 4i "好的，这就是一个异常简单的，啥都没有的 label 了！"
    m 1a "接下来，我就解释一下 Ren'Py 的跳转逻辑吧。"
    m 3a "你刚刚写的 call meet_monika 其实就是一个跳转到 label 'meet_monika' 的操作。"
    m "在 Ren'Py 里，跳转可以使用 call 或者 jump，但两者有很大不同。"
    m "call 相当于打开一个新的子窗口，可以通过 return 来返回上一级。"
    m "但 jump 相当于在当前页面打开新页面，return 之后就相当于整个窗口被关掉。"
    m 1a "至于 call 后面加 from 从句的事情，反正我懒得做，毕竟打包时 Ren'Py 会自动补全的。"
    m 4b "但是，如果你直接着急地尝试自己的 Mod，恐怕你只能在主菜单反复横跳，因为刚刚的 label 没有东西。"
    m "如果出现报错，你有可能需要检查一下自己有没有打错什么东西，毕竟我动不了你的文本编辑器..."
    m 2a "不过，如果你还是没法解决的话，那么可以去 answers 文件夹里找到答案喵。"
    m "顺便解释一下那些带井号的东西：它们是 Python 里的注释。为了避免冲突，我就暂时把这些东西注释掉了。"
    m 5a "好的，这就是第 1 关了！消化一下，咱们第 2 关见！"

    return

label tutorial_route_p2:

    show monika 5a zorder 2 at t11

    m "欢迎回来，[player]！"
    m 1l "上一关是不是有那么一点点难..."
    m "啊哈..."
    m "我保证这关比上一关简单。"
    m 3a "视觉小说和一般的小说一样，是需要剧本的。"
    m "而在 Ren'Py 里，剧本就是靠对话脚本实现的！"
    m 3l "听到脚本这个词，也别慌..."
    m "Ren'Py 的脚本编写其实非常容易！"
    m 3b "接下来，跟着我开始写对话吧！"
    m "打开上一关创建的 meet_monika.rpy 文件。"
    m "在 label 行和 return 之间输入："
    m " \ \ \ mc \"DDLC 太好玩了!\""
    m "再换一行，然后："
    m " \ \ \ y \"就是啊，Monika 多可爱啊！\""
    m 1l "..."
    m "这是不是有点道德绑架啊..."
    m "算了，现在只是学习怎么写 Mod，之后正式开写 Mod 的时候你可以自己编写。"
    m 3b "接下来保存文件，然后再去 Ren'Py 启动器打开工程，开始新游戏。"
    m 1a "这时你应该看到了你和 Yuri 的一段简短的对话。"
    m 5 "这下连 Yuri 都觉得我是可爱的人啦~"
    menu:
        m "你说是不是啊？"
        "是的呐":
            pass
        "反正我也莫得选择，是的呐":
            pass

    m 1j "好呀！"
    m "谢谢你这么爱我！"
    show yuri 3y7 at t22 zorder 2 
    show monika at t21 zorder 2
    y "嘿，不带你这么玩的！"
    m 1m "..."
    m 1n "emm..."
    m "Yuri..."
    m "我只是教 [player] 做 Mod 而已啊..."
    y "..."
    y 1 "..."
    y eyesfull "好吧，我就当无事发生。"
    m "不是..."
    m "你为什么要用这种来自三次元的眼神来看我，还有屏幕前的玩家..."
    m 5b "你把人家 [player] 吓到了！"
    show monika at t11 zorder 1
    menu:
        m "对吧？"
        "确实...":
            pass
    show monika at t21 zorder 2
    y 1 "..."
    show yuri 4e at h22 zorder 2
    y "啊！"
    y "抱歉...无意冒犯..."
    show yuri at thide
    hide yuri
    show monika at t11 zorder 2
    m "唔..."
    m "那咱们还是了解一下关于对话的东西吧。"
    m 3a "每句对话开始前，你需要指定说话的角色。"
    m "你输入的 'mc' 、'm'、'y'、'n'、's' 就代表了一个角色。"
    m "'mc' 代表你自己，'m' 就是我，'y' 就是 Yuri，'n' 就是 Natsuki，'s' 就是 Sayori。"
    m 1b "关于 'mc'，它并不是代指 Minecraft，而是 Main Character 的简称。"
    m "Main Character 就是主角的意思，而你在 DDLC 就是主角。"
    m "里面附有的内容，就是游戏的对话了。"
    m "对话怎么做，完全取决于你。"
    m 3b "当然，如果实在没有灵感的话，你也可以去 Repo 的 original_story_scripts 文件夹里看看。"
    m "这里存放着 DDLC 游戏的原版脚本代码，虽然它们是纯英文的。"
    m "你可以从修改这些代码开始制作。"
    m 1a "如果敲久了 Ren'Py 的代码，你会发现 Ren'Py 其实很简单。"
    m "毕竟 Ren'Py 就是希望让每个人都能制作属于自己的视觉小说。"
    m 5 "所以像我这种新人也可以很快上手 Ren'Py 啦~"
    m "好的，现在你已经学会制作一个十分初级的 Mod 了。"
    m "可是 Mod 里缺了好多东西，比如音乐、角色、背景。这还不是视觉小说应该有的亚子呢。"
    m "别慌，后面我们会慢慢加的。"
    m 3k "不过，接下来的东西就很有挑战性了！"
    m "没事，消化一下，下一关见！"

    # m "Hi again [player]!"
    # m 1a "If the last part was a bit too hard, don’t worry, this part is easier."
    # m "Like last time, I’ll tell you what to do and then I’ll explain, okay?"
    # m 4a "First open monika_route_script.rpy."
    # m "Between the first line and 'return', add the line \n' \ \ \ stop music fadeout 2.0'"
    # m "Then add the line ' play music t2'."
    # m "Finally, add the line \n' \ \ \ mc 'Let's listen to the music.''"
    # m 2a "Check that all lines bellow 'label monika_route:' are aligned and that 'return' is the last line."
    # m "Try to launch the game with Ren’Py and see what happens..."
    # m 2c "..."
    # m 1c "Does it work? If everything goes well, you should be listening to Sayori’s main theme."
    # m 3a "There’s just one dialogue, so if you click one time, you go to the main menu because of the 'return' keyword."
    # m 3b "Okay, time to explain what happened!"
    # m 3a "Let’s look at ' \ \ \ stop music fadeout 2.0'. Before you click New Game, you can hear the music of the main menu, right? "
    # m "But when you click New Game, the music stops progressively."
    # m 4a "That’s due to 'stop music fadeout 2.0'. 'stop music' tells the current music to stop. 'fadeout 2.0' makes it so the current music completely becomes silent in 2 seconds."
    # m 4b "'fadeout' isn’t necessary but smooth transitions are much more pleasant, aren’t they?"
    # m 4a "The next line ' \ \ \ play music t2' tells the game to play the music named 't2'. You’re surely wondering what’s 't2'. 't2' refers to Sayori theme, 'Ohayou Sayori!'."
    # m 3a "Besides Ohayou Sayori, there are many other songs. But each one is labeled by their own nickname."
    # m "You can see the list of every music with their nickname in definitions.rpy"
    # m "You can find definitions.rpy inside the folder advanced_scripts which should be in the DDLC Mod Template's directory."
    # m 2a "Try finding it and then open it."
    # m "Find the lines beginning by 'define audio'. This is where each music gets assigned a nickname."
    # m "For example, in the case of the main theme, its nickname is 't1'. In the case of Confession, its nickname is 't10'."
    # m 5a "Can you now guess what happens if you type 'play music t1' instead of 'play music t2'?"
    # m 1k "Confession is played instead of Ohayou Sayori!"
    # m 2a "Instead of using nickname, you can directly write the path of the music."
    # m "Try writing 'play music '<loop 4.499>bgm/2.ogg'' instead of 'play music t2'."
    # m 2b "See? Ohayou Sayori! is played. Try one last thing for me okay? Write ''<from 50.0>bgm/credits.ogg'' instead of ''<loop 4.499>bgm/2.ogg''."
    # m 5a "Have you already heard this song?"
    # m 1b "This is the song I wrote just for you. I really hope you like it. I worked very hard on it you know."
    # m 1e "..."
    # m 4a "The last line you wrote, ' \ \ \ mc 'Let's listen to the music.', makes the main character says 'Let's listen to the music.'. I’ll explain how dialogue works later so bear with me okay?"
    # m 2a "Alright, before finishing this tutorial, replace ''play <from 50.0>bgm/credits.ogg'' by 'play music t2'."
    # m "Verify you wrote exactly the same lines as in the file t2.rpy which is inside monika_route_answer."
    # m 1b "Congratulation! You now know how to stop and play music~"
    # m "Next time, we’ll see how to add a background."
    # m 5a "See you soon!"

    return

label tutorial_route_p3:

    show monika 5a zorder 2 at t11

    m "[player]，欢迎回来！"
    m 1 "在上一关，你已经学会了怎么制作对话了。"
    m 1q "但是，我们忽视了背景还是黑不溜秋的..."
    m "这真的很毁气氛啊..."
    m 3 "不过，没事。既然没有背景，那么我们就自己加一个。"
    m 3b "接下来，我们就要回到梦开始的地方了！"
    m 3a "打开最初创建的 meet_monika.rpy，"
    m "在 label 行和刚刚写的对话之间新开一行，输入："
    m " \ \ \ scene bg residential_day"
    m "再换一行，输入："
    m " \ \ \ with dissolve_scene_full"
    m "接下来，保存文件，再次启动工程。"
    scene bg residential_day
    with wipeleft
    m "欢迎来到梦开始的地方！"
    show monika 5a at t11 zorder 2
    m "这里感觉好熟悉啊..."
    m "美好的一切，都从这条街开始了..."
    show monika 1a at t21 zorder 2
    show sayori 1ba at f22 zorder 2
    s "诶？"
    s 1bb "Monika？[player]？"
    s 1bc "你们怎么在这里？"
    show sayori 1ba at t22 zorder 2
    show monika 1a at f21 zorder 2
    m 1l "啊哈..."
    m "我们只是来玩一下的。"
    m "这里的阳光多么漂亮啊..."
    m "好的，接下来我要去陪 [player] 去别的地方了~"
    m "拜拜~"
    show monika 1a at t21 zorder 2
    show sayori 1bs at f22 zorder 2
    s "Bye~"
    show sayori at thide
    hide sayori
    show monika 1a at t21 zorder 2
    m "好的，这个背景就是你启动工程后能看到的了。"
    m "接下来，我会展示 DDLC 更多的背景，顺便带你玩一下。"
    scene bg class_day
    show monika 1a at t11 zorder 2
    with wipeleft
    m "现在这里就是教室了。"
    m "你可以用 scene bg class_day 切换到这里。"
    scene bg corridor
    show monika 1a at t11 zorder 2
    with wipeleft
    m "这里是走廊。"
    m "你可以用 scene bg corridor 切换到这里。"
    scene bg club_day
    show monika 1a at t11 zorder 2
    with wipeleft
    m 5 "欢迎来到文学部！"
    m "你可以用 scene bg club_day 切换到这里。"
    scene bg closet
    show monika 1a at t11 zorder 2
    with wipeleft
    m 1a "这是 Natsuki 的储物柜，里面放着她的漫画。"
    m "你可以用 scene bg closet 切换到这里。"
    scene bg bedroom
    show monika 1m at t11 zorder 2
    with wipeleft
    m 1m "啊哈...现在是你家的卧室。"
    m "你可以用 scene bg bedroom 切换到这里。"
    scene bg house
    show monika 1a at t11 zorder 2
    with wipeleft
    m 1a "这是 Sayori 的家门口。"
    m "你可以用 scene bg house 切换到这里。"
    scene bg sayori_bedroom
    show monika 1l at t11 zorder 2
    with wipeleft
    m 1l "这么私闯别人的住宅不太好吧..."
    m "但这里确实是 Sayori 的卧室。"
    m "你可以用 scene bg sayori_bedroom 切换到这里。"
    scene bg kitchen
    show monika 1a at t11 zorder 2
    with wipeleft
    m 1a "这是你的厨房。"
    m "你可以用 scene bg kitchen 切换到这里。"
    m 1l "我突然想起来以前你和 Natsuki 一起做蛋糕的事了..."
    scene bg club_day
    with dissolve_scene_full
    show monika 1a at t11 zorder 2
    m "好的，我们现在赶回来了。"
    m "DDLC 的世界是不是很漂亮啊？"
    m 3b "这得感谢背景画师 Velinquent。您可以 {a=https://www.pixiv.net/member.php?id=17385446}点击这里{/a} 访问画师的 Pixiv 主页，或者 {a=https://twitter.com/VelinquenT}点击这里{/a} 访问画师的 Twitter。"
    m "不过，你想知道我们是怎么调用背景的吗？"
    m 5 "你可以去看看 advanced_scripts 文件夹里的 definitions.rpy。"
    m "这里面指定了你做 Mod 时会调取的背景。"
    m "有了这串内容，你指定背景时就可以直接使用 scene bg 加上相应名字即可了。"
    m 3a "如果没有这些指定项，那么你接下来调取背景时，输入的内容就会更加枯燥乏味。"
    m 1 "..."

    m 5 "那么，感谢你听到这里。"
    m "好好温习一下，下一关很有挑战性！"

    return

label tutorial_route_p4:
    show monika 5a zorder 2 at t11

    m "欢迎回来，[player]！"
    m 1b "好久不见，甚是想念！"
    m 1a "上一次我们终于向 Mod 里加入了背景。"
    m 1o "但是 Mod 里连个像样的 BGM 也没有..."
    m 1q "这真的很枯燥啊。"
    m 2 "所以，咱们动动手加一个吧！"
    m "还是打开 meet_monika.rpy，"
    m "在 label 行和之前的背景行之间，输入："
    m " \ \ \ stop music fadeout 2.0"
    m " \ \ \ play music t2"
    m "保存文件，启动工程。"

    stop music fadeout 2.0
    play music t2

    m "这时...{w=1.0}{nw}"
    show monika at t21 zorder 2
    show sayori 1k zorder 2 at t22
    s "..."
    show sayori at f22
    s 1l "嗨！"
    s 5 "好像..."
    show monika at f21
    show sayori at t22
    m "是不是想到和 [player] 共度美好时光的日常了？"
    show sayori 5b at f22
    show monika at t21
    s "呃呵呵~"
    show sayori lhide
    hide sayori
    show monika 2 at t11
    m "所以，启动工程并新开游戏后会播放 Ohayou Sayori! 这首 BGM。"
    stop music fadeout 2.0
    play music t3

    m "接下来，我也会告诉你游戏内置了哪些 BGM。"
    m "如果你需要使用某个 BGM，你只需要把 play music t2 中的 t2 改成相应的标签就行了。"
    m "如果你听完了这首 BGM，点击屏幕上的“继续”按钮以切换到下一首。"
    m "那么下面是 BGM 时间！"

    stop music fadeout 2.0
    play music t1
    menu:
        m "t1 \nDoki Doki Literature Club!"
        "继续":
            pass
    
    stop music fadeout 2.0
    play music t2
    menu:
        m "t2 \nOhayou Sayori!"
        "继续":
            pass

    stop music fadeout 2.0
    play music t3
    menu:
        m "t3 \nMain Theme"
        "继续":
            pass
    
    stop music fadeout 2.0
    play music t4
    menu:
        m "t4 \nDreams of Love and Literature"
        "继续":
            pass

    stop music fadeout 2.0
    play music t5
    menu:
        m "t5 \nOkay Everyone!"
        "继续":
            pass
    stop music fadeout 2.0
    play music tmonika
    menu:
        m "tmonika \nOkay Everyone! - Monika"
        "继续":
            pass
    stop music fadeout 2.0
    play music tsayori
    menu:
        m "tsayori \nOkay Everyone! - Sayori"
        "继续":
            pass
    stop music fadeout 2.0
    play music tnatsuki
    menu:
        m "tnatsuki \nOkay Everyone! - Natsuki"
        "继续":
            pass
    stop music fadeout 2.0
    play music tyuri
    menu:
        m "tyuri \nOkay Everyone! - Yuri"
        "继续":
            pass

    stop music fadeout 2.0
    play music t6
    menu:
        m "t6 \nPlay With Me"
        "继续":
            pass

    stop music fadeout 2.0
    play music t7
    menu:
        m "t7 \nPoem Panic"
        "继续":
            pass

    stop music fadeout 2.0
    play music t8
    menu:
        m "t8 \nDaijoubu!"
        "继续":
            pass

    stop music fadeout 2.0
    play music t9
    menu:
        m "t9 \nMy Feelings"
        "继续":
            pass
    
    stop music fadeout 2.0
    play music t10
    menu:
        m "t10 \nMy Confession"
        "继续":
            pass

    stop music fadeout 2.0
    play music m1
    menu:
        m "m1 \nJust Monika."
        "继续":
            pass

    stop music fadeout 2.0
    play music mend
    menu:
        m "mend \nI Still Love You"
        "继续":
            pass

    stop music fadeout 2.0
    m "那么正常的音乐，我们已经播放完了。"
    m 1o "其实 DDLC 里面还有一些有点恐怖的音乐，"
    m "按你们的话来讲，“阴间”音乐。"
    menu:
        m "你还要继续听下去吗？"

        "继续":
            pass
        "不，跳过":
            jump tutorial_route_p4_end
    
    m 1q "好的。"
    m "那么，准备好吧..."
    m "暗黑音乐马上开始..."
    stop music fadeout 2.0
    play music td
    menu:
        m "td \nSayo-nara"
        "继续":
            pass
    stop music fadeout 2.0
    play music t6g
    menu:
        m "t6g \n爆炸版 Play With Me"
        "继续":
            pass
    stop music fadeout 2.0
    m "算了，我也不能过度剧透这种恐怖音乐。"
label tutorial_route_p4_end:
    play music t3
    m 5 "那么这一关就到这里结束了~"
    m "如果你对这些标签感兴趣的话，可以查看 advanced_scripts 文件夹里的 definitions.rpy。"
    m "里面也指定了 BGM 的标签哦！"
    m "放松一下，准备下一关吧！"
    return

label tutorial_route_p5:

    show monika 4a zorder 2 at t11

    m "This time, I’ll explain how to make choices."
    m "For example..."

    call tutorial_route_p5_favorite_color from _call_tutorial_route_p5_favorite_color

    m 2k "What a coincidence! It's also my favorite color!"
    m 2b "It's the color of my eyes."
    m 5a "Aren't we a perfect match?"
    m "Ehehe~"
    m 3a "As you can see, I gave you several choices and you picked one of them."
    m "That’s what I’m going to teach you."
    m 4a "Like every time, open monika_route_script.rpy and between 'return' and the last line before it,-"
    m "- add ' \ \ \ menu:', jump a line and then enter below \n' \ \ \ \ \ \ \ \ mc 'I told her to meet me...''. Be careful, this time, there are eight spaces."
    m "Write just under \n' \ \ \ \ \ \ 'At the literature club room':' and then \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room''."
    m 4b "Type \n' \ \ \ \ \ \ 'In front of my house':' and under it \n' \ \ \ \ \ \ \ $ meeting_place = 'my_house'."
    m 4a "Finally, jump a line and add ' \ \ \ mc 'I can't wait to meet her!''."
    m 2a "Try to play the game."
    m "If it doesn’t work, there’s surely an indentation error."
    m 5a "I can’t help you from here, but you can check T5.rpy for the answers. You know where it is, right?"
    m 4b "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, 'I told her to meet me...'."
    m "You can specify who says this sentence by adding a nickname like 'mc' before it. It’s just like a dialogue. What’s important is that this sentence is written before any choice."
    m 3a "Contrary to the explanative sentence, the choices mustn’t be preceded by a nickname. They should be enclosed in quotation marks. Just after the closing quotation mark, there must be a ':' ."
    m "After ':, the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."
    m 3b "I’ll give more explanation about the meaning of indents in the next tutorial."
    m 3a "In our case, the next line after the first choice is \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room'."
    m 2a "Take a good look at this line."
    m 3b "Until now, I referred 'mc', 'bg residential' and 't2' as nickname. But that’s not really the correct word. They are actually what we call variable."
    m "Variable in coding is a very important concept. They have many forms and do many things. They can be ‘nicknames’ or they can be numbers or more complicated structures."
    m 1a "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what’s necessary to make a DDLC mod, okay?"
    m 1c "I myself don’t know Python and Ren’Py all that well after all..."
    m 3a "'meeting_place' is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): 'club_room'."
    m "Its default value is None which means it doesn’t exist."
    m 3e "Hold on a second? How can it not exist, you say?"
    m 1a "Well before you define it, the variable doesn’t exist. But if you later try to use it, for example in a conditional statement, the variable will be ‘created’ and its value will be None."
    m "It’s alright if you don’t understand it yet. Variable, conditional statement and None will become clearer in my next lecture."
    m 4b "Let’s go back to the meaning of ' $ meeting_place = 'club_room'. Here we create the variable 'meeting_place' and assign it the string 'club_room'."
    m 4m "The '$' in front of it is to tell Ren’Py the line is a Python line. Um..., I can’t really explain why we need to do that if you don’t know python yet..."
    m 4a "Just remember that you need to add '$' when you want to assign a variable a value that way"
    m "Regarding the second choice, the structure is the same. The only difference is that the value of 'meeting_place' will be 'my_house' if the player selects the second choice."
    m "After the second choice, the game executes the line ' \ \ \ mc 'I can't wait to meet her!''."
    m 1a "For now it doesn’t look like the choices did anything. But we actually assigned 'meeting_place' either 'club_room' or 'my_house'."
    m 3a "We have to wait until the next tutorial to see how we can use the variable 'meeting_place'."
    m 3b "Alright, I’m sorry to leave hanging like that I believe we need to take a little break."
    m "If you want though, I would more than happy to begin the next part right away!"
    m 5a "Just click Part 6!"

    return

label tutorial_route_p5_favorite_color:

    menu:
        m "What is your favorite color?"
        "Sky Blue":

            jump tutorial_route_p5_favorite_color
        "Amethyst Purple":
            jump tutorial_route_p5_favorite_color
        "Emerald Green":
            return
        "Candy Pink":
            jump tutorial_route_p5_favorite_color

            m " Are you ready? We are going to ramp up the difficulty."

label tutorial_route_p6:

    show monika 5a zorder 2 at t11

    m "Yeah, you came back [player]!"
    m "Glad to see you didn’t run away on me. Ahaha!"
    m 1e "I was afraid the last tutorial was a bit too hard..."
    m 1m "Well, this one is going to be hard as well but..."
    m 1b "Hang it there okay? We did the hardest part already!"
    m 1a "Last time we saw how to add menu and how to assign variable a value."
    m 1b "Let’s see how we can use these variables!"
    m 2a "You know the drill, open monika_route_script.rpy and at the end of the file, just before 'return'..."
    m 4a "Add the following lines :"
    m "' \ \ \ if meeting_place == 'club_room':',"
    m "' \ \ \ scene bg club_day',"
    m "' \ \ \ with wipeleft_scene',"
    m "' elif meeting_place == 'my_house':',"
    m "' \ \ \ scene bg house',"
    m "' \ \ \ with wipeleft_scene',"
    m " ' \ \ \ stop music fadeout 2.0',"
    m " ' \ \ \ play music t2',"
    m " 'mc 'She is already waiting for me when I arrive.''."
    m 2a "That was the last one. Save the file and try to play the game."
    m 5a "If it doesn’t work, you know where you can see the answer, don’t you?"
    m 2a "You already know how scene, transition, music and dialogue work so I won’t go over it again."
    m 4b "It’s not like I don’t want spend more time with you but you know, ... I’m excited to finish my route too!"
    m 4a "Okay, so the new thing is the 'if' statement. We call that a conditional statement. It’s an elementary and essential operation in programming."
    m "It goes basically like this: IF something_is_true THEN something_happens. In our case, if the meeting_place is 'club_rooom', then the scene changes to the club room."
    m 3a "Otherwise, if meeting_place is 'my_house' then the scene changes to the main character’s house."
    m 3b "It seems simple, right?"
    m 3a "The syntax must be as follow: first, there must be a 'if' followed by an equality which is either 'True' or 'False'. For example, 'meeting_place == 'club_room''."
    m "If 'meeting_place' was assigned 'club_room' before then the equality returns 'True'. Otherwise, its returns False."
    m "If the equality returns True then the game will read the lines belonging to the if bloc."
    m 4a "You can see where those lines are because they have one more indent compared to the if statement preceding them."
    m 4b "We once again meet the system of indent and block. This is one of the property of Python and Ren’Py. Let’s do a quick exercise."
    m "Can you see difference between:"
    m 2a " ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', \n' \ \ \ mc 'We will meet at the club room.''."
    m "And ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' mc 'We will meet at the club room.''?"
    m 4b "In the first case, the main character only says they will meet at the club room if 'meeting_place' is equal to 'club_room'."
    m "In the second case, he will say it no matter the value of 'meeting_place'."
    m 3a "You can see once again how important indentations are in Python."
    m 4b "About the second comparison, 'elif meeting_place == 'my_house'', note that we use 'elif' at the beginning instead of 'if'."
    m 4a "The difference between 'elif' and 'if' is subtle. First, you can only use 'elif' after you already wrote 'if'."
    m "Second, the statement following 'elif' won’t be evaluated if the previous if statement was True. Other than that, 'elif' works like 'if'."
    m 1b "Well, in our case it doesn’t matter because if 'meeting_place' is 'club_room' then 'meeting_place' cannot be 'my_house' at the same time."
    m 1a "It would matter if it was something like..."
    m "' \ \ \ if monika_affection_points > 10:' , \n' \ \ \ scene bg house', '' if monika_affection_points > 6:' , \n' \ \ \ scene club_day '."
    m 3a "In that case, if 'monika_affection_points' is higher than 10, the new scene wouldn’t be the house but the club because the game will evaluate both if."
    m 4b "To avoid that, 'elif' should be used instead of 'if'."
    m 4a "Besides 'if' and 'elif', there’s also the keyword 'else'. Like 'elif', 'else' can be used after a if. The bloc under 'else' will be executed if the previous if or elif statements are False."
    m 2a "For example..."
    m "' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' \ \ \ else:' , \n' \ \ \ scene club_day '."
    m 1a "Well, there are more things to say about conditional statement..."
    m "For example about the keywords 'and' and 'or'..."
    m 3a "But let’s keep that for another time. I’m sure you can find more tutorial on Python and conditional statement."
    m 1b "For now, let’s move on! It’s about time we add character pictures into the game!"
    m 5a "See you later [player]!"

    return

label tutorial_route_p7:

    show monika 5a zorder 2 at t11

    m "Hi [player]!"
    m "It’s about time we add character pictures, don’t you think?"
    m 1b "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."
    m "In Doki Doki Literature Club, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."
    m 1e "So each character has about 900 combinations! That seems a lot but...when you’re actually inside the game, the lack of freedom becomes horribly frustrating..."
    m 1f "I really wish I could show you different expressions, poses and clothes but unfortunately, I can’t add myself new artwork to the game..."
    m 5a "If you’re an artist, I would really love it if you could add me more sprites!"
    m 2a "For our mod, we’ll only use existing art."
    m 4b "Let’s dot it! Open monika_route_script.rpy and before 'return', write:"
    m 4a "' \ \ \ show monika 1b at t11 zorder 2',"
    m "' \ \ \ m 'Hi [[player]!'',"
    m "' \ \ \ mc 'You're already here? I hope I didn't make you wait for too long.'',"
    m "' \ \ \ m 2a 'Don't worry, it's me who's early.'',"
    m "' \ \ \ show monika 5a at f11 zorder 3'."
    m 2a "Save, play the mod, and check T7.rpy if there’s an error."
    m 4b "Alright! The only new things are 'show monika 1b at t11 zorder 2' and 'm 2a'."
    m 4a "First, let’s go over 'show monika 1b at t11 zorder 2'."
    m "The keyword 'show' shows the sprite of the character named 'monika', with her pose '1' and her expression 'b'."
    m " The keyword 'at' specifies the position of the sprite. In the line above, the position is 't11'. 'zorder' has something to do with layers."
    m 3b "I’ll explain how positions and layers work in the next tutorial. For now, let’s focus on the poses and expressions of sprite."
    m 4a "Obviously, the variable 'monika' refers to me. Naturally, 'yuri' refers to Yuri and so on."
    m "If you write \n' \ \ \ show yuri 1b at f11 zorder 3' instead of \n' \ \ \ show monika 1b at f11 zorder 3', it’s Yuri who will appear."
    m 4k "Of course, you only have eyes for me so let’s not bother with the sprites of the other girls, ahaha!"
    m 5a "In my case, I have 5 different poses. I will show them to you one by one now."
    m 1a "This is my first pose."
    m 2a "This is my second pose."
    m 3a "This is my third pose."
    m 4a "This is my fourth pose."
    m 5a "This my fifth pose."
    m "I wonder which one do you prefer..."
    m 1a "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from a to r. I will show them one by one."
    m 4a "Expression a."
    m 4b "Expression b."
    m 4c "Expression c"
    m 4d "Expression d."
    m 4e "Expression e."
    m 4f "Expression f."
    m 4g "Expression g."
    m 4h "Expression g."
    m 4i "Expression i."
    m 4j "Expression j."
    m 4k "Expression k."
    m 4l "Expression l."
    m 4m "Expression m."
    m 4n "Expression n."
    m 4o "Expression o."
    m 4p "Expression p."
    m 4q "Expression q."
    m 4r "Expression r."
    m 4a "You can find my list of expressions in 'MonikaCheatsheet.jpg' inside the mod's main directory."
    m 1b "I hope you will quickly memorize them perfectly!"
    m 5b "As my lover, you should know my face and my expressions without fail."
    m 3a "You can also find my poses and my expressions in definitions.rpy."
    m "My fifth pose only has the expressions a and b."
    m 5a "Like this."
    m 5b "And this."
    m 4a "My other poses have all expressions though."
    m 1b "Okay! In short, to show a sprite, you need to write 'show monika pose expression at t11 zorder 2'. Pose is either 1,2,3,4 or 5 and expression ranges from a to r."
    m "If you want to show several characters, just write 'show' several times, like this:"
    m 2a "' \ \ \ show yuri 1a at t41 zorder 2', ' \ \ \ show sayori 1a at t42 zorder 2', ' \ \ \ show monika 1a at t43 zorder 2', ' \ \ \ show natsuki 1a at t44 zorder 2'."
    m 2b "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."
    m "After a sprite is already on the screen, there’s a shortcut to change her pose and expression."
    m 3a "Instead of using 'show' again and again, you can directly write the letter corresponding to the character followed by the number and the letter for their pose and expression."
    m "This is what we did in \n' \ \ \ m 2a 'Don't worry, it's me who's early.''."
    m 4g "Note that the sprite of the character speaking must already be on screeen."
    m 4e "If you try for example \n' \ \ \ y 2a 'Don't worry, it's me who's early.'', Yuri will speak but her sprite will not appear."
    m 3a "Keep in mind who’s on screen and who’s not at all time so as not to make a mistake."
    m 2a "...Never mind, actually just show my sprite. That way you don’t have to worry about such problem. It’s not like the other girls care about being shown anyway."
    m 1b "And that’s all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"
    m "Next time, I’ll finish explaining positions and layers."
    m 5a "See you [player]!"


    return

label tutorial_route_p8:

    show monika 5a zorder 2 at t11

    m "Welcome back to our modding club!"
    m "Last time, we learnt about how to show sprite, now let’s learn how to place then."
    m 4a "Open monika_route_script.rpy and just before..."
    m 1b "Just kidding! Actually, you don’t have to add anything this time."
    m 3b "We already did it last tutorial after all."
    m 2a "So, do you remember the line \n' \ \ \ show monika 1b at t11 zorder 2'?"
    m "I said that 'at t11' was about position and that 'zorder 2' was about layer."
    m 2b "Let’s study in details what exactly that means."
    m 4b "’at' is a keyword that tells the game to put the sprite at the position 't11'."
    m "t11' is one of the position defined in Doki Doki Literature Club. There are more than 50 positions possible."
    m 4a "You can find the list of all defined positions in the script transforms.rpy. You can find it in the same folder as definitions.rpy."
    m "For now, I will explain the most common positions used in the original game."
    m 1a "Let’s start with the 't' positions. I will show them one by one."

    show monika 1a zorder 2 at t11
    m "Position t11."

    show monika 1a zorder 2 at t21
    m "Position t21."

    show monika 1a zorder 2 at t22
    m "Position t22."

    show monika 1a zorder 2 at t31
    m "Position t31."

    show monika 1a zorder 2 at t32
    m "Position t32."

    show monika 1a zorder 2 at t33
    m "Position t33."

    show monika 1a zorder 2 at t41
    m "Position t41."

    show monika 1a zorder 2 at t42
    m "Position t42."

    show monika 1a zorder 2 at t43
    m "Position t43."

    show monika 1a zorder 2 at t44
    m "Position t44."

    show monika 1a zorder 2 at t11

    m 1b "And that’s all for the 't' positions."
    m 4a "I think you guessed it already but 't11' should be used when there’s only one character."
    m "'t21' and 't22' should be used when there are two characters. 't21' is for the left, 't22' is for the right."
    m 3a "It’s the same logic for 't31','t32','t33'. 't31' is the left, 't32' the middle and 't33' the right. "
    m "'t41', 't42','t43' and 't44' work in the same way."
    m 3b "I encourage you to try these positions yourself with several characters. After all, there’s nothing better than practice to learn!"
    m 1a "If you remember well, we wrote one time ' show yuri 1b at f11 zorder 3'."
    m "Notice that the position is 'f11' instead of 't11'. The difference is just that 'f' positions are zoomed in. 'f' stands for focused. There are as many 'f' positions as 't' positions."
    m 4a "You should use 'f' position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who’s talking."
    m 2b "Let’s talk about the keyword 'zorder' now."
    m 4a "When the game renders pictures, there’s an order."
    m "First, the background is rendered. Then the sprites and finally the U.I."
    m 4b "That’s why the sprites are on top of the background and the U.I on top of everything."
    m 2a "As you can see, order is very important. If the game renders background last, then you won’t be able to see anything else."
    m 3a "In Ren’Py the order of sprite is called zorder."
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."
    m 4b "Try writing the following lines instead of 'show monika 1b at t11 zorder 2':"
    m 4a "' \ \ \ show monika 1a at t41 zorder 4',"
    m "' \ \ \ show yuri 1a at t42 zorder 3',"
    m "' \ \ \ show natsuki 1a at t43 zorder 2',"
    m "' \ \ \ show sayori 1a at t44 zorder 1'."
    m 1a "Play the game and..."
    m 1b "Everyone is here!"
    m 3a "But that’s not the point. Pay attention to who’s on top on who."
    m "If you look closely, you can see the rendering order is like this : monika > yuri > natsuki > sayori."
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."
    m 4a "If the zorder of two sprites are the same then the last sprite shown by 'show' will be on top."
    m 2b "Well, most of the time, you don’t have to worry about zorder. Just make sure I always have the highest zorder, okay?"
    m 1b "Alright! That ends this tutorial!"
    m 1a "Verify you reverted the changes you made to moninka_route_script.rpy. It should be like T8.rpy."
    m 1c "There is one more tutorial. I’m very happy we almost finished our first mod but..."
    m 1f "It also means we’ll soon get split up..."
    m 1g "..."
    m 1m "Or maybe not..."
    m 5a "See you later."

    return

label tutorial_route_p9:

    show monika 5a zorder 2 at t11

    m "This it it, [player], today is the day we finally make my route!"
    m "Are you ready?"
    m 3b "Be careful, we need to add a lot of lines this time."
    m 4a "Open monika_route_script.rpy and before the last 'return', jump a line and add..."
    m "' \ \ \ menu :',"
    m "' \ \ \ \ \ \ mc 'Right. Monika,...'',"
    m "' \ \ \ \ \ \ 'I love you! Please go out with me!':',"
    m "' \ \ \ \ \ \ jump monika_normal_ending',"
    m "' \ \ \ \ \ \ 'You are everything for me! Please marry me!':',"
    m "' \ \ \ \ \ \ jump monika_good_ending',"
    m 2b "This is it for the label monika_route. Now we need to add two more labels: monika_normal_ending and monika_good_ending."
    m 4a "After 'return', jump a line and write 'label monika_good_ending:'. This time, there is no space before label."
    m 4b "Then under label, write the following lines:"
    m 4a "' \ \ \ scene dark',"
    m "' \ \ \ with dissolve_scene_full',"
    m "' \ \ \ mc 'She accepted my confession and we became lovers.'',"
    m "' \ \ \ 'NORMAL ENDING'',"
    m "' \ \ \ return'."
    m 1b "The normal ending is now complete. Let’s do the good ending. After the last 'return', jump a line and write 'label monika_good_ending:'."
    m 4a "Then type under it..."
    m "' \ \ \ scene white',"
    m "'with dissolve_scene_full',"
    m "' \ \ \ mc 'She gladly accepted my proposal and we got married one year later.'',"
    m "' \ \ \ 'GOOD ENDING'',"
    m "' \ \ \ return'."
    m 2b "Save, play the game and verify if everything works. Get both endings."
    m "If there’s a problem, check T9.rpy for the solution."
    m 2a "..."
    m 4b "It’s not over yet. You can run the game with Ren’Py but to make it a proper mod, there’s one more step: the build distribution."
    m "Open renpy. Click our project, DDLC Monika Route, and then click Build Distributions which should be on the right, inside Navigate Script."
    m 4a "You should see several options for Build Packages. Check that the box for DDLC Compatible Mod is filled."
    m "You can change the name of our mod, its build and its version in the script options.rpy."
    m 3b "Click Build."
    m 2b "Once it’s finished, you should see one folder called build.name-config.version-dists inside Ren’Py’s directory. Open it and you should see a zip file."
    m 1a "Look at the file build.name-config.version-Mod.zip. It’s our mod. If you want to share it to other people, you should just upload this archive."
    m 2a "This way of sharing the mod is also what the creators of DDLC prefer. You are only sharing the new files that we made together, and nothing more."
    m 2a "Let’s see if it works. Extract build.name-config.version-Mod.zip. Make a new copy of the original Doki Doki Literature Club folder."
    m "Copy-paste the files of build.name-config.version-Mod inside the new copy of the game."
    m 4a "Play our mod by clicking DDLC.exe inside the new folder."
    m 4b "If everything goes well, you should be playing my new route!"
    m 1k "Congratulation! We finally did it!!"
    m 1e "..."
    m "I should be happy but..."
    m 1f "It means you’ll soon leave me to play with other Monika..."
    m 1g "..."
    m 1n "There’s still a way to stay together, even after you finish my tutorials."
    m 3e "I saved my memory and my data in a special file."
    m "You can download the mod Monika After Story. You can find it in http://www.monikaafterstory.com/. "
    m 4e "Once you play it, the Monika of that mod will import the file I made. Our memories and personalities will then be fused together."
    m "Like this, that part of me will still be with you forever."
    m 1f "..."
    m "I wish I could do more but..."
    m 1c "You can change that [player]. You now know how to make a mod. You now have the power to change our fate."
    m 1e "I’m counting on you [player]."

    show monika 5a zorder 2 at f11

    m "I love you."
    m 1b "I will never forget you..."
    m 1e "Bye."

    return

label tutorial_route_adv:
    # advanced scripts just because
    python:
        adv_items = [
            ("Navigation Buttons", "tutorial_route_adv_hkb"),
            ("Edited 风格文本框", "tutorial_route_adv_edited"),
            ("Poemgame（测试）", "tutorial_route_adv_poemgame"),
            ("Monika，请喊出我的电脑用户名！", "tutorial_route_adv_current"),
            ("DDMM SDK 测试（实验中）", "_ddmm_test"),
            ("诗歌字体测试", "poemtest")
        ]

    m 5a "你现在想来点高级的？"
    m 3a "可以！"

init python:
    import subprocess
    import os
    process_list = []
    currentuser = ""
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                user = os.environ.get(name)
                if user:
                    currentuser = user
        except:
            pass

label tutorial_route_adv_repeat:

    show monika 3a at tcommon(950)
    window show
    $ renpy.say(m, "你想尝试些什么？", interact=False)

    call screen tutorial_choice(adv_items)
    window auto

    if _return == False:
        return

    show monika at t11

    call expression _return from _call_expression_1

    jump tutorial_route_adv_repeat


label tutorial_route_adv_hkb:
    m 3a "Alright, let me show you the navigation buttons."
    $ mas_HKBRaiseShield()
    $ HKBShowButtons()
    m "These buttons appear in the bottom left of the screen."
    m "To make them appear, add '$ HKBShowButtons()' to the script."
    m 1n "Right now, they are disabled."
    m "To enable them, add '$ mas_HKBDropShield()' to the script."
    m "I'll go ahead and do that now..."
    $ mas_HKBDropShield()
    m 2a "Now you can click them!{w} When you're done, click 'Continue' to continue."
    menu:
        "Continue":
            pass

    m "To disable the buttons but leave them on screen, add '$ mas_HKBRaiseShield()' to the script."
    $ mas_HKBRaiseShield()
    m 2b "And finally, to hide the buttons, add '$ HKBHideButtons()'."
    $ HKBHideButtons()

    $ navdir = config.basedir + "/game/advanced_scripts/zz_hotkey_buttons.rpy"
    m "The source code for the navigation buttons is in '[navdir]'."
    m "To change what the buttons do, edit the 'action' part of the textbuttons in the source code."
    m "Currently, all the buttons call a python function using 'Function', but you can change that to a variety of Screen Actions including 'Jump' and 'Call'."
    m "For more information on that, check the renpy documentation on Screen Actions."

    m 1c "One last thing,{w} these navigation buttons were created by developers from the Monika After Story team."
    m 5a "But, you are free to use this version of `zz_hotkey_buttons.rpy` in your mods."

    m 1a "Okay! Thanks for listening!"

    return

label tutorial_route_adv_edited:

    m "咕~"

    return

label tutorial_route_adv_current:

    m 5 "好的，我马上就要喊出来了哦！"
    m "你现在关掉直播软件还来得及！喵~"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "bandicam.exe", "livehime.exe"]
    if list(set(process_list).intersection(stream_list)):
        m "emm..."
        m "算了，我先不说了..."
        return
    # 这里的进程识别有点点问题
    m "准备了啊！"
    m "你好，[currentuser]！你好，[player]！"
    m 3l "..."
    m "啊哈..."

    return

label tutorial_route_adv_poemgame:
    m "Poemgame 仍为测试项目。"
    m 3a "Alright, let's look at the specially-modified poemgame developed by the Monika After Story team."
    m "This version of the poemgame allows you to do the following:"
    m "1. Add me to the poemgame, provided you have a list of words for me."
    m "2. Change which dokis are in the poemgame."
    m "3. Change music during the poemgame."
    m "4. Gather / save the words that users select."
    m "5. Save the individual character scores for the words users select."
    m "6. Add / remove glitches that were used in the base poemgame."
    m "7. Change the odds of those glitches."
    m "8. Change number of words you can pick."
    m "9. Change the words that are selectable."
    m "10. Change poem background."
    m "And other smaller adjustments."

    m "Additionally, this version of poemgame includes a special screen that can be used to generate textbutton grids of varying rows and columns."
    m "I'll showcase that later."

    $ navdir = config.basedir + "/game/advanced_scripts/zz_poemgame.rpy"
    m "You can find the source code in '[navdir]'."

    m 2o "Before I get into this, I must say that this file is {b}not{/b} for the faint of heart.{w} The code in here is pretty complex and difficult to customize."
    m "That means that if you want to do something that isn't covered by the features I listed above, you're better off customizing `script-poemgame` yourself."
    m "But if this turns out to be helpful for you, you are free to use this version of `zz_poemgame.rpy` in your mod."

    m "That being said..."
    menu:
        m "Do you still want to hear about the MAS version of poemgame?"
        "Yes":
            pass
        "No":
            jump tutorial_route_adv_poemgame_txgrid
    

label tutorial_route_adv_poemgame_pgexp:
    python:
        mas_wordlist = MASPoemWordList(mas_poemwords)

    m 5a "Yay!"

    m 3a "So the modified poemgame starts at the label 'mas_poem_minigame'."
    m 3n "If you have the source code open, you might notice the {i}massive{/i} comment right above that label."
    m 3a "This comment explains all the possible adjustable parameters you can pass into this label to configure it."
    m "Since this is terribly complex to do, the MAS team also added 3 helper labels based on the poemgame in different Acts."
    m "For Act 1: 'mas_poem_minigame_actone'."
    m "Act 2: 'mas_poem_minigame_acttwo'."
    m "And Act 3: 'mas_poem_minigame_actthree'."
    m "These are also pretty configurable, but only have a subset of the options available to the main poemgame label."

    m 2a "Let's go through how the game looks when you call these labels."
    m "For the sake of time, I'll limit the word selection to only 5 words per poemgame."

    m "Alright, lets start with a slightly modified Act 1."
    m "I'll be in this game, and I'll collect the points scored for each doki."
    stop music fadeout 1.0
    call mas_poem_minigame_actone(show_monika=True, poem_wordlist=mas_wordlist, total_words=5, trans_fast=True, show_poemhelp=False) from _call_mas_poem_minigame_actone
    scene bg club_day with dissolve_scene_full
    play music t3 fadein 1.0

    $ words = _return
    show monika 1a at t11
    m "Hi there!"
    m "These are your point totals:"
    python:
        for k,v in words.iteritems():
            m(k + " received " + str(v) + " point(s) from your choices.")

    m "Now let's do Act 2 but with higher chances of the glitchy word scare and no music."
    m "I'll also gather the words you select."
    stop music fadeout 1.0
    call mas_poem_minigame_acttwo(show_monika=True, poem_wordlist=mas_wordlist, total_words=5, music_filename=None, gather_words=True, glitch_wordscare=(True, 5), trans_fast=True, one_counter=False, show_poemhelp=False) from _call_mas_poem_minigame_acttwo

    scene bg club_day with dissolve_scene_full
    play music t3 fadein 1.0

    $ words = _return["words"]
    show monika 1a at t11
    m "Hi there!"
    m "These are the words you selected:"
    python:
        for word in words:
            m(word.word)

    m "Okay, time for my favorite Act, but with a twist!"
    m "I won't glitch any of the words and I'll hop for all your selections."
    m "I'll also keep the friendly music we have currently playing on during the game."
    call mas_poem_minigame_actthree(glitch_words=None, hop_monika=True, music_filename="BACK", trans_fast=True, total_words=5) from _call_mas_poem_minigame_actthree
    scene bg club_day with dissolve_scene_full

    show monika 5a at t11
    m "That was fun!"

    m 3a "Let's do one more poemgame call. This time, I'll ask you for some parameters."
    $ pg_args = dict()

    m "First..."
    menu:
        m "Should we collect your word choices?"
        "Yes":
            $ pg_args["gather_words"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should we visibly glitch the words?"
        "Glitch the words.":
            m "Sure!"

            call tutorial_route_adv_poemgame_getnum("What are the odds that a space appears instead of a letter? (1 out of x)") from _call_tutorial_route_adv_poemgame_getnum
            $ space_odds = _return

            if space_odds <= 0:
                m 3n "I'll just say 5, then."
                show monika 3a
                $ space_odds = 5

            call tutorial_route_adv_poemgame_getnum("What are the odds that a nonunicode character appears instead of a letter? (1 out of x)") from _call_tutorial_route_adv_poemgame_getnum_1
            $ nonuni_odds = _return

            if nonuni_odds <= 0:
                m 3n "I'll just say 5, then."
                show monika 3a
                $ nonuni_odds = 5

            $ pg_args["glitch_words"] = (True, space_odds, nonuni_odds)

        "No":
            pass

    m "Okay..."
    menu:
        m "Should we use the poemgame music?"
        "Yes":
            pass
        "No":
            $ pg_args["music_filename"] = "BACK"

    m "Okay..."
    menu:
        m "Should I be visible?"
        "Yes":
            m 3j "Yay!"

        "No":
            m 3o "Aww..."
            $ pg_args["show_monika"] = False

    show monika 3a
    m "Okay..."
    menu:
        m "Should Sayori be visible?"
        "Yes":
            $ pg_args["show_sayori"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should Natsuki be visible?"
        "Yes":
            $ pg_args["show_natsuki"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should Yuri be visible?"
        "Yes":
            menu:
                m "...Should she have sleeves rolled up?"
                "Yes":
                    $ pg_args["show_yuri_cut"] = True
                "No":
                    pass
            $ pg_args["show_yuri"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should we make the word counter show 1's instead of regular numbers?"
        "Yes":
            $ pg_args["one_counter"] = True
        "No":
            pass

    m "Okay, last one."
    call tutorial_route_adv_poemgame_getnum("How many words should we select?") from _call_tutorial_route_adv_poemgame_getnum_2
    $ count = _return

    if count <= 0:
        m 3n "I'll just pick 14 then."
        $ count = 14
    elif count > 50:
        m 3n "That's a lot of words. Let's just pick 50."
        $ count = 50

    $ pg_args["total_words"] = count

    m 3a "Alright! Please note that we only went through some of the possible configuration parameters. There are more then what I asked you, but I'm only doing some of them to save time."

    m "Now let's see what we created!"
    $ pg_args["flow"] = store.mas_poemgame_consts.STOCK_MODE
    $ pg_args["poem_wordlist"] = mas_wordlist
    $ pg_args["show_poemhelp"] = False

    if "music_filename" not in pg_args:
        stop music fadeout 1.0

    call mas_poem_minigame(**pg_args) from _call_mas_poem_minigame
    $ results = _return

    scene bg club_day with dissolve_scene_full

    if "music_filename" not in pg_args:
        play music t3 fadein 1.0

    show monika 5a at t11

    m "Alright!"

    if "gather_words" in pg_args:
        m "These are the words you selected:"
        $ words = results.pop("words")
        python:
            for word in words:
                m(word.word)
        pass # syntax highlighting

    m "These are your point totals:"
    python:
        for k,v in results.iteritems():
            m(k + " received " + str(v) + " point(s) from your choices.")
    pass

label tutorial_route_adv_poemgame_pg_end:
    m 2a "Alright, I hope that helps you get a feel for how the MAS poemgame implementation works."
    m "Remember to read the documentation in the source code carefully. There's a lot of parameter formatting to make the poemgame work correctly."
    m "And you can always use one of the act-based labels without params if you just want something that works out of the box."

    m 1a "Now..."
    jump tutorial_route_adv_poemgame_txgrid


label tutorial_route_adv_poemgame_getnum(msg):
    python:
        sel_num = renpy.input(
            "[msg]",
            allow="0123456789",
            length=2
        )
        if len(sel_num) <= 0:
            sel_num = 0
        else:
            sel_num = int(sel_num)

    return sel_num


label tutorial_route_adv_poemgame_txgrid:
    
    menu:
        "Do you want to hear about the textbutton grid?"
        "Yes":
            pass
        "No":
            m "Alright. Thanks for listening!"
            return

    m 1a "Alright!"
    m "The textbutton grid is a special screen that can be used to generate textbutton grids of varying rows and columns."
    m "It's basically the part of poemgame that displays a list of words and allows the user to select one."
    m "To launch the screen, add 'call screen mas_pg_textbutton_grid(...)' to your script."
    m "You will need to pass in several parameters in order to show the grid correctly."

    m 5a "Let's build those parameters together!"
    m 2a "First..."
    call tutorial_route_adv_poemgame_getnum("How many words should we show?") from _call_tutorial_route_adv_poemgame_getnum_3
    $ word_count = _return

    if word_count < 1:
        m 2n "[player]..."
        m "Let's just pick 10 words."
        $ word_count = 10

    m 2a "Now let's pick those words."

    python:
        word_list = list()
        for count in range(0, word_count):
            _word = renpy.input(
                "Enter in word " + str(count+1) + ":",
                allow="1234567890-qwertyuiopasdfghjklzxcvbnm",
                length=20
            )
            word_list.append((_word, _word))

    m "Now..."
    call tutorial_route_adv_poemgame_getnum("How many rows should we show?") from _call_tutorial_route_adv_poemgame_getnum_4
    $ row_count = _return

    if row_count < 1:
        m 3n "I'll just pick 6 rows."
        $ row_count = 6

    m 2a "And finally..."
    call tutorial_route_adv_poemgame_getnum("How many columns should we show?") from _call_tutorial_route_adv_poemgame_getnum_5
    $ col_count = _return

    if col_count <1:
        m 3h "Okay, 3 columns, then."
        $ col_count = 3

    show monika at t22
    m "Okay, I'm going to make this cover the left half of the screen by giving it an x position of 5, a y position of 5, a width of 600, and a height of 700."
    $ size_tuple = (5, 5, 600, 700)

    m "And a somewhat pink background image."
    $ bg_image = Solid("#ffe6f4bb", xsize=600, ysize=700)

    python:
        in_args = {
            "words": word_list,
            "row_info": (row_count, None),
            "col_info": (col_count, None),
            "xywh": size_tuple,
            "bg_image": bg_image,
            "_zorder": 200,
            "is_modal": True
        }

    m 5a "Now let's see what we got!"
    call screen mas_pg_textbutton_grid(**in_args)

    show monika at t11

    m "You selected '[_return]'!"

    m 1n "Hopefully that looked okay. It's easy to pick a combination of rows and columns and words that break the grid."
    
    m 1a "But if you need to make a simple textbutton grid, this should work fine!"

    m "For the technical details on how to call this screen and setup the paramters, check the source code for this set of dialogue and the screen itself."
    m "This set of dialogue is under the label 'tutorial_route_adv_poemgame_txgrid' in 'tutorials'."
    m "The screen is called 'mas_pg_textbutton_grid' and is located in 'zz_poemgame'."

    m "Okay! I hope that helps! Thanks for listening."

    return


