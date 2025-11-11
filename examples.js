const second1 = document.getElementsByTagName('li')[1];  // getElementsByTagname returns an array. The indexes in an array start at zero, so 1 means the second <li> element.
const second2 = document.querySelectorAll('li')[1];      // the same with querySelectorAll-function


console.log("second1", second1)
console.log("second2", second2)

const bullets = document.querySelectorAll("li")


   for (let bullet of bullets) {
       bullet.innerHTML = `<b>hello</b>`;
   }
