"use strict";

const BASE_URL = "http://127.0.0.1:5001";
const $cupcakesSection = $("#cupcakes-section");
const $cupcakesList = $("#cupcakes-list");
const $cupcakesForm = $("#cupcakes-form");
const $addCupcakeButton = $("#add-cupcake-button");

/**
 * Function creates new cupcake, POSTS it to the API,
 * and then puts it on the page.
 */
async function postNewCupcake() {
  console.debug("postNewCupcake() invoked");

  const response = await axios({
    url: `${BASE_URL}/api/cupcakes`,
    method: "POST"
  })
}

/**
 * Function queries the API and gets all cupcakes in the database,
 * and then returns it as a array of objects.
 */
async function getCupcakes() {
  console.debug("getCupcakes() invoked");
  console.debug("url is", `${BASE_URL}/api/cupcakes`);

  // axios call
  const response = await axios({
    url: `${BASE_URL}/api/cupcakes`,
    method: "GET",
  });

  const cupcakes = response.data.cupcakes;
  return cupcakes;
}

/**
 * Function loads the page on start, get all the cupcakes from the API,
 * and then displays it on the page.
 */
async function start() {
  console.debug("start() invoked");
  const cupcakes = await getCupcakes();
  console.debug("cupcakes is", cupcakes);
  for (let cupcake of cupcakes) {
    putCupcakeOnPage(cupcake);
  }
}

/**
 * Function accepts one cupcake-data object, and put its on the list in the DOM.
 */
function putCupcakeOnPage(cupcakeObj) {
  console.debug("putCupcakeOnPage() invoked");
  const $newListItem = $(`
  <li>
    <img src="${cupcakeObj.image}">
    <p>
    ${cupcakeObj.flavor} flavor available in ${cupcakeObj.size} with a rating of ${cupcakeObj.rating}
    </p>
  </li>
  `);
  $cupcakesList.append($newListItem);
}

async function handleSubmit() {
  const flavor = $("#submit-flavor").val();
  const size = $("#submit-size").val();
  const rating = $("#submit-rating").val();
  const image = $("#submit-imageUrl").val();

  const cupcakeObj = { flavor, size, rating, image };

  const response = await axios({
    url: `${BASE_URL}/api/cupcakes`,
    method: "POST",
    data: {
      "flavor": flavor,
      "size": size,
      "rating": rating,
      "image": image
    }
  });

  putCupcakeOnPage(cupcakeObj);
}


function onFormSubmit(evt) {
  evt.preventDefault();
  handleSubmit();
}

$cupcakesForm.on("submit", onFormSubmit)

start();
