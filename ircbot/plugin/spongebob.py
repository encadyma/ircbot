"""Create a sentence with random capitalization"""
from itertools import cycle
from random import random


def register(bot):
    bot.listen(r'^!spongebob (.+)', spongemock)


def spongemock(bot, msg):
    """HaVe CReaTE mOCk A SEnTeNCe."""
    text = msg.match.group(1)
    if len(text) < 2:
        msg.respond(text, ping=False)
        return

    alpha = 0.25 if len(text) < 10 else 0.45
    fn_set = sorted([str.upper, str.lower], key=lambda _: random())
    fn_cycle = cycle(fn_set)

    spongebob = ''
    case_dup = 1
    transform_fn = next(fn_cycle)
    for c in text:
        spongebob += transform_fn(c)

        if not c.isalpha():
            continue

        # Exponentially decrease the chance of getting same case
        if random() > alpha ** case_dup:
            transform_fn = next(fn_cycle)
            case_dup = 1
        else:
            case_dup += 1

    msg.respond(spongebob, ping=False)
