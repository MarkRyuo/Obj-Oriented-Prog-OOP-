// DOM Document Object Model


// Using ID 

// const element = document.getElementById("intro") ;

// document.getElementById("name").innerHTML = `Konichiwa Ryuo Desu ${element.innerHTML}` ;


// Using Tag Name 
// Tag Name is using index's

// const element = document.getElementsByTagName("p") ;

// document.getElementById("name").innerHTML = `Hello Ryuo desu! ${element[2].innerHTML}` ;


// Usong ClassName 

const element = document.getElementsByClassName("intro") ; 

document.getElementById("demo").innerHTML = `Hello Mark ${element[1].innerHTML}` ;


// style.property
document.getElementById("intro").style.color = "red" ;

// Events 
const trytext = (id) => {
    id.innerHTML = "Halooooooo"
    id.style.color = "blue"
}