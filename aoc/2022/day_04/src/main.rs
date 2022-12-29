#[derive(Debug)]
struct Pair {
    first: Assignment,
    last: Assignment,
}

impl Pair {
    fn new(line: &str) -> Self {
        let (first, last) = line.split_once(',').unwrap();
        Pair {
            first: Assignment::new(first),
            last: Assignment::new(last),
        }
    }

    fn compare_a(&self) -> bool {
        ((self.first.start >= self.last.start) & (self.first.end <= self.last.end))
            | ((self.last.start >= self.first.start) & (self.last.end <= self.first.end))
    }

    fn compare_b(&self) -> bool {
        let f = self.first;
        let l = self.last;
        ((f.start <= l.start) & (l.start <= f.end))
            | ((f.start <= l.end) & (l.end <= f.end))
            | ((l.start <= f.start) & (f.start <= l.end))
            | ((l.start <= f.end) & (f.end <= l.end))
    }
}
#[derive(Debug, Clone, Copy)]
struct Assignment {
    start: u64,
    end: u64,
}

impl Assignment {
    fn new(half_line: &str) -> Self {
        let (start, end) = half_line.split_once('-').unwrap();
        let start: u64 = start.parse().unwrap();
        let end: u64 = end.parse().unwrap();
        Assignment { start, end }
    }
}

fn main() {
    let input = include_str!("input.txt");

    let sol_a: u64 = input
        .lines()
        .map(Pair::new)
        .map(|x| std::convert::Into::<u64>::into(x.compare_a()))
        .sum();

    let sol_b: u64 = input
        .lines()
        .map(Pair::new)
        .map(|x| std::convert::Into::<u64>::into(x.compare_b()))
        .sum();

    println!("sol_a: {sol_a}");
    println!("sol_b: {sol_b}");
}
