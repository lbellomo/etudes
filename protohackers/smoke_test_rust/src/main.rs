use std::io::{prelude::*, BufReader};
use std::net::{TcpListener, TcpStream};

fn main() {
    let listener = TcpListener::bind("0.0.0.0:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buf: Vec<u8> = Vec::new();
    let mut buf_reader = BufReader::new(&mut stream);
    buf_reader.read_to_end(&mut buf).unwrap();
        
    // print incoming data for debug
    let buf_str = std::str::from_utf8(&buf).unwrap_or("invalid buf");
    println!("{:#?}", &buf_str);

    stream.write_all(&buf).unwrap();
    
}
