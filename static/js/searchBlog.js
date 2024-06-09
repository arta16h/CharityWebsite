const searchField = document.querySelector("#searchField");

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;
    if(searchValue.trim().length > 0){
        fetch('/blog/search-blog', {
            body = JSON.stringify({ serachText: searchValue}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data)
        });
    }
});