const staticImage =
  "https://web.poecdn.com/protected/image/promo/allflame/panels/Panel1.webp?key=_LPj3iJu9EnVZHu8RV1ETw";
const gifImage = "screenscast.webp";

const preloadGif = new Image();
preloadGif.src = gifImage;

const previewImg = document.getElementById("preview-img");

previewImg.addEventListener("mouseenter", function () {
  previewImg.src = gifImage;
});

previewImg.addEventListener("mouseleave", function () {
  previewImg.src = staticImage;
});

const themeBtn = document.getElementById("theme-btn");

themeBtn.addEventListener("click", function () {
  document.body.classList.toggle("light-theme");
});

let count = 0;
const counterValue = document.getElementById("counter-value");
const countBtn = document.getElementById("count-btn");
const resetBtn = document.getElementById("reset-btn");

countBtn.addEventListener("click", function () {
  count++;
  counterValue.textContent = count;
});

resetBtn.addEventListener("click", function () {
  count = 0;
  counterValue.textContent = count;
});
