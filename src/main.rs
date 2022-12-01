use std::fs::File;
use std::io::prelude::*;

fn main() {
    let mut file = File::open("day1.txt").expect("Can't open file.");

    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Cannot read file.");

    let mut split = contents.split("\n\n");
    let vec_of_string: Vec<&str> = split.collect();
    let mut vec_of_sums = Vec::new();
    let mut first_largest:i32 = 0;
    let mut second_largest:i32 = 0;
    let mut third_largest:i32 = 0;
    for elf in &vec_of_string {
        let mut split = elf.split("\n");
        let vec: Vec<&str> = split.collect();
        let mut sum = 0;
        for numbers in vec{
            let my_int = numbers.parse::<i32>().unwrap();
            sum += my_int;
        }
        if(first_largest < sum){
            second_largest = first_largest;
            first_largest = sum;
        }else if(second_largest < sum && second_largest < first_largest){
            third_largest = second_largest;
            second_largest = sum;
        }else if(third_largest < sum && third_largest < second_largest){
            third_largest = sum;
        }
        vec_of_sums.push(sum);
    }
    let mut sum_of_kings:i32 = first_largest + second_largest + third_largest;
    println!("{}",sum_of_kings)
}
