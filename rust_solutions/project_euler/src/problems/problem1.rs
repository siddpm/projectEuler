pub fn solve_unopt() {
    let mut sum:i32 = 0;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }
    println!("Total sum of multiple of 3 or 5 is: {}", sum)
}

pub fn solve() {
    /*
    We will optimise the above solution by using:
    1. Noticing multiples of 5 and 3 can be written as follows: 5 *(1 + 2 + 3 + 4..199)
    2. Sum of series 1 + 2 + 3 + 4.. = n*(n+1)/2
     */

    let sum_multiple_3 = 3*(333 * 334)/2;
    let sum_multiple_5 = 5*(199 * 200)/2;

    // We don't want to double count numbers which are multiples of 3 and 5
    // lcm(3,5) = 15
    let sum_multiple_15 = 15*(66 * 67)/2;

    println!("Sum of multiple of 3 are: {}",sum_multiple_3 + sum_multiple_5 - sum_multiple_15)
}