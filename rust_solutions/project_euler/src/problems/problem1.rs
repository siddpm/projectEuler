pub fn solve() {
    let mut sum:i32 = 0;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }
    println!("Total sum of multiple of 3 or 5 is: {}", sum)
}