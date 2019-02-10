// Gets container to store Nutrient Info in
const mainContainer = document.getElementById('nutrientInfo');

function createNode(element){
    return document.createElement(element);
}

function append(parent, el){
    return parent.appendChild(el);
}

function createNutrientInfoList(){
    var container = document.createElement('div');
    container.className = ('row');
    container.innerHTML = 'NUTRIENT NAME';
    // Create list of food recommendations
    var list = document.createElement("ul");
    
    list.className = ();
    
    
}

const url = "";
const name = document.getElementById('username');
      
const getPost = () => {
    return fetch(url)
        .then(response => response.json())
        .then(function(data){
        // Parse JSON
            let 
        }
    })
}


function displayNutrition(){
    document.getElementById("nutritionInfo").innerHTML += "test"
}


