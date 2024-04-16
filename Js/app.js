// OOP (OBJECT ORIENTED PROGRAMMING)

class Character {

    constructor(name, power, speed){
        this.name = name
        this.power = power
        this.speed = speed 
    }

    introduction() {
        console.log(`Konichiwa ${this.name} desu`)
    }
}

charOne = Character("Nicole", "Moon Blade", "High diff")
charOne = Character.introduction()