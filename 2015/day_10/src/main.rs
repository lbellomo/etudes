use std::char;

fn look_and_say(num: &str) -> String {
    let mut result = String::new();
    let mut ch_count = 1;
    for (i, ch) in num.chars().enumerate() {
        // println!("{} {}", i, num.len());
        if i + 1 == num.len() {
            result.push(char::from_digit(ch_count, 10).unwrap());
            result.push(ch);
            // println!("count: {ch_count}, ch: {ch}");
            ch_count = 1;
        } else if ch == num.chars().nth(i + 1).unwrap() {
            ch_count += 1;
        } else {
            result.push(char::from_digit(ch_count, 10).unwrap());
            result.push(ch);
            // println!("count: {ch_count}, ch: {ch}");
            ch_count = 1;
        }
    }
    result
}

fn solve(num: &str, n: usize) -> usize {
    let mut num = String::from(num);

    for i in 0..n {
        num = look_and_say(&num);
        println!("{i}");
    }
    num.len()
}

fn main() {
    let mut num = "1113122113";

    println!("sol a: {}", solve(&num, 40));
    // this is super slow, don't work:
    // println!("sol a: {}", solve(&num, 50));
}
