def get_birthstone(month):
    birthstones = {
        1: "Garnet",
        2: "Amethyst",
        3: "Aquamarine",
        4: "Diamond",
        5: "Emerald",
        6: "Pearl",
        7: "Ruby",
        8: "Peridot",
        9: "Sapphire",
        10: "Opal",
        11: "Topaz",
        12: "Turquoise"
    }

    if month in birthstones:
        return birthstones[month]
    else:
        return "Invalid month"

month = int(input("Enter the month (1-12): "))
birthstone = get_birthstone(month)
print("Your birthstone is:", birthstone)

