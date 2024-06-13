const phonefield = document.querySelector("#phonefield");
const feedBackArea = document.querySelector(".invalid_feedback");
const PhoneSuccessOutput = document.querySelector(".PhoneSuccessOutput");
const ShowPasswordToggle = document.querySelector(".ShowPasswordToggle");
const PasswordField = document.querySelector("#PasswordField");
const SubmitBtn = document.querySelector(".submit_btn");

const handleToggleInput = (e) => {
    if (ShowPasswordToggle.innerHTML === `<i class="fas fa-eye"></i>`) {
        ShowPasswordToggle.innerHTML = `<i class="fas fa-eye-slash"></i>`;
        PasswordField.setAttribute("type", "text");
    } else {
        ShowPasswordToggle.innerHTML = `<i class="fas fa-eye"></i>`;
        PasswordField.setAttribute("type", "password");
    }
};
// ShowPasswordToggle.addEventListener("click", handleToggleInput);

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
                SubmitBtn.setAttribute("disabled", "disabled");
                phonefield.classList.add("is-invalid");
                feedBackArea.style.display="block";
                feedBackArea.innerHTML=`<p>${data.PhoneError}</p>`
            } else {
                SubmitBtn.removeAttribute("disabled");
            }
        });
    }
});