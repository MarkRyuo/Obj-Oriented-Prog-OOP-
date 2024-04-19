
class Person {

    constructor(fname, lname, age){
        this.fname = fname ;
        this.lname = lname ;
        this.age = age ;
    }

    introduction(){
        console.log(`Konichiwa ${this.fname} ${this.lname} desu!`) ;
    }
}

const Student_1 = new Person("Ryuo", "Malupa", 21) ;
Student_1.introduction() ;
