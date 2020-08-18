#This is a copy of glitchtext.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#This defines a single function that generates garbage text of a given character length
init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output
#符语模式
init python:
    import random

    agws = "啊wee改哈鞥嫦娥我刚不疤痕处哈维楚王嗡阿格王朔鸡e句NBA我是猪tix来试谱啊11宝宝呢囜您呢你娘比起重机顿珍汉努！碹镑铱鸹紫薯布丁*8则不呢就美丽了"

    def fujaowee(length):
        output = ""
        for x in range(length):
            output += random.choice(agws)
        return output
