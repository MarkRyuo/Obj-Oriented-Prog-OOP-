// class 


let _list = { // object list 
    fname : "Jhon Mark",
    lname : "Malupa",
    age : 21
    
}

// console.log(typeof(_list))

class Person {

    constructor(fname, lname, age){
        this.fname = fname ;
        this.lname = lname ;
        this.age = age ;
    }

    talk() {
        console.log(`Im ${this.fname} ${this.lname}, my age is ${this.age}`)
    }
}

let _person = new Person(_list["fname"], _list["lname"], _list["age"])
console.log(_person.talk())

