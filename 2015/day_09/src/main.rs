use itertools::Itertools;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;

fn parse_raw_data(raw_data: &str) -> (HashMap<(&str, &str), usize>, HashSet<&str>) {
    let mut distances = HashMap::new();
    let mut uniques = HashSet::new();
    for line in raw_data.lines() {
        let (rest, value) = line.split(" = ").collect_tuple().unwrap();
        let value: usize = value.parse().unwrap();
        let (start, end) = rest.split(" to ").collect_tuple().unwrap();
        uniques.insert(start);
        uniques.insert(end);
        distances.insert((start, end), value);
    }
    (distances, uniques)
}

fn find_distance(
    perm: Vec<&&str>,
    len_uniques: usize,
    distances: &HashMap<(&str, &str), usize>,
) -> Option<usize> {
    let mut count = 0;
    for i in 0..len_uniques - 1 {
        if distances.contains_key(&(perm[i], perm[i + 1])) {
            count += distances.get(&(perm[i], perm[i + 1])).unwrap();
        } else if distances.contains_key(&(perm[i + 1], perm[i])) {
            count += distances.get(&(perm[i + 1], perm[i])).unwrap();
        } else {
            return None;
        }
    }
    Some(count)
}

fn solve_a(distances: &HashMap<(&str, &str), usize>, uniques: &HashSet<&str>) -> usize {
    let mut min_distance = 10000000;
    for perm in uniques.iter().permutations(uniques.len()) {
        let perm_distance = find_distance(perm, uniques.len(), &distances).unwrap();
        if perm_distance < min_distance {
            min_distance = perm_distance;
        }
    }
    min_distance
}

fn solve_b(distances: &HashMap<(&str, &str), usize>, uniques: &HashSet<&str>) -> usize {
    let mut max_distance = 0;
    for perm in uniques.iter().permutations(uniques.len()) {
        let perm_distance = find_distance(perm, uniques.len(), &distances).unwrap();
        if perm_distance > max_distance {
            max_distance = perm_distance;
        }
    }
    max_distance
}

fn main() {
    let raw_data = fs::read_to_string("input.txt").unwrap();

    let (distances, uniques) = parse_raw_data(&raw_data);

    println!("sol_a: {}", solve_a(&distances, &uniques));
    println!("sol_b: {}", solve_b(&distances, &uniques));
}
