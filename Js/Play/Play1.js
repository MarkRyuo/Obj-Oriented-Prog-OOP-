
class Person {

    constructor(fname, lname){
        this.fname = fname ;
        this.lname = lname ;
        // this.age = age ;
    }

    introduction(){
        console.log(`Konichiwa ${this.fname} ${this.lname} desu!`) ;
    }

    Age(_age) {
        _age = this.age ;
        return _age ; 
    }
}

const Student_1 = new Person("Ryuo", "Malupa") ;
Student_1.introduction() ;
let helllo = Age(21) ;
console.log(`Age of ${helllo}`)