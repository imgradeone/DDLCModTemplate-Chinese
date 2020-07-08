# DDMM SDK v4.0.0-prerelease-CNModTemp

# Initialise the DDMM SDK
init -10 python:
    import urllib2, json
    ddmm_rpc_url = "http://127.0.0.1:41420/"

    def ddmm_check_online():
        try:
            request = urllib2.Request(ddmm_rpc_url, json.dumps({"method": "ping"}))
            urllib2.urlopen(request).read()
            return True
        except:
            return False
        return False

    def ddmm_make_request(payload):
        if ddmm_check_online():
            request = urllib2.Request(ddmm_rpc_url, json.dumps(payload))
            urllib2.urlopen(request).read()

    def ddmm_register_achievement(id, name, description):
        ddmm_make_request({"method": "register achievement", "payload": {"id": id, "name": name, "description": description}})

    def ddmm_earn_achievement(id):
        ddmm_make_request({"method": "earn achievement", "payload": {"id": id}})

# Register an achievement with Doki Doki Mod Manager
# id = the unique ID of the achievement, can be any string
# name = the user-facing name of the achievement
# description = the user-facing description of the achievement
label ddmm_register_achievement(id, name, description):
    $ ddmm_register_achievement(id, name, description)    
    return

# Earn an achievement
# id = the unique ID of the achievement
label ddmm_earn_achievement(id):
    $ ddmm_earn_achievement(id)        
    return

label _reg_achievements:
    python:
        ddmm_register_achievement("TEST_ACHIEVEMENT", "测试成就", "可以从教程菜单获得")
        ddmm_register_achievement("MONIKA_ROUTE_COMPLETE", "只要 Monika", "完成 Monika 路线的编程")
        achievement.register("测试成就")
        achievement.register("只要 Monika")
    
    return

# Test SDK functions
# Ren'Py 测试有限
label _ddmm_test:
    $ ddmm_online = ddmm_check_online()
    "DDMM 是否在线：[ddmm_online]"
    menu:
        "请选择想要测试的项。"
        "重新测试在线状态":
            pass # 像我们没做什么一样
        "注册成就": # TODO: 在 init -10 块中添加 call 之后移除这个选择
            call _reg_achievements from _call__reg_achievements
            "已注册成就。"
        "达成 测试成就":
            $ ddmm_earn_achievement("TEST_ACHIEVEMENT")
        "判断测试成就状态（原生）":
            $ ifnot = achievement.has("测试成就")
            m "状态：[ifnot]"
        "测试成就 (Ren'Py)":
            $ achievement.grant("测试成就")
        "达成 只要 Monika":
            $ ddmm_earn_achievement("MONIKA_ROUTE_COMPLETE")
        "退出":
            return
            # pass
    call _ddmm_test from _call_ddmm_test_2
    return
