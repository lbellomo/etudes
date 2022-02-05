use md5::{Digest, Md5};

fn find_aws(n: usize, secret_key: &[u8; 8]) -> u32 {
    let mut i = 0_u32;
    let zeros = "0".repeat(n);
    let mut hasher = Md5::new();

    loop {
        hasher.update(secret_key);
        hasher.update(i.to_string());
        let hash: String = format!("{:X}", hasher.finalize_reset());

        i += 1;
        if &hash[..n] == zeros {
            println!("End loop, the result hash is: {}", hash);
            break;
        }
    }
    i
}

fn main() {
    let secret_key = b"iwrupvqb";

    println!("sol a: {}", find_aws(5, secret_key));
    println!("sol b: {}", find_aws(6, secret_key));
}
