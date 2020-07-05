# 部分注释参照 https://github.com/GanstaKingofSA/DDLCModTemplate2.0

# 在这里命名你的 Mod
define config.name = "DDLC 中文 Mod 模板"

# 在主界面展示项目名、版本号 (True or False)
define gui.show_name = False

# 版本号
define config.version = "1.2.0"

# text placed on about screen
define gui.about = _("")

# 构建名，不要使用中文、数字、空格、分隔符，只使用英文
define build.name = "DDLCModTempCN"

# 控制设置菜单中的音量设置显示
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# 主菜单 BGM
define config.main_menu_music = audio.t1

# 进入和退出游戏菜单时使用的转场
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# 在加载存档后显示的转场
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

# 是否允许跳过
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
    build.classify("game/submods/**", "submods")
    build.classify('game/**.rpyc', "scripts")
    build.classify('game/advanced_scripts/**', "scripts")
    build.classify('game/original_story_scripts/**', "scripts")

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
