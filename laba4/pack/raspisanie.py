def ras(a):
    if a == "pon" :
        return ["org 11:15 - 12:45"]
    elif a == "vto":
        return ["ecomika 9:30 - 11:00", "org 13:00 - 14:30", "algebra 15:10 - 16:40", "fizika 16:55 - 18:25"]
    elif a == "sre":
        return ["kibernetica 9:30 - 11:00", "viit 11:15 - 12:45", "fizra 13:00 - 14:30"]
    elif a == "che":
        return ["economika 9:30 - 11:00", "algebra 11:15 - 12:45", "angliskiy 13:00 - 14:30"]
    elif a == "pya":
        return ["viit 11:15 - 12:45", ""]