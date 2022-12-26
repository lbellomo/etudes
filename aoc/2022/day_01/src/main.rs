use std::fs;
use std::collections::HashMap;

fn main() {
    let raw_data = fs::read_to_string("input.txt").unwrap();

    let mut elfs = HashMap::new();
    let mut i = 0;
    let mut count = 0;

    for line in raw_data.split('\n') {
        match line {
            "" => {
                elfs.insert(i, count);
                i += 1;
                count = 0;
            }
            _ => count += line.parse::<i32>().unwrap()
        }
    }
    let sol_a = elfs.values().max().unwrap();
    println!("sol_a: {sol_a}");

    let mut values: Vec<i32> = elfs.into_values().collect();
    values.sort();
    values.reverse();
    let sol_b = &values[0..3].iter().sum::<i32>();
    println!("sol_b: {sol_b}");

}
