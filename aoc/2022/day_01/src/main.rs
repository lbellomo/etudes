use itertools::Itertools;
use std::cmp::Reverse;

fn main() {
    let input = include_str!("input.txt");

    let top_elfs = input
        .lines()
        .map(|v| v.parse::<i32>().ok())
        .batching(|it| {
            let mut sum = None;
            while let Some(Some(v)) = it.next() {
                sum = Some(sum.unwrap_or(0) + v);
            }
            sum
        })
        .map(Reverse)
        .k_smallest(3)
        .map(|x| x.0)
        .collect::<Vec<i32>>();

    let sol_a = top_elfs.iter().max().unwrap();
    println!("sol_a: {sol_a}");
    let sol_b: i32 = top_elfs.iter().sum();
    println!("sol_b: {sol_b}");
}
