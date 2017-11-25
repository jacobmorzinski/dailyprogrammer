// # Read line from stdin
// # if no line, done
// # if line
// ## find recurring in line
// ## print answer

use std::io;
use std::collections::HashMap;

fn find_first_recurring_character(line: &String) -> Option<char> {
    let chars: Vec<char> = line.chars().collect();
    let mut seen: HashMap<char, u16> = HashMap::new();
    for c in chars {
        let how_many = match seen.get(&c) {
            Some(n) => n.clone(),
            None => 0,
        };
        if how_many == 1 {
            return Some(c)
        }
        seen.insert(c, how_many + 1);
    }
    return None
}

fn get_line_of_stdin() -> io::Result<String> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    Ok(buffer)
}

fn main() {
    let line = get_line_of_stdin().unwrap();
    if line != "" {
        let eol: &[_] = &['\r', '\n'];
        let line2 = line.trim_right_matches(eol).to_owned();
        println!("input: {:?}", &line2);
        if let Some(answer) = find_first_recurring_character(&line2) {
            println!("answer: {:?}", answer)
        }
    }
}

