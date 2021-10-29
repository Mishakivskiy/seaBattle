def clean_userID(el):
    l = len(el)
    i = 0
    while i < l:
        s_int = ''
        a = el[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = el[i]
            else:
                break
        i += 1
        if s_int != '':
            return int(s_int)

def print_field(field):
    field_s = """↘️1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟\n"""
    for i in range(0, 10):
        for j  in range(0, 11):
            if j == 0 and i == 0:
                field_s += "1️⃣"
            elif j == 0 and i == 1:
                field_s += "2️⃣"
            elif j == 0 and i == 2:
                field_s += "3️⃣"
            elif j == 0 and i == 3:
                field_s += "4️⃣"
            elif j == 0 and i == 4:
                field_s += "5️⃣"
            elif j == 0 and i == 5:
                field_s += "6️⃣"
            elif j == 0 and i == 6:
                field_s += "7️⃣"
            elif j == 0 and i == 7:
                field_s += "8️⃣"
            elif j == 0 and i == 8:
                field_s += "9️⃣"
            elif j == 0 and i == 9:
                field_s += "🔟"
            elif j != 0 and field[i][j-1] == 0:
                field_s += "🟦"
            elif j != 0 and field[i][j-1] == 1:
                field_s += "⬛"
            elif j != 0 and field[i][j-1] == 2:
                field_s += "❌"
            elif j != 0 and field[i][j-1] == 3:
                field_s += "🔘"

        field_s += "\n"

    return field_s


