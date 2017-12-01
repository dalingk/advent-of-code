use std::fs::File;
use std::path::Path;
use std::io::prelude::*;
use std::vec::Vec;

fn convert_char(c: char) -> u8 {
    c.to_digit(10).unwrap() as u8
}

fn load_file(path: &Path) -> Vec<u8> {
    let mut file = File::open(path).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    return contents.chars().map(|x| convert_char(x)).collect::<Vec<u8>>();
}

fn main() {
    let path = Path::new("../resources/day1.txt");
    let nums = load_file(&path);
    let mut total: u32 = 0;
    for (i, digit) in nums.iter().enumerate() {
        if *digit == nums[(i + 1) % nums.len()] {
            total += *digit as u32;
        }
    }
    println!("Total sum = {}", total);
}