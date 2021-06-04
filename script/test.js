var f = n => {
    while(true){
        n += 1;

        console.log(n, new Date())

        if(n > 100) break;
    }
}

let t = null;
var c = (n, nt) => {
    t = setInterval(() => {
        n += 1;
        console.log(n, new Date())

        if(n == 50){
            clearInterval(t)
            t = null

            c(n, 5000)
        }

        if(n == 51){
            clearInterval(t)
            t = null

            c(n)
        }

        if(n > 100) {
            clearInterval(t)
            t = null
        }; 
    }, nt || 0)
}

c(1)