import random

diary_text1 = "It seems I had the same dream. I have no idea what’s causing it. Perhaps it’s all the practice, trying to become a seeker. Maybe it’s just stress from school. Whatever it is, I woke up again aroused, soaked panties and unable to talk to anyone in my house about it. It’s just so embarrassing. Not only that I was covered in sweat. I assumed someone had been performing some sort of legilimency for such a thing to happen but even after checking outside our room, I realized there was no one there. What is wrong with me?"
diary_text2 = "Ah, how I love quidditch, it’s the only thing that keeps me sane these days. Between the erotic legilimency that seems to afflict me or being done by someone and all the schoolwork, it’s a true break from it all. I have one task, to catch the snitch but alas, I can’t seem to. That doesn’t make it any less fun but it would be nice to catch it just once and make the team so that I can actually play in a real match."
diary_text1 = "".join(random.sample(diary_text1, len(diary_text1)))
diary_text2 = "".join(random.sample(diary_text2, len(diary_text2)))
while "  " in diary_text1:
    diary_text1 = diary_text1.replace("  ", " ")
while "  " in diary_text2:
    diary_text2 = diary_text2.replace("  ", " ")

print(diary_text1)
print(diary_text2)
