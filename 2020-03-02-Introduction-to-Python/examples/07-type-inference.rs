// For example, the Rust programming language is statically typed, but uses
// type inference to reduce the amount of types that have to be specified by
// the programmer.
//
// $ rustc 07-type-inference.rs

fn main() {
    let x = 1;
    let x = "Hello Joe".to_owned();

    // The following line results in a compilation error (types are checked
    // during compilation because Rust is statically typed):
    //
    // error: mismatched types (expected &str, found integer)
    println!("{}", x + 2);
}
