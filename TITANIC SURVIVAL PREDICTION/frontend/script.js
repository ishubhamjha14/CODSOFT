// AOS
AOS.init({

    duration: 1400
});

// PARTICLES
particlesJS("particles-js", {

    particles: {

        number: {

            value: 75
        },

        color: {

            value: "#ffffff"
        },

        shape: {

            type: "circle"
        },

        opacity: {

            value: 0.35
        },

        size: {

            value: 3
        },

        move: {

            enable: true,

            speed: 2
        },

        line_linked: {

            enable: true,

            distance: 140,

            color: "#ffffff",

            opacity: 0.15,

            width: 1
        }
    }
});

// PREDICT FUNCTION
async function predict() {

    let resultBox = document.getElementById("result-box");

    resultBox.innerHTML = "⏳ AI analyzing passenger data...";

    let data = {

        pclass: parseInt(document.getElementById("pclass").value),

        sex: parseInt(document.getElementById("sex").value),

        age: parseInt(document.getElementById("age").value),

        sibsp: 0,

        parch: 0,

        fare: parseFloat(document.getElementById("fare").value),

        embarked: 2
    };

    try {

        let response = await fetch("http://127.0.0.1:5000/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });

        let result = await response.json();

        if(result.result === 1){

            resultBox.innerHTML =
            `🟢 Survival Probability: ${(result.probability * 100).toFixed(2)}%`;

            resultBox.style.color = "#00ff99";

        } else {

            resultBox.innerHTML =
            `🔴 Survival Probability: ${(result.probability * 100).toFixed(2)}%`;

            resultBox.style.color = "#ff4b4b";
        }

    } catch(error){

        resultBox.innerHTML = "❌ Backend connection failed";

        resultBox.style.color = "red";
    }
}