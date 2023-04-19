def solve_01():
    def parse_group(group):
        return [int(i) for i in group]

    with open("inputs/day_01.txt") as f:
        groups = [parse_group(group.split()) for group in f.read().split("\n\n")]
        
    sol_a = max(sum(group) for group in groups)
    sol_b = sum(sorted((sum(group) for group in groups), reverse=True)[:3])

    return sol_a, sol_b



if __name__ == "__main__":
    solve_01()


