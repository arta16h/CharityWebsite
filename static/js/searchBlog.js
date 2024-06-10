const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
const paginationContainer = document.querySelector(".pagination-container");
const outPut = document.querySelector(".output");
tableOutput.style.display = "none";

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    if(searchValue.trim().length > 0){
        paginationContainer.style.display = "none";
        outPut.innerHTML = "";
        fetch('/blog/search-blog', {
            body = JSON.stringify({ serachText: searchValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            appTable.style.display = "none";
            tableOutput.style.display = "block";

            if (data.length === 0) {
                tableOutput.innerHTML = "نتیجه ای یافت نشد";
            }else{
                data.forEach((item) => {
                    outPut.innerHTML += `
                        <img src=${item.imageUrl}>
                        <a>${item.author}</a>
                        <h2>${item.title}</h2>
                        <p>${item.content}</p>`;
                });
            }
        });
    }else{
        tableOutput.style.display = 'none';
        appTable.style.display = 'block';
        paginationContainer.style.display = 'block';
    }
});