async function predictFlower(){

const sepal_length =
document.getElementById(
"sepal_length"
).value;

const sepal_width =
document.getElementById(
"sepal_width"
).value;

const petal_length =
document.getElementById(
"petal_length"
).value;

const petal_width =
document.getElementById(
"petal_width"
).value;

const result =
document.getElementById(
"result"
);

const image =
document.getElementById(
"flowerImage"
);

const description =
document.getElementById(
"description"
);

const response =
await fetch(
"http://127.0.0.1:5000/predict",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

sepal_length,
sepal_width,
petal_length,
petal_width

})

}
);

const data =
await response.json();

result.innerHTML =

`
${data.species}
<br>
Confidence:
${data.confidence}%
`;

description.innerHTML =
data.description;

image.style.display =
"block";

if(
data.species ===
"Iris-setosa"
){

image.src =
"images/setosa.jpg";

}

else if(
data.species ===
"Iris-versicolor"
){

image.src =
"images/versicolor.jpg";

}

else{

image.src =
"images/virginica.jpg";

}

}