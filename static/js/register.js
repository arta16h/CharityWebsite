const phonefield = document.querySelector("#phonefield");
const feedBackArea = document.querySelector(".invalid_feedback");
const PhoneSuccessOutput = document.querySelector(".PhoneSuccessOutput");
const ShowPasswordToggle = document.querySelector(".ShowPasswordToggle");
const PasswordField = document.querySelector(".PasswordField");

const handleToggleInput = (e) => {
    if (ShowPasswordToggle.textContent === "نمایش") {
        ShowPasswordToggle.textContent = "پنهان";
    } else {
        ShowPasswordToggle.textContent = "نمایش";
    }
};
ShowPasswordToggle.addEventListener("click", handleToggleInput);

phonefield.addEventListener('keyup', (e) => {
    const PhoneVal = e.target.value;
    PhoneSuccessOutput.style.display = "block";
    PhoneSuccessOutput.textContent = 'در حال بررسی'

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
            PhoneSuccessOutput.style.display = "none";
            if (data.PhoneError){
                phonefield.classList.add("is-invalid");
                feedBackArea.style.display="block";
                feedBackArea.innerHTML=`<p>${data.PhoneError}</p>`
            }
        });
    }
});