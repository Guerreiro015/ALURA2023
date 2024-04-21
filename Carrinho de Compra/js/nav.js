const closeIcon = document.querySelector(".close-icon");
const openIcon = document.querySelector(".open-icon");
const body = document.querySelector("body");
const headerMobile = document.querySelector(".header-mobile");

closeIcon.addEventListener("click", () => {
    headerMobile.style.display = "none";
    body.style.overflow = "scroll";
});

openIcon.addEventListener("click", () => {
    headerMobile.style.display = "flex";
    body.style.overflow = "hidden";
});