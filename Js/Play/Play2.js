// Create Class 

class item {

    constructor(barcode_number, product_name, quantity){
        this.barcode_number = barcode_number ;
        this.product_name = product_name ;
        this.quantity = quantity ;
    }

    code(){
        console.log(`{this.barcode}`) ;

    }
}
// Open and display the input in div
const btn_open = () => {
    document.getElementById("con_").innerHTML = `
    <input type="text" placeholder="Barcode Number" id="_bar> <br> ` ; 
    document.getElementById("con_").innerHTML = `<input type="text" placeholder="ProductName" id="_product"> <br>`
}

