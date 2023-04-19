def solve_01():
    def parse_group(group):
        return [int(i) for i in group]

    with open("inputs/day_01.txt") as f:
        groups = [parse_group(group.split()) for group in f.read().split("\n\n")]
        
    sol_a = max(sum(group) for group in groups)
    sol_b = sum(sorted((sum(group) for group in groups), reverse=True)[:3])

    return sol_a, sol_b


def solve_02():
    with open("inputs/day_02.txt") as f:
        games = [line.strip() for line in f]

    def points_outcome(game):
        match game.split():
            # win
            case ("A", "Y") | ("B", "Z") | ("C", "X") : return 6
            # draw
            case ("A", "X") | ("B", "Y") | ("C", "Z") : return 3
            # lose
            case (_, _): return 0

    def points_shape(game):
        match game.split():
            case (_, "X"): return 1
            case (_, "Y"): return 2  
            case (_, "Z"): return 3

    def points(game):
        return points_outcome(game) + points_shape(game)

    def predict_shape(game):
        # X -> lose
        # Y -> draw
        # Z -> win
        match game.split():
            case ("A", "X"): return "A Z"
            case ("A", "Y"): return "A X"
            case ("A", "Z"): return "A Y"
            case ("B", "X"): return "B X"
            case ("B", "Y"): return "B Y"
            case ("B", "Z"): return "B Z"
            case ("C", "X"): return "C Y"
            case ("C", "Y"): return "C Z"
            case ("C", "Z"): return "C X"

    sol_a = sum(points(game) for game in games)
    sol_b = sum(points(predict_shape(game)) for game in games)

    return sol_a, sol_b


if __name__ == "__main__":
    solve_01()
    solve_02()


