from app_config import MINE_TOLERANCE


def proof_of_work(old_proof):
    incrementor = old_proof + 1

    while not (incrementor % MINE_TOLERANCE == 0 and incrementor % old_proof == 0):
        incrementor += 1

    return incrementor
