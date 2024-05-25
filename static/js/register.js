const phonefield = document.querySelector("#phonefield");
const feedBackArea = document.querySelector('.invalid_feedback')
phonefield.addEventListener('keyup', (e) => {
    const PhoneVal = e.target.value;

    phonefield.classList.remove("is-invalid");
    feedBackArea.style.display="none";

    if (PhoneVal.length > 0) {
        fetch("/validate-phonenumber", {
            body: JSON.stringify({phone: PhoneVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.PhoneError){
                phonefield.classList.add("is-invalid");
                feedBackArea.style.display="block";
                feedBackArea.innerHTML=`<p>${data.PhoneError}</p>`
            }
        });
    }
});