const API_ENDPOINT = "https://www.themealdb.com/api/json/v1/1/";

const form = document.getElementById("form");
const contentContainer = document.getElementById("content");
const previewContainer = document.getElementById("preview");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const query = e.target.querySelector("input").value;
  previewContainer.innerHTML = "";
  if (!query) return;

  e.target.querySelector("button").innerHTML = "...";

  fetch(`${API_ENDPOINT}search.php?s=${query}`)
    .then((data) => data.json())
    .then((data) => {
      const meals = data.meals;
      if (meals) {
        contentContainer.innerHTML = meals
          .map(
            (each) =>
              `<div onclick="lookUp(${each.idMeal})" class="card">
                  <img src="${each.strMealThumb}" />
                  <h3>${each.strMeal}</h3>
              </div>`
          )
          .join("");
      } else {
        contentContainer.innerHTML = `<div class="error">No Food Found With This Name</div>`;
      }
    })
    .catch((err) => console.log("error"))
    .finally(() => {
      e.target.querySelector("button").innerHTML = "Search";
    });
});

function lookUp(mealId) {
  previewContainer.innerHTML = `<div class="preview-loading" >Loading...</div>`;

  fetch(`${API_ENDPOINT}lookup.php?i=${mealId}`)
    .then((data) => data.json())
    .then((data) => {
      const meals = data.meals;
      if (meals.length > 0) {
        const meal = meals[0];
        previewContainer.innerHTML = `
         <div>
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
            </div>
        </div>
        `;
      }
    })
    .catch(() => {
      previewContainer.innerHTML = "";
    });
}
