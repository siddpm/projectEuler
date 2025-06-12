mod problems;

fn main() {
    println!("Hello, world!");
    problems::problem1::solve();

    let sum = problems::helpers::series_sum(10);
    println!("Helper sum {}",sum)
}
