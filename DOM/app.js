// DOM Document Object Model


// Using ID 

// const element = document.getElementById("intro") ;

// document.getElementById("name").innerHTML = `Konichiwa Ryuo Desu ${element.innerHTML}` ;


// Using Tag Name 
// Tag Name is using index's

const element = document.getElementsByTagName("p") ;

document.getElementById("name").innerHTML = `Hello Ryuo desu! ${element[2].innerHTML}` ;