use std::fs::File;
use std::io::Read;
static PATH: &str = "day2.txt";


pub fn solve_q1() -> i32{
    let mut file = File::open(PATH).expect("Can't open file.");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Cannot read file.");

    let mut split = contents.split("\n");
    let vec_of_string: Vec<&str> = split.collect();
    let mut sum:i32 = 0;
    for string in vec_of_string{
        match string {
            "A X" => sum +=1 + 3,
            "A Y" => sum +=2 + 6,
            "A Z" => sum +=3 + 0,
            "B X" => sum +=1 + 0,
            "B Y" => sum +=2 + 3,
            "B Z" => sum +=3 + 6,
            "C X" => sum +=1 + 6,
            "C Y" => sum +=2 + 0,
            "C Z" => sum +=3 + 3,
            _ => {}
        }
    }
    return sum;
}
pub fn solver_q2() -> i32{
    let mut file = File::open(PATH).expect("Can't open file.");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Cannot read file.");

    let mut split = contents.split("\n");
    let vec_of_string: Vec<&str> = split.collect();
    let mut sum:i32 = 0;
    for string in vec_of_string{
        match string {
            "A X" => sum +=0 + 3,
            "A Y" => sum +=3 + 1,
            "A Z" => sum +=6 + 2,
            "B X" => sum +=0 + 1,
            "B Y" => sum +=3 + 2,
            "B Z" => sum +=6 + 3,
            "C X" => sum +=0 + 2,
            "C Y" => sum +=3 + 3,
            "C Z" => sum +=6 + 1,
            _ => {}
        }
    }
    return sum;
}

