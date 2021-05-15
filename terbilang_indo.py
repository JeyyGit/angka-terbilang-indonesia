def single_to_str(single_num):
    result = ""
    if single_num == 1:
        result = "satu"
    elif single_num == 2:
        result = "dua"
    elif single_num == 3:
        result = "tiga"
    elif single_num == 4:
        result = "empat"
    elif single_num == 5:
        result = "lima"
    elif single_num == 6:
        result = "enam"
    elif single_num == 7:
        result = "tujuh"
    elif single_num == 8:
        result = "delapan"
    elif single_num == 9:
        result = "sembilan"
    elif single_num == 10:
        result = "sepuluh"
    elif single_num == 11:
        result = "sebelas"
    return result


def first_part(part):
    result = 0
    if 20 <= part < 10**2:
        result = (part - part % 10) / 10
    elif 10**2 <= part < 10**3:
        result = (part - part % 10**2) / 10**2
    elif 10**3 <= part < 10**6:
        result = (part - part % 10**3) / 10**3
    elif 10**6 <= part < 10**9:
        result = (part - part % 10**6) / 10**6
    elif 10**9 <= part < 10**12:
        result = (part - part % 10**9) / 10**9
    elif 10**12 <= part < 10**15:
        result = (part - part % 10**12) / 10**12
    return result


def second_part(part):
    result = 0
    if 20 <= part < 10**2:
        result = part % 10
    elif 10**2 <= part < 10**3:
        result = part % 10**2
    elif 10**3 <= part < 10**6:
        result = part % 10**3
    elif 10**6 <= part < 10**9:
        result = part % 10**6
    elif 10**9 <= part < 10**12:
        result = part % 10**9
    elif 10**12 <= part < 10**15:
        result = part % 10**12
    return result


def dozen_to_str(dozen_num):
    dozen_num = single_to_str(dozen_num % 10)
    result = f"{dozen_num} belas"
    return result


def tens_to_str(tens_num):
    first_num = single_to_str(first_part(tens_num))
    second_num = single_to_str(second_part(tens_num))
    result = f"{first_num} puluh {second_num}"
    return result


def hundreds_to_str(hundreds_num):
    first_num = single_to_str(first_part(hundreds_num))
    last_part = check(second_part(hundreds_num))
    if hundreds_num < 2*10**2:
        result = f"seratus {last_part}"
    else:
        result = f"{first_num} ratus {last_part}"
    return result


def thousands_to_str(thousands_num):
    first_half = check(first_part(thousands_num))
    second_half = check(second_part(thousands_num))
    if thousands_num < 2*10**3:
        result = f"seribu {second_half}"
    else:
        result = f"{first_half} ribu {second_half}"
    return result


def millions_to_str(millions_num):
    first_half = check(first_part(millions_num))
    second_half = check(second_part(millions_num))
    result = f"{first_half} juta {second_half}"
    return result


def billions_to_str(billions_num):
    first_half = check(first_part(billions_num))
    second_half = check(second_part(billions_num))
    result = f"{first_half} milyar {second_half}"
    return result


def trillions_to_str(trillions_num):
    first_half = check(first_part(trillions_num))
    second_half = check(second_part(trillions_num))
    result = f"{first_half} triliun {second_half}"
    return result


def check(num):
    result = ""
    if 1 <= num < 12:
        result = single_to_str(num)
    elif 12 <= num < 20:
        result = dozen_to_str(num)
    elif 20 <= num < 10**2:
        result = tens_to_str(num)
    elif 10**2 <= num < 10**3:
        result = hundreds_to_str(num)
    elif 10**3 <= num < 10**6:
        result = thousands_to_str(num)
    elif 10**6 <= num < 10**9:
        result = millions_to_str(num)
    elif 10**9 <= num < 10**12:
        result = billions_to_str(num)
    elif 10**12 <= num < 10**15:
        result = trillions_to_str(num)
    elif num == 0:
        print("")
    else:
        print("Number too large.")
    return result


def num_to_str(num):
    if num == 0:
        return "nol"
    elif num < 0:
        return f"negatif {check(abs(num))}"
    else:
        return check(num)


while True:
    inp = input("Nomor : ")
    if inp == "exit":
        break
    else:
        print(num_to_str(int(inp)))
        print("")
