# 部分注释参照 https://github.com/GanstaKingofSA/DDLCModTemplate2.0

## 目前中文 Mod 模板的版本为 1.4.0，基于原版模板的 1.1.2 版本改造。
## 如果你需要向别人提及模板版本，建议把这两个都放上去。
## 不要修改、删除这段注释。

# 这里可以为你的 Mod 命名。
# 把 "DDLC 中文 Mod 模板" 改成你的 Mod 名字（比如 "我永远喜欢 Sayori"）
define config.name = "DDLC 中文 Mod 模板"

# 这里可以控制是否在游戏主菜单展示 Mod 名字及版本号。
# 一般情况下可以打开以与原游戏区分，但如果 Mod 名字太长，建议改为 False
define gui.show_name = False

# 这里可以输入版本号。如果你的 Mod 版本很多，那这时版本号会很有用。
# 如果你刚刚开始，那么建议把版本号设为 "1.0"
define config.version = "1.4.0"

# 这里是在“关于”页显示的 Mod 介绍文字。
# 由于我们重新启用了关于界面，你可以在这里写点介绍。
define gui.about = _("""这里是写简介的地方。在 options.rpy 里写上你的 Mod 简介吧！""")

# 这是 Ren'Py SDK 会读取的构建名。
# 构建名只能使用 ASCII 字符，因此只能使用英文字母，不能有空格、数字、下划线。
# 例：Sayori Is The Best → SayoriIsTheBest
define build.name = "DDLCModTempCN"

# 控制设置菜单中的音量设置显示
# 音效，建议保留为 True
define config.has_sound = True

# 背景音乐，建议保留为 True
define config.has_music = True

# 语音，如果 Mod 有语音则为 True，否则为 False
define config.has_voice = False

# 这里控制主菜单的背景音乐。
# audio.t1 是 Doki Doki Literature Club 的主菜单音乐。
# 如果你想修改，那么把 "t1" 改成其他已定义的 BGM。
define config.main_menu_music = audio.t1

# 这是进入和退出游戏菜单时使用的转场。
# Dissolve(.2) 相当于转场特效。
# config.enter_transition 控制进入游戏菜单时使用的转场。
# config.exit_transition 控制退出游戏菜单 / 返回游戏时使用的转场。
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# 这是加载存档后显示的转场。
# 默认情况下为 None，你可以自定义转场，但如果不确定，请保留为 None。
define config.after_load_transition = None

# 在故事结束后显示的转场。推荐使用 Dissolve(.2)。
define config.end_game_transition = Dissolve(.5)

# 对话窗显示设置
#   show - 总是显示
#   hide - 当要显示对话时才显示
#   auto - 在 scene 表达式之前隐藏，在对话显示时显示
#
# 使用 "window <type>" 更改
define config.window = "auto"

# transitions used to show / hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# default text speed
# 0 is infinite
# > 0 is number of characters per second
default preferences.text_cps = 50

# default auto-forward delay. 0 - 30.
default preferences.afm_time = 15

# default volumes
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# 存档位置
#   Windows: %appdata%\RenPy\<config.save_directory>
#   Mac: $HOME/Libary/RenPy/<config.save_directory>
#   Linux: $HOME/.renpy/<config.save_directory>
#
# must be a literal string
define config.save_directory = "DDLCModTempCN"

# 任务栏图标
define config.window_icon = "gui/window_icon.png"

# 是否允许快进
define config.allow_skipping = True

# True means we can autosave, false means not
define config.has_autosave = False

# True means autosave when we quit, False means not
define config.autosave_on_quit = False

# Number of autosave slots to use
define config.autosave_slots = 0

# 图层。如其名，图像显示的地方
# 最好别动
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# Other things to not mess with
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)



# BUILD CONFIG

init python:

    # the following functions take file pattern:
    # file patterns are case-insensitive and matched against the path relative to the
    # base directory, with and without a leading /. If multiple patterns match
    # the first is used.
    #
    # / is directory separator
    # * matches all characters, exxcept directory separator
    # ** matches all characters, including directory separator
    #
    # EXAMPLES
    # *.txt - matches txt files in base directory
    # game/**.ogg - mathces ogg files in game directory or subdirs of game
    # **.psd - matches psd files anywhere in project
    #
    # Classify files as None to exclusde them from the built distributions
    #

    # packaged ZIP for distibution
    build.package(build.directory_name + "Mod", 'zip', build.name, description='DDLC Compatible Mod')

    # archives to create
    build.archive("scripts", build.name)
    build.archive("mod_assets", build.name)
    build.archive("submods", build.name)

    # folder / files to put in archives
    build.classify("game/mod_assets/**", "mod_assets")
    build.classify("game/gui/**", "mod_assets") # issue #1
    build.classify("game/images/**", "mod_assets")
    build.classify("game/extensions/**", "extensions")
    build.classify("game/submods/**", "submods")
    build.classify('game/**.rpyc', "scripts")
    build.classify('game/advanced_scripts/**', "scripts")

    # stuff to ignore
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)

    # stuff not in archive
    build.classify('README.html', build.name)

    # Doki Doki Mod Manager 的元数据和 Mod 背景（v4）
    build.classify('ddmm-mod.json', build.name)
    build.classify('ddmm-bg.png', build.name)

    # mark as documentation
    build.documentation('README.html')

    build.include_old_themes = False
