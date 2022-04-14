# ZeroMQ

ZeroMQ (also known as ØMQ, 0MQ, or zmq) looks like an embeddable networking library 
but acts like a concurrency framework. It gives you sockets that carry atomic messages 
across various transports like in-process, inter-process, TCP, and multicast. 

You can connect sockets N-to-N with patterns like fan-out, pub-sub, task distribution, 
and request-reply. It's fast enough to be the fabric for clustered products. 
Its asynchronous I/O model gives you scalable multicore applications, built as 
asynchronous message-processing tasks. 

It has a score of language APIs (C, C++, C#, Rust, Go, Python, Node.js, Lua, Erlang, 
Julia, Haskell, Java, Scala, Racket, etc.) and runs on most operating systems. If you are
familiar with Java Spring Framework, you will see it reminds of both ActiveMQ and RabbitMQ, 
but it is more compact and light-weight. 
