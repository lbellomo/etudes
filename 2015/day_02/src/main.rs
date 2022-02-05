use std::fs;

fn parse_line(line: &str) -> (i32, i32, i32) {
    let numbers: Vec<i32> = line.split("x").map(|x| x.parse().unwrap()).collect();
    (numbers[0], numbers[1], numbers[2])
}

fn solve_a(raw_input: &str) -> i32 {
    let mut sum = 0;
    for line in raw_input.lines() {
        let (l, w, h) = parse_line(&line);
        let sides = vec![l * w, w * h, h * l];
        let smallest_side = sides.iter().min().unwrap();

        sum += (2 * l * w) + (2 * w * h) + (2 * h * l) + smallest_side;
    }
    sum
}

fn solve_b(raw_input: &str) -> i32 {
    let mut sum = 0;
    for line in raw_input.lines() {
        let (l, w, h) = parse_line(&line);
        let mut sides = vec![l, w, h];
        let max: i32 = *sides.iter().max().unwrap();
        sides.remove(sides.iter().position(|x| *x == max).unwrap());
        sum += l * w * h + (sides[0] + sides[1]) * 2
    }
    sum
}

fn main() {
    let raw_input = fs::read_to_string("input.txt").expect("Something wrong reading the file!");

    println!("Sol a: {}", solve_a(&raw_input));
    println!("Sol b: {}", solve_b(&raw_input));
}
