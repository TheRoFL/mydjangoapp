const form = document.querySelector("form");
const heightLower = form.querySelector("#height_limit_lower");
const heightUpper = form.querySelector("#height_limit_upper");
const ageLower = form.querySelector("#age_limit_lower");
const ageUpper = form.querySelector("#age_limit_upper");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const heightLowerValue = parseInt(heightLower.value);
  const heightUpperValue = parseInt(heightUpper.value);
  const ageLowerValue = parseInt(ageLower.value);
  const ageUpperValue = parseInt(ageUpper.value);

  if (
    !heightLowerValue ||
    !heightUpperValue ||
    !ageLowerValue ||
    !ageUpperValue
  ) {
    alert("Пожалуйста, заполните все поля");
    return;
  }

  if (
    heightLowerValue < 140 ||
    heightLowerValue > 220 ||
    heightUpperValue < 140 ||
    heightUpperValue > 220
  ) {
    alert("Пожалуйста, введите рост от 140 до 200 см");
    return;
  }

  if (
    ageLowerValue < 18 ||
    ageLowerValue > 100 ||
    ageUpperValue < 18 ||
    ageUpperValue > 100
  ) {
    alert("Пожалуйста, введите возраст от 18 до 100 лет");
    return;
  }

  if (heightLowerValue > heightUpperValue) {
    alert(
      "Пожалуйста, введите корректные значения для минимального и максимального роста"
    );
    return;
  }

  if (ageLowerValue > ageUpperValue) {
    alert(
      "Пожалуйста, введите корректные значения для минимального и максимального возраста"
    );
    return;
  }

  form.submit();
});
