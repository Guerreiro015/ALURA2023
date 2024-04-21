const item = document.querySelectorAll(".item");
const btn = document.querySelectorAll(".item .btn");

for (let index = 0; index < item.length; index++) {
    item[index].addEventListener("mouseover", () => {
        btn[index].style.top = "-45px"
    });

    item[index].addEventListener("mouseout", () => {
        btn[index].style.top = "0"
    });
}