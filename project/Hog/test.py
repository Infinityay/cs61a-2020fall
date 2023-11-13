from hog import play, always_roll, extra_turn, take_turn, other, silence, GOAL_SCORE
from dice import make_test_dice, six_sided


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(num_rolls=strategy0(score0, score1), opponent_score=score1,
                                dice=dice)
            if not extra_turn(score0, score1):
                who = other(who)
        elif who == 1:
            score1 += take_turn(num_rolls=strategy1(score1, score0), opponent_score=score0,
                                dice=dice)
            if not extra_turn(score1, score0):
                who = other(who)

        say(score0, score1)
    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"

    # END PROBLEM 6
    return score0, score1


#
# Ensure that say is properly updated within the body of play.
def total(s0, s1):
    print(s0 + s1)
    return echo


def echo(s0, s1):
    print(s0, s1)
    return total


s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
