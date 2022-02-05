use std::fs;

fn solve_a(raw_data: &str) -> i32 {
    let mut floor = 0;
    for c in raw_data.chars() {
        if c == '(' {
            floor += 1
        } else if c == ')' {
            floor -= 1
        }
    }
    floor
}

fn solve_b(raw_data: &str) -> usize {
    let mut floor = 0;
    for (i, c) in raw_data.chars().enumerate() {
        if c == '(' {
            floor += 1
        } else if c == ')' {
            floor -= 1
        }

        if floor < 0 {
            return i + 1;
        }
    }
    panic!("Crash, solution not found!")
}

fn main() {
    let raw_data = fs::read_to_string("input.txt").expect("Something wrong with the file");
    let solution_a = solve_a(&raw_data);
    println!("The part a result is: {}", solution_a);

    let solution_b = solve_b(&raw_data);
    println!("The part b result is: {}", solution_b);
}
