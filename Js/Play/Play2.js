// Create Class

class item {

    constructor(barcode_number, product_name, quantity){
        this.barcode_number = barcode_number ;
        this.product_name = product_name ;
        this.quantity = quantity ;
    }

    code(){

    }
}
const btn_open = () => {
    document.getElementById("con_").innerHTML = `<input type="text"> <br>` ; 
}

const btn_close = () => {
    document.getElementById("con_").innerHTML ;
}