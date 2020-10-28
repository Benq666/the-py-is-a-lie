text = "At midnight , in the month of June , I stand beneath the mystic moon . An opiate vapor , dewy , dim , Exhales from out her golden rim , And , softly dripping , drop by drop , Upon the quiet mountain top , Steals drowsily and musically , Into the universal valley . The rosemary nods upon the grave ; The lily lolls upon the wave ; Wrapping the fog about its breast , The ruin molders into rest ; Looking like Lethe , see ! the lake , A conscious slumber seems to take , And would not , for the world , awake . All Beauty sleeps ! - and lo ! where lies Irene , with her Destinies !"

tokens = text.split(" ")
tokens.insert(0, "<START>")
tokens.append("<END>")

while len(tokens) > 1:
    token_1 = tokens.pop(0)
    token_2 = tokens.pop(0)
    tokens.insert(0, token_2)
    print(token_1 + " " + token_2)
