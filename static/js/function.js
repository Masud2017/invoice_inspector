/*
   Author : Md.Masud karim
   Email : msmasud578@gmail.com
   Description : This script is a collection of functions that the website is using for perform some interactive features
*/

"use strict"; // using the sring mode of the javascript
// Javascript script for create some interactive features

var count = 1;

function addInput() {
   let input = document.createElement("input");
   let counterInput = document.createElement("input");
   let textProduct = document.createTextNode("Enter the product#"+count.toString()+":");
   let textPrice = document.createTextNode("Enter the price#"+count.toString()+":");
   let product = document.createElement("input");
   let container = document.getElementById("container"); // Container for placing the input stuff;
   let sendContainer = document.getElementById("sendCounter");

   input.type = "text";
   input.name = "product" + count.toString();
   input.placeholder = "Enter the product name"
   input.classList.add("form-control");

   product.type = "text";
   product.name = "price" + count.toString();
   product.classList.add("form-control");
   product.placeholder = "Enter the product price";

   //counterInput.name = "counterInput";
   //counterInput.value = count;
   //sendContainer.replaceChild(counterInput);
   if (count <= 9) {
      container.appendChild(textProduct); // Pouring the text into the div
      container.appendChild(input);
      container.appendChild(textPrice);
      container.appendChild(product);
      count++;
   } else {
      document.getElementById("error").innerHTML = "You can't add data more than 10";
   }
   
   console.log("Counter value is  : ",count.toString());

}
