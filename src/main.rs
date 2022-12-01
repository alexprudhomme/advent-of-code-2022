use std::fs::File;
use std::io::prelude::*;
use crate::day1::Day1;

mod day1;

fn main() {
    let mut day1 = Day1::default();

    println!("{}", day1.solve_q1());
    println!("{}", day1.solve_q2());
}
