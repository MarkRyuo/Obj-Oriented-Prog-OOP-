// class 


let _list = { // object list 
    fname : "Jhon Mark",
    lname : "Malupa",
    age : 21
    
}

// console.log(typeof(_list))

class Person {

    constructor(_list["fname"], lname, age){
        this.fname = _list["fname"] ;
        this.lname = lname ;
        this.age = age ;
    }
}