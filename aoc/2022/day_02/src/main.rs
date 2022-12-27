fn main() {
    let input = include_str!("input.txt");
    let sol_a: i32 = input
        .lines()
        .map(|line| line.split_at(1))
        .map(|(opponent, you)| {
            let you = you.trim();
            let mut point = 0;
            match you {
                "X" => point += 1,
                "Y" => point += 2,
                "Z" => point += 3,
                _ => {}
            }

            match (opponent, you) {
                ("A", "Y") | ("B", "Z") | ("C", "X") => point += 6,
                ("A", "X") | ("B", "Y") | ("C", "Z") => point += 3,
                _ => point += 0,
            }
            point
        })
        .sum();

    let sol_b: i32 = input
        .lines()
        .map(|line| line.split_at(1))
        .map(|(opponent, target)| {
            let target = target.trim();

            let you = match (opponent, target) {
                ("A", "Z") | ("B", "Y") | ("C", "X") => "Y",
                ("B", "Z") | ("C", "Y") | ("A", "X") => "Z",
                ("C", "Z") | ("A", "Y") | ("B", "X") => "X",
                _ => panic!("invalid input"),
            };

            let mut point = 0;
            match you {
                "X" => point += 1,
                "Y" => point += 2,
                "Z" => point += 3,
                _ => {}
            }

            match (opponent, you) {
                ("A", "Y") | ("B", "Z") | ("C", "X") => point += 6,
                ("A", "X") | ("B", "Y") | ("C", "Z") => point += 3,
                _ => point += 0,
            }
            point
        })
        .sum();

    println!("sol_a = {sol_a}");
    println!("sol_b = {sol_b}")
}
