###### --------------------------------------------
## The author of these scripts is T. D. Devlin
###### --------------------------------------------

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 1
# A says "I am both a knight and a knave."
# ----------------------------------------
##   write the statement(s) in PL
stat = And(AKnight, AKnave)
##   Fill in the knowledge base
knowledge1 = And(
    Xor(AKnight, AKnave), Implication(AKnight, stat), Implication(AKnave, Not(stat))
)
# ----------------------------------------

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# ----------------------------------------
##   write the statement(s) in PL
stat = And(
    Xor(AKnight, AKnave),
    Xor(BKnight, BKnave),
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)

##   Fill in the knowledge base
knowledge2 = And(stat)
# ----------------------------------------

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# ----------------------------------------
##   write the statement(s) in PL
stat = Or(And(AKnight, BKnight), And(AKnave, BKnave))

##   Fill in the knowledge base
knowledge2 = And(
    Xor(AKnight, AKnave),
    Xor(BKnight, BKnave),
    Implication(AKnight, stat),
    Implication(AKnave, Not(stat)),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)
# ----------------------------------------


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
