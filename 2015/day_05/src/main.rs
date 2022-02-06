use std::fs;

const VOWELS: &str = "aeiou";
const NAUGHTY_LIST: [&str; 4] = ["ab", "cd", "pq", "xy"];

fn check_vowels(line: &str) -> bool {
    let count: u32 = line
        .chars()
        .map(|c| if VOWELS.contains(c) { 1 } else { 0 })
        .sum();
    count >= 3
}

fn check_twice_in_row(line: &str) -> bool {
    for i in 0..line.len() - 1 {
        if line.chars().nth(i) == line.chars().nth(i + 1) {
            return true;
        }
    }
    false
}

fn check_naughty_list(line: &str) -> bool {
    for naughty in NAUGHTY_LIST {
        if line.contains(naughty) {
            return false;
        }
    }
    true
}

fn solve_a(data: &str) -> u32 {
    let mut count = 0;
    for line in data.lines() {
        let result = check_vowels(line) & check_twice_in_row(line) & check_naughty_list(line);
        if result {
            count += 1;
        }
    }
    count
}

fn check_appears_twice(line: &str) -> bool {
    for i in 0..line.len() - 3 {
        let base: String = line.chars().skip(i).take(2).collect();
        let rest: String = line.chars().skip(i + 2).collect();
        if rest.contains(&base) {
            return true;
        }
        // println!("base: {}, rest: {}", base, rest)
    }
    false
}

fn check_twice_in_sanwitch(line: &str) -> bool {
    for i in 0..line.len() - 2 {
        if line.chars().nth(i) == line.chars().nth(i + 2) {
            return true;
        }
    }
    false
}

fn solve_b(data: &str) -> u32 {
    let mut count = 0;
    for line in data.lines() {
        let result = check_appears_twice(line) & check_twice_in_sanwitch(line);
        if result {
            count += 1;
        }
    }
    count
}

fn main() {
    let data = fs::read_to_string("input.txt").unwrap();
    println!("sol a: {}", solve_a(&data));
    println!("sol b: {}", solve_b(&data));
}
