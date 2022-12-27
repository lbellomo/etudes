fn main() {
    let input = include_str!("input.txt");

    let sol_a: u32 = input
        .lines()
        .map(|line| {
            let (first, second) = line.split_at(line.len() / 2);
            let priority = first.chars().find(|&x| second.contains(x)).unwrap();
            dbg!(priority, priority as u32);

            match priority.is_lowercase() {
                true => priority as u32 + 1 - 'a' as u32,
                false => priority as u32 + 1 - 'A' as u32 + 26,
            }
        })
        .sum();

    let vec_input = input.lines().collect::<Vec<_>>();

    // for group in vec_input.chunks(3) {
    let sol_b: u32 = vec_input
        .chunks(3)
        .map(|group| {
            // let hashset = HashSet::new();
            if let [a, b, c] = group {
                let priority = a.chars().find(|&x| b.contains(x) && c.contains(x)).unwrap();

                match priority.is_lowercase() {
                    true => priority as u32 + 1 - 'a' as u32,
                    false => priority as u32 + 1 - 'A' as u32 + 26,
                }
            } else {
                panic!("Invalid input")
            }
        })
        .sum();

    println!("sol_a: {sol_a}");
    println!("sol_b: {sol_b}");
}
