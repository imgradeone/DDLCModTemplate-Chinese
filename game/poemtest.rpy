label poemtest:

    menu:
        "测试选项？"

        "Monika":
            call showpoem(poem_cn_m1, music=False) from _call_showpoem
            pass
        "Sayori":
            call showpoem(poem_cn_s1, music=False) from _call_showpoem_1
            pass
        "Yuri":
            call showpoem(poem_cn_y1, music=False) from _call_showpoem_2
            pass
        "Natsuki":
            call showpoem(poem_cn_n1, music=False) from _call_showpoem_3
            pass

    return
        