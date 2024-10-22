const API_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/";

const form = document.getElementById("form");
const mealContainer = document.getElementById("meals");
const modalCross = document.getElementById("cross");
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modal-content");
const selectedMeal = document.getElementById("selected-meal");
const itemCount = document.getElementById("item-count");

const cartDB = new Map();

addEventListener("DOMContentLoaded", () => {
  fetch(`${API_ENDPOINT}search.php?s=`)
    .then((data) => data.json())
    .then((data) => {
      const meals = data.meals;

      if (!meals) return;

      mealContainer.innerHTML = meals.map((meal) => mealEl(meal)).join("");
    })
    .catch((err) => console.log(err));

  console.log(mealContainer);
});

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const query = e.target.querySelector("input").value;

  if (!query) return;

  e.target.querySelector("button").innerHTML = "...";

  fetch(`${API_ENDPOINT}search.php?s=${query}`)
    .then((data) => data.json())
    .then((data) => {
      const meals = data.meals;
      if (meals) {
        mealContainer.innerHTML = meals.map((each) => mealEl(each)).join("");
      } else {
        mealContainer.innerHTML = `<div class="error">No Food Found With This Name</div>`;
      }
    })
    .catch((err) => console.log("error", err))
    .finally(() => {
      e.target.querySelector("button").innerHTML = "Search";
    });
});

function closeModal() {
  modal.classList.remove("show");
}

function lookUp(mealId) {
  modal.classList.add("show");

  modalContent.innerHTML = `<div class="loading" >Loading...</div>`;

  fetch(`${API_ENDPOINT}lookup.php?i=${mealId}`)
    .then((data) => data.json())
    .then((data) => {
      const meals = data.meals;
      if (meals.length > 0) {
        const meal = meals[0];
        modalContent.innerHTML = `
           <div>
           <span id="cross" onclick="closeModal()" class="cross">&#x2715;</span>
              <img src="${meal.strMealThumb}" />
              <div>
              <h3>Name: ${meal.strMeal}</h3>
              <p>From: ${meal.strArea}</p>
              <h4>Ingredient: </h4>
              <ul>
                  <li>${meal.strIngredient1}</li>
                  <li>${meal.strIngredient2}</li>
                  <li>${meal.strIngredient3}</li>
                  <li>${meal.strIngredient4}</li>
                  <li>${meal.strIngredient5}</li>
              </ul>
              <h4>Instruction: </h4>
              <p>${meal.strInstructions.slice(0, 250)} </p>
              </div>
          </div>
          `;
      }
    })
    .catch(() => {
      previewContainer.innerHTML = "";
    });
}

function mealEl(meal) {
  return `<div  class="card">
            <img src="${meal.strMealThumb}" />
            <h3>${meal.strMeal}</h3>
            <p>Origin: ${meal.strArea}</p>

            <button onclick="addToDB('${meal.idMeal}','${meal.strMeal}','${
    meal.strMealThumb
  }',this)" class="add-cart">
             ${cartDB.has(meal.idMeal) ? "Added" : "Add To Cart"}
            </button>
            <button onclick="lookUp(${meal.idMeal})" class="details" >
              Details
            </button>
          </div>`;
}
function addToDB(mealId, mealName, mealImg, el) {
  if (cartDB.size >= 11) {
    return alert("You Can't Add More Then 11 Food item");
  }

  el.innerHTML = "Added";
  cartDB.set(mealId, { mealId, mealName, mealImg });
  renderCart();
}

function removeFromCart(id) {
  if (cartDB.has(id)) {
    cartDB.delete(id);
    renderCart();
  }
}

function renderCart() {
  itemCount.innerHTML = "Cart <small>(" + cartDB.size + ")</small>";
  selectedMeal.innerHTML = [...cartDB.values()]
    .map(
      (item) => `<div>
            <img src="${item.mealImg}" alt="">
            <h3>${item.mealName}</h3>
            <span class="delete" onclick="removeFromCart('${item.mealId}')" >&#x2715;</span>
          </div>`
    )
    .join("");
}
