use std::fs;

#[derive(Debug)]
struct Point {
    x: usize,
    y: usize,
}

#[derive(Debug)]
struct Instruction {
    instruction_type: String,
    start: Point,
    end: Point,
}

fn parse_line(line: &str) -> Instruction {
    let instruction_type;
    if line.contains("on") {
        instruction_type = "on";
    } else if line.contains("off") {
        instruction_type = "off";
    } else if line.contains("toggle") {
        instruction_type = "toggle";
    } else {
        panic!("Invalid instrucion!")
    }
    let mut split = line.split(' ');
    let mut end = split.nth_back(0).unwrap().split(',');
    let x_end = end.nth(0).unwrap().parse().unwrap();
    let y_end = end.nth(0).unwrap().parse().unwrap();

    let mut start = split.nth_back(1).unwrap().split(',');
    let x_start = start.nth(0).unwrap().parse().unwrap();
    let y_start = start.nth(0).unwrap().parse().unwrap();

    Instruction {
        instruction_type: instruction_type.to_string(),
        start: Point {
            x: x_start,
            y: y_start,
        },
        end: Point { x: x_end, y: y_end },
    }
}

fn solve(instructions: &str, part_a: bool) -> usize {
    let mut board = vec![vec![0; 1000]; 1000];

    for line in instructions.lines() {
        let instruction = parse_line(line);
        for i in instruction.start.x..instruction.end.x + 1 {
            for j in instruction.start.y..instruction.end.y + 1 {
                if part_a {
                    if instruction.instruction_type == "on" {
                        board[i][j] = 1
                    } else if instruction.instruction_type == "off" {
                        board[i][j] = 0
                    } else if instruction.instruction_type == "toggle" {
                        if board[i][j] == 0 {
                            board[i][j] = 1
                        } else if board[i][j] == 1 {
                            board[i][j] = 0
                        }
                    }
                } else {
                    if instruction.instruction_type == "on" {
                        board[i][j] += 1
                    } else if instruction.instruction_type == "off" {
                        if board[i][j] != 0 {
                            board[i][j] -= 1
                        }
                    } else if instruction.instruction_type == "toggle" {
                        board[i][j] += 2
                    }
                }
            }
        }
    }
    let mut sum = 0;
    for i in 0..1000 {
        for j in 0..1000 {
            sum += board[i][j]
        }
    }
    sum
}

fn main() {
    let instructions = fs::read_to_string("input.txt").unwrap();

    println!("Sol a: {}", solve(&instructions, true));
    println!("Sol a: {}", solve(&instructions, false));
}
