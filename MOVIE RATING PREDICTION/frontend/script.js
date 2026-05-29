async function predictRating(){

    const genre =
    document.getElementById("genre").value;

    const director =
    document.getElementById("director").value;

    const actor =
    document.getElementById("actor").value;

    const duration =
    document.getElementById("duration").value;

    const result =
    document.getElementById("result");

    const loader =
    document.getElementById("loader");

    result.innerHTML = "";

    loader.style.display = "block";

    try{

        const response =
        await fetch(
            "http://127.0.0.1:5000/predict",
            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    genre:genre,
                    director:director,
                    actor:actor,
                    duration:duration
                })
            }
        );

        const data =
        await response.json();

        loader.style.display = "none";

        if(data.error){

            result.innerHTML =
            `❌ ${data.error}`;

        }else{

            result.innerHTML =
            `⭐ ${data.rating}/10`;
        }

    }catch(error){

        loader.style.display = "none";

        result.innerHTML =
        "❌ Backend connection failed";
    }
}