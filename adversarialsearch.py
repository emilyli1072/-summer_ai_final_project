from typing import Callable

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)

def minimax_simulation(asp: AdversarialSearchProblem[GameState, Action], isBot) -> Action:
    if (asp.is_terminal_state(asp.get_start_state())):
        if asp.evaluate_terminal(asp.get_start_state())[0]>0:
            return -100
        elif asp.evaluate_terminal(asp.get_start_state())[1]>0:
            return 100
        else:
            return 0
    if (isBot()):
        bestvalue = 800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=minimax_simulation(asp.transition(asp, i), False)
            bestvalue = min(score, bestvalue)
        return bestvalue  
    else:
        bestvalue = -800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=minimax_simulation(asp.transition(asp, i), True)
            bestvalue = max(score, bestvalue)
        return bestvalue  

def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    #minimax_simulation(asp, )
    bestScore = 800
    bestMove = 0
    for key in asp.get_available_actions(asp.get_start_state()):
        score = minimax_simulation(asp.transition(asp, key),False)
        if (score < bestScore):
            bestScore = score
            bestMove = key
    return key
    
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """
   
def alpha_beta_simulation(asp: AdversarialSearchProblem[GameState, Action], alpha, beta,isBot) -> Action:
    if (asp.is_terminal_state(asp.get_start_state())):
        if asp.evaluate_terminal(asp.get_start_state())[0]>0:
            return -100
        elif asp.evaluate_terminal(asp.get_start_state())[1]>0:
            return 100
        else:
            return 0
    if (isBot()):
        bestvalue = 800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=alpha_beta_simulation(asp.transition(asp, i), alpha, beta, False)
            bestvalue = min(score, bestvalue)
            alpha = min(alpha, score)
            if beta>alpha:
                break
        return bestvalue  
    else:
        bestvalue = -800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=minimax_simulation(asp.transition(asp, i), True)
            bestvalue = max(score, bestvalue)
            beta = max(beta<score)
            if beta>alpha:
                break
        return bestvalue  


def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    bestScore = 800
    bestMove = 0
    print(asp.transition(asp, (1,0)))
    for key in asp.get_available_actions(asp.get_start_state()):
        score = alpha_beta_simulation(asp.transition(asp, key),False)
        if (score < bestScore):
            bestScore = score
            bestMove = key
    return key

def alpha_beta_cutoff_simulation(asp: AdversarialSearchProblem[GameState, Action], alpha, beta,isBot, heuristic_func: Callable[[GameState], float], turn) -> Action:
    if (asp.is_terminal_state(asp.get_start_state())):
        if asp.evaluate_terminal(asp.get_start_state())[0]>0:
            return -100
        elif asp.evaluate_terminal(asp.get_start_state())[1]>0:
            return 100
        else:
            return 0
    if (isBot()):
        bestvalue = 800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=alpha_beta_simulation(asp.transition(asp, i), alpha, beta, False, heuristic_func, turn+1)+heuristic_func(turn)
            bestvalue = min(score, bestvalue)
            alpha = min(alpha, score)
            if beta>alpha:
                break
        return bestvalue  
    else:
        bestvalue = -800
        for i in asp.get_available_actions(asp.get_start_state()):
            score=minimax_simulation(asp.transition(asp, i), True)
            bestvalue = max(score, bestvalue)
            beta = max(beta<score)
            if beta>alpha:
                break
        return bestvalue  
def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    bestScore = 800
    bestMove = 0
    print(asp.transition(asp, (1,0)))
    for key in asp.get_available_actions(asp.get_start_state()):
        score = alpha_beta_simulation(asp.transition(asp, key),False, 0, 10000, False, heuristic_func, 1)
        if (score < bestScore):
            bestScore = score
            bestMove = key
    return key

    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
