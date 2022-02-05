use std::collections::HashSet;
use std::fs;

fn navigate(data: &str) -> HashSet<(i32, i32)> {
    let mut x = 0;
    let mut y = 0;
    let mut know_pos = HashSet::new();
    know_pos.insert((x, y));

    for c in data.chars() {
        match c {
            '^' => y += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            '>' => x += 1,
            _ => panic!("invalid data!"),
        }

        know_pos.insert((x, y));
    }
    know_pos
}

fn solve_a(data: &str) -> i32 {
    navigate(data).len() as i32
}

fn solve_b(data: &str) -> i32 {
    let mut santa_data = String::new();
    let mut robot_data = String::new();
    for (i, c) in data.chars().enumerate() {
        match i % 2 {
            0 => santa_data.push(c),
            1 => robot_data.push(c),
            _ => (),
        }
    }
    let navigation_santa = navigate(&santa_data);
    let navigation_robot = navigate(&robot_data);

    let sol: HashSet<_> = navigation_santa.union(&navigation_robot).collect();
    sol.len() as i32
}

fn main() {
    let data = fs::read_to_string("input.txt").unwrap();
    println!("Sol a: {}", solve_a(&data));
    println!("Sol b: {}", solve_b(&data));
}
