# User inputs
print("""
Welcome to Zoul's Love Calculator.

We will be asking you a few questions regarding your love life. After all the questions have been answered, we will run our program and calculate how compatible both you and your partner are with each other.

Please answer as truthfully and succinctly as possible.

Ready? Let us begin.
""")

myName = input("Firstly, what is your name? ").capitalize()
theirName = input("And the name of your partner? ").capitalize()

adj1 = input("\nTell me an adjective that describes you: ").lower()
adj2 = input("And one that describes your partner: ").lower()

petName = input("\nTell me your partner's pet name for you: ").lower()
nickName = input("What the pet name you give them? ").lower()

profession1 = input("\nWhen you were young, what did you wish to be when you grow up? ").lower()
profession2 = input("And what is your profession now? ").lower()

print("\nYou are halfway done with the questions. Please be patient for a little bit more.")
shout = input("\nWhat would you say if your partner is not listening to you? ").upper()

randomFact = input("\nWhat is a random fun fact about you? You are... ").lower()

print("\nThink of 2 words that rhyme.")
rhymeWord1 = input("First rhyming word: ").capitalize()
rhymeWord2 = input("Second rhymind word: ").capitalize()

print("\nLast 5 questions! Keep it up!")
drink = input("What would you drink on a date? ").lower()

verbIng = input("\nBiggest pet peeve? ").lower()

adviceToShyTeen = input("\nWhat would you tell your younger self? ").capitalize()

print("\nAnd the last 2 questions:")
bodyPart1 = input("Which body part draws your attention first when you met them? ").lower()
bodyPart2 = input("What is the most ticklish part on your body? ").lower()

# Oopsie you have been trolled

print("""
Thank you for your input. 

Unfortunately, you have been trolled by Zoul. He has received your inputs and cleverly inserted them in this transcript of Halo, a game he loves playing since he was a kid.

Enjoy reading!
""")
print(input("[Press Enter to continue]"))

# This script has been sampled from Halo by Wesker

print(f"""
Cortana (broadcasting through ship): 
Attention all \033[92m{petName}\033[0m! Please report to your \033[92m{nickName}\033[0m.
""")
print(input("[Press Enter to continue]"))

print(f"""
Sergeant: 
You heard \033[92m{myName}\033[0m, move like you got a purpose.
""")
print(input("[Press Enter to continue]"))

print(f"""
\033[92m{myName}\033[0m: 
This is not a drill. I repeat, this is not a drill.
""")
print(input("[Press Enter to continue]"))

print(f"""
Sergeant:
Men...keep your eyes downrange, fingers on your \033[92m{bodyPart2}\033[0m, and we all go home in one piece.
""")
print(input("[Press Enter to continue]"))

print(f"""
We led those dumb \033[92m{profession1}s\033[0m out to the middle of nowhere to keep 'em from gettin' their filthy \033[92m{bodyPart1}\033[0m on \033[92m{theirName}\033[0m. 
""")
print(input("[Press Enter to continue]"))

print(f"""
But, we stumbled onto somethin' they're so \033[92m{adj1}\033[0m for, that they're \033[92m{verbIng}\033[0m to get it. 
""")
print(input("[Press Enter to continue]"))

print(f"""
Well, I don't care if it's God's own personal anti-son-of-a-bitch machine, or a giant \033[92m{rhymeWord1} {rhymeWord2}\033[0m, we're not gonna let 'em have it!
""")
print(input("[Press Enter to continue]"))

print(f"""
What we will let 'em have is \033[92m{randomFact}\033[0m, and a pool of their own \033[92m{drink}\033[0m to drown in! (Pause) 
""")
print(input("[Press Enter to continue]"))

print(f"""
(Slow and loud) \033[92m{shout}\033[0m!

Marines: Sir, yes sir!
""")
print(input("[Press Enter to continue]"))

print(f"""
Sergeant: 
UM HM damn right I am. Now move it out \033[92m{adj2}\033[0m time.

\033[92m{myName}\033[0m: 
Attention all personnel, we are reengaging the enemy. External and internal contact imminent.
""")
print(input("[Press Enter to continue]"))

print(f"""
Sergeant: 
All you \033[92m{profession2}s\033[0m who wanted to see \033[92m{theirName}\033[0m up close, this is gonna be your lucky day. \033[92m{adviceToShyTeen}\033[0m!
""")