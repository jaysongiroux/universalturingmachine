def alphabet(a):
    if a == "a": return "1"
    if a == "b": return "11"
    if a == "c": return "111"
    if a == "d": return "1111"
    if a == "e": return "11111"
    if a == "f": return "111111"
    if a == "g": return "1111111"
    if a == "h": return "11111111"
    if a == "i": return "111111111"
    if a == "j": return "1111111111"
    if a == "k": return "11111111111"
    if a == "l" or a=="L": return "111111111111"
    if a == "m": return "1111111111111"
    if a == "n": return "11111111111111"
    if a == "o": return "111111111111111"
    if a == "p": return "1111111111111111"
    if a == "q": return "11111111111111111"
    if a == "r" or a =="R": return "111111111111111111"
    if a == "s": return "1111111111111111111"
    if a == "t": return "11111111111111111111"
    if a == "u": return "111111111111111111111"
    if a == "v": return "1111111111111111111111"
    if a == "w": return "11111111111111111111111"
    if a == "x" or a == "X": return "111111111111111111111111"
    if a == "y" or a == "Y": return "1111111111111111111111111"
    if a == "z": return "11111111111111111111111111"
    # space
    if a == "Δ" or a == " " or a == "\u0394" or "Δ" in a or "\u0394" in a:
        return "111111111111111111111111111"
    if a == "-": return "1111111111111111111111111111"
    if a == "[": return "11111111111111111111111111111"
    if a == "]": return "111111111111111111111111111111"
    # space delta, as of right now cannot compare unicode char's reliably
    else:
        return "111111111111111111111111111"



